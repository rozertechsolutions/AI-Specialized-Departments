# Usage

Install dependencies in your own isolated environment, set `OPENAI_API_KEY` outside the repository, and run the package only after reviewing its guardrails.

```python
import asyncio

from marketing_engineering_agents import MarketingContext, run_marketing_request

context = MarketingContext(
    request_id="local-request-id",
    accountable_owner="named owner",
    approval_authority="named approver",
)

result = asyncio.run(
    run_marketing_request(
        "Prepare a bounded plan using only approved, non-sensitive inputs.",
        context=context,
    )
)
print(result.model_dump_json(indent=2))
```

No model, MCP server, connector, production tool, or external action is configured by default.
