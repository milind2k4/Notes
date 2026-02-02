Links:

---

# Learning Agents

## Learning Agents: Characteristics and Architectures

### Concept: Evolving Intelligence

A **Learning Agent** is an agent that improves its performance over time through experience. Unlike a static reflex agent (which has fixed rules), a learning agent modifies its own logic.

**Components of a Learning Agent:**

1.  **Performance Element:** The part that actually chooses actions (the "agent" so far).
2.  **Critic:** Evaluates how well the agent is doing based on a fixed performance standard.
3.  **Learning Element:** Uses feedback from the Critic to modify the Performance Element.
4.  **Problem Generator:** Suggests actions that might lead to new and informative experiences (Exploration).

### Internals: Types of Learning

- **Supervised Learning:** Learning from labeled examples (Teacher says "This is a cat").
- **Unsupervised Learning:** Finding patterns in unlabeled data (Clustering).
- **Reinforcement Learning (RL):** Learning from rewards and punishments (Trial and error).

---

## Reinforcement Learning Fundamentals

### Concept: The Carrot and Stick

**Reinforcement Learning (RL)** is about learning what to do—how to map situations to actions—so as to maximize a numerical reward signal. The learner is not told which actions to take, but instead must discover which actions yield the most reward by trying them.

### Key Components (The MDP Framework)

RL problems are often modeled as **Markov Decision Processes (MDPs)**.

1.  **Agent:** The learner and decision maker.
2.  **Environment:** Everything the agent interacts with.
3.  **State ($S_t$):** The current situation at time $t$.
4.  **Action ($A_t$):** What the agent does.
5.  **Reward ($R_t$):** Immediate feedback from the environment (Scalar value).
6.  **Policy ($\pi$):** The strategy. A mapping from state to action ($\pi(s) \rightarrow a$).
7.  **Value Function ($V(s)$):** Expected long-term return from state $s$.

### The RL Loop

1.  Agent observes state $S_t$.
2.  Agent takes action $A_t$.
3.  Environment transitions to $S_{t+1}$ and gives reward $R_{t+1}$.
4.  Agent updates its knowledge.
5.  Repeat.

### Exploration vs. Exploitation

- **Exploitation:** Doing what you know yields reward (Greedy).
- **Exploration:** Trying new things to see if they are better.
- **Epsilon-Greedy Strategy:** With probability $\epsilon$, explore (random action); otherwise, exploit (best known action).
