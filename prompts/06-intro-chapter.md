# 06 – Chapter 1: Introduction

**Author:** Raneem · **Agent:** Claude Code · **Date:** 2026-11-23

## Prompt

```
Yes, log the status prompt in prompts/. Then rebuild with .\build.ps1.

Write my chapter chapters/01-intro.tex (Introduction, 3 pages) in Hebrew.
Our project: a 6-month launch plan for AURA in Israel - women aged 18-28,
via TikTok and Instagram, micro-influencers and campus tasting pop-ups;
goal: build awareness and first sales in a crowded beauty market.
Follow the booklet's funnel (chapter 3): global trends (food-inspired beauty,
social commerce, Gen Z) -> the Israeli context -> why existing approaches are not
enough -> the structure of the report. Keep the roadmap figure.
Stay consistent with Raghad's chapter 4 (same market numbers and sources where relevant).
Real sources only, from web search, in references.bib.
Remove the draft boxes of this chapter. Build and show me the chapter pages.
Do not push yet.
```

## What the agent did

- Ran `git pull` (up to date) and saved the previous prompt as `prompts/05-status-check.md`.
- Read the booklet's chapter 3 (the introduction as a funnel: trends → application
  context → motivation → structure, plus an "in your project" box) and Raghad's chapter 4.
- Wrote `chapters/01-intro.tex` in four sections following the funnel:
  1.1 global trends (food-inspired beauty, social commerce and Gen Z),
  1.2 the Israeli context, 1.3 why existing launch approaches are not enough
  (shelf only, paid/celebrity ads, online only), 1.4 the structure of the report,
  with the roadmap figure and an "in our project" insight box. All `\draftnote` boxes removed.
- The Israeli numbers reuse Raghad's sources and values exactly (`mordor2026israel`,
  `datareportal2026israel`, `che2026students`, `cbs2024students`, competitor prices).
- Added 5 new sources to `references.bib` (add-only, own section), each opened and checked:
  Glossy (Jensen 2025), Personal Care Insights (Waldeck 2026; Meintjes 2025, Kyra survey),
  HypeAuditor State of Influencer Marketing 2025, Cosmetics Business 2021 (Odore sampling study).
- Build: 0 errors; chapter 1 is exactly pp. 1–3.

## What was corrected

- Sources that could not be opened (McKinsey State of Beauty: timeout; eMarketer, Business
  of Fashion, Vogue HK: 403) were **not** used.
- HypeAuditor's page has inconsistent TikTok figures (87.7% / 10.3% vs. 87% / 11.9%), so
  only the Instagram figure (76% nano-influencers) is cited.
- `\en{Z}` in a section title broke the build (hyperref PDF bookmark): the title was
  reworded without English.
- Page 2 was half empty: with ragged-bottom pages LaTeX preferred breaking before §1.3,
  because the unbreakable insight box did not fit. The box was moved after the
  report-structure paragraph (where the booklet puts it).
- Two overfull lines were fixed by rewording (one of 1.2 pt remains, invisible).
- Roadmap (`figures/tikz/roadmap.tex`): the "ספרות ומאמר דגל" label wrapped to 3 lines and
  hit the number circle; the boxes were widened slightly.
- The page-budget figure (`fig:page-budget`) was removed from chapter 1 to keep the
  chapter at 3 pages; `figures/page_budget.py` is still in the repo.
