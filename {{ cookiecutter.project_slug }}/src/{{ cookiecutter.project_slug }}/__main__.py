from __future__ import annotations

import argparse
from typing import Optional, Sequence


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(prog="{{ cookiecutter.project_name }}",
                                     description="{{ cookiecutter.project_short_description }}", )
    args = parser.parse_args(argv)

    print(args)

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
