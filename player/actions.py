# player/actions.py
# Functions for player interactions with Cheff

from player.state import PlayerState
from cheff.cheff import Cheff
from utils.rng_helpers import roll_chance
from utils.mood import adjust_mood
from utils.memory import decay_memory

def suggest_event(player, cheff, event: str, day_index: int):
    """
    Player suggests an event to Cheff.
    - First suggestion is always declined
    - Remaining events follow event_flags 50/50 logic
    - Updates mood, daily_flags, and event_flags
    Returns a pending_message dict for the daily loop
    """
    # Track player's suggestion
    player.suggested_event = event
    player.messages_sent_today += 1
    player.messages_without_response += 1

    # Initialize event_flags if not present
    if not hasattr(cheff, "event_flags"):
        cheff.event_flags = {
            "rock_climbing": None,
            "drinking": None,
            "streaming": None
        }

    # First suggestion of the day
    if not cheff.daily_flags.get("event_suggested"):
        accepted = False
        cheff.daily_flags["event_suggested"] = True
        cheff.event_flags[event] = 0  # always decline first suggestion

        # Determine remaining flags for other events
        remaining_events = [e for e, val in cheff.event_flags.items() if val is None]
        if len(remaining_events) == 2:
            if roll_chance(50):
                cheff.event_flags[remaining_events[0]] = 1
                cheff.event_flags[remaining_events[1]] = 0
            else:
                cheff.event_flags[remaining_events[0]] = 0
                cheff.event_flags[remaining_events[1]] = 0

        adjust_mood(cheff, -2)  # mood drop for declined suggestion

    else:
        # Subsequent suggestions
        accepted = cheff.event_flags.get(event, 0) == 1
        if accepted:
            cheff.daily_flags["event_decided"] = True
        adjust_mood(cheff, -2)  # slight mood drop regardless

    # Build pending message
    pending_message = {
        'event': event,
        'accepted': accepted,
        'age': 0,
        'hour': player.current_hour  # track when the message was sent
    }

    return pending_message

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
