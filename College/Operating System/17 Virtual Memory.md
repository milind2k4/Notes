Links: [[16 Memory Protection]]
___
# Virtual Memory

Virtual memory is a technique that allows the execution of processes that are **not completely in memory**. It separates logical memory from physical memory.

This allows programs to be **larger** than the actual physical RAM.

### Demand Paging

We do not load the entire program into RAM at startup. We load pages only when they are **needed** (demanded) during execution (lazy loading).

- **Valid/Invalid Bit:** Each entry in the page table has a bit.
    - **Valid (v):** The page is in RAM.
    - **Invalid (i):** The page is not in RAM (it's on the disk).

In a standard demand paging system, the Operating System (OS) brings pages from the secondary storage (disk) to the main memory (RAM) only when the executing process demands them.

However, in practice, many Demand Paging systems use optimizations like **Pre-paging**. The OS might guess which pages will be needed soon (spatial locality) and load them in advance to prevent the program from stopping frequently.

- **Mechanism:** When a process starts, the OS might load a small "working set" of pages it knows are essential (like the main function or initial variables).
- **Goal:** Balance memory efficiency with smooth performance.

#### Page Fault

A **Page Fault** is an interrupt (trap) that occurs when a program tries to access a page that is marked **Invalid** (not in RAM).

**Handling a Page Fault:**
1. CPU tries to access Page M.
2. Page Table says "Invalid". Trap to OS.
3. OS pauses the process.
4. OS looks on the Hard Disk (Swap Space) for Page M.
5. OS brings Page M into a free frame in RAM.
6. OS updates the Page Table (sets bit to Valid).
7. OS restarts the instruction that failed.

#### Performance of Demand Paging 
Page fault rate:
$$0 \leq p \leq 1$$

Effective Access Time:
$$\ce{ 
\begin{split}
EAT &= (1 - p)\times memory access \\
&+ p\times page fault service time
\end{split}
}$$

#### Thrashing

If a process does not have enough frames (memory) to hold the pages it uses frequently, the system will spend all its time swapping pages in and out of the disk, and no time executing code. This state of low CPU utilization and high paging activity is called **Thrashing**.

To reduce thrashing we reduce degree of multiprogramming. 

> Analogy for Virtual Memory:
> 
> The Library vs. The Desk.
> 
> - **The Disk (Library):** Contains millions of books (all your programs).
>     
> - **RAM (Desk):** Small space, can only fit 5 books.
>     
> - **Virtual Memory:** You pretend you have all the books on your desk.
>     
> - **Page Fault:** You reach for a book, realize it's not on the desk. You pause, walk to the library shelves, grab the book, put it on the desk (maybe removing an old one), and continue reading.

### Pure Demand Paging

**Pure Demand Paging** is the _strictest_ form of this strategy where **absolutely no pages** are loaded effectively until the program executes its first instruction.

1. The OS sets the instruction pointer to the first instruction of the process.
2. Since that page is not in memory yet, a **page fault** occurs immediately (on the very first instruction).
3. The OS brings that specific page in.
4. The process resumes, hits the next missing page, triggers another fault, and repeats.

- **Goal:** Maximum memory saving.10 No memory is wasted on pages that _might_ be used; only pages that _are_ used exist in RAM.


#### Differences

| Feature               | Demand Paging (with Pre-paging)                                                               | Pure Demand Paging                                                                     |
| --------------------- | --------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| **Initial State**     | The process starts with a few essential pages already loaded in RAM.                          | The process starts with **0 pages** in RAM.                                            |
| **First Instruction** | Usually executes smoothly without delay (if the page is pre-loaded).                          | **Always** causes a Page Fault immediately.                                            |
| **Page Fault Rate**   | Lower initially. The OS tries to anticipate needs.                                            | Very high initially (a "burst" of faults) as the program wakes up.                     |
| **Startup Latency**   | Slower process creation (time spent copying data before start), but faster initial execution. | Faster process creation (no data copying), but slower initial execution due to faults. |
| **Complexity**        | Higher. The OS needs algorithms to guess/predict which pages to pre-load.                     | Lower. The mechanism is simple: "If it's not there, fetch it."                         |

#### Analogy

- **Demand Paging (with Pre-paging):** You sit down at a restaurant, and the waiter immediately brings you bread and water because they _assume_ you will want them. You order the rest as you need it.
    
- **Pure Demand Paging:** You sit down at a completely empty table. You have to ask for a menu, then ask for a fork, then ask for water, one by one, as you need them. Nothing is given until specifically requested.11

