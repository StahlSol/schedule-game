# cheff/behavior.py
from utils.rng_helpers import roll_chance

def calculate_response_chance(message, cheff):
    """
    Calculates Cheff's chance to respond to a pending message.
    Rules:
    - Night: 10, 11, 12 AM (22-24) only
    - Afternoon: 9 AM, 8 PM, 9 PM, 10 PM (9, 20, 21, 22)
    - Early: 6-11 PM (18-23)
    - Hungover: no response until 5 PM (17)
    - Annoyed: no response from chances
    """
    flags = cheff.daily_flags
    hour = message.get('hour', cheff.current_hour)

    # Annoyed blocks all responses
    if flags.get("annoyed"):
        return False

    # Hungover restriction
    if flags.get("hungover") and hour < 17:
        return False

    # Shift-specific restrictions
    if flags.get("morning_shift"):
        # Morning shift: can only respond outside work (before or after shift)
        if 8 <= hour <= 12:  # typical morning shift hours
            return False
    if flags.get("afternoon_shift"):
        # Afternoon shift: can only respond at 9, 20, 21, 22
        if hour not in [9, 20, 21, 22]:
            return False
    if flags.get("evening_shift"):
        # Evening shift: 18-23 allowed
        if hour not in [18, 19, 20, 21, 22, 23]:
            return False
    if flags.get("day_off"):
        # Day off: can respond any time
        pass

    # Base chance
    base_chance = 90
    # Reduce by message age
    base_chance -= 8 * message.get('age', 0)
    # Mood modifier
    mood_mod = (cheff.mood - 50) / 3
    base_chance += mood_mod
    # Clamp chance
    chance = max(0, min(100, base_chance))

    return roll_chance(chance)


def check_overload(cheff, pending_messages):
    """
    Checks if too many messages have been sent without a response.
    - If 3+ messages are pending, mood drops 10 and annoyed flag is set
    """
    if len(pending_messages) >= 3 and not cheff.daily_flags.get("annoyed"):
        cheff.mood -= 10
        cheff.set_flag("annoyed")
        print("Cheff is annoyed due to too many messages! Mood drops 10.")


def apply_night_responses(cheff, pending_messages):
    """
    At the end of the day, Cheff responds to all pending messages.
    Returns list of responses for display.
    """
    responses = []
    for msg in pending_messages:
        preamble = ""
        # Add dynamic preamble if message was delayed
        if msg.get('age', 0) > 0:
            last_activity = cheff.schedule[cheff.current_day]['shift']
            preamble = f"My bad, I was {last_activity} and didn't see this. "

        # Construct response
        responses.append(preamble + f"Responding to {msg['event'].replace('_', ' ').title()}.")
    return responses
