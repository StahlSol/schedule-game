class CheffState:
    def __init__(self):
        self.mood = 100
        self.memory = 100
        self.schedule = []
        self.daily_flags = {
            "annoyed": False,
            "hungover": False,
            "called_in": False,
            "event_suggested": False,
            "event_decided": False,
            "drinking_stream": False,
            "morning_shift": False,
            "afternoon_shift": False,
            "evening_shift": False,
            "day_off": False,
        }
        self.event_flags = {
            "rock_climbing": None,
            "drinking": None,
            "streaming": None
        }

        # Track current day/hour
        self.current_day = 0
        self.current_hour = 9

        # Dynamic response flags
        self.night_message_flag = False   # Was a message only responded to at night?
        self.last_activity = None         # Most recent activity/shift


    def set_flag(self, flag_name):
        self.daily_flags[flag_name] = True

    def reset_daily_flags(self):
        for key in self.daily_flags:
            self.daily_flags[key] = False
