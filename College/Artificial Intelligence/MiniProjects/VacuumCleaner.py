import random
import time

class Environment:
    def __init__(self):
        # A and B are the two locations
        # 0 = Clean, 1 = Dirty
        self.locationCondition = {'A': '0', 'B': '0'}
        
        # Randomly dirty the environment initially
        self.locationCondition['A'] = random.choice(['0', '1'])
        self.locationCondition['B'] = random.choice(['0', '1'])

class SimpleReflexVacuumAgent(Environment):
    def __init__(self, Environment):
        self.env = Environment
        self.vacuumLocation = random.choice(['A', 'B'])
        self.score = 0

    def perceive(self):
        return self.vacuumLocation, self.env.locationCondition[self.vacuumLocation]

    def act(self):
        location, status = self.perceive()
        print(f"Vacuum is at {location}. Status: {'Dirty' if status == '1' else 'Clean'}")
        
        if status == '1':
            print("Action: Suck")
            self.env.locationCondition[location] = '0'
            self.score += 1
            print(f"Location {location} is now Clean.")
        elif location == 'A':
            print("Action: Move Right")
            self.vacuumLocation = 'B'
        elif location == 'B':
            print("Action: Move Left")
            self.vacuumLocation = 'A'
        
        print("-" * 20)

    def run(self, steps=5):
        print("Starting Vacuum Simulation...")
        print(f"Initial State: {self.env.locationCondition}")
        for _ in range(steps):
            self.act()
            time.sleep(0.5)
        print(f"Simulation Ended. Final Score: {self.score}")
        print(f"Final State: {self.env.locationCondition}")

if __name__ == "__main__":
    env = Environment()
    agent = SimpleReflexVacuumAgent(env)
    agent.run(10)
