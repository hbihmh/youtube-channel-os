\# ML-01 — Open Questions \& Resolution Log



\## Lecture



\*\*Lecture ID:\*\* ML-01



\*\*Title:\*\* What Is Machine Learning?



\*\*Module:\*\* Foundations



\---



\# Purpose



This document tracks unresolved technical, conceptual, historical,

and pedagogical questions discovered during the research of ML-01.



A question must be resolved, corrected, or explicitly deferred before

the lecture moves into final scripting.



\---



\# Status Definitions



| Status | Meaning |

|---|---|

| OPEN | Question still requires investigation |

| RESOLVED | Question has been adequately answered |

| DEFERRED | Valid question intentionally postponed to a later lecture |

| NOT RELEVANT | Determined not to affect ML-01 |



\---



\# Q01 — What is the most precise introductory definition of machine learning?



\*\*Category:\*\* Definition



\*\*Status:\*\* RESOLVED



\*\*Question:\*\*



How should machine learning be defined without making the definition

too vague for a technical audience or too advanced for an introductory

lecture?



\*\*Resolution:\*\*



Use the task-performance-experience framing associated with Mitchell

as the conceptual foundation.



For ML-01, explain machine learning as the study of methods that allow

a system to improve its performance on a task through experience.



Avoid treating "data" as a direct replacement for "experience" in the

formal definition.



\*\*Lecture Decision:\*\*



Use a precise definition first, followed by a simpler intuitive

explanation.



\---



\# Q02 — Does machine learning mean that the computer programs itself?



\*\*Category:\*\* Misconception



\*\*Status:\*\* RESOLVED



\*\*Question:\*\*



Can machine learning be accurately described as a computer programming

itself?



\*\*Resolution:\*\*



No.



The machine-learning system is still designed and implemented by

people. What changes is that some aspects of the model's behavior or

parameters are determined through a learning procedure using data or

experience rather than being completely specified as explicit rules.



\*\*Lecture Decision:\*\*



Do not use "the computer programs itself" as the definition of machine

learning.



\---



\# Q03 — Does machine learning eliminate programming?



\*\*Category:\*\* Misconception



\*\*Status:\*\* RESOLVED



\*\*Question:\*\*



Does using machine learning mean that programmers no longer need to

write programs?



\*\*Resolution:\*\*



No.



Machine-learning systems still require software, algorithms, data

pipelines, objectives, model definitions, evaluation procedures, and

other explicitly designed components.



\*\*Lecture Decision:\*\*



Explicitly reject the misconception that machine learning means

"programming is no longer required."



\---



\# Q04 — What exactly is a model?



\*\*Category:\*\* Definition



\*\*Status:\*\* RESOLVED



\*\*Question:\*\*



How should "model" be introduced without prematurely committing to a

specific mathematical model such as linear regression?



\*\*Resolution:\*\*



Use an intentionally general definition:



A model is a mathematical or computational representation that maps

inputs to outputs.



More specific model structures will be introduced later.



\*\*Lecture Decision:\*\*



Keep the definition general in ML-01.



\---



\# Q05 — What are model parameters?



\*\*Category:\*\* Definition



\*\*Status:\*\* RESOLVED



\*\*Question:\*\*



Should parameters be introduced in ML-01?



\*\*Resolution:\*\*



Yes, but only conceptually.



Parameters are values within a model that determine aspects of its

behavior and may be adjusted during training.



Do not introduce gradient descent yet.



Do not imply that every machine-learning method learns parameters using

gradient descent.



\*\*Lecture Decision:\*\*



Introduce parameters as a preview of the learning process.



\---



\# Q06 — What is the difference between parameters and hyperparameters?



\*\*Category:\*\* Definition



\*\*Status:\*\* DEFERRED



\*\*Question:\*\*



Should ML-01 explain the distinction between parameters and

hyperparameters?



\*\*Resolution:\*\*



The distinction is technically useful but unnecessary for the first

lecture.



\*\*Lecture Decision:\*\*



Mention parameters only if needed.



Detailed parameter vs hyperparameter distinctions are deferred until

they become relevant to optimization and model training.



\---



\# Q07 — What does "training" mean?



\*\*Category:\*\* Definition



\*\*Status:\*\* RESOLVED



\*\*Question:\*\*



How can training be defined without assuming gradient descent?



\*\*Resolution:\*\*



Training can be introduced as the process of using data and a learning

procedure to adjust a model's learnable components according to a

specified objective or task.



The definition must remain broad enough to include learning methods

other than gradient descent.



