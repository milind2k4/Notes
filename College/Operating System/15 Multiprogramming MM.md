Links: [[14 Memory Management]]
___
# Multiprogramming Memory Management

To increase CPU utilization, we want to keep multiple processes in the memory simultaneously (Multiprogramming). The Operating System needs a strategy to divide the available main memory among these processes.

There are two contiguous memory allocation techniques:

1. **Fixed Partitioning** (Static)
2. **Variable Partitioning** (Dynamic)

### Fixed Partitioning (Static)

Also known as **MFT (Multiprogramming with a Fixed number of Tasks)**.

In this scheme, the system's memory is divided into a **fixed number of partitions** (blocks) when the OS starts up. These partitions cannot change size or number during system operation.

- **Partitions can be of:**
    - **Equal Size:** All blocks are the same size (e.g., all 4MB).
    - **Unequal Size:** Blocks vary (e.g., 4MB, 8MB, 16MB) to accommodate different process sizes.

**Mechanism:**
When a process arrives, it is analyzed to see if it fits into a free partition. If a partition is free and large enough, the process is loaded.

#### The Problem: Internal Fragmentation

The biggest drawback of Fixed Partitioning is wasted space _inside_ a partition.

If a process requires **3 MB** and we assign it to a partition of **4 MB**, then **1 MB** is wasted.

- This 1 MB cannot be used by any other process because the partition is "occupied."
- This waste is called **Internal Fragmentation**.

> [!TIP] > Analogy:
> 
> Think of a shoe organizer or a parking lot with painted lines.
> 
> - If you have a parking spot designed for a bus (Partition), and you park a bicycle (Process) in it, the rest of the space in that spot is wasted.
>     
> - No other car can park there because the spot is technically "taken."

#### Pros and Cons

**Pros:**
- Simple to implement.
- Little OS overhead (easy to manage).

**Cons:**
- **Internal Fragmentation:** Wastes memory.
- **Limit on Process Size:** A process larger than the largest partition cannot run.
- **Limit on Degree of Multiprogramming:** The number of processes is limited by the number of partitions.


### Variable Partitioning (Dynamic)

Also known as **MVT (Multiprogramming with a Variable number of Tasks)**.

In this scheme, memory is **not** partitioned in advance. The memory is treated as one large block of available space (a hole).

Mechanism:

When a process arrives, the OS allocates exactly the amount of memory the process needs.

- If Process A needs 10 MB, it gets a 10 MB block.
- If Process B needs 5 MB, it gets a 5 MB block right next to A.
- The number of partitions and their sizes change dynamically.

#### The Problem: External Fragmentation

While this solves Internal Fragmentation (because there is no extra space inside the block), it creates a new problem.

As processes finish and leave memory, they leave "holes" or gaps between the remaining processes.

Over time, memory becomes a "Swiss cheese" of used space and tiny holes.

- **External Fragmentation** occurs when there is enough **total** free memory to satisfy a request, but the available spaces are **not contiguous** (they are scattered).

> [!tip] > Analogy:
> 
> Think of parallel parking on a street with no painted lines.
> 
> - Cars park bumper-to-bumper.
>     
> - When a small car leaves from the middle, it leaves a small gap.
>     
> - If a large truck comes along, it might not fit in that gap, even if there is plenty of space further down the street.

#### Solution: Compaction

To fix External Fragmentation, the OS can perform **Compaction** (or Defragmentation).

- The OS shuffles the memory contents to place all free memory together in one large block.
- _Disadvantage:_ This consumes a lot of CPU time and halts the system during the move.

#### Pros and Cons

**Pros:**
- No Internal Fragmentation.
- More efficient use of memory.
- No limit on the number of processes (except total RAM size).

**Cons:**
- **External Fragmentation.**
- Complex memory management (allocation and deallocation).

### Memory Allocation Strategies

When using Variable Partitioning (or Fixed with unequal sizes), the OS must decide _which_ free hole to assign to a process. There are three standard algorithms:

1. **First Fit:**
    - Allocate the **first** hole that is big enough.
    - _Speed:_ Fast (searching stops as soon as a fit is found).
    - _Result:_ Generally the best method.
2. **Best Fit:**
    - Allocate the **smallest** hole that is big enough.
    - _Speed:_ Slow (must search the entire list to find the best match).
    - _Result:_ Leaves very tiny, useless holes (high external fragmentation).
3. **Worst Fit:**
    - Allocate the **largest** available hole.
    - _Speed:_ Slow (must search the entire list to find the largest).
    - _Result:_ Leaves a large remaining hole, which might be useful for another process.

### Summary Comparison

| Feature              | Fixed Partitioning                      | Variable Partitioning                   |
| -------------------- | --------------------------------------- | --------------------------------------- |
| **Partition Size**   | Fixed at boot time                      | Dynamic, determined by process size     |
| **Complexity**       | Simple                                  | Complex                                 |
| **Fragmentation**    | Suffers from **Internal** Fragmentation | Suffers from **External** Fragmentation |
| **Multiprogramming** | Limited by number of partitions         | Limited by total RAM size               |
| **Analogy**          | Parking lot with lines                  | Parallel parking without lines          |


