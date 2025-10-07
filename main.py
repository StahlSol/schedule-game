# main.py
from cheff.state import CheffState
from game.day import run_daily_cycle
from game.schedule import generate_schedule  # if schedule generation was moved here

def main():
    # Initialize Cheff
    cheff = CheffState()
    cheff.schedule = generate_schedule()  # generates full schedule

    # Debug: print entire schedule
    # print("\n=== Full Schedule ===")
    for day in cheff.schedule:
        print(day)

    # Loop through each day
    for day_index in range(len(cheff.schedule)):
        run_daily_cycle(cheff, day_index)
        input("Press Enter to proceed to the next day...")  # <-- pause between days

    print("All days completed! Thanks for playing.")

if __name__ == "__main__":
    main()
