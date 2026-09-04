\# ML-01 — Mathematical Notes



\## Lecture



\*\*Title:\*\* What Is Machine Learning?



\*\*Lecture ID:\*\* ML-01



\---



\# Purpose



ML-01 is primarily a conceptual lecture.



The purpose of mathematics in this lecture is to establish the minimum formal

language required to explain what a machine-learning system does.



This lecture should NOT attempt to derive:



\* gradient descent,

\* derivatives,

\* loss-function gradients,

\* linear regression,

\* logistic regression,

\* backpropagation,

\* optimization algorithms.



Those topics belong to later lectures.



\---



\# 1. Minimum Mathematical Model



A useful abstract representation is:



$$

\\hat{y} = f(x;\\theta)

$$



where:



\* \\(x\\) = input

\* \\(f\\) = model or computational function

\* \\(\\theta\\) = model parameters

\* \\(\\hat{y}\\) = model output or prediction



This notation provides a bridge between the conceptual definition of a model

and the mathematical models introduced later.



\---



\# 2. Why This Equation Is Useful



The equation communicates a simple idea:



```text

Input

&#x20; ↓

Model + Parameters

&#x20; ↓

Output / Prediction

```



The parameters \\(\\theta\\) determine aspects of the model's behavior.



Training can then be introduced conceptually as a process that uses experience

or data to determine or adjust the model's learnable components.



Do not introduce a specific optimization rule in ML-01.



\---



\# 3. Training as Parameter Adjustment



A conceptual representation of training is:



$$

\\theta \\rightarrow \\theta'

$$



where:



\* \\(\\theta\\) = parameters before learning

\* \\(\\theta'\\) = parameters after the learning procedure



The purpose is to communicate that learning can change the model's behavior.



This is an abstraction, not a complete mathematical definition of training.



\---



\# 4. Optional Supervised-Learning Representation



For a supervised-learning example:



$$

(x\_i, y\_i)

$$



where:



\* \\(x\_i\\) = input for example \\(i\\)

\* \\(y\_i\\) = target output for example \\(i\\)



The model produces:



$$

\\hat{y}\_i = f(x\_i;\\theta)

$$



The distinction is:



$$

y\_i \\neq \\hat{y}\_i

$$



in general.



The target \\(y\_i\\) is the provided target associated with the training

example.



The prediction \\(\\hat{y}\_i\\) is produced by the model.



\---



\# 5. Loss Function — Deferred



Do NOT derive a loss function in ML-01.



A simple conceptual statement may be made:



> We need some way to measure how well the model is performing.



Formal loss functions begin in:



\*\*ML-05 — What Is a Loss Function?\*\*



Do not introduce MSE here except as a preview if absolutely necessary.



\---



\# 6. Gradient — Deferred



Do NOT introduce:



$$

\\nabla L

$$



or gradient-descent equations in ML-01.



These belong to:



\* ML-06 — Derivatives, Gradients \& Optimization

\* ML-07 — Gradient Descent From First Principles



\---



\# 7. Generalization — Conceptual Only



Generalization can be described conceptually:



$$

\\text{Performance on unseen data}

$$



No statistical derivation is required.



Detailed treatment is deferred to:



\* ML-04 — Training, Validation \& Test Sets

\* ML-12 — Why Do Models Overfit?



\---



\# 8. Mathematical Claims Allowed in Final Script



The following mathematical statements are approved for ML-01:



\### Approved



$$

\\hat{y} = f(x;\\theta)

$$



A model maps an input to an output, with its behavior determined in part by

parameters.



\### Approved



$$

(x\_i,y\_i)

$$



A supervised-learning example can be represented as an input and its

corresponding target output.



\### Approved



$$

\\hat{y}\_i = f(x\_i;\\theta)

$$



A model produces a prediction for a given input using its parameters.



\### Approved



$$

\\theta \\rightarrow \\theta'

$$



Training can conceptually be viewed as changing learnable model components.



\---



\# 9. Mathematical Statements Prohibited in ML-01



Do not claim:



> "The model minimizes the gradient."



Incorrect terminology.



Do not claim:



> "The model learns by taking derivatives."



Too narrow. Not all learning procedures require derivatives.



Do not claim:



> "Gradient descent is how machine learning works."



False as a general statement.



Do not claim:



> "The loss function tells the model what is correct."



Too informal and potentially misleading.



Do not derive optimization mathematics in this lecture.



\---



\# 10. Pedagogical Boundary



ML-01 should answer:



> What is a model?



> What is training?



> What are parameters?



> What is inference?



> What is generalization?



> What is supervised learning?



> What is unsupervised learning?



ML-01 should NOT attempt to answer:



> How are parameters optimized?



> Why does gradient descent work?



> How is a loss function differentiated?



> How does linear regression learn?



Those questions are intentionally reserved for later lectures.



\---



\# Mathematical Verification Status



| Item                          | Status   |

| ----------------------------- | -------- |

| \\(\\hat{y}=f(x;\\theta)\\)       | APPROVED |

| \\((x\_i,y\_i)\\)                 | APPROVED |

| \\(\\hat{y}\_i=f(x\_i;\\theta)\\)   | APPROVED |

| Parameter adjustment concept  | APPROVED |

| Loss derivation               | DEFERRED |

| Derivatives                   | DEFERRED |

| Gradients                     | DEFERRED |

| Gradient descent              | DEFERRED |

| Linear regression equations   | DEFERRED |

| Logistic regression equations | DEFERRED |



\---



\# Final Mathematical Decision



ML-01 uses \*\*minimal mathematics\*\*.



The purpose is not to teach optimization.



The purpose is to establish the mathematical vocabulary needed for the

subsequent first-principles lectures.



\*\*Decision:\*\*



> Introduce the model abstraction \\(\\hat{y}=f(x;\\theta)\\), then defer

> optimization mathematics.



