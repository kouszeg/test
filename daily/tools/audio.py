# Narrates Branje stories with Gemini TTS (free tier) -> Opus 24 kbit/s files uploaded as assets of the GitHub release
# 'audio' (outside git history, no size cap) + daily/branje/audio/index.json (in the repo).
# Runs in GitHub Actions (secret GEMINI_KEY). Free-tier quota is per model (~10 requests/day each), so the
# script walks a list of TTS models and moves on when one answers 429. Unfinished stories keep their finished
# parts (release assets part_*) and continue on the next run. The workflow uploads/deletes what _release.json lists.
#   python3 tools/audio.py                      -> stories without audio (newest first)
#   python3 tools/audio.py samples V1,V2,...    -> short voice samples to daily/tts-test/
#   python3 tools/audio.py story ID[,ID]        -> only these stories
import base64, hashlib, io, json, os, re, subprocess, sys, time, urllib.error, urllib.request, wave

ROOT = os.path.join(os.path.dirname(__file__), '..')
BR = os.path.join(ROOT, 'branje')
AD = os.path.join(BR, 'audio')
PD = os.path.join(AD, 'parts')
KEY = os.environ.get('GEMINI_KEY', '')
VOICE = os.environ.get('TTS_VOICE') or 'Algieba'   # chosen by ear (calm, smooth)
STYLE = os.environ.get('TTS_STYLE', 'calm, measured and thoughtful narrator, unhurried, warm and low; like a reflective podcast host')
MODELS = ['gemini-3.8-flash-tts', 'gemini-3.8-flash-lite-tts', 'gemini-3.1-flash-tts-preview', 'gemini-2.5-flash-preview-tts']
CHUNK = 3000          # characters per request (about 3 minutes of speech)
GAP = 21              # seconds between requests (free tier: 3 requests per minute)
dead = set()          # models whose quota is used up (or unavailable) in this run
last = [0.0]


class Quota(Exception):
    pass


def post(url, body):
    req = urllib.request.Request(url, data=json.dumps(body).encode(), headers={'Content-Type': 'application/json', 'x-goog-api-key': KEY})
    return json.load(urllib.request.urlopen(req, timeout=300))


PREBUILT = {'Zephyr', 'Puck', 'Charon', 'Kore', 'Fenrir', 'Leda', 'Orus', 'Aoede', 'Callirrhoe', 'Autonoe', 'Enceladus', 'Iapetus', 'Umbriel', 'Algieba', 'Despina', 'Erinome', 'Algenib', 'Rasalgethi', 'Laomedeia', 'Achernar', 'Alnilam', 'Schedar', 'Gacrux', 'Pulcherrima', 'Achird', 'Zubenelgenubi', 'Vindemiatrix', 'Sadachbia', 'Sadaltager', 'Sulafat'}
_vcache = {}


def voice_id(v):
    """Prebuilt voice name, or a library voice looked up by display name via GET /v1beta/voices (e.g. 'Arlo')."""
    if v in PREBUILT or v.startswith(('voice_', 'voicekey_', 'voices/')):
        return v
    if v in _vcache:
        return _vcache[v]
    tok, seen = '', 0
    for _ in range(40):
        u = 'https://generativelanguage.googleapis.com/v1beta/voices?pageSize=200' + ('&pageToken=' + tok if tok else '')
        try:
            j = json.load(urllib.request.urlopen(urllib.request.Request(u, headers={'x-goog-api-key': KEY}), timeout=60))
        except urllib.error.HTTPError as e:
            print('  voices list failed', e.code, e.read().decode(errors='replace')[:300])
            break
        items = next((x for x in j.values() if isinstance(x, list)), [])
        if not seen and items:
            print('  voice entry example:', json.dumps(items[0])[:400])
        seen += len(items)
        for it in items:
            names = [str(val) for k, val in it.items() if isinstance(val, str) and k.lower() in ('displayname', 'display_name', 'title', 'label', 'name')]
            if any(n.lower() == v.lower() or n.lower().split('/')[-1] == v.lower() for n in names):
                vid = it.get('name') or it.get('id') or it.get('voice')
                print('  voice', v, '->', vid, json.dumps(it)[:300])
                _vcache[v] = vid
                return vid
        tok = j.get('nextPageToken') or j.get('next_page_token')
        if not tok:
            break
    print('  voice', v, 'not found among', seen, 'library voices; using the name as is')
    _vcache[v] = v
    return v


