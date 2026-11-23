# 13 – Chapter 7: Risk Management

**Author:** Raghad · **Agent:** Antigravity · **Date:** 2026-11-23

## Prompt

```
Run git pull. Write my chapter chapters/07-risks.tex (Risk management, 2 pages) in Hebrew,
following the booklet (chapter 9): 6-8 real risks of the AURA launch, each with probability
and impact (1-5) and R = P x I, a colored risk matrix (TikZ), and a mitigation plan for every
risk with R >= 12. Link the risks to the goals and requirements of chapter 2 and the work
plan of chapter 6. Real sources only. Remove the draft boxes.
Run .\build.ps1, fix errors, show me. Do not commit yet.
```

## What the agent did

- Ran `git pull` (up to date at `ef48fe6`) and verified official ISO/IEC risk-management standards via web search, appending `iso2018risk` (ISO 31000:2018) and `iec2019risk` (IEC 31010:2019) to `references.bib` without editing existing entries.
- Created `figures/tikz/risk_matrix.tex`: a colored $5 \times 5$ TikZ risk matrix ($P \times I$) in AURA's palette plotting all 7 risks (`R1`–`R7`), with a dashed boundary around the mandatory $R \geq 12$ mitigation zone and a full Hebrew legend.
- Wrote `chapters/07-risks.tex` in Hebrew (2 pages, removing all `\draftnote{}` boxes):
  - Risk register (`Table 7.1`) of 7 real AURA launch risks (`R1`–`R7`) with $P$, $I$, $R = P \times I$, and explicit links to Chapter 2's goals/requirements (`G1`–`G5`, `REQ-01`–`REQ-11`) and Chapter 6's WBS/Critical Path (`WP1`–`WP6`, `M3`, `M4`).
  - Colored $5 \times 5$ TikZ risk matrix (`Figure 7.1`).
  - Mitigation, contingency, and residual-risk table (`Table 7.2`) for all 5 risks with $R \geq 12$ (`R1=16`, `R2=16`, `R3=15`, `R4=12`, `R5=12`), reducing maximum risk exposure to `6` and critical-path regulatory risk (`R3`) from `15` to `4`.
- Built with `.\build.ps1` and inspected `main.log`, `main.blg`, and rendered PNG pages of Chapter 7.

## What was corrected

Found by compiling and visually inspecting `risk_matrix.tex` and both rendered pages of Chapter 7 (exact pp. 35–36):

- **Compile error on first pass:** `\textenglish{R}` inside math mode (`$\textenglish{R} \geq \LR{12}$`) in `figures/tikz/risk_matrix.tex` triggered `\sffamily invalid in math mode`. Fixed by using pure math mode (`$R \geq 12$` and `$R = P \times I$`).
- **BiDi & consistency polish in `chapters/07-risks.tex`:**
  - Replaced `CPA` with `\en{CAC}` in Table 7.2 for terminology consistency with `00-abbreviations.tex` and Chapters 5–6.
  - Replaced `תקציב \ltr{150}K` in Table 7.1 with `תקציב \ltr{150} אלף ש"ח` so `K` never detaches in RTL, and wrapped `\mbox{\en{G1--G5}}` so the goal range stays on one line.
- **Page budget:** Hit the exact **2-page budget** (`pp. 35–36` of `main.pdf`, 50 pages total, 0 compile errors, 0 Biber warnings, 0 `\draftnote{}` left).
