# From Token Consumption to Cognitive Efficiency: Measuring ROI in Metered Machine Intelligence

*A Framework for Token-Level Productivity Accounting, Nonuse Penalty, and Human–AI Leverage*

> **Draft 1 (2026-05-31).** This revision incorporates the editorial roadmap tracked in `notes.md`: tightened notation and a variables/units table (§4), a literature comparison table (§3), one fully worked numerical example (§6), a self-measuring appendix instrument (Appendix A), and reduced societal-scope language in favor of the narrower publishable claim. **Citation note:** effect sizes attributed to specific studies below are approximate and flagged for verification before submission; per this paper's own thesis, unverified claims must not be booked as established value.

---

## 1. Abstract

Generative artificial intelligence is turning machine cognition into a measurable, priced, and increasingly routable economic input. The most visible unit of this input is the *token*: the unit through which many large language models read, generate, price, and report usage. Yet token consumption is not equivalent to productivity. A system may consume many tokens and produce little value; it may consume more tokens than a simpler workflow but reduce downstream error; or it may consume few tokens while requiring extensive human rework. As AI systems expand beyond text into audio, image, video, agents, tool use, simulation, and robotics, tokens should be understood as an early and partial proxy for a broader category: *metered machine cognition*.

This paper proposes a framework for measuring the economic return on consumed machine intelligence. The central concept is **cognitive efficiency**: validated incremental value produced per unit of metered machine cognition consumed. The framework distinguishes raw token usage, AI cost, useful output, validated value, human supervision burden, rework, latency, risk, nonuse opportunity cost, and overuse waste, and it pins each to defined variables and units (§4). It introduces task-level **Token ROI**, **Cognitive Efficiency**, the **Human–AI Leverage Ratio**, the **Nonuse Penalty**, the **Overuse Penalty**, and **Outcome-Adjusted AI Value** as candidate metrics for enterprise AI accounting and productivity research, and it demonstrates them on one worked example (§6).

The core claim is not that more AI usage automatically creates more value. Rather, as AI becomes a variable economic input, the competitive advantage will likely belong to individuals and organizations that can route, compress, supervise, validate, and operationalize machine cognition better than peers. The distinctive contribution relative to ordinary ROI is the isolation of the *machine-cognition input* in the denominator (cognitive efficiency) from the *net financial return of the whole sociotechnical process* (ROI) — a separation that surfaces the real binding constraint: expert attention and validation capacity, not token volume. The paper further argues that the reason cognitive efficiency has been unmeasured in practice is not conceptual but infrastructural: the variables that most matter ($q$, validation confidence; $d$, deployment rate) require **behavioral validation signals** — implicit traces of whether AI output was accepted, modified, or discarded — which exist in every knowledge-work domain but are only routinely captured today in software engineering.

## 2. Introduction

The first phase of generative AI adoption has largely been measured through access and activity: number of users, seats, prompts, tokens, workflows automated, or applications deployed. These measures are useful but incomplete. They measure *contact* with AI systems, not *economic conversion*. A company with high token volume may be learning rapidly, but it may also be burning compute on poorly specified tasks. A team with low token usage may be disciplined, but it may also be leaving value unrealized by failing to use AI where it would improve speed, quality, or decision-making.

This distinction matters because generative AI is not merely a software category. It is a new form of variable production input. The marginal cost of producing drafts, analyses, classifications, code, images, summaries, simulations, and recommendations is increasingly mediated by metered machine intelligence. In current language models this metering is token-based. In multimodal and agentic systems the meters may include audio seconds, image tokens, video frames, tool calls, memory retrievals, reasoning steps, simulation runs, or robotic actions. The economic object is not the token itself. The deeper object is *consumed machine cognition*: computationally generated inferential work applied to human goals.

The problem is that consumption is not value. A token is a measurable unit of input–output activity, not a unit of correctness, usefulness, originality, scientific validity, business impact, or social welfare. Treating token usage as a productivity metric risks repeating a familiar error from earlier waves of digital transformation: confusing system activity with organizational improvement. Email volume is not coordination quality. Dashboard views are not decision quality. Cloud spend is not software value. AI token consumption is not cognitive productivity.

This paper argues that AI adoption requires a new accounting layer: **cognitive efficiency measurement**. Cognitive efficiency asks how effectively consumed machine intelligence is converted into *validated incremental value*. The word "validated" is essential. AI output has economic value only when it changes an outcome: a task is completed faster, a decision improves, a customer issue is resolved, a risk is avoided, a product is improved, a scientist identifies a better candidate, a student learns more effectively, or a worker reallocates time to higher-value activity. Unvalidated output may still be useful as exploration, but it should not be booked as realized value.

