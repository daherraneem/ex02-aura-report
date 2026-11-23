# ex02-aura-report

**Course:** AI Agents & Vibe Coding (יישומי Vibe Coding ו-AI במדע וביום-יום)
**University:** University of Haifa · **Lecturer:** Dr. Yoram Segal
**Assignment:** Exercise 2 – Preparatory Report (דוח מכין)
**Team:** Raneem Daher (Claude Code) & Raghad Rabah (Antigravity)
**Status:** Project setup – LaTeX skeleton compiles; chapters not written yet

## The project

A ~40-page preparatory report in Hebrew, written in LaTeX, for the launch of **AURA**,
our fictional food-inspired lip tint brand from Exercise 1. Its structure follows the
page map in the lecturer's booklet (front matter + 8 chapters + references).

| Part | File | Pages | Owner |
|---|---|---|---|
| Cover, executive summary, TOC, lists, abbreviations | `main.tex`, `chapters/00-*.tex` | front matter (א–ד) | Shared |
| 1. Introduction and background | `chapters/01-intro.tex` | 3 | Raneem |
| 2. Problem and goals | `chapters/02-problem.tex` | 4 | Raneem |
| 3. Literature and flagship paper | `chapters/03-literature.tex` | 9 | Raneem |
| 4. Market research | `chapters/04-market.tex` | 6 | Raghad |
| 5. Launch alternatives | `chapters/05-alternatives.tex` | 8 | Raghad |
| 6. Work plan | `chapters/06-workplan.tex` | 4 | Raghad |
| 7. Risk management | `chapters/07-risks.tex` | 2 | Raghad |
| 8. Summary | `chapters/08-summary.tex` | 1 | Raneem |
| References (IEEE) | `references.bib` | 3 | Shared |

## Project structure

| Path | Purpose |
|---|---|
| `main.tex` | Main file: report details, order of the chapters |
| `aura-report.cls` | Our own class: AURA colors, cover, headings, boxes, tables, BiDi commands. The command list and changelog are at the top |
| `chapters/` | One `.tex` file per chapter |
| `figures/` | Python graph scripts (`*.py` → `*.pdf`), `aura_style.py` (shared colors and fonts) |
| `figures/tikz/` | TikZ diagrams |
| `references.bib` | Bibliography (biber, IEEE style) |
| `tests/bidi-test.tex` | One-page Hebrew/English stress test for the class |
| `prompts/` | Every prompt we wrote, word for word, with notes |
| `docs/` | Lecturer's booklet and lecture 4 summary – local only, git-ignored (copyright) |
| `CLAUDE.md`, `AGENTS.md` | Working rules for Claude Code and Antigravity (same rules) |

## How to compile

Requirements: **MiKTeX** (XeLaTeX + biber; missing packages install on the fly),
**Python 3** with **matplotlib**. Fonts: David, Gisha, Cambria, Calibri and Georgia,
which all ship with Windows.

```powershell
.\build.ps1          # full build: Python figures -> xelatex -> biber -> xelatex x2
.\build.ps1 -Quick   # one xelatex pass (text changes only)
```

Manual build:

```powershell
python figures/page_budget.py
xelatex main.tex
biber main
xelatex main.tex
xelatex main.tex
```

Class test page: `xelatex -output-directory=tests tests/bidi-test.tex`

## Progress Log

- **2026-11-22** – Project setup: copied the lecturer's booklet and lecture 4 summary to `docs/` (git-ignored); added `CLAUDE.md` and `AGENTS.md` with the team rules; built the XeLaTeX skeleton: `aura-report.cls` v0.1 (AURA cover, chapter openers in the five shade colors, boxes, tables, BiDi commands), `main.tex`, 8 chapter files + front matter following the booklet's page map, `references.bib`, a Python figure and a TikZ diagram, the `build.ps1` script and a BiDi test page. Prompt saved in `prompts/01-project-setup.md` (Raneem).
- **2026-11-22** – Chapter split: Raneem owns chapters 1, 2, 3 and 8, Raghad owns chapters 4, 5, 6 and 7, and the front matter and `references.bib` are shared. Added a rule to `CLAUDE.md` and `AGENTS.md`: every fact, number and paper must come from a real source found by web search and cited in `references.bib`. Prompt saved in `prompts/02-chapter-split.md` (Raneem).
- **2026-11-22** – Chapter 4 (Market research, 6 pages): saved Gemini planning brief (`prompts/03-gemini-consult.md`), wrote `chapters/04-market.tex` in Hebrew with TAM/SAM/SOM analysis, verified 5-competitor comparison table and Masstige positioning index, added 20 verified web sources to `references.bib` and `D2C` to `chapters/00-abbreviations.tex`, generated two AURA-styled Python figures (`figures/market_growth_tam_sam_som.py`, `figures/price_positioning.py`), and verified clean build (`main.pdf`, 25 pages, 0 errors). Prompt saved in `prompts/04-market-chapter.md` (Raghad).
- **2026-11-23** – Chapter 1 (Introduction, 3 pages): wrote `chapters/01-intro.tex` in Hebrew as the booklet's funnel (global trends → Israeli context → why existing launch approaches fall short → report structure), reusing chapter 4's market numbers and sources; added 5 verified web sources to `references.bib`; widened the roadmap boxes in `figures/tikz/roadmap.tex`; removed the chapter's draft boxes. Clean build (`main.pdf`, 26 pages, 0 errors). Prompts saved in `prompts/05-status-check.md` and `prompts/06-intro-chapter.md` (Raneem).
- **2026-11-23** – Chapter 5 (Launch alternatives, 8 pages): wrote `chapters/05-alternatives.tex` in Hebrew covering three distinct launch alternatives, a 6-criterion weighted decision matrix with 4-scenario sensitivity analysis (`figures/decision_matrix_scores.py`), a 4-layer TikZ launch architecture diagram (`figures/tikz/launch_architecture.tex`), and AURA's two-stage phygital innovation (*The AURA Tasting Bar* & *AI Flavor-Sommelier*); added 10 verified sources to `references.bib` and 8 abbreviations to `chapters/00-abbreviations.tex`. Prompt saved in `prompts/07-alternatives-chapter.md` (Raghad).
