# game/schedule.py
from utils.rng_helpers import roll_chance

SHIFT_PROBS = {
    "12pm-8pm": 0.65,
    "10am-6pm": 0.25,
    "8am-4pm": 0.10
}

def generate_schedule(days: int = 11):
    """
    Generates an initial schedule for Cheff for the specified number of days.
    Each day has a shift type and optional called-in flag.
    """
    schedule = []
    for i in range(days):
        if roll_chance(85):  # 85% chance to work
            if roll_chance(65):
                shift = "12pm-8pm"
            elif roll_chance(25):
                shift = "10am-6pm"
            else:
                shift = "8am-4pm"
        else:
            shift = "off"

        schedule.append({
            "day_index": i,
            "shift": shift,
            "called_in": False,
            "confirmed_event": None,
            "confirmed_time": None
        })
    return schedule
