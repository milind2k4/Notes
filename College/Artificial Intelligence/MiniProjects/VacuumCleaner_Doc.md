Links:

---

# Vacuum Cleaner Agent Documentation

## Overview

This project simulates a **Simple Reflex Agent** in a classic "Vacuum World" environment.

## Environment

- **Locations:** Two squares, A and B.
- **States:** Each square can be either **Dirty (1)** or **Clean (0)**.
- **Observability:** The agent knows its current location and the status of that location (Fully Observable locally).

## Agent Design

The agent follows a simple set of **Condition-Action Rules**:

1.  **IF** current location is Dirty $\rightarrow$ **Suck**.
2.  **IF** current location is Clean **AND** at A $\rightarrow$ **Move Right**.
3.  **IF** current location is Clean **AND** at B $\rightarrow$ **Move Left**.

## Code Structure

- `Environment` Class: Manages the state of the world (A/B status).
- `SimpleReflexVacuumAgent` Class:
  - `perceive()`: Reads sensors.
  - `act()`: Executes the logic above.
  - `run(steps)`: Runs the simulation loop.

## How to Run

```bash
python "MiniProjects/VacuumCleaner.py"
```

## Sample Output

```text
Vacuum is at A. Status: Dirty
Action: Suck
Location A is now Clean.
--------------------
Vacuum is at A. Status: Clean
Action: Move Right
--------------------
```
