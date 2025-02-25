from collections import Counter
from typing import Dict, List, Tuple


def get_num_words(text: str) -> int:
    """Returns the number of words in the given text."""
    return len(text.split())


def get_char_count(text: str) -> Dict[str, int]:
    """Returns a dictionary with counts of each character (case-insensitive) in the text."""
    return Counter(text.lower())


def get_sorted_char_count(char_count: Dict[str, int]) -> List[Tuple[str, int]]:
    """Returns a list of tuples sorted by character frequency in descending order."""
    return sorted(char_count.items(), key=lambda item: item[1], reverse=True)