The core thesis is that raw token consumption is an incomplete measure of AI productivity. The relevant metric is the validated incremental value created per unit of AI-related cost — including token cost, compute and infrastructure cost, human supervision, rework, latency, error risk, coordination cost, and downstream impact. This does *not* imply that fewer tokens are always better. Sometimes longer context, redundancy, debate, exploratory reasoning, or multiple candidate generations improve quality and reduce downstream error. A cognitively efficient system is not necessarily a minimal-token system. It is a system that uses *sufficient* machine cognition to produce validated outcomes with minimal avoidable waste.

This framing introduces two countervailing penalties. The **nonuse penalty** is the opportunity cost of not using AI when AI assistance would have improved speed, quality, learning, revenue, or decision quality. It is an economic counterfactual, not a moral judgment. The **overuse penalty** is the cost of excessive, poorly directed, or low-quality AI usage. High token consumption can indicate productive search, but it can also indicate confusion, weak task framing, poor judgment, or a workflow that substitutes machine verbosity for human clarity.

The paper proceeds as follows. Section 3 reviews the relevant literature and consolidates it in a comparison table. Section 4 develops the conceptual framework with explicit notation and units, concluding with §4.8 on behavioral validation signals — the instrumentation layer that makes $q$ and $d$ measurable in practice. Section 5 defines the proposed metrics. Section 6 walks through one worked numerical example. Section 7 outlines empirical research designs. Section 8 states hypotheses. Sections 9 and 10 discuss limitations and ethics. Section 11 concludes. Appendix A provides a self-measuring instrument applied to this paper.

## 3. Literature Review

The evidence base is mixed and uneven. Several studies show task-level gains in professional writing, customer support, and consulting-like knowledge work; others caution that gains are jagged, that micro gains do not automatically translate to firm or macro productivity, and that some headline results have failed validation. The framework in this paper is built to accommodate exactly this unevenness.

### 3.1 Generative AI and worker productivity

Early experimental studies suggest generative AI can improve performance on specific knowledge-work tasks, but magnitude and distribution vary. Noy and Zhang's experiment on professional writing reports that access to ChatGPT reduced completion time and raised output quality among college-educated professionals. The result matters not merely because AI improved speed but because speed and quality moved together — central to any ROI framework, since time savings alone do not imply value if quality deteriorates.

Brynjolfsson, Li, and Raymond study generative AI in customer support and find productivity gains, particularly for less-experienced workers. This suggests AI may function partly as a knowledge-transfer mechanism, embedding patterns from higher-performing workers into tools that assist lower-performing ones. For cognitive efficiency, the marginal value of AI consumption may therefore differ by worker skill, task familiarity, and feedback-loop quality.

Dell'Acqua and coauthors introduce the "jagged technological frontier." Their field experiment with consultants shows AI can improve performance on tasks inside the model's frontier while harming it on tasks outside. The same model, worker, and workflow may produce gains in one task and losses in another. Cognitive efficiency must therefore be measured at the **task level**, not only at the seat, department, or enterprise level.

### 3.2 Firm-level and macro translation

Micro gains do not automatically become firm or macro gains. The OECD's *Miracle or Myth?* analysis addresses the difficulty of translating task-level performance into macroeconomic productivity; translation depends on adoption rates, sectoral exposure, input–output linkages, complementary investment, and organizational redesign. The implication is direct: usage metrics that stop at activity cannot tell whether AI is improving output, profitability, quality, or resilience.

Organizations also absorb gains ambiguously. A worker may complete the same output faster, raise quality, produce more, spend more time on review, shift time to coordination, or capture savings as leisure. Suh and Oh's work on time reallocation suggests time saved through AI may not automatically appear as measured output. From the worker's welfare perspective the value may be positive; from the firm's accounting perspective it may be zero unless output, quality, speed, retention, or capacity improves. Cognitive efficiency therefore depends on the evaluator's objective function, which must be stated explicitly.

### 3.3 High-leverage and scientific work

AI's value may be largest in high-leverage domains where small improvements in search, prioritization, or decision quality produce large downstream effects — scientific discovery, drug development, materials science, engineering, software, finance, emergency management. But claims of AI-driven scientific acceleration require caution. Toner-Rodgers' widely discussed paper on AI-assisted materials discovery initially appeared to show large effects on discoveries, patents, and product innovation, but subsequent institutional validity concerns and withdrawal reporting mean it **should not be treated as settled evidence**. It is best used as a cautionary case for why validation, auditability, and replication are central to AI productivity research.

