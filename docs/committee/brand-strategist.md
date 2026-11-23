# Committee review — Brand Strategist

Scope: positioning, market sizing, launch alternatives, unit economics, plan/budget/KPI realism and cross-chapter number consistency in `chapters/01`, `02`, `04`–`08`, `00-abstract.tex`, `figures/decision_matrix_scores.py`, `figures/price_positioning.py`, `figures/gantt_launch.py` and `main.pdf` (body pp. 1–37).

1. **BS-01 · critical** — **Problem:** The report has no P&L and no unit economics, and on its own numbers the launch loses money. The 255K ₪ target is a consumer-price figure. Israeli retail prices include VAT (18% since January 2025), so net revenue is about 216K ₪ (255,000 / 1.18). Nowhere does the report give COGS per unit, packaging cost, marketplace commission %, payment and shipping costs, returns, or the cost of the 3,000 free samples. The only margin figure, "70%–72%" gross margin, is unsourced and belongs to Alternative A, not the chosen option. Even with that optimistic 70% margin, gross profit is about 151K ₪ before marketplace commission, against a 150K ₪ marketing budget. The 150K also has no line for inventory production or salaries, although the RACI lists 5 roles. Implied CAC: the channel table gives 127.5K/115 ₪ = ~1,109 D2C orders, 89.3K/74 ₪ = ~1,207 marketplace orders and 38.2K/69 ₪ = ~554 bar sales, about 2,870 orders in total. 150K / 2,870 = ~52 ₪ per order, against a 69–115 ₪ AOV. The report never says whether month 6 is meant to break even or is a deliberate investment, so "ROI report" (WP6) has no baseline. **Where:** `05-alternatives.tex:44`, `:87–89`, `:278–303` (body p. 29); `06-workplan.tex:38–64` (p. 32); `08-summary.tex:13–14`. **Concrete fix:** Add a one-table launch P&L for months 1–6 and a 12-month view. It needs gross → net of VAT, COGS per unit (cite a real contract-manufacturer quote or source), marketplace commission % from the platform's published terms, fulfilment, samples, inventory and people costs. State CAC, contribution margin per order and the payback month. If the plan is loss-making by design, say so and justify it with an LTV/repeat-purchase assumption.

2. **BS-02 · critical** — **Problem:** The decision matrix is tilted toward Alternative C, and its margin of victory is fragile:
   - C gets 9 on "fit to persona/sensory insight", the same as B, although B puts 70% of its budget into 4 campuses while C has 3 one-day events.
   - C gets 9 on virality versus 8 for A, although A puts 100% of its budget into digital.
   - C gets 9 on conversion versus 8 for B, although B is face-to-face.
   - Budget efficiency is scored without any revenue or profit projection per alternative (115K vs 150K vs 195K budgets chasing the same 255K target).

   The per-event cost assumptions also favour C. In B, the field costs are 55+45+40 = 140K for 4 campuses (~35K per campus). In C, 3 events plus 3,000 samples cost 40K in total (~13K per event).

   Two plausible 1–2 point corrections erase the win. With C sensory 9→7 and virality 9→8, C = 8.10 − 0.50 − 0.20 = 7.40, a tie with A. The sensitivity analysis only varies the weights, never the scores, so it cannot detect this. **Where:** `05-alternatives.tex:60–65`, `:87–89`, `:179–189` (body pp. 24–27); `figures/decision_matrix_scores.py` (scores dict, scenarios). **Concrete fix:**
   - Anchor each score to a stated rubric (for example, "virality = forecast views per 1K ₪").
   - Use the same cost-per-event basis in B and C.
   - Add an expected-profit row per alternative.
   - Add a score-sensitivity (±1/±2 per cell, or a Monte-Carlo) panel that reports how often C wins.

