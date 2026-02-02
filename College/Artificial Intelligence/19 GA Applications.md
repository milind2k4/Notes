Links:

---

# GA Applications

## Practical Applications of Genetic Algorithms

Genetic Algorithms are best suited for **Combinatorial Optimization Problems** where the search space is too large for brute force and the landscape is too rugged for gradient-based methods. Below are detailed expansions of four key application areas.

---

### 1. Traveling Salesman Problem (TSP)

**The Problem:**
Given a set of $N$ cities and the distances between each pair, find the shortest Hamiltonian Cycle (a route that visits every city exactly once and returns to the start).

- **Complexity:** The search space size is $(N-1)!/2$. For just 20 cities, that is $6 \times 10^{16}$ possible routes. This is an NP-Hard problem.

**GA Implementation Details:**

1.  **Representation (Encoding):**

    - **Path Representation (Permutation):** A logic list of city IDs.
    - _Chromosome:_ `[A, C, E, B, D]` (Order matters).
    - _Constraint:_ No duplicates allowed. All cities must be present.

2.  **Crossover Operators (Crucial):**

    - Standard single-point crossover fails because it creates invalid tours with duplicates and missing cities.
    - **PMX (Partially Mapped Crossover):**
      1.  Select a subsection of Parent 1. `P1: [1 2 | 3 4 5 | 6 7]`.
      2.  Copy to Child. `C: [x x | 3 4 5 | x x]`.
      3.  Look at the corresponding section in Parent 2. `P2: [5 4 | 6 7 2 | 1 3]`. The subsection is `[6 7 2]`.
      4.  Map the values `6, 7, 2` to the child, ensuring no conflicts by looking at the P1 $\leftrightarrow$ P2 mapping relations.
    - **OX (Order Crossover):** Preserves the relative order of cities from one parent.

3.  **Mutation Operators:**

    - **Swap Mutation:** Select two random positions and swap them. `[A, B, C, D] -> [A, D, C, B]`.
    - **Inversion Mutation (Better):** Select a sub-tour and reverse it. `[A, B, C, D, E] -> [A, D, C, B, E]` (Reversed B-C-D). This essentially "untangles" crossing paths in geometric space.

4.  **Fitness Function:**
    $$ Fitness = \frac{1}{\sum*{i=0}^{N-1} distance(City_i, City*{i+1})} $$
    - (Where $City_N$ wraps around to $City_0$).

**Real-World Example:**

- **Logistics:** UPS/FedEx route planning.
- **PCB Drilling:** A machine must drill 10,000 holes on a circuit board. The "Head" must move between holes. Minimizing travel time = Minimizing distance.

---

### 2. Feature Selection in Machine Learning

**The Problem:**
In High-Dimensional datasets (e.g., DNA Microarray data with 20,000 genes/features but only 50 patients), most features are noise. Using all of them leads to overfitting and slow training. We need the "Optimal Subset" of features.

**GA Implementation Details:**

1.  **Representation (Encoding):**

    - **Binary Encoding:** A bit string of length $D$ (Total dimensions).
    - _Chromosome:_ `1001000...1`.
    - $1$: Feature is active (fed to model).
    - $0$: Feature is masked (ignored).

2.  **Wrapper Method Approach:**

    - The GA "wraps" around a predictive model (e.g., Support Vector Machine, Decision Tree).
    - **Step 1:** GA generates a binary mask.
    - **Step 2:** Filter the dataset to keep only columns with `1`.
    - **Step 3:** Train the model (using Cross-Validation).
    - **Step 4:** Return the Validation Accuracy as Fitness.

3.  **Fitness Function (Multi-Objective):**
    Simple accuracy isn't enough; we want sparse models (few features).
    $$ Fitness = w_1 \times Accuracy - w_2 \times (\frac{\text{Count}(1s)}{\text{Total Features}}) $$

    - $w_1$: Weight for accuracy (e.g., 0.9).
    - $w_2$: Weight for parsimony/simplicity (e.g., 0.1).

4.  **Advanced Operator:**
    - **Mutation:** A bit flip `0 -> 1` adds a feature; `1 -> 0` removes one.
    - Sometimes initialization is biased towards `0` (Sparse initialization) to start with smaller subsets.

