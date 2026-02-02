import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import heapq

# 0 = Empty, 1 = Wall, 2 = Start, 3 = Goal, 4 = Path, 5 = Visited
EMPTY = 0
WALL = 1
START = 2
GOAL = 3
PATH = 4
VISITED = 5

class PathfindingVisualizer:
    def __init__(self, grid_size=20):
        self.size = grid_size
        self.grid = np.zeros((grid_size, grid_size))
        self.start = (2, 2)
        self.goal = (grid_size - 3, grid_size - 3)
        self.grid[self.start] = START
        self.grid[self.goal] = GOAL
        self.walls = self.generate_walls()
        
        self.visited_frames = []
        self.path_frames = []

    def generate_walls(self):
        # Simple random walls
        num_walls = int(self.size * self.size * 0.2)
        for _ in range(num_walls):
            r, c = np.random.randint(0, self.size, 2)
            if (r, c) != self.start and (r, c) != self.goal:
                self.grid[r, c] = WALL

    def heuristic(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def a_star(self):
        pq = []
        heapq.heappush(pq, (0, self.start))
        came_from = {}
        g_score = {self.start: 0}
        
        visited_order = []

        while pq:
            _, current = heapq.heappop(pq)
            visited_order.append(current)

            if current == self.goal:
                break

            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                neighbor = (current[0] + dr, current[1] + dc)
                
                if 0 <= neighbor[0] < self.size and 0 <= neighbor[1] < self.size:
                    if self.grid[neighbor] == WALL:
                        continue
                    
                    new_g = g_score[current] + 1
                    if neighbor not in g_score or new_g < g_score[neighbor]:
                        g_score[neighbor] = new_g
                        priority = new_g + self.heuristic(neighbor, self.goal)
                        heapq.heappush(pq, (priority, neighbor))
                        came_from[neighbor] = current
        
        # Reconstruct path
        path = []
        if self.goal in came_from:
            curr = self.goal
            while curr != self.start:
                path.append(curr)
                curr = came_from[curr]
            path.append(self.start)
            path.reverse()
        
        return visited_order, path

    def animate(self):
        visited_nodes, path_nodes = self.a_star()
        
        fig, ax = plt.subplots()
        cmap = plt.cm.colors.ListedColormap(['white', 'black', 'green', 'red', 'blue', 'yellow'])
        bounds = [0, 1, 2, 3, 4, 5, 6]
        norm = plt.cm.colors.BoundaryNorm(bounds, cmap.N)

        def update(frame):
            if frame < len(visited_nodes):
                node = visited_nodes[frame]
                if node != self.start and node != self.goal:
                    self.grid[node] = VISITED
            else:
                path_idx = frame - len(visited_nodes)
                if path_idx < len(path_nodes):
                    node = path_nodes[path_idx]
                    if node != self.start and node != self.goal:
                        self.grid[node] = PATH
            
            ax.clear()
            ax.imshow(self.grid, cmap=cmap, norm=norm)
            ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=1)
            ax.set_xticks(np.arange(-.5, self.size, 1))
            ax.set_yticks(np.arange(-.5, self.size, 1))
            ax.set_xticklabels([])
            ax.set_yticklabels([])
            ax.set_title(f"A* Search - Step {frame}")

        ani = animation.FuncAnimation(fig, update, frames=len(visited_nodes) + len(path_nodes), interval=50, repeat=False)
        plt.show()

if __name__ == "__main__":
    viz = PathfindingVisualizer()
    viz.animate()
