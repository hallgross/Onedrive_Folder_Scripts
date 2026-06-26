# Walk On Water — Publishing Workflow (One Source of Truth)
**Heavenly Hands Divine · Empire writes · Store sells.**
*Rule: there is only ONE master chapter. The Store never holds a second copy of it.*

---

## The two sides

### 🏛️ Empire = Writing & Publishing Office (private — customers never see this)
Lives in **`WOW Book – This Is How You Walk on Water/`**. This is where Loretta:
write the full chapter · save the testimony · edit & revise · approve · generate the WOW PDF ·
generate the Prayer Scroll · track related products · track publishing status.
- **Master manuscript** lives ONLY in `01 Manuscript – Chapters/CH##/`.
- Master records: **`WOW_Master_Chapters.csv`**.

### 🛍️ Store = Finished Products Only (public)
The Store shows **products published from a master chapter** — never the manuscript itself:
WOW PDF · Prayer Scroll · Study Guide · Journal · Audio Prayer · Video Teaching · Bundle · Complete Book.
- Product records: **`WOW_Product_Family.csv`** — each row points back to its master via `Master_Chapter_ID`.

---

## Why this fixes the "book shows in 2 places" problem
The chapter content was duplicated. Now the Store stores **a pointer, not a copy**:
`Product → Master_Chapter_ID → master chapter`. One truth. Editing the master never silently
changes the Store — see the version rule below.

---

## Data model (no database rebuild — additive references only)

**Master Chapter** (`WOW_Master_Chapters.csv`)
`Master_Chapter_ID` (e.g. `WOW-CH12`) · Chapter · Title · Scripture · Theme ·
Manuscript_Status · **Master_Version** · Manuscript_Location · Last_Approved

**Product** (`WOW_Product_Family.csv`)
`Product_ID` (e.g. `WOW-CH12-PDF`) · **Master_Chapter_ID** · Chapter · Product_Type ·
**Publish_Status** · Master_Version · **Published_From_Version** · Store_URL · Notes

Each master chapter → a product family:
`WOW-CH12` → `WOW-CH12-PDF`, `-SCROLL`, `-STUDY`, `-JOURNAL`, `-AUDIO`, `-VIDEO`, `-BUNDLE`.

---

## Status lifecycle (you approve every republish)

| Publish_Status | Meaning |
|---|---|
| **Draft** | Product not built yet |
| **Ready to Publish** | Built, awaiting Loretta's OK |
| **Published** | Live in store; `Published_From_Version == Master_Version` |
| **Needs Update** | Master was edited → `Master_Version > Published_From_Version` |
| **Republish Pending** | Update approved, not yet pushed live |

**The safety rule:** editing a master chapter **only flips its products to "Needs Update."**
It does NOT regenerate or overwrite anything in the Store. The live product keeps selling the
old version until **Loretta approves** the republish. Nothing is automatic.

**How a version bumps:** each time you approve an edit to a master chapter, raise its
`Master_Version` by 1. Any product whose `Published_From_Version` is now lower shows **Needs Update**.

---

## 🔒 Link permanence policy (so nothing expires)
- Your image links are **unsigned CloudFront paths** (no `?Expires=` token) — they are NOT timer-based
  expiring links. But they are hosted on Higgsfield's CDN, not storage you own.
- **Guarantee of permanence = own the file.** Every asset is logged in **`/HHD_ASSET_REGISTRY.csv`** with:
  `Collection · SKU/Chapter · Title · Higgsfield_Job_ID · Current_CDN_URL · Permanent_Owned_URL`.
- The **Higgsfield Job ID is permanent in your account** — any asset can be re-pulled/re-exported from it
  forever, even if a CDN link ever changed.
- **Action for Manus:** download each `Current_CDN_URL`, re-host into Loretta's own store/Drive, paste the
  durable link into `Permanent_Owned_URL`. Then the Store uses owned links — zero expiry risk.

---

## Goal
One source of truth · one master chapter · multiple finished products ·
Empire writes & manages · Store displays & sells · Loretta approves every publish.
