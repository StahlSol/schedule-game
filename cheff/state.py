# cheff/state.py
# Tracks Cheff's internal state

from dataclasses import dataclass, field
from typing import List, Dict, Optional

@dataclass
class CheffState:
    """
    Tracks Cheff's state throughout the game.
    """
    mood: int = 100              # 0-100
    memory: int = 100            # freshness of events/messages
    messages_without_response: int = 0
    last_activity: str = None         # Tracks what he was doing last
    night_message_flag: bool = False  # Did he respond only at night?

    # Daily flags reset each day
    daily_flags: Dict[str, bool] = field(default_factory=lambda: {
        "annoyed": False,
        "hungover": False,
        "called_in": False,
        "event_decided": False,
        "day_decided": False,
        "drinking_stream": False,
        "morning_shift": False,
        "afternoon_shift": False,
        "evening_shift": False,
        "day_off": False,
        
    })

    # 11-day schedule
    schedule: List[Dict] = field(default_factory=list)

    # Track current planned event
    current_event: Optional[str] = None
    current_event_time: Optional[str] = None

    def reset_daily_flags(self):
        """Reset transient daily flags at the start of a new day."""
        for key in self.daily_flags:
            self.daily_flags[key] = False
        self.messages_without_response = 0

    def set_flag(self, flag_name: str, value: bool = True):
        if flag_name not in self.daily_flags:
            raise KeyError(f"Unknown flag: {flag_name}")
        self.daily_flags[flag_name] = value

    def get_flag(self, flag_name: str) -> bool:
        return self.daily_flags.get(flag_name, False)
