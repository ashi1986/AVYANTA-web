# avyanta.ai — local clone

Static mirror of **https://avyanta.ai** (frontend only), saved on **2026-11-14**.

## How to open

Double-click **`start-website.bat`**.

It starts a small local web server at <http://127.0.0.1:8080/> and opens your browser.

You can also run it manually:

```powershell
cd D:\website
python serve.py        # or: python serve.py 8081
```

> Open the site through the server, not by double-clicking `index.html`.
> This is a single-page React app: its router and deep links need an HTTP
> server with a fallback to `index.html`.

## What was mirrored

- Every page listed in `sitemap.xml` plus all routes from the app bundle
  (about, services, expertise, industries, case studies, legal pages, admin shells).
  The server pre-renders real HTML per route, so each page has its own content.
- `index.html`, `robots.txt`, `sitemap.xml`, `favicon.jpg`
- `static/js/main.ccff4715.js` and its source map
- `static/css/main.706252b1.css`
- All 27 images/logos in `static/media/`
- Google Fonts (Manrope + Inter) downloaded to `static/css/fonts/` with a local
  `static/css/fonts.css`, so typography works offline.

## Known limits

- The clone is **frontend only**. Features that call the original backend will
  not work: the contact form submission, the admin login/dashboard, and
  analytics tracking. Pages that require data from an API may show a failed
  request in DevTools; this does not affect the static pages.
- External links (LinkedIn, X, Google Maps, Apollo tracker) still point online.
- `serve.py` and `start-website.bat` are added helper files, not part of the
  original site.

## Structure

```
D:\website\
├── index.html               # home page
├── about\ index.html        # /about
├── case-studies\ ...        # /case-studies/<slug>
├── industries\ ...          # /industries/<slug>
├── services\, expertise\, contact\, ...
├── static\
│   ├── css\main.706252b1.css
│   ├── css\fonts.css + fonts\
│   ├── js\main.ccff4715.js (+ .map)
│   └── media\               # images and logos
├── serve.py                 # local server with SPA fallback
└── start-website.bat        # double-click launcher
```
