# ML-01 — What Is Machine Learning?

## Definitive Recording Script & Execution Guide

**Season:** Season 1 — Machine Learning From First Principles
**Module:** Foundations
**Lecture:** ML-01
**Target Runtime:** 12–15 minutes
**Target Recording Runtime:** ~13–14 minutes
**Recording Status:** Final Recording Script
**Teaching Style:** First-principles, visual, conversational, technically grounded
**Scope:** Non-mathematical introduction

---

# GLOBAL DIRECTING RULES

### Narration

* Speak conversationally, not like reading documentation.
* Explain one idea at a time.
* Pause briefly after every important definition.
* Emphasize the words **model**, **training**, **inference**, **learning procedure**, and **generalization**.
* Do not rush the diagrams. Let the viewer see the flow before moving forward.

### Visual language

* Keep the presentation visually calm.
* Use progressive reveals rather than showing every element simultaneously.
* Highlight the exact element currently being discussed.
* Avoid decorative motion that does not communicate information.
* Never introduce a concept visually before it has been explained verbally.

### Hard scope boundary

Do **not** teach or visually introduce:

* derivatives
* gradients
* loss functions
* gradient descent
* optimization mechanics
* regression mathematics
* logistic regression
* detailed overfitting mechanisms
* mathematical parameter updates

These belong to later lectures.

---

# SCENE 01 — OPENING HOOK

### Slide

**Slide 1 — Opening Hook: The Core Illusion of Software**

### Visual Asset

`visual-assets/computer-system-illustration.svg`

### Target Duration

**~40 seconds**

### Spoken Script

> Imagine you're building a spam filter.
>
> You want your computer to look at an email and answer one simple question:
>
> **Spam or not spam?**
>
> At first, this sounds like a normal programming problem.
>
> We could write a rule:
>
> "If the email contains a suspicious word, mark it as spam."
>
> Then another rule.
>
> And another.
>
> But what happens when people write spam messages in completely different ways?
>
> Suddenly, we're trying to anticipate every possible situation.
>
> So here's the more interesting question:
>
> **What if, instead of manually writing every rule, we could give the computer examples and build a system that learns useful behavior from those examples?**
>
> That question takes us to the fundamental idea behind machine learning.

### Visual / Editing Cues

**0:00–0:05**

* Start on title slide.
* Minimal motion.
* Let title settle.

**0:05–0:15**

* Reveal the computer/input/output illustration.

**0:15–0:30**

* Highlight the input and output.
* Briefly emphasize the idea of manually specifying behavior.

**0:30–0:40**

* Transition from the traditional computer illustration toward the ML theme.
* Hold for the question:
  **"What if we could give the computer examples?"**

### Director Note

The opening should create curiosity, not define ML immediately.

---

# SCENE 02 — TRADITIONAL PROGRAMMING

### Slide

**Slide 2 — What Is Machine Learning? / Traditional Programming Foundation**

### Visual Asset

`diagrams/traditional-vs-ml.svg`

### Target Duration

**~40 seconds**

### Spoken Script

> Before we understand machine learning, let's establish the traditional programming model.
>
> In traditional programming, a programmer explicitly writes instructions that tell the computer what to do.
>
> We can summarize that idea very simply:
>
> **Input plus explicit rules produces an output.**
>
> The programmer designs the rules.
>
> The computer executes those rules.
>
> For a simple problem, this works extremely well.
>
> If we know exactly what behavior we want, we can describe it as instructions and let the computer execute them.
>
> The difficulty appears when the rules become extremely difficult to specify.

### Visual / Editing Cues

* Reveal **Input**.
* Reveal **Explicit Rules**.
* Reveal **Output**.
* Highlight each element as it is mentioned.
* Hold the complete flow for approximately 2 seconds.

### Transition

Cut or dissolve into the next slide when saying:

> "The difficulty appears when the rules become extremely difficult to specify."

---

# SCENE 03 — WHEN RULES BECOME DIFFICULT

### Slide

**Slide 3 — The Traditional Programming Paradigm vs. Machine Learning Paradigm**

### Visual Asset

`visual-assets/rules-become-difficult.svg`

### Target Duration

**~40 seconds**

### Spoken Script

