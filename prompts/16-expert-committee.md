# 16 – Expert Committee (Red Team) Review

**Author:** Raneem · **Agent:** Claude Code · **Date:** 2026-11-23

## Prompt

```
Run git pull. Now run an expert committee on the whole report, as in lecture 4 (multi-agent):
launch 5 separate subagents, each one an expert with its own role, reviewing main.pdf and the
chapter files as a RED TEAM - especially critical, thinking outside the box, no praise:
1. Marketing communications professor (content, theory, logic of the argument)
2. Brand strategist (AURA positioning, alternatives, realism of the plan)
3. Academic editor (structure by the booklet, consistency of numbers between chapters, Hebrew)
4. Design and LaTeX expert (layout, RTL/BiDi, figures, tables)
5. Lecturer grading this assignment (requirements of the lecture 4 summary, section 9)
Each subagent writes its findings to docs/committee/<role>.md (problem, where, concrete fix).
Then, as the lead, merge them into docs/committee/summary.md: a table of all findings -
agree / disagree - why - effort, and recommend the 5-8 fixes most worth doing.
Do not change the report yet. Save this prompt in prompts/. Then commit and push the committee files.
```

## What the agent did

- Ran `git pull` (up to date).
- Launched 5 independent subagents in parallel, one per role, each with its own brief:
  red team, no praise, findings as problem / where / concrete fix with severity, written to
  its own file in `docs/committee/`, no edits to the report, no quoting of the lecturer's
  copyrighted booklets (the committee files are committed).
- As the lead, merged the findings into `docs/committee/summary.md`.

- Result: 83 findings (11 critical, 42 major, 30 minor); the grading lecturer estimated
  84/100. `summary.md` gives a verdict for every finding (agree / partly / disagree /
  verify first), the reason, the effort, the owner under the ownership rule, and 8
  recommended fixes (F1–F8) with a suggested order.

## What was corrected

- The design/LaTeX subagent stalled after 10 minutes without writing anything; it was resumed
  with a lighter method (main.log first, PDF in batches of 8 pages, writing its file as it went).
- The academic-editor subagent ran for about 50 minutes without writing its file; the lead asked
  it to write its findings first and then finish its checks.
- The marketing professor said some of its points about the papers were recalled, not re-read
  (Evans et al., Miller & Kahn, Bawa & Shoemaker, an EU directive); the summary marks them
  "verify first" instead of accepting them.
- The committee files were checked for quotes from the lecturer's copyrighted booklets before
  the commit: they refer to them by section only.
- The report itself was not changed, as the prompt asked.
