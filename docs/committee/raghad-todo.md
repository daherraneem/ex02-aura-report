# To do for Raghad — after the expert committee

Written by Raneem's agent on 2026-11-23 (prompt 18), after pulling Raghad's fix commit
`2a88450` (F1, F4, F5, F6, F7 in chapters 4–7). Under the ownership rule, chapters 04–07 were
**not edited**. Most items of the committee in your chapters are already fixed by `2a88450`
(table fonts, figure sizes, short captions, typos, REQ range, Bank of Israel URL, Kelley name,
Krishna sentence, terms). Only the items below are still open. IDs refer to
[summary.md](summary.md); page numbers are body pages of the current `main.pdf` (50 pages).

## 0. What changed in Raneem's commit (please read first)

- **`aura-report.cls` v0.2** (shared, fix F3):
  - `\en` and `\ltr` are robust, so the lists of figures/tables keep their spaces.
  - English inside `\en{}` no longer hyphenates (no "Super-/Pharm", no "REQ-/01").
  - Lists of figures and tables are in the TOC; wider number box in the lists.
  - Bibliography: single spacing, small type, ragged right, URLs break, and `@online` entries
    print their year (the IEEE driver leaves it out).
  - `\sep` keeps the bullet with the previous keyword; `\emergencystretch=1.5em`;
    the abbreviations table is tighter and ragged, so the longer list fits on one page
    (it ran 85 pt past the page bottom after the new abbreviations were added).
- **Chapter 2 (Raneem), fix F2:** a **control campus** was added to the measurement design.
  - REQ-09: baseline and endline survey at the 3 pilot campuses **and one control campus**
    (online content, no tasting bar), with a foil brand.
  - G1: aided awareness ≥ 20% at the pilot campuses **and at least 10 percentage points above
    the control campus**.
  - G5 is gross "trial-to-purchase conversion"; the net effect of the bars is estimated against
    the control campus (ch. 3, §3.5).
- **Synced from your numbers** (ch. 2, abstract, summary): 1,500 samples (3 × 500 sealed minis),
  decision score 7.65, eight risks, maximum residual exposure 16 → 9.
- **Synced in prompt 21:** the sales target. Ch. 2 (G4, both tables, problem statement, guiding
  question), the abstract and the summary now use your `numbers.md` base case: **~2,200 units /
  ~150K ₪ gross (~127K net) in months 4–6**, budget 150K ₪, break-even **4,412 units in months
  9–10**. The old 255K ₪ / 3,700 units no longer appear anywhere in the report.

## 1. Still open in chapters 4–7

1. **Page budget:** chapter 4 is now **7 pages** (body pp. 17–23); the booklet gives it 6.
   The body is 38 pages instead of 37.
2. **Control campus** (follows the ch. 2 change): in ch. 6, WP3 / M3 "סקר בסיס (REQ-09)" and
   WP6 / M6 "סקר מסכם (G1)" should mention the control campus; the survey may need a line in
   the budget (it currently sits in the 35K paid media and surveys line).
3. **Overfull lines** in `07-risks.tex`: line 34 (2.7 pt) and line 71 (6.9 pt).
4. **TikZ files** (LG-14): `launch_architecture.tex` (14 uses), `risk_matrix.tex` (8),
   `wbs_tree.tex` (7) still call `\textenglish` / `\LR` directly instead of the class macros
   `\en` / `\ltr`. If the class macros do not work inside TikZ nodes, tell Raneem and a
   TikZ-safe macro will be added to the class.

## 1a. Numbers check across all chapters (prompt 21, 2026-11-23)

Raneem's agent checked the sales target, budget and break-even in every chapter, the abstract,
the TikZ files and the Python figures against `numbers.md`.

- **No number mismatches in chapters 4–7.** Ch. 4 (2,200 units / 150K gross / 127.1K net,
  ~30% of SOM, 0.59% of SAM), ch. 5 (34.0 ₪ contribution, 4,412 units / ~304K gross / ~258K net,
  months 9–10, −75.2K, budget 78K + 40K + 32K), ch. 6 (WP1–WP6 = 22 + 53 + 9 + 36 + 21 + 9 =
  150K, 100%; M6 2,200 units / 150K; break-even 4,412 in months 9–10) and the TikZ files
  `launch_architecture.tex` and `wbs_tree.tex` all match. Ch. 7 has no sales or break-even numbers.
- **Wording only (optional):** `04-market.tex` line 87, "יעד מדורג וריבועי" — "ריבועי" means
  "quadratic"; did you mean "רבעוני" (quarterly)?

## 1b. Done for you at submission (prompt 24, with your approval)

- `05-alternatives.tex`: 10 amounts written as `\ltr{43}K` printed reversed ("K43", "K75.2-" in
  Table 5.3). The K was moved inside `\ltr{}` (lines 87–89, 113, 240–243), the same fix you made
  in chapters 4, 6 and 7. No other change to your files.

## 2. Process (F8)

- **LG-02 / LG-03:** prompt 03 holds Gemini's answer, not your prompt to Gemini; prompt 04 is
  not verbatim; your approval and merge prompts are not logged. Please add them (new numbers,
  noting the session they belong to).
- **LG-11:** commit titles ≤ 72 characters and body lines wrapped at about 72.
