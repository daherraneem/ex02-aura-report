# 17 – Expert Committee Fixes (Chapters 4–7, Raghad)

**Author:** Raghad · **Agent:** Antigravity · **Date:** 2026-11-23

## Prompt

```
אני

Run git pull. Read docs/committee/summary.md (our expert committee review).
Fix in my chapters 04-07 only:
- F1: add a simple unit-economics / profit-and-loss table (price 69 NIS, cost per unit, marketing budget
  about 150K NIS, break-even point) and set a realistic sales target that matches it.
  Write the agreed new numbers (sales target, units, budget, break-even) in docs/committee/numbers.md,
  so Raneem can update chapter 2, the summary and the abstract.
- F4, F5, and the parts of F6 and F7 that are in my chapters.
Build and check, then follow the push rules in AGENTS.md and push (mention "after expert committee").
```

## What the agent did

- Pulled `9702e9a` and read `docs/committee/summary.md` along with all 5 subagent review reports (`brand-strategist.md`, `marketing-professor.md`, `academic-editor.md`, `design-latex.md`, `lecturer-grader.md`).
- **F1 (Unit economics, P&L, realistic sales target & `docs/committee/numbers.md`):**
  - Verified Israeli 18% VAT (PwC Worldwide Tax Summaries, `pwc2025israelvat`), computed net unit price (`58.5` ILS), labelled variable costs (`14.0` COGS + `6.5` fulfillment/payment + `4.0` blended commission = `24.5` ILS), contribution margin (`34.0` ILS/unit), and break-even (`4,412` physical units / `~304K` ILS gross / `~258K` net, reached in Months 9–10).
  - Revised Months 4–6 active-launch Base Case from `255K` ILS / `3,700` units to a realistic bottom-up funnel target of **`2,200` physical units (`150.0K` ILS gross / `127.1K` net = `29.7%` of Year-1 SOM)** with Low (`1,500`) / Base (`2,200`) / High (`3,000`) scenarios and explicit admission of a planned `-75.2K` ILS market-entry investment in Months 4–6 (`Table 5.3`).
  - Documented all agreed numbers, funnel assumptions, tasting-bar sizing (`3 × 500 = 1,500` sealed minis), academic calendar dates, and unified terms in `docs/committee/numbers.md` for Raneem to sync Chapters 2, 8, and the abstract.
- **F4 (Mid-tier competitors, non-price value index & robust decision matrix):**
  - Added 3 verified mid-price competitors sold in Israel (`NYX Fat Oil Lip Drip` 40 ILS, `Maybelline Teddy Tint` 46–58 ILS, `Clinique Black Honey` 77–115 ILS) to `chapters/04-market.tex`, `references.bib`, and `figures/price_positioning.py`.
  - Removed price/ml from the Chapter 4 value index, reframed it as a subjective expert positioning hypothesis with explicit anchors, and plotted AURA as a target range (`7.4–8.4`).
  - Aligned per-event field cost (`~13.3K` ILS/day) between Alt B and Alt C, reframed the digital quiz as a 3-question Flavor & Shade Quiz (2 culinary + 1 skin-tone swatch question, A/B tested conversion aid), re-scored Alt C conservatively (`7.65` vs `A=7.40`, `B=6.45`), and added a `-1` score-sensitivity check + RTL panel swap in `figures/decision_matrix_scores.py`.
- **F5 (Timeline sequence, academic calendar & expanded risk register):**
  - Fixed `chapters/06-workplan.tex`, `figures/tikz/wbs_tree.tex`, and `figures/gantt_launch.py` to sequence Formula Freeze & Focus Groups (Month 1, Dec 2026) → `REQ-01` Submission & 3,000-unit/1,500-mini production (Month 2, Jan 2027) → Approvals & Tests (Month 3, Feb 2027) → Spring Semester Launch & `M4` Commercial Gate (Month 4, Mar 2027), with an explicit `10K` ILS regulatory/trademark line and top-2 shades selected by Month-4 sell-through.
  - Expanded `chapters/07-risks.tex` and `figures/tikz/risk_matrix.tex` to 8 risks (`R1`–`R8`), adding food-imitation/hygiene (`R5=12`, citing EU Directive 87/357/EEC), raising competitor copying/Rhode shipping (`R6=12`), adding marketplace onboarding/promo risk (`R7=12`), listing only *additional* mitigations beyond the base plan, and justifying realistic residual scores (`16 → 9`, `R3: 15 → 8`).
- **F6 & F7 (Consistency, source hygiene & chapter-level layout in ch. 04–07):**
  - Unified terminology (`בר טעימות`, `משפיעניות קטנות`, `כ-15 ש"ח לטינט`, `REQ-01--REQ-11`, `52%/27%/21%` budget split, `57 מוסדות`), fixed author names to English `\en{}` everywhere, fixed all Hebrew typos (`מעניקה לחות`, `שיסוכם`, `של חקר השוק`, `צד ראשון`), removed promotional wording, raised all Ch. 4–7 tables to `\footnotesize` minimum, sized Python figures to print width (~6.5 in), added top padding to `launch_architecture.tex`, referenced Eq. (4.1) with `N_s`, fixed Table 4.1 math product, fixed `kelley1959critical` author format, updated `boi2026rates` URL, added publisher URLs to books, replaced `imf2025creator` with `hypeauditor2025state`, and added missing abbreviations (`COGS`, `FOMO`, `IEC`, `ISO`, `KPI`, `PMBOK`, `PoC`, `QR`, `VAT`) to `chapters/00-abbreviations.tex`.
- Rebuilt with `.\build.ps1`, checked `main.log`, `main.blg`, and page budgets, updated `README.md`, and committed.

## What was corrected

Found by compiling and visually inspecting the regenerated figures (`price_positioning.pdf`, `decision_matrix_scores.pdf`, `gantt_launch.pdf`) and checking `main.toc` and `main.log`:

- **`price_positioning.py`:** Repositioned the `Clinique (Black Honey)` label below its dot and moved the `AURA` range label cleanly inside the left side of the Masstige zone so labels never overlap.
- **`decision_matrix_scores.py` & `05-alternatives.tex`:** Reconciled the Sensory-First scenario score in prose (`7.80` → `7.75`) to match the exact Python calculation (`0.35×8 + 0.20×8 + 0.15×7 + 0.10×7 + 0.10×8 + 0.10×8 = 7.75`), and lowered the stacked-bar label threshold to `0.58` so all 6 criteria contributions print cleanly.
- **`gantt_launch.py`:** Aligned task `1.1` duration (`1.0` month) and task `1.3` start (`1.0`) so milestone `M1` sits flush at the end of Month 1.
- **Page budgets:** Compacted table row stretch (`\arraystretch`) and figure scaling in Chapters 4 and 7 so Chapters 4–7 preserve the booklet page map (**6 / 8 / 4 / 2 = 20 pages exact**) at `\footnotesize` minimum table font size, with 0 compile errors and 0 Biber warnings.
