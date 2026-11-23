# Expert Committee — Lead Summary

**Date:** 2026-11-23 · **Graded state:** `main` at `9be39c4` + local `main.pdf` (50 pages)
**Method:** 5 independent subagents (red team), one role each, each writing its own file;
the lead (Raneem's Claude Code) merged and judged them. The report itself was **not changed**.

| Member | File | Findings | Critical | Major | Minor |
|---|---|---|---|---|---|
| Marketing communications professor | [marketing-professor.md](marketing-professor.md) | 14 | 3 | 9 | 2 |
| Brand strategist | [brand-strategist.md](brand-strategist.md) | 14 | 3 | 9 | 2 |
| Academic editor | [academic-editor.md](academic-editor.md) | 20 | 2 | 8 | 10 |
| Design and LaTeX expert | [design-latex.md](design-latex.md) | 18 | 2 | 8 | 8 |
| Grading lecturer | [lecturer-grader.md](lecturer-grader.md) | 17 | 1 | 8 | 8 |
| **Total** | | **83** | **11** | **42** | **30** |

The grading lecturer's estimate: **84 / 100**. Points are lost mainly on the deliverable (the
PDF is not committed), the process (prompt log, README) and visible typesetting defects.

## How to read the table

- **Verdict:** *Agree* = valid, should be fixed · *Partly* = valid core, but the proposed fix
  is too large or partly wrong · *Disagree* = not worth doing or not correct ·
  *Verify first* = the reviewer recalled a paper's result from memory (it said so); check the
  paper before acting.
- **Effort:** L = under 30 min · M = 1–3 h · H = more than 3 h or needs new verified sources.
- **Owner:** who may make the fix under the ownership rule: **Ra** = Raneem (ch. 1, 2, 3, 8),
  **Rg** = Raghad (ch. 4, 5, 6, 7), **Sh** = shared file (class, bib, README, front matter) —
  small change, announced to the partner.
- **Cluster:** the recommended fix (section 3) that covers the finding.

## 1. All findings

### Content and argument

| ID | Finding (short) | Owner | Verdict | Why | Effort | Cluster |
|---|---|---|---|---|---|---|
| MP-01 | The gap ("never tested together") cannot be measured: no control campus or holdout | Ra | Agree | The strongest objection. The plan claims to measure the combination but has no comparison. A matched non-pilot campus with pre/post surveys is cheap | M | F2 |
| MP-02 | Flagship model is measured by one self-report question; G5 is called "expansion" but counts all buyers | Ra | Agree (verify detail) | G5 measures conversion, not expansion. The exact comparison design of Bawa & Shoemaker must be checked in the paper before rewriting | M | F2 |
| MP-03 | 255K ₪ target rests on unsourced SAM/SOM assumptions and is 50% of the year-1 SOM in 3 months | Rg + Ra | Agree | Confirmed by BS-03 and AE-01. The single most repeated problem | H | F1 |
| MP-04 | Communication goals are invented and not tied to a funnel | Ra | Agree | G1–G3, G5 are labelled as planning targets, but there is no funnel linking them to G4 | M | F1 |
| MP-05 | Food shade names are descriptive, not the "ambiguous" names of Miller & Kahn | Ra | Agree (verify detail) | Plausible: "Golden Honey" is descriptive. Check Miller & Kahn's name categories, then cite Skorinko as the main support | L | F2 |
| MP-06 | Sensory papers are stretched: taste of food → value of a cosmetic is untested | Ra + Rg | Agree | State the tasting-to-tint link as a hypothesis. Ch. 5's Krishna sentence overstates the review | M | F2 |
| MP-07 | De Veirman's follower-count condition dropped; Evans' disclosure cost to sharing not reported | Ra | Verify first | (a) is likely right and actually supports micro-influencers. (b) The direction of the Evans effect must be checked in the article before writing it | L | F2 |
| MP-08 | No message strategy, creative concept, creator brief or language strategy | Rg | Partly | Valid gap, but a full "message house" does not fit ch. 5's page budget. A short table is enough | M | — |
| MP-09 | Differentiation is circular: Rhode is also food-inspired; value index puts price on both axes | Rg | Agree | Same as BS-04 and AE-10 | M | F4 |
| MP-10 | Women 18–20 in Israel are mostly in military/national service; Gen Z data are not Israeli | Ra | Agree | Important Israeli context. Redefine the target as female students (≈20–28) or explain. State that the Kyra data are not Israeli | L | F6 |
| MP-11 | Decision-matrix scores have no rubric; sensitivity varies only weights | Rg | Agree | Same as BS-02 | M | F4 |
| MP-12 | Missing risks: food imitation, stall food hygiene, claims/backlash; formula change after notification | Rg | Agree (verify source) | Real risks. The EU directive on food-imitating products must be verified before it is cited | M | F5 |
| MP-13 | The 75% sampling survey is weak and worded differently in ch. 1 / 2; R5 citations do not support the risk | Ra + Rg | Agree | Unify the wording and say it is an industry survey; fix the R5 citations | L | F7 |
| MP-14 | Ch. 1 promises a social-commerce stream in ch. 3 that is not there | Ra | Partly | Fix the roadmap sentence (L). Adding a new verified paper stream is optional | L | F6 |

