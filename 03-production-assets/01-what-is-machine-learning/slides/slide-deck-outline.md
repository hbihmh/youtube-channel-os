# ML-01 — Slide Deck Outline — v1.0

**Canonical file:** `ml-01-what-is-machine-learning.pptx`  
**Slide count:** 19  
**Status:** CANONICAL / RECORDING CONTROL

| # | Exact slide title | Core teaching purpose |
|---:|---|---|
| 1 | WHAT IF WE DON'T WRITE EVERY RULE? | Hook with spam-filter problem. |
| 2 | WHAT IS MACHINE LEARNING? | State the high-level definition and central idea. |
| 3 | TRADITIONAL PROGRAMMING vs. MACHINE LEARNING | Contrast explicit rules with learning from examples. |
| 4 | THE CORE ML MENTAL MODEL | Examples → learning → model → new input → prediction. |
| 5 | HUMANS STILL DESIGN THE SYSTEM | Clarify the continuing human engineering role. |
| 6 | WHAT IS A MODEL? | Define model as computational representation for inputs/outputs. |
| 7 | WHAT DOES "LEARNING" MEAN? | Define computational learning without anthropomorphism. |
| 8 | TRAINING | Explain obtaining/adjusting the model from experience. |
| 9 | INFERENCE | Explain using the trained model on new input. |
| 10 | SUPERVISED LEARNING | Introduce examples with target outputs. |
| 11 | UNSUPERVISED LEARNING | Introduce data without provided target outputs. |
| 12 | LET'S SEE THE IDEA IN CODE | Connect concepts to the intentionally small demo. |
| 13 | OUR EXAMPLE: SPAM FILTER | Establish the toy labeled-email example. |
| 14 | RULES vs. LEARNED MODEL | Compare hard-coded behavior with behavior learned from examples. |
| 15 | DID THE SYSTEM LEARN? | Show demo behavior and make the distinction concrete. |
| 16 | CAN IT HANDLE NEW DATA? | Introduce generalization. |
| 17 | MACHINE LEARNING IS NOT MAGIC | Ground expectations and state practical limitations. |
| 18 | REMEMBER THESE 3 IDEAS | Consolidate the three core takeaways. |
| 19 | NEXT: HOW DOES A MODEL LEARN? | Bridge directly to ML-02. |

## Canonical design decisions
- This 19-slide sequence supersedes the former deck structure.
- No historical Arthur Samuel section is included in the canonical recording.
- No mathematical teaching is included.
- The deck is intentionally simple: conceptual understanding first, mechanics later.

## Hard exclusions
Derivatives, gradients, loss functions, gradient descent, optimization mechanics, regression mathematics, logistic regression, detailed overfitting mechanisms, and parameter-update equations are outside ML-01.