# Weekly job (GitHub Actions): read YouTube RSS of selected channels -> daily/lekcije/feed.json
# Keeps earlier entries (union by video id), drops YouTube Shorts, caps the total size.
import json, os, re, urllib.request, urllib.error, xml.etree.ElementTree as ET, datetime
CH=[("Veritasium","UCHnyfMqiRRG1u-2MsSQLbXA"),("Kurzgesagt","UCsXVk37bltHxD1rDPwtNM8Q"),("Nightshift (Kurzgesagt)","UCq8ZAAsI89IoJ-fn1gYpO3g"),
("3Blue1Brown","UCYO_jab_esuFRV4b17AJtAw"),("Vsauce","UC6nSFpj9HTCZ5t-N3Rm3-HA"),("SmarterEveryDay","UC6107grRI4m0o2-emgoDnAA"),("Mark Rober","UCY1kMZp36IQSyNx_9h4mpCg"),
("Tom Scott","UCBa659QWEk1AI4Tg--mrJ2A"),("PBS Space Time","UC7_gcs09iThXybpVgjHZ_7g"),("MinutePhysics","UCUHW94eEFW7hkUMVaZz4eDg"),("CGP Grey","UC2C_jShtL725hvbm1arSV9w"),
("Numberphile","UCoxcjq-8xIDTYp3uz647V5A"),("TED-Ed","UCsooa4yRKGN_zEE8iknghZA"),("Real Engineering","UCR1IuLEqb6UEA_zQ81kwXfg"),("Practical Engineering","UCMOqf8ab-42UUQIdVoKwjlQ"),
("Steve Mould","UCEIwxahdLz7bap-VDs9h35A"),("Wendover Productions","UC9RM-iSvTu1uPJb8X5yp3EQ"),("OverSimplified","UCNIuvl7V8zACPpTmmNIqP2A"),("LEMMiNO","UCRcgy6GzDeccI7dkbbBna3Q"),
("Primer","UCKzJFdi57J53Vr_BkTfN3uQ"),("Crash Course","UCX6b17PVsYBQ0ip5gyeme-Q"),("Sabine Hossenfelder","UC1yNl2E66ZzKApQdRuTQ4tw")]
NS={'a':'http://www.w3.org/2005/Atom','yt':'http://www.youtube.com/xml/schemas/2015'}
OUT=os.path.join(os.path.dirname(__file__),'..','lekcije','feed.json')
UA={'User-Agent':'Mozilla/5.0 (daily-feed)'}
class NoRedir(urllib.request.HTTPRedirectHandler):
    def redirect_request(self,*a,**k): return None
op=urllib.request.build_opener(NoRedir)
def is_short(v):
    try: return op.open(urllib.request.Request('https://www.youtube.com/shorts/'+v,headers=UA),timeout=15).status==200
    except Exception: return False
def iso_sec(d):
    m=re.fullmatch(r'P(?:(\d+)D)?T?(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?',d or '')
    return (int(m.group(1) or 0)*86400+int(m.group(2) or 0)*3600+int(m.group(3) or 0)*60+int(m.group(4) or 0)) if m else None
def lengths(ids):
    # durations via the official YouTube Data API v3 (needs repo secret YT_KEY); without a key durations are skipped
    key=os.environ.get('YT_KEY'); out={}
    if not key: return out
    for i in range(0,len(ids),50):
        u='https://www.googleapis.com/youtube/v3/videos?part=contentDetails&id='+','.join(ids[i:i+50])+'&key='+key
        try:
            for it in json.load(urllib.request.urlopen(u,timeout=20)).get('items',[]): out[it['id']]=iso_sec(it['contentDetails'].get('duration'))
        except Exception as ex: print('API FAIL',ex)
    return out
old={}
try:
    j=json.load(open(OUT,encoding='utf-8')); names=[c['name'] for c in j['channels']]
    for x in j['videos']: old[x['v']]=dict(x,ch=names[x['c']])
except Exception: pass
chans=[]
for name,cid in CH:
    ok=0
    try:
        xml=urllib.request.urlopen(urllib.request.Request('https://www.youtube.com/feeds/videos.xml?channel_id='+cid,headers=UA),timeout=20).read()
        for e in ET.fromstring(xml).findall('a:entry',NS):
            v=e.find('yt:videoId',NS).text; ok+=1
            if v in old: old[v]['t']=e.find('a:title',NS).text; continue
            if is_short(v): continue
            old[v]={'v':v,'t':e.find('a:title',NS).text,'d':e.find('a:published',NS).text[:10],'ch':name}
    except Exception as ex: print('FAIL',name,ex)
    chans.append({'name':name,'id':cid,'ok':ok>0})
vids=sorted(old.values(),key=lambda x:x['d'],reverse=True)[:800]
L=lengths([x['v'] for x in vids if not x.get('l')])
for x in vids:
    if not x.get('l') and L.get(x['v']): x['l']=L[x['v']]
print('no duration:',sum(1 for x in vids if not x.get('l')),'(set repo secret YT_KEY for durations)' if not os.environ.get('YT_KEY') else '')
idx={c['name']:i for i,c in enumerate(chans)}
vids=[dict({'v':x['v'],'t':x['t'],'d':x['d'],'c':idx[x['ch']]},**({'l':x['l']} if x.get('l') else {})) for x in vids if x['ch'] in idx]
os.makedirs(os.path.dirname(OUT),exist_ok=True)
json.dump({'updated':datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%MZ'),'channels':chans,'videos':vids},open(OUT,'w',encoding='utf-8'),ensure_ascii=False,separators=(',',':'))
print(len(vids),'videos;',sum(c['ok'] for c in chans),'/',len(chans),'channels ok')