### Brand, business and plan realism

| ID | Finding (short) | Owner | Verdict | Why | Effort | Cluster |
|---|---|---|---|---|---|---|
| BS-01 | No P&L or unit economics; ~52 ₪ marketing cost per order; VAT not removed | Rg + Ra | Agree (verify VAT) | A launch plan without contribution margin is weak. A one-table P&L with clearly labelled assumptions is enough; the VAT rate must be cited | H | F1 |
| BS-02 | Decision matrix tilted to alternative C; 1–2 point changes make a tie | Rg | Agree | Add a rubric and a score-sensitivity test; keep C only if it survives | M | F4 |
| BS-03 | Target = 4% of SAM run-rate; 3,700 units = 255,000/69 ignores bundles | Rg + Ra | Agree | Same root as MP-03 | H | F1 |
| BS-04 | Value index self-scored; removing one unproven score reverses the headline | Rg | Agree | Present it as the team's hypothesis or score AURA as a target range | M | F4 |
| BS-05 | No mid-price competitors in the set, so the "white space" may be an artifact | Rg | Agree | Needs 3–5 verified mid-tier products with prices and URLs | H | F4 |
| BS-06 | Tasting bars not sized (1,000 samples/day), two different KPIs, no hygiene plan, no academic calendar | Rg + Ra | Agree | Size per event; one KPI chain; anchor months to the academic calendar | M | F5 |
| BS-07 | Formula testing after the MoH notification forces re-notification; no production/MOQ | Rg | Agree | Sequence: formula freeze → focus group → notification → production | M | F5 |
| BS-08 | KPIs disconnected from sales; awareness survey only at pilot campuses; "AURA" name gives false positives | Ra | Agree | Control campus + foil brand in REQ-09 | M | F2 |
| BS-09 | AI Flavor Sommelier: no colour-matching basis; rated "strong" against the sensory barrier | Rg | Partly | Keep it but reframe as a conversion aid and lower its sensory score; replacing it is Raghad's call | L | F4 |
| BS-10 | Competitor copying under-rated (R7 = 6) | Rg | Agree | Raise R7 and add a real mitigation | L | F5 |
| BS-11 | Marketplace assumed, not secured; coupon codes conflict with "one price" | Rg + Ra | Agree | Add an onboarding risk and a promo policy; REQ-04 wording (Ra) must allow codes | L | F5 |
| BS-12 | No positioning statement, price test, retention/LTV, post-launch plan, commercial gate, trademark check | Rg | Partly | All valid, but a half-page section exceeds the page budget. Add a month-4 commercial gate and a trademark task; mention the rest in one sentence | M | — |
| BS-13 | Residual risk scores count the base plan as mitigation | Rg | Agree | Justify each residual in one clause; soften "16 → 6" in abstract and summary (Ra) | L | F5 |
| BS-14 | REQ-01–09 vs 11 requirements; price floor 6–15 vs 10–20; SOM buyers vs units | Rg | Agree | Consistency sweep | L | F6 |

