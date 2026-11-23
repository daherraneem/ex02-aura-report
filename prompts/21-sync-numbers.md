# 21 – Sync the Agreed Numbers

**Author:** Raneem · **Agent:** Claude Code · **Date:** 2026-11-23

## Prompt

```
Run git pull to get Raghad's fixes (keep both sides if there is a conflict).
Read docs/committee/numbers.md - the agreed numbers after the committee
(sales target ~2,200 units / ~150K NIS gross in months 4-6, budget, break-even).
Update my files to match exactly: chapter 2 (goal G4, tables, problem statement),
chapter 8 (summary) and the executive summary. Then check that the sales target,
budget and break-even numbers are the same in every chapter of the report,
and list any mismatch in Raghad's chapters in docs/committee/raghad-todo.md.
Build and check, then follow the push rules and push.
```

## What the agent did

- `git pull`: already up to date (no new commits from Raghad), so there was nothing to merge.
- Read `docs/committee/numbers.md` and replaced the old target (255K ₪ / ~3,700 units) with
  the base case: **~2,200 units / ~150K ₪ gross (~127K net) in months 4–6**.
  - `02-problem.tex`: problem text (adds break-even 4,412 units in months 9–10), current-vs-
    desired table, problem statement box, guiding question, G4 row, and the sentence on where
    G4 comes from (base case of the ch. 5 funnel, ~30% of the ch. 4 SOM).
  - `08-summary.tex`: new target and break-even.
  - `00-abstract.tex` (shared): new target and break-even (285 words, within 250–350).
- Checked the sales target, budget and break-even in every chapter, the TikZ files and the
  Python figures: chapters 4–7 match `numbers.md` (WP1–WP6 add up to 150K, 100%). No number
  mismatches; one optional wording question in ch. 4 was added to `raghad-todo.md` (§1a).
- Build: 0 errors, no undefined references, `main.pdf` 50 pages. The only overfull lines left
  are the two in `07-risks.tex` already on Raghad's list.

## What was corrected

- The new break-even sentence pushed the summary's final box onto a second page (51 pages).
  The agent shortened the first paragraph of ch. 8 (removed the list of channels, which is
  repeated in the next steps), and the summary fits on one page again.
- Two small overfull lines in ch. 2 (from before this prompt) were fixed: the id column of the
  SMART table was widened, and "עם אחריות מוגדרת" became "בעלי אחראי מוגדר".
