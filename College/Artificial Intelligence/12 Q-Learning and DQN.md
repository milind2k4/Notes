Links:

---

# Q-Learning and DQN

## Introduction to OpenAI Gym

### Concept: The Playground

**OpenAI Gym** (now maintained as Gymnasium) is a standard API for reinforcement learning environments. It provides a consistent interface for agents to interact with various worlds (CartPole, LunarLander, Atari games).

**Standard Loop:**

```python
import gymnasium as gym
env = gym.make("FrozenLake-v1")
observation, info = env.reset()

for _ in range(1000):
    action = env.action_space.sample()  # Random action
    observation, reward, terminated, truncated, info = env.step(action)
    if terminated or truncated:
        observation, info = env.reset()
env.close()
```

---

## Q-Learning

### Concept: Learning the Quality

**Q-Learning** is a model-free RL algorithm. It learns a **Q-Function** $Q(s, a)$, which estimates the **Quality** (expected future reward) of taking action $a$ in state $s$.

### Internals: The Bellman Update

The core of Q-Learning is the update rule:
$$ Q(s, a) \leftarrow Q(s, a) + \alpha [R + \gamma \max_{a'} Q(s', a') - Q(s, a)] $$

- $Q(s, a)$: Current Q-value.
- $\alpha$: Learning rate (how fast we forget old info).
- $R$: Immediate reward.
- $\gamma$: Discount factor.
- $\max_{a'} Q(s', a')$: Best possible future value from the next state.

### Implementation: The Q-Table

For small state spaces (like a grid), we store Q-values in a table (Rows=States, Cols=Actions).

1.  Initialize Q-Table with zeros.
2.  Interact with env.
3.  Update table entry using the formula.

---

## Deep Q-Networks (DQN)

### Concept: Going Deep

When the state space is huge (e.g., pixels of a video game), a table is impossible. **DQN** uses a **Deep Neural Network** to approximate the Q-function: $Q(s, a; \theta) \approx Q^*(s, a)$.

### Architecture

- **Input:** State (e.g., image frames).
- **Hidden Layers:** Convolutional layers (for images) or Dense layers.
- **Output:** Q-values for each possible action.

### Training Stability Tricks

1.  **Experience Replay:** Store transitions $(s, a, r, s')$ in a buffer and train on random batches. Breaks correlation between consecutive steps.
2.  **Target Network:** Use a separate, slowly updating network to calculate the target value ($R + \gamma \max Q_{target}$). Prevents the "chasing your own tail" instability.

---

## Visualizing Learning Progress

### Metrics

1.  **Episode Reward:** Total reward per game. Should go up.
2.  **Episode Length:** Steps taken. Should go down (for goal-based tasks) or up (for survival tasks).
3.  **Loss:** Error in Q-value prediction. Should go down.

### Tools

- **Matplotlib:** Plot Reward vs. Episode.
- **TensorBoard:** Live tracking of metrics during training.