The broader point survives without that paper: in high-leverage domains, AI value depends less on output volume than on the quality of candidate generation, filtering, validation, and human judgment. A model that generates 1,000 hypotheses is valuable only if the human–machine system can identify which deserve scarce testing resources; otherwise AI can expand the search space faster than the validation system can absorb it. The denominator here is not only token cost — it includes lab time, expert review, opportunity cost, false positives, false negatives, and downstream risk.

### 3.4 Token economics and infrastructure

Tokens currently function as a unit of accounting for many AI systems, structuring pricing, rate limits, context windows, usage logs, and optimization. But tokens are not homogeneous units of value: input, cached input, output, reasoning, image, and audio tokens differ in cost and economic meaning, and tool calls, retrieval, code execution, and agentic actions introduce costs not well captured by raw token count.

Wu and Deng frame computational token economics as a problem constrained by real-time value accounting, resource allocation, and system architecture; their "token economics trilemma" highlights tradeoffs among granularity, latency, and optimality — the more precisely one values each unit of machine cognition, the harder it becomes to do so in real time at scale. Jiang's energy-based framing treats tokens as energy-indexed computational units, a reminder that AI costs are tied to hardware, energy, cooling, and infrastructure utilization, and that a cognitive efficiency framework should support an energy or carbon numéraire where data exist.

### 3.5 Labor exposure and societal ROI (scope-limited)

The IMF's work on AI and labor exposure emphasizes uneven effects across countries, occupations, and workers, with advanced economies more exposed because their employment structures contain more cognitive-intensive roles. Exposure can mean substitution risk *or* complementarity potential — the same system can reduce labor demand in one context and raise worker productivity or bargaining power in another. This paper treats distributional and welfare questions as boundary conditions on the evaluator's objective function (§4.1, §9–10) rather than as its primary subject; the central contribution is a measurement layer, not a welfare verdict.

### 3.6 Literature comparison

| Study (author) | Domain | Design | Reported direction of effect* | Key limitation | Relevance to cognitive efficiency |
|---|---|---|---|---|---|
| Noy & Zhang | Professional writing | Randomized experiment | Faster completion *and* higher quality | Short, stylized tasks | Speed and quality can move together; numerator needs both |
| Brynjolfsson, Li & Raymond | Customer support | Field / quasi-experiment | Productivity gain, largest for novices | Single firm/context | Marginal value of AI varies by worker skill |
| Dell'Acqua et al. | Consulting | Field experiment | Gains inside frontier; losses outside | Frontier is task-specific | Measure CE at the task level, not the seat |
| OECD (*Miracle or Myth?*) | Macroeconomy | Modeling / review | Potential but uncertain macro gains | Strong translation assumptions | Activity ≠ firm or macro output |
| IMF (labor exposure) | Cross-country labor | Exposure analysis | High exposure, esp. advanced economies | Exposure ≠ realized outcome | Substitution vs. complementarity shapes societal ROI |
| Suh & Oh | Time use | Empirical study | Time saved ≠ measured output | Redeployment unobserved | Realized value depends on redeployment of saved time |
| Wu & Deng | Token economics | Systems / theory | Granularity–latency–optimality trilemma | Conceptual | Constrains denominator design and real-time CE accounting |
| Jiang | Token energy | Theory | Tokens as energy-indexed units | Conceptual | Supports an energy/carbon numéraire for CE |
| Toner-Rodgers | Materials discovery | Field (contested) | Large effects claimed — **validity concerns, withdrawn** | **Not reliable evidence** | Cautionary case: validation and replication are central |

\* Directions are summarized from the cited literature and are **approximate**; specific magnitudes must be verified against primary sources before submission.

## 4. Conceptual Framework

### 4.1 Notation, variables, and units

The framework is defined per task *i* and per evaluator with an explicit objective function (firm net value, worker welfare, social welfare, or scientific value). Unless stated otherwise, value and cost are expressed in a common currency numéraire (USD); an alternative energy numéraire (kWh or kgCO₂e) may be substituted in the denominator of cognitive efficiency where data exist.

