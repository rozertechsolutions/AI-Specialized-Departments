# Native Source Verification

Official sources checked on 2026-07-16:

- Claude Projects: `https://support.claude.com/en/articles/9517075-what-are-projects`
- Claude custom connectors using remote MCP: `https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp`
- Claude documentation index: `https://docs.claude.com/llms.txt`

## Decisions

- Claude Project instructions and project knowledge are represented as copy-ready repository artifacts.
- Connectors and MCP are omitted because this static package must not connect or authenticate external tools.
- Claude Code repository files are omitted because this platform is Claude web/desktop Projects, not Claude Code.
