// 離線快取：網站外殼先用快取；資料（JSON）先上網、失敗再用快取；題目圖片快取優先。
const VERSION = "20261006224021";
const SHELL = ["./", "index.html", "countdown.html", "assets/style.css", "assets/app.js", "assets/api.js", "assets/store.js",
  "assets/util.js", "assets/katex/katex.min.js", "assets/katex/katex.min.css", "manifest.webmanifest", "icons/icon-192.png"];
const CACHE = "g116-" + VERSION;

self.addEventListener("install", (e) => {
  e.waitUntil(caches.open(CACHE).then((c) => c.addAll(SHELL)).then(() => self.skipWaiting()));
});

self.addEventListener("activate", (e) => {
  e.waitUntil(caches.keys().then((keys) => Promise.all(keys.filter((k) => k !== CACHE).map((k) => caches.delete(k))))
    .then(() => self.clients.claim()));
});

self.addEventListener("fetch", (e) => {
  const url = new URL(e.request.url);
  if (e.request.method !== "GET" || url.origin !== location.origin) return;
  if (url.pathname.includes("/data/")) {
    e.respondWith(fetch(e.request).then((res) => {
      const copy = res.clone();
      caches.open(CACHE).then((c) => c.put(e.request, copy));
      return res;
    }).catch(() => caches.match(e.request, { ignoreSearch: true })));
    return;
  }
  e.respondWith(caches.match(e.request, { ignoreSearch: url.pathname.includes("/img/") }).then((hit) => hit || fetch(e.request).then((res) => {
    if (res.ok && (url.pathname.includes("/img/") || url.pathname.includes("/assets/"))) {
      const copy = res.clone();
      caches.open(CACHE).then((c) => c.put(e.request, copy));
    }
    return res;
  })));
});