| Symbol | Name | Unit | Definition |
|---|---|---|---|
| $V_{AI}$ | AI-assisted outcome value | $ | Validated value of the deliverable/decision produced with AI |
| $V_0$ | Baseline outcome value | $ | Validated value of the same task without AI |
| $\Delta V$ | Validated incremental value | $ | $V_{AI} - V_0$ |
| $C_{tok}$ | Token / inference cost | $ | Priced model usage (input, output, cached, reasoning, etc.) |
| $C_{inf}$ | Compute / infrastructure cost | $ | Serving, retrieval, tool execution, storage beyond tokens |
| $C_{hr}$ | Human supervision cost | $ | Framing + review + validation time × loaded wage |
| $C_{rw}$ | Rework cost | $ | Correction, cleanup, reconstruction time × wage |
| $C_{risk}$ | Expected risk cost | $ | $P(\text{error}) \times \text{cost of error}$ (hallucination, omission, bias, unsafe action) |
| $C_{coord}$ | Coordination cost | $ | Added handoff/communication overhead |
| $C_{AI}$ | Total AI-related cost | $ | $C_{tok}+C_{inf}+C_{hr}+C_{rw}+C_{risk}+C_{coord}$ |
| $C_0$ | Baseline total cost | $ | Full cost of the no-AI process (mostly human time) |
| $M$ | Metered machine cognition | $ (or kWh) | Weighted machine-cognition consumed; see §4.2 |
| $H$ | Human supervision time | hours | Framing + review + validation + rework time |
| $d$ | Deployment rate | $[0,1]$ | Share of output actually used in a decision/product/workflow |
| $q$ | Validation confidence | $[0,1]$ | Probability output is correct/acceptable after review |

Boundary conditions: (i) $V_{AI}, V_0$ are *validated* values — exploratory or unverified output enters at $q<1$, not at face value; (ii) all costs are marginal to the task and attributed to the period in which they occur; (iii) the no-AI baseline $V_0, C_0$ is itself time-varying (see §9) and must be dated.

### 4.2 Tokens as the current meter; $M$ as the general denominator

Tokens are best understood as the current visible meter for one class of machine cognition — not intelligence itself, but units through which language models process and emit information. Because they are measurable, priceable, and optimizable, they become economically important. A useful (bounded) analogy is electricity: a kilowatt-hour is not "work" in the human sense, but metering turns an invisible capability into an accountable, priceable, optimizable input. The analogy should not be overstated — tokens are model-, modality-, and provider-dependent and not directly comparable across systems.

To make the denominator concrete and resolve the "units are not standardized" objection, define metered machine cognition as a **cost-weighted composite pinned to a numéraire**:

$$M = \sum_i w_i \, u_i$$

where $u_i$ are usage quantities (text tokens, image tokens, audio seconds, tool calls, retrievals, agent steps) and $w_i$ are weights. By default the weights are the **marginal monetary cost** of each unit, so $M$ reduces to dollars and is comparable across modalities and providers; $M = C_{tok}+C_{inf}$ in the pure-LLM case. Where energy data exist, $w_i$ may instead be marginal energy, yielding an energy numéraire. This makes $M$ explicit, reproducible, and provider-portable rather than an abstract "AI unit."

### 4.3 Cognitive efficiency — and why it is not ordinary ROI

**Cognitive efficiency** is validated incremental value per unit of metered machine cognition:

$$CE = \frac{\Delta V}{M}$$

This is deliberately *not* the same object as ROI. ROI (§4.4) puts *net* value over *total* cost, including human time; it answers "did the whole sociotechnical process pay off?" Cognitive efficiency isolates the **machine-cognition input** in the denominator and asks a narrower question: "how well did we convert metered machine cognition into validated value?" The two come apart in the case that matters most: cheap tokens plus heavy human review can yield *high* $CE$ (tokens converted efficiently) and *low or negative ROI* (the process lost money on supervision). That divergence is the diagnostic signal — it tells you the binding constraint is human attention, not model spend, and points directly to the Human–AI Leverage Ratio (§4.7). A framework that collapsed $CE$ into ROI would hide exactly this.

$CE$ should not be read as "minimize tokens." In some workflows more tokens raise $\Delta V$ by reducing ambiguity, improving reasoning, generating alternatives, or lowering error risk; in others they are waste. The efficient operating point is task-dependent: enough machine cognition to improve the outcome, not so much that marginal consumption yields little or negative incremental value.

### 4.4 Token ROI

Token ROI is the net return on AI relative to its cost. Net incremental value of using AI on a task is the change in (value − cost) versus baseline:

$$\Delta N = (V_{AI} - C_{AI}) - (V_0 - C_0)$$

Two ROI variants, reported together to avoid ambiguity:

$$\text{ROI}_{\text{machine}} = \frac{\Delta N}{C_{tok}+C_{inf}} \qquad \text{ROI}_{\text{total}} = \frac{\Delta N}{C_{AI}}$$

