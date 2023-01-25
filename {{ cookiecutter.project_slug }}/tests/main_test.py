import pytest

from {{ cookiecutter.project_slug }}.__main__ import main


def test_main_no_arguments_returns_zero():
    assert main(()) == 0


def test_main_basic(capsys):
    with pytest.raises(SystemExit):
        main(("--help",))

    out, err = capsys.readouterr()

    assert err == ""
    assert "{{ cookiecutter.project_short_description }}" in out
