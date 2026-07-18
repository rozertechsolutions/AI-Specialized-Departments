# Data and AI Safe Profile

Create this manually in Warp Settings > Agents > Profiles for Data and AI work.

## Profile

- Name: Data and AI Safe
- Purpose: evidence-based Data and AI design, review, and assurance with approval-controlled repository changes.
- Base model: use the human-selected default for the workspace.
- Planning model: use the human-selected default for the workspace.

## Permissions

- Apply code diffs: Always prompt for confirmation.
- Read files: Let the agent decide for repository-local non-sensitive files.
- Create plans: Let the agent decide.
- Execute commands: Always prompt for confirmation.
- Interact with running commands: Never unless explicitly authorized for the task.
- Ask clarifying questions: Allow.
- MCP servers: Disabled by default.

## Command Denylist

- Destructive filesystem commands such as recursive remove, permission changes, and owner changes.
- Git history mutation, pushing, merging, rebasing, force pushing, tagging, release, and publish commands.
- Deployment, production, signing, submission, account, credential, secret, private endpoint, and external transfer commands.
- Package installation, model download, cloud CLI, warehouse CLI, BI admin CLI, vector-store admin CLI, and scanner commands unless the human explicitly authorizes the exact command.
