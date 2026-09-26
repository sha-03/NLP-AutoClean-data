"""Input checks for CSV datasets."""

import csv
from pathlib import Path


def validate_csv(file_path: str | Path, text_column: str) -> list[str]:
    """Return validation errors for a CSV file and its selected text column."""
    path = Path(file_path)
    if not path.is_file():
        return [f"Input file does not exist: {path}"]

    try:
        with path.open("r", encoding="utf-8-sig", newline="") as csv_file:
            reader = csv.DictReader(csv_file)
            if reader.fieldnames is None:
                return ["Input CSV is empty or has no header row."]
            if text_column not in reader.fieldnames:
                return [
                    f"Text column '{text_column}' was not found. "
                    f"Available columns: {', '.join(reader.fieldnames)}"
                ]
            if next(reader, None) is None:
                return ["Input CSV has a header but contains no data rows."]
    except (OSError, UnicodeError, csv.Error) as error:
        return [f"Could not read input CSV: {error}"]

    return []
