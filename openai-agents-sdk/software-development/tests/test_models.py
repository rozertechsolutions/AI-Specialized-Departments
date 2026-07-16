from software_development_department.models import DepartmentTask, RiskLevel


def test_task_is_immutable_and_explicit() -> None:
    task = DepartmentTask("Add capability", ("src",), ("criterion",), risk_level=RiskLevel.MEDIUM)
    assert task.authorized_scope == ("src",)
