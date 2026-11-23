# 08 – Push Chapter 1, Write Chapter 2: Problem and Goals

**Author:** Raneem · **Agent:** Claude Code · **Date:** 2026-11-23

## Prompt

```
Approved. Do not commit the regenerated figure PDFs (git checkout figures/*.pdf),
then follow the push rules and push.

After the push, run git pull and write my chapter chapters/02-problem.tex
(Problem and goals, 4 pages) in Hebrew, following the booklet (chapter 4):
- A quantified problem statement: why a new brand like AURA struggles to be noticed
  (use the numbers from chapters 1 and 4).
- The research question vs SMART design goals for the 6-month launch.
- A requirements table for the launch (must / should / could), with measurable targets.
Stay consistent with chapters 1 and 4. Real sources only. Remove the draft boxes.
Build and show me the chapter pages. Do not push chapter 2 yet.
```

## What the agent did

- Discarded the regenerated figure PDFs, added the Progress Log line to `README.md`, and
  committed and pushed Chapter 1 (`02d5244`).
- Ran `git pull` (up to date) and read the booklet's chapter 4 (current state → gap →
  question / measurable goal → requirements; research vs design projects; requirements
  table with ID, target and verification; an "in your project" box).
- Wrote `chapters/02-problem.tex` (4 pages, pp. 4–7):
  - 2.1 quantified problem: current state, and a gap in three parts (visibility, trial,
    price) using the numbers of chapters 1 and 4; current-vs-desired table; a one-sentence
    problem statement;
  - 2.2 a guiding question vs 5 SMART design goals (G1–G5), using Doran's original letters;
  - 2.3 an 11-line requirements table (REQ-01–REQ-11, must / should / could, target,
    verification) and the time, regulation and budget constraints.
- New TikZ diagram `figures/tikz/problem-chain.tex` (the booklet's figure 4.1, in AURA style).
- `references.bib`: added the URL of a checked scan of Doran (1981) to the existing entry
  (author, title and "November 1981, p. 35" read from the scan), and 2 new sources: the
  U.S. International Trade Administration on Israel's cosmetics import reform, and Pearl
  Cohen (2021) on the Attorney General's position on influencer ad disclosure.
- `00-abbreviations.tex`: added SMART and UGC (add-only).
- Build: 0 errors, 0 undefined references.

## What was corrected

- gov.il pages (Ministry of Health notification process) could not be opened (403), so the
  "approval within 6 months" detail is not used; REQ-01 says "valid notification" and is
  backed by the trade.gov page only.
- Goal values (G1–G3, G5) are marked in the text as the team's planning targets; only G4
  comes from chapter 4's SOM estimate.
- An overfull line (25 pt) was fixed by moving the Doran citation.
- The requirements table first landed above its own section heading; it is now after its
  introduction paragraph, on its own page (p. 7).
- Before the push (next prompt): pulled Raghad's chapter 5. This prompt file was renumbered
  from 07 to 08 because her chapter 5 prompt took 07. Conflicts were resolved keeping both
  sides: `references.bib` (her chapter 5 entries + my chapter 2 entries) and
  `00-abbreviations.tex` (UGC was added by both; her line was kept, mine dropped).
- Chapter 2 was aligned with chapter 5's chosen hybrid alternative: 3 campus tasting bars in
  months 4–5 (was 6 campuses), 3,000 samples, 20–30 creators with 5K–30K followers,
  sales across D2C + marketplace + pop-ups, the 299 ₪ bundle on D2C only, and the
  ~150K ₪ budget.
