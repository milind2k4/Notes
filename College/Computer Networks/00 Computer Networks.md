Links: [[01 Types of Networks]]
___
# Computer Networks

## Basic Concepts
A **Computer Network** is a set of devices (nodes) connected by communication links.

- **Node:** Any device capable of sending, receiving, or processing data (e.g., Computer, Printer, Router).
- **Communication Medium:** The path over which information travels (e.g., Copper wire, Fiber optics, Radio waves).

> [!HELP] Why networks?
> A network allows distributed processing, meaning tasks are divided among multiple computers.

### Applications of Networks
- **Resource Sharing:** Sharing printers, storage devices.
- **Information Sharing:** File exchange, database access.
- **Communication:** Email, Video conferencing.
- **Remote Access:** Accessing systems from different locations.

> [!TIP] AE2 Analogy: The ME Network
> 
> - **Computer Network:** The entire ME System.
> - **Node:** Any machine connected to the cable (e.g., ME Drive, Terminal, Controller).
> - **Medium:** The ME Glass/Smart Cable connecting them.

## Network Performance
Parameters used to measure the "quality" of a network.

- **Transit Time:** The time required for a message to travel from one device to another.
- **Response Time:** The time elapsed between an inquiry and a response.
- **Reliability:** Measured by frequency of failure and the time it takes to recover from a link failure.
- **Security:** Protecting data from unauthorized access or damage.
- **Scalability:** Ability to accommodate more users/nodes without significant performance degradation.
- **Flexibility:** Ease of connecting (or removing) devices.

## Modes of Communication
Data transmission occurs in one of three modes:

```mermaid
flowchart LR

%% Invisible links position subgraphs horizontally
S ~~~ HD ~~~ FD

subgraph S [Simplex]
    A1[Sender] -->|"One Way"| B1[Receiver]
end

subgraph HD [Half-Duplex]
    A2[Device A] -->|One at a time| B2[Device B]
    B2 -.->|Alternating| A2
end

subgraph FD [Full-Duplex]
    A3[Device A] <--> B3[Device B]
end
```

> [!TIP] Analogy for Modes
> 
> - **Simplex:** One-way street.
> - **Half-Duplex:** One-lane bridge with traffic lights (cars take turns).
> - **Full-Duplex:** Two-lane highway (cars move both ways at once).

### Simplex
Unidirectional communication. Data flows in only **one direction**.

- **Example:** Mainframe to Monitor, Keyboard to CPU, Radio broadcasting.
- **Capacity:** The entire capacity of the channel is used for one direction.

### Half-Duplex
Bidirectional communication, but **not simultaneously**.

- **Example:** Walkie-Talkie. Both parties can speak, but one at a time.
- **Mechanism:** The entire capacity is used for each direction, but they must take turns.

### Full-Duplex
Bidirectional communication **simultaneously**.

- **Example:** Telephone network, Mobile phones.
- **Mechanism:** Signals can go in both directions at the same time (often by using two channels).

> [!TIP] AE2 Analogy: Buses vs Interfaces
> 
> - **Simplex:** **Export Bus**. It can *only* send items out of the network to a chest. It cannot pull them back.
> - **Full-Duplex:** **Pattern Provider**. It can push patterns out to a Molecular Assembler AND pull the finished result back simultaneously.

## Design Issues with Networks
When designing or expanding a network, several critical issues must be addressed to ensure efficient and reliable communication.

- **Reliability:** Making sure the network is available when needed and tolerant to hardware or software failures.
- **Scalability:** The architecture must be able to support growth in the number of users or network size without a complete redesign.
- **Addressing:** Every device needs a unique identifier (like an IP or MAC address) so data can find its way to the correct destination.
- **Error Control:** Mechanisms to detect and correct data corruption that occurs during transmission (see [[10 Data Link Layer#Error Control]]).
- **Flow Control:** Preventing a fast sender from overwhelming a slow receiver by managing the transmission rate (see [[10 Data Link Layer#Flow Control]]).
- **Security & Routing:** Protecting data from unauthorized access (encryption, firewalls) and determining the optimal path for data to travel across the network.