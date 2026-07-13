# 🚀 Deploy Heavenly Hands Divine to Netlify (your permanent home)

Your site now lives in a clean **`public/`** folder in your repo — only public pages deploy, never your private
backoffice docs. Netlify publishes `public/` automatically (set in `netlify.toml`).

Structure (scales to more books):
```
public/
  index.html            ← home ("Faith Over Fear", links to your books)
  wow-book/index.html   ← the WOW Book page (videos + soundtrack)
  wow-book/videos/  wow-book/audio/
  (future) next-book/index.html …
```

---

## ✅ One-time setup (about 5 minutes)
1. Go to **netlify.com** → **Sign up** (free) with your **GitHub** account.
2. Click **Add new site → Import an existing project → GitHub**.
3. Authorize Netlify, then pick the repo **`hallgross/Onedrive_Folder_Scripts`**.
4. Netlify reads `netlify.toml` automatically — **Publish directory = `public`** (already set). Leave build command empty.
5. Click **Deploy**. In ~1 minute you'll get a live URL like `your-site.netlify.app`.
   - Home = `/` · the book = `/wow-book/`

## 🌐 Point your domain
6. In Netlify: **Domain settings → Add a custom domain** → enter **`heavenlyhandsdivine.com`** (and/or `shop.` subdomain).
7. Netlify shows you DNS records. At your domain registrar, add them (or set Netlify as your DNS). Netlify auto-issues a free SSL certificate.
   - *Cancelling Manus does NOT lose your domain — you just repoint it here.*

## 🔁 Every future update (automatic)
- Whenever Claude/Cowork commits a change (a new book, a fix), **Netlify redeploys on its own.** Nothing to re-upload.
- New book = new folder under `public/` + a card on the home page → it just appears live.

---

## 🛒 Selling (the book is in your store too)
- The book **page** (Netlify) tells the story; the **Buy** happens in your store.
- When your store product is live (Shopify/Payhip), send Cowork the **product URL** and the "Buy / Get the Book"
  buttons will link straight to checkout. Until then they use **Join Waitlist**.

## ✅ After it's live — verify
- Open `/wow-book/` on **desktop and phone**: chapter cards, ▶ videos, the 🎵 soundtrack Play/Pause, Join Waitlist, Notify Me.
- Missing chapter videos show "Testimony video coming soon" (until you add `CH##.mp4` to `wow-book/videos/`).

*Faith Over Fear — your books, your domain, your control.* ✨
