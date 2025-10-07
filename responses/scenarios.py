# responses/scenarios.py
# Event suggestion responses with optional dynamic contextual prefixes

import random

# Core responses for each event
EVENT_RESPONSES = {
    "rock_climbing": {
        "accept": [
            "Rock climbing sounds great! I’m in.",
            "Let’s do it! I’ve been wanting some exercise.",
            "Count me in for some climbing action!",
            "I’m ready for some vertical fun!"
        ],
        "decline": [
            "Nah, not feeling like climbing today.",
            "Maybe another time, climbing isn’t my vibe right now.",
            "I’ll pass on climbing, sorry!",
            "Climbing’s tough for me today, let’s skip it."
        ]
    },
    "streaming": {
        "accept": [
            "Streaming? I’m down, let’s set it up!",
            "Sounds fun, I’ll join the stream.",
            "Let’s go live! I’m in.",
            "I’m ready to stream, let’s do it."
        ],
        "decline": [
            "Streaming today? Not feeling it.",
            "I’ll skip the stream this time.",
            "Maybe later, streaming isn’t happening for me now.",
            "I’m not up for a stream right now."
        ]
    },
    "drinking": {
        "accept": [
            "Drinks? Yes, let’s go!",
            "I’m in for some drinks tonight!",
            "Sounds like a party, I’m joining!",
            "Count me in, time for a drink!"
        ],
        "decline": [
            "Not drinking today, sorry.",
            "I’ll pass on drinks this time.",
            "Maybe later, I’m skipping drinks today.",
            "Drinking’s not happening for me right now."
        ]
    }
}

# Optional dynamic prefixes for context
DYNAMIC_PREFIXES = {
    "night_message": "My bad, I was {activity} and didn’t see this. ",
    "hungover": "Ugh, I’m hungover and barely awake… ",
    "called_in": "Got pulled into work unexpectedly… ",
}

def get_event_response(event: str, accepted: bool, cheff=None, dynamic_chance: float = 0.5) -> str:
    """
    Randomly select a dialogue line for the given event and outcome.
    Optionally prepends a dynamic prefix based on Cheff's state.
    
    Parameters:
        event: Event key ('rock_climbing', 'streaming', 'drinking')
        accepted: True if Cheff accepted, False if declined
        cheff: CheffState object (optional, for dynamic context)
        dynamic_chance: Probability (0-1) that a dynamic prefix will appear
    """
    outcome = "accept" if accepted else "decline"

    if event not in EVENT_RESPONSES:
        core_response = "Cheff has nothing to say about that event."
    else:
        core_response = random.choice(EVENT_RESPONSES[event][outcome])

    # Add dynamic prefix occasionally
    prefix = ""
    if cheff and random.random() < dynamic_chance:
        if cheff.night_message_flag and cheff.last_activity:
            prefix = DYNAMIC_PREFIXES["night_message"].format(activity=cheff.last_activity)
        elif cheff.daily_flags.get("hungover", False):
            prefix = DYNAMIC_PREFIXES["hungover"]
        elif cheff.daily_flags.get("called_in", False):
            prefix = DYNAMIC_PREFIXES["called_in"]

    return prefix + core_response
