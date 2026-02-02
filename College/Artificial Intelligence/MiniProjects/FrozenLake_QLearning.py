import numpy as np
import random
import time
import os

# Environment Constants
LAKE = [
    "SFFF",
    "FHFH",
    "FFFH",
    "HFFG"
]
# S: Start, F: Frozen, H: Hole, G: Goal
ACTIONS = ['Left', 'Down', 'Right', 'Up']

class FrozenLakeEnv:
    def __init__(self):
        self.rows = 4
        self.cols = 4
        self.state = (0, 0)
        self.grid = LAKE

    def reset(self):
        self.state = (0, 0)
        return 0 # State index

    def step(self, action):
        # 0: Left, 1: Down, 2: Right, 3: Up
        r, c = self.state
        if action == 0: c = max(0, c - 1)
        elif action == 1: r = min(self.rows - 1, r + 1)
        elif action == 2: c = min(self.cols - 1, c + 1)
        elif action == 3: r = max(0, r - 1)
        
        self.state = (r, c)
        cell = self.grid[r][c]
        
        reward = 0
        done = False
        
        if cell == 'G':
            reward = 1
            done = True
        elif cell == 'H':
            reward = 0
            done = True
        
        return r * 4 + c, reward, done

class QLearningAgent:
    def __init__(self, states, actions):
        self.q_table = np.zeros((states, actions))
        self.lr = 0.8
        self.gamma = 0.95
        self.epsilon = 0.1

    def choose_action(self, state):
        if random.uniform(0, 1) < self.epsilon:
            return random.randint(0, 3) # Explore
        else:
            return np.argmax(self.q_table[state, :]) # Exploit

    def learn(self, state, action, reward, next_state):
        predict = self.q_table[state, action]
        target = reward + self.gamma * np.max(self.q_table[next_state, :])
        self.q_table[state, action] += self.lr * (target - predict)

if __name__ == "__main__":
    env = FrozenLakeEnv()
    agent = QLearningAgent(16, 4)
    
    print("Training...")
    for episode in range(1000):
        state = env.reset()
        done = False
        while not done:
            action = agent.choose_action(state)
            next_state, reward, done = env.step(action)
            agent.learn(state, action, reward, next_state)
            state = next_state

    print("Training Complete. Showing solution...")
    state = env.reset()
    done = False
    path = [(0,0)]
    
    while not done:
        action = np.argmax(agent.q_table[state, :])
        next_state, reward, done = env.step(action)
        state = next_state
        r, c = state // 4, state % 4
        path.append((r, c))
        
        # Visualization
        os.system('cls' if os.name == 'nt' else 'clear')
        for i in range(4):
            line = ""
            for j in range(4):
                if (i, j) == (r, c): line += "A "
                else: line += env.grid[i][j] + " "
            print(line)
        time.sleep(0.5)
    
    if reward == 1: print("Goal Reached!")
    else: print("Fell in a Hole!")
