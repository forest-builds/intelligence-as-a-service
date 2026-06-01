"""
Cognitive Efficiency Evaluator
Computes CE, Token ROI, Human-AI Leverage, Nonuse/Overuse Penalties, and OAV
from a logged AI-assisted workflow run.

Usage:
    python evaluate.py --input my-workflow.json
    python evaluate.py --input my-workflow.json --output results.json
"""

import argparse
import json
import sys
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class WorkflowRun:
    # Value
    baseline_value_usd: float
    ai_value_usd: float

    # Baseline cost
    baseline_human_hours: float
    baseline_loaded_wage: float
    baseline_other_cost_usd: float = 0.0
    baseline_risk_cost_usd: float = 0.0

    # AI cost components
    token_cost_usd: float = 0.0
    infra_cost_usd: float = 0.0
    ai_human_hours: float = 0.0
    ai_loaded_wage: float = 75.0
    rework_hours: float = 0.0
    risk_cost_usd: float = 0.0
    coord_cost_usd: float = 0.0

    # Validation
    validation_confidence: Optional[float] = None   # q
    deployment_rate: Optional[float] = None          # d

    # Behavioral log for estimating q and d
    behavioral_log: list = field(default_factory=list)

    # Overuse benchmark
    min_sufficient_ai_cost_usd: Optional[float] = None

    @classmethod
    def from_json(cls, data: dict) -> "WorkflowRun":
        v = data.get("value", {})
        cb = data.get("cost_baseline", {})
        ca = data.get("cost_ai", {})
        val = data.get("validation", {})
        bl = data.get("behavioral_log", {})
        ob = data.get("overuse_benchmark", {})
        wage = ca.get("loaded_wage_usd_per_hour", 75.0)
        return cls(
            baseline_value_usd=v.get("baseline_value_usd", 0.0),
            ai_value_usd=v.get("ai_value_usd", 0.0),
            baseline_human_hours=cb.get("human_hours", 0.0),
            baseline_loaded_wage=cb.get("loaded_wage_usd_per_hour", 75.0),
            baseline_other_cost_usd=cb.get("other_cost_usd", 0.0),
            baseline_risk_cost_usd=cb.get("risk_cost_usd", 0.0),
            token_cost_usd=ca.get("token_cost_usd", 0.0),
            infra_cost_usd=ca.get("infra_cost_usd", 0.0),
            ai_human_hours=ca.get("human_hours", 0.0),
            ai_loaded_wage=wage,
            rework_hours=ca.get("rework_hours", 0.0),
            risk_cost_usd=ca.get("risk_cost_usd", 0.0),
            coord_cost_usd=ca.get("coord_cost_usd", 0.0),
            validation_confidence=val.get("validation_confidence"),
            deployment_rate=val.get("deployment_rate"),
            behavioral_log=bl.get("observations", []),
            min_sufficient_ai_cost_usd=ob.get("min_sufficient_ai_cost_usd"),
        )


def estimate_qd_from_log(log: list) -> tuple[float, float]:
    """Estimate q and d from behavioral trace observations."""
    if not log:
        return 1.0, 1.0
    retention_rates = []
    deployed = []
    for obs in log:
        ai_tok = obs.get("ai_tokens", 0)
        ret_tok = obs.get("retained_tokens", 0)
        submitted = obs.get("submitted", True)
        if ai_tok > 0:
            retention_rates.append(ret_tok / ai_tok)
        deployed.append(1 if submitted else 0)
    q_hat = sum(retention_rates) / len(retention_rates) if retention_rates else 1.0
    d_hat = sum(deployed) / len(deployed) if deployed else 1.0
    return q_hat, d_hat


