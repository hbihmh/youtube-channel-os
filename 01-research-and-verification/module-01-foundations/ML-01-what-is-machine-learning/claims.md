# ML-01 — Claim Verification Ledger

## Purpose

This document contains every technically meaningful claim that may appear
in ML-01:

> What Is Machine Learning?

No major technical claim should enter the final script without passing
verification.

This ledger distinguishes between:

* technical claims that require factual verification,
* historical claims,
* definitions,
* comparisons,
* pedagogical framing,
* and statements that should not be used because they create misleading
  mental models.

---

# Verification Status Definitions

| Status           | Meaning                                                                          |
| ---------------- | -------------------------------------------------------------------------------- |
| UNVERIFIED       | Claim has been identified but evidence has not yet been checked                  |
| VERIFIED         | Evidence supports the claim and the wording is sufficiently precise              |
| NEEDS CORRECTION | Underlying idea is valid, but the wording is imprecise or potentially misleading |
| FALSE            | Available evidence contradicts the claim                                         |
| DEFERRED         | Claim is valid but intentionally postponed to a later lecture                    |

---

# Claim Ledger

## ML01-C01

**Type:** Definition

**Claim:**

A computer program is said to learn when its performance on a task, measured
by an appropriate performance measure, improves through experience.

**Importance:** CRITICAL

**Intended Lecture Section:** Formal Concept

**Candidate Sources:**

* S02 — Mitchell (1997)
* S01 — Samuel (1959)

**Status:** VERIFIED

**Verification Notes:**

The wording has been revised from the original claim.

Mitchell's formulation explicitly defines learning in terms of:

* a task or class of tasks,
* a performance measure,
* and experience.

The revised wording avoids treating "data" as a direct substitute for
Mitchell's more precise concept of experience.

This should be the primary formal definition introduced in ML-01.

---

## ML01-C02

**Type:** Definition

**Claim:**

A machine-learning system uses experience, often represented through data,
to improve its performance on a defined task according to a learning
procedure.

**Importance:** CRITICAL

**Intended Lecture Section:** Formal Concept

**Candidate Sources:**

* S02 — Mitchell (1997)
* S03 — Bishop (2006)
* S04 — Hastie, Tibshirani & Friedman (2009)

**Status:** VERIFIED

**Verification Notes:**

The original phrase "learn patterns that can be used to make predictions or
decisions" was useful intuition but too vague as a formal definition.

The revised wording emphasizes:

* experience,
* a task,
* performance,
* and a learning procedure.

"Patterns" may still be used later as an intuitive explanation, but it should
not replace the formal definition.

---

## ML01-C03

**Type:** Comparison

**Claim:**

In traditional rule-based programming, the programmer explicitly specifies
the rules or procedures that transform inputs into outputs.

**Importance:** HIGH

**Intended Lecture Section:** Problem Definition

**Candidate Sources:**

* S02 — Mitchell (1997)

**Status:** VERIFIED

**Verification Notes:**

This is an appropriate introductory comparison.

The wording deliberately avoids implying that machine-learning systems contain
no explicitly programmed components.

A machine-learning system is still software containing explicitly designed
algorithms, objectives, data-processing components, and other programmed
elements.

The distinction is primarily about where task-specific behavior is specified
and obtained.

---

## ML01-C04

**Type:** Comparison

**Claim:**

In a typical supervised machine-learning setting, training examples contain
inputs together with corresponding target outputs.

**Importance:** CRITICAL

**Intended Lecture Section:** Formal Concept

**Candidate Sources:**

* S03 — Bishop (2006)
* S04 — Hastie, Tibshirani & Friedman (2009)

**Status:** VERIFIED

**Verification Notes:**

The claim correctly captures the defining introductory characteristic of
supervised learning.

The terms "input" and "target output" are appropriate for the level of ML-01.

More detailed distinctions between regression and classification will be
introduced later.

---

## ML01-C05

**Type:** Definition

**Claim:**

A model is a mathematical or computational representation that maps inputs
to outputs or otherwise represents relationships used to perform a task.

**Importance:** HIGH

**Intended Lecture Section:** Formal Concept

**Candidate Sources:**

* S03 — Bishop (2006)
* S04 — Hastie, Tibshirani & Friedman (2009)

