# MVP v1 — Calculator With Teeth

This is the first user-facing version of Cognitive Efficiency Lab: a simple browser calculator that helps a person or small team answer:

> Is my AI usage actually worth it?

The point is not precise accounting. The point is a useful, honest projection from natural inputs: what tools you pay for, how often you use them, how much time they save, how much review they create, and whether the output actually gets used.

## Use It

Open [calculator.html](calculator.html) in a browser. No install, no server, no account.

The calculator asks for optional fields across five areas:

- Profile: personal, founder, team, or company lens
- Subscriptions: monthly spend on ChatGPT, Claude, Cursor, API usage, or other tools
- Usage: task type, tasks per week, manual baseline time, AI-assisted time, review/rework time
- Value proxy: hourly salary, loaded wage, company revenue, or conservative value per accepted task
- Validation: accepted output rate, quality lift, risk/rework burden

It returns:

- monthly AI cost
- monthly time saved
- human review burden
- net value estimate
- cognitive efficiency
- total ROI
- worth-it verdict
- next action recommendation

## Why This Shape

Existing infra tools answer what happened at the API and trace level. This MVP asks about the workflow outcome.

The calculator should feel usable even when the user only knows rough answers. Every field has a default, and the value estimate can come from either personal salary, company wage, revenue proxy, or a direct per-task value.

## V1 Scope

This version is intentionally standalone. It does not import logs, store data, or require model-provider integration.

The next useful step is to connect the calculator output to `evaluator/evaluate.py` JSON so a projected workflow and a measured workflow can use the same metric spine.

