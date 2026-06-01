# Roadmap — 90-Day Artifact Stack

The goal of the next 90 days is not introspection. It is a coherent body of work that lets serious people see the mission before it's fully explained. Judged by output, not effort.

**Scope discipline:** all public artifacts use domain-neutral, public-data-friendly workflows (open-source issue triage, literature review, claim verification, meeting-to-decision). No client-adjacent, government, grants, or emergency-management domains in public work. The framing is **AI-assisted knowledge work**.

## The credibility stack

| Layer | Artifact | Status |
|---|---|---|
| Intellectual | Working paper (cognitive efficiency framework) | ✅ Draft 1.1 |
| Mathematical | Variables, units, metric formulas | ✅ In paper §4 |
| Product | Cognitive Efficiency Evaluator (working CLI) | ✅ v0 + tests passing |
| Domain | GitHub issue triage case study | ✅ Modeled · ⬜ needs measured pilot |
| Distribution | Demo video | ⬜ Script done, record next |
| Public proof | Open repo | ✅ Live |

## Minimum viable seriousness (90-day targets)

- [x] 1 paper draft
- [x] 1 working app (evaluator, with passing regression test against the paper)
- [x] 1 case study (modeled — upgrade to measured)
- [ ] 1 demo video (script ready → record)
- [ ] 5 serious public writeups/posts
- [ ] 20 conversations with smart people / potential users
- [ ] 100 hours of focused building

## Sequenced next moves

### Now → 2 weeks
1. **Record the demo video** from [demos/demo-video-script.md](demos/demo-video-script.md). Tools already produce the on-screen proof.
2. **Upgrade the issue-triage case study to measured** — GitHub issues are public, so this is the easiest one to make real: sample 30–50 triaged issues, time baseline vs. AI-assisted, log accept/edit/discard for *q*. Turns a demo into a citable, fully-public case study.
3. **First public writeup**: the "151× vs. 0.65× — the model is free, attention is everything" finding from the issue-triage case study. Lead with the number, link the repo.

### 2 → 6 weeks
4. **Run the research-synthesis pilot** ([demos/research-synthesis/](demos/research-synthesis/)) on a real task — even on yourself. Produces a second *measured* run and feeds the paper's §6 / Appendix A (editorial open items O4/O7).
5. **Citation verification sweep** on the paper (editorial open items O1/O5) — replace directional effect sizes with sourced magnitudes + a real bibliography. This is the single biggest gap between "working paper" and "submittable."
6. **Build the Streamlit UI** for the evaluator so non-technical people can use it.
7. **Conversations**: take the case study to 5–10 people in AI tooling / dev-tools / AI-eval circles. Listen for whether the nonuse-penalty framing lands.

### 6 → 12 weeks
8. **Second + third domain case studies** — scientific claim verification and meeting-to-decision. Multiple neutral domains prove the framework generalizes.
9. **First benchmark spec** ([benchmarks/](benchmarks/)) with 3+ contributed runs.
10. **Behavioral-signal logging prototype** — instrument one real workflow to capture accept/edit/discard automatically and estimate *q* from logs (the §4.8 thesis, made real). This is the part that could become a product.

## The wedge

> As inference becomes a capability layer, organizations won't win by consuming more intelligence. They'll win by routing machine cognition through workflows that maximize validated value per unit of cost, latency, supervision, and risk — and by instrumenting those workflows to prove it.

Operate at the frontier of **converting model capability into measured value in AI-assisted knowledge work**. That lane is open.

## What not to do

- Don't treat every new idea as equally alive. Compress.
- Don't ship a wrapper and hope it looks like a company.
- Don't hide behind thought leadership without shipping the artifact underneath it.
- Don't fabricate case-study numbers. Modeled is fine if labeled; measured is the goal.
- Don't build public artifacts around client-adjacent, government, or grants/emergency-management domains. Keep it neutral.