> Let's return to our spam filter.
>
> What exactly makes an email spam?
>
> Maybe it's certain words.
>
> Maybe it's unusual links.
>
> Maybe it's information about the sender.
>
> Maybe it's the structure of the message.
>
> And often, it's some combination of several things.
>
> The problem is not that we can't write rules.
>
> The problem is that the number of possible situations can become very large.
>
> And new examples can appear that our rules never anticipated.
>
> So instead of asking:
>
> **"What rule should I write?"**
>
> we can ask:
>
> **"Can a computer learn useful patterns from examples?"**

### Visual / Editing Cues

* Reveal rules one at a time.
* Increase visual density gradually.
* Do not animate too quickly.
* On "very large," briefly show the growing rule collection.
* On the final question, clear the clutter and prepare the transition.

---

# SCENE 04 — THE CORE IDEA OF MACHINE LEARNING

### Slide

**Slide 4 — Core Mental Model**

### Visual Asset

`diagrams/core-ml-mental-model.svg`

### Target Duration

**~55 seconds**

### Spoken Script

> This is the central mental model for this entire course.
>
> Instead of manually specifying every rule that connects an input to an output, we provide experience or data to a learning system.
>
> A learning procedure uses that experience to produce or adjust a model.
>
> Then that model can be used on new inputs to produce predictions.
>
> So the basic process is:
>
> **Examples or experience, then a learning procedure, then a model, and finally predictions for new inputs.**
>
> Notice something important.
>
> Machine learning does not mean that programming disappears.
>
> Humans still design the system.
>
> We still define the task.
>
> We still decide what data to use.
>
> We still build the software around the learning process.
>
> The difference is that we design a system that can learn useful behavior from experience instead of manually specifying every rule.

### Visual / Editing Cues

* This is a **hero visual**.
* Reveal:

  1. Examples / Experience
  2. Learning Procedure
  3. Model
  4. New Input
  5. Prediction
* Highlight only the current node.
* At "programming does not disappear," briefly highlight the human/system relationship if present in supporting visual later.
* End with the complete diagram visible.

### Director Note

**Do not rush this scene.** This is the single most important mental model of ML-01.

---

# SCENE 05 — HUMANS STILL DESIGN THE SYSTEM

### Slide

**Slide 5 — Training Phase Breakdown / Human Role**

### Visual Asset

`visual-assets/human-designed-system.svg`

### Target Duration

**~35 seconds**

### Spoken Script

> There's a misconception we should remove right now.
>
> Machine learning does not mean the computer simply programs itself.
>
> Humans still design the learning system.
>
> We choose the task.
>
> We design the software.
>
> We decide what data or experience the system will use.
>
> We choose how the system should learn and how we will evaluate it.
>
> What the learning process determines is the resulting model, based on the experience we provide.
>
> So machine learning changes what we ask the computer to learn from data.
>
> It does not eliminate human engineering.

### Visual / Editing Cues

* Highlight **Human / Developer**.
* Then highlight **Learning System**.
* Then **Data / Experience**.
* End on the message:
  **Humans still design the system.**

---

# SCENE 06 — WHAT IS A MODEL?

### Slide

**Slide 6 — What Is a Model?**

### Visual Asset

`diagrams/core-ml-mental-model.svg`

Supporting:
`visual-assets/code-to-model.svg`

### Target Duration

**~40 seconds**

### Spoken Script

> Now we need one of the most important words in machine learning:
>
> **model.**
>
> A model is a computational representation that we use to produce outputs from inputs.
>
> You can think of it as a system that takes an input and produces an output.
>
> For our example:
>
> **New email goes into the spam model, and the model produces a prediction: spam or not spam.**
>
> At this stage, don't worry about what the model looks like internally.
>
> The important idea is that the model is the computational representation we use after the learning process has produced or adjusted it.

### Visual / Editing Cues

* Show:
  **Input → Model → Output**
* Highlight the model box.
* Transition to:
  **New Email → Spam Model → Spam / Not Spam**
* Avoid showing mathematical internals.

---

# SCENE 07 — WHAT DOES "LEARNING" MEAN?

### Slide

**Slide 7 — What Does Learning Actually Mean Here?**

### Visual Asset

`visual-assets/learning-from-examples.svg`

### Target Duration

**~40 seconds**

### Spoken Script