3. **BS-03 · critical** — **Problem:** The sales target contradicts the SOM it says it comes from. The year-1 SOM is 511K ₪ (2% of SAM). The 6-month target is 255K ₪ earned in only 3 selling months (months 4–6), which is 50% of the year-1 SOM in one quarter. That is an annualised run-rate of about 1.02M ₪, or 4% of SAM: double the 2% midpoint and above the stated 1.5%–2.5% upper bound (639K). The 2% penetration itself is asserted with no citation. The SAM covers students only, while the brand's target is "women 18–28" (abstract, ch. 1), so most of the stated target market is outside SAM. "3,700 equivalent units" is simply 255,000/69, which ignores the 299 ₪ five-pack (59.8 ₪/unit) and the 74/115 ₪ AOVs, so the unit count used for inventory is wrong. **Where:** `04-market.tex:78–97`, table at `:99–111` (body pp. 18–19); `02-problem.tex:49–51`, `:104` (pp. 5–6); `00-abstract.tex:4`. **Concrete fix:** Rebuild the target bottom-up from the funnel: reach → visits → CVR → orders × AOV, by channel. Show monthly ramp for months 4–6 that sums to a defensible share of the annual SOM. Cite a benchmark for first-year D2C penetration or drop the "realistic" label. Either widen the SAM to the stated 18–28 target or narrow the stated target to students. Compute units from the channel/bundle mix.

4. **BS-04 · major** — **Problem:** The value index behind "white space" is self-scored and circular. AURA is a product that does not exist yet, but it gets 2.2 for "moisturising formula" with no formula data, and 2.4 for "local accessibility" before it has any distribution. Criterion (a), "culinary narrative", is AURA's own concept, so it is built to favour AURA. The equal 2.5 weights are not justified. Removing only the unproven accessibility score gives AURA 6.4 versus Rhode 7.3, which reverses the headline. Only the social-currency score was discounted for AURA. **Where:** `04-market.tex:214–241` (body p. 21), `figures/price_positioning.py` `AURA_POINT`. **Concrete fix:** Score competitors only on verifiable attributes (price/ml, availability, shade count, rating counts), and show AURA as a target range, not a point. Alternatively, validate the index with a small consumer survey or conjoint (n ≥ 100 students) and report it as research, not as the authors' scoring.

