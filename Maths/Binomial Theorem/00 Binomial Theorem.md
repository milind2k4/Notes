Links: [[01 Binomial Coefficient]]
___
# Binomial Theorem
**Factorial** of a natural number n is denoted as $n!$ and is defined as product of first n natural numbers. 
$$n! = 1.2.3.4\dots (n-1).n$$
And we an write,
$$n! = n(n-1)! = n(n-1)(n-2)! = \dots$$

Some useful factorials are,
$$
\begin{split}
0! &= 1 \\
1! &= 1 \\
2! &= 2 \\
3! &= 6 \\
4! &= 24 \\
5! &= 120 \\
6! &= 720
\end{split}
$$

$r!$ will be divisible by all natural number less than or equals to r. It may be divisible by number more than r as well.

![[Pasted image 20231124212054.png]]
![[Pasted image 20231124212731.png]]

#### Exponent of prime p in n!
If prime $p \leq n$ then its exponent in $n!$ when expressed in prime factorisation, is given as,
$$e = \left[ \frac{ n }{ p } \right] + \left[ \frac{ n }{ p^{2} } \right] + \left[ \frac{ n }{ p^{3} } \right] + \dots$$
where [.] indicates integral part and e the exponent.

This formula works because the term $\displaystyle \left[ \frac{ n }{ p } \right]$ gives no. of integers divisible by prime p  between 1 and n. Similarly $\displaystyle \left[ \frac{ n }{ p^{2} } \right]$ gives no. of integers divisible by $p^{2}$ and so on. Then the contribution of p, $p^{2}$ etc. is counted to give the final result.

![[Pasted image 20231124215405.png]]
![[Pasted image 20231124215419.png]]

## Multinomial Expansion
[[02 Binomial Expansion]]

In the expansion of $(ax + by + cz)^{n},\ n \in N$, the coefficients of $x^{\alpha},y^{\beta}, z^{\gamma},\ (\alpha, \beta, \gamma \in W)$ can be given as,
-  if $\alpha + \beta + \gamma \neq n$, then $0$.
- if $\alpha + \beta + \gamma = n$, then
  $$\frac{ n! }{ \alpha!\beta!\gamma! }$$


To find sum of coefficients in an expansion, put all variable terms = 1. And we can put $x = 1 /x$ to flip the series. 

Let $x_{1},x_{2},x_{3}\dots x_{r}$ are different variables, then the numbers of distinct terms in the expansion of $(x_{1} + x_{2} + x_{3} + \dots + x_{r})^{n}$ where $r, n \in N$, will be,
$$\text{no of terms} = {n+r-1 \choose r-1}$$

### Examples 
![[Pasted image 20231130203233.png]]
![[Pasted image 20231130203521.png]]

![[Pasted image 20231130204359.png]]
![[Pasted image 20231130204415.png]]
Alternatively for the last 3 parts,
![[Pasted image 20231130205253.png]]

![[Pasted image 20231130210815.png]]
![[Pasted image 20231130212152.png]]

## Misc. Examples 
**No. of rational terms:**
![[Pasted image 20231127182024.png]]
![[Pasted image 20231127183154.png]]

**Division problems:**
![[Pasted image 20231128200758.png]]
![[Pasted image 20231128200814.png]]

![[Pasted image 20231201153945.png]]

![[Pasted image 20231201155503.png]]

**Integral and Fractional Part in Binomial expansion,**
![[Pasted image 20231205101229.png]]
![[Pasted image 20231205101242.png]]
![[Pasted image 20231205101552.png]]

