# Cognitive Efficiency Lab

**The frontier rewards model capability. We measure whether organizations convert it into value.**

As inference becomes a capability layer, the winning question is not "how much AI did we use?" It is: **how much validated value did we create per unit of machine cognition, human attention, cost, and risk?**

This lab builds the theory, math, tooling, and evidence base for answering that question.

---

## The stack

| Layer | Artifact | Status |
|---|---|---|
| Theory | [Working paper](paper/draft-1.md) — cognitive efficiency framework | Draft 1 |
| Math | Variables, units, and metric formulas | In paper §4 |
| Tool | [Cognitive Efficiency Evaluator](evaluator/) | Skeleton |
| Demos | [Research synthesis workflow](demos/research-synthesis/) | Protocol ready |
| Benchmarks | [Domain benchmarks](benchmarks/) | Incoming |

---

## Core thesis

Token consumption is not cognitive productivity.

The relevant measure is **cognitive efficiency**: validated incremental value produced per unit of metered machine cognition consumed.

$$CE = \frac{\Delta V}{M}$$

Where:
- $\Delta V$ = validated incremental value (outcome improved vs. baseline)
- $M$ = metered machine cognition (dollars of inference cost, by default)

This is not ordinary ROI. ROI asks whether the whole sociotechnical process paid off. Cognitive efficiency isolates the machine-cognition input and asks how well it was converted — which surfaces the real binding constraint: **human–AI leverage** (expert attention and validation capacity), not token volume.

---

## Key metrics

| Metric | Formula | What it surfaces |
|---|---|---|
| Cognitive Efficiency | ΔV / M | Machine cognition → validated value conversion rate |
| Token ROI (machine) | ΔN / C_machine | Return per dollar of inference |
| Token ROI (total) | ΔN / C_AI | Return per dollar of full AI-attributed cost |
| Human–AI Leverage | ΔV / H | Validated value per hour of human supervision |
| Nonuse Penalty | ΔN when > 0 | Cost of not using AI where it would have helped |
| Overuse Penalty | C_AI − C*_AI | Excess cost without comparable incremental value |
| Outcome-Adjusted AI Value | V · q · d − C_risk | Value after accounting for validation and deployment |

---

## The instrumentation insight

The reason cognitive efficiency goes unmeasured is not conceptual. It is infrastructural.

Every knowledge-work domain has an implicit **behavioral validation signal** — the delta between what the AI produced and what the human ultimately submitted, sent, published, or acted on. This signal encodes $q$ (validation confidence) and $d$ (deployment rate) without surveys or rubrics.

| Domain | AI output | Behavioral signal |
|---|---|---|
| Code | Suggested completion | Accept / edit / revert |
| Documents | Paragraph or section | Kept verbatim / edited / deleted |
| Research | Claim with citation | Survived final draft / removed |
| Email | Draft reply | Sent as-is / edited / discarded |
| Proposals | Section of a bid | Included in submission / cut |
| Customer support | Suggested response | Sent / escalated / rewritten |
| Legal | Draft clause | Survived redline / struck |

The instrumentation layer — not the model — is the durable competitive asset.

---

## Read the paper

→ **[paper/draft-1.md](paper/draft-1.md)** — full working paper, Draft 1

Includes: notation and variables table · literature comparison table · worked numerical example (1,500-word brief, all six metrics) · empirical research designs · hypotheses · self-measuring appendix.

Editorial state: **[paper/editorial-notes.md](paper/editorial-notes.md)**

---

## The evaluator

→ **[evaluator/](evaluator/)**

A tool that takes an AI-assisted workflow run and returns a cognitive efficiency score and full metric breakdown. Input schema defined. Python implementation in progress.

**Try it:** fill out [evaluator/input-template.json](evaluator/input-template.json) with your own workflow data and run `python evaluator/evaluate.py`.

---

## Demos

→ **[demos/research-synthesis/](demos/research-synthesis/)**

The first demo: AI-assisted research synthesis. Three-condition pilot comparing no AI, AI drafting only, and AI drafting + critique + human verification. Primary metric: validated claims per (dollar + human hour).

More demos incoming: enterprise document review · agentic coding workflow · AI-assisted compliance testing.

---

## Contributing

This is an open research project. No affiliation required.

Ways to contribute:

- **Run a pilot** — instrument a workflow against the [research-synthesis protocol](demos/research-synthesis/protocol.md) and submit your measurements
- **Verify a citation** — check a primary source from the [literature table](paper/draft-1.md#36-literature-comparison), add the correct effect size and DOI
- **Add a domain** — add a behavioral validation signal row for a domain not yet covered
- **Build an evaluator module** — implement a domain-specific $q$/$d$ estimator from behavioral logs
- **Open an issue** — challenge a hypothesis, propose a benchmark, flag a weak claim

See [CONTRIBUTING.md](CONTRIBUTING.md).

---

## License

[MIT](LICENSE) — use freely, attribution appreciated.
