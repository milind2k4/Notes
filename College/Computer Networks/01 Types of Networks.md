Links: 
___
# Types of Networks

Networks can be classified based on geographical coverage, communication type, and architecture.

> [!TIP] Remember these terms for comparison:
> - Scalable 
> - Flexible 
> - Cost 
> - Scalable 
> - Latency
> - Efficiency

## Classification by Area
Based on the geographical area they cover:

> [!TIP] Comparison Summary
> | Type | Range | Ownership | Error Rate |
> | :--- | :--- | :--- | :--- |
> | **LAN** | Small (< 1km) | Private | Lowest |
> | **MAN** | Medium (< 50km) | Public/Private | Moderate |
> | **WAN** | Large (Worldwide) | Distributed | Highest |

> [!TIP] AE2 Analogy: Distance
> - **LAN:** Your **Main Base Wiring**. Cables running room-to-room. High speed (dense cables), instant access.
> - **WAN:** **Quantum Network Bridge**. Connecting your Overworld base to your Nether lava pump. It spans "Dimensions" (huge distances) but requires special infinite-range infrastructure.

##### Personal Area Network (PAN)
- **Scope:** Smallest network, covering an individual's workspace (approx. 10 meters).
- **Ownership:** Personal/Private.
- **Example:** Bluetooth connecting headphones to phone, USB connection.
- **Use Case:** Transferring files between personal devices.

##### Local Area Network (LAN)
- **Scope:** Covers a small geographical area such as a building, office, or home.
- **Ownership:** Private (owned by an organization or individual).
- **Speed:** High data transfer rates (100 Mbps to 10 Gbps).
- **Technology:** Ethernet (wired), Wi-Fi (wireless).
- **Example:** Home Wi-Fi network connecting phone, laptop, and TV.

##### Metropolitan Area Network (MAN)
- **Scope:** Covers a larger area like a city or heavy campus.
- **Ownership:** Can be private or public (ISP).
- **Mechanism:** Interconnects multiple LANs.
- **Example:** Cable TV network, City-wide Wi-Fi.

##### Wide Area Network (WAN)
- **Scope:** Spans a large physical distance (Country, Continent, Globe).
- **Ownership:** Distributed (no single owner).
- **Mechanism:** Interconnects LANs and MANs using public networks (telephone lines, satellites).
- **Example:** The Internet (collection of networks).

## Classification by Communication
Based on how data is transmitted between nodes.

### Point-to-Point
A direct, dedicated link between two devices.

- **Mechanism:** The entire capacity of the link is reserved for these two devices.
- **Pros:** High Security, Dedicated Bandwidth, Low Latency.
- **Cons:** Not Scalable (Need n-1 lines for 1 device to connect to n others).
- **Example:** Leased line between two bank branches, Microwave link between two towers.

```mermaid
graph LR
    A[Sender] <-->|Dedicated Link| B[Receiver]
```

### Point-to-Multipoint
A single link is shared by multiple devices.

- **Mechanism:** Bandwidth is shared either spatially (channels) or temporally (time slots).
- **Example:** College Wi-Fi, Mainframe connecting to terminals.
- **Pros:** Flexible, Scalable, Cost-effective.
- **Cons:** Security risks (shared medium), Lower efficiency (shared bandwidth).

```mermaid
graph LR
    %% Central Hub
    Center((Central Hub))

    %% Connections to Multiple Points
    Center --- NodeA[Remote Node A]
    Center --- NodeB[Remote Node B]
    Center --- NodeC[Remote Node C]
    Center --- NodeD[Remote Node D]
```

### Broadcast
One sender transmits data to **all** connected receivers simultaneously.

- **Mechanism:** Uses a single communication channel shared by all.
- **Example:** TV, Radio, Ethernet (in some configs).
- **Pros:** Low Latency, Multiple user connectivity.
- **Cons:**
    - **No privacy:** Everyone receives the message.
    - **Bandwidth Wastage:** If a message is intended for only *one* person but sent via broadcast, the channel is occupied (blocking others) for data that is irrelevant to most.
    - **Processing Overhead:** Every node must process the packet to decide whether to keep or discard it.

> [!TIP] AE2 Analogy: Wireless Access Point
> The **Wireless Access Point** blasts the network signal to a defined radius. Any **Wireless Terminal** in range receives the signal. It doesn't target a specific player; it just covers the area.

