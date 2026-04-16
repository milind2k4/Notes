Links: [[05 Process Scheduling]]
___
# CPU Scheduling

aka Process Scheduling

CPU Scheduling is a fundamental service of the operating system. Its goal is to meet the objectives of multiprogramming and multitasking by deciding which process in the **Ready Queue** gets to use the CPU.

It is the process of providing the CPU (a resource) to a program, not the other way around.

##### When Does Scheduling Occur?

CPU scheduling decisions must be made when a process:

1.  **Switches from Running to Waiting:** (e.g., I/O request, `wait()` for a child)
2.  **Switches from Running to Ready:** (e.g., an interrupt or time quantum expires)
3.  **Switches from Waiting to Ready:** (e.g., I/O completion)
4.  **Terminates:** (e.g., calls `exit()`)

#### Preemptive vs. Non-Preemptive Scheduling

**Non-Preemptive:** The OS _cannot_ stop a process in the middle. Scheduling only happens at points 1 (Waiting) and 4 (Terminated). Once a process gets the CPU, it runs until it's done or it voluntarily gives up the CPU.

**Preemptive:** The OS _can_ stop (preempt) a running process. Scheduling happens at all four points. This is essential for time-sharing and interactive systems.

#### The Dispatcher

The scheduler _selects_ the next process, but the **Dispatcher** is the module that actually allocates the CPU to that process.

The dispatcher must:

- **Switch context:** Save the state (PCB) of the old process and load the state of the new one.
- Switch to user mode.
- Jump to the proper location in the new process (its Program Counter).

> [!TIP] Analogy: Context Switch = Switching Books
> Imagine you are reading a book (Process A) and your friend interrupts you to ask for help with homework (Process B).
>
> 1.  You mark your page in the book with a **bookmark** (Save PCB of A).
> 2.  You help your friend (Run Process B).
> 3.  When done, you open the book to the bookmark and resume exactly where you left off (Restore PCB of A).
>
> The time spent putting the bookmark in and opening the book back up is **Overhead** (Dispatch Latency). You aren't reading _or_ helping during that split second.

**Dispatch Latency:** The time it takes for the dispatcher to stop one process and start another. This is pure overhead, so it must be as fast as possible.

#### Performance Criteria

To compare scheduling algorithms, we use several criteria:

- **CPU Utilization:** The percentage of time the CPU is busy should be high.
- **Throughput:** The number of processes completed per unit of time should be high.
- **Turnaround Time:** The total time from when a process is _submitted_ to when it is _completed_ should be low. (This is `Waiting Time + Burst Time`).
- **Waiting Time:** The total time a process spends in the **Ready Queue** should be low.
- **Response Time:** The time from when a request is submitted until the _first response_ is produced. This is most important for interactive systems.

## CPU Scheduling Algorithms

### First-Come, First-Served (FCFS)

The process that requests the CPU first is allocated the CPU first. This is managed with a simple FIFO queue.

> [!TIP] Analogy: Grocery Store Queue
> Imagine a single cashier at a grocery store.
>
> - **FCFS**: People are served in the exact order they arrive.
> - **Problem**: If the person in front has a full cart (Long Burst Time), everyone behind them waits, even if they only have a pack of gum. This is the **Convoy Effect**.

- **Nature:** Non-Preemptive.
- **Example:**

  - P1 (Burst: 24)
  - P2 (Burst: 3)
  - P3 (Burst: 3)

  **Case 1: Arrive P1, P2, P3**

  - **Gantt Chart:**
    ```c
    |    P1 (24)    | P2 (3) | P3 (3) |
    0              24       27       30
    ```
  - **Waiting Time:** P1 = 0, P2 = 24, P3 = 27
  - **Average Waiting Time (AWT):** (0 + 24 + 27) / 3 = **17 ms**

  **Case 2: Arrive P2, P3, P1**

  - **Gantt Chart:**
    ```c
    | P2 (3) | P3 (3) |    P1 (24)    |
    0        3        6              30
    ```
  - **Waiting Time:** P2 = 0, P3 = 3, P1 = 6
  - **Average Waiting Time (AWT):** (0 + 3 + 6) / 3 = **3 ms**

**Disadvantage:** This example shows the **Convoy Effect**. One long process (P1) makes all the short processes (P2, P3) wait, leading to a high average waiting time.

### Shortest-Job-First (SJF)

The CPU is assigned to the process that has the smallest _next_ CPU burst.

> [!TIP] Analogy: Express Checkout Lane
> "10 items or less".
>
> - The cashier always picks the person with the fewest items in their basket.
> - **Benefit**: The average waiting time for everyone drops significantly because short tasks clear out fast.
> - **Risk**: If short customers keep arriving, the person with a full cart (Long Burst) might never get served (**Starvation**).

- **Nature:** Non-Preemptive.
- **Advantage:** This is provably the optimal algorithm for minimizing the _average waiting time_.

**Example:**
P1 (Burst: 6)
P2 (Burst: 8)
P3 (Burst: 7)
P4 (Burst: 3)

**Gantt Chart (Sorted by burst):**

```c
| P4 (3) | P1 (6) | P3 (7) | P2 (8) |
0        3        9        16       24
```

**Waiting Time:** P4 = 0, P1 = 3, P3 = 9, P2 = 16
**Average Waiting Time (AWT):** (0 + 3 + 9 + 16) / 4 = **7 ms**

