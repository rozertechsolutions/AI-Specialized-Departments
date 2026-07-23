from __future__ import annotations

from mobile_development_agents.policies.security import contains_secret, validate_relative_project_path


def validate_user_input(text: str) -> tuple[str, ...]:
    issues: list[str] = []
    if contains_secret(text):
        issues.append("Input appears to contain a secret.")
    if "publish" in text.lower() or "submit to app store" in text.lower():
        issues.append("Publishing or store submission is prohibited.")
    return tuple(issues)


def validate_requested_path(path: str) -> tuple[str, ...]:
    return tuple(finding.message for finding in validate_relative_project_path(path) if finding.blocked)


def build_sdk_input_guardrail() -> object:
    try:
        from agents import GuardrailFunctionOutput, input_guardrail
    except ImportError as exc:
        raise RuntimeError("Install openai-agents to build SDK input guardrails.") from exc

    @input_guardrail(run_in_parallel=False)
    async def block_unsafe_mobile_request(ctx: object, agent: object, input: object) -> object:
        issues = validate_user_input(str(input))
        context = getattr(ctx, "context", None)
        request = getattr(context, "request", None)
        if request is not None:
            issues = (*issues, *validate_requested_path(str(request.project_context.project_root)))
        return GuardrailFunctionOutput(
            output_info={"issues": issues},
            tripwire_triggered=bool(issues),
        )

    return block_unsafe_mobile_request
