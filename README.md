# Intelligence as a Service
### *From Token Consumption to Cognitive Efficiency: Measuring ROI in Metered Machine Intelligence*

A framework for token-level productivity accounting, nonuse penalty, and human–AI leverage.

**Status:** Draft 1 · active development · open to contribution

---

## What this is

As AI becomes a variable production input, raw token consumption is an incomplete measure of productivity. This project proposes **cognitive efficiency** — validated incremental value per unit of metered machine cognition — as the right accounting layer for enterprise AI.

The core claim is narrow and defensible: **AI productivity requires outcome-adjusted accounting of metered cognition, and the binding constraint is human–AI leverage (expert attention and validation capacity), not token volume.**

## Read the paper

→ **[intelligence-as-a-service.md](intelligence-as-a-service.md)** — Draft 1 working paper

Sections:
1. Abstract
2. Introduction
3. Literature Review (with comparison table)
4. Conceptual Framework — notation, variables, and the CE ≠ ROI argument
5. Proposed Metrics — Token ROI, Cognitive Efficiency, Human–AI Leverage, Nonuse/Overuse Penalties, OAV
6. **Worked Numerical Example** — 1,500-word brief, all six metrics derived
7. Empirical Research Designs
8. Hypotheses
9. Limitations
10. Ethics and Policy
11. Conclusion
12. Appendix A — Self-measuring instrument (the paper measuring its own production)

## Key concepts

| Metric | Formula | What it surfaces |
|---|---|---|
| Cognitive Efficiency | ΔV / M | How well machine cognition converted to validated value |
| Token ROI (machine) | ΔN / (C_tok + C_inf) | Return per dollar of inference |
| Token ROI (total) | ΔN / C_AI | Return per dollar of full AI-attributed cost |
| Human–AI Leverage | ΔV / H | Validated value per hour of human supervision |
| Nonuse Penalty | ΔN (when > 0) | Cost of not using AI where it would have helped |
| Overuse Penalty | C_AI − C*_AI | Excess cost without comparable incremental value |

The worked example (§6) shows why Token ROI (machine) can look like ~71× while Token ROI (total) is ~1.75× — the gap is entirely explained by human supervision cost, which is the real binding constraint.

## Editorial state

→ **[notes.md](notes.md)** — living changelog and open-items tracker

What's done in Draft 1, what's still open, and the prioritized next steps. The biggest open items before submission:

- **O1/O5** — verify all cited effect sizes against primary sources; write the bibliography
- **O2** — turn the overuse counterfactual into a real benchmarking protocol
- **O3** — build scoring rubrics for validation confidence *q* and deployment rate *d*
- **O4** — replace the illustrative §6 numbers with at least one real measured run (the pilot)
- **O7** — populate Appendix A with this paper's actual production data

## Pilot study (ready to run)

The paper proposes its own measurement. The pilot compares three workflows for producing a 1,500-word research brief:

1. No AI
2. AI drafting only
3. AI drafting + AI critique + human citation verification

Primary metric: **validated claims per (dollar + human hour)**
Secondary metric: **final quality score / total AI-related cost**

Results from any run of this pilot can be submitted as a contribution (see below).

## Contributing

This is an open research project. Contributions welcome:

- **Run the pilot** and submit your measurements (fill out Appendix A)
- **Verify citations** — check a primary source from §3.6, add the correct effect size + DOI
- **Write a worked example** in a non-writing domain (code, sales, education)
- **Propose a scoring rubric** for *q* (validation confidence) or *d* (deployment rate) in a specific domain
- **Open an issue** with a challenge to any hypothesis

No academic affiliation required. Cite, fork, use commercially — see [LICENSE](LICENSE).

## Evidence base

| Author(s) | Domain | Design |
|---|---|---|
| Noy & Zhang | Professional writing | Randomized experiment |
| Brynjolfsson, Li & Raymond | Customer support | Field / quasi-experiment |
| Dell'Acqua et al. | Consulting | Field experiment |
| OECD (*Miracle or Myth?*) | Macroeconomy | Modeling / review |
| IMF (labor exposure) | Cross-country labor | Exposure analysis |
| Suh & Oh | Time use | Empirical study |
| Wu & Deng | Token economics | Systems / theory |
| Jiang | Token energy | Theory |
| Toner-Rodgers | Materials discovery | ⚠️ **validity concerns, withdrawn** — cited as cautionary case only |

Full details and limitations in [§3.6 of the paper](intelligence-as-a-service.md).

## License

[MIT](LICENSE) — do whatever you want, attribution appreciated.
