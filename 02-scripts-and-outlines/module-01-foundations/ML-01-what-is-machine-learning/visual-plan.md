# ML-01 — Visual Plan — v1.0

**Canonical deck:** `slides/ml-01-what-is-machine-learning.pptx`  
**Rule:** visual plan follows the 19-slide deck exactly.

| # | Slide | Primary visual | Supporting asset / action |
|---:|---|---|---|
| 1 | WHAT IF WE DON'T WRITE EVERY RULE? | Opening hook | `visual-assets/computer-system-illustration.svg` |
| 2 | WHAT IS MACHINE LEARNING? | Concept statement | Slide-native examples → learning → model |
| 3 | TRADITIONAL PROGRAMMING vs. MACHINE LEARNING | Paradigm comparison | `diagrams/traditional-vs-ml.svg` |
| 4 | THE CORE ML MENTAL MODEL | Hero flow | `diagrams/core-ml-mental-model.svg` |
| 5 | HUMANS STILL DESIGN THE SYSTEM | Human/system relationship | `visual-assets/human-designed-system.svg` |
| 6 | WHAT IS A MODEL? | Input → model → output | `visual-assets/code-to-model.svg` |
| 7 | WHAT DOES “LEARNING” MEAN? | Experience → learning → behavior | `visual-assets/learning-from-examples.svg` |
| 8 | TRAINING | Training flow | `diagrams/training-vs-inference.svg` |
| 9 | INFERENCE | Inference flow | `diagrams/training-vs-inference.svg` |
| 10 | SUPERVISED LEARNING | Labeled examples | `diagrams/supervised-learning-flow.svg` |
| 11 | UNSUPERVISED LEARNING | Unlabeled data → structure | Slide-native visual only |
| 12 | LET'S SEE THE IDEA IN CODE | Concept → code → behavior | `04-codebase/01-what-is-machine-learning/ml_01_demo.py` |
| 13 | OUR EXAMPLE: SPAM FILTER | Concrete example | `visual-assets/spam-email-illustration.svg` |
| 14 | RULES vs. LEARNED MODEL | Direct comparison | `diagrams/traditional-vs-ml.svg` |
| 15 | DID THE SYSTEM LEARN? | Demo behavior/output | Screen-recorded `ml_01_demo.py` output |
| 16 | CAN IT HANDLE NEW DATA? | Generalization | `diagrams/generalization-concept.svg`; `visual-assets/generalization-reminder.svg` |
| 17 | MACHINE LEARNING IS NOT MAGIC | Limitations / grounding | `visual-assets/ml-is-not-magic.svg` |
| 18 | REMEMBER THESE 3 IDEAS | Final mental model | `diagrams/core-ml-mental-model.svg`; `visual-assets/generalization-reminder.svg` |
| 19 | NEXT: HOW DOES A MODEL LEARN? | Transition | `visual-assets/ml-02-transition.svg` |

## Visual rules
1. Do not introduce a visual concept before narration explains it.
2. Use progressive emphasis, not decorative animation.
3. Slides 4, 8–10, and 16 are explanation-critical; pause long enough to read them.
4. The code screen is only used in slides 12 and 15.
5. No visual may introduce derivatives, gradients, loss functions, gradient descent, optimization mechanics, regression mathematics, logistic regression, detailed overfitting, or parameter-update equations.

## Asset status
**Active:** all assets mapped in the table except the historical Arthur Samuel visual.  
**Deferred/unused:** `visual-assets/historical-arthur-samuel.svg` is retained for possible future use but is not part of the canonical 19-slide ML-01 recording.  
**Animations:** no rendered animation files are required for the canonical deck; editor motion is specified by the recording script.