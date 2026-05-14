Links: [[00 Computer Networks]]
___
# Network Security and Cryptography

Network security involves policies and practices adopted to prevent and monitor unauthorized access, misuse, modification, or denial of a computer network and network-accessible resources.

## Cryptography
Cryptography is the process of converting readable data (plaintext) into an unreadable format (ciphertext) to secure it from unauthorized access.

- **Symmetric Encryption:** Both the sender and receiver use the exact *same* secret key to encrypt and decrypt the message. (Fast, but requires a secure way to share the key initially).
- **Asymmetric Encryption:** Uses a mathematically linked pair of keys: a **Public Key** (shared with everyone) to encrypt the message, and a **Private Key** (kept absolutely secret) to decrypt it.

### RSA Encryption Algorithm
RSA (Rivest-Shamir-Adleman) is one of the oldest and most widely used **Asymmetric** encryption algorithms. It relies on the mathematical difficulty of factoring the product of two massive prime numbers.

#### RSA Steps

##### Key Generation
Choose two distinct prime numbers, $p$ and $q$.

Calculate $n$,
$$n = p \times q$$
*(This $n$ is used as the modulus for both public and private keys).*

Calculate the totient,
$$\phi(n) = (p-1) \times (q-1)$$

Choose an integer $e$ (Public Key) such that $1 < e < \phi(n)$, and $e$ is coprime to $\phi(n)$ (meaning their greatest common divisor is 1).

Compute $d$ (Private Key) to satisfy the congruence relation,
$$d \times e \equiv 1 \bmod{\phi(n)}$$

##### Encryption

The sender converts a message into a number $M$, and uses the receiver's Public Key $(e, n)$ to create the Ciphertext ($c$),
$$c = M^{e \pmod{n}}$$

##### Decryption
The receiver uses their own secretly held Private Key $(d, n)$ to recover the original message ($M$),
$$M = c^d \bmod{n}$$

> [!EXAMPLE] RSA Numerical Walkthrough
> Let's encrypt the message $M = 9$.
> 
> **1. Key Generation:**
> - Let $p = 3$ and $q = 11$.
> - $n = 3 \times 11 = \mathbf{33}$.
> - $\phi(n) = (3-1) \times (11-1) = 2 \times 10 = \mathbf{20}$.
> - Choose $e = 3$ (since 3 and 20 are coprime). 
>   **Public Key = (3, 33)**.
> - Calculate $d$ such that $(d \times 3) \pmod{20} = 1$. 
>   The number 7 works, since $7 \times 3 = 21$, and $21 \pmod{20} = 1$
>   **Private Key = (7, 33)**.
> 
> **2. Encryption:**
> - $c = 9^3 \pmod{33} = 729 \pmod{33} = \mathbf{3}$.
> - The encrypted ciphertext sent across the network is **3**.
> 
> **3. Decryption:**
> - $M = 3^7 \pmod{33} = 2187 \pmod{33} = \mathbf{9}$.
> - The original message **9** is successfully recovered!

## Digital Signatures
A Digital Signature is a mathematical scheme used to verify the authenticity and integrity of a digital message or document.

Unlike normal encryption (where you encrypt with the receiver's *Public Key* so only they can read it), a Digital Signature works in reverse:
1. The sender explicitly encrypts the signature using their own **Private Key**.
2. The receiver uses the sender's openly available **Public Key** to decrypt it.

> [!NOTE] Why does this work?
> If the signature successfully decrypts using the sender's Public Key, it provides mathematical proof that it **must** have been encrypted by the corresponding Private Key. Since only the sender possesses the Private Key, it guarantees the sender is exactly who they claim to be (Authenticity).
