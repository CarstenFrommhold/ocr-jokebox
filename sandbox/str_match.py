""" Pure Python string comparison (fuzz packages lead to some C+ issues @Raspi)
"""
from difflib import SequenceMatcher
from operator import itemgetter
from typing import Tuple
from rapidfuzz import process, fuzz

# Note that Sequence Matcher is upper/lower sensitive.


def best_match(input: str, options: list) -> Tuple[str, float]:

    matches = []
    for option in options:
        matches.append((
            option,
            SequenceMatcher(None, input.lower(), option).ratio()
        ))

    matches.sort(reverse=True, key=itemgetter(1))
    return matches[0]

options_ = ["guns and roses", "coldplay", "daft punkt"]

print(best_match("Gusn an Roses", options_))
print(best_match("Cldpla1", options_))
print(best_match("COLDPLAY", options_))

print(
    process.extract(
    "Gusn an Roses", options_, scorer=fuzz.WRatio, limit=1)
)

print(
    process.extract(
    "Cldpla1", options_, scorer=fuzz.WRatio, limit=1)
)

print(
    process.extract(
    "Cldpla1", options_, scorer=fuzz.WRatio, limit=1)
)
