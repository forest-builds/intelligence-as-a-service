# notes.md — Editorial state of `intelligence-as-a-service.md`

**Current draft:** Draft 1.1 · **Last pass:** 2026-05-31 · **Target:** publishable working paper

This file is the running editorial tracker for the paper. It records what each pass changed, what's still open, and what to do next. The paper no longer carries its critique inline — that lives here.

---

## 1. Changelog

### Repo build-out (2026-05-31) — paper became a lab

Not a paper change, but the paper is now backed by working artifacts (see [ROADMAP.md](../ROADMAP.md)):

- **Evaluator implemented** (`evaluator/evaluate.py`) — computes all six metrics from a workflow run; standard-library Python, no deps. **Regression test passes**: reproduces this paper's §6 worked example exactly (CE 33.3×, ΔN $426.50, leverage $80/h, OAV $1,280). The tool and the paper provably agree.
- **Behavioral-log estimator** built — estimates $q$ and $d$ from accept/retain/submit traces (operationalizes §4.8).
- **FEMA Public Assistance case study** (`demos/fema-pa-review/`) — modeled scenario run through the tool. Key finding reinforces the thesis in a real domain: deliverable quality barely moves (ΔV $100), but reviewer time drops 2.3× and the nonuse penalty is $499/package; Token ROI machine 142× vs. total 1.38× — tokens are a rounding error, expert attention is the constraint.
- **Demo video script + 90-day roadmap** added.
- **Note for O4:** the §6 numbers are still illustrative; the FEMA case is *modeled*, not measured. First *measured* run (research-synthesis pilot or measured FEMA) remains the top open item.

### Draft 1.1 (2026-05-31) — added §4.8 behavioral validation signals

- **New section §4.8: Behavioral Validation Signals.** Core insight: $q$ and $d$ go unmeasured not because the concept is wrong but because the instrumentation layer hasn't been built. Every knowledge-work domain has an implicit behavioral trace — the delta between AI output and what the human ultimately submitted/sent/published. Formalizes $\hat{q} = \mathbb{E}[r_t]$ from the token-retention rate $r_t$. Includes a domain taxonomy table (code, docs, research, email, proposals, slides, support, legal, tutoring). Names the instrumentation layer — not the model — as the durable competitive asset.
- **Abstract updated** to surface the behavioral validation signal insight.
- **§2 roadmap sentence updated** to reference §4.8.
- **O3 partially resolved** — §4.8 shows how $q$ and $d$ can be estimated from behavioral traces without rubrics or annotation, which changes the nature of the open item (see updated O3 below).

### Draft 1 (2026-05-31) — executed the full revision roadmap
- **Math tightened + variables/units table (was Draft-1 item).** Added §4.1 notation table (all $V$, $C$, $M$, $H$, $q$, $d$ defined with units and boundary conditions). Rewrote every metric with consistent symbols. Token ROI now split into `ROI_machine` and `ROI_total` to stop the ambiguity about what's in the denominator.
- **Literature comparison table (was Draft-2 item).** Added §3.6: study × domain × design × effect direction × limitation × relevance. Toner-Rodgers included as a *cautionary* row, flagged not-reliable. Effect magnitudes deliberately left directional + flagged for verification.
- **Worked numerical example (was Draft-3 item).** Added §6: 1,500-word brief, no-AI vs. AI-assisted, full cost/value table and all six metrics derived. Punchline built in: Token-ROI(machine) ~71× is an artifact of human-time savings; the real constraint is the 2.5 h of supervision (Human–AI Leverage).
- **Self-measuring appendix instrument (was Draft-4 item).** Added Appendix A: fillable template for measuring this paper's own production.
- **Reduced societal scope (was Draft-5 item).** §3.5, §9, §10 trimmed; distribution/welfare reframed as boundary conditions on the evaluator's objective function. Conclusion now leads with the narrow, defensible claim (outcome-adjusted accounting + human–AI leverage as the binding constraint).
- **Resolved 3 of 5 "weakest claims":**
  - *Units not standardized* → fixed: $M$ pinned to a cost numéraire (default) with optional energy numéraire (§4.2).
  - *CE collapses into ROI* → fixed: §4.3 argues the divergence (high CE, low ROI) is the diagnostic, not a bug.
  - *Toner-Rodgers* → fixed: framed as contested/withdrawn throughout.
