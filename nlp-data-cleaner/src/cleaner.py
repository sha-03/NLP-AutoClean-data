"""Text and CSV cleaning operations."""

import csv
import html
import re
from pathlib import Path

from src.nlp_processor import remove_stopwords
from src.utils import ensure_parent_directory


_URL_PATTERN = re.compile(r"https?://\S+|www\.\S+", flags=re.IGNORECASE)
_HTML_PATTERN = re.compile(r"<[^>]+>")
_WHITESPACE_PATTERN = re.compile(r"\s+")


def clean_text(text: str, lowercase: bool = False) -> str:
    """Remove HTML and URLs, decode entities, and normalize whitespace."""
    text = html.unescape(_HTML_PATTERN.sub(" ", text))
    text = _URL_PATTERN.sub(" ", text)
    text = _WHITESPACE_PATTERN.sub(" ", text).strip()
    return text.lower() if lowercase else text


def clean_csv(
    input_path: str | Path,
    output_path: str | Path,
    text_column: str,
    lowercase: bool = False,
    drop_stopwords: bool = False,
) -> int:
    """Clean the selected text column and write a CSV; return rows written."""
    ensure_parent_directory(output_path)
    rows_written = 0

    with Path(input_path).open("r", encoding="utf-8-sig", newline="") as input_file:
        reader = csv.DictReader(input_file)
        if reader.fieldnames is None:
            raise ValueError("Input CSV has no header row.")

        with Path(output_path).open("w", encoding="utf-8", newline="") as output_file:
            writer = csv.DictWriter(output_file, fieldnames=reader.fieldnames)
            writer.writeheader()
            for row in reader:
                text = clean_text(row.get(text_column) or "", lowercase=lowercase)
                if drop_stopwords:
                    text = remove_stopwords(text)
                row[text_column] = text
                writer.writerow(row)
                rows_written += 1

    return rows_written
