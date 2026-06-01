# Case Study: Open-Source GitHub Issue Triage

**Type:** Modeled scenario (transparent assumptions, not a measured pilot)
**Domain:** Open-source software maintenance — domain-neutral, public-data-friendly
**Purpose:** Demonstrate the cognitive efficiency framework on a workflow every engineer understands, using fully public data.

> ⚠️ **This is a modeled scenario, not measured data.** Every number traces to a documented assumption in [workflow.json](workflow.json). The value is the *method* and the *interpretation*, not the specific figures. Because GitHub issues are public, this is one of the easiest case studies in the repo to upgrade to *measured* — see [How to make this real](#how-to-make-this-real).

## The workflow

Maintainers of popular open-source projects drown in issues. Each incoming issue needs to be:

- **Classified** (bug / feature / question / docs)
- **Deduplicated** against existing issues
- **Severity-estimated** (blocker vs. nice-to-have)
- **Routed** to the right area or maintainer
- **Responded to** — ideally fast, so contributors stay engaged

Maintainer attention is the scarce resource, and maintainer burnout is the well-documented failure mode. That makes triage a near-perfect test of the thesis: **the constraint is human attention, not compute.**

It also has a clean behavioral validation signal: the maintainer either accepts the AI's labels/draft response as-is, edits them, or discards them. That accept/edit/discard trace estimates *q* directly ([paper §4.8](../../paper/draft-1.md)).

## Two conditions

| | Baseline (maintainer) | AI-assisted |
|---|---|---|
| Maintainer time | 12 min | 4 min verify + 1 min edit |
| Loaded wage | $100/h | $100/h |
| Machine cognition (M) | $0 | $0.07 (LLM + embedding search) |
| Expected risk cost | $5 (misroute) | **$8** (bad auto-response to a contributor) |
| Deliverable value | $40 | $42 |
| Validation confidence (q) | — | 0.82 |

Note the **risk goes up** with AI here ($5 → $8): an auto-drafted response that's wrong or tone-deaf can alienate a contributor — a real community cost only partly offset by verification. The framework captures that instead of pretending AI is pure upside.

## Results

Run it yourself:

```bash
python evaluator/evaluate.py --input demos/github-issue-triage/workflow.json
```

| Metric | Value |
|---|---|
| Validated incremental value (ΔV) | **$2** / issue |
| Net incremental value (ΔN) | **$10.59** / issue |
| Metered machine cognition (M) | $0.07 |
| Cognitive Efficiency (ΔV / M) | 28.6× |
| Token ROI (machine) | 151.3× |
| Token ROI (total) | **0.65×** |
| Human–AI Leverage (ΔV / H) | $24/h |
| Nonuse Penalty | **$10.59** / issue |
| Overuse Penalty | $0.06 |
| Outcome-Adjusted AI Value | $26.44 |

## Interpretation — the non-obvious findings

**1. The two ROI numbers disagree by 230×, and that's the whole point.**
Token ROI on the machine cost alone is 151×. On total cost including the maintainer's 5 minutes, it's **0.65×** — below 1. The $0.07 of compute is invisible; the 5 minutes of maintainer attention is everything. Anyone optimizing the model bill is optimizing the wrong variable by two orders of magnitude. This is the paper's central claim, in a domain where it's impossible to miss.

**2. The value is throughput, not better triage.**
Per-issue quality barely moves (ΔV = $2). The economics come from time: 12 min → 5 min is a **2.4× throughput multiplier**. For a maintainer triaging 200 issues, that's the difference between a weekend lost and an afternoon. A "triage accuracy" dashboard would call this a wash; cognitive efficiency sees a real gain — and locates it correctly in capacity, not quality.

**3. AI raised risk, and the framework says so.**
Expected risk went from $5 to $8 because a bad auto-response carries community cost. The Outcome-Adjusted AI Value ($26.44) and the low *q* (0.82) both flag it: 18% of AI drafts needed editing, and the residual risk is real. The right optimization here is not a bigger model — it's raising *q* (better-grounded responses) and gating auto-replies behind review for sensitive issues.

**4. Overuse is a rounding error ($0.06).**
Don't waste effort shaving the $0.07 compute bill. Every dollar of improvement is in maintainer time and response quality.

## Sensitivity: which assumptions matter?

The weakest assumption is the **$40 deliverable-value anchor**. The headline metrics barely depend on its level:

- **ΔN ($10.59)** depends on cost and risk *deltas* plus ΔV ($2), not on the $40 level.
- **Throughput (2.4×)** depends only on the time figures — the most defensible number here.
- **Leverage ($24/h)** depends on ΔV and human time, not the anchor.
- **CE (28.6×)** scales with ΔV — if AI's consistency uplift is worth $6 instead of $2, CE triples. This is the assumption most worth measuring.

## How to make this real

GitHub issues are public, so this is highly reproducible:

1. Pick an active OSS repo with a public issue tracker.
2. Sample 30–50 recently-triaged issues.
3. For each: have a maintainer (or a careful annotator) triage cold, timing it — that's baseline.
4. Run an AI triage pass; have the maintainer verify, logging accept/edit/discard per label and per drafted response — that gives measured *q* and verification time.
5. Pull real token + embedding cost from the API.
6. Score triage correctness against the eventual ground-truth resolution.

Then open a PR moving this from `MODELED` to `MEASURED`. That single change turns a framework demo into a citable, fully-public case study.

## Files

- [workflow.json](workflow.json) — evaluator input with documented assumptions
- [results.json](results.json) — evaluator output
