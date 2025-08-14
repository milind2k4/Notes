Links: [[00 Straight Line]]
___
# Section Formula
Let $A:(x_{1},y_{1})$ and $B:(x_{2},y_{2})$ are two given points, then coordinates of a point P dividing AB in the ratio $\lambda:\mu$ can be given as,

$$P:\left( \frac{ \lambda x_{2} + \mu x_{1} }{ \lambda + \mu }, \frac{ \lambda y_{2} + \mu y_{1} }{ \lambda + \mu } \right)$$

> **Proof:**
> $$
> \begin{split}
> \Delta APC \sim \Delta ABD \\
> \frac{ AC }{ AP } &= \frac{ AD }{ AB } \\
> \frac{ AD }{ AC } &= \frac{ AB }{ AP } \\
> \frac{ AD }{ AC } - 1 &= \frac{ AB }{ AP } - 1 \\
> \frac{ CD }{ AC } &= \frac{ PB }{ AP } \\
> &= \frac{ \mu }{ \lambda } \text{ (given)} \\
> \frac{ x_{2} - x_{p} }{ x_{p} - x_{1} } &= \frac{ \mu }{ \lambda  } \\
> x_{p} &= \frac{ \lambda x_{2} + \mu x_{1} }{ \lambda + \mu } \\
> \text{By Symmetry,} \\
> y_{p} &= \frac{ \lambda y_{2} + \mu y_{1} }{ \lambda + \mu } 
> \end{split}
> $$

![[Pasted image 20230705081548.png]]

Coordinates of mid point of AB are given as,
$$M:\left( \frac{ x_{1} + x_{2} }{ 2 }, \frac{ y_{1} + y_{2} }{ 2 } \right)$$
If P divides AB in the ratio $3:2$ internally then that means that the distance from A is 3 parts and from B is 2 parts.
![[Pasted image 20230705082143.png]]

If P divides BA in the ratio $3:2$ then that means that the distance from B is 3 parts and from A is 2 parts. Thus we count from the first point.
![[Pasted image 20230705082150.png]]

#### External Division
If P divides AB externally in the ratio $\lambda : \mu$ then take -ve sign with any one of $\lambda$ or $\mu$. 
$$P:\left( \frac{ \lambda x_{2} - \mu x_{1} }{ \lambda - \mu }, \frac{ \lambda y_{2} - \mu y_{1} }{ \lambda - \mu } \right)$$

As we more closer to either of the points the ratio tends to infinite and as we move farther away the ratio tends to 1/1.

In external division if P divides AB in the ratio $\lambda : \mu$ then P will be on the side of A if $\lambda < \mu$. This is because if it is on the side of B then the point will be closer to B than A which is opposite to what we require. 

For example,
![[Pasted image 20230705082550.png]]

### Harmonic Conjugate
Let A, B are two points then the point P and Q are called HC wrt A, B if they divide AB in the same ratio, one internally and other externally. 

That is, 
$$\frac{ AP }{ BP } = \lambda$$
$$\frac{ AQ }{ BQ } = \lambda$$

![[Pasted image 20230705083843.png]]

Now,
$$
\begin{split}
\frac{ PA }{ PB } &= \frac{ QA }{ QB } \\
\frac{ PA }{ BA - PA } &= \frac{ QA }{ QA - BA } \\
\\
\frac{ BA - PA }{ PA } &= \frac{ QA - BA }{ QA } \\
\\
\frac{ BA }{ PA } - 1 &= 1 - \frac{ BA }{ QA } \\
\frac{ BA }{ PA } + \frac{ BA }{ QA } &= 2 \\
\frac{ 1 }{ PA } + \frac{ 1 }{ QA } &= \frac{ 2 }{ BA } 
\end{split}
$$
Thus, AP, AB and AQ are in HP. Thus the name *Harmonic* Conjugate. 

Now if M is the mid point of AB, and P, Q are harmonic conjugate of each other wrt A, B,
$$
\begin{split}
\frac{ PA }{ PB } &= \frac{ QA }{ QB } \\
\\
\frac{ MP + MA }{ MB - MP } &= \frac{ MA + MQ }{ MQ - MB } \\
\\
\frac{ MP + MB }{ MB - MP } &= \frac{ MB + MQ }{ MQ - MB } \\
\\
\text{Adding in the Num. ,} \\ \text{and subt. in the denom.} \\ 
\frac{ 2MB }{ 2MP } &= \frac{ 2MQ }{ MB } \\
\\
MB^{2} &= MP. MQ \\
MA . MB &= MP. MQ
\end{split}
$$
Thus MP, MB and MQ are in GP. 

Example,
![[Pasted image 20230705084434.png]]
![[Pasted image 20230705084454.png]]