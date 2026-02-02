Links: [[College/Operating System/08 Concurrency]]
___
# Critical Section Problem

In concurrent programming, a **Critical Section** is a part of a program's code (like a block or a function) that accesses a **shared resource**. This resource could be a shared variable, a database, a file, or any piece of data that multiple processes or threads might try to modify.

The **Critical Section Problem** is the challenge of designing a protocol or system that allows multiple processes to cooperate and use these shared resources without causing data inconsistency (like race conditions).

A valid solution must satisfy three requirements:

1.  **Mutual Exclusion:** If one process (`P1`) is executing in its critical section, then no other process can be executing in *its* critical section for the *same shared resource*. This is the most important rule; it prevents race conditions.

2.  **Progress (No Deadlock):** If no process is currently in its critical section and some processes want to enter, a decision *must* be made about which process enters next. This decision cannot be postponed indefinitely. This prevents a deadlock where everyone is waiting, and no one can move forward.

3.  **Bounced Waiting (No Starvation):** There must be a limit on the number of times other processes are allowed to enter their critical sections after a process has made a request to enter its own. This ensures that no process is "starved" by being repeatedly overlooked by the scheduler.

## Mutual Exclusion

**Mutual Exclusion (Mutex)** is the property of ensuring that the first requirement (above) is met. It's the core concept for preventing race conditions.

We achieve mutual exclusion by creating a "lock." A process must **acquire the lock** *before* entering its critical section and **release the lock** *after* exiting it. While one process holds the lock, all other processes that try to acquire it must wait.

The general structure of a process looks like this:

```c
do {

// 1. Acquire Lock
entry_section();
    // 2. CRITICAL SECTION
    // (Access shared data)
// 3. Release Lock
exit_section();
// REMAINDER SECTION
// (Do non-shared work)
} while (true);

```

## Software Solutions (Historical)

These are early, important academic solutions that solve the critical section problem for two processes using only shared memory. They are complex and not used in modern systems (we use hardware-backed mutexes now), but they are foundational.

### Dekker’s Solution

Dekker’s algorithm (1965) was the first provably correct solution to the critical section problem for two processes. It uses two shared variables:

- `turn`: An `int` that indicates whose turn it is to enter (0 or 1).
- `flag[2]`: A `boolean` array. `flag[i] = true` means process `Pi` *wants* to enter.

**How it works:**
- A process `Pi` signals its intent by setting `flag[i] = true`.
- It then checks if the other process `Pj` *also* wants to enter (`flag[j] == true`).
- **If YES:** The processes check the `turn` variable.
    - If `turn == j`, it means it's the *other* process's turn. `Pi` sets its own `flag[i] = false` (to let `Pj` in) and waits until `turn == i`. Then it sets `flag[i] = true` again and repeats the check.
    - If `turn == i`, `Pi` knows it can proceed and enters the critical section.
- **If NO:** `Pi` enters its critical section immediately.

- **On exit:** `Pi` sets `turn = j` (giving the turn to the other process) and sets `flag[i] = false`.

- **Guarantees:** Mutual Exclusion, Progress, and Bounded Waiting.

```c
// Pi is the current process (0 or 1)
// Pj is the other process (1 or 0)

do {
	flag[i] = true; // 1. Signal intent
	
	while (flag[j] == true) { // 2. If other wants to enter
		if (turn == j) { // 3. And it is their turn
			flag[i] = false; // 4. Back off
			while (turn == j); // 5. Wait for turn
			flag[i] = true; // 6. Retry
		}
	}
	
	// --- CRITICAL SECTION ---

	turn = j; // 7. Give turn to other
	flag[i] = false; // 8. Reset flag
	
	// --- REMAINDER SECTION ---

} while (true);
```

### Peterson’s Solution

Peterson's solution (1981) is a much simpler and more elegant two-process solution that also uses two shared variables:

- `turn`: An `int` that indicates whose turn it is (0 or 1).
- `flag[2]`: A `boolean` array. `flag[i] = true` means process `Pi` *wants* to enter.

**How it works (Process `Pi`):**

```c
// Pi is the current process (0 or 1)
// Pj is the other process (1 or 0)

do {
    // 1. Signal intent
    flag[i] = true;

    // 2. Give turn to the other process
    turn = j;

    // 3. Wait ONLY if the other process
    //    ALSO wants to enter AND it's its turn
    while (flag[j] == true && turn == j) {
        // Busy-wait (do nothing)
    }

    // --- CRITICAL SECTION ---

    // 4. Release lock (signal exit)
    flag[i] = false;

    // --- REMAINDER SECTION ---

} while (true);
```

**Why it works:**

- If `Pj` doesn't want to enter (`flag[j] == false`), `Pi` enters immediately.
    
- If both want to enter (`flag[i]` and `flag[j]` are true), they both set `turn`. Whichever process set `turn` _last_ (e.g., if `Pi` set `turn = j` and then `Pj` set `turn = i`), that process will be the one that _waits_, and the other will enter. The `turn` variable acts as the tie-breaker.
    
- **Guarantees:** Mutual Exclusion, Progress, and Bounded Waiting.
    

**Note:** On modern CPUs with complex caching, these solutions can fail due to memory reordering. They require special "memory fence" instructions to work, which is why modern systems use **hardware-supported atomics, mutexes, and semaphores** instead.