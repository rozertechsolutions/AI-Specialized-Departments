from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class MarketingContext:
    request_id: str
    accountable_owner: str
    approval_authority: str
    allowed_data_categories: frozenset[str] = field(default_factory=frozenset)
    authorized_external_actions: frozenset[str] = field(default_factory=frozenset)
