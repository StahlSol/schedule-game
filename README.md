# Cheff Cleff: Invitation Simulator
*“Get Cheff Cleff to commit to one social event. If you can.”*

## Overview
**Cheff Cleff: Party Inviter Simulator** is a short, dialogue-driven game played entirely through a simulated messaging interface.  
The player's objective is to get Cleff to agree to attend an event on a day he is actually free — despite vague replies, limited messaging, and random real-life interruptions.

---

## Core gameplay loop
1. Player selects the event window (8-11 days).  
2. Player may send as many messages as they want across those days.  
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
| Days window   | 8–11 days   | Player chooses the length during the session based on their impression of his schedule. |
| Mood   (Todo) | 0–10        | Depletes with messaging and bad interactions; affects RNG. |

## Game Week:

- [1] Thursday  
- [2] Friday
- [3] Saturday
- [4] Sunday
- [5] Monday
- [6] Tuesday     [Random new events added to schedule]
- [7] Wednesday
- [8] Thursday    [Possible event day]
- [9] Friday      [Possible event day]
- [10] Saturday   [Possible event day]
- [11] Sunday     [Possible event day]

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

##  Cheff Cleff Behavior Systems

Below is a breakdown of all core logic and RNG systems that govern Cheff’s behavior throughout the simulation.

---

###  1. Schedule Generation
- At the start of a session, a full weekly schedule is **randomly generated** for Cleff.
- Each day has an **85% base chance** to be a **work day**.
- Days marked as **off** have a **25% chance** at the start of the day to become a **call-in work day**.
- In the event of a call-in, the **type of work shift** is determined using the same probabilities as a normal work day.
- Since each day’s data is generated independently, **you cannot infer** future work days from known ones.

---

###  2. Work Day Types
Depending on the RNG roll, Cleff’s work schedule and communication patterns differ:

| Work Type | Probability | Work Hours | Response Behavior | Notes |
|------------|--------------|-------------|-------------------|-------|
| **Late Shift** | 65% | 12 PM – 8 PM | Responds in the morning only; ignores evening messages (final message guaranteed) | Common default shift |
| **Mid Shift** | 25% | 10 AM – 6 PM | May respond morning or night; 15% chance of **double-booking** | Most flexible |
| **Early Shift** | 10% | 8 AM – 4 PM | Only responds at night | Rarest schedule |

---

###  6. Communication Rules

Cleff’s communication follows semi-predictable patterns based on **time of day**, **message freshness**, and **mood**.  
The player must balance timing and tone to avoid overwhelming or frustrating him.


####  Message Freshness
Each hour that passes after sending a message reduces the chance of Cleff responding.  
The probability of a reply in any given free hour is calculated as: Response Chance = (Base Formula) + (Mood - 50) / 3
Base Formula = (90 - 8 × [hours since message])%

> **Example:**  
> If 3 hours have passed and Cleff’s mood is 65 →  
> Response Chance = (90 - 8×3) + (65 - 50)/3 = **66%** response chance.

- Messages become **stale** after 8 hours, effectively dropping to 0% chance of a reply that day.  
- Sending too many messages too quickly can trigger **Overload**.


####  Overload Condition
If the player sends **3 or more messages** without receiving a response:
- Cleff becomes **annoyed**, setting the `annoyed` flag for the rest of the day.  
- His **mood decreases by 10 permanently**.  
- He will **ignore all further messages** that day, except for his **guaranteed nightly response**.  
- The `annoyed` flag automatically **resets the next morning**.

---

####  Availability Rules
- Asking about a day more than **4 days in advance** results in:  
  > “I don’t have my schedule for that day yet.”  
- Cleff’s **work schedule** and **daily conditions** are independent; learning one day’s schedule doesn’t reveal others.


####  Guaranteed Responses
- Cleff will **always** send one message before bed, even if ignoring earlier ones.  

---

