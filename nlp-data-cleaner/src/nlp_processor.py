"""Lightweight token and stop-word processing without external models."""

import re


_STOP_WORDS = frozenset(
    "a an and are as at be been but by for from had has have he her hers him his "
    "i in is it its me my of on or our ours she that the their theirs them they "
    "this those to was we were what when where which who will with you your yours".split()
)
_TOKEN_PATTERN = re.compile(r"\b[\w']+\b", flags=re.UNICODE)


def tokenize(text: str) -> list[str]:
    """Split text into word-like tokens."""
    return _TOKEN_PATTERN.findall(text)


def remove_stopwords(text: str) -> str:
    """Return tokens joined by spaces after removing a small English stop list."""
    return " ".join(
        token for token in tokenize(text) if token.casefold() not in _STOP_WORDS
    )
