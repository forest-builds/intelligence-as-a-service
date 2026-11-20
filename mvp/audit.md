# Repo Audit For MVP v1

## Current State

The repo already has the important spine:

- `paper/draft-1.md`: credible theory and metric definitions
- `evaluator/evaluate.py`: working metric engine
- `evaluator/test_evaluate.py`: regression tests against the paper example
- `demos/github-issue-triage/`: concrete case study with measured-style output
- `ROADMAP.md`: clear next steps

The missing piece is a low-friction artifact a normal person can use before they understand the paper.

## Product Gap

The evaluator asks for accounting-ready inputs: baseline value, AI value, token cost, risk cost, and validation confidence. That is right for research, but too cold for first contact.

MVP v1 should accept fuzzy, natural fields:

- what subscriptions do you pay for?
- how often do you use them?
- what task are you using AI for?
- how long would it take manually?
- how long does it take with AI?
- how much review and rework does it create?
- how often does the output actually get used?
- what is your salary, loaded wage, company revenue, or per-task value proxy?

Then it should translate those into the existing metric spine.

## Recommendation On Sibling Repos

Do not port a full stack from `archetype`, `the-state`, or `finance` yet.

- `archetype` has a useful React/Vite frontend pattern, but it brings a frontend build system before this repo needs one.
- `the-state` is a richer Python service/app structure, but the MVP does not need service complexity.
- `finance` may have CLI hygiene worth copying later, but the current evaluator CLI is already enough.

For v1, use a standalone HTML calculator and keep the Python evaluator as the serious backend/math artifact. If usage proves real, then migrate the calculator into a React app or Streamlit UI.

## Next Build Steps

1. Add export from the browser calculator to evaluator-compatible JSON.
2. Add a handful of presets: resume/application, coding, research synthesis, customer support, founder strategy.
3. Add a one-week worksheet for measured usage.
4. Add a public demo flow: fill calculator, export JSON, run evaluator, compare projected vs. measured.

