# 02 – Chapter Split and Sources Rule

**Author:** Raneem · **Agent:** Claude Code · **Date:** 2026-11-22

## Prompt

```
Use this chapter split in CLAUDE.md, AGENTS.md and the chapter files:
Raneem: 01-intro, 02-problem, 03-literature, 08-summary.
Raghad: 04-market, 05-alternatives, 06-workplan, 07-risks.
Shared: front matter, references.bib, abbreviations.
Also add this rule to both files: every fact, number and paper must come from a real,
checkable source found by web search and cited in references.bib - never invent sources.
Then commit and push.
```

## What the agent did

- Filled the ownership table in `CLAUDE.md` and `AGENTS.md`:
  - Raneem: chapters 1, 2, 3 and 8 (17 pages);
  - Raghad: chapters 4, 5, 6 and 7 (20 pages);
  - shared: the front matter (`00-abstract`, `00-abbreviations`) and `references.bib`.
- Set the `Owner:` line in the header comment of every chapter file.
- Added the sources rule to both files. The rule was made concrete: every entry needs a
  DOI or a working URL, and a fact with no verified source is left out (no citing from
  memory).
- Added an owner column to the chapter table in `README.md` and a Progress Log line.
- Rebuilt the PDF to check that nothing broke, then committed and pushed the setup
  (prompt 01) and this change, after the user's approval in this prompt.

## What was corrected

- Nothing was corrected. `AGENTS.md` was regenerated from `CLAUDE.md`, so the two files
  differ only in the title line and the line that names the other file.
