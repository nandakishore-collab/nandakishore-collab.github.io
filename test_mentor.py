"""Unit tests for prompt construction; these tests do not call the API."""

import pytest

from src.codementor.mentor import MentorConfigurationError, build_user_prompt


def test_build_user_prompt_includes_request_context():
    prompt = build_user_prompt(
        language="Python",
        help_mode="Explain an error",
        code="print(unknown_name)",
        question="Why does this raise a NameError?",
    )

    assert "Programming language: Python" in prompt
    assert "Help requested: Explain an error" in prompt
    assert "Why does this raise a NameError?" in prompt
    assert "print(unknown_name)" in prompt
    assert "```python" in prompt


@pytest.mark.parametrize(
    "field_overrides",
    [
        {"language": ""},
        {"help_mode": ""},
        {"code": "   "},
        {"question": ""},
    ],
)
def test_build_user_prompt_rejects_missing_inputs(field_overrides):
    values = {
        "language": "Python",
        "help_mode": "Explain an error",
        "code": "print('hello')",
        "question": "Explain this code.",
    }
    values.update(field_overrides)

    with pytest.raises(MentorConfigurationError):
        build_user_prompt(**values)
