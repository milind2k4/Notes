Links:

---

# Multi-Agent Learning

## Cooperative and Competitive Agents

### Concept: Friends and Foes

In **Multi-Agent Reinforcement Learning (MARL)**, the environment is non-stationary because other agents are changing their policies simultaneously.

1.  **Cooperative:** Agents share a common goal.
    - _Example:_ Warehouse robots moving packages without colliding.
    - _Challenge:_ **Credit Assignment Problem**. If the team wins, which agent contributed the most?
2.  **Competitive:** Zero-sum games.
    - _Example:_ AlphaGo vs. Lee Sedol.
    - _Challenge:_ Opponent modeling. I need to predict what _you_ will do.

---

## Traffic Control Simulation

### Problem: The Gridlock

Traditional traffic lights use fixed timers. Smart traffic control uses MARL.

### MAS Solution

- **Agents:** Each intersection is an agent.
- **State:** Number of cars waiting in each lane.
- **Action:** Switch Light Green/Red.
- **Reward:** -1 for every second a car waits (Minimize total wait time).

**Coordination:**

- Independent Q-Learning (IQL): Each intersection ignores others (treats them as part of the environment). Simple but unstable.
- Joint Action Learning: Agents share information (e.g., "I am sending 50 cars your way").

---

## RL in Multi-Agent Scenarios

### Challenges

1.  **Non-Stationarity:** Since everyone is learning, the "best" strategy keeps changing.
2.  **Scalability:** The joint state space grows exponentially with the number of agents.

### Approaches

1.  **Centralized Training, Decentralized Execution (CTDE):**
    - During training, a central "God" critic sees everything and guides the agents.
    - During execution, agents act alone based on their local view.
2.  **Parameter Sharing:** All agents share the same Neural Network weights (if they are homogeneous), speeding up learning.