```mermaid
graph TD
    %% Source of the broadcast
    Source{{Broadcast Source}}

    %% The medium/cloud through which it spreads
    Medium(Communication Medium/Airwaves)

    %% Receiving nodes (All receive the same signal)
    Node1[Receiver 1]
    Node2[Receiver 2]
    Node3[Receiver 3]
    Node4[Receiver 4]

    Source == "Signal Sent to All" ==> Medium
    Medium -.-> Node1
    Medium -.-> Node2
    Medium -.-> Node3
    Medium -.-> Node4

    %% Styling to emphasize the "One-to-All" nature
    style Source fill:#ffeb3b,stroke:#fbc02d,stroke-width:2px
    style Medium fill:#e1f5fe,stroke:#01579b,stroke-dasharray: 5 5
```

## Classification by Architecture
Based on the logical design and functional roles.

> [!CAUTION] Common Pitfall
> Don't confuse **Architecture** (Logical design) with **Topology** (Physical layout). Client-Server is an architecture; Star or Bus is a topology.

### Peer-to-Peer (P2P)

A decentralized architecture where every node has equal status.

- **Roles:** Each node acts as both **Client** and **Server**.
- **Pros:** Easy to set up, No single point of failure, Low cost.
- **Cons:** Difficult to manage security and backups (decentralized).
- **Example:** Bitcoin (Blockchain nodes), Napster (File sharing).

> [!TIP] AE2 Analogy: P2P Tunnels
> **ME P2P Tunnels** create a direct 1-to-1 connection between two points using an existing network purely as a carrier. Just like a P2P network overlay, the two endpoints talk "directly" to each other, ignoring the rest of the cabling in between.

```mermaid
graph LR
    %% P2P Mesh
    NodeA[Node A] <--> NodeB[Node B]
    NodeB <--> NodeC[Node C]
    NodeC <--> NodeA
    NodeA <--> NodeD[Node D]
    NodeD <--> NodeB
```

### Client-Server
A centralized architecture with distinct roles.

- **Roles:**
- **Server:** Provides resources (files, compute).
    - **Client:** Requests resources.
- **Pros:** Centralized control, Better security, Easier backups.
- **Cons:** Single point of failure (if Server goes down), Expensive hardware.
- **Example:** Web Browsing (Browser = Client, Website = Server), Email (Outlook = Client, GMail Server).

> [!TIP] AE2 Analogy: Controller & Terminals
> - **Server:** The **ME Controller + Drive Array**. It holds all the storage and manages power/channels. If the Controller breaks, everything goes offline (Single Point of Failure).
> - **Client:** The **Crafting Terminal**. It has no storage itself; it just "requests" items from the Drives (Server).

```mermaid
graph TD
    Server[Central Server]
    Client1[Client 1]
    Client2[Client 2]
    Client3[Client 3]

    Server <--> Client1
    Server <--> Client2
    Server <--> Client3
    
    style Server fill:#f9f,stroke:#333,stroke-width:1px
```

### Hybrid
Combines features of both P2P and Client-Server.

- **Goal:** To leverage the scalability of P2P and the control of Client-Server.
- **Mechanism:** Some nodes act as clients accessing a central server for authentication or indexing, while data transfer happens directly between peers.
- **Example:** BitTorrent (Tracker server + Peer download), Skype (Login server + P2P call).
- **Pros:** Scalable (P2P), Controlled (CS), Efficient.
- **Pros:** Scalable (P2P), Controlled (CS), Efficient.
- **Cons:** Complex implementation.

> [!TIP] AE2 Analogy: Sub-Networks
> You have your **Main Base Network** (Server) handling all storage. You also have a small, independent **Ore Processing Sub-Network** (Peer). It does its own work but connects to the Main Network via an **Interface + Storage Bus** to share the final ingots. It's independent (P2P-ish) but integrated (Client-Server).

```mermaid
graph TD
    %% Centralized Part (Client-Server)
    Server[Central Server]
    ClientA[Client A]
    ClientB[Client B]
    ClientC[Client C]

    Server --> ClientA
    Server --> ClientB
    Server --> ClientC

    %% Decentralized Part (P2P between Clients)
    ClientA <--> ClientB
    ClientB <--> ClientC

    style Server fill:#f9f,stroke:#333,stroke-width:2px
```