> We should also be precise about what we mean when we say that a machine "learns."
>
> We're not saying that a computer suddenly becomes a human-like thinker.
>
> In machine learning, learning refers to a computational process through which a system improves its performance on a task through experience.
>
> The system receives experience.
>
> A learning procedure uses that experience.
>
> And the resulting system may perform better on the task.
>
> So when we say that a model learns from examples, we're describing a computational process.
>
> We're not claiming human consciousness, emotions, or human understanding.

### Visual / Editing Cues

* Reveal:
  **Experience → System → Improved Performance**
* Highlight **Experience**.
* Then **System**.
* Then **Improved Performance**.
* Hold on:
  **"Learning = improvement through experience."**

---

# SCENE 08 — TRAINING

### Slide

**Slide 8 — Training Phase Breakdown**

### Visual Asset

`diagrams/training-vs-inference.svg`

### Target Duration

**~40 seconds**

### Spoken Script

> Now let's introduce another important term:
>
> **training.**
>
> Training is the process through which a learning procedure uses available data or experience to produce or adjust a model.
>
> So we can think about training as:
>
> **Training data goes into a learning procedure, and a model is produced or adjusted.**
>
> The exact mechanism depends on the machine-learning method.
>
> We don't need those details yet.
>
> For this lecture, remember one simple idea:
>
> **Training is how we obtain or adjust the model using experience.**

### Visual / Editing Cues

* Highlight **Training** side of the diagram.
* Follow the flow from data to model.
* Keep any mechanism/internal-process representation visually abstract.
* Do not show gradients, loss, or optimization terminology.

---

# SCENE 09 — INFERENCE

### Slide

**Slide 9 — Inference Phase Breakdown**

### Visual Asset

`diagrams/training-vs-inference.svg`

### Supporting Visual

`visual-assets/spam-email-illustration.svg`

### Target Duration

**~35 seconds**

### Spoken Script

> Once training has produced a model, we can use that model on new inputs.
>
> This is commonly called **inference**.
>
> The basic flow is:
>
> **New input, trained model, prediction.**
>
> For our spam example:
>
> **New email, trained spam model, spam or not spam.**
>
> And this distinction is important.
>
> Training is about using experience to produce or adjust the model.
>
> Inference is about using that resulting model to produce an output for new input.

### Visual / Editing Cues

* Visually separate training from inference.
* Highlight **New Input**.
* Then **Trained Model**.
* Then **Prediction**.
* Pause briefly between the two definitions.

---

# SCENE 10 — SUPERVISED LEARNING

### Slide

**Slide 10 — Supervised Learning Paradigm**

### Visual Asset

`diagrams/supervised-learning-flow.svg`

### Target Duration

**~45 seconds**

### Spoken Script

> Our spam example has another important property.
>
> The examples already have answers attached to them.
>
> For example:
>
> Email A — Spam.
>
> Email B — Not spam.
>
> Email C — Spam.
>
> These examples contain inputs together with corresponding target outputs.
>
> This is the basic idea behind **supervised learning**.
>
> In supervised learning, we learn from examples where the input is accompanied by a target output.
>
> The target gives the learning process information about the desired output for that example.
>
> Supervised learning is one of the major categories of machine learning.
>
> We'll study specific supervised-learning algorithms later.

### Visual / Editing Cues

* Reveal example pairs one at a time.
* Highlight **Input** and **Target** separately.
* Then animate the examples flowing toward the learning procedure.
* Do not reveal any mathematical learning mechanism.

---

# SCENE 11 — UNSUPERVISED LEARNING

### Slide

**Slide 11 — Unsupervised Learning / General Concepts**

### Visual Asset

`diagrams/supervised-learning-flow.svg`

or use a clean simplified unlabeled-data visual if present in the deck.

### Target Duration

**~35 seconds**

### Spoken Script

> But what if our data doesn't come with target answers?
>
> Suppose we have a collection of data, but nobody tells us which category each example belongs to.
>
> Machine-learning methods can still be used to learn structure from that data.
>
> This is the basic idea behind **unsupervised learning**.
>
> The key distinction is simple:
>
> **Supervised learning uses examples with target outputs.**
>
> **Unsupervised learning works with data without provided target outputs.**
>
> We'll explore specific methods later.
>
> For now, that's all we need.