def evaluate(run: WorkflowRun) -> dict:
    # Resolve q and d
    if run.validation_confidence is not None:
        q = run.validation_confidence
    elif run.behavioral_log:
        q, _ = estimate_qd_from_log(run.behavioral_log)
    else:
        q = 1.0

    if run.deployment_rate is not None:
        d = run.deployment_rate
    elif run.behavioral_log:
        _, d = estimate_qd_from_log(run.behavioral_log)
    else:
        d = 1.0

    # Cost components
    baseline_human_cost = run.baseline_human_hours * run.baseline_loaded_wage
    baseline_cost = (baseline_human_cost + run.baseline_other_cost_usd
                     + run.baseline_risk_cost_usd)

    ai_human_cost = (run.ai_human_hours + run.rework_hours) * run.ai_loaded_wage
    m = run.token_cost_usd + run.infra_cost_usd           # metered machine cognition
    c_ai = m + ai_human_cost + run.risk_cost_usd + run.coord_cost_usd

    # Core quantities
    delta_v = run.ai_value_usd - run.baseline_value_usd   # validated incremental value
    delta_n = (run.ai_value_usd - c_ai) - (run.baseline_value_usd - baseline_cost)  # net incremental value

    # Metrics
    ce = delta_v / m if m > 0 else None
    roi_machine = delta_n / m if m > 0 else None
    roi_total = delta_n / c_ai if c_ai > 0 else None
    total_human_hours = run.ai_human_hours + run.rework_hours
    leverage = delta_v / total_human_hours if total_human_hours > 0 else None
    nonuse_penalty = delta_n if delta_n > 0 else 0.0
    overuse_penalty = (c_ai - run.min_sufficient_ai_cost_usd
                       if run.min_sufficient_ai_cost_usd is not None else None)
    oav = run.ai_value_usd * q * d - run.risk_cost_usd

    # Narrative summary
    lines = []
    if ce is not None:
        lines.append(f"Cognitive efficiency {ce:.1f}× (${delta_v:.0f} validated value per ${m:.2f} of machine cognition).")
    if leverage is not None:
        lines.append(f"Human–AI leverage ${leverage:.0f}/h.")
    if roi_total is not None:
        if roi_machine is not None and roi_machine > 10 * roi_total:
            lines.append(
                f"Token ROI (machine) {roi_machine:.1f}× vs. total {roi_total:.2f}× — "
                "gap driven by human supervision cost, which is the binding constraint."
            )
        else:
            lines.append(f"Token ROI (total) {roi_total:.2f}×.")
    if overuse_penalty is not None and overuse_penalty > 0:
        lines.append(f"Overuse penalty ${overuse_penalty:.2f} — cheaper config reaches comparable outcome.")
    if q < 0.9:
        lines.append(f"Validation confidence low ({q:.0%}) — significant output was modified or rejected.")

    return {
        "delta_v_usd": round(delta_v, 2),
        "delta_n_usd": round(delta_n, 2),
        "m_usd": round(m, 4),
        "c_ai_usd": round(c_ai, 2),
        "q": round(q, 3),
        "d": round(d, 3),
        "cognitive_efficiency": round(ce, 2) if ce is not None else None,
        "token_roi_machine": round(roi_machine, 2) if roi_machine is not None else None,
        "token_roi_total": round(roi_total, 4) if roi_total is not None else None,
        "human_ai_leverage_usd_per_hour": round(leverage, 2) if leverage is not None else None,
        "nonuse_penalty_usd": round(nonuse_penalty, 2),
        "overuse_penalty_usd": round(overuse_penalty, 2) if overuse_penalty is not None else None,
        "outcome_adjusted_value_usd": round(oav, 2),
        "summary": " ".join(lines),
    }


def main():
    parser = argparse.ArgumentParser(description="Cognitive Efficiency Evaluator")
    parser.add_argument("--input", required=True, help="Path to workflow JSON file")
    parser.add_argument("--output", help="Path to write results JSON (default: stdout)")
    args = parser.parse_args()

    with open(args.input) as f:
        data = json.load(f)

    run = WorkflowRun.from_json(data)
    results = evaluate(run)

    output = json.dumps(results, indent=2)
    if args.output:
        with open(args.output, "w") as f:
            f.write(output)
        print(f"Results written to {args.output}")
    else:
        print(output)


if __name__ == "__main__":
    main()
