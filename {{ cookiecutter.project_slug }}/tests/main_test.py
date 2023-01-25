from {{ cookiecutter.project.slug }} import _main

def test_main_basic(capsys):
    _main.main(())
    out, err = capsys.readouterr()

    assert {{ cookiecutter.project_slug }} in out
    assert {{ cookiecutter.project_short_description }} in out
