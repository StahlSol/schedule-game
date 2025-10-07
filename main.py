# main.py
from cheff.state import CheffState
from game.schedule import generate_schedule
from game.day import run_daily_cycle

def main():
    cheff = CheffState()
    cheff.schedule = generate_schedule()
    
    print("\n=== Full Schedule ===")
    for day in cheff.schedule:
        print(day)

    # Run the first day
    run_daily_cycle(cheff, 0)

if __name__ == "__main__":
    main()
