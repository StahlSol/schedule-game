# cheff/actions.py
# Functions that modify Cheff's state (mood, memory, schedule, responses)

from cheff.state import CheffState
from utils.rng_helpers import roll_chance
from utils.mood import adjust_mood
from utils.memory import decay_memory

def respond_to_suggestion(cheff: CheffState, suggestion: str) -> str:
    """
    Determines Cheff's response to a suggested event.
    First suggestion is always declined, subsequent suggestions depend on mood/RNG.
    """
    cheff.messages_without_response += 1

    # First suggestion always declined
    if not cheff.daily_flags["event_decided"]:
        adjust_mood(cheff, -2)  # mood drop for declining
        return f"Cheff: Nah, not feeling {suggestion} today."

    # Subsequent suggestions have a chance
    if roll_chance(50):  # placeholder, could be dynamic based on mood
        cheff.daily_flags["event_decided"] = True
        cheff.current_event = suggestion
        return f"Cheff: Ok, let's do {suggestion}!"
    else:
        adjust_mood(cheff, -1)
        return f"Cheff: Hmm, not sure about {suggestion}."

def apply_hangover(cheff: CheffState):
    """
    Sets the hungover flag and reduces mood for the day.
    """
    cheff.set_flag("hungover")
    adjust_mood(cheff, -10)

def receive_message(cheff: CheffState):
    """
    Update Cheff's state when a player message is received.
    Handles overload logic.
    """
    cheff.messages_without_response += 1

    if cheff.messages_without_response >= 3:
        cheff.set_flag("annoyed")
        adjust_mood(cheff, -10)
        return "Cheff is annoyed and won't respond until the nightly message."

def call_in_to_work(cheff: CheffState, day_index: int, shift_type: str):
    """
    Handles call-ins for off days.
    Updates the schedule and sets the called_in flag.
    """
    cheff.set_flag("called_in")
    if day_index < len(cheff.schedule):
        cheff.schedule[day_index]["called_in"] = True
        cheff.schedule[day_index]["shift"] = shift_type

def end_of_day_response(cheff: CheffState):
    """
    Sends the guaranteed end-of-day message.
    Resets annoyed flag for next day.
    """
    cheff.daily_flags["annoyed"] = False
    cheff.messages_without_response = 0
    # Mood may be updated based on events that day
    decay_memory(cheff)
    return "Cheff: That's it for today!"