$\text{ROI}_{\text{machine}}$ is the return per dollar of machine cognition; $\text{ROI}_{\text{total}}$ is the return per dollar of the full AI-attributable cost including supervision. When the two diverge sharply, human cost dominates — again pointing to leverage, not tokens.

### 4.5 Nonuse penalty

The nonuse penalty is the counterfactual opportunity cost of *not* using AI where it would have improved the outcome:

$$\text{Nonuse Penalty} = (V_{AI} - C_{AI}) - (V_0 - C_0) = \Delta N \quad (\text{when } \Delta N > 0)$$

It matters because AI governance often focuses on overuse, misuse, and risk while undercounting the cost of avoiding useful AI: slower research, worse service, weaker decision support, lower learning velocity, higher operating cost. It is not a moral charge — confidentiality, regulation, task unsuitability, reliability concerns, lack of validation, or human-development goals are valid reasons to abstain. It is an economic counterfactual only.

### 4.6 Overuse penalty

The overuse penalty is the cost of excessive or inefficient usage relative to a *minimum sufficient* AI-assisted process achieving a comparable validated outcome:

$$\text{Overuse Penalty} = C_{AI} - C_{AI}^{*}$$

where $C_{AI}^{*}$ is the cost of the cheapest configuration (smaller model, shorter prompt, retrieval compression, better template, fewer agent steps) that reaches a statistically comparable $V_{AI}$ at comparable $q$. $C_{AI}^{*}$ is counterfactual and must be **estimated by benchmarking** (§5.5), not assumed. The conceptual point stands regardless: organizations may mistake AI *intensity* for AI *maturity*. The goal is effective conversion, not maximum consumption.

### 4.7 Human–AI leverage

Human–AI leverage is validated incremental value per unit of human supervision time:

$$\text{Leverage} = \frac{\Delta V}{H}$$

AI does not eliminate human judgment in most valuable workflows; it relocates it — from drafting to framing, searching to filtering, producing to validating, execution to orchestration. If output requires too much review, leverage falls; if a skilled human can quickly steer and validate AI into a high-value result, leverage rises. Because human attention is typically the scarce input, leverage is likely one of the strongest predictors of real-world AI ROI, and explains why training, domain expertise, workflow design, and evaluation infrastructure matter as much as model access.

### 4.8 Behavioral validation signals — the missing instrumentation layer

The framework's two softest variables are $q$ (validation confidence) and $d$ (deployment rate). In practice, they go unmeasured not because the concept is wrong but because the instrumentation has not been built. The reason $q$ and $d$ are *easy* to measure in software engineering is that code editors already capture an implicit behavioral signal: the user either accepts the suggestion, edits it, or reverts it. That accept–edit–revert trace is a verifiable reward that can be observed without asking the user anything.

Every knowledge-work domain has an equivalent trace. It is the delta between what the AI produced and what the human ultimately submitted, sent, published, or acted on. We call these **behavioral validation signals**: implicit, non-intrusive records of whether AI output was accepted, modified, or discarded at each stage of a workflow.

| Domain | AI output | Behavioral signal |
|---|---|---|
| Code | Suggested completion | Accept / edit / revert |
| Document drafting | Paragraph or section | Kept verbatim / edited / deleted |
| Research | Claim with citation | Survived final draft / removed |
| Email | Draft reply | Sent as-is / edited / discarded |
| Proposals / sales | Section of a bid | Included in submission / cut |
| Slides | Generated layout or copy | Kept / reformatted / replaced |
| Customer support | Suggested response | Sent / escalated / rewritten |
| Legal / compliance | Draft clause | Survived redline / struck |
| Tutoring | Explanation or worked example | Student accepted / requested re-explanation |

The pattern is consistent: wherever a human takes a final action downstream of an AI output, the gap between the AI's version and the human's final version encodes $q$ and $d$ directly and continuously — without surveys, rubrics, or explicit scoring.

**Formalizing the signal.** Let $r_t \in [0,1]$ be a scalar representation of the behavioral signal at step $t$ — for example, the fraction of AI-generated tokens retained in the final submission. Then an empirical estimate of $q$ can be constructed as:

$$\hat{q} = \mathbb{E}[r_t \mid \text{task type, user, context}]$$

and $d$ is simply the share of interactions where the output entered any downstream artifact at all ($r_t > 0$). Both can be estimated from logs without human annotation, exactly as Cursor estimates them from code editor telemetry.

