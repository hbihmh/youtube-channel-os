# ML-01 — What Is Machine Learning?

## Definitive Recording Script & Execution Map — v1.0

**Canonical deck:** `slides/ml-01-what-is-machine-learning.pptx`  
**Runtime target:** 12–15 minutes  
**Scope:** conceptual, non-mathematical introduction

### Global directing rules
- Speak conversationally and explain one idea at a time.
- Let diagrams breathe; highlight only the element being discussed.
- Use the exact slide order below. Do not improvise a new teaching sequence.
- No derivatives, gradients, loss functions, gradient descent, optimization mechanics, regression mathematics, logistic regression, detailed overfitting mechanisms, or parameter-update equations.

## 19-scene recording script

### 01 — WHAT IF WE DON'T WRITE EVERY RULE?
**Visual:** Slide 1; `visual-assets/computer-system-illustration.svg`  
**Script:** Imagine you're building a spam filter. You want a computer to look at an email and answer: spam or not spam? We could write rules for suspicious words, links, senders, and so on. But spam can be written in many different ways. So what if, instead of manually writing every rule, we could give the computer examples and build a system that learns useful behavior from them? That question takes us to machine learning.

### 02 — WHAT IS MACHINE LEARNING?
**Visual:** Slide 2  
**Script:** At a high level, machine learning is a way of building systems that improve their performance on a task through experience. The key idea is not that a computer becomes a human-like thinker. It is that we use a learning procedure and experience to produce a model that can perform a task better.

### 03 — TRADITIONAL PROGRAMMING vs. MACHINE LEARNING
**Visual:** Slide 3; `diagrams/traditional-vs-ml.svg`  
**Script:** In traditional programming, we can think in terms of input, explicit rules, and output. The programmer specifies the decision procedure and the computer executes it. In machine learning, we provide examples and a learning procedure. The result is a model, which can then produce outputs for new inputs. The difference is where important decision behavior comes from, not programming versus no programming.

### 04 — THE CORE ML MENTAL MODEL
**Visual:** Slide 4; `diagrams/core-ml-mental-model.svg`  
**Script:** This is the mental model I want you to remember. Examples or experience go into a learning procedure. That produces or adjusts a model. Then a new input goes into the model and we get a prediction. Humans still design the overall system; the learning process determines aspects of the model from experience.

### 05 — HUMANS STILL DESIGN THE SYSTEM
**Visual:** Slide 5; `visual-assets/human-designed-system.svg`  
**Script:** Machine learning does not mean the computer programs itself. Humans still choose the task, design the software, prepare or select data, choose the learning approach, and evaluate the result. What is learned from experience is part of the resulting model. ML changes what we ask the system to learn; it does not remove engineering.

### 06 — WHAT IS A MODEL?
**Visual:** Slide 6; `visual-assets/code-to-model.svg`  
**Script:** A model is a computational representation used to produce outputs from inputs. Think of it as the part of the system we use after learning to make predictions or decisions. For a spam filter, a new email goes into the spam model and the model produces spam or not spam. We do not need its internal mathematics yet.

### 07 — WHAT DOES “LEARNING” MEAN?
**Visual:** Slide 7; `visual-assets/learning-from-examples.svg`  
**Script:** When we say a machine learns, we mean a computational process that uses experience to improve performance on a task. We are not claiming consciousness, emotions, or human-like understanding. The word learning is useful, but the mechanism is computational.

### 08 — TRAINING
**Visual:** Slide 8; `diagrams/training-vs-inference.svg`  
**Script:** Training is the process in which a learning procedure uses available data or experience to produce or adjust a model. The details depend on the method. For this lecture, the important distinction is simple: training is where available experience is used to obtain the model we will later use.

### 09 — INFERENCE
**Visual:** Slide 9; `diagrams/training-vs-inference.svg`  
**Script:** After training, we have a trained model. When we give that model a new input and ask it to produce an output, we are doing inference. Training uses available experience to obtain or adjust the model. Inference uses that resulting model on input data.