**Status:** VERIFIED

**Verification Notes:**

The definition is intentionally broad enough for an introductory lecture.

The wording avoids restricting models to one mathematical form.

Specific model forms such as linear regression will be introduced in later
lectures.

---

## ML01-C06

**Type:** Definition

**Claim:**

Model parameters are values that determine aspects of a model's behavior and
are typically learned or adjusted during training.

**Importance:** CRITICAL

**Intended Lecture Section:** Formal Concept

**Candidate Sources:**

* S02 — Mitchell (1997)
* S03 — Bishop (2006)

**Status:** VERIFIED

**Verification Notes:**

The wording distinguishes parameters from hyperparameters.

Parameters are part of the model and are commonly learned or adjusted during
training.

The claim deliberately does not state that every parameter is learned using
gradient descent.

Gradient-based optimization will be introduced later.

---

## ML01-C07

**Type:** Definition

**Claim:**

Training is the process through which a model's parameters or other learnable
components are adjusted using experience or data according to a learning
procedure.

**Importance:** CRITICAL

**Intended Lecture Section:** Formal Concept

**Candidate Sources:**

* S02 — Mitchell (1997)
* S03 — Bishop (2006)
* S04 — Hastie, Tibshirani & Friedman (2009)

**Status:** VERIFIED

**Verification Notes:**

The definition remains algorithm-independent.

Training should not be presented as synonymous with gradient descent because
many learning procedures do not use gradient descent.

Gradient descent will be treated as one important optimization method in
ML-07 and subsequent lectures.

---

## ML01-C08

**Type:** Definition

**Claim:**

Inference refers to applying a trained model to input data to obtain a
prediction, output, or other result required by the task.

**Importance:** HIGH

**Intended Lecture Section:** Formal Concept

**Candidate Sources:**

* S03 — Bishop (2006)

**Status:** VERIFIED

**Verification Notes:**

The definition is appropriate for an introductory ML context.

The wording deliberately avoids defining inference as exclusively
probabilistic inference.

In later contexts, "inference" can have more specialized meanings depending
on the model and problem.

---

## ML01-C09

**Type:** Definition

**Claim:**

Generalization refers to a model's ability to perform effectively on data or
examples that were not used to fit the model.

**Importance:** CRITICAL

**Intended Lecture Section:** Formal Concept

**Candidate Sources:**

* S02 — Mitchell (1997)
* S03 — Bishop (2006)
* S04 — Hastie, Tibshirani & Friedman (2009)

**Status:** VERIFIED

**Verification Notes:**

The claim correctly introduces the central distinction between performance
on training examples and performance on unseen examples.

ML-01 should introduce the concept without going deeply into statistical
learning theory.

Detailed treatment of generalization, overfitting, and model assessment will
be developed in ML-04 and ML-12.

---

## ML01-C10

**Type:** Definition

**Claim:**

Supervised learning involves learning from examples in which target outputs
are provided for the corresponding inputs.

**Importance:** CRITICAL

**Intended Lecture Section:** Formal Concept

**Candidate Sources:**

* S03 — Bishop (2006)
* S04 — Hastie, Tibshirani & Friedman (2009)

**Status:** VERIFIED

**Verification Notes:**

The definition correctly identifies the presence of target outputs as the
central introductory characteristic of supervised learning.

The lecture should avoid suggesting that supervised learning is limited to
classification.

Regression is also supervised learning and will appear later in the season.

---

## ML01-C11

**Type:** Definition

**Claim:**

Unsupervised learning involves learning from data without provided target
outputs for the learning task.

**Importance:** HIGH

**Intended Lecture Section:** Formal Concept

**Candidate Sources:**

* S03 — Bishop (2006)
* S04 — Hastie, Tibshirani & Friedman (2009)

**Status:** VERIFIED

**Verification Notes:**

The claim is appropriate as an introductory definition.

Unsupervised learning should not be reduced to the statement "finding
patterns."

That phrase may be used as intuition, but unsupervised learning includes
different objectives and methods.

The absence of provided target outputs is the safer defining characteristic
for ML-01.

---

## ML01-C12

**Type:** Fact / Historical

**Claim:**

