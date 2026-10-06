# hri_overload_task
HRI project for uni with a Kinova Gen3 arm setup.

Current design (6 Oct 2026): one Kinova Gen3 arm shows colour-number items on an ESP32 screen; participants enter them on a tablet. Coordinated vs uncoordinated robot timing.

- `docs/HRI_Study_Design_ESP32.docx`: study design form (course layout)
- `docs/HRI_ESP32_Plan.md`: explanation, setup, analysis, software plan and timeline
- `tools/make_schedules.py`: generates item lists, timing and participant groups into `schedules/`
- `tools/build_form_esp32.py`: rebuilds the form from `docs/source/`