###  4. Hungover Condition
- **10% daily chance** for Cleff to start the day hungover.  
- While hungover:
  - No responses are possible until evening.
  - Mood temporarily set to **–10** for that day.
- Condition automatically clears at the **start of the next day**.

---
###  5. Dynamic Schedule Events

- Starting **on Day 5**, each remaining day has a chance to spontaneously generate a **new evening plan**, provided Cleff **isn’t working a late shift**.  
- These spontaneous plans can **conflict with pre-scheduled events**, potentially causing last-minute cancellations.

####  Chance of a New Plan
- **Morning Shift (8 AM – 4 PM):** 35% chance of scheduling a new plan.  
- **Afternoon Shift (10 AM – 6 PM):** 55% chance of scheduling a new plan.  
- **Evening Shift (12 PM – 8 PM):** Never schedules additional plans (already late).  

####  Possible Plans
New spontaneous plans may include:
- Drinking stream  
- Volleyball tournament  
- Grocery run  
- Dinner date with boyfriend  
- Going to bed early  
- Playing *Monster Hunter*

>  **Note:** If the “drinking stream” plan occurs, it guarantees a **Hungover Condition** for the following day.

---

###  6. Event Preferences
- There are **three event types**:
  1. Streamer Event  
  2. Rock Climbing  
  3. Going Drinking  
- For each session, Cleff is in the mood for **exactly one** of these.  
- The event he’s in the mood for is **randomly chosen** between the **two events not suggested first** (the first suggestion is **always declined**).

---

###  7. Scheduling Behavior
- Suggesting a **specific time** always results in a **positive response**, regardless of actual availability:  
  > “That sounds fun, I’ll try to make it!”
- However, this **does not guarantee attendance** — the day of the event will run final checks to see if he actually shows.

---
### 8. Mood Mechanic
- Cheff's mood starts at 100 points
- Each message sent lowers his mood by (n*0.65) where n is the amount of total messages sent
- Mood can be affected by hangover condition, lowering his mood by 10 for a day
- Having a morning shift will also lower his mood by 10 for that day
- Mood will effect the chance of responding with the following calculation: (Base chance)% + (Mood-50)/3%
- If Cheff is in a good mood, he will be more likely to respond

---

###  9. Event Day Resolution
On the scheduled event day, the game simulates Cleff’s day and runs sequential checks to determine attendance:

#### **  Preliminary Checks
**
Before the event simulation begins, two initial checks are performed to confirm that an event can actually occur.

1.  **Event Confirmed** — Has the player and Cleff agreed on a specific event type?  
   - If **no event** has bee# set, the simulation ends immediately with no outcome.

2.  **Time Agreed Upon** — Has a specific time been confirmed for the event?  
   - If **no time** was set, Cleff may respond ambiguously (“I’ll see what I can do”),  
     but the event will not proceed to simulation.

####  Attendance Checks
1.  **Original Schedule** — Is he working that day?  
2.  **Call-In Check** — Was he unexpectedly called into work?  
3.  **Mood Check** — `(100 - mood)%` chance to skip.  
4.  **Memory Check** — `(100 - memory freshness)%` chance to forget.  
5.  **Random Failure** — Flat 25% chance “something came up.”  

If any check fails:
- The event is canceled.
- Player receives an apology/excuse message referencing the last relevant flag (e.g. “Sorry, got called in,” “Something came up,” “Totally forgot!”).

---

## Player Mechanics

Each hour, the player can select one action:

### Core Actions
- **Suggest Event** – Choose from 3 event options (Streamer, Rock Climb, Drink)
- **Ask About X Day** – Check Cleff’s availability for a given day
- **Set / Reschedule Event** – Confirm or adjust the event date
- **Remind Him** – Boosts event memory freshness
- **Poke** – Nudges for a reply (resets message freshness slightly)
- **Wait 1 Hour** – Advances time by 1 hour (until 11pm)
- **Sleep** – Ends the day
  