\*\*Lecture Decision:\*\*



Use a general definition.



\---



\# Q08 — What does inference mean?



\*\*Category:\*\* Definition



\*\*Status:\*\* RESOLVED



\*\*Question:\*\*



Should inference be introduced in ML-01?



\*\*Resolution:\*\*



Yes, briefly.



Inference can be introduced as using a trained model to produce an

output for an input.



Avoid presenting inference as necessarily being a particular

probabilistic operation.



\*\*Lecture Decision:\*\*



Introduce the training → inference distinction briefly.



\---



\# Q09 — What is generalization?



\*\*Category:\*\* Generalization



\*\*Status:\*\* RESOLVED



\*\*Question:\*\*



Should generalization be introduced in the first lecture?



\*\*Resolution:\*\*



Yes, at an intuitive level.



Generalization refers to how effectively a learned model performs on

data beyond the examples used during training.



Detailed evaluation methodology, train/validation/test splitting, and

data leakage are deferred.



\*\*Lecture Decision:\*\*



Introduce the idea but do not teach the full evaluation framework.



\---



\# Q10 — What is supervised learning?



\*\*Category:\*\* Definition



\*\*Status:\*\* RESOLVED



\*\*Question:\*\*



How should supervised learning be introduced?



\*\*Resolution:\*\*



Supervised learning can be introduced as learning from examples where

target outputs are provided.



The mathematical formulation of supervised learning is deferred.



\*\*Lecture Decision:\*\*



Use one simple example and avoid unnecessary formalism.



\---



\# Q11 — What is unsupervised learning?



\*\*Category:\*\* Definition



\*\*Status:\*\* RESOLVED



\*\*Question:\*\*



How should unsupervised learning be explained without reducing it to

"finding patterns"?



\*\*Resolution:\*\*



Introduce it as learning from data where target outputs are not provided.



The lecture should acknowledge that unsupervised learning contains

multiple problem types and should not be reduced to one universal

algorithm or objective.



\*\*Lecture Decision:\*\*



Keep the explanation short and conceptual.



\---



\# Q12 — Should reinforcement learning be introduced?



\*\*Category:\*\* Scope



\*\*Status:\*\* DEFERRED



\*\*Question:\*\*



Should ML-01 explain supervised, unsupervised, and reinforcement

learning as the three categories of machine learning?



\*\*Resolution:\*\*



Reinforcement learning is important, but including it as a complete

third category risks expanding the scope of ML-01 unnecessarily.



\*\*Lecture Decision:\*\*



If mentioned, describe reinforcement learning only as another major

learning setting.



Do not teach its formal framework in ML-01.



\---



\# Q13 — Is Arthur Samuel's checkers work appropriate for the opening?



\*\*Category:\*\* Historical



\*\*Status:\*\* RESOLVED



\*\*Question:\*\*



Can Arthur Samuel's checkers work be used as historical context?



\*\*Resolution:\*\*



Yes.



Samuel's 1959 work provides useful historical context for early

machine-learning research.



The historical example should not be presented as the modern formal

definition of machine learning.



\*\*Lecture Decision:\*\*



Use the example as an opening or historical hook.



\---



\# Q14 — Did Samuel's program actually "learn"?



\*\*Category:\*\* Historical / Technical



\*\*Status:\*\* RESOLVED



\*\*Question:\*\*



Can the lecture safely say that Samuel's checkers program improved

through experience?



\*\*Resolution:\*\*



Yes, provided the wording accurately reflects Samuel's documented

learning procedures and does not imply modern deep-learning methods.



The final script should use historically precise wording.



\*\*Lecture Decision:\*\*



Use restrained wording such as:



"Samuel developed an early checkers program that used learning

procedures to improve its playing performance."



\---



\# Q15 — Can machine learning be described as "thinking"?



\*\*Category:\*\* Pedagogical



\*\*Status:\*\* RESOLVED



\*\*Question:\*\*



Should the lecture describe machine-learning systems as thinking like

humans?



\*\*Resolution:\*\*



No.



The term "thinking" can introduce an unsupported assumption about human

cognition, consciousness, or understanding.



\*\*Lecture Decision:\*\*



Use computational terminology such as:



\- learning

\- prediction

\- representation

\- optimization

\- computation



Avoid anthropomorphic claims.



\---



\# Q16 — Is the "teaching a student" analogy safe?



\*\*Category:\*\* Pedagogical



\*\*Status:\*\* RESOLVED



\*\*Question:\*\*



Can human learning be used as an analogy for machine learning?



\*\*Resolution:\*\*



