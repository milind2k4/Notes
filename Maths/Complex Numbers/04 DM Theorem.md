Links: [[01 Algebra and Rotation]]
___
# De Moivre's Theorem (DMT)
$$(\cos \theta + i\sin \theta)^{n} = (e^{ i\theta })^{n}$$
If $n \in I$,
$$(e^{ i\theta })^{n} = e^{ in\theta } = \cos n\theta + i\sin n\theta$$
i.e. there will be unique answer.

If $n \notin I$ and $n = \frac{p}{q}$, where $p,q \in I$, then there will be q answers and one of them will be $\cos n\theta + i\sin n\theta$.

### Applications of DMT 
##### Solving $z^{n} = z_{o}$
where n is natural number and $z_{o}$ is given complex no. 

1. Express $z_{o}$ in exponential form. 
2. Add $2k\pi$ in argument of $z_{o}$.
3. Shift n on RHS and put $k = 0,1,2,3\dots n-1$ to get required n roots. 

All the roots are obtained by rotating the first answer by a certain angle and thus are unique. 

![[Pasted image 20231114182650.png]]
![[Pasted image 20231114183239.png]]

Let roots of $z^{n} = z_{o}$ are $z_{1},z_{2},z_{3} \dots z_{n}$ then,
1. All the roots will lie symmetrically on a circle centred at origin with radius $|z_{o}|^{1/n}$.
2. Roots form a GP with CR $e^{ i(2\pi/n) }$. 
3. Sum of the roots will be 0. 
4. Product of the roots will be $(-1)^{n+1}z_{o}$.

## nth Roots of Unity 
We will solve $z^{n} = 1$ where $n \in N$.

$$
\begin{split}
z^{n} &= e^{ i(2k\pi) } \\
z &= e^{ i (2k\pi/n) } , k = 0, 1, 2, \dots n-1
\end{split}
$$
Giving,
$$z = 1, e^{ i(2\pi/n) }, e^{ i(4\pi/n) } , e^{ i(6\pi/n) } \dots e^{ i(2(n-1)\pi/n) } $$
Now if $e^{ i(2\pi/n) } = a$, then
$$z = 1, , a^{2}, a^{3} \dots a^{n-1}$$

![[nth-root-of-unity.png]]

All roots will be symmetrically placed on circle of unit radius centred at origin. 

![[Nth roots of unity.png]]

Roots will form GP with CR = $e^{ i(2\pi/n) }$.

If we join all roots, they will be vertices of a regular polygon of n sides. 

As $a$ is a root,
$$a^{n} = (e^{ i(2\pi/n) })^{n} = e^{ i(2\pi) } = 1$$

All roots are unimodular. 
$$|a^{r}| = 1$$

Since all roots are unimodular,
$$\overline{a^{r}} = \frac{ 1 }{ a^{r} }$$

Roots will be conjugate of each other,
$$a^{n-1} = \frac{ a^{n} }{ a } = \frac{ 1 }{ a } = \bar{a}$$
$$a^{n-2} = \frac{ a^{n} }{ a^{2} } = \frac{ 1 }{ a^{2} } = \overline{a^{2}}$$

We can write,
$$a^{r} = e^{ i(2r\pi)/n } = \cos\left( \frac{ 2r\pi }{ n } \right) + i \sin\left( \frac{ 2r\pi }{ n } \right)$$

Now, as sum of roots is 0 and product is 1,
$$
\begin{split}
Re\left( \sum a \right) &= 0 \\
1 + \cos \frac{2\pi}{n} + \cos \frac{4\pi}{n} + \dots + \cos \frac{2(n-1)\pi}{n} &= 0 \\
Im\left( \sum a \right) &= 0 \\
\sin \frac{2\pi}{n} + \sin \frac{4\pi}{n} + \dots + \sin \frac{2(n-1)\pi}{n} &= 0 
\end{split}
$$

Factorising $z^{n}- 1$ we get,
$$z^{n}-1 = (z-1)(z-a)(z-a^{2})(z-a^{3})\dots(z-a^{n-1})$$

