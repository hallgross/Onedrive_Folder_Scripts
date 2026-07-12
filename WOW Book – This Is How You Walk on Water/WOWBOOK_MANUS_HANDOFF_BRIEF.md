# 📦 WOW Book — Manus Handoff Brief
*From Loretta / Cowork → Manus. Purpose: deploy the FINISHED book to the live site and add NEW visuals. Do NOT rebuild the book.*

> **Golden rule:** The book is already written, approved, and assembled in this repo. **Deploy it — do not regenerate it.**
> Rebuilding is what caused wrong video clips and broken buttons before. Spend the **25,000 credits on NEW visuals only**
> (list at the bottom), not on redoing finished work.

---

## ✅ WHAT IS DONE (deploy as-is — do not change wording, titles, or order)
| Asset | Path in repo |
|-------|--------------|
| **Full book (print-ready)** | `00 Full Book – Sell Ready/This_Is_How_You_Walk_on_Water_FULL_BOOK.html` |
| **Sales listing copy** | `00 Full Book – Sell Ready/WOWBOOK_Sales_Listing.md` |
| **Launch checklist** | `00 Full Book – Sell Ready/WOWBOOK_Launch_Checklist.md` |
| **Book cover (art + title)** | `00 Full Book – Sell Ready/WOWBOOK_Cover.html` |
| **Book landing page (functional)** | `book-landing.html` |
| **All 30 chapters (approved)** | `01 Manuscript – Chapters/CH01…CH30/` |
| **Divina interlude (unnumbered, after Ch 11)** | `01 Manuscript – Chapters/INTERLUDE_Birth_of_Divina/` |
| **Prophecy journals — transcription** | `07 Testimony Journals – Prophetic Words/WOWBOOK_Prophecy_Journals_Transcription.md` |
| **Prophecy journals — gallery** | `07 Testimony Journals – Prophetic Words/WOWBOOK_Prophecy_Journals_Gallery.html` |
| **Journals → chapters placement map** | `07 Testimony Journals – Prophetic Words/WOWBOOK_Journals_to_Chapters_Placement_Map.md` |
| **Chapter videos (Loretta's own)** | `11 Videos/CH##.mp4` (+ CH20, I Rise finale, Dove Kiss) |
| **Soundtrack (13 tracks)** | `12 Soundtrack/WOWBOOK_*.mp3` |
| **ME likeness frames registry** | `WOWBOOK_ME_Frames_Registry.md` |

### Locked facts (do not alter)
- **Title:** *This Is How You Walk on Water* — by **Loretta Hall** · Heavenly Hands Divine · *Faith Over Fear*.
- **Finale:** CH30 = **"Mother of Many Nations: The Closing Commission"** (walk-on-water testimony kept + MMN closing).
- **Interlude:** "Prophetic Interlude: The Birth of Divina" sits **after Ch 11**, unnumbered (30-chapter structure intact).
- **Editions/pricing:** Digital eBook **$9.99** · Paperback **$19.99** · Hardcover/Gift **$29.99** · free Waitlist.

---

## 🎬 Chapter videos — the naming scheme (use this, no symbolic clips)
Each chapter plays its own file from the `11 Videos` folder, by chapter number:
```
11 Videos/CH01.mp4 … CH30.mp4
```
**Do NOT wire generic/symbolic stock clips to chapters.** Only Loretta's approved videos, named `CH##.mp4`.
Missing chapters simply show no video until Loretta adds the file. CH20 and the I Rise finale are already in place.

---

## 🛠️ SITE FUNCTIONAL REQUIREMENTS (this is where the live site failed — fix on your side)
Every clickable-looking button must do something real. Test on **desktop AND mobile**:
1. **Preview** → opens that chapter's preview text (or a clear "Coming Soon" message). No dead buttons.
2. **Join Waitlist / Notify Me** → submits to a **real database/list** (not just localStorage) with a visible confirmation.
3. **Buy / Buy Scroll** → real checkout (Stripe/Payhip/Gumroad). Buy Scroll uses the **correct WOW-PR scroll SKU** for that chapter. If checkout isn't live yet, the button must say "Coming Soon" — never look clickable with no action.
4. **Soundtrack** → if implemented, show a visible **Play/Pause** control. If not implemented on the site, do not imply the preview plays music.
5. Return a **real 30-row verification table** (Chapter | Preview | Waitlist | Buy Scroll | Correct link/SKU | Mobile tested) — tested live, not assumed.
6. **Self-host** all images/videos/audio in the site repo (no Higgsfield-CDN dependency, no broken links).

---

## 🔒 PRIVACY & BRAND RULES (must follow)
- **CH1–CH4 (early life):** symbolic artwork ONLY. Loretta was in foster care — **no childhood photos**. The absence of photos is part of the testimony.
- **Medical chapters (CH11–CH13):** no readable wristbands, record numbers, full documents, addresses, or private patient info. Crop/blur anything sensitive.
- **James (CH02):** use his real Army photo **unaltered** — do not repaint or AI-edit his face. Honorable, tender. He has passed; handle gently, no "deceased" on the image.
- **No other people's faces** without Loretta's approval. No accusations, no private family details.
- **Model rule:** Loretta is her own model (Higgsfield Souls). Default **Coral Elegance Unveiled** for faith/signature.
- **Keep WOWBOOK (the book) separate from WOWB / WOW-PR (Prayer Scroll products).** Never merge or rename.

---

## 🟢 WHERE THE 25,000 CREDITS SHOULD GO (NEW visuals only)
1. **Animate Loretta's 13 "ME" likeness frames into moving videos** (Coral Soul) — see `WOWBOOK_ME_Frames_Registry.md` for the exact start-frames and per-chapter scene prompts. These replace still frames on CH04,06,09,10,11,12,14,15,18,19,24,28,29.
2. **Book trailer** (30–60s) — testimony montage → cover → "Coming Soon / buy link".
3. **Collection reel** — short social cut for Instagram/TikTok.
4. Any **missing chapter artwork/video** Loretta flags.

Do **not** spend credits regenerating chapters, journals, the finale, or the soundtrack — those are final.

---

*Faith Over Fear. The book is finished — deploy it, don't rebuild it.* ✨
