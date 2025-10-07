# player/actions.py
# Functions for player interactions with Cheff

from player.state import PlayerState
from cheff.cheff import Cheff
from utils.rng_helpers import roll_chance
from utils.mood import adjust_mood
from utils.memory import decay_memory

def suggest_event(player: PlayerState, cheff: Cheff, event: str):
    """
    Player suggests an event to Cheff.
    First suggestion is always declined according to mechanics.
    """
    player.suggested_event = event
    player.messages_sent_today += 1
    player.messages_without_response += 1

    # Mood drop for declined suggestion
    adjust_mood(cheff, -2)

    # RNG determines eventual interest in suggested event
    if roll_chance(50):  # placeholder chance for acceptance of next suggestion
        cheff.daily_flags['event_decided'] = True
        cheff.schedule[0]['confirmed_event'] = event
        return True
    return False

def ask_about_day(player: PlayerState, cheff: Cheff, day_index: int):
    """
    Player asks about a specific day.
    Returns a vague response if day is too far in the future (>4 days ahead)
    """
    player.messages_sent_today += 1
    player.messages_without_response += 1

    if day_index > 4:  # 4-day rule
        return "I don't have my schedule for that day yet."
    else:
        # Vague availability
        return f"Seems like I might be free around the {cheff.schedule[day_index]['shift']} shift."

def set_event(player: PlayerState, cheff: Cheff, event: str, time: str):
    """
    Player confirms an event and time.
    Guaranteed positive response from Cheff.
    """
    player.confirmed_event = event
    player.confirmed_time = time
    player.event_decided = True
    player.day_decided = True

    # Cheff responds positively
    cheff.daily_flags['event_decided'] = True
    cheff.schedule[0]['confirmed_event'] = event
    cheff.schedule[0]['confirmed_time'] = time
    return f"Cheff: That sounds fun, I'll try to make it."

def poke(cheff: Cheff, player: PlayerState):
    """
    Refreshes message freshness and triggers overload if necessary.
    """
    player.messages_without_response = 0  # reset for simplicity
    # Overload logic
    if player.messages_without_response >= 3:
        cheff.daily_flags['annoyed'] = True
        adjust_mood(cheff, -10)
        return "Cheff is annoyed and won't respond until the nightly message."
    return "Poke sent."

def wait_one_hour(player: PlayerState, cheff: Cheff):
    """
    Player waits 1 hour; triggers memory decay and potential automatic responses.
    """
    decay_memory(cheff)
    # Placeholder: trigger any automatic reply logic here
