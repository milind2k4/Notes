Links:

---

# Maze Reflex Agent Documentation

## Overview

This project simulates a **Simple Reflex Agent** navigating a maze using the **Right-Hand Rule**.

## Environment

- **Maze:** A grid with Walls (`#`) and Empty spaces (` `).
- **Observability:** Partially Observable. The agent only sees walls immediately Ahead, Left, and Right relative to its facing direction.

## Agent Design

The agent uses a classic **Wall Following** strategy (Right-Hand Rule):

1.  **IF** Right is clear $\rightarrow$ Turn Right, Move Forward.
2.  **ELSE IF** Ahead is clear $\rightarrow$ Move Forward.
3.  **ELSE** $\rightarrow$ Turn Left.

This logic guarantees finding the exit in a **simply connected maze** (no loops/islands), but can get stuck in loops in complex mazes.

## Code Structure

- `MazeEnvironment` Class:
  - `get_percept()`: Returns boolean tuple `(WallAhead, WallLeft, WallRight)`.
  - `move_forward()`, `turn_left()`, `turn_right()`: Actuators.
- `ReflexMazeAgent` Class:
  - `act()`: Implements the Right-Hand Rule logic.

## How to Run

```bash
python "MiniProjects/MazeReflex.py"
```
