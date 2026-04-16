Links: [[00 Computer Networks]], [[10 Data Link Layer]], [[08 Physical Layer]]
___
# Ethernet

**Ethernet** is the predominant technology for connecting devices in a wired Local Area Network (LAN) or Wide Area Network (WAN). It dictates how network devices format, transmit, and process data packets to communicate with one another effectively.

Ethernet standardizes the operation of both the **Physical Layer** and the **[[12 Multiple Access Protocols|Data Link Layer (MAC sublayer)]]**.

- **Standard:** Ethernet follows the **IEEE 802.3** set of networking protocol standards.

## Ethernet Generations

Ethernet has continually evolved since its invention (1973) to meet the demand for higher bandwidth, moving from coaxial cables to twisted-pair copper and fiber-optics.

| Generation               | Speed                          | Common Cable Types         | Variants (Nomenclature)            |
|:------------------------ |:------------------------------ |:-------------------------- |:---------------------------------- |
| **Traditional Ethernet** | 10 Mbps (Originally 2.94 Mbps) | Coaxial, Thicknet, Thinnet | 10BASE-T, 10BASE2                  |
| **Fast Ethernet**       | 100 Mbps                       | Twisted Pair, Fiber Optic  | 100BASE-TX, 100BASE-FX, 100BASE-T4 |
| **Gigabit Ethernet**     | 1 Gbps (1,000 Mbps)            | CAT5e, CAT6, Fiber Optic   | 1000BASE-T, 1000BASE-SX            |
| **10-Gigabit Ethernet**  | 10 Gbps                        | CAT6a, CAT7, Fiber Optic   | 10GBASE-T, 10GBASE-SR              |

> [!FAQ] Nomenclature Syntax (e.g., 100BASE-TX)
> - **100:** The speed in Megabits per second (Mbps).
> - **BASE:** Refers to "Baseband" signaling (meaning the signal occupies the broad frequency spectrum for transmitting completely).
> - **TX:** Refers to the physical medium type (T = Twisted Pair, F = Fiber, C = Coaxial).

## How Ethernet Works
Ethernet dictates both how the physical electrical signals are transmitted on the wire, and how raw data is packaged into structured formats for delivery.

> [!TIP] Analogy: The Standardized Postal System
> Think of Ethernet like the standardized postal service for a city (LAN). To ensure your letter (data) reaches its destination, it must be placed into a universally accepted envelope (Ethernet Frame) with a very clearly formatted "To" address and "From" address (MAC addresses) written on the outside.

#### The Ethernet Frame Structure
To transmit data, the Data Link Layer takes a network packet and wraps it into an **Ethernet Frame**. The IEEE 802.3 standard specifically defines the structure that every single frame must rigorously follow:

| Preamble |  SFD   | Destination MAC | Source MAC | Type / Length |  Payload Data   |   FCS   |
|:--------:|:------:|:---------------:|:----------:|:-------------:|:---------------:|:-------:|
| 7 Bytes  | 1 Byte |     6 Bytes     |  6 Bytes   |    2 Bytes    | 46 - 1500 Bytes | 4 Bytes |

- **Preamble & SFD:** Used to synchronize the sender and receiver's clocks and signal the very beginning of the frame.
- **Destination & Source MAC:** The physical hardware addresses of the recipient and sender.
- **Type / Length:** Identifies the upper-layer protocol (like IPv4 or IPv6) encapsulated within the payload.
- **Payload Data:** The actual data being transmitted. If it is less than 46 bytes, "padding" is added to meet the minimum size.
- **Frame Check Sequence (FCS):** A 4-byte CRC (Cyclic Redundancy Check) value used by the receiver to verify if the frame was corrupted during transmission.

## Ethernet Topologies
The physical arrangement of Ethernet networks has significantly evolved alongside its speeds.

#### Legacy Ethernet (Hubs)
Early implementations utilized a Half-Duplex **Bus** or **Star (with Hub)** topology. 

In a Hub, all connected ports belong to the exact same collision domain. If two computers transmit simultaneously, their signals physically collide. 

This required the strict use of the **CSMA/CD** protocol (Carrier Sense Multiple Access with Collision Detection) to manage traffic and resolve collisions.

#### Modern Ethernet (Switches)
Modern Ethernet overwhelmingly utilizes intelligent **Switches** in a Star topology. 

A Switch separates every single port into its own isolated collision domain. 

Devices communicate over dedicated point-to-point links (Full-Duplex), meaning they can simultaneously send and receive data. Because of this, collisions are virtually impossible, rendering CSMA/CD entirely obsolete in modern switched networks.
