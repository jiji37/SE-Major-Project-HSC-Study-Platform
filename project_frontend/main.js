// Register the service worker
fetch("https://<https://potential-space-broccoli-7v5g9xwp7479fxjv7-5000.app.github.dev/>-5000.app.github.dev/api/hello")
  .then(res => res.json())
  .then(data => console.log(data));
if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register('/SE-Major-Project-HSC-Study-Platform/project_frontend/service-worker.js')
      .then(reg => console.log('Service Worker registered:', reg))
      .catch(err => console.log('Service Worker registration failed:', err));
  }