### Structure, consistency, sources and language

| ID | Finding (short) | Owner | Verdict | Why | Effort | Cluster |
|---|---|---|---|---|---|---|
| AE-01 | 255K target vs SOM; "equivalent units" undefined; time window worded two ways | Rg + Ra | Agree | Same as MP-03 / BS-03 | H | F1 |
| AE-02 | Weak sources presented as research (McKinsey article, vendor case study, landing pages, BoI home page) | Rg | Agree | Replace with exact pages or drop the numbers; call trade sources "industry reports" | M | F7 |
| AE-03 | Two budget splits for alternative C (52/27/21% vs 45/30/25%) | Rg | Agree | Pick one | L | F6 |
| AE-04 | "בפרויקט שלנו" box titles are first person; promotional words ("מנצחת", "מובטחת") | Ra + Rg | Partly | The box title follows the booklet's own "in your project" box, so it can stay. The promotional words should go | L | F6 |
| AE-05 | References 6 pp. instead of 3; front matter 6 pp. | Sh | Agree | Class fix: single spacing and URL breaking in the bibliography | M | F3 |
| AE-06 | Online references print no year; three books without DOI/URL; brand names in lower case | Sh + Rg | Agree | Check the biblatex online driver; add URLs or ISBN links to the books | M | F7 |
| AE-07 | No paper newer than 2022; flagship analysis thin | Ra | Partly | Recency is not a rule. The flagship depth issue is real — get the full text through the library | M | F2 |
| AE-08 | G5 counts all buyers; no baseline; matrix row says "tested" | Ra | Agree | Same as MP-01 / MP-02; change the project row to "planned measurement" | L | F2 |
| AE-09 | The campus activity has 5 names (דוכן / בר / פופ-אפ …) | Ra + Rg | Agree | Choose "בר טעימות" (ch. 5's term) everywhere | L | F6 |
| AE-10 | Value index and decision matrix presented as "quantitative and transparent" | Rg | Agree | Same as BS-04 | L | F4 |
| AE-11 | Ch. 1 says three trends; abstract says two | Ra | Agree | Trivial | L | F6 |
| AE-12 | Ch. 3 says "seven principles" and "four principles" | Ra | Agree | Trivial | L | F6 |
| AE-13 | Pharmacy price band appears as ~15, 10–20 and 6–15 ₪ | Ra + Rg | Agree | One range everywhere | L | F6 |
| AE-14 | Instagram age base differs between ch. 1 and 4; "57 institutions" vs "57 campuses" | Ra + Rg | Agree | Trivial | L | F6 |
| AE-15 | Inconsistent names for small influencers | Ra + Rg | Agree | Trivial | L | F6 |
| AE-16 | Ch. 7 says REQ-01–09 but uses REQ-10/11; ch. 4 AURA row omits the marketplace | Rg | Agree | Trivial | L | F6 |
| AE-17 | Abbreviations missing (KPI, PoC, QR, FOMO …); "מיועץ" non-standard | Sh | Agree | Add-only entries | L | F6 |
| AE-18 | Author names in Hebrew in ch. 5–6, English in ch. 2–3 | Ra + Rg | Agree | Use English in `\en{}` everywhere | L | F6 |
| AE-19 | Hebrew typos ("מלחחת", "וווקר", "יוסכם", missing word) | Ra + Rg | Agree | Trivial | L | F6 |
| AE-20 | LOF/LOT drop spaces; not in the TOC | Sh | Agree | Same as DL-01 | M | F3 |

### Design and LaTeX

| ID | Finding (short) | Owner | Verdict | Why | Effort | Cluster |
|---|---|---|---|---|---|---|
| DL-01 | LOF/LOT lose the space after `\en`/`\ltr` (fragile commands in captions) | Sh | Agree | Root cause found in the class; robust commands fix every caption at once | M | F3 |
| DL-02 | Bibliography URLs run past the margin (up to 105 pt) | Sh | Agree | Class: URL break penalties + ragged right | L | F3 |
| DL-03 | `\en{}` tokens hyphenated at line ends (Super-/Pharm, REQ-/01) | Sh | Agree | Disable hyphenation inside `\en` in the class | L | F3 |
| DL-04 | Tables at `\scriptsize` (8 pt) in ch. 4–7; inconsistent with ch. 1–3 | Rg | Agree | Minimum `\footnotesize`; cut words instead of shrinking | M | F3 |
| DL-05 | Python figure labels print at ~5 pt | Rg | Agree | Set figsize to the real text width | M | F3 |
| DL-06 | Fig. 5.1 panels in LTR order; Gantt axis LTR | Rg | Agree | Swap axes; one caption line for the Gantt | L | F3 |
| DL-07 | A product in Table 4.1 displays backwards (three LTR islands) | Rg | Agree | One math unit; same factorisation as Eq. 4.1 | L | F3 |
| DL-08 | Pages with large empty areas (body pp. 7, 15, 25) | Ra + Rg | Agree | Float placement; `floatpagefraction` in the class | M | F3 |
| DL-09 | LOF/LOT misaligned; entry 4.2 is 55 pt overfull; 117 `\endL`/`\endR` warnings | Sh | Agree | Mostly solved by DL-01; short captions for long ones | M | F3 |
| DL-10 | Launch-architecture TikZ overlaps itself and splits a list | Rg | Agree | Padding + `[t]` placement | L | F3 |
| DL-11 | Numbers separated from ש"ח at line ends | Sh | Partly | Ties in the worst places are enough; a new `\nis` macro is optional | L | F3 |
| DL-12 | Flagship box author list prints the comma on the wrong side; citations inside wrapped English | Ra + Rg | Agree | One `\en{}` for the author list | L | F3 |
| DL-13 | Garbled author name in ref. [52]; "Language hebrew not supported" warning | Rg + Sh | Agree | Fix the `Jr.` field order; `langid` | L | F7 |
| DL-14 | Figure fonts differ (David in matplotlib vs Gisha/Calibri in TikZ) | Rg | Partly | Nice to have; low grading impact | M | — |
| DL-15 | Box types used for different meanings | Ra + Rg | Partly | Document the semantics in the class comment; re-map only clear misuses | L | — |
| DL-16 | English curly quotes and ASCII `"` instead of gershayim | Sh | Disagree | ASCII `"` in ש"ח is standard Hebrew typing; a global replace risks breaking TeX. Low value | — | — |
| DL-17 | Lone bullet in the keyword line; LOF/LOT not in TOC; double space in cover title; course names differ | Sh | Agree | Small class fixes | L | F3 |
| DL-18 | Hebrew subscript in Eq. 4.1 too small; uneven numbering | Rg | Agree | Use `N_s` with a "where" clause | L | F3 |

### Process and deliverables

| ID | Finding (short) | Owner | Verdict | Why | Effort | Cluster |
|---|---|---|---|---|---|---|
| LG-01 | Final `main.pdf` not committed (git-ignored) | Sh | Agree | Planned for submission; do it with `git add -f` after the last fix round | L | F8 |
| LG-02 | Prompt log not fully verbatim (files 03, 04) | Rg | Agree | Only Raghad can recover her original prompts | L | F8 |
| LG-03 | Raghad's approval/merge prompts not logged | Rg | Agree | Same | L | F8 |
| LG-04 | 36 overfull boxes, text outside the margins | Sh | Agree | Same as DL-02 / DL-09 | M | F3 |
| LG-05 | LOF/LOT BiDi defects; flagship box comma | Sh + Ra | Agree | Same as DL-01 / DL-12 | M | F3 |
| LG-06 | README stale ("chapters not written yet"), no workflow section, no PDF link | Sh | Agree | Cheap and visible to the grader | L | F8 |
| LG-07 | References 6 pp. → numbered part is 43 pp., not 40 | Sh | Agree | Same as AE-05 | M | F3 |
| LG-08 | Multi-agent loop incomplete: committee after all pushes, fixes not applied, prompt 16 placeholder | Ra | Agree | Closing the loop (apply fixes in a logged prompt, rebuild) is exactly what this committee is for | M | F8 |
| LG-09 | Sources checked differently by the two agents (McKinsey, Vogue HK, IMF landing page, BoI) | Rg | Partly | A timeout on Raneem's side does not make Raghad's source invalid, but each must be re-opened and pointed to the exact page | M | F7 |
| LG-10 | Kelley name garbled; ISBN in small caps; Eq. 4.1 never referenced | Rg | Agree | Trivial | L | F7 |
| LG-11 | Raghad's commit messages too long / unwrapped | Rg | Agree | From now on; never rewrite history | L | F8 |
| LG-12 | Raneem's chapters have no Python graph | Ra | Agree | Each partner gets half the grade. A literature-matrix heat-map (ch. 3) is cheap and replaces a table | M | — |
| LG-13 | `page_budget.py` is dead code still built | Ra | Agree | Use it or delete it | L | F8 |
| LG-14 | Raghad's TikZ uses `\textenglish`/`\LR` directly | Rg + Sh | Partly | Class macros may not work inside TikZ; add a documented TikZ-safe macro to the class | L | F3 |
| LG-15 | Prompt numbering clash during the work | Sh | Agree | Already disclosed; add "pull, then reserve the number" to both rule files | L | F8 |
| LG-16 | Cover lacks faculty/department; abbreviations RACI/SMART lack English | Sh | Agree | Trivial | L | F8 |
| LG-17 | Empty float page (Table 2.3); tables below 11 pt | Ra + Rg | Agree | Same as DL-04 / DL-08 | M | F3 |

## 2. Disagreements and items to verify

- **Disagree:** DL-16 (gershayim). Low value, and a global replace risks breaking TeX.
- **Partly:** AE-04 (the "בפרויקט שלנו" title follows the booklet's own box convention), MP-08 / BS-12
  (valid, but full sections break the page budget — add compact versions), LG-09 (re-check, do not
  assume invalid), DL-14 / DL-15 (nice to have).
- **Verify before acting** (the reviewer said it recalled these from memory):
  Evans et al. — direction of the disclosure effect on attitude and sharing (MP-07);
  Miller & Kahn — name categories (MP-05); Bawa & Shoemaker — comparison-group design (MP-02);
  the EU directive on products that look like food (MP-12); the Israeli VAT rate (BS-01).
  Each must be checked in the source, and cited, before it enters the report.

## 3. Recommended fixes (most worth doing)

Ordered by impact on the grade and on the logic of the report. Each fix lists the findings it
closes and who does it.

| # | Fix | Closes | Owner | Effort |
|---|---|---|---|---|
| **F1** | **Rebuild the sales target as a funnel with a light P&L.** One table, months 4–6, per channel: reach → visits → conversion → orders × AOV, plus stall traffic × conversion; define "unit" once; net of VAT; COGS, commission and marketing cost as labelled assumptions; low / base / high case. Use the same numbers in ch. 2, 4, 5, the abstract and the summary | MP-03, MP-04, BS-01, BS-03, AE-01 | Rg (ch. 4–5) + Ra (ch. 2, abstract, summary) | H |
| **F2** | **Make the measurement honest.** Add a non-pilot control campus and a baseline/endline survey with a foil brand (REQ-09); rename G5 "trial-to-purchase conversion"; change the project row in the literature matrix to "planned measurement"; reframe the gap as "do lab-proven mechanisms transfer to a real campus launch?"; limit the claims about the naming and sensory papers to their scope (after the verification list above) | MP-01, MP-02, MP-05, MP-06, MP-07, BS-08, AE-07, AE-08 | Ra (ch. 2–3) | M |
| **F3** | **Class and layout fixes (one shared change).** Robust `\en`/`\ltr`, no hyphenation inside `\en`; bibliography single-spaced, `\small`, ragged right, URL breaking (refs 6 → about 3–4 pp.); LOF/LOT in the TOC; `\sep` without a lone bullet; `floatpagefraction`; then fix the per-chapter items (table font ≥ `\footnotesize`, figure sizes, Fig. 5.1 panel order, Table 4.1 product, TikZ overlap, Table 2.3 float page). Raise the class version, recompile `tests/bidi-test.tex` | DL-01–DL-12, DL-17, DL-18, AE-05, AE-20, LG-04, LG-05, LG-07, LG-14, LG-17 | Sh (class) + Ra / Rg per chapter | M |
| **F4** | **Make the choice of alternative robust.** Scoring rubric per criterion, one evidence line per score, a ±1 score-sensitivity test (keep C only if it still wins), the same cost-per-event basis for B and C; present the value index as the team's hypothesis (or score AURA as a target range) and add mid-price competitors | MP-09, MP-11, BS-02, BS-04, BS-05, BS-09, AE-10 | Rg (ch. 4–5) | M–H |
| **F5** | **Fix the timeline and the risk register.** Formula freeze → focus groups → MoH notification → production; size the tasting bars per event with one KPI chain and the academic calendar; add risks for food imitation, stall hygiene, claims/backlash and marketplace onboarding; raise R7; justify every residual score and soften "16 → 6" | MP-12, BS-06, BS-07, BS-10, BS-11, BS-13 | Rg (ch. 6–7) + Ra (REQ wording, abstract, summary) | M |
| **F6** | **Consistency sweep.** One name for the tasting bar, one pharmacy price band, REQ-01–11 everywhere, one budget split, "two/three trends", "seven principles", influencer tiers, author names in English, target defined as female students (≈20–28), the ch. 1 roadmap sentence, Hebrew typos, promotional wording, missing abbreviations | MP-10, MP-14, BS-14, AE-03, AE-04, AE-09, AE-11–AE-19 | Ra + Rg, each in own files; Sh for abbreviations | L |
| **F7** | **Source hygiene.** Re-open every weak web source and point it to the exact page (BoI dated rate, influencer benchmark report, McKinsey); call trade sources "industry reports"; make the sampling-survey wording identical; fix the Kelley name, `langid`, years of online entries, URLs for the books | MP-13, AE-02, AE-06, DL-13, LG-09, LG-10 | Rg (most entries) + Ra (own) | M |
| **F8** | **Process and deliverables.** Update the README (status, page table, workflow section, links); log Raghad's missing prompts; fill in prompt 16; apply the fixes in a logged prompt and rebuild; decide on `page_budget.py`; add "pull, then reserve the prompt number" and commit-message length limits to both rule files; complete the cover and abbreviations; commit the final `main.pdf` at submission | LG-01–LG-03, LG-06, LG-08, LG-11, LG-13, LG-15, LG-16 | Sh + Rg (her prompts) | L |

**Suggested order:** F3 and F6 first (low risk, visible on every page), then F2 and F7, then
F1, F4 and F5 together (they change shared numbers, so Raneem and Raghad should agree on the
new figures before editing), and F8 last, together with the final build.

**Not recommended now:** DL-16, DL-14, a full message house (MP-08) and a half-page brand
section (BS-12) — they cost pages the booklet does not give.

## 4. Status (updated 2026-11-23)

- **Raghad, commit `2a88450`:** F1, F4, F5, F6, F7 in chapters 4–7 (new numbers in
  [numbers.md](numbers.md)).
- **Raneem, prompt 18:** F3 (class v0.2), F2 (chapters 2–3), F6/F7 in chapters 1–3, 8 and the
  abstract. Open items for chapters 4–7 are in [raghad-todo.md](raghad-todo.md).
- **Still open:** syncing the sales target (F1) in chapter 2, the abstract and the summary to
  `numbers.md`; F8 (README, prompt-log gaps, final PDF at submission).
