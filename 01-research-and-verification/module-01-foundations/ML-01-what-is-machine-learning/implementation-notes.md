\# ML-01 — Implementation Notes



\## Lecture



\*\*Lecture ID:\*\* ML-01



\*\*Title:\*\* What Is Machine Learning?



\---



\# Implementation Purpose



ML-01 is a conceptual lecture.



The implementation component should demonstrate the distinction between:



1\. manually specified rules,

2\. a model,

3\. parameters,

4\. training,

5\. inference.



The code should NOT attempt to implement a complete machine-learning

algorithm.



\---



\# 1. Code Philosophy



The code exists to support the conceptual explanation.



It is not included merely because the lecture is part of a machine-learning

course.



Every line of code must answer one of these questions:



\* What is an input?

\* What is a model?

\* What is a parameter?

\* What is an output?

\* What changes during learning?



\---



\# 2. Recommended Demonstration



Use a deliberately tiny model:



$$

\\hat{y}=wx+b

$$



However, ML-01 should NOT derive or train this model.



The equation is only used as a preview of what a mathematical model can look

like.



Example conceptual Python:



```python

def model(x, w, b):

&#x20;   return w \* x + b



x = 5

w = 2

b = 1



prediction = model(x, w, b)



print(prediction)

```



Expected output:



```text

11

```



\---



\# 3. What This Demonstrates



The example demonstrates:



```text

x

↓

model

↓

parameters (w, b)

↓

prediction

```



It establishes that a model can be represented computationally.



It does NOT demonstrate learning.



\---



\# 4. Do NOT Call This Training



The following code:



```python

def model(x, w, b):

&#x20;   return w \* x + b

```



is a model definition.



It is NOT a learning algorithm.



Changing:



```python

w = 2

b = 1

```



manually is NOT training.



This distinction must be explicitly maintained in the lecture.



\---



\# 5. Optional Conceptual Comparison



Traditional programming:



```python

def classify\_temperature(temp):

&#x20;   if temp > 30:

&#x20;       return "hot"

&#x20;   else:

&#x20;       return "not hot"

```



The rule is explicitly specified by the programmer.



Model-based example:



```python

def model(x, w, b):

&#x20;   return w \* x + b

```



The second example still contains explicitly programmed structure.



The purpose of the comparison is NOT to claim that machine-learning systems

contain no rules.



The purpose is to establish that later training procedures can determine

learnable parameters from experience/data rather than requiring every

task-specific parameter to be manually specified.



\---



\# 6. Code Execution Requirements



Before recording:



\* \[ ] Python version documented

\* \[ ] Code runs without modification

\* \[ ] Expected output confirmed

\* \[ ] No unnecessary external dependencies

\* \[ ] No deprecated APIs

\* \[ ] Variable names are understandable

\* \[ ] Mathematical notation matches the implementation



For ML-01, standard Python is sufficient.



NumPy is NOT required.



\---



\# 7. Dependencies



ML-01 requires:



```text

Python 3.x

```



No third-party package is required.



\---



\# 8. Code Scope



\### Include



\* tiny model function

\* explicit input

\* explicit parameters

\* model output

\* optional rule-based comparison



\### Exclude



\* NumPy

\* scikit-learn

\* gradient descent

\* optimization

\* loss calculation

\* datasets

\* neural networks

\* training loops

\* plotting

\* external APIs



These belong to later lectures.



\---



\# 9. Pedagogical Safety



Never say:



> "This code is learning."



unless a genuine learning procedure is actually implemented.



Instead say:



> "This is a model. In later lectures, we will build the learning process

> that adjusts its parameters."



Never imply:



> changing `w` manually = learning.



It is parameter assignment.



Never imply:



> a mathematical function automatically becomes machine learning.



A model becomes part of a machine-learning system when combined with an

appropriate learning procedure, experience/data, objective, and evaluation

context.



\---



\# 10. Final Implementation Decision



ML-01 will contain a \*\*small conceptual Python demonstration\*\*.



The code will demonstrate the relationship:



$$

\\hat{y}=f(x;\\theta)

$$



but will intentionally stop before implementing learning.



The actual learning process begins in later lectures.



\*\*Decision:\*\*



> Demonstrate the model first. Build the learning algorithm later.



