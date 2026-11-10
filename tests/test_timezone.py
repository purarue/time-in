"""Regression tests for invalid timezone handling."""

from click.testing import CliRunner

from time_in.__main__ import main


def test_invalid_timezone_clean_error() -> None:
    # used to raise a raw ValueError with a traceback
    result = CliRunner().invoke(main, ["tz", "Nope/NotReal"])
    assert result.exit_code == 2
    assert "failed to parse timezone" in result.output
    assert "Traceback" not in result.output


def test_valid_timezone_still_works() -> None:
    result = CliRunner().invoke(main, ["tz", "US/Eastern"])
    assert result.exit_code == 0
