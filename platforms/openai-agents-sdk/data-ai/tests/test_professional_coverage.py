from data_ai_agents_sdk.agents import ROLE_INSTRUCTIONS


def test_professional_responsibilities_are_covered():
    text = "\n".join(ROLE_INSTRUCTIONS.values())

    for term in (
        "strategy",
        "portfolio",
        "orchestration",
        "solution",
        "governance",
        "privacy",
        "metadata",
        "semantic",
        "contracts",
        "dataset",
        "platform",
        "quality",
        "lineage",
        "observability",
        "BI",
        "causal",
        "experiments",
        "ML",
        "GenAI",
        "RAG",
        "inference",
        "MLOps",
        "LLMOps",
        "evaluation",
        "red-team",
        "responsible AI",
        "human oversight",
        "assurance",
    ):
        assert term in text


def test_safety_and_separation_rules_are_covered():
    text = "\n".join(ROLE_INSTRUCTIONS.values())

    for term in (
        "Do not implement specialist work",
        "Do not override specialists",
        "approve your own",
        "Do not call models",
        "Do not deploy",
        "final independent assurance",
        "missing provenance",
        "fabricated metrics",
    ):
        assert term in text
