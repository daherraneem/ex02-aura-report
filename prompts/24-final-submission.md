# 24 – Final Submission

**Author:** Raneem · **Agent:** Claude Code · **Date:** 2026-11-23

## Prompt

```
Run git pull to get Raghad's last fixes (keep both sides if there is a conflict). Then finalize for submission:
1. Cover: each student's Hebrew name directly under her own English name:
   Raneem Daher / רנים דאהר, Raghad Rabah / רגאד רבאח. No ID numbers anywhere in the repo.
2. Full build: 0 errors, no draft boxes, and check every page visually.
3. Add the final PDF to the repo as report/rr-mkcom-ex02-report.pdf (on purpose, for the grader).
4. Screenshots in assets/screenshots/: the cover, one chapter opener, one page with a Python
   graph, one TikZ diagram, and the risk matrix.
5. README.md, professional, in English: at the top a "Final Submission" section with a link to the PDF;
   then the project in short, team and chapter split, how to build, the screenshots, the multi-agent
   expert committee (what it found, what we fixed, what we chose not to fix and why), and the Progress Log.
6. Check the prompts/ folder: continuous numbering with no gaps, no empty prompt files.
   Fix numbering only by renaming, and update links to them.
Then follow the push rules and push, and create the git tag submission-ex02 and push it.
```

## What the agent did

- `git pull`: Raghad's commit `e99f082` (chapters 4–7 and TikZ fixes) was already in; no conflict.
- **Cover:** new class command `\addauthor{en}{he}` (`aura-report.cls` v0.3, changelog line),
  one column per student with the Hebrew name under the English name; `main.tex` uses it with
  the spellings from the prompt. `tests/bidi-test.tex` still compiles.
- **ID numbers:** searched all tracked files and the git history; none found (only DOIs).
- **Build and page check:** full build, then every page of `main.pdf` rendered and checked.
  Found 10 amounts in chapter 5 (Raghad's file) written as `\ltr{43}K`, which printed reversed
  ("K43", "K75.2-"). Raneem confirmed that Raghad approved this fix, so the agent moved the K
  inside `\ltr{}` (the same fix Raghad made in chapters 4, 6 and 7). Final build: 49 pages,
  0 errors, 0 overfull lines, no undefined references, no draft boxes.
- **PDF and screenshots:** `report/rr-mkcom-ex02-report.pdf`; five PNGs in `assets/screenshots/`
  (cover, chapter 3 opener, Fig. 4.1, Fig. 5.2, risk matrix Fig. 7.1).
- **README:** rewritten in English with the requested sections; the Progress Log was kept word
  for word, with a new line for this prompt.
- **Prompt log:** 01–24, continuous, no gaps, no empty files; no renames needed, so no links
  changed.
- Committed after Raneem's approval, pushed, and created and pushed the tag `submission-ex02`.

## What was corrected

- The first attempt at the chapter 5 fix used `sed` in Git Bash, which read `\l` in the
  replacement as "lowercase" and wrote `\tr{`; the build failed. The file was restored from git
  and the fix was redone with a Python script.
- The references end with two lines of entry [58] alone on page 42; left as is (cosmetic).
