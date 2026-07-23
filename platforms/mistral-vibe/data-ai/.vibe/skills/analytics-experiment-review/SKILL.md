---
name: analytics-experiment-review
description: Review statistical analysis, causal inference, decision intelligence, experiment design, interpretation, and reproducible evidence.
user-invocable: true
allowed-tools:
  - grep
  - read_file
  - task
---

# Analytics Experiment Review

## Use When
An analysis, causal claim, segmentation, statistical study, controlled experiment, decision model, or experiment result needs independent review.

## Procedure
1. Confirm question, decision use, target population, data source, assumptions, exclusion criteria, metric definitions, and success thresholds.
2. Review design, assignment, sample size, power, confounders, interference, bias, uncertainty, calibration, sensitivity, and guardrails.
3. Verify reproducible queries or notebooks are traceable without exposing sensitive data.
4. State interpretation limits and block unsupported causal, significance, or business-impact claims.
5. Return status as exactly `PASS`, `FAIL`, or `BLOCKED`.

## Output
Validity findings, uncertainty, interpretation limits, decision risks, required evidence, blockers, and status.
