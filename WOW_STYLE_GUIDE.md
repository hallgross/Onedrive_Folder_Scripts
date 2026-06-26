# Walk On Water (WOW) — Master Style Guide
**Heavenly Hands Divine · Premium Devotional Companion Series**
*Use this so every WOW PDF stays visually identical — only the chapter-specific content changes.*

---

## 1. Page & Format
- **Page size:** US Letter (8.5 × 11 in), portrait
- **Margins:** 1 in left/right; ~1.1 in top for section headers; 0.5 in footer zone
- **Length:** 14–15 pages per chapter (varies only with story/insert length)
- **Engine:** generated from `build_wow_all.py` (single source — do not hand-edit individual PDFs)

## 2. Color Palette (exact hex)
| Role | Hex |
|------|-----|
| Navy (scripture, accents) | `#0b2a4a` |
| Ocean blue | `#1b6ca8` |
| **Gold (brand accent)** | `#c9a227` |
| Teal (section headers) | `#1b4d5e` |
| Ink (body text) | `#15202b` |
| Soft grey (captions/footer) | `#5b6b7b` |
| Journal rule lines | `#cdd6df` |
| Insert panel background | `#f3f7fb` |

## 3. Typography
- **Brand wordmark / labels:** Helvetica-Bold / Helvetica (uppercase)
- **Titles & headers:** Times-Bold
- **Scripture & blessings:** Times-Italic (navy)
- **Body / testimony:** Times-Roman, 11.5 pt, 16.5 leading
- **Section headers:** Times-Bold 16 pt, teal, with a gold underline rule
- **Footer:** Helvetica 8 pt, soft grey

## 4. Gold Accents
- Gold underline beneath every section header
- Gold left-bar on "From the Book" insert panels
- Gold author signature line: *Loretta "Lolo" Hall*
- Gold brand wordmark on cover & back cover

## 5. Cover (unique per chapter, consistent frame)
- **Water scene** drawn per chapter, themed to the message. Five scene types:
  - `dawn` (sunrise water) · `storm` (dramatic waves + lightning) · `night` (moon + stars) · `open` (bright horizon glow) · `glory` (gold rays from heaven)
- Consistent overlay on every cover: **HEAVENLY HANDS DIVINE** wordmark → **WALK ON WATER SERIES** → gold rule → **CHAPTER [Word]** → Title → focus line → scripture reference → **Loretta "Lolo" Hall**
- A translucent navy panel sits behind the title for legibility on any scene.

## 6. Page Order (every chapter, in this exact sequence)
1. **Cover** (themed water scene)
2. **Welcome** (from Lolo)
3. **Key Scripture** (verse + why it matters)
4. **Chapter Story** (Testimony Reflection, signed Lolo)
5. **From the Walk On Water Book** *(if inserts provided — up to 3 gold-framed excerpts)*
6. **Reflection** (4 questions + writing lines)
7. **Prayer**
8. **Declaration** ("I declare…")
9. **Action Steps** (checkboxes)
10. **Journal — What God Spoke to Me** (16 lines)
11. **Prayer Notes** (request · date · answered)
12. **Related Products**
13. **Closing Blessing** (signed Lolo)
14. **Back Cover** (brand, website, store, socials, copyright, series #, **QR code**)

## 7. Footer (every interior page)
`Heavenly Hands Divine  •  Walk On Water Series  •  Chapter [#]  •  [page number]` — Helvetica 8 pt, centered, soft grey.

## 8. QR Code
- Real scannable QR on the **back cover** of every chapter
- Encodes: `https://www.heavenlyhandsdivine.com/wow/chapter-[#]`
- Caption: "Scan: prayer • worship • teaching • video"
- White quiet-zone box behind it; ~1.25 in square
- **To activate:** point each chapter URL to that chapter's prayer/worship/teaching/video page.

## 9. Standard Reusable Copy
- **Closing Blessing:** *"May the God who called you upon the waters strengthen your faith, calm every storm before you, and remind you that His hand has never left yours. Continue to walk in faith, knowing that He who began a good work in you will carry it to completion."*
- **Related Products:** Matching Prayer Scroll · Selah Victory Figurine · Divina Wings Apparel · Walk On Water Study Guide · Faith Journal
- **Reflection questions (standard set):** What is God saying to me? · What fear do I need to release? · What promise do I need to believe? · What step of faith am I being asked to take?
- **Signature block:** *Loretta "Lolo" Hall — Founder, Heavenly Hands Divine*

## 10. What changes per chapter (the ONLY variables)
Chapter number · title · focus line · scripture (ref + verse) · Testimony Reflection · prayer · declarations · cover scene type · QR URL · book inserts (optional).

## 11. To produce a new/updated chapter
Edit only the chapter's entry in `build_wow_all.py` (`CH` list / `OV` overrides), then rebuild. Never edit a PDF directly — the script guarantees identical styling. The build prints an **audit** confirming all 11 required sections are present in every chapter, and writes `WOW_AUDIT.csv`.

*Faith Over Fear.* ✨