### 10 — SUPERVISED LEARNING
**Visual:** Slide 10; `diagrams/supervised-learning-flow.svg`  
**Script:** In supervised learning, the training examples include target outputs. For spam classification, an example might be an email paired with the target spam. Another might be an email paired with not spam. The targets tell the learning process what output is associated with each example. We will study specific supervised algorithms later.

### 11 — UNSUPERVISED LEARNING
**Visual:** Slide 11  
**Script:** What if the data does not come with target answers? Unsupervised learning works with data without provided target outputs. The system can be used to learn useful structure from that data. For now, remember the distinction: supervised learning has provided targets; unsupervised learning does not.

### 12 — LET'S SEE THE IDEA IN CODE
**Visual:** Slide 12; `04-codebase/01-what-is-machine-learning/ml_01_demo.py`  
**Script:** Now let's connect the idea to code. The ML-01 demo is deliberately small. It contrasts a manually written spam rule with a tiny learned model. The point is not to teach an industrial spam filter. The point is to make the conceptual difference visible: explicit behavior in one case, and behavior obtained from examples in the other.

### 13 — OUR EXAMPLE: SPAM FILTER
**Visual:** Slide 13; `visual-assets/spam-email-illustration.svg`  
**Script:** Here is our toy example. We have a few labeled email examples, and we use them as experience for a very small learning procedure. The resulting model can receive a new email and produce a prediction. This is intentionally simple so we can see the idea without hiding it behind a large framework.

### 14 — RULES vs. LEARNED MODEL
**Visual:** Slide 14; `diagrams/traditional-vs-ml.svg`  
**Script:** On the rule-based side, we directly write a condition such as checking for a particular word. On the learned side, we provide examples, run the learning procedure, and use the resulting model. Again, the lesson is not that one approach is always better. The lesson is understanding the different source of the behavior.

### 15 — DID THE SYSTEM LEARN?
**Visual:** Slide 15; demo output / code screen  
**Script:** The demo now shows the resulting behavior. We trained on examples and then asked the model to classify an input. The important observation is that the prediction comes from the model produced by the learning process rather than from a new hand-written rule for that exact email. That is the behavior we wanted to make concrete.

### 16 — CAN IT HANDLE NEW DATA?
**Visual:** Slide 16; `diagrams/generalization-concept.svg` + `visual-assets/generalization-reminder.svg`  
**Script:** But there is a crucial requirement. A model should not only work on the examples it already saw. We care about how it performs on relevant new data. That ability is called generalization. A useful model learns behavior that can transfer beyond the exact training examples.

### 17 — MACHINE LEARNING IS NOT MAGIC
**Visual:** Slide 17; `visual-assets/ml-is-not-magic.svg`  
**Script:** Machine learning is powerful, but it is not magic. Data matters. Models can make mistakes. New situations can be difficult. More data by itself does not guarantee better results. A learning system performs according to its data, task, model, learning procedure, and evaluation. Understanding those pieces is how we understand the system.

### 18 — REMEMBER THESE 3 IDEAS
**Visual:** Slide 18; `diagrams/core-ml-mental-model.svg` + `visual-assets/generalization-reminder.svg`  
**Script:** If you remember only three ideas, remember these. First, machine learning uses experience to improve performance on a task. Second, training produces or adjusts a model, and inference uses that model on new input. Third, useful models need to generalize to relevant new data. Those three ideas form our foundation.

### 19 — NEXT: HOW DOES A MODEL LEARN?
**Visual:** Slide 19; `visual-assets/ml-02-transition.svg`  
**Script:** We now know what the learning process is supposed to accomplish. But how does a model actually become better? What changes inside the model? How does the learning procedure know what to do? Those are the questions for ML-02: How Does a Machine Learning Model Learn?

## Recording gate
Before recording, verify the slide number, visual asset, narration, and code action against the master synchronization matrix. If any one differs, fix the source documents before recording.