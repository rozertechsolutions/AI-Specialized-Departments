from __future__ import annotations

from .models import ReviewOutput


def serialize_review_output(output: ReviewOutput) -> str:
    return output.model_dump_json()


def deserialize_review_output(payload: str) -> ReviewOutput:
    return ReviewOutput.model_validate_json(payload)
