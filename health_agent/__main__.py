import sys

from .agent import run


def main() -> None:
    if len(sys.argv) < 2:
        print('usage: python -m health_agent "вопрос"', file=sys.stderr)
        raise SystemExit(1)
    print(run(sys.argv[1]))


if __name__ == "__main__":
    main()
