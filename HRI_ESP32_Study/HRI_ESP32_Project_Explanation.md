# HRI Project: Two Robot Heads, a Depth Camera and ROS 2

Team: Enrique Feria Abascal, Samin Haque, Sinan Onder. Updated 7 October 2026.

This folder holds the whole project in three files:
- `HRI_Study_Design_ESP32_RobotHeads.docx`: the course study design form.
- This explanation file.
- `HRI_ESP32_Two_Modes.png`: the image below.

![Setup and the two modes](HRI_ESP32_Two_Modes.png)

## 1. Summary

- Two **robot heads** (ESP32 screens with animated faces, on stands) stand left and right of the participant.
- **Each robot gives its own instruction**: a colour (red or blue) and a number. The participant takes a block with that number from a tray and puts it in the bin of that colour.
  - At most two blocks are open at once (one per robot), and they can be done in **either order**.
  - There are **two bins**: red and blue.
- The participant also keeps a **running mental total** of all numbers. Sorting is the main task.
- An **overhead Intel RealSense depth camera** sees each block land in a bin. The robot that asked for it then glances at that bin, blinks and clears its screen. No tapping is needed; tapping the screen stays as a fallback.
- **Coordinated:** both robots give an instruction at the same moment, every 10 s. **Uncoordinated:** each robot runs on its own irregular schedule and they never give one at the same moment. Both modes have 20 blocks and the same trial length.
- The research question, H1 to H4, NASA-TLX, setup choice, 16 participants and 10-minute sessions stay the same.

## 2. What changed from the last version

| Part | Last version | This version |
|---|---|---|
| What each screen shows | Left: colour only, right: number only (one block split over two robots) | **Each robot shows a full instruction: colour and number** |
| Blocks open at once | One | **Up to two (one per robot), any order** |
| Bins | Three (red, blue, yellow) | **Two (red, blue)** |
| Knowing a block is sorted | Video coded afterwards | **RealSense sees it live; the robot reacts** (tap as fallback) |
| Rhythm | One block every 5 s | Each robot every 10 s, so still one block every 5 s on average |
| Camera | Recording only | Perception that closes the loop, plus optional add-ons (section 8) |

## 3. The setup

```
        [left robot head]      RealSense (overhead,      [right robot head]
        RED 3                  looking down)             BLUE 8
          (on a stand)                                     (on a stand)

                      [ red bin ]         [ blue bin ]

                         [ tray of numbered blocks ]

                                participant
          (optional: 720p webcam between the robots, facing the participant)
```

