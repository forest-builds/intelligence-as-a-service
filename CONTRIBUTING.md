# Contributing

This is an open research project. No affiliation, credentials, or permission required.

## Ways to contribute

### 1. Run a pilot and submit measurements

The fastest way to contribute real data.

1. Pick a demo protocol from [demos/](demos/)
2. Run it against your own workflow (any domain, any model)
3. Fill out [evaluator/input-template.json](evaluator/input-template.json) for each condition
4. Run `python evaluator/evaluate.py --input your-file.json --output results.json`
5. Open a PR adding your input + results to `demos/<domain>/runs/your-run.json`

Include a short description: what task, what model, what context. You can anonymize or aggregate numbers if needed.

### 2. Verify a citation

The paper's literature table (§3.6) lists effect directions without precise magnitudes or DOIs. Each unverified row is an open contribution.

1. Find a row in the table with no DOI or sourced effect size
2. Pull the primary source
3. Add the correct magnitude, year, venue, and DOI to the table
4. Open a PR with a note on what you changed and why

### 3. Add a behavioral validation signal domain

The §4.8 domain table is incomplete. Add a row for a domain not yet covered:

- What is the AI output?
- What is the behavioral signal (what action does the human take)?
- How would you compute $r_t$ (token retention or equivalent) from logs?

### 4. Build an evaluator module

The evaluator's behavioral log → $q$/$d$ estimator is generic. Domain-specific calibration will be more accurate.

Open issues list domains where a calibrated module would be valuable. Pick one, implement it, and open a PR against `evaluator/`.

### 5. Challenge a hypothesis

The paper lists H1–H8 as empirical predictions. If you have data or a strong argument against one, open an issue. A hypothesis that fails empirically is more valuable than one that goes untested.

### 6. Propose a benchmark

See [benchmarks/README.md](benchmarks/README.md). If you have a domain with a clean task definition and a measurable output, propose a benchmark spec as an issue.

## Standards

- **No unsupported claims.** If you add a number or assertion to the paper, cite the source.
- **Show your work.** Include raw evaluator input/output, not just derived metrics.
- **Flag uncertainty.** It is better to report $q = \text{unknown}$ than to guess.
- **Keep it task-level.** Aggregate metrics obscure the jagged frontier. Report per-task where possible.

## Questions

Open an issue. That is the right place for questions, proposals, and debate.
