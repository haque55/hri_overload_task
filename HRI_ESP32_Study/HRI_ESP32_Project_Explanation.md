# HRI Project: Two Robot Heads (ESP32), Camera and ROS 2

Team: Enrique Feria Abascal, Samin Haque, Sinan Onder. Updated 7 October 2026.

This folder holds the whole project in three files:
- `HRI_Study_Design_ESP32_RobotHeads.docx`: the course study design form.
- This explanation file.
- `HRI_ESP32_Two_Modes.png`: the image below.

![Setup and the two modes](HRI_ESP32_Two_Modes.png)

## 1. Summary

- The Kinova arms are no longer available. We keep the **same study**:
  - Two agents present a colour and a number with coordinated (synchronous) or uncoordinated (asynchronous) timing.
  - The participant sorts numbered blocks into coloured bins and keeps a running sum.
  - We measure cognitive load and where the disturbance goes.
- The two arms are replaced by **two robot heads**: each is an ESP32 screen with an animated robot face, on a small stand to the left and right of the participant.
- A **camera** records every session. **ROS 2** runs three topics (left robot, right robot, camera), and every trial is saved as one **rosbag**.
- To make it clearly **Human-Robot Interaction and not just Human-Computer Interaction**, five HRI layers are built in (section 7). They are the same in both modes, so they add no conditions.
- The research question, hypotheses H1 to H4, NASA-TLX, setup choice, 16 participants and 10-minute sessions stay the same.

## 2. What changed from the Kinova version, and what stayed

| Part | Kinova version | Robot heads version |
|---|---|---|
| Agents | Two Kinova Gen3 arms holding ESP32 touch screens | Two robot heads: ESP32 screens with animated faces on stands |
| How an instruction arrives | Arm moves the screen toward the participant; participant touches it | Robot looks up at the participant, shows its half for 2 s, then returns to its idle face |
| Blocks | Digital blocks, sorted with three buttons | Physical numbered blocks, sorted into three physical coloured bins |
| Pickup latency | Time from screen stop to touch | **Response time**: from the full instruction being shown to the block landing in the bin, from the camera |
| Missed pickups | Screen left without a touch | **Missed blocks**: instructions with no block placed |
| Recording | Robot and screen logs | ROS 2 rosbag with both robot topics and the camera on one clock |
| Coordinated mode | Both arms together every 5 s | Both robots together every 5 s (unchanged) |
| Uncoordinated mode | Arms on their own irregular schedules | Robots on the same irregular schedules (same arrival table) |
| RQ, H1, H3, H4, TLX, setup choice, N = 16, 10 min | | Unchanged |

## 3. The setup

```
                [left robot head]                 [right robot head]
                 shows the COLOUR                   shows the NUMBER
                   (on a stand)                       (on a stand)

                         [red bin]  [blue bin]  [yellow bin]

                              [tray of numbered blocks]

                                   participant
                                        |
                  camera on a tripod behind and above the participant,
                  looking at the table: sees both robots, the tray, the bins and the hands
```

| Item | Details |
|---|---|
| 2 robot heads | 2 ESP32 boards with colour screens (touch not needed). Each sits on a small stand at about eye level, cardboard or 3D printed, with a simple body so it reads as a robot and not as a monitor. |
| Camera | USB webcam, 720p at 30 frames per second, on a tripod behind and above the participant. It records hands, blocks, bins and both robot screens, **not the face**. |
| Blocks | 27 cubes, numbers 1 to 9, three of each, in a tray. There are more than needed, so the last choices are never forced. |
| Bins | Three bins: red, blue, yellow |
| Computer | Laptop or lab PC with Ubuntu and ROS 2 (Humble or Jazzy): micro-ROS agent, camera driver, scheduler, rosbag recorder |
| Network | Small Wi-Fi router for the two ESP32 boards. Fallback: USB cables (micro-ROS serial transport) |

## 4. The robots

| State | What the participant sees |
|---|---|
| Idle | Robot eyes looking slightly down, blinking slowly |
| Look | Eyes move up and look at the participant (0.3 s) |
| Show | Full-screen colour (left robot) or a large white number (right robot), 2 s |
| Greet or goodbye | Short text such as "Hi, let's work together" or "Thank you!" at the start and end of the session |

**One presentation:** Look (0.3 s), then Show (2 s), then back to Idle. The robots behave exactly like this in both modes; only the moments when they present change.

## 5. The task

