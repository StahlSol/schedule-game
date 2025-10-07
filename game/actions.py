# game/actions.py
from utils.rng_helpers import roll_chance

def handle_suggest_event(cheff):
    """
    Handles the player suggesting an event to Cheff.
    Rules:
    - First suggestion of the day is automatically declined
    - Remaining events: one accepted by 50/50 chance, the other declined
    - Event flags are permanent for the session
    - Sets daily_flags['event_suggested'] and daily_flags['event_decided']
    Returns a pending message dict with 'event', 'accepted', and 'age'
    """
    print("\nWhich event to suggest?")
    print("1. Rock Climbing")
    print("2. Drinking")
    print("3. Streaming")

    events_map = {"1": "rock_climbing", "2": "drinking", "3": "streaming"}

    while True:
        event_choice = input("> ")
        event = events_map.get(event_choice)
        if event:
            break
        else:
            print("Invalid choice. Pick 1, 2, or 3.")

    # Initialize event_flags if not already
    if not hasattr(cheff, "event_flags"):
        cheff.event_flags = {e: None for e in events_map.values()}

    # First suggestion logic
    if not cheff.daily_flags.get("event_suggested"):
        accepted = False
        cheff.daily_flags["event_suggested"] = True
        cheff.event_flags[event] = 0  # always decline first suggestion

        # Determine remaining events permanently
        remaining_events = [e for e in cheff.event_flags if cheff.event_flags[e] is None]
        if len(remaining_events) == 2:
            if roll_chance(50):
                cheff.event_flags[remaining_events[0]] = 1
                cheff.event_flags[remaining_events[1]] = 0
            else:
                cheff.event_flags[remaining_events[0]] = 0
                cheff.event_flags[remaining_events[1]] = 1


    else:
        # Subsequent suggestions
        flag_value = cheff.event_flags.get(event)
        if flag_value == 1:
            accepted = True
            cheff.daily_flags["event_decided"] = True
        else:
            accepted = False

    # Sending message reduces mood slightly
    cheff.mood -= 5
    print(f"You suggested {event.replace('_', ' ').title()} to Cheff.")


    # Return pending message object
    return {'event': event, 'accepted': accepted, 'age': 0}
