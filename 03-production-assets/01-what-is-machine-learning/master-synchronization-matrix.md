# ML-01 — Master Synchronization Matrix — v1.0

This is the **single production control plane** for ML-01. The canonical deck defines the 19 production units. Every recording-facing document derives from this matrix.

**Canonical deck:** `03-production-assets/01-what-is-machine-learning/slides/ml-01-what-is-machine-learning.pptx`  
**Recording status:** RECORDING READY — document synchronization complete

| # | Slide / scene | Narration source | Visual | Code / action | Gate |
|---:|---|---|---|---|---|
| 1 | WHAT IF WE DON'T WRITE EVERY RULE? | recording-script §01 | computer-system-illustration.svg | Hook only | READY |
| 2 | WHAT IS MACHINE LEARNING? | §02 | slide-native concept | None | READY |
| 3 | TRADITIONAL PROGRAMMING vs. MACHINE LEARNING | §03 | traditional-vs-ml.svg | None | READY |
| 4 | THE CORE ML MENTAL MODEL | §04 | core-ml-mental-model.svg | None | READY |
| 5 | HUMANS STILL DESIGN THE SYSTEM | §05 | human-designed-system.svg | None | READY |
| 6 | WHAT IS A MODEL? | §06 | code-to-model.svg | None | READY |
| 7 | WHAT DOES “LEARNING” MEAN? | §07 | learning-from-examples.svg | None | READY |
| 8 | TRAINING | §08 | training-vs-inference.svg | None | READY |
| 9 | INFERENCE | §09 | training-vs-inference.svg | None | READY |
| 10 | SUPERVISED LEARNING | §10 | supervised-learning-flow.svg | None | READY |
| 11 | UNSUPERVISED LEARNING | §11 | slide-native visual | None | READY |
| 12 | LET'S SEE THE IDEA IN CODE | §12 | slide 12 + code screen | ml_01_demo.py | READY |
| 13 | OUR EXAMPLE: SPAM FILTER | §13 | spam-email-illustration.svg | Demo context | READY |
| 14 | RULES vs. LEARNED MODEL | §14 | traditional-vs-ml.svg | None | READY |
| 15 | DID THE SYSTEM LEARN? | §15 | demo output | Run/show ml_01_demo.py | READY |
| 16 | CAN IT HANDLE NEW DATA? | §16 | generalization-concept.svg + generalization-reminder.svg | None | READY |
| 17 | MACHINE LEARNING IS NOT MAGIC | §17 | ml-is-not-magic.svg | None | READY |
| 18 | REMEMBER THESE 3 IDEAS | §18 | core-ml-mental-model.svg + generalization-reminder.svg | Recap | READY |
| 19 | NEXT: HOW DOES A MODEL LEARN? | §19 | ml-02-transition.svg | Transition | READY |

## Cross-document contract
- `02-scripts-and-outlines/.../outline.md` defines the teaching beats.
- `02-scripts-and-outlines/.../script.md` defines the approved lecture content.
- `02-scripts-and-outlines/.../visual-plan.md` defines visual execution.
- `02-scripts-and-outlines/.../production-checklist.md` is the operational gate and mirrors this matrix.
- `03-production-assets/.../recording-script.md` is the spoken recording execution map.
- `03-production-assets/.../recording-readiness.md` is the final readiness declaration.
- `03-production-assets/.../recording-readiness-checklist.md` is the pre-session checklist.
- `03-production-assets/.../asset-inventory.md` is the asset registry.

## Canonical asset policy
The old duplicate PPTX filename is removed. `historical-arthur-samuel.svg` is retained as DEFERRED/UNUSED because the historical section is not in the 19-slide deck. No rendered animation files are required.

## Scope gate
No recording-facing artifact may introduce derivatives, gradients, loss functions, gradient descent, optimization mechanics, regression mathematics, logistic regression, detailed overfitting mechanisms, or parameter-update equations.