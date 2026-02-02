Links:
___
# CSPs

## Constraint Satisfaction Problems (CSPs)

A **Constraint Satisfaction Problem (CSP)** is a mathematical problem defined as a set of objects whose state must satisfy a number of constraints or limitations. Unlike standard search (which cares about the _path_), CSPs only care about the **goal state**.

**Components of a CSP:**

1.  **Variables ($X$):** The things we need to assign values to. (e.g., $X = \{WA, NT, Q, NSW, V, SA, T\}$ for map coloring).
2.  **Domains ($D$):** The possible values for each variable. (e.g., $D = \{Red, Green, Blue\}$).
3.  **Constraints ($C$):** Rules that limit valid assignments. (e.g., $WA \neq NT$).

### Constraint Graph

CSPs are often visualized as a graph where:

- **Nodes** = Variables.
- **Edges** = Constraints between variables.

### Backtracking Search

The primary algorithm for solving CSPs is **Backtracking Search**, which is essentially DFS with a twist: it checks constraints _as it goes_.

```python
# Pseudo-code for Backtracking
def backtracking_search(csp):
    return backtrack({}, csp)

def backtrack(assignment, csp):
    # 1. Success?
    if len(assignment) == len(csp.variables):
        return assignment

    # 2. Select Unassigned Variable (Heuristics apply here!)
    var = select_unassigned_variable(assignment, csp)

    # 3. Try Values
    for value in order_domain_values(var, assignment, csp):
        if is_consistent(var, value, assignment, csp):
            assignment[var] = value
            result = backtrack(assignment, csp)
            if result: return result
            del assignment[var] # Backtrack!

    return Failure
```

### Example: Map Coloring (Australia)

**Problem:** Color the map of Australia using Red, Green, Blue such that no two adjacent regions have the same color.

- **Variables:** WA, NT, SA, Q, NSW, V, T
- **Domain:** {R, G, B}
- **Constraints:** WA $\neq$ NT, WA $\neq$ SA, etc.

**Trace:**

1.  Assign WA = Red.
2.  Assign NT = Green (Valid).
3.  Assign SA = Blue (Valid).
4.  ... If we hit a dead end (e.g., Q has no valid colors left), we **backtrack** to the previous step and try a different color.

### Heuristics

Standard backtracking is slow ($O(d^n)$). We use heuristics to speed it up:

1.  **MRV (Minimum Remaining Values):** Pick the variable with the _fewest_ legal moves left (The "Fail Fast" principle).
2.  **Degree Heuristic:** Pick the variable involved in the _most_ constraints.
3.  **LCV (Least Constraining Value):** Pick the value that rules out the _fewest_ choices for neighbors.

## Real-World Applications

- **Sudoku:** A classic CSP.
- **Scheduling:** Assigning classes to rooms/times without conflicts.
- **Circuit Layout:** Placing components on a chip without overlapping wires.
