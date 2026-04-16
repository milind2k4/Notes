Links: [[10 Data Link Layer]]
___
# Error Control
Errors can occur due to noise or interference, changing `0`s to `1`s or vice versa.

- **Single-bit Error:** Only one bit in a data unit is changed.
- **Burst Error:** Two or more bits in a data unit are changed.

### Error Detection Techniques
These techniques allow the receiver to detect if an error has occurred.

#### Parity Check
Adds an extra bit (redundancy bit) to make the total number of `1`s even or odd.

##### Simple Parity Check
Detects single-bit errors.
- **Even Parity:** The parity bit is set so that the total number of `1`s (including the parity bit) is **Even**.
- **Odd Parity:** The parity bit is set so that the total number of `1`s is **Odd**.

> [!EXAMPLE] Even Parity
> - **Data:** `1011001` (contains four `1`s)
> - **Parity Bit:** `0` (since 4 is already even)
> - **Transmitted:** `1011001` + `0` = `10110010`

##### 2D Parity Check (LRC & VRC)
2D Parity check (Two-Dimensional Parity Check) organizes data into a table to detect and correct errors more effectively.

- **VRC (Vertical Redundancy Check):** Parity is calculated for each data unit (row) independently. This is the **Row Parity**.
- **LRC (Longitudinal Redundancy Check):** Parity is calculated across all data units for each bit position (column). This is the **Column Parity**.

**How it works:**
1. Data units are arranged in a block of rows and columns.
2. A parity bit is added to each row (VRC).
3. A parity bit is added to each column (LRC).
4. The entire block, including the parity bits, is transmitted.

> [!TIP] Detection & Correction
> - **Detection:** Can detect all single-bit errors, burst errors affecting specific rows/columns, and most multiple-bit errors.
> - **Correction:** If a **single bit** flips, it will cause a parity mismatch in exactly **one row** and **one column**. The intersection of that row and column identifies the corrupted bit, allowing it to be flipped back.

> [!NOTE] 
> Even if up to 3 bits are corrupted, 2D parity can typically detect the error, though it might only be able to correct single-bit errors.

**Example Matrix (Even Parity):**

| Data Unit            | Bit 1 | Bit 2 | Bit 3 | Bit 4 | Row Parity (VRC) |
|:-------------------- |:----- |:----- |:----- |:----- |:---------------- |
| Row 1                | 1     | 1     | 0     | 0     | **0**            |
| Row 2                | 1     | 0     | 1     | 0     | **0**            |
| Row 3                | 0     | 1     | 1     | 1     | **1**            |
| **Col Parity (LRC)** | **0** | **0** | **0** | **1** | **1**            |

**Received Data (with error at Row 2, Bit 3):**

| Data Unit            | Bit 1 | Bit 2 | Bit 3     | Bit 4 | Row Parity (VRC) | Status                              |
|:-------------------- |:----- |:----- |:--------- |:----- |:---------------- |:----------------------------------- |
| Row 1                | 1     | 1     | 0         | 0     | **0**            | OK                                  |
| Row 2                | 1     | 0     | **0**     | 0     | **0**            | **ERROR** (Sum is 1, expected Even) |
| Row 3                | 0     | 1     | 1         | 1     | **1**            | OK                                  |
| **Col Parity (LRC)** | **0** | **0** | **0**     | **1** | **1**            | -                                   |
| **Status**           | OK    | OK    | **ERROR** | OK    | -                | -                                   |

**Result:** The intersection of **Row 2** and **Bit 3** shows a parity mismatch. The receiver knows exactly which bit is wrong and flips it back to `1`.

#### Checksum
Used widely in the Internet (IP/TCP) to check for errors in "words".