### Visual / Editing Cues

* First show labeled examples.
* Remove the targets.
* Show only data.
* Reveal:
  **Data → Learning Procedure → Discovered Structure**
* Keep this intentionally high-level.
* Do not introduce clustering mathematics.

---

# SCENE 12 — GENERALIZATION

### Slide

**Slide 12 — Generalization: Performing on Unseen Data**

### Visual Asset

`diagrams/generalization-concept.svg`

Supporting:
`visual-assets/generalization-reminder.svg`

### Target Duration

**~50 seconds**

### Spoken Script

> Now we reach one of the most important ideas in machine learning:
>
> **generalization.**
>
> Imagine we train a model using a collection of emails.
>
> The model performs very well on those exact emails.
>
> Does that automatically mean we've built a useful spam filter?
>
> No.
>
> The real question is what happens when we give the model emails it has not seen before.
>
> A useful model should be able to perform effectively on new data.
>
> That's what we mean by generalization.
>
> The goal isn't simply to reproduce the training examples.
>
> The goal is to learn something useful that can be applied to new cases.
>
> This idea will become extremely important later when we study how models are evaluated.

### Visual / Editing Cues

* Start with **Training Examples**.
* Move to **Model**.
* Then reveal **New / Unseen Examples**.
* Finally reveal **Useful Predictions**.
* Emphasize "new" or "unseen."
* **Do not show underfitting, overfitting, bias, or variance.**

### Director Note

This is another **critical teaching moment**. Slow down slightly.

---

# SCENE 13 — WHAT MACHINE LEARNING IS NOT

### Slide

**Slide 13 — Failure Modes & Limitations / Common Misconceptions**

### Visual Asset

`visual-assets/ml-is-not-magic.svg`

### Target Duration

**~65 seconds**

### Spoken Script

> Before we move on, let's clear up a few common misconceptions.
>
> First:
>
> **"Machine learning means the computer programs itself."**
>
> Not exactly.
>
> Humans still design and program the learning system.
>
> Second:
>
> **"Machine learning doesn't require programming."**
>
> It does.
>
> Machine-learning systems still require software for data processing, learning, evaluation, deployment, and many other parts of the system.
>
> Third:
>
> **"AI learns exactly like humans."**
>
> We shouldn't assume that.
>
> Machine learning is a computational learning process. Human learning is a very different phenomenon.
>
> Fourth:
>
> **"More data always makes a model better."**
>
> More data can help, but data quality, relevance, the task, the model, and many other factors matter.
>
> And finally:
>
> **"Machine learning automatically finds the correct answer."**
>
> It doesn't guarantee perfect answers.
>
> Performance depends on the task, the data, the learning system, the model, and how we evaluate it.
>
> Machine learning is powerful, but it isn't magic.

### Visual / Editing Cues

Use a **Myth → Correction** rhythm.

For each misconception:

1. Show myth.
2. Brief pause.
3. Replace with correction.
4. Highlight the key phrase.
5. Move on.

Do not spend equal time on every misconception; maintain pace.

---

# SCENE 14 — COMPLETE MENTAL MODEL

### Slide

**Slide 14 — Complete Mental Model**

### Visual Asset

`diagrams/core-ml-mental-model.svg`

### Target Duration

**~40 seconds**

### Spoken Script

> Let's put everything together.
>
> This is the mental model I want you to remember from this lecture.
>
> **Data or experience.**
>
> Then a **learning procedure**.
>
> That produces or adjusts a **model**.
>
> Then we give the model a **new input**.
>
> And the model produces a **prediction**.
>
> So:
>
> **Data or experience → learning procedure → model → new input → prediction.**
>
> That is the basic machine-learning pipeline we've been building throughout this lecture.

### Visual / Editing Cues

* Start with an empty canvas if possible.
* Reveal each node sequentially.
* Highlight each node exactly when spoken.
* End with the entire pipeline visible.
* Hold for 2–3 seconds.

### Director Note

This is the **hero recap shot**. It should be clean enough that a viewer could pause the video and understand the entire lecture from this frame.

---

# SCENE 15 — END-TO-END SPAM EXAMPLE

### Slide

**Slide 15 — The Spam Filter Example**

### Visual Asset

`diagrams/spam-classifier-example.svg`