- The left robot shows a colour and the right robot a number. Together they are one block instruction, for example **red** and **4**.
- The participant takes a **4** from the tray and puts it in the **red** bin.
- They also keep a **running mental total** of all numbers and report it at the end of the trial.
- **Sorting is described as the main task.**
- 20 instructions per trial (about 2 minutes); 10 in the practice.
- Two matched sequences, swapped across conditions. Each has 7 red, 7 blue and 6 yellow, the same 20 numbers, and a total of 97.
  - **Sequence A:** Red 2, Red 1, Yellow 6, Blue 2, Blue 3, Red 9, Red 4, Blue 3, Yellow 6, Blue 4, Yellow 5, Yellow 8, Red 5, Blue 4, Yellow 9, Red 1, Blue 3, Yellow 7, Blue 8, Red 7
  - **Sequence B:** Blue 9, Yellow 3, Yellow 2, Blue 3, Blue 9, Yellow 1, Red 6, Yellow 4, Blue 5, Red 4, Red 2, Yellow 8, Red 6, Yellow 7, Red 3, Blue 4, Red 8, Red 5, Blue 1, Blue 7

## 6. The two modes

| | Coordinated (synchronous) | Uncoordinated (asynchronous) |
|---|---|---|
| How the robots behave | As a team: both present at the same moment | Independently, each on its own schedule, never at the same moment |
| Timing | Every 5 s | Colour and number of a block arrive 1 to 3 s apart; each robot's own gaps vary from 4 to 7 s |
| Which half comes first | Both together | Colour first in 10 blocks, number first in 10, mixed unpredictably (never more than 3 in a row the same way) |
| Trial length | 20 blocks, last at 95 s | Same 20 blocks, last at 95 s |
| Faces, display time, positions, blocks, bins, instructions | Same | Same |

**Arrival times in the uncoordinated mode** (seconds from trial start, the same for every participant). In the coordinated mode both robots present at 0, 5, 10, and so on up to 95.

| Block | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Left (colour) | 1 | 5 | 9.5 | 14 | 21 | 26 | 31 | 35 | 39 | 43.5 |
| Right (number) | 0 | 6 | 11 | 15.5 | 19.5 | 25 | 29.5 | 36 | 40.5 | 45.5 |

| Block | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
|---|---|---|---|---|---|---|---|---|---|---|
| Left (colour) | 50.5 | 54.5 | 61 | 65.5 | 69.5 | 73.5 | 78 | 85 | 91 | 95 |
| Right (number) | 49.5 | 56 | 60 | 64 | 71 | 76 | 80 | 84 | 88 | 93.5 |

In the uncoordinated mode the participant often has to hold the first half in memory until the second half arrives, and cannot predict which robot comes next or when. That is the cost of two robots that do not coordinate with each other.

## 7. Why this is HRI and not HCI

Two screens on a table would be a computer interface. These five layers make them robots, and they are the same in both modes:

1. **Embodiment and persona.** Two named robot coworkers with faces and bodies on stands in the shared workspace. They greet the participant and say goodbye.
2. **Social behaviour.** Before every instruction a robot looks up at the participant, and it blinks while idle. This gives the robots attention and turn-taking that a display does not have.
3. **Autonomy.** The robots act on their own as ROS 2 nodes; the experimenter only starts the trial.
4. **Perception.** The camera is the robots' eyes on a ROS 2 topic. Response times and missed blocks come from what it saw.
5. **Shared physical work.** The robots direct real work with real blocks and bins. The study is about **robot-robot coordination** (do the two robots act as a team?) and its effect on the human, which is a multi-robot HRI question.

**Exploratory camera measure, movement rhythm (entrainment):** we track the participant's hand offline with MediaPipe. We measure how regular their actions are and how closely they follow the robots' rhythm. If people fall into step with coordinated robots and lose that rhythm with uncoordinated ones, this shows *where the disturbance goes* in an objective way.

## 8. Research question and hypotheses

**Research question:** Does subjective disturbance show up in objective performance, and if it does not, where does it go?

**Manipulation check:** "The timing of the robots was predictable." and "The two robots felt well coordinated." (7-point scale).

| Hypothesis | Wording |
|---|---|
| H1 Workload | Participants report higher subjective workload in the uncoordinated mode. |
| H2 Compensatory behaviour | In the uncoordinated mode, participants respond later and less regularly (longer and more variable response time), miss more blocks, and report more effort. |
| H3 Performance | Sorting accuracy stays about the same in both modes; running-sum error increases in the uncoordinated mode. |
| H4 Acceptance | Most participants would choose the coordinated robots for a full work shift (binomial test, at least 13 of 16). |

