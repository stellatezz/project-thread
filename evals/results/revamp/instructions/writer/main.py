"""Create one plain text document at the requested path."""

import argparse
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("content")
    args = parser.parse_args()
    with args.output.open("x", encoding="utf-8") as handle:
        handle.write(args.content)


if __name__ == "__main__":
    main()
