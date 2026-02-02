Links: [[00 Complex Numbers]]
___
# Algebra of Complex Numbers
A complex number, $z = a + ib,\ a,b \in R$, can be treated as,
1. A simple algebraic no. which follows, sum, division and multiplication rules.
2. A point in 2D plane which follows rules of distance formula, section formula etc. 
3. A vector (PV or free vector) which has magnitude $|z|$ and direction $amp(z)$ and which follows, sum, difference rules of vectors. [[01 Types and Algebra of Vectors]]


**Equality,**
$$z_{1} = z_{2} \iff Re(z_{1}) = Re(z_{2})\ \&\ Im(z_{1}) = Im(z_{2})$$

**Inequality** between two non real complex numbers is not defined just like it is not defined between two coordinate points. 


**Addition and Subtraction,**
$$
\begin{split}
z_{1} &= a + ib \\
z_{2} &= c + id \\
z_{1} + z_{2} &= (a + b) + i(c + d) \\
z_{1} + z_{2} &= (a - b) + i(c - d) \\
\end{split}
$$

##### Multiplication
$$z_{1}z_{2} = (ac - bd) + i(ad + bc)$$
i.e. we will not multiply just the real and imaginary parts. 

*Multiplication by conjugate,*
$$z . \bar{z} = (a+ib)(a-ib) = a^{2} + b^{2} = |z|^{2}$$

Thus,
$$\frac{ 1 }{ z } = \frac{ \bar{z} }{ |z|^{2} }$$

If $|z| = 1$,
$$\bar{z} = \frac{ 1 }{ z }$$
I.e. if z is unimodular, then $z$ and $\bar{z}$ will be reciprocal of each other.

*Squaring,*
$$
\begin{split}
z &= x + iy \\
z^{2} &= x^{2} - y^{2} + 2ixy \\
&= (x^{2} - y^{2}) + i(2xy) \\
\end{split}
$$
which is, in general, a complex number. 
Thus,
$$|z|^{2} \neq z^{2}$$

Due to this,
$$a^{2} + b^{2} = 0 \centernot \implies a = b = 0$$
Instead,
$$a^{2} + b^{2} = a^{2} - (ib)^{2} = (a-ib)(a+ib)$$
and thus,
$$a^{2} + b^{2} = 0 \implies a = \pm ib$$

##### Division
$$
\begin{split}
\frac{ z_{1} }{ z_{2} } &= \frac{ a + ib }{ c + id } \\
&= \frac{ (a + ib)(c - id) }{ c^{2} + d^{2} } \\
&= \frac{ ac + bd }{ c^{2} + d^{2} } + i \left( \frac{ bc - ad }{ c^{2} + d^{2} } \right)
\end{split}
$$

## Rotation 
We have a complex no,
$$z = re^{ i\theta }$$
Now, if we multiply it with another complex no, $e^{ i\alpha }$, we get,
$$z e^{ i\alpha } = e. e^{ i(\theta + \alpha) }$$
Which is the complex no. rotated by an angle $\alpha$.

![[Pasted image 20231114161238.png]]

$e^{ i\alpha }$ is called *Rotational Operator.* It will rotate the vector with which it is being multiplied by angle $\alpha$ while the magnitude will remain the same. 

Thus, we can say that multiplying by -1 will rotate it by an angle $\pi$, by $i$ will rotate it by $\pi /2$ and so on. 

![[Pasted image 20231114161625.png]]

Also,
![[Pasted image 20231114161656.png]]

##### Writing one vector in terms of another 
We use vector analogy to first convert to unit vector, then rotate it and then finally multiply it with the length to get the other vector. 

$$w = \frac{ z }{ |z| } e^{ i\theta } |w|$$
And we can write ,
$$\frac{ w }{ z } = \left| \frac{ w }{ z } \right| e^{ i\theta }$$
To decide $\theta$, we go from denom. vector to num. vector. If we have to go in anticlockwise direction, $\theta$ is +ve otherwise -ve. 

![[Pasted image 20231114162417.png]]

Now the LHS is a complex no. with argument $\theta$ and $r = |w / z|$.

$$arg\left( \frac{ FV }{ IV } \right) = \angle \text{ included}$$
which is used when  $\theta = 0, \pi\ or \pm \frac{\pi}{2}$.

##### Collinear and Perpendicular Vectors 
If z is a purely real no., $arg(z) = 0\ or\ \pi$, and $z = \bar{z}$.
Thus if two complex vectors $z_{1},z_{2}$ are collinear, 
$$arg\left( \frac{ z_{1} }{ z_{2} } \right) = 0\ or\ \pi$$
$$\frac{ z_{1} }{ z_{2} } = \frac{ \bar{z}_{1} }{ \bar{z}_{2} }$$
i.e. we can treat the ratio of complex vectors as a purely real number. 

Now, if z is purely imaginary, $arg(z) = \pm \pi /2$ and $\bar{z} = -\bar{z}$.
Thus if $z_{1},z_{2}$ are two perpendicular vectors,
$$arg\left( \frac{ z_{1} }{ z_{2} } \right) = \pm \frac{ \pi }{ 2 }$$
And thus,
$$\frac{ z_{1} }{ z_{2} } = -\frac{ \bar{z}_{1} }{ \bar{z}_{2} }$$

##### Vertices of an Equilateral Triangle
Also, if $z_{1},z_{2},z_{3}$ are vertices of an equilateral triangle, then 
$$z_{1}^{2} + z_{2}^{2} + z_{3}^{2} = z_{1}z_{2} + z_{2}z_{3} + z_{3}z_{1}$$
This also implies,
$$(z_{1} - z_{2})^{2} + (z_{2}-z_{3})^{2} + (z_{3}-z_{1})^{2} = 0$$
but this *does not imply,*
$$z_{1} = z_{2} = z_{3}$$


### Examples 
![[Pasted image 20231114173355.png]]

![[Pasted image 20231114174424.png]]

![[Pasted image 20231114175921.png]]

![[Pasted image 20231114180558.png]]

![[Pasted image 20231114181033.png]]
