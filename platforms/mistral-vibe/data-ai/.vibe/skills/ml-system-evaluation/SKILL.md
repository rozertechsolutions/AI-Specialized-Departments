---
name: ml-system-evaluation
description: Review ML features, training, validation, comparison, documentation, leakage controls, release-candidate identity, and model acceptance evidence.
user-invocable: true
allowed-tools:
  - grep
  - read_file
  - task
---

# ML System Evaluation

## Use When
A machine-learning model, feature pipeline, training process, comparison, validation plan, model card, or release candidate needs independent review.

## Procedure
1. Confirm model purpose, inputs, outputs, users, baseline, feature sources, data splits, evaluation data, thresholds, lifecycle owner, and risk owner.
2. Review leakage, contamination, representative slices, fairness-relevant slices, uncertainty/calibration, robustness, failure modes, and fallback behavior.
3. Verify model documentation, reproducibility, packaging/interface contract, configuration/version control, monitoring needs, and rollback criteria.
4. Distinguish builder tests from independent acceptance; block fabricated or missing metrics.
5. Return status as exactly `PASS`, `FAIL`, or `BLOCKED`.

## Output
Evaluation findings, release blockers, model-documentation gaps, monitoring requirements, human approvals, blockers, and status.
