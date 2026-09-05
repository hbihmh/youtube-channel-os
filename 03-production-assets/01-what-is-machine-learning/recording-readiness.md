# ML-01 — Recording Readiness Package

**Lecture ID:** ML-01  
**Title:** What Is Machine Learning?  
**Season:** Season 01  
**Module:** Foundations  
**Phase:** 4I-8 — Recording Readiness  
**Purpose:** Final production-readiness package before recording begins.

---

## 1. Recording Readiness Objective

ML-01 is ready to enter recording only when the script, visuals, code demonstration, recording plan, technical setup, and quality gates are all verified.

This phase prepares the recording session. It does **not** create or publish recording footage.

### Recording principle

> Record exactly what has been approved. Do not introduce new concepts, examples, terminology, or claims during recording that are outside the approved ML-01 scope.

---

## 2. Source-of-Truth Documents

Use these documents as the production references:

| Document | Purpose |
|---|---|
| `02-scripts-and-outlines/module-01-foundations/ML-01-what-is-machine-learning/script.md` | Narration/script source |
| `02-scripts-and-outlines/module-01-foundations/ML-01-what-is-machine-learning/visual-plan.md` | Visual sequencing and intent |
| `02-scripts-and-outlines/module-01-foundations/ML-01-what-is-machine-learning/production-checklist.md` | Script-to-visual synchronization |
| `01-research-and-verification/module-01-foundations/ML-01-what-is-machine-learning/claims.md` | Claim verification source |
| `03-production-assets/01-what-is-machine-learning/asset-inventory.md` | Live production asset inventory |
| `03-production-assets/01-what-is-machine-learning/slides/slide-deck-outline.md` | 19-scene slide mapping |
| `04-codebase/01-what-is-machine-learning/README.md` | Code package usage/reference |

---

## 3. Final Teaching Scope

### Must be taught

- What machine learning is at a high level
- Traditional programming vs. learning from examples
- The role of data/experience
- Learning procedure
- Model
- Training
- Inference
- Supervised learning
- Unsupervised learning
- Generalization
- Common misconceptions
- One complete spam-classification example
- Brief historical context: Arthur Samuel and early machine learning
- The core ML mental model

### Must not be taught in ML-01

- Derivatives
- Gradients
- Loss functions
- Gradient descent
- Optimization mathematics
- Optimization landscapes
- Linear regression mathematics
- Logistic regression
- Detailed overfitting mechanisms
- Detailed bias/variance analysis
- Python implementation as a teaching topic

If a later concept is mentioned for continuity, keep it strictly as a **preview/deferred topic**, not an explanation.

---

## 4. Recording Structure

Record in the approved lecture order. Avoid unnecessary retakes across unrelated sections.

| Scene | Teaching purpose | Primary recording support |
|---:|---|---|
| 01 | Opening hook | Opening visual / simple system framing |
| 02 | Traditional programming | `traditional-vs-ml.svg` + supporting visual |
| 03 | Why explicit rules become difficult | `rules-become-difficult.svg` |
| 04 | Core ML idea | `core-ml-mental-model.svg` |
| 05 | Humans still design the system | `human-designed-system.svg` |
| 06 | Model concept | Core model visual / slides |
| 07 | Meaning of learning | `learning-from-examples.svg` |
| 08 | Training | `training-vs-inference.svg` |
| 09 | Inference | `training-vs-inference.svg` |
| 10 | Supervised learning | `supervised-learning-flow.svg` |
| 11 | Unsupervised learning | Slide/diagram support |
| 12 | Generalization | `generalization-concept.svg` + `generalization-reminder.svg` |
| 13 | Misconceptions | `ml-is-not-magic.svg` / slide sequence |
| 14 | Complete mental model | `core-ml-mental-model.svg` |
| 15 | End-to-end spam example | `spam-classifier-example.svg` + `spam-email-illustration.svg` |
| 16 | Historical context | `historical-arthur-samuel.svg` |
| 17 | Final recap | Summary slide |
| 18 | Final takeaway | `traditional-vs-ml.svg` |
| 19 | Bridge to ML-02 / outro | `ml-02-transition.svg` + outro slide |

---

## 5. Recording Modes

### A. Presenter / narration

- Follow the final approved script.
- Speak naturally rather than reading mechanically.
- Preserve technical terminology exactly where precision matters.
- Pause after definitions and major mental models.
- Do not improvise additional technical explanations.

### B. Slide / visual capture

- Keep the active visual synchronized with the narration.
- Do not display a visual before its concept is introduced unless it is intentionally used as a hook.
- Prefer one clear teaching visual at a time.
- Avoid overcrowding the frame.

### C. Code demonstration

The ML-01 code demonstration is intentionally simple. It illustrates the difference between explicit rules and a learned threshold-style toy model.

Do not turn the demonstration into a lesson about optimization, gradients, loss functions, or production ML systems.

