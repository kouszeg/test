// Network-first, revalidated (cache:'no-cache'): always tries the latest version from GitHub Pages; cache is only an offline fallback.
// Only same-origin GETs are handled (GitHub API calls pass through untouched).
// Only daily-*/pomocnik-* caches are ever deleted: other apps on kouszeg.github.io share this origin's Cache Storage.
const C='daily-v4.28',FILES=['./','index.html','manifest.webmanifest','icon-192.png','icon-512.png'];
self.addEventListener('install',e=>{e.waitUntil(caches.open(C).then(c=>c.addAll(FILES)));self.skipWaiting();});
self.addEventListener('activate',e=>e.waitUntil(caches.keys().then(ks=>Promise.all(ks.filter(k=>(k.startsWith('daily-')||k.startsWith('pomocnik-'))&&k!==C).map(k=>caches.delete(k)))).then(()=>self.clients.claim())));
self.addEventListener('fetch',e=>{
  const u=new URL(e.request.url);
  if(e.request.method!=='GET'||u.origin!==location.origin||u.pathname.endsWith('.mp3')) return; // audio streams straight from the network (range requests, no caching)
  e.respondWith(fetch(e.request,{cache:'no-cache'}).then(r=>{if(r.ok&&!u.search){const cp=r.clone();caches.open(C).then(c=>c.put(e.request,cp));}return r;})
    .catch(()=>caches.match(e.request,{ignoreSearch:true}).then(m=>m||caches.match('./'))));
});
