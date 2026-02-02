Links:

---

# Game AI

## Agentic AI for Games and Simulation

### Concept: Beyond NPCs

Traditional Game AI (NPCs) uses **Finite State Machines (FSMs)** or **Behavior Trees** (e.g., "If player close, attack; else patrol").
**Agentic AI** uses **Reinforcement Learning** to _learn_ how to play. The agent isn't told _how_ to win, just _what_ winning looks like.

### Case Study: Self-Learning Bot

Imagine a bot learning to play a platformer (like Mario).

- **Input:** Screen pixels.
- **Output:** Buttons (Jump, Run, Left, Right).
- **Goal:** Reach the flag.

---

## Reward Shaping and Environment Design

### Concept: The Art of Teaching

If you only give a reward when the agent wins the game (Sparse Reward), it might never win by random chance, so it learns nothing.
**Reward Shaping** involves giving intermediate rewards to guide the agent.

### Example: Snake Game

- **Bad Reward:** +1 only when eating an apple. (Agent wanders aimlessly for too long).
- **Shaped Reward:**
  - +10 for eating apple.
  - -10 for hitting wall (Death).
  - -0.1 per step (Penalty for wasting time).
  - +0.1 if getting closer to apple (Distance heuristic).

**Risk:** **Reward Hacking**. The agent might find a loophole.

- _Example:_ If you reward "staying alive" in Tetris, the agent might pause the game forever.

---

## Developing AI Agents (Snake / Flappy Bird)

### Snake AI Architecture

1.  **State Representation:**
    - Is there danger ahead/left/right? (3 bools)
    - Is food up/down/left/right? (4 bools)
    - Current Direction.
2.  **Action Space:** [Straight, Left, Right].
3.  **Algorithm:** Deep Q-Learning (DQN).
    - Input: State vector (size 11).
    - Hidden Layers: Dense (Linear -> ReLU -> Linear).
    - Output: Q-values for 3 actions.

### Training Process

1.  **Initialize:** Random weights.
2.  **Play:** Agent plays thousands of games.
3.  **Learn:**
    - Store moves in memory.
    - Sample a batch.
    - Calculate Loss $(Q_{pred} - Q_{target})^2$.
    - Backpropagate to update weights.
4.  **Result:** An agent that can play indefinitely without dying.
