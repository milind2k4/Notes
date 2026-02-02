Links:

---

# Grid Agent Documentation

## Overview

This project simulates a **Goal-Based Agent** navigating a grid world with obstacles to reach a specific target.

## Environment

- **Grid:** $10 \times 10$ virtual grid.
- **Obstacles:** Randomly placed walls (`#`).
- **Goal:** Bottom-right corner (`G`).
- **Observability:** Fully Observable (Agent has access to the map).

## Agent Design

The agent uses **A\* Search** to plan a path from Start to Goal.

1.  **Formulate Goal:** Reach $(9, 9)$.
2.  **Formulate Problem:** Find a sequence of moves avoiding `#`.
3.  **Search:** Run A\* with Manhattan Distance heuristic.
4.  **Execute:** Follow the calculated path step-by-step.

## Code Structure

- `GridEnvironment` Class: Generates the grid and handles display.
- `GoalBasedAgent` Class:
  - `formulate_plan()`: Implements A\* algorithm.
  - `act()`: Executes the next move in the plan.

## How to Run

```bash
python "MiniProjects/GridAgent.py"
```

_Note: The script clears the console to create a simple animation effect._
