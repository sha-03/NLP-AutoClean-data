"""Command-line entry point for cleaning a CSV text column."""

import argparse
from pathlib import Path

from src.cleaner import clean_csv
from src.validator import validate_csv


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Clean text in a CSV file.")
    parser.add_argument("input", type=Path, help="Path to the source CSV file")
    parser.add_argument("output", type=Path, help="Path for the cleaned CSV file")
    parser.add_argument(
        "--text-column", default="text", help="CSV column containing text (default: text)"
    )
    parser.add_argument(
        "--lowercase", action="store_true", help="Convert cleaned text to lowercase"
    )
    parser.add_argument(
        "--remove-stopwords",
        action="store_true",
        help="Remove a small built-in list of English stop words",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.input.resolve() == args.output.resolve():
        print("Error: input and output paths must be different.")
        return 1

    errors = validate_csv(args.input, args.text_column)
    if errors:
        for error in errors:
            print(f"Error: {error}")
        return 1

    try:
        rows_written = clean_csv(
            args.input,
            args.output,
            args.text_column,
            lowercase=args.lowercase,
            drop_stopwords=args.remove_stopwords,
        )
    except (OSError, UnicodeError, ValueError) as error:
        print(f"Error: {error}")
        return 1

    print(f"Cleaned {rows_written} rows into {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
