Links:
___
# Implementing Agents

## Agent Architecture

### The Blueprint

To implement an agent in code, we generally separate the **Environment** (the world simulation) from the **Agent** (the decision maker).

### The Loop

The core of any agent simulation is the **Interaction Loop**:

1.  **Environment** generates a `Percept`.
2.  **Agent** receives `Percept` via sensors.
3.  **Agent** processes `Percept` and returns an `Action`.
4.  **Environment** accepts `Action`, updates state, and generates next `Percept`.

```python
# Pseudo-code for the loop
while not environment.is_done():
    percept = environment.get_percept(agent)
    action = agent.program(percept)
    environment.execute_action(agent, action)
```

## State Management

### Memory

For non-reflex agents, maintaining state is critical. State allows the agent to remember the past and plan for the future.

### The `Agent` Class Pattern

We can define a base class for all agents.

```python
class Agent:
    def __init__(self):
        self.alive = True
        self.performance = 0

    def program(self, percept):
        """The brain of the agent. Must be implemented by subclasses."""
        raise NotImplementedError
```

### Table-Driven Agent

A simple agent that uses a lookup table for every possible percept sequence.

- **Pros:** Optimal if the table is correct.
- **Cons:** **Impossible** for large problems (Table size grows exponentially: $|P|^T$).

```python
class TableDrivenAgent(Agent):
    def __init__(self, table):
        super().__init__()
        self.table = table
        self.percept_history = []

    def program(self, percept):
        self.percept_history.append(percept)
        # Convert list to tuple to use as dict key
        sequence = tuple(self.percept_history)
        return self.table.get(sequence, 'NoOp')
```

---

## Designing a Smart Vacuum (Reflex)

### Problem Statement

- **Environment:** A 2-location grid (A, B). Each square can be Dirty or Clean.
- **Actions:** Left, Right, Suck, NoOp.
- **Sensors:** Location (A/B), Status (Dirty/Clean).

### Implementation Logic

```python
def reflex_vacuum_program(percept):
    location, status = percept

    if status == 'Dirty':
        return 'Suck'
    elif location == 'A':
        return 'Right'
    elif location == 'B':
        return 'Left'
```

---

## Designing a Grid Navigator (Goal-Based)

### Problem Statement

- **Environment:** $N \times N$ Grid with obstacles.
- **Goal:** Reach $(N-1, N-1)$.
- **Mechanism:** The agent needs a **Model** of the world (the grid map) and a **Search Algorithm** (BFS/A\*) to plan the path.

### Implementation Logic

1.  **Update State:** Mark current position as visited.
2.  **Formulate Goal:** "Go to (GoalX, GoalY)".
3.  **Plan:** Run A\* to find sequence of moves.
4.  **Execute:** Return the first move in the sequence.

### Analysis: Hard-Coding vs Learning

- **Hard-Coded (Reflex):** Fast, but fails if the environment changes (e.g., if 'Right' is blocked).
- **Planning (Goal-Based):** Can adapt to obstacles dynamically but requires computation time.
