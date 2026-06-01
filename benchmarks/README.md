# Benchmarks

Domain-specific cognitive efficiency benchmarks — standardized tasks with known baselines, used to compare models, workflows, and configurations against each other.

A benchmark here is not a leaderboard. It is a **reference workflow**: a defined task, a scoring protocol, and a growing set of logged runs that let you answer:

- Is workflow A more cognitively efficient than workflow B on this task type?
- Does a stronger model improve CE or just raise cost?
- What is the overuse penalty of using GPT-5 vs. a fine-tuned smaller model for this task?

## Incoming benchmarks

| Benchmark | Domain | Primary metric |
|---|---|---|
| `research-brief-1500` | Research synthesis | Verified claims / ($ + human-hours) |
| `compliance-doc-review` | Regulatory document review | Accurate flags / ($ + human-hours) |
| `pr-bug-resolution` | Software engineering | Accepted PRs / $ machine cognition |
| `sales-account-research` | Business development | Qualified leads / $ AI cost |

## Format

Each benchmark folder will contain:
- `spec.md` — task definition, scoring rubric, baseline protocol
- `runs/` — contributed measurement files (evaluator output)
- `leaderboard.md` — aggregated CE scores across runs, models, and configurations

## Contribute a run

Pick a benchmark spec, run your workflow against it, submit your evaluator output. See [CONTRIBUTING.md](../CONTRIBUTING.md).
