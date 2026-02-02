Links:

---

# Evolutionary Computation

## Fundamentals of Evolutionary Computation

### Concept: Nature-Inspired Optimization

**Evolutionary Computation (EC)** is a family of algorithms inspired by biological evolution. They are used to solve optimization problems where traditional methods (like calculus-based gradient descent) fail because the problem is:

- Non-differentiable.
- Discontinuous.
- Has many local optima (rugged landscape).

### Darwinian Principles

EC is based on Charles Darwin's theory of **Natural Selection**:

1.  **Variation:** Individuals in a population are different.
2.  **Inheritance:** Traits are passed to offspring.
3.  **Selection:** Individuals with favorable traits (higher fitness) are more likely to survive and reproduce.
4.  **Time:** Over generations, the population adapts to the environment.

**The Metaphor:**

- **Individual** $\rightarrow$ A potential solution.
- **Environment** $\rightarrow$ The problem constraints.
- **Fitness** $\rightarrow$ Quality of the solution.

---

## Introduction to Evolutionary Algorithms (EAs)

EAs are stochastic search methods that mimic the metaphor of natural biological evolution. EAs operate on a **population** of potential solutions applying the principle of **survival of the fittest** to produce better and better approximations to a solution.

### Types of EAs

1.  **Genetic Algorithms (GA):** Focus on optimizing general combinatorial problems using binary strings.
2.  **Genetic Programming (GP):** Evolving computer programs (LISP trees) to solve a task.
3.  **Evolutionary Strategies (ES):** Focus on optimizing continuous real-valued parameters.
4.  **Evolutionary Programming (EP):** Focus on evolving finite state machines.
