Links: [[00 Binomial Theorem]]
___
# Binomial Coefficient
${}^{n}C_{r}$ is called binomial coefficient and is defined as no. of ways of selecting r objects from n different object.

$${}^{n}C_{r} = \binom{n}{r} =  {n \choose r} = \frac{ n! }{ r!(n-r)! }$$
Which can also be written as,
$${}^{n}C_{r} = \frac{ n.(n-1).(n-2).(n-3) \dots (n-r+1) }{ r! }$$
where the num. will have r terms. 

##### Properties of Combination
$${}^{n}C_{r} = {}^{n}C_{n-r}$$

This can be intuitively understood by the fact that the ratio of selection and rejection is 1. If we are selecting r, then we are rejecting n-r and both must be equal. 

For ${}^{n}C_{r}$ to be defined, $n \in N$ and $r \in W$ and $n \geq r$. 

Some combinations,
$$
\begin{split}
{}^{n}C_{0} &= {}^{n}C_{n} = 1 \\
{}^{n}C_{1} &= {}^{n}C_{n-1} = n \\
{}^{n}C_{2} &= {}^{n}C_{n-2} = \frac{ n(n-1) }{ 2 }
\end{split}
$$

If two combinations are equal,
$${}^{n}C_{x} = {}^{n}C_{y}$$
then, either $x = y$ or $x + y = n$.

From the alternate formula,
$${}^{n}C_{r} = \frac{ n.(n-1).(n-2).(n-3) \dots (n-r+1) }{ r! }$$
since this is an integer, the num. will be divisible by $r!$

Thus, *product of any r consecutive integers is divisible by $r!$.* 

If $p$ is a prime number, then ${}^{p}C_{r}$ will be divisible by p for all $r = 1,2,3 \dots, p-1$. 
I.e. all binomial coefficients will be divisible by p except the first and the last. 

Now,
$$
\begin{split}
{p \choose r} &= \frac{ p(p-1)(p-2) \dots (p-r+1) }{ r! } \\
&= p(\text{Integer})
\end{split}
$$
as p is prime and $r < p$, hence no factor of $r!$ can cancel out p from the numerator. 
I.e. ${}^{p}C_{r}$ is divisible by $p$. 

##### Some Results 
$${}^{n}C_{r} + {}^{n}C_{r-1} = {}^{n+1}C_{r}$$
> Proof:
> $$
> \begin{split}
> {}^{n}C_{r} + {}^{n}C_{r-1} &= \frac{ n! }{ r!(n-r)! } + \frac{ n! }{ (r-1)!(n-r+1)! } \\
> &= \frac{ n! }{ r!(n-r+1)! } (n-r+1 + r) \\
> &= \frac{ (n+1)! }{ r!(n+1-r)! } \\
> &= {}^{n+1}C_{r}
> \end{split}
> $$

$${}^{r}C_{r} + {}^{r+1}C_{r} + {}^{r+2}C_{r} + \dots {}^{n}C_{r} = {}^{n+1}C_{r+1}$$
![[Pasted image 20231201163403.png]]

$$\frac{ {}^{n}C_{r} }{ {}^{n}C_{r-1} } = \frac{ n - r + 1 }{ r }$$
> Proof:
> $$
> \begin{split}
> \frac{ {}^{n}C_{r} }{ {}^{n}C_{r-1} } &= \frac{ \frac{ n! }{ r!(n-r!) } }{ \frac{ n! }{ (r-1)!(n-r+1)! } } \\
> &= \frac{ 1 /r }{ 1 /n-r+1 } \\
> &= \frac{ n - r + 1 }{ r }
> \end{split}
> $$

$$r.{}^{n}C_{r} = n. {}^{n-1}C_{r-1}$$
> Proof:
> $$
> \begin{split}
> r.{}^{n}C_{r} &= \frac{ r.n! }{ r!(n-r)! } \\
> &= \frac{ r }{ r } \frac{ n (n-1)! }{ (r-1)!(n-r)! } \\
> &= n. {}^{n-1}C_{r-1} 
> \end{split}
> $$

### Examples 
![[Pasted image 20231127171129.png]]

Shortcut of this,
![[Pasted image 20231127171554.png]]

![[Pasted image 20231127172511.png]]
![[Pasted image 20231127184214.png]]
![[Pasted image 20231127184250.png]]
![[Pasted image 20231201154557.png]]

![[Pasted image 20231201155847.png]]

![[Pasted image 20231201161712.png]]
![[Pasted image 20231201161746.png]]

![[Pasted image 20231201162549.png]]
![[Pasted image 20231201162604.png]]

![[Pasted image 20231201154306.png]]

![[Pasted image 20231201165105.png]]
![[Pasted image 20231201165112.png]]