def wav_pcm(b):
    """WAV bytes (or raw 24 kHz s16le) -> raw PCM."""
    if b[:4] == b'RIFF':
        with wave.open(io.BytesIO(b)) as w:
            return w.readframes(w.getnframes())
    return b


def synth_once(model, text):
    wait = GAP - (time.time() - last[0])
    if wait > 0:
        time.sleep(wait)
    last[0] = time.time()
    try:  # Interactions API (documented for the 3.x TTS models)
        j = post('https://generativelanguage.googleapis.com/v1beta/interactions', {
            'model': model,
            'input': [{'type': 'user_input', 'content': [{'type': 'text', 'text': text, 'annotations': [{'type': 'speech_metadata', 'style': STYLE}]}]}],
            'response_format': {'type': 'audio'},
            'generation_config': {'speech_config': [{'voice': voice_id(VOICE)}]}})
        data = [c['data'] for s in j.get('steps', []) if s.get('type') == 'model_output' for c in s.get('content', []) if c.get('type') == 'audio' and c.get('data')]
        if data:
            return b''.join(wav_pcm(base64.b64decode(d)) for d in data)
        raise RuntimeError('no audio in interactions response: ' + json.dumps(j)[:300])
    except urllib.error.HTTPError as e:
        msg = e.read().decode(errors='replace')[:400]
        if e.code == 429:
            raise Quota(model + ' 429 ' + msg)
        if e.code not in (400, 404):
            raise RuntimeError(f'{model} HTTP {e.code} {msg}')
        print('  interactions not accepted for', model, e.code, msg[:160])
    # older models: generateContent with an audio response
    try:
        j = post(f'https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent', {
            'contents': [{'parts': [{'text': f'Read the following text aloud in its own language ({STYLE}):\n\n{text}'}]}],
            'generationConfig': {'responseModalities': ['AUDIO'], 'speechConfig': {'voiceConfig': {'prebuiltVoiceConfig': {'voiceName': VOICE}}}}})
        part = j['candidates'][0]['content']['parts'][0]['inlineData']['data']
        return wav_pcm(base64.b64decode(part))
    except urllib.error.HTTPError as e:
        msg = e.read().decode(errors='replace')[:400]
        if e.code == 429:
            raise Quota(model + ' 429 ' + msg)
        raise RuntimeError(f'{model} generateContent HTTP {e.code} {msg}')


def synth(text):
    """Try the models in order; returns (pcm, model) or raises Quota when every model is used up."""
    for m in MODELS:
        if m in dead:
            continue
        for attempt in range(2):
            try:
                pcm = synth_once(m, text)
                if len(pcm) < 24000:  # less than 0.5 s of audio: treat as a failure
                    raise RuntimeError('audio too short')
                return pcm, m
            except Quota as q:
                print('  quota:', str(q)[:200])
                dead.add(m)
                break
            except Exception as ex:
                print(f'  {m} attempt {attempt + 1} failed:', str(ex)[:300])
                if attempt == 1:
                    dead.add(m)
    raise Quota('all TTS models used up')


OPUS = ['-c:a', 'libopus', '-b:a', '24k', '-application', 'voip']   # speech: ~0.18 MB per minute


def to_audio(pcm, path):
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-f', 's16le', '-ar', '24000', '-ac', '1', '-i', '-', *OPUS, path], input=pcm, check=True)


def mp3_len(path):
    r = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', path], capture_output=True, text=True)
    return round(float(r.stdout.strip() or 0))


def narration(md):
    """Markdown story -> plain text for reading aloud: no figures, links, markup or source lists."""
    md = re.sub(r'^---[\s\S]*?\n---\n', '', md)
    md = re.sub(r'```[\s\S]*?```', '', md)
    out = []
    for b in re.split(r'\n\s*\n', md):
        b = b.strip()
        if not b:
            continue
        m = re.match(r'^(#{1,3})\s+(.*)$', b)
        if m and re.match(r'^(Viri|Za ogled|Sources|References|Watch)\b', m.group(2), re.I):
            break
        if m:
            b = m.group(2).rstrip('.:') + '.'
        b = re.sub(r'!\[[^\]]*\]\([^)]*\)', '', b)
        b = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', b)
        b = re.sub(r'[*_`]+', '', b)
        b = re.sub(r'^>\s?', '', b, flags=re.M)
        b = re.sub(r'^\s*[-+]\s+', '', b, flags=re.M)
        b = re.sub(r'<[^>]+>', '', b)
        b = re.sub(r'\s*\n\s*', ' ', b).strip()
        if b:
            out.append(b)
    return out


