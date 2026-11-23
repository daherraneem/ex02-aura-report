# 25 – Reasons for the Open Items, then Submit

**Author:** Raneem · **Agent:** Claude Code · **Date:** 2026-11-23

## Prompt

```
Before committing, add a short reason to each item in "Left open at submission" in the README:
- LG-12: the Python graphs are in chapters 4-6 (market, decision matrix, Gantt), where the data is;
  chapters 1-3 are text and theory, so a graph there would be decoration.
- LG-13: remove page_budget.py from the build (it is not used in the report) - this one is now fixed.
- LG-02/03: the planning talk with Gemini happened in the browser; we saved its brief as the record,
  and the real prompts to the agents start at prompt 04.
- LG-15/LG-11: minor rule-file wording; the rules themselves were followed in practice (see prompts/).
- LG-16: the cover follows the course details given by the lecturer.
Then approved: commit, push, create and push the tag submission-ex02.
```

## What the agent did

- Ran `git pull` (up to date).
- Replaced the "Left open at submission" sentence in the README with a table: finding,
  decision and the reason given in the prompt for each item; LG-13 is marked fixed.
- LG-13: `figures/page_budget.py` and `figures/page_budget.pdf` were not used anywhere in the
  report; both were removed with `git rm` (the build runs every script in `figures/`, so this
  removes it from the build). Rebuilt: same 49 pages, 0 errors.
- Updated the Progress Log line of prompt 24 and the prompt range (01–25) in the README.
- Committed the submission (prompts 24 and 25 together), pushed, and created and pushed the
  tag `submission-ex02`.

## What was corrected

- Nothing.
