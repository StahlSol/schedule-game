# main.py
from cheff.state import CheffState
from cheff.actions import apply_hangover, call_in_to_work, end_of_day_response
from utils.rng_helpers import roll_chance
from responses.scenarios import get_event_response

SHIFT_TYPES = ["morning", "afternoon", "evening", "off"]

SHIFT_PROBS = {
    "12pm-8pm": 0.65,
    "10am-6pm": 0.25,
    "8am-4pm": 0.10
}

def generate_schedule(days: int = 11):
    schedule = []
    for i in range(days):
        if roll_chance(85):
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

def start_of_day(cheff: CheffState, day_index: int):
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

    if "12pm-8pm" in day["shift"]:
        cheff.set_flag("evening_shift")
    elif "10am-6pm" in day["shift"]:
        cheff.set_flag("afternoon_shift")
    elif "8am-4pm" in day["shift"]:
        cheff.set_flag("morning_shift")
    else:
        cheff.set_flag("day_off")

    # Reset first suggestion flag for the day
    cheff.daily_flags["event_suggested"] = False
    cheff.daily_flags["event_decided"] = False

    # Reset event flags if first day
    if not hasattr(cheff, "event_flags"):
        cheff.event_flags = {
            "rock_climbing": None,
            "drinking": None,
            "streaming": None
        }

    print(f"Day schedule: {day}")
    print(f"Daily flags: {cheff.daily_flags}")

def main():
    cheff = CheffState()
    cheff.schedule = generate_schedule()

    print("\n=== Full Schedule ===")
    for day in cheff.schedule:
        print(day)

    # Start Day 1
    day_index = 0
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

        if action == 1:
            print("\nWhich event to suggest?")
            print("1. Rock Climbing")
            print("2. Drinking")
            print("3. Streaming")
            event_choice = input("> ")
            events_map = {"1": "rock_climbing", "2": "drinking", "3": "streaming"}
            event = events_map.get(event_choice)

            if event:
                # First suggestion
                if not cheff.daily_flags.get("event_suggested"):
                    accepted = False
                    cheff.daily_flags["event_suggested"] = True
                    cheff.event_flags[event] = 0

                    # Determine remaining flags
                    remaining_events = [e for e in cheff.event_flags if cheff.event_flags[e] is None]
                    if len(remaining_events) == 2:
                        if roll_chance(50):
                            cheff.event_flags[remaining_events[0]] = 1
                            cheff.event_flags[remaining_events[1]] = 0
                        else:
                            cheff.event_flags[remaining_events[0]] = 0
                            cheff.event_flags[remaining_events[1]] = 0

                    print("First suggestion of the day is automatically declined.")

                else:
                    # Subsequent suggestions
                    if cheff.event_flags[event] == 1:
                        accepted = True
                        cheff.daily_flags["event_decided"] = True
                    else:
                        accepted = False

                pending_message = {'event': event, 'accepted': accepted, 'age': 0}
                cheff.mood -= 5

                print(f"You suggested {event.replace('_', ' ').title()} to Cheff.")
                if accepted:
                    print("Cheff seems like he might accept this...")
                else:
                    print("Cheff seems unsure or likely to decline.")
            else:
                print("Invalid choice.")

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

if __name__ == "__main__":
    main()