5. **BS-05 · major** — **Problem:** The "white space at 45–95 ₪" rests on a competitor set with no mid-price players. The set is 4 imported premium brands plus 1 discount brand (Essence 6–15 ₪). It leaves out every mass/masstige brand on Super-Pharm/BE shelves (for example Maybelline, L'Oréal, NYX, Catrice, Israeli private labels), which is exactly the 45–95 ₪ band. So the gap may be an artifact of how the sample was chosen. The positioning text also contradicts itself on price floor: "10–20 ₪" (`04-market.tex:253`) vs "6–15 ₪" (`05-alternatives.tex:13`). **Where:** `04-market.tex:137–209`, `:252–262` (body pp. 19–22); `01-intro.tex:65–71`. **Concrete fix:** Add 3–5 verified mid-tier lip tints/oils sold in Israeli pharmacy chains, with prices and URLs. Re-draw the positioning map, and state what, besides price, AURA owns in that band.

6. **BS-06 · major** — **Problem:** The 3 tasting bars are operationally unrealistic and inconsistently specified:
   - REQ-08 requires 1,000 samples per event, and the experience is designed as a "3-minute campus break". That is ~50 person-hours of one-to-one service per event-day.
   - The ~13K ₪ per event must cover booth, food, staff, café partner, 1,000 samples and campus fees. Alternative B budgets 40K for staff alone.
   - The sales link is unclear. The channel table expects ~185 units per event sold on site, while G5 expects ≥10% of 3,000 sample recipients (300) to buy with the booth code within 30 days. Two different success definitions are given for the same channel.
   - There is no food-safety, allergen (honey, cocoa, berries) or lip-tester hygiene plan. Serving food on campus is missing from the risk register.
   - The plan has no calendar anchoring. If month 1 starts at the report date (November 2026), months 4–5 may fall in the exam period or semester break, when campus foot traffic is lowest.

   **Where:** `02-problem.tex:103`, `:144` (pp. 6–7); `05-alternatives.tex:291–296`, `:329–339` (pp. 28–29); `06-workplan.tex:42`; `07-risks.tex:197–207`; `figures/gantt_launch.py` (tasks 4.2). **Concrete fix:** Size each event bottom-up: hours × stations × throughput. Set a realistic samples-per-event figure, or switch to take-away sealed minis. Give a per-event cost table. Use one channel KPI that links samples to code redemptions to units. Anchor months to real dates against the academic calendar. Add a food/hygiene risk (R8) with a licensed-caterer mitigation.

7. **BS-07 · major** — **Problem:** The regulatory, formula and inventory timeline does not hold together:
   - REQ-01 notifications are submitted in month 1 (summary step 1; R3 mitigation), and notification is tied to the final formulation.
   - R5 plans student focus groups in months 1–2 to "refine texture, scent and longevity before filling stock". Any change after notification forces a re-notification on the critical path.
   - Gantt task 1.1 squeezes brand book, packaging and stock production for 5 shades into ~2.4 months, with no MOQ, lead time, quantity or safety-stock figure.
   - The regulatory and lab work shares one 32K line with the website, the AI agent and the marketplace (`06-workplan.tex:40`), while ch. 5 lists that same 32K without regulation (`05-alternatives.tex:87`).

   **Where:** `07-risks.tex:87`, `:95` (pp. 35–36); `08-summary.tex:31`; `figures/gantt_launch.py` task 1.1; `06-workplan.tex:40`, `:54` (p. 32). **Concrete fix:** Sequence formula freeze → focus-group validation → notification → production, or start before month 1. State the production run (units per shade, MOQ, lead time, reorder point). Give regulation its own budget line.

8. **BS-08 · major** — **Problem:** The KPIs are disconnected from the sales goal and are not measured in a defensible way. G2's 1,000,000 views is a vanity metric with no funnel that turns views into the ~2,870 orders needed. G1, ≥20% aided awareness, is stated as "among the target audience" in the guiding question but "in the pilot campuses" in the SMART table and abstract. Surveying only the 3 campuses that received bars builds selection bias into the result. "AURA" is a generic word that many existing brands use, so aided recognition will produce false positives unless the survey includes a foil brand. G5's 10% conversion has no benchmark. **Where:** `02-problem.tex:84`, `:101–105` (pp. 5–6); `00-abstract.tex:9`; `06-workplan.tex:137–138` (p. 34). **Concrete fix:**
   - Define one funnel (views → link clicks → sessions → CVR → orders) with a cited benchmark at each step.
   - Measure awareness in pilot campuses and in a non-pilot control campus, with a fictitious foil brand.
   - Fix G1's population wording in all places.
   - Cite a sampling-conversion benchmark or present 10% as a hypothesis to be tested.

9. **BS-09 · major** — **Problem:** The "AI Flavor Sommelier" is neither necessary nor credible as a solution to the sensory barrier. It maps a coffee order or dessert preference to a lip shade, which has no basis in colour matching. Shade fit depends on skin tone and undertone, which the plan deliberately avoids asking about, so wrong-shade purchases and returns are a likely result. In Table 5.1 the plan rates it a "strong" answer to the sensory barrier, while rating Alternative A "weak" because a screen cannot convey scent or texture (`05-alternatives.tex:50–52`). The same limitation applies to the sommelier, so the two ratings are inconsistent and the sensory score is inflated. The cited Octane AI evidence is about quiz funnels, not an AI agent, and an Instagram DM agent needs Meta API work that is not budgeted. **Where:** `05-alternatives.tex:86–89`, `:126–129`, `:344–359`, table at `:362–387` (pp. 24–25, 28–30). **Concrete fix:** Replace it with a 3-question quiz (taste for storytelling + one skin-tone question for fit) and swatches on 3–4 diverse skin tones. Treat it as a conversion aid, not a sensory solution. Re-score the sensory criterion, and cost the build explicitly or remove it.

10. **BS-10 · major** — **Problem:** Competitor reaction is underrated, and the brand has no moat. R7 ("aggressive competitor reaction or copying the culinary concept") is rated P=2, I=3. Yet the report's own evidence shows food-inspired lip products are mainstream: e.l.f.'s pickle lipstick (`01-intro.tex:24–26`), Rhode (`04-market.tex:40–43`), and Essence "Juicy Bomb" already on Super-Pharm shelves at 6–10 ₪ (`04-market.tex:150`). A pharmacy brand can add food names and scents to a 15–30 ₪ tint within one season, and Rhode opening official shipping to Israel would remove AURA's price and availability gap. The mitigation, one limited-edition shade (REQ-11), is not a defence. **Where:** `07-risks.tex:205`, `:229` (pp. 35–36). **Concrete fix:** Raise R7 to at least P=3, I=4 (R ≥ 12) so that it gets a full mitigation and contingency plan. State the defensible assets (formula claim, owned community/CRM, flavour IP, retail exclusivity), and add a price-response rule if a 30 ₪ copy appears.

11. **BS-11 · major** — **Problem:** The marketplace channel is assumed rather than secured, and the channel-conflict rules have gaps:
   - 35% of revenue (89.3K ₪) is assigned to "Terminal X or Super-Pharm Online" before the platform is chosen. Neither the platform's acceptance of an unknown brand, nor the commercial model (commission, consignment or wholesale), nor its payment terms is shown.
   - "Commission limited to 35% of volume" (Table 5.1) describes the volume share, not the cost.
   - REQ-04 requires one 69 ₪ unit price in every channel, yet REQ-06 gives every creator and booth a coupon code, and the bar QR gives a "launch benefit". The effective price therefore differs by channel. Marketplaces also run their own promotions, which the brand does not control.
   - Chapter 1 argues against "pharmacy shelf only", but the plan then routes 35% of sales through a pharmacy chain's online store, and this tension is never discussed.

   **Where:** `05-alternatives.tex:79–83`, `:125`, `:255–259`, `:308–313` (pp. 24–25, 29); `02-problem.tex:140`, `:142`; `01-intro.tex:85–87`. **Concrete fix:** Choose one marketplace, cite its published seller terms and commission, and model the net revenue. Define a promo policy: a discount ceiling per channel, codes valid on D2C only, and a MAP clause with the marketplace. Add "marketplace rejects or delays onboarding" as a risk, with a fallback reallocation.

12. **BS-12 · major** — **Problem:** Elements a brand strategist would require are missing:
   - No positioning statement, brand pyramid or reasons-to-believe. The "creamy-moisturising" claim (Table 4.2) has no substantiation and would need claim support before it can be advertised.
   - No price test. 69 ₪ and 299 ₪ are carried over from Exercise 1 and never validated, for example with a Van Westendorp survey or an A/B test.
   - No repeat-purchase or retention target and no LTV figure, although LTV appears in the abbreviations.
   - No post-launch plan (months 7–12: reorder, retail expansion, year-2 budget).
   - No commercial kill or pivot criteria. M3 is only a regulatory gate, so nothing triggers cutting spend if month-4 sales fall short of the target.
   - The month-5 plan already names the "leading shades" (Golden Honey, Silk Cocoa) before any sales data exists.
   - The "AURA" name has no trademark clearance in Israel.

   **Where:** `04-market.tex:172`; `05-alternatives.tex:260–264` (p. 29); `06-workplan.tex:121–141` (p. 34); `08-summary.tex`. **Concrete fix:** Add a half-page "brand and commercial guardrails" section with:
   - a positioning statement;
   - a price-test plan;
   - repeat-rate and LTV targets;
   - a month-4 commercial gate (for example, if sales are below 50% of the month-4 plan, cut paid media and re-weight to the D2C bundle);
   - a months 7–12 outline;
   - a trademark search as a WP1 task.

   Replace the named "leading shades" with "the top-2 shades by month-4 sell-through".

13. **BS-13 · minor** — **Problem:** The residual-risk scores are arbitrary. R1 (market saturation, 16) falls to a residual of 6 through "mitigations" that are the base plan itself (tasting bars, the AI share card), so the base plan is counted twice. R3 falls to 1×4 = 4, although the critical-path risk of re-notification (BS-07) remains. The summary and abstract then present "16 → 6" as a headline result. **Where:** `07-risks.tex:241–260`, `:265–268` (p. 36); `08-summary.tex:13–14`; `00-abstract.tex:22`. **Concrete fix:** List only mitigations that are additional to the base plan, give each a cost and an owner, and justify every residual P and I in one clause. Soften the headline claim.

14. **BS-14 · minor** — **Problem:** Several cross-chapter numbers and scopes disagree:
   - Chapter 6 says the plan covers "REQ-01–REQ-09" (`06-workplan.tex:12`, `:61`), while chapter 2 defines 11 requirements and chapter 7 uses REQ-10 and REQ-11.
   - The discount floor is "6–15 ₪" (`05-alternatives.tex:13`) versus "10–20 ₪" (`04-market.tex:253`).
   - The SOM range "1.5%–2.5%" is reported with "≈2,960 buyers" but "≈7,400 equivalent units", a ratio of 2.5 units per buyer that is equal to the annual purchase-frequency assumption, so year-1 repeat buying is counted inside the SOM and again as the "LTV" upside.

   **Where:** as cited; body pp. 18–19, 23, 31–32. **Concrete fix:** Change ch. 6 to "REQ-01–REQ-11", or explicitly scope out REQ-10/11. Use one price floor. State whether the SOM customer count already includes repeat purchases.