Arthur L. Samuel published a paper on machine-learning procedures using the
game of checkers in 1959.

**Importance:** MEDIUM

**Intended Lecture Section:** Hook / Historical Context

**Candidate Sources:**

* S01 — Samuel (1959)

**Status:** VERIFIED

**Verification Notes:**

Samuel's paper, "Some Studies in Machine Learning Using the Game of Checkers,"
was published in the IBM Journal of Research and Development in 1959.

Bibliographic details:

* Volume: 3
* Issue: 3
* Pages: 210–229
* DOI: 10.1147/rd.33.0210

The claim should remain historical and should not be presented as the origin
of all machine learning.

---

## ML01-C13

**Type:** Fact / Historical

**Claim:**

Samuel's checkers experiments demonstrated that a computer program could
improve its checkers-playing performance through machine-learning
procedures and experience.

**Importance:** MEDIUM

**Intended Lecture Section:** Intuition

**Candidate Sources:**

* S01 — Samuel (1959)

**Status:** VERIFIED

**Verification Notes:**

Samuel's paper explicitly reports experiments in which a computer learned to
play a better game of checkers than the person who wrote the program.

The paper also describes learning procedures involving experience from
machine-played games.

For pedagogical accuracy, do not imply that the system "understood" checkers
in a human sense.

Use the example to demonstrate improvement through experience.

---

## ML01-C14

**Type:** Pedagogical

**Claim:**

Machine learning should not be explained as a system that "thinks like a
human."

**Importance:** HIGH

**Intended Lecture Section:** Limitations / Misconceptions

**Candidate Sources:**

* Pedagogical/editorial reasoning

**Status:** VERIFIED

**Verification Notes:**

This is a pedagogical safety rule rather than a textbook definition.

The purpose is to prevent anthropomorphic interpretations.

Machine-learning systems can produce sophisticated behavior without implying
human-like thought, consciousness, understanding, or reasoning.

This statement should therefore be framed explicitly as a teaching
clarification rather than as a scientific theorem.

---

## ML01-C15

**Type:** Pedagogical

**Claim:**

The analogy of "teaching a student" can help explain learning from examples,
but the analogy must not imply that machine-learning models possess human
understanding, consciousness, intentions, or experiences.

**Importance:** HIGH

**Intended Lecture Section:** Intuition

**Candidate Sources:**

* Pedagogical reasoning

**Status:** VERIFIED

**Verification Notes:**

The analogy is acceptable only if its boundaries are explicitly stated.

Safe analogy:

> We provide examples and a learning procedure, and the system changes its
> behavior based on what it has learned.

Unsafe interpretation:

> The model understands the examples in the same way a human student does.

The analogy must therefore be followed by a technical explanation of what
actually changes inside the computational system.

---

# Claims That Must NOT Be Made

The following statements are prohibited in ML-01 unless a future lecture
establishes a precise technical context that makes the statement defensible.

---

## PROHIBITED-01

> "Machine learning means the computer programs itself."

**Reason:**

This is an oversimplification.

Machine-learning systems are designed and implemented by humans. The learning
procedure may automatically determine or adjust parts of the model behavior,
but this does not mean the computer independently creates the entire program.

---

## PROHIBITED-02

> "Machine learning does not require programming."

**Reason:**

Machine-learning systems require software, algorithms, objectives, data
pipelines, evaluation procedures, and other explicitly designed components.

The distinction from traditional programming is not "programming versus no
programming."

---

## PROHIBITED-03

> "AI learns exactly like humans."

**Reason:**

Machine-learning systems and biological learners operate through fundamentally
different mechanisms.

Human-learning analogies may be useful pedagogically, but they must not be
presented as literal equivalence.

---

## PROHIBITED-04

> "More data always makes a model better."

**Reason:**

Performance depends on multiple factors, including:

* data quality,
* data distribution,
* relevance,
* noise,
* model capacity,
* objective,
* optimization,
* and evaluation conditions.

Increasing data quantity does not guarantee improved performance.

---

## PROHIBITED-05

> "Machine learning finds the correct answer automatically."

**Reason:**

A machine-learning system optimizes or learns according to a specified
objective, data, assumptions, learning procedure, and evaluation criterion.

The resulting model is not automatically guaranteed to produce universally
correct answers.

