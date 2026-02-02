Links: [[17 Virtual Memory]]
___
# Page Replacement Algorithms

M means Miss and H means Hit

### First in First Out (FIFO)

**Strategy:** Replace the page that has been in memory the longest.

**Reference String:** `7 0 1 2 0 3 0 4 2 3 0 3 2 1 2 0 1 7 0 1`
**Frames:** 3


| Reference   | 7     | 0     | 1     | 2     | 0   | 3     | 0     | 4     | 2     | 3     | 0     | 3   | 2   | 1     | 2     | 0   | 1   | 7     | 0     | 1     |
| :---------- | :---- | :---- | :---- | :---- | :-- | :---- | :---- | :---- | :---- | :---- | :---- | :-- | :-- | :---- | :---- | :-- | :-- | :---- | :---- | :---- |
| **Frame 1** | 7     | 7     | 7     | 2     | 2   | 2     | 2     | 4     | 4     | 4     | 0     | 0   | 0   | 0     | 0     | 0   | 0   | 7     | 7     | 7     |
| **Frame 2** |       | 0     | 0     | 0     | 0   | 3     | 3     | 3     | 2     | 2     | 2     | 2   | 2   | 1     | 1     | 1   | 1   | 1     | 0     | 0     |
| **Frame 3** |       |       | 1     | 1     | 1   | 1     | 0     | 0     | 0     | 3     | 3     | 3   | 3   | 3     | 2     | 2   | 2   | 2     | 2     | 1     |
| **Fault?**  | **M** | **M** | **M** | **M** | H   | **M** | **M** | **M** | **M** | **M** | **M** | H   | H   | **M** | **M** | H   | H   | **M** | **M** | **M** |

**Total Page Faults:** 15

#### Belady's Anomaly

FIFO suffers from **Belady's Anomaly**: Increasing the number of frames can sometimes _increase_ the number of page faults.

### Least Recently Used (LRU)

**Strategy:** Replace the page that has not been used for the longest period of time.

**Reference String:** `7 0 1 2 0 3 0 4 2 3 0 3 2 1 2 0 1 7 0 1`
**Frames:** 3

| Reference   | 7     | 0     | 1     | 2     | 0   | 3     | 0   | 4     | 2     | 3     | 0     | 3   | 2   | 1     | 2   | 0     | 1   | 7     | 0   | 1   |
| :---------- | :---- | :---- | :---- | :---- | :-- | :---- | :-- | :---- | :---- | :---- | :---- | :-- | :-- | :---- | :-- | :---- | :-- | :---- | :-- | :-- |
| **Frame 1** | 7     | 7     | 7     | 2     | 2   | 2     | 2   | 4     | 4     | 4     | 0     | 0   | 0   | 1     | 1   | 1     | 1   | 1     | 1   | 1   |
| **Frame 2** |       | 0     | 0     | 0     | 0   | 0     | 0   | 0     | 0     | 3     | 3     | 3   | 3   | 3     | 3   | 0     | 0   | 0     | 0   | 0   |
| **Frame 3** |       |       | 1     | 1     | 1   | 3     | 3   | 3     | 2     | 2     | 2     | 2   | 2   | 2     | 2   | 2     | 2   | 7     | 7   | 7   |
| **Fault?**  | **M** | **M** | **M** | **M** | H   | **M** | H   | **M** | **M** | **M** | **M** | H   | H   | **M** | H   | **M** | H   | **M** | H   | H   |

**Total Page Faults:** 12

### Optimal

**Strategy:** Replace the page that will not be used for the longest period of time. (Impossible to implement in real-time, used as a benchmark).

**Reference String:** `7 0 1 2 0 3 0 4 2 3 0 3 2 1 2 0 1 7 0 1`
**Frames:** 3

| Reference   | 7     | 0     | 1     | 2     | 0   | 3     | 0   | 4     | 2   | 3   | 0     | 3   | 2   | 1     | 2   | 0   | 1   | 7     | 0   | 1   |
| :---------- | :---- | :---- | :---- | :---- | :-- | :---- | :-- | :---- | :-- | :-- | :---- | :-- | :-- | :---- | :-- | :-- | :-- | :---- | :-- | :-- |
| **Frame 1** | 7     | 7     | 7     | 2     | 2   | 2     | 2   | 2     | 2   | 2   | 2     | 2   | 2   | 2     | 2   | 2   | 2   | 7     | 7   | 7   |
| **Frame 2** |       | 0     | 0     | 0     | 0   | 0     | 0   | 4     | 4   | 4   | 0     | 0   | 0   | 0     | 0   | 0   | 0   | 0     | 0   | 0   |
| **Frame 3** |       |       | 1     | 1     | 1   | 3     | 3   | 3     | 3   | 3   | 3     | 3   | 3   | 1     | 1   | 1   | 1   | 1     | 1   | 1   |
| **Fault?**  | **M** | **M** | **M** | **M** | H   | **M** | H   | **M** | H   | H   | **M** | H   | H   | **M** | H   | H   | H   | **M** | H   | H   |

**Total Page Faults:** 9
