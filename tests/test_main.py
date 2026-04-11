import pytest
from typer.testing import CliRunner

from scrim_wheel.main import app

runner = CliRunner()


def test_roll_default_count():
    result = runner.invoke(app, ["apple", "banana", "cherry"])
    assert result.exit_code == 0
    output_lines = result.output.strip().splitlines()
    assert len(output_lines) == 1
    assert output_lines[0] in ["apple", "banana", "cherry"]


def test_roll_with_count():
    result = runner.invoke(app, ["--count", "2", "alpha", "beta", "gamma", "delta"])
    assert result.exit_code == 0
    output_lines = result.output.strip().splitlines()
    assert len(output_lines) == 2
    for item in output_lines:
        assert item in ["alpha", "beta", "gamma", "delta"]


def test_roll_no_duplicates():
    items = ["a", "b", "c", "d", "e"]
    result = runner.invoke(app, ["--count", "5"] + items)
    assert result.exit_code == 0
    output_lines = result.output.strip().splitlines()
    assert sorted(output_lines) == sorted(items)


def test_roll_count_equals_items():
    items = ["x", "y", "z"]
    result = runner.invoke(app, ["--count", "3"] + items)
    assert result.exit_code == 0
    output_lines = result.output.strip().splitlines()
    assert len(output_lines) == 3
    assert sorted(output_lines) == sorted(items)


def test_roll_count_exceeds_items():
    result = runner.invoke(app, ["--count", "5", "one", "two"])
    assert result.exit_code == 1
    assert "Error" in result.output or "Error" in (result.stderr or "")


def test_roll_single_item():
    result = runner.invoke(app, ["only"])
    assert result.exit_code == 0
    assert result.output.strip() == "only"
