from __future__ import annotations

import argparse
from typing import Optional, Sequence


def main(argv: Optional[Sequence[str]] = None):
    parser = argparse.ArgumentParser(prog="{{ cookiecutter.project_name }}",
                                     description="{{ cookiecutter.project_short_description }}", )
    args = parser.parse_args(argv)


if __name__ == '__main__':
    raise SystemExit(main())
