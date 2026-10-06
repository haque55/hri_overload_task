# HRI Project: Two Arms with ESP32 Screens

Team: Enrique Feria Abascal, Samin Haque, Sinan Onder. Updated 6 October 2026.

The study stays the same as the block version (`HRI_Study_Design_Final_Presentable`). We only replace the physical blocks with two ESP32 touch screens, one held by each Kinova Gen3 arm. The research question, constructs, H1 to H4, measures, design, 16 participants and 10-minute sessions are unchanged. The updated form is `HRI_Study_Design_ESP32_TwoArms.docx` in this folder.

![The two modes](HRI_ESP32_Two_Modes.png)

## 1. The idea in short

- Each block still has a colour and a number from 1 to 9, but it is now digital and split across the two arms. The **left arm's screen shows the colour** (the whole screen lights up in red, blue or yellow). The **right arm's screen shows the number** (a large white digit).
- An arm moves its screen from a waiting position toward the participant. The screen lights up only when the arm has stopped.
- The participant **takes** each half by touching its screen. This replaces taking a block from the gripper. The screen goes blank and the arm moves it away again. If nobody touches it within 2 seconds, it moves away anyway.
- The participant **sorts** the block by pressing one of three large coloured buttons (red, blue, yellow). These replace the three bins.
- The participant keeps a **running mental total** of the numbers, as before.

## 2. The two modes

| | Coordinated (baseline) | Uncoordinated |
|---|---|---|
| How the arms move | Together, like one team | Independently, each on its own schedule |
| Arrival | Both screens arrive at the same time, every 5 s | Never at the same time: colour and number of a block arrive 1 to 3 s apart |
| Which comes first | Always both together | Colour first in 10 blocks, number first in 10, mixed unpredictably |
| Each arm's own gap | 5 s | 4 to 7 s (average about 5 s) |
| Gap between any two arrivals | 5 s | 1 to 4 s |
| Blocks and trial length | 20 blocks, last arrival at 95 s | Same 20 blocks, last arrival at 95 s |
| Arm speed, positions, screens, buttons | Same | Same |

In the coordinated mode the participant sees one complete block every 5 seconds and can catch both screens with both hands. In the uncoordinated mode the same information comes in two separate pieces at moments the participant cannot predict, so they have to watch both arms all the time. That is what "robot temporal coordination between the two arms" means in this study.

### Arrival times (seconds from trial start)

The uncoordinated sequence was generated once with fixed rules and is used for every participant. Rules: each arm needs at least 4 s between its own arrivals (1 s in, up to 2 s at the participant, 1 s out); any two arrivals are at least 1 s apart; the two halves of a block are 1 to 3 s apart; colour-first and number-first are balanced 10 and 10, with never more than 3 in a row the same way; first arrival at 0 s and last at 95 s, as in the coordinated trial.

| Block | Coordinated (both arms) | Uncoordinated: colour (left) | Uncoordinated: number (right) | First |
|---|---|---|---|---|
| 1 | 0 | 1 | 0 | number |
| 2 | 5 | 5 | 6 | colour |
| 3 | 10 | 9.5 | 11 | colour |
| 4 | 15 | 14 | 15.5 | colour |
| 5 | 20 | 21 | 19.5 | number |
| 6 | 25 | 26 | 25 | number |
| 7 | 30 | 31 | 29.5 | number |
| 8 | 35 | 35 | 36 | colour |
| 9 | 40 | 39 | 40.5 | colour |
| 10 | 45 | 43.5 | 45.5 | colour |
| 11 | 50 | 50.5 | 49.5 | number |
| 12 | 55 | 54.5 | 56 | colour |
| 13 | 60 | 61 | 60 | number |
| 14 | 65 | 65.5 | 64 | number |
| 15 | 70 | 69.5 | 71 | colour |
| 16 | 75 | 73.5 | 76 | colour |
| 17 | 80 | 78 | 80 | colour |
| 18 | 85 | 85 | 84 | number |
| 19 | 90 | 91 | 88 | number |
| 20 | 95 | 95 | 93.5 | number |

