import os
import time
import random

# Maze Constants
EMPTY = ' '
WALL = '#'
START = 'S'
GOAL = 'G'
AGENT = 'A'
VISITED = '.'

class MazeEnvironment:
    def __init__(self):
        # A simple maze
        self.grid = [
            ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
            ['#', 'S', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#'],
            ['#', '#', '#', ' ', '#', ' ', '#', '#', ' ', '#'],
            ['#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#'],
            ['#', ' ', '#', '#', '#', '#', ' ', '#', ' ', '#'],
            ['#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#'],
            ['#', '#', '#', '#', ' ', '#', '#', '#', ' ', '#'],
            ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
            ['#', '#', '#', '#', '#', '#', '#', '#', 'G', '#']
        ]
        self.agent_pos = (1, 1)
        self.goal_pos = (8, 8)
        self.rows = len(self.grid)
        self.cols = len(self.grid[0])
        self.facing = 'East' # North, East, South, West

    def get_percept(self):
        """
        Returns (WallAhead, WallLeft, WallRight)
        """
        r, c = self.agent_pos
        
        # Helper to get coords based on direction
        def get_coords(direction):
            if direction == 'North': return r-1, c
            if direction == 'East': return r, c+1
            if direction == 'South': return r+1, c
            if direction == 'West': return r, c-1
        
        # Determine directions relative to facing
        directions = ['North', 'East', 'South', 'West']
        idx = directions.index(self.facing)
        
        ahead = directions[idx]
        left = directions[(idx - 1) % 4]
        right = directions[(idx + 1) % 4]
        
        def is_wall(pos):
            nr, nc = pos
            if 0 <= nr < self.rows and 0 <= nc < self.cols:
                return self.grid[nr][nc] == WALL
            return True # Out of bounds is a wall

        return (is_wall(get_coords(ahead)), is_wall(get_coords(left)), is_wall(get_coords(right)))

    def move_forward(self):
        r, c = self.agent_pos
        if self.facing == 'North': nr, nc = r-1, c
        elif self.facing == 'East': nr, nc = r, c+1
        elif self.facing == 'South': nr, nc = r+1, c
        elif self.facing == 'West': nr, nc = r, c-1
        
        if self.grid[nr][nc] != WALL:
            self.agent_pos = (nr, nc)
            if self.grid[nr][nc] == EMPTY:
                self.grid[nr][nc] = VISITED
            return True
        return False

    def turn_left(self):
        dirs = ['North', 'East', 'South', 'West']
        self.facing = dirs[(dirs.index(self.facing) - 1) % 4]

    def turn_right(self):
        dirs = ['North', 'East', 'South', 'West']
        self.facing = dirs[(dirs.index(self.facing) + 1) % 4]

    def display(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for r in range(self.rows):
            line = ""
            for c in range(self.cols):
                if (r, c) == self.agent_pos:
                    # Arrow based on facing
                    if self.facing == 'North': char = '^'
                    elif self.facing == 'East': char = '>'
                    elif self.facing == 'South': char = 'v'
                    elif self.facing == 'West': char = '<'
                    line += char + " "
                else:
                    line += self.grid[r][c] + " "
            print(line)
        print(f"Facing: {self.facing}")

class ReflexMazeAgent:
    def __init__(self, env):
        self.env = env

    def act(self):
        # Right-Hand Rule (Wall Follower)
        # 1. If right is open, turn right and move.
        # 2. Else if ahead is open, move forward.
        # 3. Else turn left.
        
        wall_ahead, wall_left, wall_right = self.env.get_percept()
        
        if not wall_right:
            self.env.turn_right()
            self.env.move_forward()
        elif not wall_ahead:
            self.env.move_forward()
        else:
            self.env.turn_left()

if __name__ == "__main__":
    env = MazeEnvironment()
    agent = ReflexMazeAgent(env)
    
    steps = 0
    max_steps = 100
    
    while env.agent_pos != env.goal_pos and steps < max_steps:
        env.display()
        agent.act()
        time.sleep(0.2)
        steps += 1
    
    env.display()
    if env.agent_pos == env.goal_pos:
        print("Goal Reached!")
    else:
        print("Max steps reached or stuck.")
