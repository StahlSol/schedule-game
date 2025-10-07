# player/state.py
# Tracks player actions, chosen events, and message state

from dataclasses import dataclass, field

@dataclass
class PlayerState:
    """Tracks the player’s state throughout a session."""
    
    # Event tracking
    suggested_event: str = None       # most recent suggested event
    confirmed_event: str = None       # agreed-upon event type
    confirmed_time: str = None        # agreed-upon time
    
    # Message tracking
    messages_sent_today: int = 0
    messages_without_response: int = 0
    
    # Other state
    last_message_hour: int = None     # last time a message was sent
    last_response_hour: int = None
    pending_messages: list = field(default_factory=list)
    
    # Utility flags
    event_decided: bool = False
    day_decided: bool = False
    
    def reset_daily(self):
        """Reset daily message counts and flags, but not confirmed events."""
        self.messages_sent_today = 0
        self.messages_without_response = 0
        self.pending_messages.clear()
        self.event_decided = False
        self.day_decided = False
