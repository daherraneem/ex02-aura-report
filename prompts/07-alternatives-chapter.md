# 07 – Chapter 5: Launch Alternatives

**Author:** Raghad · **Agent:** Antigravity · **Date:** 2026-11-23

## Prompt

```
Now write my chapter chapters/05-alternatives.tex (Launch alternatives, 8 pages) in Hebrew,
following the booklet (chapter 7):
- 2-3 truly different launch strategies for AURA (use the brief in the gemini-consult prompt
  file if it exists), each with its advantages and costs.
- A weighted decision matrix: 5-6 criteria, weights that sum to 1.0, scores, and the winner.
- The chosen strategy explained as a clear "architecture" of the launch (a TikZ diagram).
- What is innovative in our approach.
Stay consistent with chapter 4 (my market research). Real sources only, in references.bib.
Save this prompt in prompts/ with the next number.
Remove the draft boxes of this chapter. Run .\build.ps1, fix errors, show me. Do not commit yet.
```

## What the agent did

- Read `prompts/03-gemini-consult.md`, `prompts/04-market-chapter.md`, `prompts/01-project-setup.md`, `aura-report.cls`, `references.bib`, `chapters/00-abbreviations.tex`, `figures/tikz/roadmap.tex`, `figures/aura_style.py`, `build.ps1`, and `main.tex`.
- Verified all academic and industry sources via web search and added 10 real, checkable references (with DOIs, ISBN, or canonical URLs + `urldate = 2026-11-23`) to `references.bib` without modifying existing entries: Ulrich, Eppinger & Yang (2020), McKinsey *State of Beauty 2025*, McKinsey Personalization (2021), Krishna (2012), Alexander & Varley (2025), Banik (2021), Terminal X Beauty, Super-Pharm Online Marketplace, The Influencer Marketing Factory (2025), and Octane AI (2025).
- Added new abbreviations used in Chapter 5 (`AI`, `AOV`, `ASMR`, `CAC`, `CRM`, `LTV`, `ROI`, `UGC`) alphabetically to `chapters/00-abbreviations.tex` without modifying existing entries.
- Created two figures matching AURA's visual identity:
  - `figures/decision_matrix_scores.py` → `figures/decision_matrix_scores.pdf` (stacked weighted-score breakdown by criterion + 4-scenario sensitivity analysis).
  - `figures/tikz/launch_architecture.tex` (4-layer TikZ diagram of AURA's chosen Omnichannel Hybrid launch architecture with phygital synergy and zero-party data/UGC feedback loop).
- Wrote `chapters/05-alternatives.tex` in Hebrew (removing all `\draftnote{}` boxes), fully consistent with Chapter 4 (`69` ILS / `10` ml, `299` ILS bundle, `~255K` ILS / `~3,700` units 6-month PoC target, `~211.6K` female students, `57` campuses, `Masstige` White Space) and aligned with Chapter 6's 6-month launch timeline.
- Built the report with `.\build.ps1` and inspected `main.log`, `main.blg`, and rendered PNG images of every page of Chapter 5.

## What was corrected

Found by compiling and visually inspecting both figures and every rendered page of Chapter 5:

- **TikZ diagram (`figures/tikz/launch_architecture.tex`):**
  - On the first render, the tinted layer background rectangles were drawn *after* the inner boxes, hiding the inner content. Moved all four background frames to be drawn first so every box is 100% visible.
  - Wrapped every English phrase in `\textenglish{...}` and every numeric range/percentage in `\LR{...}` inside `\texthebrew{...}` labels so `AI Flavor-Sommelier`, `Terminal X`, and ranges (`20--30`, `2--5`, `4--5`, `5--6`) never invert in BiDi.
  - Shortened Layer 3 box headers to one line and tightened vertical spacing so no box touches a layer tag or arrow.
- **Python figure (`figures/decision_matrix_scores.py`):**
  - Replaced mixed Hebrew+English `ROI` in Panel A's legend with pure Hebrew (`יעילות תקציבית והחזר (0.20)`) to eliminate BiDi reordering.
  - Lowered the stacked-bar label threshold to `0.58` so all weighted contributions display cleanly, and widened Panel B bar spacing (`w_bar = 0.27`, `width_ratios = [1.18, 1.12]`) so bar value labels never touch neighboring bars.
- **Page budget, BiDi & typography in `chapters/05-alternatives.tex`:**
  - Tightened prose repetition across Sections 5.1–5.4 to bring Chapter 5 from 11 pages to the exact **8-page budget** (pages 12–19 in the current skeleton) with balanced density, zero orphan headings, and zero `\draftnote{}` boxes.
  - Fixed Hebrew grammar (`גלגל התנופה`), narrowed Table 5.3 column widths to eliminate its `11.7pt` overfull warning, and removed `\mbox` around long English phrases to clear overfull `\hbox` lines.
