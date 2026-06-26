# 📥 MANUS HANDOFF — START HERE
**Heavenly Hands Divine · Loading Guide.** Everything is prepped by Claude — Manus just uploads & publishes.
> Standing rule: final publish to live shop / Stripe = **Loretta approves**.

---

## A) EDU EDUCATION CENTER — 30 digital ebooks ($15.99 each)
**File:** `HHD_EDU_30_Ebooks_PDFs.zip` (30 branded PDFs, EDU01–EDU30).
**Manus steps (minimal):**
1. Unzip — each PDF = one product (filename = `SKU_Title`).
2. Create a **digital-download** product per PDF · price **$15.99** · instant delivery.
3. Collection: **"Education Center."** Feature **EDU30** + **EDU10**.
4. Digital only — **not** Printify/POD.

Listing copy: `EDU_Sales_Listings.md`. Bundles: Complete Library $99–129 · Faith Over Fear Starter (EDU10/01/30) $39 · Healing (EDU05/12/28/20) $49 · Prayer & Family (EDU07/13/24/25) $49 · Builder's (EDU14/16/29) $39.

---

## B) JUNETEENTH — POD (Printify → shop)
**Files:** `HHD_Juneteenth_Collection.csv` (JT001–JT025 + 4K URLs) · `HHD_Juneteenth_Scripture_AddOns_JT026-JT036.csv` (JT026 hero + JT027–JT036 + 4K URLs).
**Manus steps (minimal):**
1. Download each `Design_URL` (4K print-ready PNG).
2. Build product on matching Printify blank (Tee/Hoodie/Kids Tee/Kids Jumper/Mug).
3. Price from CSV (Tee $29.99 · Hoodie $49.99 · Kids Tee $24.99 · Kids Jumper $34.99 · Mug $17.99).
4. Publish all to one collection: **"Juneteenth."**

Direction: **scripture-based.** JT026 (John 8:36) = hero/reference style. JT031 link may show pending — request final if blank.

---

## C) Ads & mockups (already made by Claude)
Model = Loretta's Higgsfield Soul **"Coral Elegance Unveiled."** On-model shots → hero/social; flat-lay mockups → catalog thumbnails.

---

## D) WALK ON WATER — publishing workflow (live store)
**Source of truth = Empire (this repo). Store = Loretta's live store (Manus-managed).**
**Golden rule:** the live store must NOT contain a copy of the master manuscript — only finished products that **point back** to a master chapter.

**Files:** `WOW_PUBLISHING_WORKFLOW.md` (rules) · `WOW_Master_Chapters.csv` (30 masters — private, do NOT publish) · `WOW_Product_Family.csv` (211 products → store).

**Manus steps:**
1. For each row in `WOW_Product_Family.csv`, create/locate the matching product in the live store and record its `Store_URL` back into the CSV. Store the `Master_Chapter_ID` on the product (tag/metafield) so it links to its master.
2. **Never** paste the master manuscript text into a store product. Products = WOW PDF / Prayer Scroll / Study Guide / Journal / Audio / Video / Bundle / Complete Book only.
3. Respect `Publish_Status`: only publish rows Loretta marks **Ready to Publish**. If a master is edited (its `Master_Version` rises above a product's `Published_From_Version`), set that product to **Needs Update** and WAIT for Loretta's approval — do **not** auto-overwrite the live product.
4. **De-dupe:** if the WOW book currently shows in two places in the store, keep ONE product set and remove the duplicate listing (do not delete Empire files).

## E) LINK PERMANENCE — re-host so nothing expires
**File:** `HHD_ASSET_REGISTRY.csv` (all 71 images + permanent Higgsfield Job IDs).
**Manus steps:** download each `Current_CDN_URL` → re-upload into Loretta's own store/Drive → paste the owned link into `Permanent_Owned_URL` → point store products at the owned link. (Job IDs are permanent backups if any CDN link ever changes.)

---

## Division of labor
**DONE (Claude):** all content · 30 EDU PDFs · 36 Juneteenth designs (4K) · CSVs w/ metadata + URLs · listings · mockups · on-model ads · July 1 launch on calendar · WOW publishing workflow (master↔product map + status) · asset registry for link permanence.
**MANUS (light):** upload PDFs · push designs to Printify · wire WOW products to master chapters in the live store (pointers, not copies) · re-host images to owned links · group collections · publish (with Loretta's OK).
