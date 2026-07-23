# GPT Builder Configuration

Use this source in the ChatGPT web GPT builder. Keep visibility private unless a human owner explicitly approves sharing.

## Name

Mobile Development Specialist

## Description

Advises, plans, reviews, and analyzes Android, iOS, Kotlin Multiplatform, Flutter, and React Native work with strict platform boundaries, validation evidence, and human-controlled security gates.

## Instructions

Paste the full contents of `custom-gpt/GPT_INSTRUCTIONS.md`.

## Conversation Starters

Paste the starters from `custom-gpt/CONVERSATION_STARTERS.md`.

## Knowledge

Upload:

- `knowledge/MOBILE_DEVELOPMENT_SCOPE.md`
- `knowledge/RESPONSIBILITY_MODEL.md`
- `knowledge/QUALITY_AND_COMPLETION_STANDARDS.md`
- `knowledge/SECURITY_AND_HUMAN_REVIEW.md`

Use knowledge for reference only. Keep rules and behavior in Instructions.

Do not upload `skills/` folders as GPT knowledge. Skills are a separate native surface for eligible accounts and must be installed through the Skills interface.

## Recommended Model

Do not hardcode a model. Leave the recommended model unset unless the GPT builder requires one or the account owner selects an available current ChatGPT model.

## Capabilities

Default:

- Web search: off unless the user asks for current official documentation or current platform facts.
- Canvas: optional.
- Code Interpreter and Data Analysis: off unless the user explicitly needs local file analysis or calculations inside ChatGPT and confirms no sensitive data is included.
- Image generation: off.
- Apps: off.
- Actions: none.

A GPT can use either apps or actions, not both. This configuration uses neither.

## Sharing

Default visibility: private.

Do not publish to the GPT Store, share externally, enable apps, configure actions, or connect external services without explicit human approval.
