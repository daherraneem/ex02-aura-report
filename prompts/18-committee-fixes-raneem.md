# 18 – Apply Committee Fixes F3, F2, F6/F7 (Raneem's files)

**Author:** Raneem · **Agent:** Claude Code · **Date:** 2026-11-23

## Prompt

```
Run git pull. Implement these fixes from docs/committee/summary.md, after the expert committee:
- F3 (class and layout: aura-report.cls, main.tex, compact bibliography 3-4 pages, lists in contents, table/figure sizes)
- F2 (honest measurement, in my chapters 2 and 3)
- The parts of F6 and F7 that are in my files (chapters 01, 02, 03, 08 and the abstract).
Do NOT edit Raghad's chapters 04-07: write any issues there in docs/committee/raghad-todo.md.
Do NOT change the sales numbers yet (F1 waits for Raghad).
Build and check, then follow the push rules and push (mention "after expert committee" in the commit).
```

## What the agent did

- **F3, class `aura-report.cls` v0.2** (shared file, changelog line added):
  - `\en` / `\ltr` made robust → the lists of figures/tables keep their spaces (DL-01, AE-20);
  - no hyphenation inside `\en` (DL-03); `\emergencystretch=1.5em`;
  - lists of figures and tables added to the TOC, with the right page; wider number box (DL-09);
  - compact bibliography: single spacing, `\small`, ragged right, URL breaks, and the year
    printed for `@online` entries (DL-02, LG-04, AE-05, AE-06) — references went from 6 to 4
    pages (5 after Raghad's new sources);
  - `\sep` keeps the bullet with the previous keyword (DL-17);
  - tighter, ragged abbreviations table (it overflowed after the list grew).
  - `tests/bidi-test.tex` recompiled after the class change: correct.
- **F2, chapters 2–3:** a control campus (online content, no tasting bar) and baseline/endline
  surveys with a foil brand (REQ-09); G1 measured against the control campus; G5 presented as
  gross trial-to-purchase conversion; the flagship measurement table rebuilt (net effect vs
  control, A not measurable in the 6-month window); the literature-matrix project row changed
  to "planned measurement"; the gap reframed (lab → real launch, and the combination) with an
  explicit working hypothesis; claims limited to the papers' scope (Elder & Krishna = food ads;
  the naming effect supported by Skorinko, not by Miller & Kahn; Leung remedy and creator-size
  assumption labelled as the team's).
- **F6/F7 in Raneem's files:** one name for the campus activity ("בר טעימות"), two trends
  (not three), the Kyra survey marked as non-Israeli, the Instagram age base, one wording of
  the Odore sampling survey, the ch. 1 roadmap sentence, students as the first segment, the
  flagship author list in one `\en{}`, "seven principles", a sample defined in REQ-08.
- Pulled Raghad's commit `2a88450` (her fixes for ch. 4–7, new numbers in
  `docs/committee/numbers.md`) and synced the non-sales numbers in Raneem's files: 1,500
  samples, decision score 7.65, eight risks, residual 16 → 9.
- Wrote `docs/committee/raghad-todo.md` with the items still open in chapters 4–7.
- Build: 0 errors, 0 undefined references, 0 biber warnings, 4 overfull lines left (≤ 7 pt);
  `main.pdf` 50 pages.

## What was corrected

- Four claims the marketing professor recalled from memory were checked against the papers'
  abstracts (OpenAlex) before acting: De Veirman (the uniqueness effect is about influencers
  in general, not only high-follower ones — the committee was wrong), Evans (direction not
  stated — left neutral), Bawa & Shoemaker (control group not stated in the abstract — the
  report no longer attributes it to the paper), Miller & Kahn ("unusual" names — applied).
- The Israeli military-service age claim (MP-10) was left out: its only source was an archived
  government PDF that could not be opened.
- The new `\sep` swallowed the line break (control-word space), giving a 55 pt overfull keyword
  line; fixed with explicit glue.
- The new measurement paragraph pushed chapter 2 to 5 pages; the redundant closing insight box
  of chapter 2 was removed (the chapter keeps its key-message and guiding-question boxes).
- The first version of `raghad-todo.md` was written before Raghad's commit was pulled; it was
  rewritten to keep only the items that are still open.
- **Not done (as instructed):** the sales target in ch. 2, the abstract and the summary is still
  255K ₪ / ~3,700 units, while Raghad's chapters now use 2,200 units / 150K ₪ gross.
