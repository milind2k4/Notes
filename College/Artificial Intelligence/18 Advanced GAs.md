Links:

---

# Advanced GAs

## Advanced Techniques

### Elitism

**Problem:** Random selection/crossover might destroy the absolute best solution found so far.
**Solution:** Always copy the top $k$ individuals (Elites) directly to the next generation without modification.

- _Benefit:_ Guarantees fitness never decreases.

### Diversity Preservation

**Problem:** Premature Convergence. If one decent solution dominates, the whole population becomes identical clones, and search stops.
**Solutions:**

- **Crowding:** New offspring only replace similar parents.
- **Fitness Sharing:** Reduce fitness of individuals that are clustered together (penalize popularity).

### Parameter Tuning

GAs are sensitive to:

- **Population Size:** Too small $\rightarrow$ little diversity. Too large $\rightarrow$ slow.
- **Mutation Rate:** Too low $\rightarrow$ stuck in local optima. Too high $\rightarrow$ random search.
- **Crossover Rate:** Usually high (0.8 - 0.9).

---

## Hybrid GAs

### Concept: Best of Both Worlds

GAs are good at finding the "right hill" (Global Search) but bad at climbing to the very peak (Local Search).
**Hybrid GA:** Run GA to get close, then run a Local Search (like Hill Climbing) on the best individuals.

### Memetic Algorithms

A specific type of Hybrid GA where each individual "learns" during its lifetime (improves itself via local search) before reproducing.

- **Metaphor:** Evolution (Genes) + Culture/Learning (Memes).
- **Workflow:**
  1.  GA Loop.
  2.  Apply Local Search to every offspring.
  3.  Update offspring with optimized version.