Supporting:
`visual-assets/spam-email-illustration.svg`

### Target Duration

**~55 seconds**

### Spoken Script

> Let's run through the entire process one final time using our spam classifier.
>
> We begin with examples.
>
> Email A is spam.
>
> Email B is not spam.
>
> Email C is spam.
>
> Email D is not spam.
>
> These examples provide experience for our learning system.
>
> During training, the learning procedure uses those examples to produce or adjust a model.
>
> Now a completely new email arrives.
>
> We give that email to the trained model.
>
> The model produces a prediction:
>
> **Spam.**
>
> Or:
>
> **Not spam.**
>
> The important point is that we're not simply trying to memorize those four emails.
>
> We want the model to learn useful behavior that can be applied to new emails.
>
> And that brings us back to generalization.

### Visual / Editing Cues

Progressive five-step sequence:

**Step 1:** Show labeled emails.

**Step 2:** Animate examples into learning procedure.

**Step 3:** Reveal model.

**Step 4:** Introduce a visually distinct new email.

**Step 5:** Route new email through trained model to prediction.

At "new email," visually distinguish it from training examples.

### Director Note

This scene should feel like the payoff of the lecture.

---

# SCENE 16 — HISTORICAL PERSPECTIVE

### Slide

**Slide 16 — A Brief Historical Perspective**

### Visual Asset

`visual-assets/historical-arthur-samuel.svg`

### Target Duration

**~35 seconds**

### Spoken Script

> The idea of machines improving through experience is not new.
>
> One important early figure was Arthur Samuel.
>
> In the 1950s, Samuel worked on computer programs for playing checkers and explored ways for a program to improve its playing performance through experience.
>
> In 1959, he published an important paper titled:
>
> **"Some Studies in Machine Learning Using the Game of Checkers."**
>
> We don't need the historical details for this lecture.
>
> The important point is that the idea of machines improving their performance through experience has a long history.

### Visual / Editing Cues

* Show **1959** first.
* Reveal Arthur Samuel.
* Then checkers.
* Finally show the paper title briefly.
* Keep the entire scene visually simple.
* Do not turn this into a history lecture.

---

# SCENE 17 — FINAL RECAP

### Slide

**Slide 17 — Key Takeaways & Summary**

### Visual Asset

`diagrams/core-ml-mental-model.svg`

Supporting:
`visual-assets/generalization-reminder.svg`

### Target Duration

**~50 seconds**

### Spoken Script

> Let's recap the vocabulary we've built.
>
> **Machine learning** is a computational approach in which a system improves its performance on a task through experience.
>
> A **model** is a computational representation used to produce outputs from inputs.
>
> **Training** is the process through which a learning procedure uses available experience or data to produce or adjust a model.
>
> **Inference** is using that trained model to produce an output for new input.
>
> **Supervised learning** uses examples with corresponding target outputs.
>
> **Unsupervised learning** works with data without provided target outputs.
>
> And **generalization** is the ability of a model to perform effectively on data it wasn't simply trained on.
>
> These are the basic building blocks we'll use throughout the rest of the course.

### Visual / Editing Cues

Use concise keyword cards:

* Machine Learning
* Model
* Training
* Inference
* Supervised Learning
* Unsupervised Learning
* Generalization

Highlight each term as it is spoken.

---

# SCENE 18 — FINAL TAKEAWAY

### Slide

**Slide 18 — What We Did NOT Cover / Final Takeaway**

### Visual Asset

`diagrams/traditional-vs-ml.svg`

### Target Duration

**~45 seconds**

### Spoken Script

> If you remember only one comparison from this lecture, remember this.
>
> In traditional programming:
>
> **Input plus explicit rules produces an output.**
>
> In machine learning:
>
> **Examples and a learning procedure are used to produce a model.**
>
> Then:
>
> **The model and a new input produce an output.**
>
> The fundamental idea is not that humans stop programming.
>
> The idea is that for certain problems, instead of manually specifying every rule needed for the desired behavior, we design a learning system that uses experience to produce a model capable of performing the task.
>
> That's the foundation we're going to build on.

### Visual / Editing Cues

* Split-screen comparison.
* Left: Traditional Programming.
* Right: Machine Learning.
* Reveal each flow sequentially.
* End with both complete flows visible.

### Important