| Item | Details |
|---|---|
| 2 robot heads | 2 ESP32 boards with colour touch screens on stands at about eye level, each with a simple body and an antenna LED, so they read as robots and not as monitors |
| Depth camera | Intel RealSense **D435** recommended: wide view, and its global-shutter depth sensors cope with moving hands. A D415 or D435i also works (the D435i's IMU is not needed). Mounted about 70 to 80 cm above the table, looking straight down at the tray and the two bins. It sees hands and blocks, not faces. |
| Webcam (optional) | 720p webcam between the robots, facing the participant, for the attention idea in section 8 |
| Blocks | 36 cubes of about 4 cm, numbers 1 to 9, four of each, in a tray, so the choice is never forced |
| Bins | Two shallow bins, red and blue, so blocks stay visible from above |
| Computer | Ubuntu with ROS 2 (Humble or Jazzy), `realsense2_camera`, micro-ROS agent, our scheduler and bin-watcher nodes, rosbag2 |
| Network | Small Wi-Fi router for the ESP32s. Fallback: USB (micro-ROS serial transport) |

## 4. The robots

| State | What the participant sees |
|---|---|
| Idle | Big robot eyes, slow blink, antenna LED blue |
| Look | Eyes move up and look at the participant (0.3 s) |
| Instruction | The screen fills with the colour, a large white number in the middle and small eyes above it, as if the robot is holding a card. Antenna LED red. |
| Done | Eyes glance toward the bin where the block landed, one blink, back to Idle |
| Timeout | After 6 s without the block, the instruction fades and the robot returns to Idle (counted as missed) |
| Greet and goodbye | "Hi, let's work together" at the start, "Thank you!" at the end |

The robots behave exactly like this in both modes. Only the moments when they give instructions change. The Done reaction is the same whether the block went into the right or the wrong bin, so it gives no feedback on correctness.

## 5. The task

- A robot shows, for example, **RED 3**. The participant takes a **3** from the tray and puts it in the **red** bin.
- If both robots have an open instruction (always in the coordinated mode, sometimes in the uncoordinated mode), the participant does them in **either order**.
- Each robot gives 10 instructions per trial, 20 blocks in total, about 2 minutes. Practice: 10 blocks.
- Running total: all 20 numbers, reported at the end of the trial. In both sequences it is 97.

**Two matched sequences** (the same numbers, 10 red and 10 blue, swapped across conditions):

| Sequence | Left robot | Right robot |
|---|---|---|
| A | Red 3, Blue 8, Red 9, Red 4, Blue 9, Red 7, Blue 3, Red 6, Blue 4, Blue 2 | Red 2, Blue 1, Blue 8, Red 5, Red 1, Blue 4, Red 7, Blue 3, Red 6, Blue 5 |
| B | Red 7, Blue 9, Blue 3, Red 8, Blue 6, Red 5, Red 2, Blue 4, Red 5, Blue 7 | Red 4, Blue 3, Red 4, Blue 3, Red 8, Blue 9, Blue 1, Red 2, Blue 6, Red 1 |

## 6. The two modes

| | Coordinated (synchronous) | Uncoordinated (asynchronous) |
|---|---|---|
| How the robots behave | As a team: both give an instruction at the same moment | Independently: each on its own schedule, never at the same moment (at least 1.5 s apart) |
| Timing | Both robots at 0, 10, 20 ... 90 s | Each robot's own gaps vary from 6 to 14 s (average 10 s); the time between any two instructions varies from 1.5 to 8.5 s |
| Which robot comes next | Both together | Mixed: sometimes left, sometimes right, sometimes the same robot twice in a row |
| Blocks and trial length | 20 blocks, last instructions at 90 s | Same 20 blocks, last instruction at 90 s |
| Faces, reactions, 6 s limit, bins, tray, instructions | Same | Same |

**Instruction times in the uncoordinated mode** (seconds, the same for every participant):

| Instruction | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Left robot | 0 | 12 | 18.5 | 25.5 | 35.5 | 49 | 58 | 67 | 75.5 | 85 |
| Right robot | 2 | 10.5 | 23 | 33.5 | 40.5 | 46.5 | 56 | 64.5 | 78.5 | 90 |

Since each robot's gaps are at least 6 s and an instruction closes after at most 6 s, a robot never has two open instructions. That keeps the maximum at two open blocks.

**What the participant experiences:**
- **Coordinated:** two blocks every 10 s, always together, then a calm gap. Easy to plan: "two blocks, do both, wait".
- **Uncoordinated:** the same 20 blocks arrive one at a time, at moments and from sides the participant cannot predict. Sometimes a new one arrives while they are still carrying the last. They have to keep watching both robots.

## 7. Why this is a robotics project and not just HCI

The setup is a small **multi-robot system with a closed sense, think, act loop in ROS 2**:

1. **Sense:** the RealSense depth stream watches the bins (and, optionally, the hands and the participant's attention).
2. **Think:** the bin watcher turns depth changes into "a block landed in the red bin". The scheduler decides which robot's instruction that completes and when each robot speaks next.
3. **Act:** the robot heads change state: they look up, show the instruction, glance at the bin and clear.

On top of that:
- **Embodiment:** two robot coworkers with faces, bodies and names in the shared workspace.
- **Social behaviour:** gaze to the participant, gaze to the bin, blinking.
- **Autonomy:** the experimenter only starts the trial.
- **Shared physical work:** real blocks into real bins.
- **Research question:** how coordination *between two robots* affects a human teammate, which is a multi-robot HRI question.

## 8. Camera ideas

### In the study (core)

| # | Idea | What it does | Why it makes the project robotic | Effort |
|---|---|---|---|---|
| C1 | **Robots that see the sort** (RealSense depth) | Watches the depth inside each bin. When the height rises by about one block and stays while no hand is over the bin, a block has landed. The event goes to the robot whose open instruction has that colour (the oldest first if both match). | Real-time depth perception closing the loop between the physical world and robot behaviour; exact timestamps without tapping | Low to medium (one Python node, numpy on the depth image) |
| C2 | **Perception-driven robot gaze** | When a block lands, the robot's eyes glance toward that bin before clearing. | The robot visibly reacts to what its sensor saw (attention driven by perception) | Low |
| C6 | **Order strategy** (comes free from C1) | With two blocks open, logs which one the participant does first: left or right, older or newer, same bin or other bin | Shows how people schedule work between two robots; an exploratory measure | None |

### Optional add-ons (pick zero to two if time allows)

| # | Idea | What it does | Effort |
|---|---|---|---|
| C3 | **Who are you looking at?** (720p webcam) | Webcam between the robots facing the participant. Head direction from face landmarks (MediaPipe) tells which robot the person is looking at. Counting glances between the robots per minute gives a **monitoring cost**: in the uncoordinated mode people should check both robots more often. The robots can also **return eye contact** when looked at. Privacy: processed live; only the head angle is recorded, not the face video. | Medium |
| C4 | **3D hand tracking** (RealSense colour plus depth) | Hand keypoints with depth give the hand's path in 3D. It measures **hesitations** (the hand stops in mid-air for more than 0.5 s), **re-picks** (a block lifted and put back) and **movement rhythm** (does the participant fall into the robots' rhythm?). Can run offline on the recordings. | Medium |
| C5 | **Tagged blocks** (AprilTags) | A small printed AprilTag on every face of each block. The camera then knows *which number* landed in *which bin*, so sorting accuracy is automatic (no bin check) and each block can be tracked from tray to bin. | Medium (printing, calibration) |

### Follow-up studies (paper extensions, not in the form)

| # | Idea | Question |
|---|---|---|
| E1 | **Robots that adapt their pace** | If the camera sees two open blocks and slow placements, the next instruction waits. Does a workload-aware robot team remove the cost of poor coordination? |
| E2 | **A "wait" gesture** | The participant shows an open palm to the camera and both robots pause. Does giving the human control over robot timing help? |
| E3 | **Robots that point the way** | Before an instruction, the robot's eyes glance at the target bin. Can a gaze cue make unpredictable robots easier to work with? |
| E4 | **Wrong-bin repair** (needs C5) | The camera sees a wrong placement and the robot says "oops, wrong bin". Does a repair message help or hurt trust and workload? |
| E5 | **One bad robot** | Only one robot is badly timed. Does the other robot lose trust too? |

## 9. Screen ideas: keeping the screens robot-like

- **Face first:** the eyes are always visible. Even while showing an instruction, small eyes sit above the card, so it is a robot holding a card, not a display.
- **Gaze:** the robot looks up at the participant before speaking and glances at the bin when it sees the block. With C3 it also returns eye contact.
- **Antenna LED** for robot state (blue idle, red waiting for a block), visible from the side.
- **Touch as a robot sense:** tapping the screen means "done". It is the fallback if C1 fails, and in the pilot it checks C1's accuracy (camera time against tap time).
- **Bodies and names** on the stands; the robots greet and say goodbye.
- **Optional:** one small servo per head so the robot turns toward the participant. This is not needed for the study.

## 10. Research question and hypotheses

**Research question:** Does subjective disturbance show up in objective performance, and if it does not, where does it go?

**Manipulation check:** "The timing of the robots was predictable." and "The two robots felt well coordinated." (7-point scale).

| Hypothesis | Wording |
|---|---|
| H1 Workload | Higher subjective workload in the uncoordinated mode |
| H2 Compensatory behaviour | In the uncoordinated mode, participants respond later and less regularly (longer and more variable response time), miss more blocks, and report more effort |
| H3 Performance | Sorting accuracy stays about the same in both modes; running-sum error increases in the uncoordinated mode |
| H4 Acceptance | Most participants would choose the coordinated robots for a full work shift (binomial test, at least 13 of 16) |

## 11. Measures

**Subjective:** NASA-TLX after each mode, the manipulation check, the setup choice, and two interview questions.

**Objective (all from the ROS 2 recordings):**

| Measure | Definition |
|---|---|
| Sorting accuracy | Instructions completed with the right number in the right bin. Bin contents are checked after each trial, or read automatically with C5. |
| Running-sum error | Absolute difference between the reported and the correct total (97) |
| Response time | For each block, from when the participant could start it until the camera sees it in the bin. "Could start" means its instruction appeared, or the previous block was finished if that was later. Mean and variability per trial. |
| Missed blocks | Instructions cleared after 6 s without their block |
| Hesitations (exploratory) | Hand pauses and re-picks (C4) |
| Order strategy (exploratory) | Which open block is done first (C6) |
| Monitoring glances (optional) | Glances between the robots per minute (C3) |

**Why "could start":** in the coordinated mode the second block of each pair always waits while the first is handled. Measuring from "could start" removes that built-in wait, so both modes are compared fairly.

## 12. Procedure (about 10 minutes)

1. Consent signed beforehand, including consent to the overhead video (hands and blocks only).
2. Briefing and instructions (1 min). The robots greet the participant.
3. Practice with 10 blocks (1 min).
4. Trial 1 with 20 blocks (2 min), in the counterbalanced order.
5. Manipulation check and NASA-TLX (1.5 min). Meanwhile the experimenter empties the bins into the tray and starts the next recording.
6. Trial 2 with the other mode (2 min).
7. Manipulation check and NASA-TLX (1.5 min).
8. Setup choice, interview and debrief (1 min). The robots say goodbye.

Book 15-minute slots. Recruit 18 for 16 complete participants: 4 groups of 4 (order crossed with sequences A and B).

## 13. ROS 2 setup

**The three required topics, recorded in one rosbag per trial:**

| Topic | Published by | Content |
|---|---|---|
| `/robot_left/screen` | Scheduler and bin watcher | JSON in `std_msgs/String`, for example `{"seq": 3, "state": "show", "colour": "RED", "number": 4}` and `{"seq": 3, "state": "done", "bin": "RED"}` |
| `/robot_right/screen` | Scheduler and bin watcher | The same for the right robot |
| `/camera/color/image_raw` | `realsense2_camera` | Overhead colour video, recorded compressed |

Because the bin watcher writes its "done" events into the robot topics, every instruction, every detection and every video frame sits in the same three-topic bag on one clock.

**Nodes:**

| Node | Job |
|---|---|
| `realsense2_camera` | Publishes colour and depth aligned to colour |
| `bin_watcher` (Python) | Reads the depth image inside the two bin areas. When a block-sized rise stays for 0.3 s with no hand above the bin rim, it sends "done" to the matching robot. |
| `scheduler` (Python) | Reads the participant's group and the timing table; sends look, show and timeout to each robot; keeps track of open instructions |
| `micro_ros_agent` | Bridges the two ESP32s (Wi-Fi or USB) |
| ESP32 firmware | Subscribes to its robot topic and draws the face, card and reactions. On a tap it can report "done" (fallback). |
| `ros2 bag record` | One bag per trial |

**Notes:**
- **Calibration:** once per setup, click the corners of each bin in the depth image and save them in a config file. Optional: AprilTags on the table corners to find the bins automatically.
- **Depth recording:** the depth stream is used live. If the course allows more than three topics, also record `/camera/aligned_depth_to_color/image_raw` so that detection can be rerun offline.
- **Optional add-ons** add their own topics: C3 head angle, C4 hand keypoints, C5 tag detections.

## 14. Analysis plan

| | Measure | Test |
|---|---|---|
| Manipulation check | 2 items | Wilcoxon signed-rank, reported first |
| H1 | Raw NASA-TLX total | Paired t-test, effect size dz |
| H2 | Response time (mean and variability), missed blocks, TLX Effort | Paired t-tests; Wilcoxon for missed blocks |
| H3 | Sorting accuracy, running-sum error | Wilcoxon signed-rank |
| H4 | Setup choice | Exact binomial test (13 of 16) |
| Exploratory | Hesitations, order strategy, monitoring glances | Descriptive and paired comparisons |

Tools: pandas, pingouin, scipy, matplotlib, rosbag2 Python reader, and MediaPipe for C3 and C4. With 16 participants a paired t-test detects only large effects (dz about 0.75), so effect sizes are always reported.

## 15. Ethics and data

- The overhead camera records hands, blocks and bins, not faces. The consent form says this, why we record, how long we keep the data and who can see it.
- With C3, face landmarks are processed live and only the head angle is stored.
- Data is stored under participant IDs on university storage and deleted after the project if the course allows.
- Ask the supervisor in week 1 whether the video needs formal ethics approval.

## 16. Pilot checks (week 4)

1. **Detection:** C1 detects at least 95% of blocks within about 0.3 s of the tap time (participants also tap in the pilot), with no false events from hands.
2. **Fair limit:** the 6 s limit is fair in the coordinated mode: two blocks fit comfortably.
3. **Difficulty:** the uncoordinated mode feels harder and causes some missed blocks or sum errors. If not, shorten all gaps and keep the same averages.
4. **Readability:** both screens are readable at a glance from the participant's position.
5. **Time:** a full session fits in 10 minutes.

## 17. Timeline (7 October to 13 December 2026)

| Week | Dates | Work | Milestone |
|---|---|---|---|
| 1 | 5 to 11 Oct | Agree on this version. Mount the RealSense, install ROS 2, `realsense2_camera` and micro-ROS. Buy blocks and bins. Ask about ethics. | Design agreed |
| 2 | 12 to 18 Oct | ESP32 faces, card and reactions over micro-ROS. First bag with both robots and the camera. Bin watcher detects blocks in the two bins. | **M1:** a block dropped in a bin makes the right robot react (18 Oct) |
| 3 | 19 to 25 Oct | Scheduler with both timing tables, 6 s limit, greetings, tap fallback. Full dry run. Consent form, questionnaires, recruiting outside the HRI course. Decide on optional add-ons. | **M2:** a full trial runs and records end to end (25 Oct) |
| 4 | 26 Oct to 1 Nov | Pilot with 2 to 3 lab members (detection against taps, timing, difficulty). Analysis script on the pilot bags. | **M3:** protocol frozen, ethics cleared (1 Nov) |
| 5 to 6 | 2 to 15 Nov | Data collection: 18 participants in 15-minute slots, about 3 afternoons; the rest is buffer. | **M4:** data complete (15 Nov) |
| 7 | 16 to 22 Nov | Analysis: manipulation check, then H1 to H4. | **M5:** results ready (22 Nov) |
| 8 | 23 to 29 Nov | Exploratory measures (order strategy, add-ons), figures, methods and results. | |
| 9 | 30 Nov to 6 Dec | Discussion, full draft, slides, short demo video of both modes. | Draft complete (6 Dec) |
| 10 | 7 to 13 Dec | Final edits, rehearsal, presentation and submission. | **M6:** submitted (by 13 Dec) |

**Work split** (names to be assigned):

- **Robots:** ESP32 faces and reactions, micro-ROS, stands.
- **Perception:** RealSense, bin watcher, calibration, optional add-ons.
- **Study side:** scheduler tables, form, consent, questionnaires, recruiting, pilot, statistics.

## 18. Risks and fallbacks

| Risk | Fallback |
|---|---|
| Hands cause false "block landed" events | Persistence rule (the rise must stay with no hand above the rim); tune in the pilot |
| Depth noise at bin edges | Use only the inner part of each bin and the median depth |
| Bin watcher misses a block | Tap fallback: participants tap the robot's screen when done |
| micro-ROS over Wi-Fi is unstable | USB serial transport |
| Uncoordinated mode not harder in the pilot | Shorter gaps in both modes, same averages |
| Ethics for video takes long | Ask in week 1; the camera sees hands only |

## 19. Open decisions for the team

1. Camera detection with tap fallback (recommended), or tapping only?
2. Which RealSense: D435 (recommended), D435i or D415?
3. Which optional add-ons, if any: C3 attention (recommended if time allows), C4 hand tracking, C5 tagged blocks?
4. Robot names, or "left robot" and "right robot"?
5. Is formal ethics approval needed for the video?
