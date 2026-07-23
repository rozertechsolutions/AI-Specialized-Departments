---
name: workflow-implement-web-change
description: "Guide scoped web implementation work with evidence, reviews, and safety gates."
user-invocable: true
allowed-tools:
  - read
  - read_file
  - grep
  - write_file
  - edit
  - search_replace
  - ask_user_question
---

# Implement Web Change

Use this slash-command Skill to guide scoped web implementation after approval boundaries are clear. Preserve native conventions, make only requested repository changes, record evidence, and stop before deployment, publication, Git mutation, or external side effects.

## Expected input
Requested behavior, acceptance criteria, affected files or surfaces, prohibited changes, selected Vibe agent, and verification expectations.

## Expected output
Changed files, behavior, direct verification evidence, unresolved risks, required reviews, and NOT EXECUTED checks.

## Gates
1. Verify inputs, scope, stack, and applicable risks.
2. Produce or inspect only the approved artifacts.
3. Request independent review for security-sensitive or release-sensitive work.
4. Record evidence for every completion claim.
5. Stop with BLOCKED if a required decision or approval is missing.

## Safety
Do not execute commands, install dependencies, mutate Git, deploy, publish, authenticate, expose secrets, or perform destructive actions automatically.
