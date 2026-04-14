const CACHE_NAME = 'simple-pwa-cache-v1';
const urlsToCache = [
  '/SE-Major-Project-HSC-Study-Platform/project_frontend/index.html',
  '/SE-Major-Project-HSC-Study-Platform/project_frontend/manifest.json',
  '/SE-Major-Project-HSC-Study-Platform/project_frontend/main.js',
  '/SE-Major-Project-HSC-Study-Platform/project_frontend/service-worker.js',
  '/SE-Major-Project-HSC-Study-Platform/project_frontend/main.css',
  'SE-Major-Project-HSC-Study-Platform/project_frontend/Screenshot_2026-04-13_104648-removebg-preview.png',
];

// Install the service worker
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then((cache) => cache.addAll(urlsToCache))
  );
});

// Fetch resources
self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request)
      .then((response) => response || fetch(event.request))
  );
});

