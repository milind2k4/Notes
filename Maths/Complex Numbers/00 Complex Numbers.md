Links: [[00 Quadratic Equations and Expressions]]
___
# Complex Numbers
$\sqrt{ -1 } = i$ is an imaginary quantity. 

So,
$$
\begin{split}
i^{2} &= -1 \\
i^{3} &= -i \\
i^{4} &= 1 
\end{split}
$$
and so on. 

Thus, if n is an integer.
$$
\begin{split}
i^{4n} &= 1 \\
i^{4n+1} &= i \\
i^{4n+2} &= -1 \\
i^{4n+3} &= -i 
\end{split}
$$
Adding all 4 we get zero. 

Thus, for $m \in I$,
$$i^{m} + i^{m+1} + i^{m+2} + i^{m+3} = 0$$

A number of type $a + ib$ where $a,b \in R$ is called complex number (say z).
$$z = a + ib$$
The real part of $z$ is $a$ and imaginary part is $b$ (coefficient of $i$) and we write,
$$z = Re(z) + iIm(z)$$

If there is some unknown variable in the expression, we cannot directly say anything about imaginary or real part of z. 

#### Complex Plane
A complex number can be denoted on a 2D plane by a point and this plane is called **Complex or Argand plane.**

We can say that real numbers are 1D and complex are 2D. We require two axes, one real and one imaginary to represent a complex number. 

The complex plane can be treated as a simple coordinate 2D plane. 

![[Arg and Mod of Complex no.png]]

Set of complex no. is represented by $\mathbb{C}$. 

Numbers lying on real axis are called real numbers and the numbers not on it are called non real or imaginary numbers.

A number on the complex plane is called complex number. 

Real no. are also called *purely real* and they lie on the horizontal axis. So, numbers lying on vertical axis are called *purely imaginary.*

Origin, i.e. $0 + i 0$ is a complex, real, purely real, purely imaginary but not an imaginary number. 

##  [[01 Algebra and Rotation]]

### [[02 Argument, Conjugate and Mod]]

### Locus of Variable point
Equality denotes a curve and inequality represents a region for which the curve is dividing boundary.

If $Re(z)$ is written then visualise it as x and if $Im(z)$ as y. 

- If a variable point $P:z$ satisfies,
	$$|z - z_{1}| = r$$
	where $z_{1}$ is a given point and r is constant.
	
	Then we can say that the locus of P will be a circle centred at the given point and having radius r.
	$\\$

- If $A:z_{1}$ and $B:z_{2}$ are given points and $P:z$ is a variable point such that,
	$$|z - z_{1}| = |z - z_{2}|$$
	then, locus of P is the perpendicular bisector of AB.
	$\\$

- If $A:z_{1}$ is fixed point and $P:z$ is a variable point such that,
	$$arg(z - z_{1}) = \theta$$
	then locus of P will be a ray originating from A at angle $\theta$.
	
	![[Pasted image 20231113215438.png]]

In most cases we will give answer in trig. form. 

For example,
![[Pasted image 20231113221246.png]]

## Square root of Complex No.
Let $a,b \in R$ then to find square roots of $a + ib$ let,
$$
\begin{split}
z &= x + iy \\
&= \sqrt{ a + ib } \\
x^{2} - y^{2} + i 2xy &= a + ib \\
\text{Equating real and im. part}, \\
x^{2} - y^{2} &= a \\
2xy &= b
\end{split}
$$
Also, taking mod both sides,
$$
\begin{split}
x + iy &= \sqrt{ a + ib } \\
\sqrt{ x^{2} + y^{2} } &= \sqrt{ \sqrt{ a^{2} + b^{2} } } \\
x^{2} + y^{2}  &= \sqrt{ a^{2} + b^{2} }
\end{split}
$$

This gives, 
$$x = \pm \sqrt{ \frac{ a + \sqrt{ a^{2} + b^{2} } }{ 2 } }$$
$$y = \pm \frac{ b }{ |b| } \sqrt{ \frac{ \sqrt{ a^{2} + b^{2} } - a }{ 2 } }$$

![[Pasted image 20231117091402.png]]

Thus finally giving,
$$\sqrt{ z } = \pm\left( \sqrt{ \frac{ |z| + Re(z) }{ 2 } } + i (sgn(Im(z))) \sqrt{ \frac{ |z| - Re(z) }{ 2 } } \right)$$


## Misc. Examples 
![[Pasted image 20231113221819.png]]

![[Pasted image 20231113222406.png]]

![[Pasted image 20231113222551.png]]

![[Pasted image 20231114155815.png]]

![[Pasted image 20231114160507.png]]

$\\$
![[Pasted image 20231117124441.png]]
![[Pasted image 20231117124448.png]]
![[Pasted image 20231117124459.png]]
