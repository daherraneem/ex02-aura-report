# 01 – Project Setup

**Author:** Raneem · **Agent:** Claude Code · **Date:** 2026-11-22

## Prompt

```
We are starting Exercise 2 of the course "AI Agents & Vibe Coding": a ~40-page preparatory report
(דוח מכין) in Hebrew, written in LaTeX. Team: Raneem Daher (Claude Code) and Raghad Rabah (Antigravity).
Our project: the launch of AURA, our fictional food-inspired lip tint brand from Exercise 1.

Set up the project:
1. Copy the lecturer's files from my Downloads folder into docs/: the preparation report booklet
   (preparation-report-book) and the lecture 4 summary (l04-summary). Add both to .gitignore -
   they are the lecturer's copyrighted files. Read them; they define the report structure.
2. Create CLAUDE.md and AGENTS.md (same rules, for Claude and for Antigravity):
   - Always run "git pull" before starting work. Never force push.
   - Save every prompt the user writes, word for word, in prompts/NN-short-name.md
     (continuous numbering, no gaps), with a short note on what the agent did and what was corrected.
   - Before every push: show a summary and wait for approval; commit message = short title +
     2-3 lines (what, why, critical or minor); add a line to the Progress Log in README.md.
   - Each partner edits only her own chapter files.
3. Build the LaTeX skeleton, compiled with XeLaTeX, Hebrew RTL with correct BiDi:
   - main.tex + our own class file aura-report.cls (original design in AURA colors, not a default look).
   - chapters/ with one .tex file per chapter, following the booklet's page map (intro, problem,
     literature, market, alternatives, work plan, risks, summary) + front matter and references.bib.
   - figures/ for Python graph scripts and TikZ diagrams.
   - Use a Hebrew font that exists on Windows. Compile and fix errors until a PDF is produced.
4. README.md: course, exercise, team, how to compile, and a Progress Log.
Save this prompt as prompts/01-project-setup.md.
Before pushing: show me a summary and the compiled PDF, and wait for my approval.
```

## What the agent did

- Copied `preparation-report-book.pdf` and `l04-summary.pdf` into `docs/` and git-ignored
  them. Downloads had 3 copies of the booklet and 2 of the summary; their checksums were
  identical, so one copy of each was taken.
- Read both files. Structure source: the page map (booklet, table 1.1): front matter
  (א–ד), intro 3, problem 4, literature 9, market 6, alternatives 8, plan 4, risks 2,
  summary 1, references 3 = 40 pages. The formatting rules (table 11.1) and the BiDi and
  CLS rules (chapters 14–15) went into the class and into `CLAUDE.md`/`AGENTS.md`.
- Built `aura-report.cls` v0.1:
  - XeLaTeX with polyglossia/bidi; David for Hebrew body text, Gisha for headings, Cambria for English;
  - 12 pt, 1.5 spacing, 2.5 cm margins + 0.5 cm binding;
  - AURA palette from Exercise 1, and each chapter opener uses one of the five shade colors;
  - a cover with the five "aura" glows;
  - four box types, styled tables, `\en` / `\ltr` / `\mathheb`, a `diagram` environment, and an IEEE bibliography;
  - Hebrew-letter page numbers in the front matter, and "page X of Y" in the body.
- Created `main.tex` and the chapter files, with the booklet's sections adapted to a brand
  launch and a `\draftnote` stating what each section must prove. Also created
  `references.bib`, a Python figure (`figures/page_budget.py`) and a TikZ diagram
  (`figures/tikz/roadmap.tex`).
- Created `build.ps1`, a one-page BiDi stress test (`tests/bidi-test.tex`, booklet
  Prompt B4), `CLAUDE.md`, `AGENTS.md` and `README.md`.
- Result: `main.pdf`, 18 pages (skeleton), 0 errors.

## What was corrected

Found by compiling and looking at every page as an image:

- Compile errors:
  - `\par` inside a titlesec argument (moved into a macro);
  - biblatex must load after polyglossia, while hyperref must load before it.
- David has no italic (a fake slant was added). The header height was too small.
- The header rule showed on chapter-opening and front-matter pages; the TOC used the 1.5 body spacing.
- Cover: the glows had hard edges (changed to soft fading), and the title broke in the middle of a phrase.
- Python chart: the Hebrew was reversed. matplotlib 3.11 already handles BiDi (libraqm),
  so `heb()` now reorders text only on older versions.
- Found by the BiDi test page:
  - `--` printed as two hyphens in Hebrew text (TeX ligatures added to the Hebrew fonts);
  - mirrored brackets in a formula with Hebrew;
  - Hebrew left-aligned in `l` table columns (rule: use `r` / `p{}`);
  - a paragraph that starts with `\en{}` flipped to LTR (fixed with `\leavevmode` in `\en` / `\ltr`);
  - the keymessage box turned LTR (the title is no longer attached to the text);
  - a space before every colon ("התאריך :"). David's colon glyph has a wide side
    bearing, so a kern was added in the class, for David only.
- Open: chapter owners are not assigned yet ("to be assigned" in `CLAUDE.md`/`AGENTS.md`).