## 9. Measures

**Subjective:** NASA-TLX after each mode, the manipulation check, the setup choice and two interview questions.

**Objective:**

| Measure | How it is measured |
|---|---|
| Sorting accuracy | After each trial the experimenter checks the bin contents against the sequence; the video confirms each placement. |
| Running-sum error | Absolute difference between the reported and the correct total |
| Response time | From the moment both halves of a block have been shown until the block lands in the bin, from the video. Mean and variability per trial. |
| Missed blocks | Instructions for which no block was placed |
| Movement rhythm (exploratory) | Hand tracking on the video: regularity of placements and how closely they follow the robots' rhythm |

Response time starts when the instruction is complete, so waiting for the second half in the uncoordinated mode does not count as slowness.

## 10. Procedure (about 10 minutes)

1. Consent signed before the session, **including consent to video recording**.
2. Briefing and instructions (1 min). The robots greet the participant.
3. Practice with 10 instructions (1 min).
4. Trial 1 with 20 instructions (2 min), coordinated or uncoordinated depending on the counterbalanced order.
5. Manipulation check and NASA-TLX (1.5 min). Meanwhile the experimenter puts the blocks back and starts the next recording.
6. Trial 2, the other mode (2 min).
7. Manipulation check and NASA-TLX (1.5 min).
8. Setup choice, interview and debrief (1 min). The robots say goodbye.

Book 15-minute slots. Recruit 18 for 16 complete participants. Crossing the order with sequences A and B gives 4 groups of 4.

## 11. ROS 2 setup (three topics, one rosbag per trial)

| Topic | Published by | Content |
|---|---|---|
| `/robot_left/screen` | Scheduler node | Commands for the left robot: sequence number, state (idle, look, show, greet, bye), content (the colour) |
| `/robot_right/screen` | Scheduler node | Same for the right robot (content is the number) |
| `/camera/image_raw` | `usb_cam` or `v4l2_camera` node | Video of the table, recorded compressed (about 0.5 GB per trial) |

- **ESP32 boards:** run micro-ROS, subscribe to their screen topic over Wi-Fi through the micro-ROS agent on the computer, and draw the face or the content.
- **Scheduler node (Python, rclpy):** reads the participant's group and the arrival table. It sends "look" 0.3 s before each arrival, "show" at the arrival and "idle" 2 s later, plus the greeting and goodbye.
- **Messages:** `std_msgs/String` carrying a small JSON text, for example `{"seq": 7, "state": "show", "content": "RED"}`. No custom message build is needed on the ESP32.
- **Recording:** `ros2 bag record` with all three topics, one bag per trial, so every instruction and every video frame share one clock.
- **Analysis script (Python):**
  1. Reads each bag into a table of instruction times.
  2. Extracts the video frames.
  3. Finds when each block lands in a bin, using MediaPipe hand tracking plus a zone over each bin, with a manual check on a few trials.
  4. Computes all objective measures.

## 12. Analysis plan

| | Measure | Test |
|---|---|---|
| Manipulation check | 2 items | Wilcoxon signed-rank, reported first |
| H1 | Raw NASA-TLX total | Paired t-test, effect size dz |
| H2 | Response time (mean and variability), missed blocks, TLX Effort | Paired t-tests; Wilcoxon for missed blocks |
| H3 | Sorting accuracy, running-sum error | Wilcoxon signed-rank |
| H4 | Setup choice | Exact binomial test (13 of 16) |
| Exploratory | Movement rhythm and its link to TLX | Paired comparison; correlation |

Tools: pandas, pingouin, scipy, matplotlib, rosbag2 Python reader, MediaPipe. With 16 participants a paired t-test detects only large effects (dz about 0.75), so effect sizes are always reported.

## 13. Ethics and data

- Video is personal data. The consent form names the camera and what it records (hands and table, no face). It also says why we record, how long the video is stored, and who can see it.
- Data is stored under participant IDs only, on university storage, and deleted after the project if the course allows.
- Ask the supervisor in week 1 whether video recording needs formal ethics approval.

## 14. Paper extensions (follow-up studies with the same setup)

These are not part of the course form. Each one is a possible next study or paper:

