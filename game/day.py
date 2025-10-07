# game/day.py
from cheff.actions import apply_hangover, call_in_to_work, end_of_day_response
from utils.rng_helpers import roll_chance
from responses.scenarios import get_event_response

def start_of_day(cheff, day_index: int):
    """
    Prepares Cheff for a new day:
    - Reset daily flags
    - Determine call-ins
    - Apply hungover condition if necessary
    """
    cheff.reset_daily_flags()
    print(f"\n--- Day {day_index + 1} Start ---")
    print(f"Initial mood: {cheff.mood}, memory: {cheff.memory}")

    day = cheff.schedule[day_index]

    if day["shift"] == "off" and roll_chance(25):
        call_in_to_work(cheff, day_index, "10am-6pm")
        print(f"Cheff got called into work today! New shift: {cheff.schedule[day_index]['shift']}")

    if roll_chance(10):
        apply_hangover(cheff)
        print("Cheff is hungover today!")

    # Set shift flags
    if "12pm-8pm" in day["shift"]:
        cheff.set_flag("evening_shift")
    elif "10am-6pm" in day["shift"]:
        cheff.set_flag("afternoon_shift")
    elif "8am-4pm" in day["shift"]:
        cheff.set_flag("morning_shift")
    else:
        cheff.set_flag("day_off")

    # Reset first suggestion and decision flags
    cheff.daily_flags["event_suggested"] = False
    cheff.daily_flags["event_decided"] = False

    # Initialize event flags if not present
    if not hasattr(cheff, "event_flags"):
        cheff.event_flags = {
            "rock_climbing": None,
            "drinking": None,
            "streaming": None
        }

    print(f"Day schedule: {day}")
    print(f"Daily flags: {cheff.daily_flags}")

def run_daily_cycle(cheff, day_index: int):
    """
    Handles the full daily loop:
    - Hourly message processing
    - Player actions
    - End-of-day wrap-up
    """
    start_of_day(cheff, day_index)
    print("\nMan, I really want to hang out with my friend Cheff. I should see if he's free next week.\n")

    current_hour = 9
    end_hour = 23
    pending_message = None

    while current_hour <= end_hour:
        print(f"\n--- Hour {current_hour}:00 ---")
        print(f"Cheff mood: {cheff.mood}, memory: {cheff.memory}")
        print(f"Daily flags: {cheff.daily_flags}")

        if pending_message:
            pending_message['age'] += 1
            if not cheff.daily_flags.get("hungover") or cheff.daily_flags.get("day_off") \
               or cheff.daily_flags.get("morning_shift") or cheff.daily_flags.get("afternoon_shift") \
               or cheff.daily_flags.get("evening_shift"):
                if roll_chance(90):
                    response_text = get_event_response(
                        pending_message['event'],
                        pending_message['accepted'],
                        cheff
                    )
                    print(f"Cheff responds: {response_text}")
                    pending_message = None

        # Show player options
        print("\nChoose an action:")
        print("1. Suggest Event")
        print("2. Ask Availability")
        print("3. Poke")
        print("4. Set Event Date")
        print("5. Remind")
        print("6. Wait 1 hour / Sleep")

        try:
            action = int(input("> "))
        except ValueError:
            print("Invalid input. Choose a number 1-6.")
            continue

        # Here you can either implement each action or delegate to a helper
        if action == 1:
            # Suggest event logic (with first-suggestion decline & event flags)
            from game.actions import handle_suggest_event  # optional modular approach
            pending_message = handle_suggest_event(cheff)
        elif action == 2:
            print("Ask availability not implemented yet.")
        elif action == 3:
            print("Poke: Refreshing message freshness.")
        elif action == 4:
            print("Set Event Date: Scheduling not implemented yet.")
        elif action == 5:
            print("Remind: Reminder not implemented yet.")
        elif action == 6:
            print("Waiting 1 hour...")
        else:
            print("Invalid choice.")

        current_hour += 1

    print("\n" + end_of_day_response(cheff))
    print(f"End-of-day flags: {cheff.daily_flags}\n")