Yes, but only as a limited analogy.



The analogy may help explain learning from examples, but it must not

imply that machine-learning models possess human understanding,

intentions, consciousness, or cognition.



\*\*Lecture Decision:\*\*



If used, explicitly identify the analogy as an approximation.



\---



\# Q17 — Should mathematics appear in ML-01?



\*\*Category:\*\* Scope



\*\*Status:\*\* RESOLVED



\*\*Question:\*\*



Should ML-01 contain detailed mathematical derivations?



\*\*Resolution:\*\*



No.



ML-01 should establish the conceptual vocabulary required for later

mathematical lectures.



Detailed equations for loss functions, derivatives, gradients, and

optimization belong to later lectures.



\*\*Lecture Decision:\*\*



Use minimal mathematical notation only when it improves clarity.



\---



\# Q18 — Should Python implementation appear in ML-01?



\*\*Category:\*\* Scope



\*\*Status:\*\* RESOLVED



\*\*Question:\*\*



Should ML-01 include a complete machine-learning implementation?



\*\*Resolution:\*\*



No.



The purpose of ML-01 is conceptual orientation.



Implementation begins later after the required mathematical concepts

have been established.



\*\*Lecture Decision:\*\*



A tiny computational demonstration may be shown, but no complete

learning algorithm should be implemented in ML-01.



\---



\# Q19 — Does more data always improve machine-learning performance?



\*\*Category:\*\* Empirical / Misconception



\*\*Status:\*\* RESOLVED



\*\*Question:\*\*



Can the lecture claim that more training data always produces a better

model?



\*\*Resolution:\*\*



No.



Performance depends on factors including data quality, distribution,

label quality, model capacity, objective, and evaluation procedure.



More data can be beneficial, but "more data always makes the model

better" is too strong.



\*\*Lecture Decision:\*\*



Do not make the absolute claim.



\---



\# Q20 — Does machine learning automatically find the correct answer?



\*\*Category:\*\* Misconception



\*\*Status:\*\* RESOLVED



\*\*Question:\*\*



Can learning be described as automatically discovering the correct

answer?



\*\*Resolution:\*\*



No.



A learned system optimizes or estimates according to its objective,

data, assumptions, model class, and learning procedure.



\*\*Lecture Decision:\*\*



Do not use "correct answer automatically" as a general description.



\---



\# Deferred Questions



The following topics are intentionally outside the scope of ML-01.



| Topic | Target Lecture |

|---|---|

| Train / validation / test methodology | ML-04 |

| Data leakage | ML-04 |

| Loss functions | ML-05 |

| Empirical risk | ML-05 |

| Derivatives | ML-06 |

| Gradients | ML-06 |

| Optimization | ML-06 |

| Gradient descent | ML-07 |

| Learning rate | ML-07 |

| Linear regression | ML-08 |

| Training linear regression | ML-09 |

| NumPy implementation | ML-10 |

| Learning-rate experiments | ML-11 |

| Overfitting / underfitting | ML-12 |

| Bias / variance | ML-12 |

| Regularization | ML-12 |

| Logistic regression | ML-13 |

| Cross-entropy | ML-14 |

| Classification metrics | ML-15 |



\---



\# Final Scope Decision



ML-01 is ready to proceed toward scripting when:



\- \[x] Core definition is resolved.

\- \[x] Rule-based programming comparison is resolved.

\- \[x] Model concept is resolved.

\- \[x] Training concept is resolved.

\- \[x] Inference concept is resolved.

\- \[x] Generalization is introduced at an appropriate level.

\- \[x] Supervised learning is defined.

\- \[x] Unsupervised learning is defined.

\- \[x] Historical context is reviewed.

\- \[x] Major misconceptions are explicitly controlled.

\- \[x] Pedagogical analogy risks are identified.

\- \[x] Later mathematical topics are deferred.

\- \[x] Complete implementation is deferred.

\- \[x] No known unresolved question blocks scripting.



\---



\# Research Gate



Before moving to the script-writing stage:



```text

ALL CRITICAL QUESTIONS

&#x20;       ↓

RESOLVED OR DEFERRED

&#x20;       ↓

NO BLOCKING TECHNICAL ISSUE

&#x20;       ↓

CLAIMS VERIFIED

&#x20;       ↓

MATHEMATICAL SCOPE CONTROLLED

&#x20;       ↓

IMPLEMENTATION SCOPE CONTROLLED

&#x20;       ↓

PEDAGOGICAL RISKS CONTROLLED

&#x20;       ↓

READY FOR SCRIPTING

