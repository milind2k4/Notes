Links: [[04 Process]], [[06 CPU Scheduling]]
___
# Concurrent Processes
**Concurrent processes** are two or more processes that are "in progress" at the same time.

This does **not** mean they are *executing* at the same exact instant. It means their execution lifetimes overlap.

- On a single-core system, concurrency is achieved through **multitasking** (or time-sharing). The OS switches the CPU between processes (context switching). This is **interleaved execution**.
- On a multi-core system, concurrency can be achieved through **parallelism**, where two processes *actually run* on different CPU cores at the same physical instant. This is **simultaneous execution**.

#### Principle of Concurrency
The "principle of concurrency" refers to the fundamental rules and challenges involved in managing multiple, interacting processes that overlap in time.

The core principle is **interleaving and overlapping execution** to achieve:
1.  **Increased CPU Utilization (Multiprogramming):**
    - In a simple batch system, when a process `P1` performs a slow I/O operation (like reading from disk), the CPU sits idle.
    - The principle of concurrency allows the OS to **pause** `P1` (while it waits for I/O) and **switch** the CPU to another process, `P2`.
    - This keeps the CPU busy, maximizing throughput.

2.  **Increased Responsiveness (Multitasking):**
    - In an interactive system, a user might be running a web browser, a text editor, and a music player.
    - Concurrency, managed by a time-sharing scheduler (like Round Robin), gives each process a small "slice" of CPU time.
    - This happens so fast that it gives the user the illusion that all processes are running at once, making the system feel responsive.

3.  **Support for Modular Program Structure:**
    - Complex problems can be broken down into simpler, separate, cooperating processes (or threads).
    - For example, a web server can have one process that "listens" for new connections and hands off each connection to a separate "worker" process.

#### Challenges of Concurrency
The principle of concurrency is powerful, but it introduces significant problems that the OS must manage. These problems arise when processes are **not** independent and must share data or resources.

1. **Race Conditions:**
    - A situation where the outcome of a program depends on the unpredictable sequence or timing of concurrent processes.
    - **Example:** `Process A` and `Process B` both read a bank balance of $100.
        1.  `A` calculates `100 + 50 = 150`.
        2.  *Before `A` can save,* the OS switches to `B`.
        3.  `B` calculates `100 - 30 = 70`.
        4.  `B` saves $70.
        5.  The OS switches back to `A`.
        6.  `A` saves $150, overwriting `B`'s change.
    - The final balance is $150, and the $30 withdrawal is lost.

2. **Resource Contention & Mutual Exclusion:**
    - Processes need to compete for finite resources (CPU, memory, printers, files).
    - To prevent race conditions, the OS must enforce **Mutual Exclusion**. This means that when one process is using a shared resource or variable, no other process can be allowed to access it.
    - The part of the code that accesses the shared resource is called the **Critical Section**.

3. **[[07 Deadlocks|Deadlock:]]**
    - A situation where two or more processes are permanently blocked, each waiting for a resource held by the other.
    - **Example:**
        1.  `Process A` locks `Resource 1`.
        2.  `Process B` locks `Resource 2`.
        3.  `Process A` tries to lock `Resource 2` (and waits).
        4.  `Process B` tries to lock `Resource 1` (and waits).
    - Neither process can proceed.

4. **Starvation (Indefinite Blocking):**
    - A process is repeatedly "overlooked" by the scheduler and never gets the resource it needs, even though the resource becomes available.
    - This can happen in a priority-based scheduler if a low-priority process is always preempted by new, high-priority processes.

### Managing Concurrency: Synchronization
To make concurrency work, the OS must provide mechanisms to manage these challenges. This is called **process synchronization**.

The core principle of synchronization is **Mutual Exclusion**, which is implemented using:
- **Semaphores:** A counter used to control access.
- **Mutexes (Mutual Exclusion Locks):** A simple lock that a process must acquire before entering its critical section.
- **Monitors:** A high-level language construct that bundles shared data and the procedures that can access it.