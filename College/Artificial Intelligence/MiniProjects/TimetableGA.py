import random
import copy
import os
import time

# Constants
POPULATION_SIZE = 50
GENERATIONS = 100
MUTATION_RATE = 0.1
ELITISM_COUNT = 2

# Problem Data
COURSES = ['AI', 'Networks', 'Security', 'Cloud', 'DevOps']
PROFESSORS = ['Prof. A', 'Prof. B', 'Prof. C', 'Prof. D', 'Prof. E']
ROOMS = ['R101', 'R102', 'R103']
TIMESLOTS = ['9-10', '10-11', '11-12', '12-1', '2-3']
DAYS = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']

# Gene: (Course, Prof, Room, Day, Time)
class Schedule:
    def __init__(self):
        self.genes = []
        self.fitness = 0
        
    def generate_random(self):
        self.genes = []
        for course in COURSES:
            gene = {
                'Course': course,
                'Prof': random.choice(PROFESSORS),
                'Room': random.choice(ROOMS),
                'Day': random.choice(DAYS),
                'Time': random.choice(TIMESLOTS)
            }
            self.genes.append(gene)
            
    def calculate_fitness(self):
        conflicts = 0
        
        # Hard Constraints
        # 1. Room Conflict: Two classes in same room at same time
        # 2. Prof Conflict: One prof teaching two classes at same time
        
        for i in range(len(self.genes)):
            for j in range(i + 1, len(self.genes)):
                g1 = self.genes[i]
                g2 = self.genes[j]
                
                if g1['Day'] == g2['Day'] and g1['Time'] == g2['Time']:
                    if g1['Room'] == g2['Room']:
                        conflicts += 1
                    if g1['Prof'] == g2['Prof']:
                        conflicts += 1
                        
        self.fitness = 1 / (1 + conflicts)
        return self.fitness

def crossover(p1, p2):
    child = Schedule()
    mid = len(p1.genes) // 2
    child.genes = p1.genes[:mid] + p2.genes[mid:]
    return child

def mutate(schedule):
    if random.random() < MUTATION_RATE:
        idx = random.randint(0, len(schedule.genes) - 1)
        # Mutate one attribute
        attr = random.choice(['Room', 'Day', 'Time', 'Prof'])
        if attr == 'Room': schedule.genes[idx]['Room'] = random.choice(ROOMS)
        elif attr == 'Day': schedule.genes[idx]['Day'] = random.choice(DAYS)
        elif attr == 'Time': schedule.genes[idx]['Time'] = random.choice(TIMESLOTS)
        elif attr == 'Prof': schedule.genes[idx]['Prof'] = random.choice(PROFESSORS)

def run_ga():
    # 1. Init
    population = []
    for _ in range(POPULATION_SIZE):
        s = Schedule()
        s.generate_random()
        s.calculate_fitness()
        population.append(s)
        
    for gen in range(GENERATIONS):
        # Sort by fitness
        population.sort(key=lambda x: x.fitness, reverse=True)
        
        if population[0].fitness == 1.0:
            print(f"Solution found in Gen {gen}!")
            break
            
        # Elitism
        new_pop = population[:ELITISM_COUNT]
        
        # Selection & Crossover
        while len(new_pop) < POPULATION_SIZE:
            parent1 = random.choice(population[:10]) # Top 10 selection
            parent2 = random.choice(population[:10])
            child = crossover(parent1, parent2)
            mutate(child)
            child.calculate_fitness()
            new_pop.append(child)
            
        population = new_pop
        print(f"Gen {gen}: Best Fitness = {population[0].fitness:.4f}")

    # Display Best
    best = population[0]
    print("\nOptimal Timetable:")
    print(f"{'Day':<5} | {'Time':<6} | {'Course':<10} | {'Prof':<10} | {'Room':<5}")
    print("-" * 50)
    for g in best.genes:
        print(f"{g['Day']:<5} | {g['Time']:<6} | {g['Course']:<10} | {g['Prof']:<10} | {g['Room']:<5}")

if __name__ == "__main__":
    run_ga()
