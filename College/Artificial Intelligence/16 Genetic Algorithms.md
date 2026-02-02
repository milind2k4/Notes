Links:

---

# Genetic Algorithms

## Workflow and Structure

### Concept: The Circle of Life

A **Genetic Algorithm (GA)** follows a standard iterative cycle:

1.  **Initialization:** Create a random population of solutions.
2.  **Evaluation:** Calculate the fitness of each individual.
3.  **Selection:** Pick parents based on fitness.
4.  **Crossover (Recombination):** Combine parents to create offspring.
5.  **Mutation:** Randomly tweak offspring to introduce diversity.
6.  **Replacement:** Form the new generation.
7.  **Termination:** Stop if a good enough solution is found or max generations reached.

---

## Core Components

### Chromosome Representation

How do we encode a solution?

- **Binary Encoding:** `1011001` (Knapsack problem).
- **Permutation Encoding:** `[2, 4, 1, 3]` (TSP - Order matters).
- **Value Encoding:** `[1.2, 3.5, -0.4]` (Real-valued weights).

### Fitness Function

The objective function to maximize.

- _Example (TSP):_ Fitness = $1 / \text{Total Distance}$. (Shorter distance = Higher fitness).

### Selection Strategies

How do we choose parents?

- **Roulette Wheel Selection:** Probability $\propto$ Fitness. (Rich get richer).
- **Tournament Selection:** Pick $k$ random individuals, best one wins. (Adjustable pressure).
- **Rank Selection:** Based on rank order, not raw fitness value. (Prevents super-individuals from dominating early).

### Crossover Techniques

- **One-Point Crossover:** Split at index $k$, swap tails.
  - `111|11` + `000|00` $\rightarrow$ `11100`
- **Two-Point Crossover:** Swap middle segment.
- **Uniform Crossover:** Flip a coin for each gene.

### Mutation Methods

- **Bit Flip:** `0` $\rightarrow$ `1`.
- **Swap:** Exchange two genes (Essential for Permutation encoding like TSP to maintain valid path).
- **Gaussian Mutation:** Add random noise to real values.