These times assume a 1 s move each way. If the real arms need longer at a safe speed (measured in week 2), the schedule is stretched with the same rules.

### Block sequences

Two matched sequences: 7 red, 7 blue and 6 yellow blocks each, the same 20 numbers, total 97 in both, different order and pairing. They are swapped across conditions, as in the block version.

- **Sequence A:** Red 2, Red 1, Yellow 6, Blue 2, Blue 3, Red 9, Red 4, Blue 3, Yellow 6, Blue 4, Yellow 5, Yellow 8, Red 5, Blue 4, Yellow 9, Red 1, Blue 3, Yellow 7, Blue 8, Red 7
- **Sequence B:** Blue 9, Yellow 3, Yellow 2, Blue 3, Blue 9, Yellow 1, Red 6, Yellow 4, Blue 5, Red 4, Red 2, Yellow 8, Red 6, Yellow 7, Red 3, Blue 4, Red 8, Red 5, Blue 1, Blue 7

Crossing the two orders with the two sequences gives 4 groups of 4 participants.

## 3. What makes it more fun

- **Catching screens.** The participant reaches out and touches a lit screen, a bit like catching a ball. On touch, the coloured tile or the number gives a short "caught" animation and the board's speaker clicks. This is the same in both modes and gives no right or wrong feedback.
- **Big arcade buttons** for sorting, with a satisfying click, instead of dropping blocks into bins.
- **Two-handed catches** in the coordinated mode, when both screens arrive together.
- **Demo mode for the course presentation only** (not used with participants): the screens show each person's catch time after a short round. It is a fun way to show the setup on presentation day.

## 4. What changed in the form, and what did not

Only the sentences that described physical blocks, bins, grippers or handovers were rewritten. Everything else is word for word the Final Presentable version.

| Section | Change |
|---|---|
| Specific research question | "handover timing" became "timing between two Kinova Gen3 arms that present information on ESP32 screens" |
| Constructs | Compensatory behaviour: "double waits" became "missed pickups" |
| H2 | "take blocks later" became "take the screens later"; "more double waits" became "miss more pickups" |
| Experimental conditions | New description of the screens, the touch to take, and the two modes (section 2 above); buttons replace bins |
| Ordering effects | "reloads the blocks" became "loads the next trial" (no physical reload needed) |
| Objective measures | Sorting accuracy is read from the button log. Pickup latency is now "screen stops until touch". **Double waits** became **missed pickups** (a screen leaves after 2 s without a touch) |
| Procedure | Workstation now has three coloured buttons and two screens; everything else unchanged |
| Hypotheses H1, H3, H4, manipulation check, NASA-TLX, setup choice, interview, session timing, sample size | Unchanged |

Why double waits had to go: in the coordinated mode both screens always arrive together, so "two things waiting at once" happens in every block by design and says nothing about compensation. Missed pickups measures the same idea (the participant cannot keep up with the robots) and works in both modes.

## 5. Recheck of HRI_Study_Design_Final_Presentable

- Text is clean: no long dashes or arrows, British spelling throughout, all 7 Hoffman and Zhao hint lines plus the one Section 8.6 mention, headings in the course order.
- One formatting fault: the H1 bullet was in a separate Word list from H2 to H4. It looks the same, but editing the list in Word behaves oddly. Fixed in the new file, so all four hypotheses are now in one list.
- Weak points that the blocks version already had, and that the screens version keeps on purpose because we are keeping the study the same. Any of them can still be fixed later:
  1. Sorting accuracy will probably be near 100% in both modes, so "sorting stays the same" (H3) is partly guaranteed by an easy task.
  2. The running sum gives only one number per trial. An unannounced check after block 10 would add a second.
  3. The manipulation check comes before NASA-TLX, so it may hint at the timing before workload is rated. Swapping the order fixes this.
  4. The practice trial timing is not specified. Mixing both modes in the practice would keep it neutral.
