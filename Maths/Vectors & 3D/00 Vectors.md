Links: [[01 Types and Algebra of Vectors]]
___
# Vectors
A vector is a quantity as well as direction. 
It is represented by a directed line segment. 

Length is the magnitude.

### Angle between Vectors
It is the angle b/w their lines of action after making their initial or final point the same. It is always the smaller angle. If $\theta$ is the angle then $\theta \in [0,\pi]$.

It is denoted by
$$\widehat{(\vec{a},\vec{b})}$$

### Octants

x,y,z axes divide space in 8 parts. 
$$(x,y,z)$$

4 of them are,
$$(+,+,+)$$
$$(-,+,+)$$
$$(-,-,+)$$
$$(+,-,+)$$

The rest 4 are the same with $-ve$ z-axis.

### Components of a Vector

$$\vec{ P } = a \hat{i} + b\hat{j} + c\hat{k}$$

And $a\hat{i},\ b\hat{j},\ c\hat{k}$ are components (or projection) of P along $x,y,z$ axis respectively. 

![[Pasted image 20231031211156.png]]

If we take any 2 vectors of the three, we get the projection of P along the plane containing those unit vectors. For example, $a\hat{i} + b\hat{j}$ is the projection of P along the x-y plane. 


Magnitude of P is,
$$|\vec{P}| = \sqrt{ a^{2} + b^{2} + c^{2} }$$

Unit vector in the direction of P is,
$$\hat{P} = \frac{ a \hat{i} + b \hat{j} + c \hat{k} }{ \sqrt{ a^{2} + b^{2} + c^{2} } }$$

### Direction angles and Direction Cosines 
For point P or $\overline{OP}$ angles made by OP with +ve directions of x, y and z axes are called **direction angles** and the cosine of which are called **direction cosines (d.c.)** and usually they are denoted by l, m and n. 

![[Pasted image 20231031211834.png]]

$$
\begin{split}
l &= \cos \alpha = \frac{ a }{ \sqrt{ a^{2} + b^{2} + c^{2} } } \\
m &= \cos \beta = \frac{ b }{ \sqrt{ a^{2} + b^{2} + c^{2} } } \\
n &= \cos \upgamma = \frac{ c }{ \sqrt{ a^{2} + b^{2} + c^{2} } }
\end{split}
$$
Thus we can write,
$$\hat{P} = \cos \alpha \hat{i} + \cos \beta \hat{j} + \cos\upgamma \hat{k}$$
$$\hat{P} = l \hat{i} + m \hat{j} + n \hat{k}$$

Thus direction cosines are the components of the unit vector along the direction. 

And, since the vector is unit vector,
$$\cos ^{2}\alpha + \cos ^{2} \beta + \cos ^{2}\upgamma = 1$$
$$l^{2} + m^{2} + n^{2} = 1$$

Converting to sine,
$$\sum \sin ^{2} \alpha = 2$$

Examples,
![[Pasted image 20231031213245.png]]
![[Pasted image 20231031213256.png]]

### Linear Combination of Vectors 
If $\vec{a}$ is given, then any vector $\vec{b}$ collinear with $\vec{a}$ can uniquely be written as,
$$\vec{b} = \lambda \vec{a}$$

If a vector is non collinear with $\vec{a}$ then it cannot be expressed in terms of $\vec{a}$ alone. 

If $\vec{a}$ and $\vec{b}$ are non collinear then,
1. They will lie in a unique plane wrt orientation.
2. If $\lambda \vec{a} + \mu \vec{b} = \vec{0}$, then $\lambda = \mu = 0$. 
2. If $\lambda \vec{a} + \mu \vec{b} = \lambda_{1} \vec{a} + \mu_{1} \vec{b}$, then $\lambda = \lambda_{1}\ \&\ \mu = \mu_{1}$. (similarly for 3 non coplanar vectors)


Any vector $\vec{r}$ in the plane of $\vec{a}$ and $\vec{b}$ can be written uniquely as a linear combination of $\vec{a}$ and $\vec{b}$.
$$\vec{r} = \lambda \vec{a} + \mu \vec{b}$$

If $\vec{a}, \vec{b}, \vec{c}$ are three non coplanar vectors then,
1. If $\lambda\vec{a} + \mu \vec{b} + \eta \vec{c} = \vec{0}$ then $\lambda = \mu = \eta = 0$

If $\vec{r}$ is any vector in space, then it can be written uniquely as a linear combination of non coplanar $\vec{a},\vec{b},\vec{c}$, i.e.,
$$\vec{r} = \lambda \vec{a} + \mu \vec{b} + \eta \vec{c}$$
$$\vec{r} = \lambda \vec{a} + \mu \vec{b} + \eta (\vec{a} \times b)$$
$$\vec{r} = \lambda (\vec{a} \times \vec{b}) + \mu (\vec{b} \times \vec{c}) + \eta (\vec{c} \times a)$$

For Example,
![[Pasted image 20231110105830.png]]
![[Pasted image 20231110110014.png]]

## Solving Vector Equations 
If only scalar equations are given, then assume the unknown vector in terms of known vectors. 

To get rid of cross product we can use [[07 Vector Triple Product]].

If both sides have one same vectors, we will club all of them together. 
$$
\begin{split}
\vec{a} \times \vec{b} &= \vec{c} \times \vec{a} \\
\vec{a} \times (\vec{b} + \vec{c}) &= \vec{0} \\
\vec{b} + \vec{c} &= \lambda \vec{a}
\end{split}
$$

#### Examples 
![[Pasted image 20231110203228.png]]

![[Pasted image 20231110203637.png]]
(here it will be $k^{2} + A^{2}$ instead of $1 + k^{2}$)

![[Pasted image 20231110203942.png]]

![[Pasted image 20231110204420.png]]
![[Pasted image 20231110204431.png]]

![[Pasted image 20231110204806.png]]
![[Pasted image 20231110204816.png]]