Do not use this scene to teach mathematical learning mechanisms.

---

# SCENE 19 — BRIDGE TO ML-02 / OUTRO

### Slide

**Slide 19 — ML-02: How Does a Machine Learning Model Learn?**

### Visual Asset

`visual-assets/ml-02-transition.svg`

### Target Duration

**~35 seconds**

### Spoken Script

> So now we have the basic picture.
>
> A machine-learning system can use experience to produce or adjust a model.
>
> But that leaves us with the next fundamental question:
>
> **How does that actually happen?**
>
> How does a model change from being poor at a task to becoming better at it?
>
> What happens inside the learning process?
>
> That's what we'll explore in the next lecture:
>
> **ML-02 — How Does a Machine Learning Model Learn?**
>
> I'll see you there.

### Visual / Editing Cues

**First 10 seconds**

* Keep the visual minimal.
* Let the question build.

**Middle**

* Reveal:
  **How does learning actually happen?**

**Final**

* Full-screen:
  **ML-02 — How Does a Machine Learning Model Learn?**

* Hold for approximately 3 seconds.

* Fade to black.

---

# RECORDING EXECUTION GUIDE

## 1. Recommended Recording Order

Record the lecture in this exact order:

1. Slide 1 — Hook
2. Slide 2 — Traditional Programming
3. Slide 3 — Rules Become Difficult
4. Slide 4 — Core ML Mental Model
5. Slide 5 — Human Role
6. Slide 6 — Model
7. Slide 7 — Learning
8. Slide 8 — Training
9. Slide 9 — Inference
10. Slide 10 — Supervised Learning
11. Slide 11 — Unsupervised Learning
12. Slide 12 — Generalization
13. Slide 13 — Misconceptions
14. Slide 14 — Complete Mental Model
15. Slide 15 — Spam Example
16. Slide 16 — Historical Perspective
17. Slide 17 — Recap
18. Slide 18 — Final Takeaway
19. Slide 19 — ML-02 Bridge

---

# 2. Recording Style

### Voice

Use a calm, confident teaching voice.

Not:

> "Machine learning is a computational approach in which..."

as if reading a textbook.

Instead:

> "Here's the important idea..."

Use natural contractions where appropriate:

* "we're"
* "it's"
* "doesn't"
* "we'll"

### Pace

Target approximately:

**130–150 spoken words per minute**

Slow down slightly for:

* machine-learning definition
* model definition
* training vs inference
* supervised vs unsupervised
* generalization
* final mental model

Speed up slightly during:

* misconception list
* historical context
* recap

---

# 3. Emphasis Words

Naturally emphasize:

**machine learning**

**learning procedure**

**model**

**training**

**inference**

**supervised learning**

**unsupervised learning**

**generalization**

**new data**

**experience**

Do not over-emphasize every technical term.

---

# 4. Visual Highlighting Rules

When saying:

> "Examples"

Highlight **Examples / Experience**.

When saying:

> "Learning Procedure"

Highlight **Learning Procedure**.

When saying:

> "Model"

Highlight **Model**.

When saying:

> "New Input"

Highlight **New Input**.

When saying:

> "Prediction"

Highlight **Prediction**.

The viewer should always be able to answer:

**"Where should I look right now?"**

---

# 5. Transition Rules

### Concept → Concept

Use a clean dissolve or short cut.

### Process → Process

Use progressive animation.

### Major mental model

Use a slower reveal.

### Historical section

Use a simple cut.

### Final recap

Use a slightly faster rhythm.

### ML-02 transition

Use the cleanest transition of the lecture.

Avoid:

* flashy zooms
* excessive camera movement
* unnecessary particle effects
* decorative animations
* distracting sound effects

---

# 6. Screen Recording / Demo Rule

If the actual code/notebook demonstration is included in the final production edit:

* Record the code/demo separately from the main narration where practical.
* Zoom the editor so code is readable at 1080p.
* Never leave tiny code on screen.
* Narration should explain the conceptual purpose of the demo.
* Do not turn ML-01 into a Python tutorial.
* Do not explain implementation details beyond what is required to reinforce the ML mental model.

The demo exists to support the concept, not become a second lesson.

---

# 7. Retake Policy

Immediately retake a sentence when:

