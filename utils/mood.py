# utils/mood.py

def adjust_mood(cheff, amount: int):
    """
    Adjust Cheff's base mood by the given amount.
    Ensures mood stays within 0-100.
    """
    cheff.mood += amount
    if cheff.mood > 100:
        cheff.mood = 100
    elif cheff.mood < 0:
        cheff.mood = 0

def get_effective_mood(cheff, include_flags: bool = True) -> int:
    """
    Calculate Cheff's current effective mood, optionally including
    modifiers from daily flags.
    
    Parameters:
        cheff: CheffState object
        include_flags: if True, apply post-calculation adjustments
    Returns:
        effective mood (0-100)
    """
    mood = cheff.mood

    if include_flags:
        if cheff.daily_flags.get("hungover", False):
            mood -= 10
        if cheff.daily_flags.get("morning_shift", False):
            mood -= 5
        if cheff.daily_flags.get("called_in", False):
            mood -= 15
        if cheff.daily_flags.get("day_off", False):
            mood += 15

    # Clamp to 0-100
    if mood > 100:
        mood = 100
    elif mood < 0:
        mood = 0

    return mood
