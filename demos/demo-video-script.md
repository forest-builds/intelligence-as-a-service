# Demo Video Script (3–5 min)

**Goal:** show, in one sitting, that this is a real framework with a working tool and a real-domain application — not a thought-leadership post.

**Format:** screen recording + voiceover. No face needed. Terminal + the repo on screen.

---

## Beat 1 — The problem (0:00–0:40)

> Every company is about to run AI across every workflow. Almost none of them can answer a simple question: is it actually worth it?
>
> They measure tokens, seats, prompts — activity. But token consumption is not productivity. A team can burn millions of tokens producing work that gets thrown away, and a disciplined team can leave huge value on the table by not using AI where it would help.
>
> The unit everyone reports — tokens — is the wrong unit.

*On screen:* a typical AI usage dashboard (tokens, seats, prompts). Then strike through "tokens."

## Beat 2 — The insight (0:40–1:30)

> The real object isn't the token. It's metered machine cognition — consumed AI capability applied to a goal. And the metric that matters is cognitive efficiency: validated incremental value per unit of machine cognition.
>
> Here's the catch that makes this not just "ROI with a new name." When you separate the machine-cognition cost from the human supervision cost, you find the binding constraint is almost never tokens. It's expert attention.

*On screen:* the CE formula, then the metrics table from the README.

## Beat 3 — The tool (1:30–2:40)

> So I built an evaluator. You give it one workflow run — costs, time, value, validation — and it returns the full breakdown.
>
> First, does it agree with the theory? The paper has a worked example. Let me run the tool on it.

*On screen — live terminal:*
```bash
python evaluator/test_evaluate.py
```
> It reproduces the paper exactly. Cognitive efficiency 33×. But look at this: Token ROI on the machine cost alone is 71×. On the total cost including human review, it's 1.75×. That hundred-fold gap is human supervision. The tokens are a rounding error. The reviewer's time is the whole game.

## Beat 4 — The case (2:40–4:00)

> Now a real domain. FEMA Public Assistance: after a disaster, every reimbursement package — 150 pages of invoices and contracts — gets reviewed by an expert. Slow, expensive, and errors cost millions in later deobligations.

*On screen — live terminal:*
```bash
python evaluator/evaluate.py --input demos/fema-pa-review/workflow.json
```
> AI assists the review. Watch what the framework surfaces that a quality dashboard would miss. Deliverable quality barely moves. But reviewer time drops from 4 hours to 1.75 — a 2.3× capacity multiplier — and expected error cost halves. Net value: $499 per package.
>
> Across one disaster's worth of packages, that's millions in forgone value and tens of thousands of reviewer-hours — the nonuse penalty. That's the number a program office should track. Not the token bill.

## Beat 5 — The implication (4:00–4:45)

> The pattern holds across domains: the model is cheap, expert attention is scarce, and the value is in routing, validation, and throughput — not consumption.
>
> The durable advantage isn't who has the biggest model. It's who instruments their workflows to capture whether AI output actually gets used — and closes the loop. That instrumentation layer is the asset.
>
> Paper, evaluator, and case study are all open source. Link below. Run it on your own workflow.

*On screen:* repo URL, the three artifacts.

---

## Shot list / assets needed

- [ ] Terminal with repo cloned, font size up
- [ ] `python evaluator/test_evaluate.py` run captured
- [ ] `python evaluator/evaluate.py --input demos/fema-pa-review/workflow.json` run captured
- [ ] README scroll (metrics table, behavioral signal table)
- [ ] FEMA case study README scroll (interpretation section)
- [ ] Lower-third with repo URL

## One-line pitch (for the post that carries the video)

> I built an open-source evaluator that measures whether AI-assisted work actually produces value — beyond token cost — and applied it to a public-sector workflow. The finding: tokens are a rounding error; expert attention is the constraint everyone is mismeasuring.
