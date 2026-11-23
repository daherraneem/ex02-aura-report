# Prompt 23 – Open items from `docs/committee/raghad-todo.md`

- **Date:** 2026-11-23
- **Author:** Raghad Rabah
- **Tool:** Antigravity

## Prompt sent (verbatim)

```text
Run git pull. Fix the open items in docs/committee/raghad-todo.md in my chapters:
chapter 4 back to about 6 pages, mention the control campus in chapter 6,
fix the overfull lines in chapter 7, use the class macros (\en, \ltr) in my TikZ files,
and fix any number mismatch listed there.
Build and check, then commit. Do not push - I will push from GitHub Desktop.
```

## What was done

1. Pulled latest `origin/main` (`97591be`) and reviewed `docs/committee/raghad-todo.md` (confirming zero number mismatches in Chapters 4–7 against `docs/committee/numbers.md`).
2. **Chapter 4 (`chapters/04-market.tex`):** fixed the wording typo on line 87 (`וריבועי` → `ורבעוני`) and tightened prose, table spacing, and figure widths (`0.80\linewidth` / `0.72\linewidth`) while keeping all 8 competitors, all sources, equations, and `\footnotesize` minimum table font, bringing Chapter 4 back to 6 pages.
3. **Chapter 6 (`chapters/06-workplan.tex` + `figures/tikz/wbs_tree.tex`):** added the control campus (and foil brand, aligned with Chapter 2 `REQ-09` and `G1`) to `WP3`/`M3`, `WP6`/`M6`, Table 6.2 (`RACI`), and `wbs_tree.tex`, and explicitly broke out the two-wave pilot+control survey budget (`5K` ILS: `2.5K` in `WP3` + `2.5K` in `WP6`) inside the existing `35K` paid-media & surveys bucket (`30K` paid media + `5K` surveys; total `150K` unchanged).
4. **Chapter 7 (`chapters/07-risks.tex`):** adjusted column widths in Table 7.1 and Table 7.2 to clear both overfull `\hbox` warnings while keeping Chapter 7 on 2 pages.
5. **TikZ class macros (`LG-14`):** replaced all raw `\textenglish{...}` / `\LR{...}` calls with class macros `\en{...}` / `\ltr{...}` in `figures/tikz/launch_architecture.tex`, `figures/tikz/wbs_tree.tex`, and `figures/tikz/risk_matrix.tex`.

## What was verified / corrected

- First rebuild brought Chapter 4 back to 6 pages (pp. 17–22), but adding the control-campus details pushed Chapter 6 to 5 pages (pp. 31–35), and `main.log` revealed that both Chapter 7 overfull lines (`07-risks.tex:34` and `71`) were caused by column 1 (`\hcell{מזהה}`) needing `p{0.92cm}`.
- Widened column 1 to `p{0.92cm}` in Tables 7.1 and 7.2 (clearing all overfull `\hbox` warnings across the entire 49-page report to **0**), and tightened Table 6.1/6.2/6.3 vertical spacing + Gantt width (`0.94\linewidth`) to bring Chapter 6 back to **exact 4 pages** (pp. 31–34).
- Visual PNG inspection of all three TikZ figures (`launch_architecture.tex`, `wbs_tree.tex`, `risk_matrix.tex`) confirmed that class macros `\en` and `\ltr` work cleanly inside `\texthebrew{...}` TikZ nodes with no BiDi or font regressions.
- Visual inspection also caught two polish issues and fixed them: (1) Figure 4.2 had floated alone onto page 22 after the `keymessage` box — added `\clearpage` before Figure 4.2 so page 22 displays Figure 4.2, the concluding analysis, and the `keymessage` box together; (2) `\ltr{...}K` rendered as `K150` / `K)30–5)` in BiDi — moved `K` inside `\ltr{...}` (`\ltr{150K}`, `\ltr{5--30K}`, etc.) across Chapters 4, 6, 7 and `launch_architecture.tex`.
- Final clean build: `main.pdf`, **49 pages** (body pp. 1–37 matching the booklet page map: Ch. 4 = 6 pp., Ch. 5 = 8 pp., Ch. 6 = 4 pp., Ch. 7 = 2 pp.; references pp. 38–42), **0 errors**, **0 Biber warnings**, **0 overfull lines**.
