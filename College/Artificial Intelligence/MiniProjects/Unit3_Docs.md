Links:

---

# Unit 3 Mini-Projects Documentation

## 1. Frozen Lake Q-Learning

### Overview

Solves the "Frozen Lake" environment where an agent must cross a slippery grid to reach a goal without falling into holes.

### Algorithm

- **Q-Learning:** Updates a Q-Table based on rewards.
- **Exploration:** Epsilon-Greedy strategy.

### How to Run

```bash
python "MiniProjects/FrozenLake_QLearning.py"
```

---

## 2. Snake AI Agent

### Overview

A simplified simulation of an agent learning to play Snake.

### Logic

- **State:** Head position relative to food.
- **Reward:** Positive for eating, negative for dying or moving away from food.
- **Note:** The provided code uses a rule-based heuristic to demonstrate the _behavior_ of a trained agent, as training a full DQN takes hours.

### How to Run

```bash
python "MiniProjects/SnakeAI.py"
```

---

## 3. Traffic Control Simulation

### Overview

Simulates an intelligent traffic light agent at an intersection.

### Logic

- **Adaptive Control:** Switches lights not just on a timer, but based on queue lengths.
- **Goal:** Minimize total waiting time for all cars.

### How to Run

```bash
python "MiniProjects/TrafficControl.py"
```