**Example:**

- **Cancer Diagnosis:** Identifying which 5 genes out of 20,000 are responsible for a tumor type. The GA finds the 5-gene signature that best predicts the outcome.

---

### 3. Scheduling (Job Shop Scheduling)

**The Problem:**
We have $J$ Jobs and $M$ Machines. Each job typically consists of a sequence of operations (e.g., Cut -> Paint -> Dry) that must happen in order. Each operation requires a specific machine for a specific duration. The goal is to minimize the **Makespan** (Total time to finish everything).

**GA Implementation Details:**

1.  **Representation (Direct vs Interpretive):**

    - **Operation-Based Representation:** A permutation with repetitions.
    - If Job 1 has 3 operations ($O_{1,1}, O_{1,2}, O_{1,3}$) and Job 2 has 2 ($O_{2,1}, O_{2,2}$).
    - Chromosome: `[1, 2, 1, 2, 1]`
      - First `1`: Schedule $O_{1,1}$.
      - First `2`: Schedule $O_{2,1}$.
      - Second `1`: Schedule $O_{1,2}$.
    - This ensures topological precedence (Operation 2 of Job 1 is never scheduled before Operation 1).

2.  **Decoding (The Scheduler):**

    - The GA only provides the _sequence_. A "Scheduler" algorithm (like a greedy builder) actually places the tasks on the Gantt Chart, respecting machine availability.

3.  **Fitness Function:**

    - Calculate the completion time of the very last task on the Gantt Chart.
    - $Fitness = \frac{1}{\text{Makespan}}$.

4.  **Handling Constraints:**
    - **Hard Constraints:** Overlap (Two jobs on Machine A at same time). Handled by the Decoder (it purely puts them in sequence).
    - **Soft Constraints:** Due Dates (Job 1 must finish by 5 PM). Handled by Penalty:
      $$ Cost = \text{Makespan} + \sum (\text{Lateness of Job}\_i \times \text{Penalty}) $$

**Example:**

- **University Timetabling:** Assigning (Course, Prof, Room) tuples to (Day, Time) slots. Conflicts (Prof being in two places) are heavily penalized in the fitness function.

---

### 4. Autonomous Route Planning (UAVs / Drones)

**The Problem:**
A drone must fly from Source ($S$) to Target ($T$) in a 3D city environment. It must avoid static obstacles (buildings), dynamic obstacles (other drones), and minimize battery usage (path length).

**GA Implementation Details:**

1.  **Representation:**

    - **Variable-Length Real-Valued Encoding:** A list of 3D coordinates (Waypoints) between Start and End.
    - Chromosome: $[P_1, P_2, P_3, ... P_k]$ where $P_i = (x, y, z)$.
    - Start and End are fixed. The GA evolves the intermediate points.

2.  **Operators:**

    - **Mutation:**
      - _Perturb:_ Move a point slightly $(x+\Delta, y+\Delta)$.
      - _Insert:_ Add a new waypoint to navigate around a complex obstacle.
      - _Delete:_ Remove a waypoint to smooth the path.
    - **Crossover:** Splice two paths. Take the first half of Path A and connect it to the second half of Path B (geometry must be handled carefully).

3.  **Fitness Function (Weighted Sum):**
    $$ F = w_d \cdot \text{Dist} + w_s \cdot \text{Smooth} + w_c \cdot \text{Clearance} $$

    - **Distance:** $\sum |P_i - P_{i+1}|$.
    - **Smoothness:** Sum of angles between segments (sharp turns consume energy).
    - **Clearance (Safety):** If the line segment $P_i \rightarrow P_{i+1}$ intersects a building, add a massive penalty (e.g., +10,000).

4.  **Smoothing:**
    - The GA produces jagged linear segments. In post-processing (or inside the fitness evaluation), these points are treated as Control Points for a **B-Spline** or **Bezier Curve** to generate a flyable trajectory.

**Example:**

- **Search and Rescue:** A swarm of drones evolving paths to cover a search area maxmially while maintaining communication range with the base station.
