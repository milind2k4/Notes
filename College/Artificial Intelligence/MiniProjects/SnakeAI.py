import random
import time
import os
import numpy as np

# Constants
WIDTH = 10
HEIGHT = 10
EMPTY = 0
SNAKE = 1
FOOD = 2

class SnakeEnv:
    def __init__(self):
        self.reset()

    def reset(self):
        self.snake = [(5, 5), (5, 4), (5, 3)]
        self.food = self._place_food()
        self.score = 0
        self.done = False
        return self._get_state()

    def _place_food(self):
        while True:
            food = (random.randint(0, HEIGHT-1), random.randint(0, WIDTH-1))
            if food not in self.snake:
                return food

    def _get_state(self):
        # Simplified state: Head pos, Food pos
        head = self.snake[0]
        return head + self.food

    def step(self, action):
        # 0: Up, 1: Right, 2: Down, 3: Left
        head = self.snake[0]
        dr, dc = [(-1, 0), (0, 1), (1, 0), (0, -1)][action]
        new_head = (head[0] + dr, head[1] + dc)

        # Check collisions
        if (not (0 <= new_head[0] < HEIGHT and 0 <= new_head[1] < WIDTH)) or (new_head in self.snake):
            self.done = True
            return self._get_state(), -10, True

        self.snake.insert(0, new_head)
        
        reward = 0
        if new_head == self.food:
            self.score += 1
            reward = 10
            self.food = self._place_food()
        else:
            self.snake.pop()
            # Shaped reward: Distance to food
            dist_old = abs(head[0]-self.food[0]) + abs(head[1]-self.food[1])
            dist_new = abs(new_head[0]-self.food[0]) + abs(new_head[1]-self.food[1])
            if dist_new < dist_old: reward = 1
            else: reward = -1

        return self._get_state(), reward, False

    def render(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        grid = [[' ' for _ in range(WIDTH)] for _ in range(HEIGHT)]
        for r, c in self.snake: grid[r][c] = 'O'
        fr, fc = self.food
        grid[fr][fc] = 'X'
        
        print(f"Score: {self.score}")
        print('#' * (WIDTH + 2))
        for row in grid:
            print('#' + ''.join(row) + '#')
        print('#' * (WIDTH + 2))

# Simple Rule-Based AI (Mocking a trained agent for demo)
def get_best_action(env):
    head = env.snake[0]
    food = env.food
    
    # Simple logic: Move towards food
    if head[0] > food[0]: return 0 # Up
    if head[0] < food[0]: return 2 # Down
    if head[1] > food[1]: return 3 # Left
    if head[1] < food[1]: return 1 # Right
    return 0

if __name__ == "__main__":
    env = SnakeEnv()
    
    while not env.done:
        env.render()
        action = get_best_action(env)
        env.step(action)
        time.sleep(0.2)
    
    print("Game Over!")
