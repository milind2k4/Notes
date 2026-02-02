Links: [[09 Critical Section Problem]], [[10 Process Synchronization]]
___
# Classical Problems of Synchronization

These problems are used to test synchronization schemes (semaphores, monitors) and to demonstrate the power and challenges of concurrency control.

### Producer-Consumer Problem
Also known as the **Bounded-Buffer Problem**.

**Scenario:**
Two processes share a fixed-size buffer (an array).
- **Producer:** Generates data and puts it into the buffer.
- **Consumer:** Takes data out of the buffer and consumes it.

**Constraints:**
1.  **Overflow:** The Producer must not try to add data if the buffer is full.
2.  **Underflow:** The Consumer must not try to remove data if the buffer is empty.
3.  **Mutual Exclusion:** Only one process can access the buffer at a time to prevent data corruption.

**Synchronization Variables:**
- `mutex` (Binary Semaphore, init = 1): Provides mutual exclusion for buffer access.
- `empty` (Counting Semaphore, init = N): Counts empty slots.
- `full` (Counting Semaphore, init = 0): Counts filled slots.

**Solution:**
```c
// --- Producer Process ---
do {
    // Produce an item
    item = produce_item();

    wait(empty);   // Wait for an empty slot (decrements empty)
    wait(mutex);   // Lock the buffer

    // CRITICAL SECTION: Add item to buffer
    buffer[in] = item;
    in = (in + 1) % N;

    signal(mutex); // Unlock the buffer
    signal(full);  // Signal that a new full slot is available

} while (TRUE);

// --- Consumer Process ---
do {
    wait(full);    // Wait for a filled slot (decrements full)
    wait(mutex);   // Lock the buffer

    // CRITICAL SECTION: Remove item from buffer
    item = buffer[out];
    out = (out + 1) % N;

    signal(mutex); // Unlock the buffer
    signal(empty); // Signal that a new empty slot is available

    // Consume the item
    consume_item(item);

} while (TRUE);
```

### Readers-Writers Problem

**Scenario:**
A database or file is shared among several concurrent processes.
- **Readers:** Only read the data; they do not perform any updates.
- **Writers:** Can both read and write.

**Constraints:**
1. **Multiple Readers:** If one process is reading, other readers _can_ also read simultaneously.
2. **Exclusive Writer:** If a writer is writing, no other process (reader or writer) can access the database.
3. **Priority:** The standard solution (below) gives priority to Readers. A writer might starve if readers keep coming.

**Synchronization Variables:**
- `mutex` (Semaphore, init = 1): Protects the `read_count` variable.
- `wrt` (Semaphore, init = 1): Ensures exclusive access for the writer.
- `read_count` (Integer, init = 0): Tracks how many readers are currently active.

**Solution:**

```c
// --- Writer Process ---
do {
    wait(wrt);   // Request exclusive access

    // WRITING SECTION

    signal(wrt); // Release access

} while (TRUE);

// --- Reader Process ---
do {
    wait(mutex);      // Protect read_count
    read_count++;
    
    // If I am the FIRST reader, I must lock out the writer
    if (read_count == 1) {
        wait(wrt);
    }
    signal(mutex);

    // READING SECTION (Multiple readers can be here)

    wait(mutex);      // Protect read_count
    read_count--;

    // If I am the LAST reader leaving, I unlock the writer
    if (read_count == 0) {
        signal(wrt);
    }
    signal(mutex);

} while (TRUE);
```

### Dining Philosophers Problem

**Scenario:**
Five philosophers sit at a circular table with a bowl of rice in the center. There are five chopsticks (or forks), one between each pair of philosophers.

**Life Cycle:** A philosopher alternates between Thinking and Eating.

To eat, a philosopher needs two chopsticks (the one on their left and the one on their right).

**Constraints:**
- A philosopher can only pick up one chopstick at a time.
- They cannot pick up a chopstick if their neighbor is holding it.

**The Problem (Deadlock):**
If every philosopher becomes hungry at the same time and picks up their left chopstick, they will all wait forever for the right chopstick. This is a deadlock.

**Synchronization Variables:**
- `chopstick[5]` (Array of Semaphores, all init = 1).

**Naive Solution (Deadlock Prone):**

```c
// Philosopher i
do {
    wait(chopstick[i]);            // Pick up left
    wait(chopstick[(i + 1) % 5]);  // Pick up right

    // EAT

    signal(chopstick[i]);          // Put down left
    signal(chopstick[(i + 1) % 5]); // Put down right

    // THINK
} while (TRUE);
```

**Better Solutions (To avoid deadlock):**
1. **Limit Eaters:** Allow at most 4 philosophers to sit at the table.
2. **Asymmetric Solution:** Odd-numbered philosophers pick up the left chopstick first; Even-numbered pick up the right first.
3. **Monitor/Atomic Action:** A philosopher picks up both chopsticks only if both are available.

### Sleeping Barber Problem

**Scenario:**
A barbershop consists of a waiting room with $N$ chairs and a barber room with one barber chair.

- **If there are no customers:** The barber falls asleep in his chair.
- **If a customer arrives and the barber is asleep:** The customer wakes the barber.
- **If a customer arrives and the barber is busy:**
    - If there is a free chair in the waiting room, the customer sits and waits.
    - If there are no free chairs, the customer leaves.

**Synchronization Variables:**
- `customers` (Semaphore, init = 0): Counts waiting customers (and wakes barber).
- `barber` (Semaphore, init = 0): Indicates if the barber is ready to cut hair.
- `mutex` (Semaphore, init = 1): Protects access to `free_seats`.
- `free_seats` (Integer, init = N): Number of available chairs.

**Solution:**

```c
// --- Barber Process ---
do {
    wait(customers); // Sleep if no customers. Wake up if signal received.

    wait(mutex);     // Lock seat count
    free_seats++;    // One chair becomes free (customer moves to barber chair)
    signal(barber);  // Tell customer "I am ready to cut"
    signal(mutex);   // Unlock seat count

    // CUT HAIR

} while (TRUE);

// --- Customer Process ---
do {
    wait(mutex);     // Lock seat count to check availability

    if (free_seats > 0) {
        free_seats--;       // Sit in waiting chair
        signal(customers);  // Notify barber (wake him up if needed)
        signal(mutex);      // Unlock seat count

        wait(barber);       // Wait for barber to be ready for ME
        
        // GET HAIRCUT
    } else {
        signal(mutex);      // Unlock seat count
        // LEAVE SHOP (No seats available)
    }
} while (TRUE);
```