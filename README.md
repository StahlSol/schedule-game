# Cheff Cleff: Party Inviter Simulator
*“Get Cheff Cleff to commit to one social event. If you can.”*

## Overview
**Cheff Cleff: Party Inviter Simulator** is a short, dialogue-driven game played entirely through a simulated messaging interface.  
The player's objective is to get Clayton to agree to attend an event on a day he is actually free — despite vague replies, limited messaging, and random real-life interruptions.

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
- Over-messaging in a single day → Clayton becomes overwhelmed and may ignore messages.  
- Asking **too far in advance** yields “my schedule isn't released that far out” (wastes a message).  
- Asking **too late** can cause automatic conflicts (“I already made plans”).  
- Long/compound messages risk upsetting Clayton and may cause immediate negative outcomes.

---

## Player constraints

| Resource      | Limit       | Notes |
|---------------|-------------|-------|
| Messages      | 10 total    | Strategic communication budget. |
| Days window   | 6–9 days    | Player chooses the length at game start. |
| Mood bar      | 0–10        | Depletes with messaging and bad interactions; affects RNG. |

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
- Multiple Clayton personalities (e.g., Busy, Flaky, Hungover) for replayability.  
- Post-game summary explaining what went wrong/right.  
- Achievements for interesting edge-case outcomes.

---


