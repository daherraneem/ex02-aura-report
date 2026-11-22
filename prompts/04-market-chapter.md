# 04 – Chapter 4: Market Research

**Author:** Raghad · **Agent:** Antigravity · **Date:** 2026-11-22

## Prompt

```
First read AGENTS.md and follow its rules for the whole session.
Then read README.md, main.tex, aura-report.cls (command list at the top) and chapters/01-intro.tex.

Save the next numbered prompt file in prompts/ as "gemini-consult" with the brief below,
noting it came from a planning talk with Gemini in the browser.

Then write my chapter chapters/04-market.tex (Market research, 6 pages) in Hebrew,
using the brief: TAM/SAM/SOM, a comparison table of real competitors, and two Python graphs
(use figures/aura_style.py like figures/page_budget.py).
Check every number and competitor with web search - real sources only, in references.bib.
Run .\build.ps1, fix errors, and show me the chapter. Do not commit yet.
```

*(Note: The full Strategic Launch Brief attached to this prompt from Raghad's browser planning talk with Gemini was saved separately as `prompts/03-gemini-consult.md`; the prompt wrapper was pasted multiple times in the chat input and is recorded once above.)*

## What the agent did

- Ran `git pull` (up to date) and read `AGENTS.md`, `README.md`, `main.tex`, `aura-report.cls`, `chapters/01-intro.tex`, `chapters/04-market.tex`, `references.bib`, `figures/aura_style.py`, `figures/page_budget.py`, and Exercise 1's target pricing (`69` ILS / tube, `299` ILS / 5-shade bundle).
- Saved the Gemini browser planning brief as `prompts/03-gemini-consult.md`.
- Verified all global/Israeli market metrics, higher-education demographics, digital reach, exchange rate, and competitor retail prices/availability via web search, adding 20 verified sources (canonical URLs + `urldate = 2026-11-22`) to `references.bib` without modifying Raneem's existing entry. Added `D2C` alphabetically to `chapters/00-abbreviations.tex`.
- Built two Python figures using `figures/aura_style.py`:
  - `figures/market_growth_tam_sam_som.py` -> `figures/market_growth_tam_sam_som.pdf` (Israel cosmetics market 2026–2031 CAGR forecast + TAM/SAM/SOM log-scale funnel).
  - `figures/price_positioning.py` -> `figures/price_positioning.pdf` (verified Israeli price ranges vs. transparent 4-criterion sensory-brand-accessibility value index, highlighting AURA's `69` ILS Masstige White Space).
- Wrote `chapters/04-market.tex` in Hebrew (6 pages, 0 `\draftnote{}` left, 3 tables, 2 Python figures, 3 AURA styled boxes, 20 cited sources).
- Compiled with `.\build.ps1` and inspected `main.log`, `main.blg`, and rendered PNG images of both Python figures and all 6 pages of Chapter 4.
- After user approval, added a Progress Log entry to `README.md`, committed, and pushed.

## What was corrected

Found by compiling and visually inspecting every figure and every rendered page:

- **Compile error on first pass:** `\en{...}` inside `\section{}`/`\subsection{}` headings triggered a `hyperref` PDF-bookmark error (`\aura@next` from `\aura@peekcolon`). Fixed by keeping section/subsection headings in pure Hebrew (matching the skeleton style) and placing `\en{TAM}`, `\en{SAM}`, `\en{SOM}` in the opening sentences.
- **Python figure layout fixes:**
  - `market_growth_tam_sam_som.py`: increased `wspace` to `0.74`, widened figure to `8.2 x 3.55`, shortened y-tick labels so the two panels never overlap, raised the `CAGR` badge, and padded `xlim` so `$408.5M` does not touch the y-axis spine.
  - `price_positioning.py`: moved the legend cleanly below the x-axis (`ncol=2`) so it does not cover `Essence`, widened and heightened the shaded Masstige opportunity box so the `AURA` label and box caption stay comfortably inside the dashed border.
- **BiDi & typography fixes in `chapters/04-market.tex`:**
  - Merged adjacent `\en{}` calls (e.g. `\en{Rhode} \en{Peptide Lip Tint}` -> `\en{Rhode (Peptide Lip Tint)}`) so brand + product names never reorder right-to-left inside tables.
  - Replaced `₪` inside `\ltr{...}` ranges with `\ltr{...} ש"ח` and wrote `מגיל \ltr{13} ומעלה` / `מגיל \ltr{18} ומעלה` to prevent symbol flipping.
  - Wrapped `\mbox{\en{No-Makeup Look}}` so it does not split awkwardly across a hyphen.
  - Switched Equation (4.1) to a compact two-line `align` so the equation number stays aligned with the formula.
- **Page budget & table widths:**
  - Tightened repetitive competitor prose and adjusted float placement (`[htb]`) so Chapter 4 hits the **exact 6-page budget** (pages 6–11 in the current skeleton) with zero orphan headings, zero float-only pages, and balanced visual density.
  - Adjusted `\tabcolsep` and column widths in Tables 4.2 and 4.3, plus rephrased one opening line to eliminate overfull `\hbox` warnings in Chapter 4.
  - Protected `{Israel}` in braces in `references.bib` titles for proper IEEE capitalization.
