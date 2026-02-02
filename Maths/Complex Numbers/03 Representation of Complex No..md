Links: [[00 Complex Numbers]]
___
# Representation of Complex No. 
#### Cartesian or Algebraic Form 
[[05 Complex no in a Plane]]

$$z = x + iy,\ x,y \in R$$
This is just like a point $(x,y)$ in 2D. 

It can be used in finding locus or solving equations. 

![[Pasted image 20231113202639.png]]

#### Polar or Trig. Form
$$z = r\cos \theta + i r\sin \theta$$
$$z = r(\cos \theta + i \sin \theta)$$
Here r gives idea of distance (i.e. magnitude) and $\cos \theta + i\sin \theta$ gives idea of direction (i.e. argument). 

This is written in short as,
$$z = r. cis (\theta)$$

If $\theta$ is amplitude, then $z = r. cis(\theta)$ is called *true polar form.* 

![[Pasted image 20231113202729.png]]

Conversion examples,
![[Pasted image 20231113203332.png]]


If $\theta \in R$,
$$|\cos \theta + i \sin \theta| = 1$$
$$cis(-\theta) = \frac{ 1 }{ cis(\theta) } = \overline{cis(\theta)}$$

If $\theta_{1}, \theta_{2} \in R$, then,
- **Multiplication,**
	$$cis(\theta_{1}) . cis(\theta_{2}) = cis(\theta_{1} + \theta_{2})$$
	
	As,
	$$(\cos \theta_{1} + i\sin \theta_{1})(\cos \theta_{2} + i \sin \theta_{2}) = \cos(\theta_{1} + \theta_{2}) + i (\sin \theta_{1} + \theta_{2})$$

- **Division,**
	$$\frac{ cis(\theta_{1}) }{ cis(\theta_{2}) } = cis(\theta_{1} - \theta_{2})$$

which are the same properties as of exponents. 

#### Exponential Form 
[[02 Formula and Expansions#Expansions]]

$$e^{ x } = 1 + x + \frac{ x^{2} }{ 2! } + \frac{ x^{3} }{ 3! } + \dots$$
Now putting $x = ix$,
$$
\begin{split}
e^{ ix } &= 1 + ix - \frac{ x^{2} }{ 2! } - \frac{ ix^{3} }{ 3! } + \dots \\
&= \left( 1 - \frac{ x^{2} }{ 2! } + \frac{ x^{4} }{ 4! } + \dots \right) + i\left( x - \frac{ x^{3} }{ 3! } + \frac{ x^{5} }{ 5! } - \dots \right) \\
&= \cos x + i \sin x 
\end{split}
$$

Thus,
$$e^{ix} = \cos x + i \sin x$$
This is called **Euler's Formula.**

$$
\begin{split}
z &= x + iy,\ x,y \in R \\
&= r(cis(\theta)) \\
&= r e^{ i\theta }
\end{split}
$$
Thus $e^{ i\theta }$ can be treated as a unit vector. 

Using this, we have,
$$
\begin{split}
1 &= e^{ i(0) } \\
-1 &= e^{ i\pi } \\
i &= e^{ i\pi/2 } \\
-i &= e^{ -i\pi/2 }
\end{split}
$$


And, if $\theta \in R$,
$$|e^{ i\theta }| = 1$$
Conjugate,
 $$
\begin{split}
\overline{ e^{ i\theta } } &= \cos \theta - i \sin \theta \\
&= \cos(-\theta) + i \sin(-\theta) \\
&= e^{ -i\theta } \\
&= \frac{ 1 }{ e^{ i\theta } }
\end{split}
$$

And we can write,
$$
\begin{split}
\cos \theta &= \frac{ e^{ i\theta } + e^{ -i\theta } }{ 2 } \\
\sin \theta &= \frac{ e^{ i\theta } - e^{ -i\theta } }{ 2i }
\end{split}
$$

##### Adding 1
$$
\begin{split}
1 + e^{ i\theta } &= e^{ i\theta/2 } (e^{ i\theta/2 } + e^{ -i\theta/2 }) \\
&= 2\cos \frac{\theta}{2} . e^{ i\theta/2 }
\end{split}
$$
Taking modulus,
$$|1 + e^{ i\theta }| = 2\left| \cos \frac{\theta}{2} \right|$$

##### Subtracting from 1
$$
\begin{split}
1 - e^{ i\theta } &= 1 + e^{ i(\pi + \theta) } \\
&= 2 \cos\left( \frac{ \pi + \theta }{ 2 } \right). e^{ i\left( \large \frac{ \pi + \theta }{ 2 } \right) } \\
&= - 2 \sin (\theta /2). e^{ i(\pi/2 + \theta/2) } \\
&= 2 \sin \frac{ \theta }{ 2 } e^{ i(\pi + \pi/2 + \theta/2) } \\
&= 2 \sin \frac{ \theta }{ 2 } e^{ i(3\pi/2 + \theta/2) } \\
&= 2 \sin \frac{ \theta }{ 2 } e^{ i(\theta/2 - \pi/2) } 
\end{split}
$$

Taking modulus,
$$|1 - e^{ i\theta }| =  2 \left| \sin \frac{ \theta }{ 2 } \right|$$

### Complex no. as a point in 2D plane 

If complex no. associated with 3 points A, B, C are $z_{1},z_{2},z_{3}$ then,

Distance AB,
$$AB = |z_{1} - z_{2}|$$

Complex no. for point P which divides AB in the ratio $\lambda:\mu$,
$$z_{P} = \frac{ \lambda z_{2} + \mu z_{1} }{ \lambda + \mu }$$

Mid point of AB,
$$z_{M} = \frac{ z_{1} + z_{2} }{ 2 }$$

For triangle ABC, complex no. associated with 
- *Centroid,*
	$$z_{G} = \frac{ z_{1} + z_{2} + z_{3} }{ 3 }$$
- *Orthocentre,*
	$$z_{H} = \frac{ \sum z_{1}\tan A }{ \sum \tan A }$$
- *Circumcentre,*
	$$z_{K} = \frac{ \sum z_{1} \sin2A }{ \sum \sin 2A }$$
- *Incentre,*
  $$z_{I} = \frac{ \sum az_{1} }{ \sum a }$$

If the points are collinear with B in between A and C,
$$
\begin{split}
AB + BC &= AC \\
|z_{1} - z_{3}| + |z_{2} - z_{3}| &= |z_{1} - z_{3}| 
\end{split}
$$

![[Pasted image 20231113214026.png]]

### Complex no. as a Vector
$z_{2} - z_{1}$ is a vector joining the points corresponding to $z_{1},z_{2}$ and directed towards $z_{2}$ (the first one).

Thus $|z_{2} - z_{1}|$ is the distance between A and B.

For argument of $z_{2} - z_{1}$, put the vector at origin and then find the angle with +ve real axis. 

![[Pasted image 20231113214233.png]]

![[Pasted image 20231114174740.png]]

