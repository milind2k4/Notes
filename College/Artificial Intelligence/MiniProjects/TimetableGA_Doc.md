Links:

---

# Timetable Scheduling GA Documentation

## Overview

This project uses a **Genetic Algorithm** to solve a simplified University Timetable Scheduling problem.
The goal is to assign Courses, Professors, Rooms, and Timeslots such that no conflicts occur.

## Problem Constraints

- **Hard Constraints:**
  1.  No two classes can be in the same **Room** at the same **Time**.
  2.  No **Professor** can teach two classes at the same **Time**.

## Genetic Algorithm Design

### 1. Chromosome (Representation)

A list of dictionaries, where each dictionary represents a scheduled class:

```python
{'Course': 'AI', 'Prof': 'Prof. A', 'Room': 'R101', 'Day': 'Mon', 'Time': '9-10'}
```

### 2. Fitness Function

$$ Fitness = \frac{1}{1 + \text{Conflicts}} $$

- 0 Conflicts $\rightarrow$ Fitness = 1.0 (Perfect).
- More Conflicts $\rightarrow$ Lower Fitness.

### 3. Operators

- **Selection:** Truncation Selection (Top 10 parents).
- **Crossover:** Single-Point Crossover (mixes class schedules).
- **Mutation:** Randomly changes a Room, Day, Time, or Professor.
- **Elitism:** Preserves the top 2 solutions.

## How to Run

```bash
python "MiniProjects/TimetableGA.py"
```