- Already solved by the screens: the exact pickup moment now comes from the touch screen, sorting is logged by the buttons instead of scored live, and there is no block reloading between trials.

## 6. Hardware

| Item | Choice | Note |
|---|---|---|
| Arms | 2 Kinova Gen3, one on each side of the workstation | Second arm moved to IP 192.168.1.11 |
| Screens | 2 M5Stack Core2 (ESP32, 2.0 inch capacitive touch screen, battery, speaker) | Battery means no cable along the arm. Capacitive touch needs no pressing force. |
| Screen holders | 3D-printed cradle with a 40 mm square handle the gripper closes on | Bolt to the tool flange instead if there is no gripper |
| Sorting buttons | 3 large arcade buttons (red, blue, yellow) with a USB encoder in a small box | Shows up on the PC as a game controller, no firmware needed |
| Network | Small dedicated Wi-Fi router | Screens and PC on it; arms on their own Ethernet links |
| PC | Ubuntu 22.04, ROS 2 Humble | One PC for both arms, screens and buttons, so all times use one clock |

Rough cost of new parts: about 150 euro (two screens about 100, buttons and encoder about 20, router about 30).

## 7. Software

| Piece | What it does |
|---|---|
| Screen firmware (Arduino, M5Unified) | Waits on UDP for `SHOW <id> <colour or number>` and `BLANK <id>`. Draws, then replies `LIT <id>`. On a touch while lit, sends `TOUCH <id>` and plays the catch animation. Ignores touches while blank. |
| Arm node, one per arm (ROS 2, rclpy) | Same plan as for the blocks: stock `ros2_kortex` driver, each arm in its own ROS domain (11 and 12), taught poses replayed with fixed move times, no MoveIt. Per presentation: move to the presentation pose to arrive at the scheduled time, send `SHOW`, wait for `TOUCH` or 2 s, send `BLANK`, move back. No picking from a chute, so the cycle is much simpler than with blocks. |
| Button logger | Reads the USB button box and logs each press with the PC time |
| Session script | Starts both arm nodes with one shared start time and the participant's group |
| Analysis notebook | pandas, pingouin, scipy, matplotlib |

**Log, one row per screen presentation:** participant, group, condition, trial, arm, block index, colour or number, scheduled arrival, arm stopped, screen lit, touch time, blank time, missed flag.
**Button log:** participant, trial, PC time, colour pressed.

## 8. Measures and analysis

| | Measure | Test |
|---|---|---|
| Manipulation check | 2 items, 7-point, reported first | Wilcoxon signed-rank |
| H1 workload | Raw NASA-TLX total (subscales exploratory) | Paired t-test, effect size dz |
| H2 compensatory behaviour | Pickup latency (mean and variability), missed pickups, TLX Effort | Paired t-tests; Wilcoxon for missed pickups |
| H3 performance | Sorting accuracy (button presses matched to blocks in order), running-sum error | Wilcoxon signed-rank (small counts, many zeros) |
| H4 acceptance | Setup choice | Exact binomial test, at least 13 of 16 |

With 16 participants a paired t-test detects only large effects (dz about 0.75), so effect sizes are always reported.

## 9. Safety

- The participant touches screens held by the arms, so the safety rules from the block handover still apply. The presentation pose is within easy reach, at chest height, never above the head.
- Screens stay blank while the arms move, so the cue to reach is a lit screen on a stopped arm. Participants are told to touch only lit screens.
- Speed and acceleration limits on, collision detection confirmed active in the ROS control mode, protection zones set. The two arms' workspaces do not overlap.
- Check in the pilot that touching the screen never trips the arm's collision protection. Capacitive touch needs almost no force.
- A researcher stands at the emergency stop for the whole robot part.

