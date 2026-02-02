Links:
___
# Knowledge and Ethics

## Knowledge Representation (KR)

### Teaching Computers to Reason

**Knowledge Representation** is the field of AI dedicated to representing information about the world in a form that a computer system can utilize to solve complex tasks. It's not just about storing data (like a database); it's about storing _meaning_.

### Logic Systems

#### Propositional Logic (PL)

The simplest logic. Deals with facts that are either True or False.

- **Symbols:** $P, Q, R$ (e.g., $P$ = "It is raining").
- **Connectives:** $\land$ (AND), $\lor$ (OR), $\neg$ (NOT), $\Rightarrow$ (Implies).
- **Example:** $(P \land Q) \Rightarrow R$ ("If it is raining AND I am outside, THEN I get wet").
- **Limitation:** Can't handle objects or relations easily (Need a separate symbol for "Socrates is a man", "Plato is a man").

#### First-Order Logic (FOL)

Extends PL with **Objects**, **Relations**, and **Quantifiers**.

- **Objects:** Socrates, Plato.
- **Predicates:** $Man(x)$, $Mortal(x)$.
- **Quantifiers:**
  - $\forall$ (For All): $\forall x, Man(x) \Rightarrow Mortal(x)$ ("All men are mortal").
  - $\exists$ (There Exists): $\exists x, King(x)$ ("There exists a King").

#### Knowledge Graphs & Ontologies

- **Knowledge Graph:** A network of real-world entities and their relationships (e.g., Google's Knowledge Graph).
  - (Tom Cruise) --[acted_in]--> (Top Gun)
- **Ontology:** A formal naming and definition of the types, properties, and interrelationships of the entities (The "Schema" of the world).

### A Simple Rule-Based System

Using a library like `kanren` (Logic Programming in Python) or simple Python classes.

```python
# A simple Forward Chaining inference engine
facts = {"Man(Socrates)", "Man(Plato)"}
rules = [
    # If X is a Man, then X is Mortal
    lambda fact: f"Mortal({fact.split('(')[1]}" if fact.startswith("Man") else None
]

new_facts = set()
for fact in facts:
    for rule in rules:
        inference = rule(fact)
        if inference:
            new_facts.add(inference)

print(f"Inferred Facts: {new_facts}")
# Output: {'Mortal(Socrates)', 'Mortal(Plato)'}
```

## AI Ethics

### Responsible AI

As AI becomes powerful, we must ensure it is safe, fair, and beneficial.

### Key Challenges

1.  **Bias & Fairness:**
    - _Problem:_ Models trained on biased data produce biased results (e.g., a hiring AI favoring men because historical data shows more men hired).
    - _Solution:_ Diverse datasets, fairness metrics (Demographic Parity).
2.  **Transparency & Explainability (XAI):**
    - _Problem:_ Deep Learning models are "Black Boxes". We don't know _why_ they made a decision.
    - _Solution:_ LIME, SHAP values (Techniques to highlight which input features drove the prediction).
3.  **Accountability:**
    - _Problem:_ Who is responsible if a self-driving car crashes? The coder? The manufacturer? The driver?

### The Black Box Problem

| System                  | Accuracy | Explainability            |
| :---------------------- | :------- | :------------------------ |
| **Decision Tree**       | Medium   | High (If A > 5 then B...) |
| **Deep Neural Network** | High     | Low (Millions of weights) |

> [!IMPORTANT] > **EU AI Act:** The first comprehensive AI law. It classifies AI by risk (Unacceptable, High, Limited, Minimal). High-risk systems (e.g., medical, policing) require strict compliance and explainability.
