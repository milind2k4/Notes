Links: [[27 Application Layer]], [[00 Computer Networks]]
___
# Network Management and Remote Access

## Simple Network Management Protocol (SNMP)
SNMP is an Application Layer protocol used to collect data from, and configure, network devices (like routers, switches, and servers) on an IP network.

> [!TIP] Analogy: The AE2 ME Controller & Storage Buses
> Think of SNMP as the global monitoring system for a massive AE2 network:
> - **SNMP Manager:** Your main **ME Terminal** or **ME Controller** interface. This is where you (the admin) look to see exactly how many resources you have and which machines are active.
> - **SNMP Agent:** This is like an **ME Storage Bus** or **ME Interface** attached to a specific machine. The machine "reports" its internal data (like how much power it’s using or how many items it has produced) back to the central controller.
> - **MIB (Management Information Base):** The specific "metadata" about that machine. For example, a Pulverizer reports its "Speed" and "Energy Usage" in its own MIB format, which the Manager understands.

### The Architecture
SNMP operates using a straightforward client-server model, but with specific terminology:

1. **SNMP Manager:** The centralized system (Client) used by a human network administrator to monitor the network.
2. **SNMP Agent:** A software module running on the actual managed device (Server/Router). The agent collects local hardware data (CPU usage, bandwidth, errors) and sends it to the Manager when requested.

### SMI and MIB
To ensure that a Cisco router and a Juniper switch can both be understood by the same SNMP Manager, the data must be standardized.

- **SMI (Structure of Management Information):** The strict set of rules defining exactly how data should be named and formatted.
- **MIB (Management Information Base):** A virtual database located on the Agent. It stores the actual statistical data about the device (e.g., "Interface 1 has dropped 40 packets"). The Manager reads the MIB to determine the health of the device.

## Remote Access Protocols
Network administrators frequently need to log into remote servers or routers to configure them via a command-line interface.

### Telnet
Telnet is one of the earliest remote access protocols (operating on TCP Port 23). It establishes a remote connection allowing a user to log into a server and execute commands as if they were physically sitting in front of the machine's keyboard and monitor.

#### Network Virtual Terminal (NVT)
Because different operating systems (like Windows, Linux, or legacy mainframes) use completely different character codes for basic keystrokes (like `Enter` or `Backspace`), Telnet uses a universal intermediate format called the **Network Virtual Terminal (NVT).**

- The Client's Telnet software translates the local keystrokes into standard NVT characters.
- These NVT characters are sent across the network.
- The Server's Telnet software translates the NVT characters back into the specific format the remote OS expects.

#### The Fatal Flaw
Telnet transmits all data—including keystrokes, usernames, and passwords—in **completely plain text.**

Anyone sniffing the network traffic with a tool like Wireshark can easily steal the credentials by simply reading the packets. 

For this reason, Telnet is considered highly insecure and is virtually obsolete on the modern internet.

### SSH (Secure Shell)
SSH was designed specifically as a secure replacement for Telnet. It provides the exact same virtual terminal functionality, but wraps the entire session in strong cryptographic encryption.

#### How It Works
1. **Authentication:** Uses Public Key Cryptography (like RSA) to authenticate the remote computer and optionally the user.
2. **Encryption:** Once authenticated, a Symmetric Key is generated to encrypt all the data flowing through the terminal session. Even if a hacker intercepts the packets, they will only see mathematical garbage.

#### Uses of SSH
- Securely accessing and administering remote Linux servers.
- Securely transferring files via SFTP (SSH File Transfer Protocol).

> [!TIP] SSH Port Forwarding (Tunneling)
> SSH can be used to create an encrypted "tunnel" between your local machine and a remote server. 
> 
> **Analogy: AE2 Quantum Network Bridges**
> In AE2, if you have two isolated networks in different dimensions, you can’t just run a cable through the void. Instead, you use a **Quantum Network Bridge**. This creates a single, specific "link" that tunnels data between the two locations as if they were directly connected. 
> 
> **SSH Port Forwarding** does the exact same thing for software: it takes a local port (Dimension A) and bridges it securely through the SSH tunnel to a remote port (Dimension B), bypassing any "walls" or firewalls in between.
> 
> Imagine a company has an internal database running on Port 5432 that is heavily firewalled and blocks all outside internet traffic. However, the firewall *does* allow SSH traffic on Port 22. 
> 
> By using **Local Port Forwarding**, you can tell your SSH client: *"Take any traffic I send to my local Port 5432, encrypt it, shove it through the SSH tunnel on Port 22, and when it reaches the remote server, decrypt it and forward it directly to the internal database."*
> 
> This allows you to securely access internal resources from the outside world without exposing the database to the public internet.

#### Example: Connecting to an Amazon EC2 Server
When you spin up a virtual Linux server (an EC2 instance) on Amazon Web Services (AWS), they provide you with a `.pem` file. This file contains your Private Key for RSA authentication.

To securely log into the remote server from your local terminal, you use the following SSH command:

```bash
ssh -i "my-secret-key.pem" ec2-user@ec2-198-51-100-24.compute-1.amazonaws.com
```

**Command Breakdown:**

- `ssh`: Invokes the SSH client program.
- `-i "my-secret-key.pem"`: Tells the client to use this specific Private Key file for authentication (instead of relying on a weak password).
- `ec2-user`: The default username for Amazon Linux instances.
- `@ec2-198-51-100-24...`: The Hostname (or IP address) of the remote AWS server you are connecting to.
