Links:

---

# Implementing GAs

## Implementing Genetic Algorithms in Python

### Writing a Basic GA from Scratch

A simple GA to maximize the function $f(x) = x^2$ where $x$ is an integer between 0 and 31 (5-bit binary).

```python
import random

# Parameters
POP_SIZE = 10
GENES = 5
GENERATIONS = 20
MUTATION_RATE = 0.1

# 1. Initialization
population = [[random.randint(0, 1) for _ in range(GENES)] for _ in range(POP_SIZE)]

def decode(individual):
    return int("".join(map(str, individual)), 2)

def fitness(individual):
    x = decode(individual)
    return x ** 2

for gen in range(GENERATIONS):
    # 2. Evaluation
    fitness_scores = [fitness(ind) for ind in population]

    # 3. Selection (Roulette Wheel)
    total_fitness = sum(fitness_scores)
    probs = [f / total_fitness for f in fitness_scores]
    parents = random.choices(population, weights=probs, k=POP_SIZE)

    # 4. Crossover (Single Point)
    offspring = []
    for i in range(0, POP_SIZE, 2):
        p1, p2 = parents[i], parents[i+1]
        point = random.randint(1, GENES-1)
        offspring.append(p1[:point] + p2[point:])
        offspring.append(p2[:point] + p1[point:])

    # 5. Mutation
    for ind in offspring:
        if random.random() < MUTATION_RATE:
            point = random.randint(0, GENES-1)
            ind[point] = 1 - ind[point] # Flip bit

    population = offspring
    best_ind = max(population, key=fitness)
    print(f"Gen {gen}: Best x={decode(best_ind)}, Fitness={fitness(best_ind)}")
```

---

## Visualizing GA Evolution

### Concept: Tracking Progress

We typically plot:

1.  **Best Fitness:** Should increase monotonically (if elitism is used) or generally trend up.
2.  **Average Fitness:** Shows how the whole population is improving.

**Matplotlib Implementation:**

```python
import matplotlib.pyplot as plt

best_fitness_history = []
avg_fitness_history = []

# Inside the loop...
best_fitness_history.append(max(fitness_scores))
avg_fitness_history.append(sum(fitness_scores) / POP_SIZE)

# After loop...
plt.plot(best_fitness_history, label="Best Fitness")
plt.plot(avg_fitness_history, label="Avg Fitness")
plt.xlabel("Generation")
plt.ylabel("Fitness")
plt.legend()
plt.show()
```
