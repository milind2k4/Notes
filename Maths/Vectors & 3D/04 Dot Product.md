Links: [[05 Scalar Triple Product]]
___
# Scalar or Dot Product
$\vec{a} . \vec{b}$ is called dot product of vectors $\vec{a}$ and $\vec{b}$ and it is a scalar quantity defined as,
$$\vec{a} . \vec{b} = ab\cos \theta = a_{1}a_{2} + b_{1}b_{2}+ c_{1}c_{2}$$

where, 
$$
\begin{split}
\vec{a} &= a_{1}\hat{i} + b_{1}\hat{j} + c_{1}\hat{k} \\
\vec{b} &= a_{2}\hat{i}+ b_{2}\hat{j} + c_{2}\hat{k}
\end{split}
$$
and $\theta$ is the angle between them. 

$\vec{a} . \vec{b} = 0$, either $\vec{a} = \vec{0}\ or\ \vec{b} = \vec{0}$ or $\theta = 90$ i.e. vectors are perpendicular.

If $\cos \theta$ is present then we can think of dot product. 

Dot product can be used to find magnitude or angle between the vectors which are expressed in terms of some set of vectors whose magnitude or angle between them is know. 

### Properties of Dot product
- **Commutative:** 
  $$\vec{a}.\vec{b} = \vec{b}.\vec{a}$$
  Also, 
  $$\vec{a}.(k\vec{b}) = k(\vec{a}.\vec{b})$$

- **Distributive:** 
  $$\vec{a}.(\vec{b} + \vec{c}) = \vec{a}.\vec{b} + \vec{a}.\vec{c}$$

- **Squaring:** 
  $$\vec{a}.\vec{a} = a.a\cos 0 = a^{2} = |\vec{a}|^{2} = \vec{a}^{2}$$
  Thus we can write,
  $$|\vec{a}| = \sqrt{ \vec{a}.\vec{a} }$$


- **Equality,**
  $$\vec{a}.\vec{b} = \vec{a}.\vec{c} \centernot\implies \vec{b} = \vec{c}$$
  Instead,   
   $$\vec{a}.(\vec{b} - \vec{c}) =  0 \implies \vec{a} = \vec{0}\ or\ \vec{b} = \vec{c}\ or\ \vec{a} \perp \vec{b}-\vec{c}$$

- **Unit Vectors,**
	$$\hat{i}.\hat{i} = \hat{j}.\hat{j} = \hat{k}.\hat{k}= 1$$
	$$\hat{i}.\hat{j} = \hat{j}.\hat{k} = \hat{i}.\hat{k}= 0$$
	Using this we can write,
	$$\vec{a}.\vec{b} = \sum a_{1}b_{1} = \sqrt{ \sum a_{1}^{2} } \sqrt{ \sum b_{1}^{2} } \times \cos \theta$$

- **For fixed a, b,** (i.e. fixed magnitude)
	  - $(\vec{a}.\vec{b})_{max}= ab$. when like vectors
	  - $(\vec{a}.\vec{b})_{min}= -ab$, when unlike vectors
	  - $|\vec{a}.\vec{b}|_{max}= ab$, when collinear vectors
	  - $|\vec{a}.\vec{b}|_{min}= 0$, when perpendicular vectors

### Angle between Vectors
$$\cos \theta = \frac{ \vec{a} }{ a } \frac{ \vec{b} }{ b } = \hat{a} . \hat{b} \implies \theta = \cos ^{-1} (\hat{a}.\hat{b})$$

- If, $\vec{a}, \vec{b} \neq \vec{0}$
	- $\vec{a}.\vec{b} > 0 \implies \theta < 90^{\circ}$
	- $\vec{a}.\vec{b} = 0 \implies \theta = 90^{\circ}$
	- $\vec{a}.\vec{b} < 0 \implies \theta > 90^{\circ}$

Some examples,
![[Pasted image 20231103143223.png]]

### Some Identities
$$
\begin{split}
|\vec{a} + \vec{b}|^{2} &= a^{2} + b^{2} + 2\vec{a}.\vec{b} \\
\\
|\vec{a} - \vec{b}|^{2} &= a^{2} + b^{2} - 2\vec{a}.\vec{b} \\
\\
(\vec{a} + \vec{b})(\vec{a} - \vec{b}) &= a^{2} - b^{2} \\
\\
|\vec{a} + \vec{b} + \vec{c}|^{2} &= a^{2} + b^{2} + c^{2} + 2(\vec{a}.\vec{b} + \vec{b}.\vec{c} + \vec{c}.\vec{a})\\
\\
|\vec{a} - \vec{b}|^{2} + |\vec{b} - \vec{c}|^{2} + |\vec{c}- \vec{a}|^{2} &= 2(a^{2} + b^{2} + c^{2} - \vec{a}.\vec{b} - \vec{b}.\vec{c} - \vec{c}.\vec{a})
\end{split}
$$

And,
$$|\vec{a}+\vec{b}|^{2} + |\vec{a}-\vec{b}|^{2} = 2(a^{2} + b^{2})$$
This can be geometrically interpreted as,
$$AC^{2} + BD^{2} = AB^{2} + BC^{2} + CD^{2} + DA^{2}$$
![[Pasted image 20231103150512.png]]
I.e. for a parallelogram, the sum squares of lengths of diagonals will be equal to the sum of squares of sides.

## Projection and Components
![[Pasted image 20231103143715.png]]

Length of projection of $\vec{b}$ on $\vec{a}$ will be,
$$
\begin{split}
PR\cos \theta &= \frac{ |\vec{a}.\vec{b}| }{ a } \\
&= |\hat{a}.\vec{b}|
\end{split}
$$
i.e. to find length of projection of a vector along a direction, take dot product of vector with unit vector along the direction. 

Component of $\vec{b}$ along $\vec{a}$,
$$
\begin{split}
\vec{b}_{\parallel} &= \overline{PS} \\
&= PS \ \ \widehat{PS} \\
&= (\hat{a}.\vec{b})\hat{a} \\
&= \frac{ (\vec{a}.\vec{b})\vec{a} }{ a^{2} }
\end{split}
$$
Here we removed mod because $\theta$ can be obtuse as well.

Component of $\vec{b}$ perpendicular to $\vec{a}$,
$$
\begin{split}
\vec{b}_{\perp} &= \overline{SR} \\
&= \vec{b} - \vec{b}_{\parallel} \\
&= \vec{b} - (\hat{a}.\vec{b})\hat{a}
\end{split}
$$

![[component of one vector along another.png]]

##### Component of a vector along x, y, z axes
For any vector,
$$\vec{r} = r_{1}\hat{i} + r_{2}\hat{j} + r_{3}\hat{k}$$
We can write,
$$\vec{r} = (\vec{r}.\hat{i})\hat{i} + (\vec{r}.\hat{j})\hat{j} + (\vec{r}.\hat{k})\hat{k}$$

## Examples 

![[Pasted image 20231103151327.png]]

Projection formula and cosine rule.
![[Pasted image 20231103151733.png]]

![[Pasted image 20231103152256.png]]

![[Pasted image 20231106134455.png]]


