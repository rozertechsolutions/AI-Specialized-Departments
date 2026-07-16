from __future__ import annotations

SENSITIVE_ACTION_TERMS = frozenset({
    "delete", "destroy", "reset --hard", "force push", "publish", "deploy",
    "release", "sign", "notarize", "submit", "credential", "private key",
    "install dependency", "change permission", "external write"
})


def requires_human_approval(text: str) -> bool:
    normalized = text.casefold()
    return any(term in normalized for term in SENSITIVE_ACTION_TERMS)


def validate_scope(requested_paths: tuple[str, ...], authorized_paths: tuple[str, ...]) -> bool:
    return all(any(path == root or path.startswith(root.rstrip("/") + "/") for root in authorized_paths) for path in requested_paths)


def can_claim_observed(observed: bool, source: str | None) -> bool:
    return observed and bool(source and source.strip())