- **Housekeeping.** Removed the Draft-0 preamble and the critique block that was pasted onto the end of the paper; folded the evidence-base sentence into §3.

---

## 2. Open items

Ordered by what most blocks publishability.

| # | Item | Where | Status | Blocker |
|---|---|---|---|---|
| O1 | **Verify all cited effect sizes** against primary sources (Noy & Zhang, Brynjolfsson et al., Dell'Acqua et al., IMF, OECD). Replace directional language with sourced magnitudes + full citations/bibliography. | §3, §3.6 | Open | Needs literature pull; no bibliography section yet |
| O2 | **Overuse penalty still counterfactual.** $C_{AI}^*$ defined but only illustrated. Needs a real benchmarking protocol (model-swap / prompt-compression ladder) to estimate "minimum sufficient." | §4.6, §5.5 | Partial | Requires experimental design or pilot data |
| O3 | **$q$ and $d$ measurement.** §4.8 shows behavioral traces can estimate both without annotation. Remaining work: (a) design the logging schema for at least two non-code domains; (b) show empirically that $\hat{q}$ from token retention correlates with expert quality scores. | §4.8, §5.6 | Partial | Domain instrumentation design |
| O4 | **Worked example uses illustrative numbers.** Replace §6 figures with at least one real measured run (the pilot below feeds this directly). | §6 | Open | Run the pilot |
| O5 | **No bibliography / reference list.** Author names only; no years, venues, DOIs. | whole paper | Open | Depends on O1 |
| O6 | **Empirical designs not yet powered.** §7 lacks sample sizes, randomization detail, primary-outcome pre-registration. | §7 | Open | Pre-registration pass |
| O7 | **Appendix A is empty.** Self-measuring instrument is a template; populate with this paper's actual production data before submission. | Appendix A | Open | Track production now |

---

## 3. Strengths to preserve (don't lose these in editing)

1. **"Metered machine cognition"** is the right abstraction — avoids "tokens = intelligence" while keeping tokens economically meaningful.
2. **Nonuse / overuse pair** — most AI-ROI discussion only worries about waste/hype; the nonuse counterfactual is the differentiator.
3. **Human–AI leverage** is the likely publishable insight — the constraint is expert attention, not token volume. (Now the lead claim in §11.)
4. **Living-example appendix** — self-auditing without being gimmicky.
5. **Activity → output → validated value → operationalized value** separation — where most enterprise AI measurement fails.
6. **Behavioral validation signals (§4.8)** — the new sharpest edge. The reason CE is unmeasured isn't the framework, it's the missing instrumentation. This generalizes what Cursor does for code to every knowledge-work domain. Potentially the most original contribution in the paper.

---

## 4. Next steps (prioritized)

1. **Run the pilot (§5 below).** Feeds O4 (real worked example) and O2 (overuse benchmarking) and populates Appendix A (O7).
2. **Literature verification sweep** → closes O1 + O5; write the bibliography.
3. **Draft scoring rubrics for $q$ and $d$** → closes O3.
4. **Pre-register §7 designs** with sample sizes / primary outcomes → closes O6.
5. Optional Draft 2: a second worked example in a *non-writing* domain (code or sales) to show the framework generalizes.

---

## 5. Pilot study (ready to run)

A research-writing cognitive-efficiency pilot, on yourself or a small group — small enough to run, rigorous enough to be credible, directly aligned with the living-example thesis. This is the operationalized form of §7.2.

**Design — three workflows for a 1,500-word research brief:**
1. No AI.
2. AI drafting only.
3. AI drafting + AI critique + human citation verification.

**Track:** input tokens · output tokens · model cost · human time · claims generated · verified claims · removed unsupported claims · final quality (2–3 reviewers) · rework time · final usefulness rating.

**Primary metric:** validated claims per (dollar + human hour).
**Secondary metric:** final quality score / total AI-related cost.

**Maps to the framework:** primary metric ≈ $CE$ with a claims-based numerator; secondary ≈ $\text{ROI}_{\text{total}}$; the workflow-3 vs. workflow-2 contrast estimates the overuse/leverage of the critique+verification step (O2); all outputs drop straight into Appendix A (O7) and replace the illustrative §6 numbers (O4).
