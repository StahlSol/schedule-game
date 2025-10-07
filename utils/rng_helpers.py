# utils/rng_helpers.py
import random

def roll_chance(percent: float) -> bool:
    """
    Roll a random chance.
    :param percent: 0-100 chance
    :return: True if roll succeeds, False otherwise
    """
    return random.random() < percent / 100.0

def roll_multiple(odds: list) -> int:
    """
    Given a list of percentages, return the index that was selected.
    Example: [65, 25, 10] returns 0, 1, or 2 based on probability.
    """
    r = random.random() * 100
    cumulative = 0
    for i, p in enumerate(odds):
        cumulative += p
        if r < cumulative:
            return i
    return len(odds) - 1