**Why this matters beyond measurement.** A system that continuously captures behavioral validation signals can do more than measure cognitive efficiency after the fact — it can improve the underlying AI over time. The learning loop is: generate output → capture behavioral signal → update model toward outputs that survive human review. This is the mechanism behind Cursor's continual learning: online training steps taken on batches of accept/revert signals, measured in days not months. The same architecture applies to any domain with a behavioral trace.

This implies that the organizations best positioned to improve cognitive efficiency over time are not those with the most tokens or the largest models, but those that **instrument their workflows to capture behavioral validation signals and close the loop**. The instrumentation layer — not the model — is the durable competitive asset. A general model becomes a specialized, high-leverage model through accumulated behavioral signal, domain by domain, workflow by workflow.

## 5. Proposed Metrics

All metrics use the §4.1 notation and are measured **per task**, because AI performance is jagged (§3.1).

### 5.1 Task-Level Token ROI
$\text{ROI}_{\text{machine}} = \Delta N / (C_{tok}+C_{inf})$ and $\text{ROI}_{\text{total}} = \Delta N / C_{AI}$. Instrumentation per task: baseline and AI-assisted completion time; token consumption (by type); model/infra cost; human review time; rework time; output quality score; deployment flag; downstream result.

### 5.2 Cognitive Efficiency
$CE = \Delta V / M$, with $M$ from §4.2 (dollar numéraire by default; energy numéraire optional). A mature organization may report $CE$ in both numéraires for high-volume systems.

### 5.3 Human–AI Leverage Ratio
$\text{Leverage} = \Delta V / H$. Especially useful for enterprise adoption because human attention is the scarce resource: a tool that saves token cost but raises review burden may not improve productivity, while a tool that consumes more tokens but sharply cuts expert review time may be economically superior.

### 5.4 Nonuse Penalty
$\Delta N$ when positive, estimated by randomized trials, matched comparisons, or dated historical baselines (e.g., AI-assisted vs. traditional account research; AI-assisted vs. standard bug resolution; learning gains with vs. without AI tutoring).

### 5.5 Overuse Penalty
$C_{AI} - C_{AI}^{*}$, where $C_{AI}^{*}$ is found by benchmarking cheaper configurations against the same validated-outcome bar. Overuse is excess cost **without** comparable incremental value — not merely high token count.

### 5.6 Outcome-Adjusted AI Value
$$\text{OAV} = V_{AI} \cdot q \cdot d - C_{risk}$$
This discourages booking unused drafts, unverified analyses, or risky outputs as realized value, and allows probabilistic evaluation: high potential value at low validation confidence is not equal to verified, deployed value. $q$ and $d$ require scoring rubrics or domain-specific validation methods (a known soft spot — see `notes.md`).

## 6. Worked Numerical Example

**Task:** produce a 1,500-word research brief. **Evaluator:** firm net value. **Loaded wage:** \$75/hour. Two workflows are compared: a no-AI baseline and an AI-assisted workflow (AI drafting + AI critique + human citation verification). *All figures are illustrative, chosen to demonstrate the arithmetic and the interpretation.*

| Quantity | Baseline (no AI) | AI-assisted |
|---|---|---|
| Human time $H$ | 6.0 h | 2.5 h (0.5 framing + 1.0 review + 0.5 verification + 0.5 rework) |
| Human cost $C_{hr}+C_{rw}$ | \$450.00 | \$187.50 |
| Tokens (in / out) | — | 40,000 / 20,000 |
| Token + infra cost $C_{tok}+C_{inf}=M$ | \$0.00 | \$6.00 |
| Expected risk cost $C_{risk}$ | \$20.00 | \$50.00 |
| **Total cost** $C$ | **\$470.00** | **\$243.50** |
| Claims generated | 18 | 26 |
| Verified claims | 18 | 21 |
| Unsupported claims removed | 0 | 5 |
| Quality (2 reviewers, /10) | 7.0 | 8.0 |
| Validation confidence $q$ | 1.00 | 0.95 |
| Deployment rate $d$ | 1.00 | 1.00 |
| **Deliverable value** $V$ | **\$1,200.00** | **\$1,400.00** |
| Net value $V - C$ | \$730.00 | \$1,156.50 |

**Derived metrics (AI-assisted vs. baseline):**

