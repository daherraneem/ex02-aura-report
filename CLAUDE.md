# CLAUDE.md – Rules for Claude Code (Raneem)

Project: Exercise 2 of "AI Agents & Vibe Coding" (University of Haifa): a ~40-page
preparatory report (דוח מכין) in Hebrew, written in LaTeX, about the launch of
**AURA**, our food-inspired lip tint brand from Exercise 1.
Team: Raneem Daher (Claude Code) and Raghad Rabah (Antigravity).
The same rules are in `AGENTS.md` for Antigravity. **Keep the two files in sync.**

## 1. Git

- **Always run `git pull` before starting work.**
- **Never force push** (`git push --force` / `-f`), never rewrite pushed history.
- Commit or push only after the user approves (see section 3).

## 2. Prompt log

- Save **every prompt the user writes, word for word**, in `prompts/NN-short-name.md`.
- Numbering is continuous across both partners, with no gaps: run `git pull`, look at
  the highest number in `prompts/`, and use the next one.
- Each file has: the prompt (verbatim, in a code block), a short note on what the agent
  did, and what was corrected (by the user or after a check).
- Format: see `prompts/01-project-setup.md`.

## 3. Before every push

1. Show the user a summary of the changes (and the compiled PDF when the report changed),
   and **wait for approval**.
2. Commit message: a short title + 2-3 lines: what changed, why, and whether it is a
   **critical** or a **minor** change.
3. Add a line to the **Progress Log** in `README.md`: date, what was done, who did it.

## 4. Ownership

- **Each partner edits only her own chapter files** in `chapters/`.
- Shared files: the front matter (`chapters/00-abstract.tex`,
  `chapters/00-abbreviations.tex`), `references.bib`, `main.tex`, `aura-report.cls`,
  `README.md`, `CLAUDE.md`, `AGENTS.md`.
  Change them only for your own needs, keep the change small, and say so in the summary.
  `references.bib` and `00-abbreviations.tex`: only add entries, never edit the
  partner's entries.

| File | Chapter | Pages | Owner |
|---|---|---|---|
| `chapters/00-abstract.tex` | Executive summary + keywords | front | **Shared** |
| `chapters/00-abbreviations.tex` | Abbreviations and terms | front | **Shared** |
| `chapters/01-intro.tex` | 1. Introduction and background | 3 | **Raneem** |
| `chapters/02-problem.tex` | 2. Problem and goals | 4 | **Raneem** |
| `chapters/03-literature.tex` | 3. Literature and flagship paper | 9 | **Raneem** |
| `chapters/04-market.tex` | 4. Market research | 6 | **Raghad** |
| `chapters/05-alternatives.tex` | 5. Launch alternatives | 8 | **Raghad** |
| `chapters/06-workplan.tex` | 6. Work plan | 4 | **Raghad** |
| `chapters/07-risks.tex` | 7. Risk management | 2 | **Raghad** |
| `chapters/08-summary.tex` | 8. Summary | 1 | **Raneem** |
| `references.bib` | References | 3 | **Shared** |

Raneem: 17 pages (chapters 1, 2, 3, 8). Raghad: 20 pages (chapters 4, 5, 6, 7).

## 5. Writing the report

The requirements come from the lecturer's booklet `docs/preparation-report-book.pdf`
(part A: content; part B: LaTeX, CLS, BiDi) and `docs/l04-summary.pdf` (section 9).
These PDFs are copyrighted: they are git-ignored and must **never** be committed.

- **Use only the commands of `aura-report.cls`.** Its command list is at the top of the
  file. Do not invent new commands in chapter files; a new command goes into the class
  (raise its version and add a changelog line).
- **BiDi rules:**
  - every English word, name or acronym goes in `\en{...}`, and a multi-word phrase is one `\en{...}`;
  - every number, decimal, range, percent, date, price or version goes in `\ltr{...}` together with its unit/symbol;
  - never put Hebrew inside `\en{}`;
  - Hebrew inside a formula uses `\mathheb{}`, with brackets inside it;
  - TikZ goes inside `\begin{diagram}`, with Hebrew labels in `\texthebrew{}`;
  - in tables the first column is on the right, and columns are `r` or `p{}` (never `l`).
- Style: third person, professional; a technical term in Hebrew gets the English term in
  brackets on first use. No "we tested it and it worked great".
- Every figure and table is referenced in the text (`\ref`) and explained. Figure
  captions go below, table captions above.
- **Real sources only – never invent sources.** Every fact, number and paper must come
  from a real, checkable source **found by web search** and cited in `references.bib`.
  - Every factual claim has a `\cite{}`. Every entry in `references.bib` is cited, and
    every `\cite` exists in the file.
  - Each entry has a DOI or a working URL (`url` + `urldate`), checked when it was added.
  - If a source cannot be found and verified, leave the fact out. Never guess authors,
    years, titles or numbers, and never cite from memory.
- Python graphs: `figures/<name>.py` → `figures/<name>.pdf`, using `figures/aura_style.py`
  (AURA colors, `heb()` for Hebrew labels). TikZ diagrams: `figures/tikz/<name>.tex`.
- Remove all `\draftnote{}` boxes before submission.

## 6. Build and check

- Build: `.\build.ps1` (Python figures → xelatex → biber → xelatex ×2). Quick: `.\build.ps1 -Quick`.
- 0 errors before every push. Read `main.log` for `!`, undefined references and overfull boxes.
- After a class change, also compile `tests/bidi-test.tex` and check that the page is still correct.
- Check the PDF page by page: no reversed Hebrew or numbers, no heading at the bottom of a
  page, no split box, and nothing outside the margins.
