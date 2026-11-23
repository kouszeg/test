# Builds branje/index.json from branje/*.md front matter. Order: newest date first, then file order in ORDER.
import json, re, glob, os, sys
D=os.path.join(os.path.dirname(__file__),'..','branje')
items=[]
for f in sorted(glob.glob(os.path.join(D,'*.md'))):
    s=open(f,encoding='utf-8').read(); m=re.match(r'^---\n(.*?)\n---\n',s,re.S); fm=dict(l.split(':',1) for l in m.group(1).split('\n'))
    fm={k.strip():v.strip() for k,v in fm.items()}; body=s[m.end():]
    text=re.sub(r'```svg[\s\S]*?```','',body); text=re.sub(r'\[([^\]]*)\]\([^)]*\)',r'\1',text)
    words=len(re.findall(r'\w+',text)); sid=os.path.basename(f)[:-3]
    items.append({'id':sid,'title':fm['title'],'sub':fm.get('subtitle',''),'area':fm['area'],'date':fm['date'],'words':words,'min':max(1,round(words/160))})
order=sys.argv[1:]  # optional explicit order of ids within the same date
items.sort(key=lambda x:(x['date'],-order.index(x['id']) if x['id'] in order else 0),reverse=True)
json.dump(items,open(os.path.join(D,'index.json'),'w',encoding='utf-8'),ensure_ascii=False,indent=1)
for i in items: print(i['date'],i['min'],'min',i['words'],'w',i['title'])
