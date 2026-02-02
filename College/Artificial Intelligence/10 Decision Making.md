Links:

---

# Decision Making

## Markov Decision Processes (MDPs)

### Concept: Decision Making under Uncertainty

In simple search (A\*), actions are deterministic (Go North $\rightarrow$ You are North). In the real world, actions can fail (Go North $\rightarrow$ 10% chance you slip and stay put).
An **MDP** is a framework for decision making in stochastic environments where the outcome is partly random and partly under the control of a decision maker.

**Components (Tuple $<S, A, T, R, \gamma>$):**

1.  **States ($S$):** All possible situations the agent can be in.
2.  **Actions ($A$):** The set of choices available in each state.
3.  **Transition Model ($T(s, a, s')$):** The probability of reaching state $s'$ if we execute action $a$ in state $s$.
    - Notation: $P(s' | s, a)$
4.  **Reward Function ($R(s)$):** The immediate reward received for entering state $s$.
5.  **Discount Factor ($\gamma$):** A number between 0 and 1 that determines how much the agent cares about future rewards vs immediate rewards.
6.  **Policy ($\pi$):** The solution to an MDP. It is a map telling the agent what to do in every state ($\pi(s) \rightarrow a$).

### Internals: The Bellman Equation

The core idea is that the "Value" or "Utility" of a state is the immediate reward plus the discounted expected value of the next state.

$$ V(s) = R(s) + \gamma \max*{a} \sum*{s'} T(s, a, s') V(s') $$

- **R(s):** Reward for current state.
- **$\gamma$:** Discount factor.
- **$\max_a$:** We assume the agent will choose the best action.
- **$\sum_{s'}$:** Evaluation of all possible outcomes weighted by their probability.

---

### Exam-Style Example: Solving an MDP Step-by-Step

**Question:**
Consider a robot in a simple world.

- Current State: A
- Possible Actions: Move Right
- Outcomes of Move Right:
  - 80% chance to reach State B (Value $V(B) = 10$).
  - 20% chance to reach State C (Value $V(C) = 5$).
- Reward for being in State A: $R(A) = -1$ (Cost of living).
- Discount Factor $\gamma = 0.9$.
- **Calculate the Utility of State A, $V(A)$.**

**Solution steps that you would write in an exam:**

**Step 1: Write down the Bellman Equation formula.**
$V(s) = R(s) + \gamma \sum T(s, a, s') V(s')$
_(Note: Since there is only one action "Move Right", we don't need the `max` operator)._

**Step 2: Substitute the known values.**

- $s = A$
- $R(A) = -1$
- $\gamma = 0.9$
- Transition 1: $T(A, Right, B) = 0.8$, $V(B) = 10$
- Transition 2: $T(A, Right, C) = 0.2$, $V(C) = 5$

**Step 3: Perform the calculation.**

$$
\begin{aligned}
V(A) &= -1 + 0.9 \times [ (0.8 \times 10) + (0.2 \times 5) ] \\
V(A) &= -1 + 0.9 \times [ 8 + 1 ] \\
V(A) &= -1 + 0.9 \times [ 9 ] \\
V(A) &= -1 + 8.1 \\
V(A) &= 7.1
\end{aligned}
$$

**Answer:** The Utility of State A is **7.1**.

---

## Game Theory

### Concept: Strategic Decision Making

When multiple agents compete, my outcome depends on _your_ move. This is the study of strategic interaction.

- **Zero-Sum Game:** My win is your loss (Chess, Poker). Total utility sum is constant (0).
- **General-Sum Game:** Win-Win or Lose-Lose is possible (Prisoner's Dilemma, Trade).

### Nash Equilibrium

A situation where **no player has an incentive to deviate** from their chosen strategy after considering an opponent's choice. It is a "stable" state of the game.

---

### Exam-Style Example: Finding Nash Equilibrium

**Question:**
Consider the "Prisoner's Dilemma" represented by likely jail time (years). The payoff matrix is below. Find the Nash Equilibrium.

| Player A \ Player B | Confess (Defect) | Remain Silent (Cooperate) |
| :------------------ | :--------------- | :------------------------ |
| **Confess**         | (-5, -5)         | (0, -10)                  |
| **Silent**          | (-10, 0)         | (-1, -1)                  |

_(Notation: (A's payoff, B's payoff). Higher numbers are better, so 0 > -5)._

**Solution steps:**

**Step 1: Analyze Player A's best moves.**

- If B chooses **Confess**: A can choose Confess (-5) or Silent (-10). $\rightarrow$ **A chooses Confess.**
- If B chooses **Silent**: A can choose Confess (0) or Silent (-1). $\rightarrow$ **A chooses Confess.**
- _Conclusion:_ A has a **Dominant Strategy** to Confess.

**Step 2: Analyze Player B's best moves.**

- If A chooses **Confess**: B can choose Confess (-5) or Silent (-10). $\rightarrow$ **B chooses Confess.**
- If A chooses **Silent**: B can choose Confess (0) or Silent (-1). $\rightarrow$ **B chooses Confess.**
- _Conclusion:_ B has a **Dominant Strategy** to Confess.

**Step 3: Identify the Equilibrium.**
The cell where both players' best responses intersect is likely the Nash Equilibrium.

- A chooses Confess AND B chooses Confess.
- The State is **(Confess, Confess)** with payoff (-5, -5).

**Step 4: Verify Stability.**

- In (Confess, Confess):
  - Can A improve by switching to Silent? No (-5 $\rightarrow$ -10).
  - Can B improve by switching to Silent? No (-5 $\rightarrow$ -10).
- Therefore, **(Confess, Confess) is the Nash Equilibrium.**

---

## Rule-Based Decision Logic

### Concept: Expert Systems Redux

For simpler domains, we don't need complex math. We can use **Production Rules**.

**Structure:**

- **Working Memory:** Current facts (e.g., `Temp = 40C`).
- **Rule Base:** `IF-THEN` logic.
- **Inference Engine:** Matches facts to rules to fire actions.

### Example: Thermostat Logic

```python
rules = [
    {"if": lambda s: s['temp'] < 18, "then": "Turn Heater On"},
    {"if": lambda s: s['temp'] > 24, "then": "Turn AC On"},
    {"if": lambda s: 18 <= s['temp'] <= 24, "then": "Idle"}
]

state = {'temp': 26}
for rule in rules:
    if rule['if'](state):
        print(rule['then']) # Output: Turn AC On
```

### Analysis: MDP vs Rules

| Feature             | MDP                              | Rule-Based              |
| :------------------ | :------------------------------- | :---------------------- |
| **Environment**     | Stochastic (Uncertain)           | Deterministic (Certain) |
| **Complexity**      | High (Solves for optimal policy) | Low (Simple logic)      |
| **Maintainability** | Hard (Math heavy)                | Easy (Add new rules)    |