- Validated incremental value: $\Delta V = 1{,}400 - 1{,}200 = \$200$.
- Net incremental value: $\Delta N = (1{,}400 - 243.50) - (1{,}200 - 470) = 1{,}156.50 - 730 = \$426.50$.
- Machine cognition: $M = \$6.00$.
- **Cognitive Efficiency:** $CE = \Delta V / M = 200 / 6 \approx \mathbf{33\times}$ (validated \$ per \$ of machine cognition).
- **Token ROI (machine):** $\Delta N / (C_{tok}+C_{inf}) = 426.50 / 6 \approx \mathbf{71\times}$.
- **Token ROI (total):** $\Delta N / C_{AI} = 426.50 / 243.50 \approx \mathbf{1.75\times}$.
- **Human–AI Leverage:** $\Delta V / H = 200 / 2.5 = \mathbf{\$80/h}$.
- **Nonuse Penalty:** $\Delta N = \mathbf{\$426.50}$ (cost of *not* using AI here).
- **Overuse Penalty:** suppose a cheaper config (smaller drafting model, $M=\$1.50$) reaches a statistically comparable brief (quality 7.8, value ≈ \$1,360) at the same verification bar. Then $C_{AI}^{*}\approx \$239$ and Overuse Penalty $\approx 243.50 - 239 = \mathbf{\$4.50}$ — small, but the diagnostic is the *gap*, not the level.
- **Outcome-Adjusted AI Value:** $\text{OAV} = 1{,}400 \times 0.95 \times 1.00 - 50 = \mathbf{\$1{,}280}$.

**Interpretation — the point of the example.** Token ROI (machine) looks enormous at ~71×, but that number is driven almost entirely by *human-time savings*, not token frugality; Token ROI (total) is a far more sober ~1.75×. Cognitive efficiency (~33×) confirms the tokens themselves were converted well. Yet the binding constraint is the 2.5 hours of human supervision: at \$80/h of leverage, the workflow's economics live or die on *review and verification capacity*, exactly as the thesis predicts. The five removed unsupported claims are where most of the risk — and most of the human cost — actually sits. A naïve dashboard reporting only tokens or only gross output would miss all of this.

## 7. Empirical Research Designs

### 7.1 Software engineering
Randomly assign developers to comparable tasks under escalating AI conditions: (1) no AI; (2) basic AI access; (3) AI with structured prompts; (4) AI with retrieval and test automation; (5) AI with model routing and a review checklist. Outcomes: completion time, code quality, test coverage, defect rate, review time, rework, token consumption, satisfaction. $CE$ = accepted pull requests (validated code quality) per unit of $M$. Hypothesis: AI raises speed but improves *net* value only when paired with validation infrastructure (tests, review, security checks).

### 7.2 Research writing
Evaluate AI-assisted drafting, literature synthesis, and citation verification: short research briefs produced under different AI conditions, scored for factual accuracy, citation validity, argument quality, originality, clarity, revision burden, and expert acceptance. $CE$ measured as *accepted claims per unit of $M$ after citation verification* — not words per token. (This design is operationalized as the pilot in `notes.md`.)

### 7.3 Business development and sales
Test AI-assisted account research, proposal drafting, and opportunity qualification against baseline workflows on comparable opportunities. Outcomes: research time, lead quality, proposal quality, win rate, response rate, cost per qualified opportunity. Because outcomes are noisy, include intermediate validated outcomes (better qualification, faster pursuit decisions, reduced wasted pursuit effort).

### 7.4 Education and tutoring
Evaluate AI tutoring across baseline ability levels under: no AI, unguided AI tutoring, structured AI tutoring, AI tutoring with teacher oversight. Outcomes: learning gains, time on task, confidence, error correction, teacher review burden, retention. $CE$ in education = learning gains per unit of AI *and* human support — distinguishing productivity (faster completion) from learning (mastery).

## 8. Hypotheses

- **H1.** Raw token consumption is weakly correlated with validated incremental value across heterogeneous tasks.
- **H2.** Token ROI varies more by task type, workflow design, and user expertise than by model access alone.
- **H3.** Human–AI leverage is higher for users with stronger task framing, domain knowledge, and evaluation ability.
- **H4.** Longer AI interactions improve outcomes for exploratory, ambiguous, or high-stakes tasks but reduce efficiency for routine, low-ambiguity tasks.
- **H5.** The nonuse penalty is highest where AI improves both speed and quality *and* outputs can be validated cheaply.
- **H6.** The overuse penalty is highest in workflows with weak task framing, low validation standards, excessive agentic loops, or unclear decision ownership.
- **H7.** Firm-level AI productivity gains depend more on workflow redesign and validation infrastructure than on aggregate token volume or seat adoption.
- **H8.** In high-leverage domains, AI creates value primarily by improving search, prioritization, and candidate generation, but net value depends on the capacity and quality of human or institutional validation.

