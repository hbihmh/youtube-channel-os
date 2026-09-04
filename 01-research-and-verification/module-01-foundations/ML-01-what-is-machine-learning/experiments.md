\# ML-01 — Experiment Notes



\## Lecture



\*\*Lecture ID:\*\* ML-01



\*\*Title:\*\* What Is Machine Learning?



\*\*Module:\*\* Foundations



\---



\# Purpose



This document defines the experiments and demonstrations that may be

used to support the technical and pedagogical claims in ML-01.



ML-01 is primarily conceptual.



Therefore, experiments should remain simple and should demonstrate

the central idea of learning from examples rather than introducing

unnecessary mathematical or implementation complexity.



\---



\# Experiment Policy



Experiments must satisfy the following rules:



1\. Every experiment must have a clear pedagogical purpose.

2\. The experiment must not introduce concepts that belong to later

&#x20;  lectures unless explicitly labeled as a preview.

3\. Results must be reproducible.

4\. Any numerical result shown in the final video must come from an

&#x20;  actually executed experiment.

5\. The experiment must not be presented as proof of a general claim

&#x20;  when it only demonstrates an example.

6\. Code behavior must be verified before recording.

7\. Any analogy used to explain the result must remain technically

&#x20;  consistent with the underlying computation.



\---



\# Experiment 01 — Rule-Based Programming vs Learning



\## Objective



Demonstrate the conceptual difference between explicitly specified

rules and a system whose behavior is determined by parameters learned

from examples.



\## Type



Conceptual demonstration.



\## Status



PLANNED



\## Proposed Demonstration



Construct a very small example where:



\- A rule-based program receives an input.

\- The programmer explicitly defines the decision rule.

\- A learning-based approach receives examples instead.

\- The model's behavior is determined by what it learns from those

&#x20; examples.



\## Expected Learning Outcome



The viewer should understand that machine learning does not mean

"no programming."



Instead, the programmer designs the learning system, objective,

data representation, and learning procedure, while the model's

parameters are adjusted through the learning process.



\## Technical Risk



Do not imply that all machine-learning systems learn in exactly the

same way.



Do not imply that traditional software never changes its behavior

through data.



\---



\# Experiment 02 — Learning From Examples



\## Objective



Provide an intuitive demonstration of how examples can be used to

produce a model capable of making predictions on new inputs.



\## Type



Simple computational demonstration.



\## Status



PLANNED



\## Proposed Demonstration



Use a very small synthetic dataset.



For example:



| Input | Target |

|---:|---:|

| 1 | 2 |

| 2 | 4 |

| 3 | 6 |

| 4 | 8 |



Use this only as an intuitive example of a relationship between

inputs and targets.



A simple model can later be introduced to demonstrate how a model

can represent the relationship.



\## Expected Learning Outcome



The viewer should understand the basic relationship:



```text

Examples

&#x20;  ↓

Learning procedure

&#x20;  ↓

Model

&#x20;  ↓

Prediction for new input

