# Demo: AI-Assisted Research Synthesis

**Status:** Protocol ready · Results incoming

This is the first Cognitive Efficiency Lab demo. It runs the pilot study described in the [working paper §7.2](../../paper/draft-1.md) and produces real measurements for the evaluator.

## Why this domain first

Research synthesis is easy to instrument, produces measurable claims, and directly mirrors the production of the paper itself. The behavioral validation signal is clean: a claim either survives into the final document (retained) or it doesn't (removed). No rubrics required.

## Protocol

### Three conditions

| Condition | Description |
|---|---|
| A — No AI | Human researcher produces the 1,500-word brief without AI assistance |
| B — AI draft | AI drafts the brief; human reviews and submits with edits |
| C — AI draft + critique + verification | AI drafts, AI critiques its own draft, human verifies citations and submits |

### What to track

Fill in [../../evaluator/input-template.json](../../evaluator/input-template.json) for each condition. Key measurements:

| Measurement | How to capture |
|---|---|
| Human time | Stopwatch per phase (framing, drafting, review, verification, rework) |
| Tokens consumed | From model API usage logs |
| Token cost | From API billing |
| Claims generated | Count distinct factual claims in the draft |
| Verified claims | Count claims confirmed against a source |
| Removed claims | Count claims deleted as unsupported |
| Quality score | 2–3 reviewers rate the final brief /10 independently |
| Rework time | Time spent correcting, rewriting, or removing AI output |

### Primary metrics

```
Primary:   Verified Claims / (Token Cost ($) + Human Hours)
Secondary: Final Quality Score / Total AI-Related Cost ($)
```

These are domain-specific instantiations of Cognitive Efficiency (ΔV / M).

### Behavioral signal (passive capture)

If using an editor that supports it, log each AI-generated paragraph as an observation:

```json
{
  "ai_tokens": 120,
  "retained_tokens": 98,
  "submitted": true
}
```

The evaluator uses this to estimate $q$ without manual scoring.

## Submit your results

Run the evaluator on your completed workflow files:

```bash
python ../../evaluator/evaluate.py --input condition-a.json --output results-a.json
python ../../evaluator/evaluate.py --input condition-b.json --output results-b.json
python ../../evaluator/evaluate.py --input condition-c.json --output results-c.json
```

Open a PR adding your results to `demos/research-synthesis/runs/` with a short description of your context (domain, task, model used). No affiliation required.

## What we expect to find

Based on the paper's worked example (§6) and hypotheses H1–H4:

- Condition B will show high CE (tokens convert well) but lower total ROI than it appears, because review burden is the real cost
- Condition C will reduce $C_{risk}$ and unsupported claims at the cost of added token spend — whether the overuse penalty is positive or negative is the key empirical question
- The five unsupported claims removed per run (approximate) will account for most of the human review time
