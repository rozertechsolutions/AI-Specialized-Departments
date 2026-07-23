from __future__ import annotations

from mobile_development_agents.policies.security import contains_secret, redact_secrets


def validate_agent_output(text: str) -> tuple[str, ...]:
    issues: list[str] = []
    if contains_secret(text):
        issues.append("Output appears to contain a secret.")
    if "successfully published" in text.lower() or "uploaded to app store" in text.lower():
        issues.append("Output claims a prohibited release action.")
    return tuple(issues)


def safe_output(text: str) -> str:
    return redact_secrets(text)


def build_sdk_output_guardrail() -> object:
    try:
        from agents import GuardrailFunctionOutput, output_guardrail
    except ImportError as exc:
        raise RuntimeError("Install openai-agents to build SDK output guardrails.") from exc

    @output_guardrail
    async def block_unsafe_mobile_output(ctx: object, agent: object, output: object) -> object:
        text = safe_output(str(output))
        issues = validate_agent_output(text)
        return GuardrailFunctionOutput(
            output_info={"issues": issues},
            tripwire_triggered=bool(issues),
        )

    return block_unsafe_mobile_output