Opening LHS using $x^{n} - y^{n}$, [[02 Formula and Expansions#Factorization of Difference]],

$$(z-1)(1 + z + z^{2} + \dots z^{n-1}) = (z-1)(z-a)(z-a^{2})\dots(z-a^{n-1})$$
Cancelling $z-1$,
$$1 + z + z^{2} + \dots z^{n-1} = (z-a)(z-a^{2})\dots (z-a^{n-1})$$
In short we can write,
$$\sum_{r=0}^{n-1} z^{r} = \prod_{r=1}^{n-1}(z-a^{r})$$
$$\sum_{r=0}^{n-1} z^{r} = \prod_{r=1}^{n-1}(z- e^{ i(2r\pi/n) })$$

Now if we put z = 1,
$$
\begin{split}
n &= \prod_{r=1}^{n-1} (1 - e^{ i(2\pi r/n) }) \\
| n | &= \prod_{r=1}^{n-1} | (1 - e^{ i(2\pi r/n) }) | \\
n &= \prod_{r=1}^{n-1} 2 \left( \sin \frac{ \pi r }{ n } \right) \\
n &= 2^{n-1} \prod_{r=1}^{n-1} \left( \sin \frac{ \pi r }{ n } \right) \\
\end{split}
$$

Thus we get,
$$\sin \frac{\pi}{n} . \sin \frac{2\pi}{n}. \sin \frac{3\pi}{n}. \dots . \sin \frac{ (n-1)\pi }{ n } = \frac{ n }{ 2^{n-1} }$$

### Cube Roots of Unity 
#important 

$$
\begin{split}
z^{3} &= 1 \\
&= e^{i(0)} \\
&= e^{ i(2k\pi) } \\
z &= e^{ i(2k\pi/3) }
\end{split}
$$

Giving,
$$z = 1, e^{ i(2\pi/3) }, e^{ i(4\pi/3) }$$
$$z = 1, e^{ i(2\pi/3) }, e^{ -i(2\pi/3) }$$

Usually it is denoted as,
$$e^{ i(2\pi/3) } = \omega$$
Hence if we multiply an complex no. with $\omega$ then it is rotated by 120$^{\circ}$ in anticlockwise direction.

Thus,
$$z = 1, \omega, \omega^{2}$$
And,
$$\omega = - \frac{ 1 }{ 2 } + \frac{ i\sqrt{ 3 } }{ 2 }$$
$$\omega^{2} = \bar{\omega} = - \frac{ 1 }{ 2 } - \frac{ i\sqrt{ 3 } }{ 2 }$$

Cube roots of $1 = 1, \omega, \omega^{2}$
Cube roots of $-1 = -1, -\omega, -\omega^{2}$

Plotting them on unit circle we get an equilateral triangle. 

![[Cube roots of unity.png]]

From here,
$$|\omega| = |\omega^{2}| = 1$$
Thus,
$$\bar{\omega} = \frac{ 1 }{ \omega } = \omega^{2}$$
$$\overline{\omega^{2}} = \frac{ 1 }{ \omega^{2} } = \omega$$

$$\omega^{3n} = 1, \omega^{3n+1} = \omega, \omega^{3n+2} = \omega^{2}$$

Sum of the roots is zero,
$$1 + \omega + \omega^{2} = 0$$

Sum of any 3 consecutive powers of $\omega$ will be zero.
$$\omega^{r} + \omega^{r+1} + \omega^{r+2} = 0$$

Also, as $(\omega^{2})^{2} = \omega$,
$$
\begin{split}
\sqrt{ \omega } &= \pm \omega^{2} \\
\sqrt{ \omega^{2} } &= \pm \omega
\end{split}
$$

#### Raise and Add

If a square root of a number $a$ is $b$ then the other will be $-b$. 
If a cube root of a number $a$ is $b$ then other cube roots will be $b\omega$ and $b\omega^{2}$. 

Similarly, if a biquadratic root of a number $a$ is $b$ then other 3 roots will be $-b, ib, -ib$.

If we raise each root to some power and add then,
$$1^{p} + \omega^{p} + (\omega^{2})^{p} = 3$$
if $p = 3k$ i.e. p is a multiple of 3.
$$1^{p} + \omega^{p} + (\omega^{2})^{p} = 0$$
if $p = 3k+1\ or\ 3k+2$ i.e. p is a not multiple of 3.

This works for nth roots of unity as well.

If nth roots of units are $1, a, a^{2}, a^{3} \dots a^{n-1}$, then,
$$1^{p} + (a)^{p} + (a^{2})^{p} + \dots (a^{n-1})^{p} = n$$
if p is a multiple of n.
$$1^{p} + (a)^{p} + (a^{2})^{p} + \dots (a^{n-1})^{p} = 0$$
if p is not a multiple of n.


#### Cubic Formulae 
We have, (first)
$$z^{3} - 1 = (z-1)(z-\omega)(z-\omega^{2})$$
Putting $z = a /b$ in the first and taking LCM we will get,
$$a^{3} - b^{3} = (a - b)(a - \omega b)(a - \omega^{2}b)$$

Putting $b = -b$,
$$a^{3} + b^{3} = (a - b)(a + \omega b)(a + \omega^{2}b)$$

Now factorising LHS in first,
$$(z-1)(z^{2} + z + 1) = (z-1)(z-\omega)(z-\omega^{2})$$
Thus,
$$z^{2} + z + 1 = (z-\omega)(z-\omega^{2})$$

Putting $z = a /b$ and taking LCM we will get,
$$
\begin{split}
a^{2} + ab + b^{2} &= (a - \omega b)(a - \omega^{2}b) \\
&=  (b - \omega a)(b - \omega^{2}a)
\end{split}
$$

And,
$$a^{2} + b^{2} + c^{2} - ab - bc - ca = (a + b\omega + c\omega^{2})(a + b\omega^{2} + c\omega)$$

Using this sum of cubes can be factorised,
$$
\begin{split}
a^{3} + b^{3} + c^{3} - 3abc &= (a + b + c) (a^{2} + b^{2} + c^{2} - ab - bc - ca) \\
&= (a + b + c)(a + b\omega + c\omega^{2})(a + b\omega^{2} + c\omega)
\end{split}
$$

## Examples 
![[Pasted image 20231115102808.png]]

![[Pasted image 20231115103039.png]]

![[Pasted image 20231115111935.png]]

![[Pasted image 20231115112319.png]]

![[Pasted image 20231117115413.png]]
(this is question 5)

![[Pasted image 20231117120304.png]]

![[Pasted image 20231117121131.png]]

$\\$
![[Pasted image 20231117122710.png]]
![[Pasted image 20231117122725.png]]
![[Pasted image 20231117122742.png]]