from src.agent.sandbox.base import CommandResult
from src.agent.sandbox.feedback import build_feedback, classify_failure


def test_classify_module_not_found_error():
    failure_type = classify_failure(
        "pytest",
        "",
        "ModuleNotFoundError: No module named 'requests'",
    )

    assert failure_type == "ModuleNotFoundError"


def test_build_feedback_contains_retry_guidance():
    feedback = build_feedback(
        stage="pytest",
        error="Generated test failed in sandbox.",
        retry_count=0,
        max_retries=3,
        command_result=CommandResult(
            exit_code=1,
            stdout="",
            stderr="ModuleNotFoundError: No module named 'requests'",
        ),
    )

    assert "ModuleNotFoundError" in feedback
    assert "第 1 次重试" in feedback
    assert "完整新计划" in feedback