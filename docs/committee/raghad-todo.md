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
- **Not synced yet:** the sales target. Ch. 2, the abstract and the summary still say
  **255K ₪ / ~3,700 units** (Raneem was told not to change sales numbers in this round). They
  will be updated to your `numbers.md` base case (2,200 units / 150K ₪ gross) in the next round.

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

## 2. Process (F8)

- **LG-02 / LG-03:** prompt 03 holds Gemini's answer, not your prompt to Gemini; prompt 04 is
  not verbatim; your approval and merge prompts are not logged. Please add them (new numbers,
  noting the session they belong to).
- **LG-11:** commit titles ≤ 72 characters and body lines wrapped at about 72.
