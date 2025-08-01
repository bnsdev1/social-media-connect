"""Simple in-memory dashboard for post history."""

from typing import List, Dict

POST_HISTORY: List[Dict] = []


def log_post(result: Dict) -> None:
    POST_HISTORY.append(result)


def get_history() -> List[Dict]:
    return POST_HISTORY
