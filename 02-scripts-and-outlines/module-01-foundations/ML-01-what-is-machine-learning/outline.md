# ML-01 — What Is Machine Learning?

## Canonical Lecture Outline — v1.0

**Lecture ID:** ML-01  
**Season:** Season 1 — Machine Learning From First Principles  
**Module:** Foundations  
**Target runtime:** 12–15 minutes  
**Canonical production deck:** `03-production-assets/01-what-is-machine-learning/slides/ml-01-what-is-machine-learning.pptx`

## Purpose
Establish the foundational mental model for machine learning without teaching the mechanics of optimization. The viewer should leave able to explain what ML is, why it differs from explicitly programmed rules, and how training, inference, supervised learning, unsupervised learning, models, and generalization fit together.

## Central thesis
> Machine learning is a way of building systems in which a learning procedure uses experience to improve a model's performance on a task.

## Exact 19-part lecture structure

| # | Teaching beat | Outcome |
|---:|---|---|
| 1 | Opening hook | Create the spam-filter problem and the question of learning from examples. |
| 2 | What is machine learning? | Introduce learning from experience as the central idea. |
| 3 | Traditional programming vs ML | Contrast explicit rules with examples + learning procedure + model. |
| 4 | Core ML mental model | Establish Examples → Learning → Model → New Input → Prediction. |
| 5 | Humans still design the system | Remove the misconception that ML eliminates programming/engineering. |
| 6 | What is a model? | Define a model as a computational representation used to produce outputs from inputs. |
| 7 | What does “learning” mean? | Explain computational improvement through experience, not human-like consciousness. |
| 8 | Training | Define training as using available experience/data to produce or adjust a model. |
| 9 | Inference | Define inference as using a trained model on new input. |
| 10 | Supervised learning | Introduce examples with corresponding target outputs. |
| 11 | Unsupervised learning | Introduce learning from data without provided target outputs. |
| 12 | Concept → code → behavior | Connect the conceptual model to the ML-01 demo without introducing mathematics. |
| 13 | Spam example | Set up the concrete toy classification example. |
| 14 | Rules vs learned model | Show why examples can replace a growing list of manually written decision rules in the toy example. |
| 15 | Did the system learn? | Show the demo output and distinguish a learned model from hard-coded rules. |
| 16 | New data / generalization | Introduce the requirement that the model should work on relevant unseen data. |
| 17 | ML is not magic | State practical limitations: data matters, mistakes happen, new situations can be difficult. |
| 18 | Three ideas to remember | Consolidate the mental model: learn from experience; train → model → infer; generalize. |
| 19 | Bridge to ML-02 | Ask how a model actually becomes better and transition to ML-02. |

## Scope boundary
ML-01 is conceptual. Do not teach or derive derivatives, gradients, loss functions, gradient descent, optimization mechanics, regression mathematics, logistic regression, detailed overfitting mechanisms, or parameter-update equations. Those are deferred to later lectures.

## Production rule
The 19-slide deck, recording script, visual plan, production checklist, recording-readiness documents, and asset inventory must use the same numbering and sequence above. Any future change to the sequence must update the master synchronization matrix first.