---
description: Data and AI intake, feasibility, value, alternatives-to-AI, impact, and risk triage workflow
agent: data-ai-orchestrator
subtask: false
---

# Data and AI Intake Triage

Run the `use-case-risk-triage` Skill, identify required specialist reviews, and return `PASS`, `FAIL`, or `BLOCKED`.

## Gates
1. Confirm business outcome, users, lifecycle owner, value hypothesis, alternatives to AI, success metrics, and stop conditions.
2. Classify data sensitivity, decision impact, privacy, allowed use, third-party exposure, production impact, and human-review gates.
3. Identify evidence, owners, validation needs, monitoring, rollback or retirement expectations, and independent assurance path.
4. Stop with `BLOCKED` if required authority, evidence, or risk acceptance is missing.

## Safety
Do not access sensitive datasets, run shell commands, call web services, configure MCP, deploy, publish, spend, sign, submit, or mutate production.
