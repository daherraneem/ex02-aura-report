# 09 – Merge Chapter 5, Push Chapter 2, Write Chapter 3: Literature Review

**Author:** Raneem · **Agent:** Claude Code · **Date:** 2026-11-23

## Prompt

```
First run git pull to get Raghad's chapter 5. If references.bib or another file has a conflict,
keep BOTH sides, never delete her entries. Do not commit the regenerated figure PDFs.
Then approve and push my chapter 2, following the push rules.

After the push, write my chapter chapters/03-literature.tex
(Literature review and flagship paper, 9 pages) in Hebrew, following the booklet (chapter 5):
- A thematic (not paper-by-paper) review of real peer-reviewed papers on: sensory marketing,
  food names and product naming, influencer marketing, and product sampling / trial.
- A literature matrix table: papers vs themes.
- One flagship paper analysed in depth (method, findings, limits, what it means for AURA).
- The knowledge gap in one sentence, leading to our project.
Every paper must be real and have a DOI, checked by web search. Stay consistent with chapters 1, 2, 4 and 5.
Remove the draft boxes. Build and show me the chapter pages. Do not push chapter 3 yet.
```

## What the agent did

- Pulled Raghad's chapter 5; resolved the conflicts in `references.bib` and
  `00-abbreviations.tex` keeping both sides (details in `prompts/08-problem-chapter.md`);
  aligned chapter 2 with chapter 5; pushed chapter 2 (`904c076`).
- Read the booklet's chapter 5 (thematic critical review, literature matrix, flagship
  paper chosen by three criteria with a Venn figure, analysis, knowledge gap).
- Verified 12 peer-reviewed papers: each DOI checked against Crossref and/or OpenAlex
  (authors, title, journal, volume, issue, pages), and each abstract read on OpenAlex or
  Semantic Scholar before it was used. Krishna (2012) reuses Raghad's existing entry.
- Wrote `chapters/03-literature.tex` (9 pages, pp. 8–16): search method; thematic review in
  4 themes (sensory/touch, names and food, influencers, sampling), each with a critical
  reading and its meaning for AURA; a table of 7 design principles mapped to the goals and
  requirements of chapter 2; the literature matrix (12 papers × 4 themes + the project row);
  flagship choice (Venn diagram `figures/tikz/flagship-venn.tex` + criteria table);
  in-depth analysis of Bawa & Shoemaker (2004) with the model ΔS = E + A − C and a table of
  how each component will be measured in the launch; the knowledge gap in one sentence.
- Added 11 entries to `references.bib` (own section, add-only). Build: 0 errors.

## What was corrected

- One candidate DOI (10.1108/00070701111177665), which was expected to be an in-store
  sampling paper, belongs to a different paper on Crossref; it was dropped.
- No free full text of the flagship paper was found, so its analysis uses only the
  published abstract and the indexed record (field experiments, panel data); the limits
  are labelled as the team's own assessment.
- A detail not in the Elder & Krishna abstract ("smell, texture, taste") was removed.
- TikZ: `\\` inside `\texthebrew{}` in a node without a text width failed; text width added.
- The section heading 3.2 was alone at the bottom of a page; a short intro paragraph was
  added. `REQ-06` broke at its hyphen; wrapped in `\mbox`.
