# 12 – Chapter 6: Work Plan

**Author:** Raghad · **Agent:** Antigravity · **Date:** 2026-11-23

## Prompt

```
Run git pull. Write my chapter chapters/06-workplan.tex (Work plan, 4 pages) in Hebrew,
following the booklet (chapter 8): a WBS diagram (TikZ), a RACI table, and a Gantt chart
for the 6-month launch with milestones. Use the chosen alternative of chapter 5 and the
numbers of chapter 2: 3 campus tasting bars, 20-30 creators, budget of about 150K NIS
(add a short budget table). Real sources only. Remove the draft boxes.
Run .\build.ps1, fix errors, show me. Do not commit yet.
```

## What the agent did

- Ran `git pull` (up to date at `335688d`) and read `chapters/02-problem.tex`, `chapters/06-workplan.tex`, `chapters/00-abbreviations.tex`, and `references.bib` to align every deliverable, requirement (`REQ-01`–`REQ-09`), goal (`G1`–`G5`), and budget figure (`150`K ILS) with Chapters 2, 4, and 5.
- Verified 3 canonical project-management sources via web search and appended them to `references.bib` without modifying existing entries: PMI *PMBOK Guide* 7th ed. (2021, ISBN `978-1628256642`), Kerzner 13th ed. (2022, ISBN `978-1119805373`), and Kelley & Walker (1959, DOI `10.1145/1460299.1460318`). Added `CPM` alphabetically to `chapters/00-abbreviations.tex`.
- Created two figures matching AURA's visual identity:
  - `figures/tikz/wbs_tree.tex` — 6-package TikZ WBS tree diagram (`WP1`–`WP6`) with 3 deliverables per package and strict BiDi separation.
  - `figures/gantt_launch.py` → `figures/gantt_launch.pdf` — 6-month Python Gantt chart showing 11 core tasks, highlighted Critical Path (`REQ-01` → `M3` Go/No-Go → `Go-Live` → Optimization → Retention & ROI), and milestones `M1`–`M6`.
- Wrote `chapters/06-workplan.tex` in Hebrew (removing all `\draftnote{}` boxes) with WBS + budget table (`150`K ILS across `WP1`–`WP6`), RACI table (5 roles, single `A` per row), Gantt chart, milestones verification table (`M1`–`M6`), critical-path analysis, and handoff to Chapter 7.
- Compiled with `.\build.ps1` and inspected `main.log`, `main.blg`, and rendered PNG images of every page of Chapter 6.

## What was corrected

Found by compiling and visually inspecting `gantt_launch.pdf`, `wbs_tree.tex`, and all 4 rendered pages of Chapter 6 (exact pp. 31–34):

- **Python Gantt chart (`figures/gantt_launch.py`):** Replaced mixed trailing English `UGC (G2)` on task `5.1` with `תוכן גולשות (G2)` so BiDi ordering is 100% clean across all 11 task labels.
- **BiDi & overfull fixes in `chapters/06-workplan.tex`:**
  - Merged the four English RACI terms into a single `\en{Responsible, Accountable, Consulted, Informed}` phrase (per `AGENTS.md`), fixing LTR word order and clearing a `31pt` overfull `\hbox`.
  - Wrapped `\mbox{\en{WP1--WP6}}` so the range never breaks awkwardly across lines.
  - Narrowed Table 6.2 (`tab:raci`) first column from `4.9cm` to `4.3cm` (`\tabcolsep = 4pt`) and broke bold formatting cleanly in the Critical Path paragraph to eliminate the remaining `11pt` overfull warnings.
- **Page budget:** Hit the exact **4-page budget** (`pp. 31–34` of `main.pdf`, 49 pages total, 0 compile errors, 0 Biber warnings, 0 `\draftnote{}` left).
