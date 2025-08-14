Links: [[02 Properties of Log]]
___
# Characteristic & Mantissa
### Characteristic
The Integral part of $\log$.
$\log_{b}a =T$
$[T] \to \text{Characteristic}$

### Mantissa
The Fractional part of $\log$.
$\log_{b}a = T$
$\{T\} \to \text{Mantissa}$

## Notes
1. Number of integers having C $\alpha$ if base is $\beta$ are:
$$
\begin{split}
(\beta^{\alpha+1} & - \beta^{\alpha} - 1) + 1 \\
\implies \beta^{\alpha+1} & - \beta^{\alpha} \\
\implies \beta^{\alpha}(\beta & - 1)
\end{split}
$$
   +1 is due to $\beta^{\alpha}$ as it's C is also $\alpha$. 

2. If base is 10 then changing the position of the decimal point has no effect on the Mantissa. 
**Proof: **
$$
\begin{split}
\text{Let } & x = \text{pq.rs}\ \&\ y = \text{0.pqrs} \\
\text{Then, } & \\
& \log_{10}x = \log_{10}(\text{pq.rs}) = C + M \\
\text{Again, } & \\
& \log_{10}y = \log_{10}(\text{0.pqrs}) \\
\implies & \log_{10}(\text{pq.rs} \times 10^{-2}) \\
\implies & \log_{10}(\text{pq.rs}) + \log_{10}10^{-2} \\
\implies & (C+M) + -2 \\
\implies & (C-2)+M \\
\therefore\ & \text{M is unchanged.} \\
\end{split}
$$

3. If base of log is 10 then if a +ve number n has C $\alpha$ then its integral will have $\alpha+1$ digits.
   i.e. if $\log_{10}n = C.M$ then $[n]$ has digits C + 1

3. If $l$ is a positive fraction and its characteristic of log with base 10 is $-a$ then there will be $a-1$ number of zeros after decimal point and before first non-zero digit. 
   e.g. $\log_{10}0.0083 = -2.sth = -3 + 0.sth$, here C is $-3$ and the number has 2 zeros after decimal
   
   ![[Pasted image 20230428075649.png]]

## Number of Digits in an Integer
When a natural number has [[03 Characteristic & Mantissa#Characteristic|characteristic]] $'\alpha'$ (when base is 10)
then it has $\alpha+1$ digits.

> $$\log_{10}10 = 1$$
> $$\log_{10}100 = 2$$
> $$\log_{10}70 = 1.sth$$ 
> $$\text{And 70 has 1+1 = 2 digits.}$$

![[Pasted image 20230428074509.png]]

### For numbers less than 1
If a $+ve$ fraction has characteristic $-\alpha$ (when base is 10), then number of zeros between decimal point and the 1st significant digit will be $\alpha-1$

> $$\log_{10}0.1 = -1$$
> $$\log_{10}0.01 = -2$$
> $$\log_{10}0.001 = -3$$
> $$\log_{10}0.0073 = -2.sth$$
> $$\text{And it has 2 zeros b/w the decimal and the first sig. fig.}$$

**To solve questions, convert all the terms into powers of 10 or the arguments as given in the question.**