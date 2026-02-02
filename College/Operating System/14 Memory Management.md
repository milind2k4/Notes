Links: [[00 Operating System]]
___
# Memory Management: Early Systems

Memory management is the functionality of an operating system which handles or manages primary memory. It keeps track of each and every memory location, regardless of whether it is allocated to some process or it is free.

> [!TIP] > Analogy: Desk Space
>
> - **RAM (Memory)** = **Your Desk Surface**.
> - **Hard Disk** = **The Bookshelf**.
> - **Process** = **A Project**.
>
> To work on a project, you must take the file off the bookshelf and open it on your desk. If your desk is full, you can't open any more files unless you put some back on the shelf (Swapping/Paging). Memory Management is the art of organizing your desk so you can work on multiple projects without it becoming a mess.

Before modern complex systems (like Paging and Segmentation), memory management was very simple. We look at the two earliest stages here.

### Basic Bare Machine

This is the most primitive form of computer usage. In this scheme, there is essentially **no Operating System** managing the memory.

- **Concept:** The user has complete control over the entire system. The user is the programmer and the operator.
- **Memory Layout:** The entire memory space is dedicated to the **User Program**.
- **Mechanism:**
  1. The user manually loads the program (maybe via punch cards or tape).
  2. The processor executes the program.
  3. The program finishes.
  4. The user manually clears the memory and loads the next program.

**Characteristics:**

- **No Protections:** The program has direct access to hardware. If the code has a bug (e.g., an infinite loop writing to memory), it can crash the machine or overwrite BIOS instructions.
- **Single Tasking:** Only one thing happens at a time.

> Think of a Game Boy (Game Cartridge). When you insert a game cartridge, that game takes over the entire machine. There is no "Windows" or "macOS" running in the background. If you want to play a different game, you must physically remove the first one and insert the second. The machine is "bare" for the game to use.

### Resident Monitor

As hardware became faster, the time wasted by humans manually loading jobs became a problem (high setup time). The **Resident Monitor** was the first step towards a true Operating System (Batch Systems).

- **Concept:** A small program (the Monitor) is permanently stored in a specific section of the memory (usually low memory or high memory).
- **Memory Layout:** Memory is divided into two contiguous sections:
  1. **Monitor Area:** Reserved for the OS (Resident Monitor).
  2. **User Area:** Available for user programs.

**How it works (Automatic Job Sequencing):**

1. The Resident Monitor is always running.
2. It reads a job (program) from the input device.
3. It loads that job into the **User Area**.
4. It transfers control to the job.
5. When the job finishes (or crashes), control is automatically transferred _back_ to the Resident Monitor.
6. The Monitor immediately loads the next job.

Hardware Support: The Fence Register

Because the OS and the User Program now share the same RAM, we have a danger: The User Program could overwrite the OS!

To prevent this, hardware support called a **Fence Register** was introduced.

- The Fence Register stores the memory address where the Monitor ends and User Space begins.
- If the User Program tries to access memory _above_ the fence (inside the Monitor's territory), the hardware traps the error and terminates the program.

> Think of a Jukebox.
>
> - **Bare Machine:** You have to manually put a vinyl record on, play it, wait, take it off, and put the next one on.
> - **Resident Monitor:** The Jukebox mechanism is the "Monitor." You load a stack of records (the batch of jobs). The mechanical arm (the Monitor) plays one, and when it finishes, it automatically grabs the next one. The records cannot touch or break the mechanical arm because the arm is protected (Fence Register).

### Summary Comparison

| Feature          | Basic Bare Machine                   | Resident Monitor                       |
| ---------------- | ------------------------------------ | -------------------------------------- |
| **OS Presence**  | None                                 | Small "Monitor" program always present |
| **Memory Usage** | User gets 100%                       | User shares memory with Monitor        |
| **Job Loading**  | Manual (by human)                    | Automatic (by Monitor)                 |
| **Protection**   | None                                 | Fence Register                         |
| **Efficiency**   | Low (CPU idle during manual loading) | Higher (CPU kept busy)                 |
