Links: [[21 Transport Layer]], [[00 Computer Networks]]
___
# Congestion Control & QoS

**Congestion** refers to a network state where the message traffic becomes so heavy that it significantly slows down the network's response time, potentially causing routers to violently drop packets due to buffer overflows.

**Congestion control** refers to the mechanisms that can either prevent congestion before it happens (Open Loop) or remove it after it has occurred (Closed Loop).

## Congestion Control Approaches

### Open Loop Techniques (Prevention)
These techniques are designed to proactively avoid congestion before it starts.

- **Retransmission Policy:** Senders use timers to detect lost packets, but aggressively retransmitting them too quickly can cause *more* congestion. A good policy paces retransmissions.
- **Window Policy:** Using "Selective Repeat" ARQ instead of "Go-Back-N" ARQ prevents the sender from dumping unnecessarily large chunks of duplicate data onto the network.
- **Acknowledgement Policy:** The receiver does not need to send an ACK for every single packet. Delaying ACKs reduces network traffic.
- **Discarding Policy:** Intermediate routers are programmed to drop less-sensitive packets (like an audio frame) to save highly sensitive packets (like a text message) before buffers fill.
- **Admission Policy:** Virtual circuit networks simply refuse to establish a new connection if they calculate it will cause congestion.

### Closed Loop Techniques (Removal)
These techniques react to fix congestion that has already occurred.
- **Back Pressure:** A congested router forces the router immediately upstream from it to slow down, propagating backward until it hits the original source.
- **Choke Packet:** The congested router explicitly generates a specialized "Choke Packet" and sends it directly back to the source machine, telling it to throttle its transmission rate.
- **Implicit Signaling:** The source machine infers congestion by noticing that its packets are taking longer to be acknowledged (or timing out entirely).
- **Explicit Signaling:** The router adds a tiny flag (1 bit) inside the header of passing data packets, alerting the destination that the network is congested so the destination can warn the source.

## TCP Congestion Control Policy
TCP specifically reacts to congestion by dynamically reducing the Sender's Window Size. The size is dictated by the smaller of two variables: the Receiver Window (how much the receiver can handle) and the **Congestion Window (cwnd)** (how much the network can handle).

TCP regulates the `cwnd` using a strict three-phase algorithm:

### Phase 1: Slow Start (Exponential Increase)
- The Congestion Window starts at exactly **1 Maximum Segment Size (1 MSS)**.
- Every time an ACK is successfully received, the window size doubles.
- The growth is technically "Slow" because it starts at 1, but it increases **exponentially** ($1, 2, 4, 8, 16\dots$).
- This phase stops the moment the `cwnd` reaches a predetermined **Threshold**.

### Phase 2: Congestion Avoidance (Additive Increase)
- To avoid prematurely crashing the network, the exponential growth stops when the Threshold is hit.
- The `cwnd` now increases **additively** (by +1 MSS) for every full window of acknowledged segments ($16, 17, 18, 19\dots$).
- It continues this slow, steady climb until congestion is explicitly detected (via a timeout or duplicate ACKs).

### Phase 3: Congestion Detection (Multiplicative Decrease)
- If a timeout occurs (meaning a packet was lost, likely due to a router dropping it from a full buffer), TCP assumes extreme congestion.
- **Reaction:**
  1. The Threshold is aggressively dropped to **one half (1/2)** of the current window size.
  2. The `cwnd` is instantly dropped all the way back to **1 MSS**.
  3. The **Slow Start** phase immediately begins again.


## Quality of Service (QoS)
QoS refers to a set of traffic management algorithms used in networks to prioritize specific data types and guarantee a certain level of performance.

### QoS Parameters
These are the measurable factors used to evaluate network performance:
1. **Bandwidth:** The maximum rate of data transfer across a given path.
2. **Jitter:** The variation in packet delay (highly disruptive for VoIP and Video).
3. **Throughput:** The actual rate of successful data delivery.
4. **Error Rate:** The percentage of corrupted packets.
5. **Packet Loss:** The percentage of packets permanently dropped by routers.
6. **Latency:** The time it takes a packet to travel from source to destination.

### Techniques to Improve QoS
Beyond strict traffic shaping algorithms, networks employ several fundamental techniques to manage and improve Quality of Service:

1. **Over Provisioning:** The simplest but most expensive solution. It involves intentionally building a network with significantly more bandwidth capacity than the maximum expected peak demand. If a network is heavily over-provisioned, congestion never occurs, naturally guaranteeing excellent QoS.
2. **Buffering:** When packets arrive at a router faster than they can be processed, the router places them in a queue (a buffer memory). This absorbs sudden, unexpected bursts of traffic, preventing immediate packet loss. However, excessive buffering can severely increase Latency and Jitter.
3. **Scheduling:** Instead of a simple "First In, First Out" (FIFO) queue, routers can be programmed with intelligent scheduling algorithms to prioritize specific data.
    - **Priority Queuing:** Highly sensitive traffic (like VoIP or video calls) is always processed first, while less sensitive traffic (like background email syncing) is forced to wait.
    - **Weighted Fair Queuing:** Divides bandwidth into different classes, ensuring that even low-priority traffic gets *some* guaranteed percentage of the bandwidth so it doesn't get starved completely.

### Traffic Shaping Algorithms
Traffic shaping forcefully regulates the rate of data transmission into the network. Two famous algorithms are used to smooth out "bursty" traffic.

#### Leaky Bucket vs. Token Bucket

| Feature           | Leaky Bucket                                                                                         | Token Bucket                                                                                                                |
| ----------------- | ---------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| **Mechanism**     | Water (data) pours in at a variable rate, but leaks out of a small hole at a strictly constant rate. | Tokens are generated at a constant rate. Data can only be sent if a token is spent.                                         |
| **Burstiness**    | **Does not allow bursts.** Smooths everything to a fixed, average output rate.                       | **Allows bursts.** If tokens accumulate while idle, a massive burst of data can be sent instantly.                          |
| **Packet Loss**   | If the bucket overflows (buffer full), new incoming packets are violently discarded.                 | If the bucket overflows (max tokens reached), tokens are discarded, but data packets are never lost directly by the bucket. |
| **Best Use Case** | Streaming video/audio where a constant, predictable bit-rate is required.                            | General web traffic and file downloads where occasional large bursts of speed are highly desirable.                         |

![[Pasted image 20260501144224.png]]