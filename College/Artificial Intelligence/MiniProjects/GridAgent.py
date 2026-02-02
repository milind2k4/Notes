import heapq
import random
import time
import os

# Grid Constants
EMPTY = 0
OBSTACLE = 1
START = 2
GOAL = 3
AGENT = 4
PATH = 5

class GridEnvironment:
    def __init__(self, size=10, obstacle_prob=0.2):
        self.size = size
        self.grid = [[EMPTY for _ in range(size)] for _ in range(size)]
        self.start = (0, 0)
        self.goal = (size-1, size-1)
        self.agent_pos = self.start
        
        # Generate Obstacles
        for r in range(size):
            for c in range(size):
                if (r, c) != self.start and (r, c) != self.goal and random.random() < obstacle_prob:
                    self.grid[r][c] = OBSTACLE

    def display(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Agent Position: {self.agent_pos}")
        for r in range(self.size):
            line = ""
            for c in range(self.size):
                if (r, c) == self.agent_pos:
                    line += "A "
                elif (r, c) == self.goal:
                    line += "G "
                elif self.grid[r][c] == OBSTACLE:
                    line += "# "
                elif self.grid[r][c] == PATH:
                    line += ". "
                else:
                    line += "  "
            print(line)
        print("-" * 20)

class GoalBasedAgent:
    def __init__(self, env):
        self.env = env
        self.plan = [] # Queue of moves

    def heuristic(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def formulate_plan(self):
        """Uses A* Search to find a path to the goal."""
        start = self.env.agent_pos
        goal = self.env.goal
        
        pq = []
        heapq.heappush(pq, (0, start))
        came_from = {}
        g_score = {start: 0}
        
        while pq:
            _, current = heapq.heappop(pq)
            
            if current == goal:
                break
            
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                neighbor = (current[0] + dr, current[1] + dc)
                
                if 0 <= neighbor[0] < self.env.size and 0 <= neighbor[1] < self.env.size:
                    if self.env.grid[neighbor[0]][neighbor[1]] == OBSTACLE:
                        continue
                        
                    new_g = g_score[current] + 1
                    if neighbor not in g_score or new_g < g_score[neighbor]:
                        g_score[neighbor] = new_g
                        priority = new_g + self.heuristic(neighbor, goal)
                        heapq.heappush(pq, (priority, neighbor))
                        came_from[neighbor] = current
        
        # Reconstruct path
        path = []
        if goal in came_from:
            curr = goal
            while curr != start:
                path.append(curr)
                curr = came_from[curr]
            path.reverse()
        
        self.plan = path
        if not self.plan:
            print("No path found!")

    def act(self):
        if not self.plan:
            self.formulate_plan()
            if not self.plan: return False # Stuck
        
        next_pos = self.plan.pop(0)
        self.env.agent_pos = next_pos
        self.env.grid[next_pos[0]][next_pos[1]] = PATH # Mark trail
        return True

if __name__ == "__main__":
    env = GridEnvironment(size=10)
    agent = GoalBasedAgent(env)
    
    env.display()
    time.sleep(1)
    
    while env.agent_pos != env.goal:
        success = agent.act()
        env.display()
        if not success:
            print("Agent is stuck.")
            break
        time.sleep(0.3)
    
    if env.agent_pos == env.goal:
        print("Goal Reached!")
