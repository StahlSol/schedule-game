# Cheff Cleff: Party Inviter Simulator
*“Get Cheff Cleff to commit to one social event. If you can.”*

## Overview
**Cheff Cleff: Party Inviter Simulator** is a short, dialogue-driven game played entirely through a simulated messaging interface.  
The player's objective is to get Cleff to agree to attend an event on a day he is actually free — despite vague replies, limited messaging, and random real-life interruptions.

---

## Core gameplay loop
1. Player selects the event window (6–9 days).  
2. Player may send **10 messages total** across those days.  
3. Clayton replies with varying accuracy, tone, and timing.  
4. Player picks which day will be the event.  
5. The game resolves on the **Day of Reckoning** (success or one of many failure reasons).

---

## Messaging system
- UI simulates a messaging app (timestamps, typing bubbles, read receipts optional).  
- Player chooses how many messages to send each day (subject to the 10-message cap).  
- Over-messaging in a single day → Cleff becomes overwhelmed and may ignore messages.  
- Asking **too far in advance** yields “my schedule isn't released that far out” (wastes a message).  
- Asking **too late** can cause automatic conflicts (“I already made plans”).  
- Long/compound messages risk upsetting Clayton and may cause immediate negative outcomes.

---

## Player constraints

| Resource      | Limit       | Notes |
|---------------|-------------|-------|
| Messages      | 10 total    | Strategic communication budget. |
| Days window   | 6–9 days    | Player chooses the length during the session based on their impression of his schedule. |
| Mood bar      | 0–10        | Depletes with messaging and bad interactions; affects RNG. |

## Game Week:



---

## Hidden mechanics & RNG
- Clayton’s real schedule is **hidden** and only hinted at via vague replies (e.g. “Probably free in the afternoon”).  
- Each scheduled plan has hidden constraints (work end times, naps, etc.) which are not fully revealed to the player.  
- Random sabotage events can occur and guarantee failure even if the day is correctly chosen (examples: car trouble, family call, sudden work shift, hungover).  
- The chance of these events is affected by Clayton’s mood and prior interactions.

---

## Day of Reckoning (resolution)
- **Success:** Clayton shows up.  
- **Failure:** A personalized excuse is delivered (e.g. “Forgot,” “Work called me in,” “Too tired after work,” “Something came up,” etc.).  
- Outcome text explains *why* Clayton didn’t come.

---

## Mood & impact
- The **Mood Bar** (visual element) represents Clayton’s tolerance and patience.  
- Mood decreases with: many messages, alarmist/compound messages, and annoying timing.  
- Mood influences:
  - Helpfulness/clarity of responses.  
  - Likelihood of RNG failures.  
  - Probability Clayton honors the plan.

---

## Design philosophy
- No explicit tutorials — players learn by experimenting and failing.  
- Tone is comedic, dry, and painfully relatable.  
- Focus on short play sessions and strong emergent narrative from poor communication.

---

## Planned features
- Message-app styled GUI (typing indicators, subtle sounds).  
- Post-game summary explaining what went wrong/right.  
- Achievements for interesting edge-case outcomes.
- Rely on a large pool of pre-written dialogue options and responses
- Utilize many flags that will alter the responses slightly with dynamic string creation

---

## Cheff Cleff Mechanics

- At the start of the session, a full schedule is randomly generated for Cleff
- Each day has an 85% chance of becoming a work day  
- Depending on the kind of work day, his actions that day will change.
- Free days he tends to stream
- 65% to work 12pm-8pm - He won't respond in the evening (final message of the day is still guarenteed), but will respond in the morning
- 25% to work 10am-6pm - He can respond at night or morning but has a 15% chance of double booking on these days
- 10%  to work 8am - 4pm - He will only respond at night. 
- Since its all RNG, there is nothing to interpret about the other work days of the week based on a single known day.
- Each hour Cleff is free, he has a (90 - 8*[hours since message])%  chance to respond to an unanswered message. (message freshness)
- Each day, Cleff has a 10% of being hung over, making it impossible to receive any responses from him until evening.
- At the end of the day, he's guarenteed to respond before bed.
- On day 5, each remaining day has a 35% chance spontaniously have a new plan in the evening (if it's not a late work day)
- There will be 3 options for events to do with Cheff (streamer event, rock climbing, going drinking)
- Each session, Cleff will be in the mood for exactly 1 of these events.
- The event he is in the mood for will always be a 50/50 chance between the 2 options that were not initially suggested
- This means the first suggestion will always be declined. 

## Player Mechanics

- Each hour, the player can select an action:
  
* Suggest Event (3 options) -> Ask about X day -> Double Check availability
* Set date of event -> Reschedule
* Remind him of the event
* Poke (refresh the freshness of the current message waiting)
* Wait 1 hour (until the end of the day, 11pm)
* Sleep (at the end of the day)

  
