Links: [[05 OSI Model]], [[00 Computer Networks]]
___
# Session Layer

The **Session Layer** (Layer 5 of the OSI Model) is responsible for establishing, managing, and terminating communication sessions between two computers. It essentially acts as the network's "dialog controller."

While the Transport Layer establishes the physical data connection, the Session Layer dictates *how* the applications interact over that connection.

> [!TIP] Analogy: AE2 Security Terminals & Wireless Links
> Think of the Session Layer as an **AE2 Wireless Receiver** or **Security Terminal** login. 
> 
> When you link a Wireless Terminal to your base, a "session" is established. The Session Layer manages this connection—it handles the authentication (login), maintains the active link while you're in range, and gracefully terminates the session when you disconnect. 
> 
> Furthermore, the **Synchronization (Checkpoints)** function is like the system's "save state"—if the wireless signal flickers, it doesn't forget who you are or what items you were looking at; it picks up right where the session left off.

## Core Responsibilities

### Dialog Control
The Session Layer decides which device is allowed to transmit data and when. It supports three modes of dialog:

- **Simplex:** Data flows in one direction only.
- **Half-Duplex:** Both devices can transmit data, but *only one at a time* (like a walkie-talkie). The Session layer uses data tokens to enforce whose turn it is to speak.
- **Full-Duplex:** Both devices can transmit and receive data simultaneously (like a telephone call).

### Synchronization (Checkpoints)
For long data transfers (like downloading a massive file), the Session Layer adds synchronization points (checkpoints) into the data stream.

- **Why?** If a 10 GB download crashes at 9.9 GB, it would be devastating to start over from 0 GB.
- **How it works:** The Session Layer inserts a checkpoint every 100 MB. If the connection drops at 550 MB, the system only needs to retransmit the data starting from the 500 MB checkpoint, rather than the entire file.

## Common Session Layer Protocols
Because modern networks (specifically the TCP/IP model) often merge Layers 5, 6, and 7 into a single "Application" layer, distinct Session layer protocols are less prominent today. However, legacy and specialized protocols still exist:

- **RPC (Remote Procedure Call):** Allows a program to execute code on a remote server as if it were a local function.
- **NetBIOS (Network Basic Input/Output System):** Allows applications on separate computers to communicate over a local area network (LAN).
- **PAP (Password Authentication Protocol):** Manages the initial login and authentication session over a Point-to-Point connection.
