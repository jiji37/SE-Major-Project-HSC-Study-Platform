// Register the service worker
if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register('/Programming-for-the-web/simple-pwa/service-worker.js')
      .then(reg => console.log('Service Worker registered:', reg))
      .catch(err => console.log('Service Worker registration failed:', err));
  }