---

# Claim Verification Summary

## Technical Claims

| Category               | Number |
| ---------------------- | -----: |
| Critical               |      7 |
| High importance        |      4 |
| Medium importance      |      2 |
| Technical claims total |     13 |

## Pedagogical Claims

| Category                    | Number |
| --------------------------- | -----: |
| High importance pedagogical |      2 |
| Pedagogical claims total    |      2 |

## Prohibited Statements

| Category              | Number |
| --------------------- | -----: |
| Prohibited statements |      5 |

## Overall Ledger

| Category              | Number |
| --------------------- | -----: |
| Tracked claims        |     15 |
| Prohibited statements |      5 |
| Total tracked items   |     20 |

### Current Verification State

| Status           | Number |
| ---------------- | -----: |
| VERIFIED         |     15 |
| NEEDS CORRECTION |      0 |
| UNVERIFIED       |      0 |
| FALSE            |      0 |
| DEFERRED         |      0 |

---

# Verification Rule

Before a claim enters the final script:

```text
CLAIM IDENTIFIED
       ↓
SOURCE FOUND
       ↓
SOURCE ACTUALLY SUPPORTS CLAIM?
       ↓
WORDING PRECISE?
       ↓
CONTEXT CORRECT?
       ↓
NO HIDDEN ASSUMPTION?
       ↓
PEDAGOGICALLY SAFE?
       ↓
VERIFIED
```

A claim marked `NEEDS CORRECTION`, `UNVERIFIED`, or `FALSE` must not enter
the final lecture script as written.

---

# Source Mapping

| Claim | Primary Source(s) | Verification Role                  |
| ----- | ----------------- | ---------------------------------- |
| C01   | S02, S01          | Formal meaning of learning         |
| C02   | S02, S03, S04     | General conceptual framing         |
| C03   | S02               | Programming vs learning comparison |
| C04   | S03, S04          | Supervised learning                |
| C05   | S03, S04          | Model concept                      |
| C06   | S02, S03          | Parameters                         |
| C07   | S02, S03, S04     | Training                           |
| C08   | S03               | Inference                          |
| C09   | S02, S03, S04     | Generalization                     |
| C10   | S03, S04          | Supervised learning                |
| C11   | S03, S04          | Unsupervised learning              |
| C12   | S01               | Historical publication             |
| C13   | S01               | Samuel's checkers experiments      |
| C14   | Pedagogical       | Anthropomorphism safeguard         |
| C15   | Pedagogical       | Analogy safety                     |

---

# Editorial Rules for ML-01

1. **Use Mitchell's task-performance-experience framework as the formal
   definition.**

2. **Use Samuel primarily for historical context and an early concrete
   example.**

3. Do not present Samuel's 1959 work as the beginning of all machine learning.

4. Do not define machine learning merely as "learning patterns."

5. Do not imply that machine learning eliminates programming.

6. Do not imply that models think, understand, or experience the world like
   humans.

7. Do not introduce gradient descent as if it defines machine learning.

8. Do not imply that supervised learning means classification only.

9. Do not imply that unsupervised learning has one single objective.

10. Introduce generalization conceptually, but defer detailed statistical
    analysis to later lectures.

11. Every mathematical statement introduced in ML-01 must be separately
    verified in `mathematical-notes.md`.

12. Every code-related statement must be separately tested and documented in
    `implementation-notes.md`.

13. Every analogy must pass pedagogical safety review before appearing in the
    final script.

---

# Final Gate for ML-01

ML-01 may proceed to script development only when:

* [x] Core technical claims have been reviewed
* [x] Formal definition is precise
* [x] Historical claims are supported
* [x] Supervised and unsupervised definitions are appropriately scoped
* [x] Generalization is introduced without overclaiming
* [x] Anthropomorphic explanations are controlled
* [x] Prohibited statements are documented
* [ ] Mathematical notes have been completed
* [ ] Implementation notes have been completed
* [ ] Experiment plan has been completed
* [ ] Final script has passed technical review
* [ ] Final script has passed pedagogical safety review

**Current stage:**

> CLAIM VERIFICATION COMPLETE → MATHEMATICAL / IMPLEMENTATION REVIEW NEXT