**Steps on Sender Side:**
1. Divide data into $k$ segments of $n$ bits each (words).
2. Add all sections using binary addition.
3. If there is a carry, add it back to the sum (**1's complement addition**).
4. Complement the final sum (flip bits) to get the **Checksum**.
5. Transmit Data + Checksum.

> [!EXAMPLE] Checksum Calculation
> **Data:** `1001` and `0011` ($k=2, n=4$)
> 1. **Sum:** `1001` + `0011` = `1100`
> 2. **Checksum (1's complement of Sum):** `0011`
> 3. **Result:** Transmission contains `1001`, `0011`, and `0011`.

**On Receiver Side:**
1. Add all received segments (data words) and the checksum together using binary addition.
2. If there is a carry, add it back to the sum.
3. Complement the final result.
4. **Decision:** 
    - If the result is **all `0`s**, the data is accepted (No error).
    - If the result is **non-zero**, the data is rejected (Error detected).

> [!EXAMPLE] Receiver Side
> Using the same data from the sender side: `1001`, `0011` and Checksum: `0011`.
> 1. **Sum segments:** `1001` + `0011` + `0011` (Checksum)
> 2. `1001` + `0011` = `1100`
> 3. `1100` + `1011` = `1111`
> 4. **Complement of `1111`** = **`0000`** $\to$ **Data Accepted!**

#### Cyclic Redundancy Check (CRC)
Uses binary division and generator polynomials.
- Both sender and receiver agree on a **Generator Polynomial** (Key).
- Popular Polynomials:
    - CRC-8 (ATM Header): 
	$$x^{8} + x^{2} + x + 1$$
	- CRC-10 (ATM Adaption Layer (AAL)): 
	$$x^{10} + x^{9} + x^{5} + x^{4} + x^{2} + 1$$
	- ITU-16 (HDLC (High Level Data Link Control)): 
	$$x^{16} + x^{12} + x^{5} + 1$$
	- ITU-32 (LAN Cables)
		$$x^{32} + x^{26} + x^{23} + x^{22} + x^{16} + x^{12} + x^{11} + x^{10} + x^{8} + x^{7} + x^{5} + x^{4} + x^{2} + x + 1$$

> [!EXAMPLE] CRC Calculation Walkthrough
> **Sender Side:**
> 1. **Data:** `1001`
> 2. **Generator:** `1011` (Since Generator length is 4, we append 3 zeros to the data)
> 3. **Appended Data:** `1001000`
> 4. **Binary Division (Using XOR):**
>    Divide `1001000` by `1011`.
>    - `1001` XOR `1011` = `0010`
>    - Bring down `0`, current = `0100` (Leading bit is 0, XOR with `0000`) $\to$ `0100`
>    - Bring down `0`, current = `1000` (Leading bit is 1, XOR with `1011`) $\to$ `0011`
>    - Bring down `0`, current = `0110` (Leading bit is 0, XOR with `0000`) $\to$ `0110`
> 5. **Remainder (CRC):** `110`
> 6. **Transmitted Data:** Data + CRC = `1001110`
>
> **Receiver Side:**
> 1. Divides the received data (`1001110`) by the exact same generator (`1011`).
> 2. If the remainder is all zeros (`000`), the data is accepted. Otherwise, it is rejected.

### Error Correction: Hamming Code
Hamming code can both detect and correct errors.
- **Parity Bit Positions:** Bits at positions $2^n$ (1, 2, 4, 8...) are reserved for parity ($P_1, P_2, P_4 \dots$).
- **Data Bit Positions:** All other positions are used for actual data ($D_3, D_5, D_6, D_7 \dots$).
- The value of parity bits is calculated based on specific combinations of data bits to ensure error detection can pinpoint the exact faulty bit.

> [!EXAMPLE] Hamming Code Calculation (Even Parity)
> **Goal:** Send data `1011` (4 bits). Let's compute the Hamming Code.
> 
> **1. Calculate Number of Parity Bits ($r$):**
> We need 3 parity bits. Total length = 7 bits.
> 
> **2. Assign Positions:**
> | Position | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
> | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
> | **Type** | $P_1$ | $P_2$ | $D_3$ | $P_4$ | $D_5$ | $D_6$ | $D_7$ |
> | **Value**| ? | ? | **1** | ? | **0** | **1** | **1** |
> 
> **3. Calculate Parity Bits (Even Parity):**
> - **$P_1$** (checks 1, 3, 5, 7): Data at bits 3, 5, 7 is `1`, `0`, `1`. There are two `1`s (already even), so **$P_1 = 0$**.
> - **$P_2$** (checks 2, 3, 6, 7): Data at bits 3, 6, 7 is `1`, `1`, `1`. There are three `1`s (odd), so **$P_2 = 1$**.
> - **$P_4$** (checks 4, 5, 6, 7): Data at bits 5, 6, 7 is `0`, `1`, `1`. There are two `1`s (already even), so **$P_4 = 0$**.
> 
> **4. Final Transmitted Data:**
> The final transmitted 7-bit word is **`0110011`**.
>
> **5. Correction Logic (Receiver):**
> The receiver recalculates $P_1, P_2, P_4$. If errors are detected, the incorrect parity values (read backwards, like $P_4P_2P_1$) form the binary integer of the exact corrupted bit's position. For example, if the result is binary `101`, position `5` is corrupted. The receiver simply flips the 5th bit to correct it!