**Disadvantage:** You cannot know the length of the next CPU burst. It's predicted using past behavior (exponential averaging).

### Shortest-Remaining-Time-First (SRTF)

aka Preemptive SJF.

The CPU is allocated to the job with the shortest _remaining_ time.

- **Nature:** Preemptive.
- If a new process arrives with a CPU burst shorter than the _remaining_ time of the current process, it will be preempted.

**Example:**

| Process | Arrival Time | Burst Time |
| :------ | :----------- | :--------- |
| P1      | 0            | 8          |
| P2      | 1            | 4          |
| P3      | 2            | 9          |
| P4      | 3            | 5          |

- **Gantt Chart:**
  ```c
  | P1 (1) | P2 (4) | P4 (5) |  P1 (7)  |  P3 (9)  |
  0        1        5        10         17         26
  ```

**Timeline:**

1.  t=0: P1 starts.
2.  t=1: P2 arrives (Burst=4). P1 has 7 remaining. 4 < 7, so **P2 preempts P1**.
3.  t=5: P2 finishes. Ready Queue: P1 (rem 7), P3 (burst 9), P4 (burst 5). **P4 is shortest**.
4.  t=10: P4 finishes. Ready Queue: P1 (rem 7), P3 (burst 9). **P1 is shortest**.
5.  t=17: P1 finishes. Ready Queue: P3 (burst 9).
6.  t=26: P3 finishes.

**Waiting Time:** (Completion - Arrival - Burst)

- P1: (17 - 0 - 8) = 9
- P2: (5 - 1 - 4) = 0
- P3: (26 - 2 - 9) = 15
- P4: (10 - 3 - 5) = 2

**AWT:** (9 + 0 + 15 + 2) / 4 = **6.5 ms**

### Priority Scheduling

A priority is associated with each process. The CPU is allocated to the process with the highest priority. (Conventionally, a lower number means higher priority).

> [!TIP] > **Analogy: VIP Access**
>
> - A hospital ER triage.
> - **Priority**: Heart attack victim (High Priority) gets treated before a sprained ankle (Low Priority), even if the sprained ankle arrived first.
> - **Starvation**: If critical patients keep arriving, the sprained ankle waits forever.
> - **Aging**: After waiting 5 hours, the sprained ankle becomes "critical" simply because they've waited so long.

- **Nature:** Can be **Non-Preemptive** or **Preemptive**.
- **Preemptive:** A new, higher-priority process will preempt the currently running process.
- **Non-Preemptive:** The new process is just put at the front of the ready queue.
- **Disadvantage:** **Starvation** (or indefinite blocking). A low-priority process may never run if there is a steady stream of high-priority processes.
  - **Solution:** **Aging**. A technique where the priority of a process increases the longer it waits in the ready queue.

### Round Robin (RR)

aka Preemptive FCFS.

This algorithm is designed for time-sharing systems.

> [!TIP] > **Analogy: Sharing a Toy**
>
> - Imagine kids sharing a single toy (CPU).
> - **Time Quantum**: A parent sets a timer for 5 minutes.
> - **Mechanism**: Kid A plays for 5 mins. Timer rings. Parent takes toy, gives it to Kid B. Kid A goes to the back of the line.
> - **Fairness**: Everyone gets a turn. No one hogs the toy forever.

- **Nature:** Preemptive.
- **Time Quantum (Time Slice):** A small unit of time (e.g., 10 ms).
- **Mechanism:** The ready queue is a circular FIFO queue. The scheduler gives each process the CPU for one time quantum.
  - If the process finishes its burst, it terminates.
  - If it doesn't, it is preempted and put at the _end_ of the ready queue.

**Example:** (P1=24, P2=3, P3=3) and **Time Quantum = 4 ms**

**Gantt Chart:**

```c
| P1 | P2 | P3 | P1 | P1 | P1 | P1 | P1 |
0    4    7    10   14   18   22   26   30
```

**Timeline:**

1.  P1 runs (0-4). (20 remaining).
2.  P2 runs (4-7). Finishes.
3.  P3 runs (7-10). Finishes.
4.  P1 runs (10-14). (16 remaining).
5.  ...P1 continues in 4ms bursts until it finishes at t=30.

**Waiting Time:**

- P1: 0 + (10 - 4) = 6
- P2: 4
- P3: 7

**AWT:** (6 + 4 + 7) / 3 = **5.67 ms** (Much better than FCFS)

### Multilevel Queue Scheduling

This algorithm partitions the ready queue into several separate queues, each with its own scheduling algorithm.

- Processes are **permanently assigned** to one queue based on their properties (e.g., interactive vs. batch).
- **Example:**
  - **Foreground Queue** (Interactive): Uses **Round Robin**.
  - **Background Queue** (Batch): Uses **FCFS**.
- Scheduling must be done _between_ the queues, (e.g., fixed-priority, where the Foreground queue must be empty before the Background queue can run).

### Multilevel Feedback Queue Scheduling (MLFQ)

This is the most complex and common algorithm. It is what we actually use to implement multilevel queue scheduling.

- It **allows processes to move between queues**.
- This implements **Aging**. A process that waits too long in a low-priority queue can be moved to a higher-priority queue (prevents starvation).
- It also punishes CPU-heavy processes. If a process uses its entire time quantum, it is **demoted** to a lower-priority queue.
- This separates processes by their CPU-burst behavior, giving interactive (I/O-bound) processes high priority and CPU-bound processes low priority.