## 10. Pilot checks (week 4)

1. Every touch is detected and logged, and the 2 s limit feels fair in the coordinated mode.
2. The uncoordinated mode feels harder and gives some missed pickups or sum errors. If it does not, shorten the gaps in both modes, keeping the same averages.
3. The colour screen is readable at a glance and the number is legible from the participant's position.
4. A full session fits in 10 minutes (book 15-minute slots anyway).

## 11. Timeline (6 October to mid-December 2026)

| Week | Dates | Robot and hardware | Software | Study and participants | Milestone |
|---|---|---|---|---|---|
| 1 | 5 to 11 Oct | Order 2 screens, button box parts, router. Move the second arm to IP .11. Both arms moving with the stock ROS 2 driver. Confirm gripper and DoF. | ROS 2 Humble on the lab PC; fake hardware on laptops. | Send the updated form to the supervisor. Ask about ethics approval now. | Design agreed |
| 2 | 12 to 18 Oct | Print and fit both screen holders. Teach waiting and presentation poses on both arms. Time the moves. | Screen firmware (SHOW, BLANK, TOUCH). Button box logging. | | **M1:** each arm brings a lit screen and a touch is logged (18 Oct) |
| 3 | 19 to 25 Oct | Fix the workstation layout and e-stop position. | Arm nodes on fake hardware, then both real arms running from the schedule. Touch to leave, 2 s limit, logging. Full dry run. | Instructions script, consent form, debrief, questionnaires (check items, NASA-TLX, setup choice). Start recruiting outside the HRI course. | **M2:** a full trial runs and logs end to end (25 Oct) |
| 4 | 26 Oct to 1 Nov | Safety check with the supervisor. | Analysis notebook built on pilot logs. | Pilot with 2 to 3 lab members, tune timing, book slots. | **M3:** protocol frozen, ethics cleared (1 Nov) |
| 5 to 6 | 2 to 15 Nov | Arms on standby. | Check logs after every session day. | 18 participants in 15-minute slots, about 3 afternoons, rest is buffer. | **M4:** data complete (15 Nov) |
| 7 | 16 to 22 Nov | Pack down. | Run the analysis: manipulation check first, then H1 to H4. | | **M5:** results ready (22 Nov) |
| 8 | 23 to 29 Nov | Film the setup in both modes for the presentation. | Final figures. | Write methods and results. | |
| 9 | 30 Nov to 6 Dec | | | Discussion, full report draft, slides, internal review. | Draft complete (6 Dec) |
| 10 | 7 to 13 Dec | Demo mode ready for presentation day. | | Final edits, rehearse, present and submit. | **M6:** submitted (by 13 Dec) |

**Work split** (assign names at the next meeting):

- **Robot and safety:** both arms, poses, screen holders, protection zones, workstation, e-stop.
- **Software:** screen firmware, arm nodes, button logger, session script, schedule.
- **Study side:** instructions, consent, questionnaires, recruiting, pilot, analysis notebook.

**Critical path:** ethics approval and M2. If ethics is not cleared by 1 November, data collection moves to 16 to 29 November and weeks 7 and 8 merge. If both arms are not running from ROS by M2, use the Kinova Python API for the trial loop instead; nothing else in the plan changes.

## 12. Risks and fallbacks

| Risk | Fallback |
|---|---|
| Wi-Fi delay on touch or screen messages (should stay under about 50 ms) | USB cables to the screens |
| Touch trips the arm's collision protection | Raise the thresholds slightly and add automatic fault clearing, or use a softer touch (screen in a padded frame) |
| Arms slower than 1 s per move at safe speed | Stretch the schedule with the same rules; trial gets a few seconds longer |
| Uncoordinated mode not harder in the pilot | Shorter gaps in both modes, same averages |
| A screen battery runs low | Charge between session blocks; USB-C cable as backup |
| One arm faults during a session | Clear faults and repeat the trial; note it in the log |
