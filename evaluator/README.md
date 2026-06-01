# Cognitive Efficiency Evaluator

Takes a logged AI-assisted workflow run and returns a full cognitive efficiency breakdown: CE, Token ROI (machine and total), Human–AI Leverage, Nonuse Penalty, Overuse Penalty, and Outcome-Adjusted AI Value.

## Quick start

```bash
pip install -r requirements.txt
python evaluate.py --input my-workflow.json
```

Or fill out the template and run interactively:

```bash
cp input-template.json my-workflow.json
# edit my-workflow.json with your workflow data
python evaluate.py --input my-workflow.json
```

## Input schema

See [input-template.json](input-template.json) for the full template. Key fields:

| Field | Type | Description |
|---|---|---|
| `task_description` | string | What the AI-assisted task was |
| `baseline_value_usd` | float | Estimated value of task completed without AI |
| `ai_value_usd` | float | Estimated value of task completed with AI |
| `baseline_cost_usd` | float | Full cost of no-AI process (human time × wage) |
| `tokens_input` | int | Input tokens consumed |
| `tokens_output` | int | Output tokens consumed |
| `token_cost_usd` | float | Total inference cost |
| `infra_cost_usd` | float | Additional compute/infra cost beyond tokens |
| `human_hours` | float | Framing + review + verification + rework time |
| `loaded_wage_usd` | float | Fully loaded hourly wage for human time |
| `rework_hours` | float | Hours spent correcting/cleaning AI output |
| `risk_cost_usd` | float | Expected cost of errors (P(error) × cost of error) |
| `coord_cost_usd` | float | Coordination/handoff overhead |
| `validation_confidence` | float | q: probability output is correct/acceptable [0–1] |
| `deployment_rate` | float | d: share of output actually used [0–1] |
| `domain` | string | Task domain (code, writing, research, email, …) |
| `model` | string | Model identifier used |

## Output

```json
{
  "cognitive_efficiency": 33.4,
  "token_roi_machine": 71.1,
  "token_roi_total": 1.75,
  "human_ai_leverage_usd_per_hour": 80.0,
  "nonuse_penalty_usd": 426.5,
  "outcome_adjusted_value_usd": 1280.0,
  "summary": "Tokens converted efficiently (CE 33×). Binding constraint is human supervision (2.5h). Consider reducing review burden before optimizing model cost."
}
```

## Behavioral validation signals

If you don't have explicit $q$ and $d$ values, the evaluator can estimate them from behavioral traces. Pass a `behavioral_log` array instead:

```json
"behavioral_log": [
  { "ai_tokens": 340, "retained_tokens": 310, "submitted": true },
  { "ai_tokens": 120, "retained_tokens": 0,   "submitted": false }
]
```

The evaluator computes $\hat{q} = \mathbb{E}[\text{retained} / \text{ai\_tokens}]$ and $\hat{d} = P(\text{submitted} = \text{true})$ from the log.

## Status

- [x] Input schema defined
- [x] Input template
- [ ] Core metric calculations (`evaluate.py`)
- [ ] CLI interface
- [ ] Behavioral log → q/d estimator
- [ ] Domain-specific calibration
- [ ] Streamlit UI
