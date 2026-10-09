// Bump V whenever index.html changes, or phones keep the old copy.
const V='liftlog-v16';
const FILES=['./','./index.html','./manifest.webmanifest','./icon-180.png','./icon-512.png'];
self.addEventListener('install',e=>e.waitUntil(caches.open(V).then(c=>c.addAll(FILES)).then(()=>self.skipWaiting())));
self.addEventListener('activate',e=>e.waitUntil(caches.keys().then(ks=>Promise.all(ks.filter(k=>k!==V).map(k=>caches.delete(k)))).then(()=>self.clients.claim())));
// Serve the cached copy, refresh the cache from the network. waitUntil keeps iOS from killing the
// worker before the fresh copy is stored.
self.addEventListener('fetch',e=>{
  if(e.request.method!=='GET')return;
  const net=fetch(e.request);
  const saved=net.then(res=>{if(!res.ok)return;const copy=res.clone();return caches.open(V).then(c=>c.put(e.request,copy))}).catch(()=>{});
  e.respondWith(caches.match(e.request).then(hit=>hit||net));
  e.waitUntil(saved);
});
