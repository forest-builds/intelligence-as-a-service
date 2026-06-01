# Case Study: FEMA Public Assistance Document Review

**Type:** Modeled scenario (transparent assumptions, not a measured pilot)
**Domain:** Regulatory / public-sector document review
**Purpose:** Demonstrate the cognitive efficiency framework on a high-value, high-friction institutional workflow — and show which assumptions actually move the metrics.

> ⚠️ **This is a modeled scenario, not measured data.** Every number traces to a documented assumption in [workflow.json](workflow.json). The value of this case study is the *method* and the *interpretation*, not the specific figures. To turn it into a primary-source case study, replace the assumptions with measured values from a real review pilot (see [How to make this real](#how-to-make-this-real)).

## The workflow

After a disaster declaration, FEMA Public Assistance (PA) reimburses state, local, tribal, and territorial governments (and certain nonprofits) for eligible response and recovery costs. Each **project worksheet package** — often 100–200 pages of invoices, contracts, damage descriptions, force-account labor records, and photos — must be reviewed for:

- **Eligibility** under the Stafford Act and program policy
- **Cost reasonableness** and documentation completeness
- **Compliance** with 2 CFR 200 procurement and cost principles
- **Duplication of benefits** (insurance, other federal funding)

This is expert-intensive, document-heavy, and slow — and errors are expensive: missed ineligible costs or documentation gaps surface later as OIG findings, deobligations, and audit recoupment, sometimes years after funds are spent.

It also has a **clean behavioral validation signal**: the reviewer either accepts the AI's eligibility determination/flag as-is, modifies it, or rejects it. That accept/modify/reject trace estimates *q* directly (see [paper §4.8](../../paper/draft-1.md)).

## Two conditions

| | Baseline (human) | AI-assisted |
|---|---|---|
| Reviewer time | 4.0 h | 1.5 h verify + 0.25 h rework |
| Loaded wage | $90/h | $90/h |
| Machine cognition (M) | $0 | $3.50 (tokens + retrieval/OCR) |
| Expected downstream error cost | $400 (8% × $5,000) | $200 (4% × $5,000) |
| Deliverable value | $2,000 | $2,100 |
| Validation confidence (q) | — | 0.88 |

In the AI condition, the model ingests the package, extracts cost line items, checks completeness against an eligibility checklist, and drafts the determination narrative; the human reviewer verifies the flags and the determination.

## Results

Run it yourself:

```bash
python evaluator/evaluate.py --input demos/fema-pa-review/workflow.json
```

| Metric | Value |
|---|---|
| Validated incremental value (ΔV) | **$100** / package |
| Net incremental value (ΔN) | **$499** / package |
| Metered machine cognition (M) | $3.50 |
| Cognitive Efficiency (ΔV / M) | **28.6×** |
| Token ROI (machine) | 142.6× |
| Token ROI (total) | **1.38×** |
| Human–AI Leverage (ΔV / H) | $57/h |
| Nonuse Penalty | **$499** / package |
| Overuse Penalty | $2.30 |
| Outcome-Adjusted AI Value | $1,648 |

## Interpretation — the non-obvious findings

**1. The value is throughput and risk, not better reviews.**
Deliverable quality barely moves (ΔV = $100). The economics come almost entirely from two places the headline output quality metric would miss: reviewer time (4.0 h → 1.75 h, a **2.3× capacity multiplier**) and halved expected error cost ($400 → $200). A dashboard tracking "review quality" would conclude AI did almost nothing here. A dashboard tracking cognitive efficiency sees a **$499/package** net gain.

**2. Token ROI (machine) at 142× is a vanity number.**
Token ROI (total) is 1.38×. The 100× gap is entirely human verification cost. This is the paper's central thesis showing up in a real domain: **the binding constraint is expert attention, not tokens.** The $3.50 of machine cognition is a rounding error; the 1.75 hours of reviewer time is the whole game. Optimizing model cost here is optimizing the wrong variable.

**3. The nonuse penalty compounds at scale.**
$499/package is the cost of *not* using AI on a package where it would help. Across a disaster with, illustratively, 10,000 project packages, that is **~$5M of forgone net value and ~22,500 reviewer-hours** that could have accelerated obligation of recovery funds to communities. The nonuse penalty, not the token bill, is the number a program office should care about.

**4. Overuse is negligible here — so don't over-engineer.**
The cheaper-config benchmark saves only $2.30/package. Effort spent shaving model cost is wasted; effort spent reducing the 12% of determinations the reviewer has to modify (raising *q*) is where the leverage is.

## Sensitivity: which assumptions matter?

The weakest assumption is the **$2,000 deliverable value anchor**. Good news: the headline metrics barely depend on it.

- **ΔN ($499)** depends on the *deltas* in cost and risk, plus ΔV ($100) — not on the $2,000 level. Change the anchor to $1,000 or $4,000 and ΔN is unchanged.
- **Leverage ($57/h)** depends on ΔV and human time — also independent of the anchor level.
- **CE (28.6×)** *does* scale with ΔV. If AI's consistency uplift is worth $300 instead of $100, CE triples to ~86×. This is the assumption most worth measuring.
- **Throughput (2.3×)** depends only on the time figures and is the most defensible number in the whole study.

**Takeaway:** report throughput and ΔN with confidence; treat CE as anchor-sensitive until ΔV is measured.

## How to make this real

Replace the modeled assumptions in [workflow.json](workflow.json) with measured values from a pilot:

1. Time 10–20 real package reviews under each condition (stopwatch per phase).
2. Log the reviewer's accept/modify/reject decision per AI flag → gives measured *q*.
3. Pull actual token + infra cost from API/billing.
4. For error cost, use the program's historical deobligation rate × average deobligation, or a panel estimate.
5. For deliverable value, the cleanest anchor is reviewer cost-to-produce; for the uplift, have a second senior reviewer score defensibility of AI-assisted vs. baseline packages blind.

Then open a PR moving this from `MODELED` to `MEASURED`. That single change turns this from a framework demonstration into a citable public-sector case study — the domain-credibility artifact.

## Files

- [workflow.json](workflow.json) — evaluator input with documented assumptions
- [results.json](results.json) — evaluator output