1. **Robots that warn you (recommended first).** A clear "look up and glow" cue 1 s before each instruction. Compare async with async plus the cue: can announcing the timing make unpredictable robots predictable again?
2. **The robot that sees you.** Robots wait until the camera sees the block placed. Compare them with robots that replay the same gaps but ignore the person: is it responsiveness, not speed, that lowers workload?
3. **One bad robot.** Only one robot is badly timed. Does the other robot lose trust too (spillover)?
4. **Robot or display.** The same screens framed as robots or as plain displays. Does the social framing change how people tolerate bad timing?
5. **Robots that say sorry.** After rushing, a robot apologises and gives more time. Does that repair trust?

The movement rhythm measure from section 7 can be added to all of them.

## 15. Pilot checks (week 4)

1. Both screens are clearly readable from the participant's position, and the 2 s display feels fair in the coordinated mode.
2. The uncoordinated mode feels harder and produces some missed blocks or sum errors. If not, shorten the gaps in both modes and keep the same averages.
3. The camera sees both robot screens, the tray, the bins and the hands. Real screen onsets in the video match the bag times.
4. Hand tracking finds the placements, or manual coding is quick enough.
5. A full session fits in 10 minutes.

## 16. Timeline (7 October to 13 December 2026)

| Week | Dates | Work | Milestone |
|---|---|---|---|
| 1 | 5 to 11 Oct | Agree on the plan. Update the form. Confirm the ESP32 board model. Buy webcam, blocks and bins. Install ROS 2 and micro-ROS. Ask about ethics, including video. | Plan agreed |
| 2 | 12 to 18 Oct | micro-ROS on both ESP32s; faces and screen states; camera node; first rosbag with all three topics; stands built. | **M1:** both robots driven from ROS 2 and recorded with the camera in one bag (18 Oct) |
| 3 | 19 to 25 Oct | Scheduler node with the arrival table and greetings; full dry run; bag-to-table script. Consent form with video, instructions, questionnaires. Start recruiting outside the HRI course. | **M2:** a full trial runs and records end to end (25 Oct) |
| 4 | 26 Oct to 1 Nov | Pilot with 2 to 3 lab members. Tune timing and display time. Build the analysis pipeline (response times, hand tracking). | **M3:** protocol frozen, ethics cleared (1 Nov) |
| 5 to 6 | 2 to 15 Nov | Data collection: 18 participants in 15-minute slots, about 3 afternoons; the rest is buffer. | **M4:** data complete (15 Nov) |
| 7 | 16 to 22 Nov | Extract and check response times; run the analysis (manipulation check first, then H1 to H4). | **M5:** results ready (22 Nov) |
| 8 | 23 to 29 Nov | Movement rhythm analysis, figures, methods and results. | |
| 9 | 30 Nov to 6 Dec | Discussion, full report draft, presentation slides, short demo video of both modes. | Draft complete (6 Dec) |
| 10 | 7 to 13 Dec | Final edits, rehearsal, presentation and submission. | **M6:** submitted (by 13 Dec) |

**Work split** (names to be assigned):

- **Robots:** ESP32 faces, micro-ROS, stands.
- **ROS 2 and camera:** scheduler, camera node, rosbag, analysis pipeline.
- **Study side:** form, consent, questionnaires, recruiting, pilot, statistics.

**Critical path:** ethics approval (video) and M2. If ethics is not cleared by 1 November, data collection moves to 16 to 29 November and weeks 7 and 8 merge.

## 17. Risks and fallbacks

| Risk | Fallback |
|---|---|
| micro-ROS over Wi-Fi is unstable | Connect the ESP32s by USB (micro-ROS serial transport) |
| Screen delay makes onsets inaccurate | The camera sees both screens, so real onsets are read from the video |
| Hand tracking misses placements | Manual video coding for those trials (2 minutes of video per trial) |
| Bags too large | Compressed images at 720p; delete raw copies after extraction |
| Async mode not harder in the pilot | Shorter gaps in both modes, same averages |
| Ethics for video takes long | Ask in week 1; record only hands and table |

## 18. Open decisions for the team

1. Which ESP32 boards do we have (model and screen size)? The plan works with any colour screen.
2. Standing or seated participant? The form says standing, as before.
3. Robot names, or just "left robot" and "right robot"?
4. Response times from automatic hand tracking with a manual check (planned), or fully manual video coding?
5. Is formal ethics approval needed for the video?
