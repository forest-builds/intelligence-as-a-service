"""
Regression test: the evaluator must reproduce the paper's §6 worked example exactly.
If these assertions fail, the tool and the paper have diverged.

Run:
    python evaluator/test_evaluate.py
"""

import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from evaluate import WorkflowRun, evaluate  # noqa: E402

HERE = os.path.dirname(__file__)


def approx(a, b, tol=0.01):
    return abs(a - b) <= tol


def test_paper_section_6():
    with open(os.path.join(HERE, "examples", "paper-section-6.json")) as f:
        data = json.load(f)
    r = evaluate(WorkflowRun.from_json(data))

    # Values published in paper §6
    checks = {
        "delta_v_usd": 200.0,
        "delta_n_usd": 426.5,
        "m_usd": 6.0,
        "cognitive_efficiency": 33.33,
        "token_roi_machine": 71.08,
        "token_roi_total": 1.7515,
        "human_ai_leverage_usd_per_hour": 80.0,
        "nonuse_penalty_usd": 426.5,
        "overuse_penalty_usd": 4.5,
        "outcome_adjusted_value_usd": 1280.0,
        "q": 0.95,
        "d": 1.0,
    }
    failures = []
    for key, expected in checks.items():
        actual = r[key]
        if not approx(actual, expected):
            failures.append(f"  {key}: expected {expected}, got {actual}")
    if failures:
        print("FAIL — evaluator diverged from paper §6:")
        print("\n".join(failures))
        return False
    print("PASS — evaluator reproduces paper §6 exactly:")
    for key in checks:
        print(f"  {key} = {r[key]}")
    return True


def test_behavioral_log_estimation():
    """q and d should be estimable from a behavioral log when explicit scores are absent."""
    data = {
        "value": {"baseline_value_usd": 100, "ai_value_usd": 200},
        "cost_baseline": {"human_hours": 1.0, "loaded_wage_usd_per_hour": 50},
        "cost_ai": {"token_cost_usd": 1.0, "human_hours": 0.5, "loaded_wage_usd_per_hour": 50},
        "validation": {"validation_confidence": None, "deployment_rate": None},
        "behavioral_log": {
            "observations": [
                {"ai_tokens": 100, "retained_tokens": 90, "submitted": True},
                {"ai_tokens": 100, "retained_tokens": 50, "submitted": True},
                {"ai_tokens": 100, "retained_tokens": 0, "submitted": False},
            ]
        },
    }
    r = evaluate(WorkflowRun.from_json(data))
    # q = mean(0.9, 0.5, 0.0) = 0.4667 ; d = 2/3 = 0.667
    ok = approx(r["q"], 0.467, 0.01) and approx(r["d"], 0.667, 0.01)
    print(f"{'PASS' if ok else 'FAIL'} — behavioral log estimation: q={r['q']}, d={r['d']}")
    return ok


if __name__ == "__main__":
    results = [test_paper_section_6(), test_behavioral_log_estimation()]
    print()
    if all(results):
        print(f"All {len(results)} tests passed.")
        sys.exit(0)
    else:
        print(f"{results.count(False)} of {len(results)} tests FAILED.")
        sys.exit(1)
