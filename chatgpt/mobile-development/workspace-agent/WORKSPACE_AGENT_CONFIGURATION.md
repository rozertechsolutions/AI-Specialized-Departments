# Workspace Agent Configuration

Use only in an eligible ChatGPT Business or Enterprise workspace where Workspace Agents are enabled by an admin.

## Agent Name

Mobile Development Specialist

## Tagline

Mobile architecture, implementation planning, reviews, and release readiness for Android, iOS, KMP, Flutter, and React Native.

## Description

An internal mobile development assistant that applies strict role ownership, platform boundaries, validation evidence, security gates, and human review for mobile application work.

## Instructions

Paste the full contents of `workspace-agent/AGENT_INSTRUCTIONS.md`.

## Files

Attach the files in `workspace-agent/FILES_MANIFEST.md`.

## Skills

If workspace Skills are available and approved, attach or install only the reviewed workflow Skill packages from `skills/`. Package each Skill as one top-level directory containing its `SKILL.md`; do not attach the entire repository.

## Tools And Apps

Default tools:

- Memory: off unless the workspace owner requires it for this agent and confirms retention behavior.
- Web search: off by default; enable only for current official documentation lookup.
- Image generation: off.
- Apps/connectors: none.
- Custom MCP: none.
- Slack channel: none.
- API trigger: none.
- Schedule: none.

## Access

Default ChatGPT channel access: private to the owner.

Do not publish to the organization directory, configure Slack, create a schedule, add an API trigger, connect apps, configure custom MCP, or publish the agent without explicit human approval.
