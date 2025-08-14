Links: [[00 Conic Sections]]
___
# Ellipse 
In ellipse, there are two pairs of focus and directrix. 

### [[02.1 Std. Equation. terms and Other Ellipses]]

### Auxiliary Circle and Parametric Point
Auxiliary circle is the circle drawn taking the major axis as diameter. This will have equation,
$$x^{2} + y^{2} = a^{2}$$

Here, P and Q are called **Corresponding Points.**

Parametric point on ellipse can be taken as,
$$Q:(a\cos \theta, b\sin \theta)$$
This is also called point $\theta$. 
Here $\theta$ is called **Eccentric Angle.** 
One thing to note is that this angle is not the angle made by joining O and Q. 

The ratio of distance between corresponding points and perpendicular from ellipse,
$$\frac{ PQ }{ QN } = \frac{ a\sin \theta - b\sin \theta }{ b\cos \theta } = \frac{ a- b }{ b }$$
Thus we can say that ellipse is the locus of a point which divides the perpendicular from circle onto a fixed diameter in a fixed ratio. 

![[Pasted image 20230919165815.png]]

### Focal Distance

$$
\begin{split}
\frac{ PS_{1} }{ PL_{1} } &= e \\
PS_{1} &= ePL_{1} \\
&= e\left( \frac{ a }{ e } - x_{P} \right) \\
&= a - ex_{P} \\
\text{Similarly,} \\
PS_{2} &= ePL_{2} \\
&= e\left( \frac{ a }{ e } + x_{P} \right) \\
&= a + ex_{P} \\
\end{split}
$$
Thus focal distances of a point P on the ellipse,
$$fd = a \pm ex_{P}$$

![[Pasted image 20230919170625.png]]

For point $\theta$ (i.e. $(a\cos \theta, b\sin \theta)$, 
$$fd = a(1 \pm e\cos \theta)$$

For any point on ellipse, the sum of focal distances,
$$PS_{1} + PS_{2} = 2a$$
which is a constant and the length of major axis. 

Ellipse can be treated as locus of a point for which sum of distances from two fixed points is constant (2a). 

![[Pasted image 20230919171142.png]]

If P is a variable point and A, B are two fixes points such that PA + PB = k, then locus of P will be,
1. *Ellipse,* if k > AB. In this case k = 2a, and A, B will be foci.
2. *Line Segment AB,* if k = AB. 
3. *Not obtainable (i.e. not possible),* if k < AB


### Equation of Chord 
![[Pasted image 20230919173613.png]]

Two points are $\theta_{1},\theta_{2}$. 

$$AB = \frac{ x }{ a }\cos \left( \frac{ \theta_{1} + \theta_{2} }{ 2 } \right) + \frac{ y }{ b } \sin \left( \frac{ \theta_{1} + \theta_{2} }{ 2 } \right) = \cos \left( \frac{ \theta_{1} - \theta_{2} }{ 2 } \right)$$

Now, if this line passes through $(\alpha,0)$,
$$\frac{ \alpha }{ a } \cos \left( \frac{ \theta_{1} + \theta_{2} }{ 2 } \right) = \cos \left( \frac{ \theta_{1} - \theta_{2} }{ 2 } \right)$$

Using C and D,
$$\frac{ \alpha - a }{ \alpha + a } = 
\frac{ 
\cos\left( \frac{ \theta_{1} - \theta_{2} }{ 2 } \right)
- \cos \left( \frac{ \theta_{1} + \theta_{2} }{ 2 } \right) }
{ \cos\left( \frac{ \theta_{1} 
- \theta_{2} }{ 2 } \right) + \cos \left( \frac{ \theta_{1} + \theta_{2} }{ 2 } \right)
 }$$

$$\tan \frac{ \theta_{1} }{ 2 } \tan \frac{ \theta_{2} }{ 2 } = \frac{ \alpha - a }{ \alpha + a }$$
I.e. the product of tan of half of the eccentric angle is constant. 

For $S_{1}, \alpha = ae$,
$$\tan \frac{ \theta_{1} }{ 2 } \tan \frac{ \theta_{2} }{ 2 } = \frac{ e - 1 }{ e + 1 }$$

For $S_{2}, \alpha = -ae$,
$$\tan \frac{ \theta_{1} }{ 2 } \tan \frac{ \theta_{2} }{ 2 } = \frac{ e + 1 }{ e - 1 }$$


### Location of a Point 
Like [[02 Location of a Point wrt Circle|circle]]. 

![[Pasted image 20230919173640.png]]

## [[02.5 Examples (Ellipse)]]