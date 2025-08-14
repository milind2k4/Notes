Links: [[00 Binomial Theorem]]
___
# Divisibility and Last Digits
If we divide an integer by a natural no. k, then remainder will be one of the numbers among $0,1,2,3 \dots k-1$.
i.e. division by k will result in k types of remainders. 

If an integer n is divided by a natural number p, and if quotient is q and remainder is r, then this info. can be written as,
$$n = q.p + r$$
Also, $r \in \{ 0,1,2,3\dots p-1 \}$.

Remainder can also be denoted as,
$$R\left( \frac{n}{p} \right) = r$$

Note that we do not cancel. 
![[Pasted image 20231205102232.png]]

Thus,
$$
\begin{split}
R\left( \frac{ kn }{ kp } \right) &\neq R\left( \frac{ n }{ p } \right) \\
R\left( \frac{ kp + n }{ p } \right) &= R\left( \frac{ n }{ p } \right) \\
\end{split}
$$
If $n < p$ and $p, n \in N$, then,
$$R\left( \frac{ n }{ p } \right) = n$$

#### Finding Remainder
To calculate the remainder when $n^{m}$ is divided by $p$, identify the exponent of n which has difference of 1 with some multiple of p. 

Once identified, express, $n^{m}$ in the terms of this exponent and hence find required remainder.

![[Pasted image 20231205105709.png]]
![[Pasted image 20231205110328.png]]

#### Divisbility of Difference of Powers
From [[02 Formula and Expansions#Factorization of Difference]],

For $n \in N$, $x^{n} - y^{n}$ will be divisible by $x - y$.

For odd integer $n$, $x^{n} + y^{n}$ will be divisible by $x + y$.

![[Pasted image 20231205111009.png]]

![[Pasted image 20231205111642.png]]

### Last Digits

#### Unit Digit
Unit digit of $n^{m}$ repeats in cyclic order. 

For example, for 2,
![[Pasted image 20231205113034.png]]

For other numbers also, this is applicable.

Whose unit digit does not change,

|   No.   | Unit Digit |
|:-------:|:----------:|
| $0^{m}$ |     0      |
| $1^{m}$ |     1      |
| $5^{m}$ |     5      |
| $6^{m}$ |     6      | 

**Whose unit digit cycles in 4,**

|  $2^{m}$   | Unit digit |
|:----------:|:----------:|
| $2^{4k+1}$ |     2      |
| $2^{4k+2}$ |     4      |
| $2^{4k+3}$ |     8      |
|  $2^{4k}$  |     6      |

$\\$

|  $3^{m}$   | Unit digit |
|:----------:|:----------:|
| $3^{4k+1}$ |     3      |
| $3^{4k+2}$ |     9      |
| $3^{4k+3}$ |     7      |
|  $3^{4k}$  |     1      | 

$\\$

|  $7^{m}$   | Unit digit |
|:----------:|:----------:|
| $7^{4k+1}$ |     7      |
| $7^{4k+2}$ |     9      |
| $7^{4k+3}$ |     3      |
|  $7^{4k}$  |     1      | 

$\\$

|  $8^{m}$   | Unit digit |
|:----------:|:----------:|
| $8^{4k+1}$ |     8      |
| $8^{4k+2}$ |     4      |
| $8^{4k+3}$ |     2      | 
|  $8^{4k}$  |     6      |

**Whose unit digit cycles in 2,**

|  $4^{m}$   | Unit digit |
|:----------:|:----------:|
| $4^{2k+1}$ |     4      | 
|  $4^{2k}$  |     6      |

$\\$

|  $9^{m}$   | Unit digit |
|:----------:|:----------:|
| $9^{2k+1}$ |     9      |
|  $9^{2k}$  |     1      | 


For example,
![[Pasted image 20231205113250.png]]

#### Last Digits 
To find last digits of $n^{m}$ if unit digit of n is 1,3,7,9 then express it as a multiple of 10 $\pm$ 1 then expand.

![[Pasted image 20231205114108.png]]
![[Pasted image 20231205114115.png]]
