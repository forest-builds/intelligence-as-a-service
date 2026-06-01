# Demos

Real workflow runs measured against the cognitive efficiency framework. Each demo produces evaluator output and feeds back into the paper. All domains are public-data-friendly and tool-agnostic.

| Demo | Domain | Status |
|---|---|---|
| [github-issue-triage](github-issue-triage/) | Open-source issue triage (public data) | ✅ Modeled case study (run through evaluator) |
| [research-synthesis](research-synthesis/) | AI-assisted literature review | Protocol ready |
| scientific-claim-verification | Checking whether citations support claims | Incoming |
| meeting-to-decision | Transcript → decisions, actions, risks | Incoming |

See also: [demo-video-script.md](demo-video-script.md) — 3–5 min script that walks the evaluator + the issue-triage case study.

To add your own: copy the closest existing demo folder, run the protocol, fill out the evaluator input template, and open a PR.

**Modeled vs. measured:** the issue-triage case study is *modeled* (transparent assumptions, run through the real tool) — it demonstrates the method and exposes which assumptions matter. Upgrading any demo from modeled to *measured* (real timed runs, logged accept/edit/discard decisions) is the highest-value contribution. Because GitHub issues are public, issue-triage is the easiest one to make real.
