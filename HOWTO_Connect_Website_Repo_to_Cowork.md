# 🔌 How to Connect the Website Repo to Cowork (so Claude can fix the live site)

**Goal:** give a Cowork session access to **`hallgross/heavenlyhandsdivine-website`** (the live site repo),
alongside your book repo, so Claude can go through the pages and fix every button.

> Why: the current session is locked to `onedrive_folder_scripts` only. Signing in doesn't change that —
> the repo has to be added when the session/environment is set up.

---

## ✅ Steps

1. **Go to** claude.ai/code (Claude Code on the web / Cowork).
2. **Start a new session** (or "New environment").
3. When it asks which **GitHub repository** to work in, **choose `hallgross/heavenlyhandsdivine-website`**
   (the website). If it lets you add more than one, **add `hallgross/onedrive_folder_scripts` too** so both are available.
4. If the website repo **doesn't appear in the list**, the GitHub app needs permission:
   - Go to **GitHub → Settings → Applications → Claude (or "Installed GitHub Apps")**
   - Click **Configure**, and under **Repository access**, **add `heavenlyhandsdivine-website`** (or choose "All repositories").
   - Save, then return to Cowork and refresh the repo list.
5. **Start the session.**
6. In chat, tell Claude: **"the website repo is connected"** — Claude will verify access and start fixing the live pages/buttons.

---

## 📋 Once connected, tell Claude to:
- Go through **every page and button** on the live site
- Fix **Preview / Join Waitlist / Buy Scroll** (correct chapter ID + WOW-PR scroll SKU)
- Replace the stock music with **Loretta's 13-track soundtrack** (scroll-synced) + a visible Play/Pause
- Wire the **book trailer + collection reel** once made
- Deploy your finished **book-landing.html** as the real `/wow-book`
- Return a **tested 30-row verification table** (desktop + mobile)

## Docs
Full reference: https://code.claude.com/docs/en/claude-code-on-the-web

*Faith Over Fear — one connection away from fixing it for real.* ✨