* a technical term is mispronounced
* a definition changes meaning
* "training" and "inference" are accidentally reversed
* "target" and "input" are confused
* the speaker introduces an out-of-scope mathematical concept
* a sentence becomes difficult to understand
* a visual cue is missed at a critical teaching moment

Minor natural speech imperfections can remain if they do not affect comprehension.

Do not chase artificial perfection.

---

# 8. Critical Technical Accuracy Checks

Before accepting the recording, verify:

* [ ] ML is described as learning/improving through experience.
* [ ] Humans are still clearly responsible for designing the learning system.
* [ ] A model is described as a computational representation.
* [ ] Training is distinguished from inference.
* [ ] Supervised learning is associated with target outputs.
* [ ] Unsupervised learning is described without provided target outputs.
* [ ] Generalization is associated with useful performance on new/unseen data.
* [ ] No claim says ML guarantees correct answers.
* [ ] No claim says more data automatically guarantees better results.
* [ ] No claim implies machine learning works exactly like human learning.
* [ ] Arthur Samuel's historical section remains brief.
* [ ] No mathematical mechanism is prematurely taught.

---

# 9. Hard Scope Check Before Final Edit

Search the final narration/transcript for these terms:

* derivatives
* gradients
* gradient descent
* loss function
* optimization
* regression
* logistic regression
* optimization landscape
* parameter update equations
* overfitting
* underfitting
* bias-variance tradeoff

Any occurrence should be reviewed against the approved scope.

A later concept may be referenced only if the narration is explicitly establishing a boundary, not teaching that concept.

---

# 10. Final Audio Checklist

Before final export:

* [ ] Voice is clearly understandable.
* [ ] No clipping.
* [ ] No obvious background noise.
* [ ] Volume remains consistent.
* [ ] Pauses do not feel unnaturally long.
* [ ] Technical terms are clearly pronounced.
* [ ] Slide transitions do not cut off words.
* [ ] Visual changes occur at the intended teaching moments.
* [ ] Music, if used, never competes with narration.
* [ ] No unnecessary sound effects distract from teaching.

---

# 11. Final Visual Checklist

* [ ] All 19 slides appear in correct order.
* [ ] Every visual corresponds to the narration.
* [ ] Text is readable at 1080p.
* [ ] No SVG is cropped incorrectly.
* [ ] No diagram introduces a concept before narration.
* [ ] No forbidden mathematical concepts appear visually.
* [ ] Generalization visual remains simplified.
* [ ] Supervised-learning visual does not contain optimization terminology.
* [ ] Core mental model receives sufficient screen time.
* [ ] Spam example clearly separates training examples from new input.
* [ ] ML-02 transition is clean and minimal.
* [ ] No visual is present merely for decoration.

---

# 12. Final Director's Quality Gate

ML-01 is **READY FOR FINAL EDIT** only if all of the following are true:

### Content

* [ ] Narration follows the approved first-principles scope.
* [ ] Definitions are technically defensible.
* [ ] No premature mathematics is taught.
* [ ] No major concept is introduced without explanation.

### Pedagogy

* [ ] Traditional programming is established first.
* [ ] The limitation of explicit rules motivates ML.
* [ ] The core ML mental model is introduced early.
* [ ] Model → training → inference relationships are clear.
* [ ] Supervised/unsupervised distinction is simple.
* [ ] Generalization is introduced correctly.
* [ ] The spam example unifies the lecture.
* [ ] The ending creates a natural question for ML-02.

### Production

* [ ] Voice recording is clean.
* [ ] Slides are synchronized.
* [ ] Visual highlights match narration.
* [ ] No distracting transitions.
* [ ] Code/demo remains secondary to teaching.
* [ ] Final runtime is between approximately 12 and 15 minutes.

### Final decision

**If every critical item passes:**

> **ML-01 — READY FOR FINAL EDIT**

Otherwise:

> **RETURN TO RECORDING / EDITING**

Do not proceed to YouTube publishing until the final fact-check and technical QA stages defined by the master production SOP are completed.

---

# END OF ML-01 RECORDING SCRIPT

**Core takeaway for the director:**

> Do not make the viewer memorize machine-learning terminology.

Make them **see the process**:

**Experience → Learning Procedure → Model → New Input → Prediction**

Everything in ML-01 should reinforce that mental model.
