Links: [[27 Application Layer]], [[00 Computer Networks]]
___
# DNS and Web Protocols

## Domain Name System (DNS)
To identify an entity on the internet, IP addresses are used. However, humans are incredibly bad at remembering raw 32-bit (IPv4) or 128-bit (IPv6) numbers. The **Domain Name System (DNS)** acts as the "phonebook" of the internet, mapping human-readable names (like `google.com`) to numerical IP addresses.

### Name Space
The names assigned to machines must be strictly unique.
- **Flat Name Space:** A simple list of unique names (e.g., `Host1`, `Host2`). It cannot scale globally because names will eventually collide, and it is impossible to manage centrally.
- **Hierarchical Name Space:** The internet uses a hierarchical structure to guarantee uniqueness. Names are divided into multiple parts, separated by dots (e.g., `mail.google.com`).

#### The Hierarchical DNS Tree
The DNS system is structured as an inverted tree, theoretically limited to 128 levels.

(TLD = Top Level Domains)

```mermaid
graph TD
    Root((Root Domain<br><b>.</b>))
    
    %% Top Level Domains (TLDs)
    com[<b>.com</b><br>Generic TLD]
    org[<b>.org</b><br>Generic TLD]
    uk[<b>.uk</b><br>Country TLD]
    
    %% Second Level Domains
    google[<b>google</b>.com]
    wiki[<b>wikipedia</b>.org]
    
    %% Subdomains
    mail[<b>mail</b>.google.com]
    drive[<b>drive</b>.google.com]
    
    Root --> com
    Root --> org
    Root --> uk
    
    com --> google
    org --> wiki
    
    google --> mail
    google --> drive
    
    style Root fill:#ef5350,stroke:#333,color:#fff
    style com fill:#ffb74d,stroke:#333
    style org fill:#ffb74d,stroke:#333
    style uk fill:#ffb74d,stroke:#333
```

### How DNS Works (Step-by-Step Resolution)

When you type a URL into your browser, a complex sequence of requests occurs across the global DNS hierarchy to resolve the name into a numerical IP address.

#### Recursive vs. Iterative Resolution

##### Recursive Resolution
In recursive resolution, the client (or resolver) delegates the entire task to a DNS server. That server is now responsible for finding the answer. If it doesn't have the IP in its cache, it contacts other servers on behalf of the client, acting as a middleman until it can return the final IP or an error.

```mermaid
sequenceDiagram
    participant C as Client (Resolver)
    participant S1 as DNS Server 1
    participant S2 as DNS Server 2
    participant S3 as Authoritative Server

    C->>S1: 1. Where is google.com?
    Note over S1: "I'll find it for you."
    S1->>S2: 2. Where is google.com?
    S2->>S3: 3. Where is google.com?
    S3-->>S2: 4. It is at 142.250.190.46
    S2-->>S1: 5. It is at 142.250.190.46
    S1-->>C: 6. Here is the IP!
```

##### Iterative Resolution
In iterative resolution, the DNS server does not perform the search for the client. Instead, if it doesn't know the answer, it provides a **Referral** (a "hint" pointing to the next authoritative server down the tree). The client (resolver) must then take that hint and manually contact the next server itself. This process repeats until the client reaches the Authoritative Server.

```mermaid
sequenceDiagram
    participant C as Client (Resolver)
    participant Root as Root Server (.)
    participant TLD as TLD Server (.com)
    participant Auth as Authoritative Server

    C->>Root: 1. Where is google.com?
    Root-->>C: 2. I don't know, but ask .com TLD (Referral)
    C->>TLD: 3. Where is google.com?
    TLD-->>C: 4. I don't know, but ask Auth Server (Referral)
    C->>Auth: 5. Where is google.com?
    Auth-->>C: 6. It is at 142.250.190.46
```

#### The Resolution Path
A standard real-world DNS lookup typically uses a **hybrid** approach:

1. **The User** performs a **Recursive Query** to the **DNS Resolver** (ISP/Google).
2. **The Resolver** then performs a series of **Iterative Queries** to the Root, TLD, and Authoritative servers to find the answer.
3. Once found, the Resolver caches the result and returns it to the User.

```mermaid
sequenceDiagram
    autonumber
    participant User as PC / Browser (The User)
    participant Res as DNS Resolver (ISP/8.8.8.8)
    participant Root as Root Server (.)
    participant TLD as TLD Server (.com)
    participant Auth as Authoritative Server (google.com)

    User->>Res: Where is google.com? (Recursive)
    Note over Res: Checks Cache... (Miss)
    Res->>Root: Where is google.com? (Iterative)
    Root-->>Res: I don't know, but ask .com TLD
    Res->>TLD: Where is google.com? (Iterative)
    TLD-->>Res: I don't know, but ask Authoritative NS
    Res->>Auth: Where is google.com? (Iterative)
    Auth-->>Res: It's at 142.250.190.46
    Res->>User: Here is the IP!
```

### DNS Spoofing (Cache Poisoning)
A severe cyberattack where an attacker feeds fake DNS data into a DNS resolver's cache. If a user asks for `facebook.com`, the poisoned DNS server maliciously redirects them to a fake IP address controlled by the hacker, entirely without the user's knowledge.

#### Prevention Methods
Modern networks employ several strict defenses against cache poisoning:
##### DNSSEC (DNS Security Extensions) 

The definitive solution. DNSSEC adds cryptographic digital signatures to DNS records. 

When a resolver receives an IP address, it verifies the signature using a public key to guarantee the data actually came from the authoritative server and wasn't altered in transit.

##### Port Randomization
Older DNS resolvers always used UDP Port 53 to send queries, making it easy for attackers to guess where to inject the fake response. 

Modern resolvers randomize the source port for every single query. This forces the attacker to guess both the 16-bit Transaction ID *and* the 16-bit Source Port, which is computationally infeasible before the real response arrives.

##### HTTPS / TLS 

While not a DNS-level fix, HTTPS serves as a crucial safety net. Even if a user is successfully spoofed and sent to a fake `facebook.com` IP address, the attacker's server will not possess the genuine cryptographic SSL/TLS certificate for Facebook. 

The victim's browser will immediately detect the mismatch and throw a massive security warning, blocking the connection.