### D. Transitions

Use short pauses between major sections. Give the viewer enough time to read diagrams without making the lecture feel slow.

---

## 6. Speaker Notes — High-Risk Delivery Points

Before recording, rehearse these terms aloud:

- machine learning
- learning procedure
- computational representation
- model
- training
- inference
- supervised learning
- unsupervised learning
- target output
- generalization
- Arthur Samuel

### Definitions requiring deliberate delivery

**Machine learning:** emphasize that the system uses experience to improve performance on a task.

**Model:** emphasize that it is a computational representation used to produce outputs from inputs.

**Training:** emphasize obtaining or adjusting the model using available experience/data.

**Inference:** emphasize using the trained model on new input.

**Generalization:** emphasize performance on new/unseen data rather than simply the training examples.

---

## 7. Recording Continuity Rules

1. Use the same terminology throughout the lecture.
2. Keep the traditional-programming comparison consistent:
   `Input + Explicit Rules → Output`.
3. Keep the ML comparison consistent:
   `Examples / Experience → Learning Procedure → Model → New Input → Prediction`.
4. Keep training and inference clearly separated.
5. Do not switch between competing definitions of “model.”
6. Use “target output” consistently for supervised learning.
7. Keep the historical section brief.
8. Do not expand the five misconception section into unrelated AI commentary.
9. Keep the spam example consistent with the slides and code.
10. End with the approved bridge to ML-02.

---

## 8. Technical Recording Setup

Verify before the session:

- [ ] Recording resolution selected and tested.
- [ ] Screen capture source tested.
- [ ] Microphone selected and tested.
- [ ] Headphone/monitoring checked.
- [ ] Input levels checked.
- [ ] Camera framing checked if camera is used.
- [ ] Lighting checked if camera is used.
- [ ] Desktop notifications disabled.
- [ ] Unnecessary applications closed.
- [ ] Browser tabs unrelated to recording closed.
- [ ] Presentation opens correctly.
- [ ] Required SVG/visual assets open correctly.
- [ ] Python environment is ready for the demo.
- [ ] Notebook/script launches without errors.
- [ ] Recording storage has sufficient free space.
- [ ] Test recording completed and playback checked.

**Note:** Exact resolution, frame rate, audio format, and encoder settings should be fixed by the channel's recording standard before the first session. Do not invent settings ad hoc during recording.

---

## 9. File and Session Organization

Recommended session structure:

```text
ML-01-recording/
├── raw/
├── screen-capture/
├── audio/
├── retakes/
├── notes/
└── selects/
```

Suggested recording naming convention:

```text
ML-01_S01_hook_take01
ML-01_S02_traditional-programming_take01
ML-01_S03_rules-difficult_take01
...
ML-01_S19_bridge-outro_take01
```

Keep the original raw recordings. Do not overwrite failed or superseded takes.

---

## 10. Retake Policy

Retake a scene when:

- a technical term is mispronounced or materially misstated;
- the definition becomes ambiguous;
- a sentence changes the approved meaning;
- the wrong visual is displayed;
- the visual and narration become desynchronized;
- audio contains an obvious technical defect;
- an external interruption affects the take;
- an unsupported claim is introduced.

Do not retake solely because of a minor natural pause unless it harms clarity or editing continuity.

---

## 11. Final Recording Gate

Recording may begin only when all items below are checked:

- [ ] Phase 4I-7 is closed.
- [ ] Production asset inventory reflects the live repository.
- [ ] Final script is available locally for recording.
- [ ] Script-to-visual mapping has been reviewed.
- [ ] Critical visuals are available.
- [ ] Slide deck opens correctly.
- [ ] Code demo has been tested.
- [ ] Scope boundary has been reviewed.
- [ ] Technical recording setup has passed a test recording.
- [ ] Speaker has rehearsed difficult terminology.
- [ ] Recording order is understood.
- [ ] Storage and file naming are ready.
- [ ] No unresolved blocker remains.

**Gate status:** `READY TO RECORD` only after every applicable checkbox is verified.

---

## 12. Scope Guard During Recording

If an idea comes up naturally during narration that belongs to a later lecture, do not expand it spontaneously.

Use a short bridge such as:

> “We will unpack that mechanism later.”

Then return to the approved ML-01 explanation.

The goal of ML-01 is a strong mental model, not maximum technical depth.

---

## 13. Post-Session Handoff

After recording:

1. Preserve all raw takes.
2. Identify technically usable takes.
3. Record any required retakes.
4. Log continuity issues and unresolved narration problems.
5. Hand selected footage/audio to the editing stage.
6. Do not silently rewrite technical claims during editing.
7. Any substantive factual change returns to the appropriate verification workflow.

**Phase boundary:** This document ends at recording readiness. Editing, final fact check, GitHub release, YouTube publishing, and post-publish review belong to later SOP stages.
