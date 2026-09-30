import pytest

from project import main


def test_main_runs(capsys: pytest.CaptureFixture[str]) -> None:
    main()
    assert capsys.readouterr().out
