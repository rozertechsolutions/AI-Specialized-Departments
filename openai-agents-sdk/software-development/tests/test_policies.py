from software_development_department.policies import requires_human_approval, validate_scope


def test_sensitive_actions_require_approval() -> None:
    assert requires_human_approval("publish the package")
    assert not requires_human_approval("review the code without changes")


def test_scope_validation() -> None:
    assert validate_scope(("src/a.py",), ("src",))
    assert not validate_scope(("../outside",), ("src",))