def chunks(paras):
    cur, res = '', []
    for p in paras:
        if cur and len(cur) + len(p) > CHUNK:
            res.append(cur)
            cur = ''
        cur = (cur + '\n\n' + p) if cur else p
    if cur:
        res.append(cur)
    return res


def samples(voices):
    s = open(os.path.join(BR, '2026-11-23-tambora.md'), encoding='utf-8').read()
    P = narration(s)
    k = next((i for i, x in enumerate(P) if x.startswith('Aprila 1815')), 2)
    text = '\n\n'.join(P[k:k + 3])[:900]
    os.makedirs(os.path.join(ROOT, 'tts-test'), exist_ok=True)
    global VOICE
    for v in voices:
        VOICE = v
        try:
            pcm, m = synth(text)
        except Quota as q:
            print('STOP', q)
            break
        to_audio(pcm, os.path.join(ROOT, 'tts-test', f'gemini_{v}.ogg'))
        print('sample', v, m, len(pcm) // 48000, 's')


def stories(only=None):
    os.makedirs(PD, exist_ok=True)
    ip = os.path.join(AD, 'index.json')
    idx = json.load(open(ip, encoding='utf-8')) if os.path.exists(ip) else {}
    items = json.load(open(os.path.join(BR, 'index.json'), encoding='utf-8'))
    done = 0
    rel = {'upload': [], 'delete': []}
    for it in items:  # newest first
        sid = it['id']
        if only and sid not in only:
            continue
        paras = narration(open(os.path.join(BR, sid + '.md'), encoding='utf-8').read())
        h = hashlib.sha1(('\n'.join(paras) + VOICE + STYLE).encode()).hexdigest()[:12]
        if idx.get(sid, {}).get('h') == h:
            continue
        parts = chunks(paras)
        print(f'{sid}: {len(parts)} parts')
        models = []
        try:
            for n, t in enumerate(parts):
                pp = os.path.join(PD, f'part_{sid}.{h}.{n}.ogg')
                if os.path.exists(pp):
                    continue
                pcm, m = synth(t)
                models.append(m)
                to_audio(pcm, pp)
                rel['upload'].append(pp)
                print(f'  part {n + 1}/{len(parts)} {m} {len(pcm) // 48000} s')
        except Quota as q:
            print('STOP:', q)
            break
        # all parts ready: join with a short pause, drop the parts
        lst = os.path.join(PD, 'list.txt')
        sil = os.path.join(PD, 'sil.ogg')
        subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-f', 'lavfi', '-i', 'anullsrc=r=24000:cl=mono', '-t', '0.7', *OPUS, sil], check=True)
        with open(lst, 'w') as f:
            for n in range(len(parts)):
                if n:
                    f.write(f"file '{os.path.abspath(sil)}'\n")
                f.write(f"file '{os.path.abspath(os.path.join(PD, f'part_{sid}.{h}.{n}.ogg'))}'\n")
        out = os.path.join(AD, sid + '.ogg')
        subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', lst, *OPUS, out], check=True)
        for f in os.listdir(PD):
            if f.startswith(f'part_{sid}.') or f in ('list.txt', 'sil.ogg'):
                if f.startswith('part_'):
                    rel['delete'].append(f)
                os.remove(os.path.join(PD, f))
        rel['upload'] = [x for x in rel['upload'] if os.path.exists(x)] + [out]
        idx[sid] = {'h': h, 'd': mp3_len(out), 'f': 'ogg', 'v': VOICE, 'm': sorted(set(models))}
        json.dump(idx, open(ip, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        done += 1
        print(f'  -> {out} {idx[sid]["d"]} s')
    # remove audio of stories that no longer exist
    ids = {it['id'] for it in items}
    for sid in [k for k in idx if k not in ids]:
        idx.pop(sid)
        rel['delete'].append(sid + '.ogg')
    json.dump(idx, open(ip, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    rel['upload'] = sorted(set(x for x in rel['upload'] if os.path.exists(x)))
    rel['delete'] = sorted(set(rel['delete']))
    json.dump(rel, open(os.path.join(AD, '_release.json'), 'w'), indent=1)
    print('stories narrated this run:', done, '| models used up:', sorted(dead))


if __name__ == '__main__':
    if not KEY:
        sys.exit('GEMINI_KEY missing')
    if len(sys.argv) > 1 and sys.argv[1] == 'samples':
        samples((sys.argv[2] if len(sys.argv) > 2 else 'Charon').split(','))
    elif len(sys.argv) > 2 and sys.argv[1] == 'story':
        stories(set(sys.argv[2].split(',')))
    else:
        stories()