## 9. Limitations

1. **Value is hard to measure.** Time saved is easier to quantify than decision quality, creativity, learning, or risk reduction; some benefits are intangible, delayed, or distributed.
2. **Baselines are unstable.** As workers learn and tools improve, the no-AI counterfactual drifts; $V_0, C_0$ must be dated and periodically re-measured.
3. **Token measures are model-dependent.** Pinning $M$ to a cost numéraire (§4.2) mitigates but does not eliminate cross-system incomparability.
4. **Validation is expensive.** More rigorous validation raises measurement cost — a real tradeoff between accounting precision and administrative burden.
5. **Metrics can be gamed.** Rewarding token frugality too narrowly suppresses valuable exploration; rewarding usage volume invites overuse. Metric design must avoid distorting behavior.
6. **Some benefits are welfare, not enterprise, gains.** If AI reduces stress or creates leisure without raising output, firm ROI misses it. The benefit is real; the evaluator's objective function must be explicit.

## 10. Ethical and Policy Considerations

Fine-grained AI-usage measurement can improve governance but can also become worker surveillance. Organizations should measure *workflows*, not punish individuals for token patterns out of context. There is a distributional concern: if AI raises the leverage of already-skilled workers more than others, gains concentrate; if it gives lower-skilled workers access to expert patterns, within-task inequality may fall. Which dominates depends on task structure, access, training, and incentives. Where data exist, environmental cost should enter via the energy/carbon numéraire (§4.2). Finally, validation standards must be domain-sensitive: the acceptable error rate for brainstorming slogans is not that of medical, legal, financial, or public-safety output. Cognitive efficiency must therefore be **risk-adjusted** (via $C_{risk}$ and $q$), not speed- and cost-only.

## 11. Conclusion

As machine cognition becomes metered, priced, routed, and optimized, tokens are the most visible unit of the transformation but not its underlying object. The deeper object is *metered machine cognition*: consumed AI capability applied to human goals. The central measurement problem is **conversion** — how effectively consumed machine intelligence becomes validated economic, creative, scientific, educational, or operational value. Raw usage cannot answer this; neither can seat licenses, prompt counts, or token volume.

This paper proposes cognitive efficiency as that accounting layer, distinguishing consumption from output, output from validated value, and validated value from net value after cost, risk, and supervision. Its sharpest, most defensible claim is narrow: **AI productivity requires outcome-adjusted accounting of metered cognition, and the binding constraint is human–AI leverage — expert attention and validation capacity — not token volume.** The winners in AI adoption will be those who route machine cognition to the right tasks, compress unnecessary context, expand it where it improves outcomes, supervise effectively, validate claims, reduce rework, avoid overuse, and recognize the opportunity cost of nonuse. The question is no longer "How much AI did we use?" but "How much validated value did we create per unit of machine cognition, human attention, cost, and risk?"

## Appendix A. The Paper as a Living Example (Self-Measuring Instrument)

This paper can be treated as a pilot instance of its own framework — a transparent record of how metered machine cognition contributed to a knowledge-work output, **not** as proof of the framework. The instrument below is the template; populate it for the actual production run before submission.

| Field | Symbol / unit | Value | Notes |
|---|---|---|---|
| Human concept-note time | h | _[fill]_ | Pre-draft framing |
| AI drafting tokens (in / out) | tokens | _[fill]_ | By model |
| Token + infra cost | $ ($M$) | _[fill]_ | Default numéraire |
| Human review time | h | _[fill]_ | Editing + structure |
| Citation verification time | h | _[fill]_ | Human-intensive bottleneck |
| Revision cycles | count | _[fill]_ | |
| Claims generated | count | _[fill]_ | |
| Claims retained after review | count | _[fill]_ | Verified |
| Claims removed as unsupported | count | _[fill]_ | |
| Final quality score | /10 | _[fill]_ | 2–3 reviewers |
| Validation confidence $q$ | $[0,1]$ | _[fill]_ | |
| Reuse value | $ | _[fill]_ | White paper / talk / proposal |
| **Token ROI (total)** | $\Delta N / C_{AI}$ | _[derive]_ | |
| **Cognitive Efficiency** | $\Delta V / M$ | _[derive]_ | |
| **Human–AI Leverage** | $\Delta V / H$ | _[derive]_ | |

Expected qualitative findings, to be confirmed: AI accelerates structure and drafting; citation verification remains a human-intensive bottleneck; AI generates useful candidate framings but unsupported claims must be removed. The value is not more words — it is a clearer, better-validated argument produced faster than the baseline.
