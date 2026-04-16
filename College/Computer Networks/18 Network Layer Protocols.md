Links: [[00 Computer Networks]], [[15 Network Layer]]
___
# Network Layer Protocols

The Network Layer utilizes several auxiliary protocols to support the delivery of IP datagrams. These protocols handle tasks that the base IP protocol cannot do inherently, such as physical address mapping, error reporting, and multicasting.

## Physical Mapping Protocols

Because local network devices communicate via Physical (MAC) addresses at the Data Link Layer, but remote devices route packets using Logical (IP) addresses, protocols are required to map these two addressing schemes together.

### ARP (Address Resolution Protocol)
ARP is responsible for converting a known **Logical Address (IP)** to an unknown **Physical Address (MAC)**. 

In a Local Area Network (LAN), every device in a physical link is strictly identified by its MAC address. When a device knows the target IP address but not the target MAC address, it uses ARP.

- **Request:** The sender **broadcasts** an ARP Request pack to all devices on the local subnet ("Who has this IP address?").
- **Response:** The device that actually owns the requested IP address sends a **unicast** ARP Reply directly back to the sender ("That's me, here is my MAC address").

> [!TIP] Analogy: ME Terminal Searching
> Think of ARP like querying an AE2 ME Terminal. You request a purely logical concept (e.g., "Give me 1 Iron Ingot" / IP Address), and the ME system must broadcast a search across the entire cabling network to discover exactly which physical Storage Drive (MAC Address) actually houses the item before it can be retrieved.

![[Pasted image 20260408095229.png]]

![[Pasted image 20260408095256.png]]

*Note: The Target Hardware address field is initially left blank but is ultimately filled in by the responding node or router.*

### RARP (Reverse ARP)
RARP operates perfectly in reverse to ARP. It finds the **Logical Address (IP)** for a machine when its **Physical Address (MAC)** is already known.

This is typically used when a diskless machine boots up and needs to discover its assigned IP address from a central RARP server.
- **Request:** The RARP request is **broadcasted** with the machine's MAC address.
- **Response:** The RARP server replies in **unicast** with the assigned IP address.

![[Pasted image 20260408095949.png]]

![[Pasted image 20260408100050.png]]

## Control & Error Protocol

### Internet Control Message Protocol (ICMP)
The base IP protocol does not have any built-in mechanisms for error reporting or correction. If a router discards a packet due to a time-out or unreachable destination, IP alone has no way of informing the original sender. The **ICMP suite** was created explicitly to solve this by handling operational queries and reporting errors.

ICMP serves two primary uses:

1. **Error Reporting:** (e.g., Destination Unreachable, Time Exceeded/TTL expiration).
2. **Operational Queries:** (e.g., Echo Requests/Replies used by the `ping` command network diagnostic tool).

> [!TIP] Analogy: AE2 Smart Cable Tooltips
> Without the WAILA/The One Probe tooltips or Smart Cable visual indicators, an AE2 network has no way of reporting why a device isn't working — it simply shuts down if it lacks power or a channel. ICMP operates exactly like a Smart Cable: it provides active, back-channel diagnostic reports ("Network Unreachable", "Missing Route") so you aren't left in the dark when silent failures happen.

### How ICMP Works
- ICMP is a connectionless protocol (meaning no handshake is required).
- ICMP messages are purely informational. They are **encapsulated** directly within the payload of a standard IP datagram.
- Devices (hosts, routers, gateways) automatically generate and send ICMP packets back to a sender the moment they are forced to drop the sender's packet.

## Multicast Protocol (IGMP)

### Internet Group Management Protocol (IGMP)
IGMP is the primary communication protocol used by hosts and adjacent routers to orchestrate and manage **Multicast Groups** across IPv4 networks.

Multicasting allows a single sender to transmit data to a specific, subscribed group of multiple receivers simultaneously, rather than broadcasting it inefficiently to every device on a network. 

- **Primary Uses:** Streaming internet television, Web Conferencing, and Online Gaming relying on synchronized, multi-client states.
- **IPv6 Successor:** In IPv6 environments, IGMP has been entirely replaced by **MLDP (Multicast Listener Discovery Protocol)**.

> [!TIP] Analogy: Multicasting via P2P Tunnels
> IGMP is functionally identical to configuring a many-to-one or one-to-many AE2 **P2P Tunnel**. 
> 
> Instead of running heavy, individual dense cables to every single molecular assembler across your base (Unicasting), you multicast. 
> 
> You link one main P2P input to a specific "group" of P2P outputs. Data passing through the input is replicated only to those subscribed outputs, saving massive network channel overhead.
