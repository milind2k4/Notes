import random
import time
import os

# Simulation Constants
LANES = ['North', 'South', 'East', 'West']
GREEN_DURATION = 5

class IntersectionAgent:
    def __init__(self, name):
        self.name = name
        self.queues = {lane: 0 for lane in LANES}
        self.current_green = 'North' # North/South or East/West
        self.timer = GREEN_DURATION
        self.total_wait_time = 0

    def step(self):
        # 1. Cars arrive randomly
        for lane in LANES:
            if random.random() < 0.3: # 30% chance of car arriving
                self.queues[lane] += 1

        # 2. Traffic Light Logic (Simple Adaptive)
        # If current green lane is empty and other lane has cars, switch early
        ns_cars = self.queues['North'] + self.queues['South']
        ew_cars = self.queues['East'] + self.queues['West']
        
        switched = False
        if self.timer <= 0:
            self.switch_lights()
            switched = True
        elif self.current_green == 'North' and ns_cars == 0 and ew_cars > 0:
            self.switch_lights()
            switched = True
        elif self.current_green == 'East' and ew_cars == 0 and ns_cars > 0:
            self.switch_lights()
            switched = True
        
        if not switched:
            self.timer -= 1

        # 3. Flow Traffic
        if self.current_green == 'North':
            if self.queues['North'] > 0: self.queues['North'] -= 1
            if self.queues['South'] > 0: self.queues['South'] -= 1
        else:
            if self.queues['East'] > 0: self.queues['East'] -= 1
            if self.queues['West'] > 0: self.queues['West'] -= 1

        # 4. Calculate Wait Time (Cost)
        current_wait = sum(self.queues.values())
        self.total_wait_time += current_wait

    def switch_lights(self):
        if self.current_green == 'North':
            self.current_green = 'East'
        else:
            self.current_green = 'North'
        self.timer = GREEN_DURATION

    def display(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Intersection: {self.name}")
        print(f"Total Wait Time (Cost): {self.total_wait_time}")
        print("-" * 20)
        
        # Visualizing the Intersection
        #       N
        #       |
        #   W --+-- E
        #       |
        #       S
        
        n_q = self.queues['North']
        s_q = self.queues['South']
        e_q = self.queues['East']
        w_q = self.queues['West']
        
        ns_light = "GREEN" if self.current_green == 'North' else "RED"
        ew_light = "GREEN" if self.current_green == 'East' else "RED"
        
        print(f"      N: {n_q} ({ns_light})")
        print(f"      |")
        print(f"W: {w_q} -+- E: {e_q} ({ew_light})")
        print(f"      |")
        print(f"      S: {s_q} ({ns_light})")
        print("-" * 20)

if __name__ == "__main__":
    agent = IntersectionAgent("Main St & 1st Ave")
    
    for _ in range(50):
        agent.step()
        agent.display()
        time.sleep(0.2)
