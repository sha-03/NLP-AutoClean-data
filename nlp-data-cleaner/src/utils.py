"""Small shared utilities for the data-cleaning pipeline."""

from pathlib import Path


def ensure_parent_directory(file_path: str | Path) -> None:
    """Create the parent directory for a file path if it does not exist."""
    Path(file_path).parent.mkdir(parents=True, exist_ok=True)
