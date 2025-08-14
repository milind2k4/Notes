Links: [[00 Determinants]], [[01 Expansion]], [[07 Vector Triple Product]]
___
# Vector or Cross Product 
$\vec{a} \times \vec{b}$ is called the vector product of vectors $\vec{a}$ and $\vec{b}$ and is a vector quantity. 

$$|\vec{a} \times \vec{b}| = ab\sin \theta$$
And the direction is perpendicular to both $\vec{a}$ and $\vec{b}$. (i.e. perpendicular to plane formed by $\vec{a}, \vec{b}$) and it will follow right handed system. 

A vector $\perp$ to both $\vec{p}$ and $\vec{q}$ can be taken as $\lambda(\vec{p} \times \vec{q})$. 

Thus, cross product can be written as,
$$\vec{a} \times \vec{b} = (ab\sin \theta) \hat{n}$$
where $\hat{n}$ is a direction $\perp$ to the plane of $\vec{a},\vec{b}$. 

![[Cross-product.png]]

Now, if vector product is zero,
$\vec{a} \times \vec{b} = \vec{0}$, then either $\vec{a}, \vec{b} = \vec{0}$ or $\vec{a}, \vec{b}$ are collinear. 

And presence of $\sin \theta$ may imply application of vector product. 


If $\vec{a}.\vec{c} = \vec{b}.\vec{c} = 0$ then $\vec{a}, \vec{b}\perp \vec{c}$ and we can write, $\vec{c} = \lambda(\vec{a}\times \vec{b})$

#### Properties of Cross Product
- **Self Product,** 
  $$\vec{a} \times \vec{a} = 0$$ 

- **Not Commutative,** 
  $$\vec{a} \times \vec{b} = -\vec{b} \times \vec{a}$$
  
- **Constant Multiplication,**
  $$\vec{a} \times (k\vec{b}) = k(\vec{a} \times \vec{b})$$
  
- **Distributive,**
  $$\vec{a} \times (\vec{b}+\vec{c}) = \vec{a}\times \vec{b} + \vec{a}\times \vec{c}$$
  
- **Equality,**
   $$\vec{a} \times \vec{b} = \vec{a} \times \vec{c} \centernot\implies \vec{b} = \vec{c}$$
   Instead,
$$\begin{split}
\vec{a} \times (\vec{b} - \vec{c}) &=  \vec{0} \\
\vec{a} = \vec{0}\ &or\ \vec{b} = \vec{c} \\
\vec{a} \text{ is collinear} &\text{ with } \vec{b} - \vec{c}\\
\end{split}
$$

- **Not Associative,**
  $$\vec{a} \times (\vec{b} \times \vec{c}) \neq (\vec{a} \times \vec{b}) \times \vec{c}$$

- **For Unit vectors,**
	$$\hat{i} \times \hat{i} = \hat{j} \times \hat{j} =  \hat{k} \times \hat{k} = \vec{0}$$
	And,
	$$
	\begin{split}
	\hat{i} \times \hat{j} &= \hat{k} \\
	\hat{j} \times \hat{k} &= \hat{i} \\
	\hat{k} \times \hat{i} &= \hat{j} \\
	\end{split}
	$$
	
  ![[Pasted image 20231105103831.png]]  

#### To Calculate $\vec{a} \times \vec{b}$

Let,
$$\vec{a} = a_{1}\hat{i} + a_{2}\hat{j} + a_{3}\hat{k}$$
$$\vec{b} = b_{1}\hat{i} + b_{2}\hat{j} + b_{3}\hat{k}$$

Then,
$$
\vec{a} \times \vec{b} =
\begin{vmatrix}
\hat{i} & \hat{j} & \hat{k} \\
a_{1} & a_{2} & a_{3} \\
b_{1} & b_{2} & b_{3}
\end{vmatrix}
$$

#### Lagrange's identity
$$
\begin{split}
|\vec{a} \times \vec{b}|^{2} &= a^{2}b^{2}\sin ^{2}\theta \\
&= a^{2}b^{2}(1-\cos ^{2}\theta) \\
&= a^{2}b^{2} - a^{2}b^{2}\cos ^{2}\theta \\
&= (\vec{a}.\vec{a})(\vec{b}.\vec{b}) - (\vec{a}.\vec{b})^{2} 
\end{split}
$$
This can be written as,
$$
|\vec{a} \times \vec{b}|^{2} = 
\begin{vmatrix}
\vec{a}.\vec{a} & \vec{a}.\vec{b} \\
\vec{a}.\vec{b} & \vec{b}.\vec{b}
\end{vmatrix}
$$

## Area
### Area of a Triangle 
##### When Side vectors are given
![[Pasted image 20231105105906.png]]

Here,
$$\vec{a} + \vec{b} + \vec{c} = \vec{0}$$

Now,
$$
\begin{split}
\text{area} &= \frac{ 1 }{ 2 } AD.BC \\
&= \frac{ 1 }{ 2 } AB \sin \theta. BC \\
&= \frac{ 1 }{ 2 } |\overline{BA}| \times \overline{BC} \\
&= \frac{ 1 }{ 2 } |(-\vec{c}) \times \vec{a}| \\
&= \frac{ 1 }{ 2 } |\vec{c} - \vec{a}|
\end{split}
$$

By symmetry,
$$\text{area} = \frac{ 1 }{ 2 } |\vec{a} \times \vec{b}| = \frac{ 1 }{ 2 } |\vec{b} \times \vec{c}| = \frac{1}{2} |\vec{c} \times \vec{a}|$$

##### When Position vectors are given
$$
\begin{split}
\ce{ area } &= \frac{1}{2} |(\vec{c} - \vec{b}) \times (\vec{a} - \vec{b})| \\
&= \frac{1}{2} |(\vec{a} \times \vec{b}) + (\vec{b} \times \vec{c}) + (\vec{c} \times \vec{a})|
\end{split}
$$

![[Pasted image 20231105111432.png]]


### Area of a Parallelogram
If side vectors are given,

$$\ce{ area } = |\vec{a}\times \vec{b}|$$
i.e. cross of adjacent sides. 

![[Pasted image 20231105111845.png]]

Thus, we can say that geometrically, cross product represents area of parallelogram whose sides are the vectors. 

![[main-qimg-75a165db1cf8ff2c620861fbe7be361e.png]]


### Area of any Quadrilateral
If diagonal vectors $\vec{d}_{1} \text{ and } \vec{d}_{2}$ are given,
$$\ce{ area } = \frac{1}{2} |\vec{d_{1}} \times \vec{d_{2}}|$$

> Proof:
> $$
> \begin{split}
> \text{area} &= Ar(OAB) + Ar(OBC) + Ar(OCD) + Ar(OAD) \\
> &= \frac{ 1 }{ 2 } 
> (
> |\vec{b}_{1} \times \vec{a}_{2}| +
> |\vec{a}_{1} \times \vec{b}_{1}| +
> |\vec{b}_{2} \times \vec{a}_{1}| +
> |\vec{a}_{2} \times \vec{b}_{2}|
> ) \\
> &= \frac{ 1 }{ 2 } |
> \vec{b}_{1} \times \vec{a}_{2} +
> \vec{a}_{1} \times \vec{b}_{1} +
> \vec{b}_{2} \times \vec{a}_{1} +
> \vec{a}_{2} \times \vec{b}_{2}
> | \\
> &= \frac{ 1 }{ 2 }|
> (\vec{a}_{1} - \vec{a}_{2}) \times \vec{b}_{1} +
> (\vec{a}_{2} - \vec{a}_{1}) \times \vec{b}_{2}
> | \\
> &= \frac{ 1 }{ 2 } |
> (\vec{a}_{1} - \vec{a}_{2}) \times 
> (\vec{b}_{1} - \vec{b}_{2})
> | \\
> &= \frac{ 1 }{ 2 } |\vec{d}_{1} \times \vec{d}_{2}|
> \end{split}
> $$

![[Pasted image 20231105112514.png]]

Thus finally,
$$\text{area} = \frac{ 1 }{ 2 } |\text{cross of diagonals}|$$
$$\text{area} = \frac{1}{2} d_{1}d_{2} \sin \theta$$
In case of rhombus, $\theta = \pi /2$,
$$\text{area} = \frac{ 1 }{ 2 }d_{1}d_{2}$$

![[Pasted image 20231105113711.png]]

## Examples 
![[Pasted image 20231105105010.png]]

![[Pasted image 20231105105453.png]]

Sine  rule,
![[Pasted image 20231105105743.png]]

To check collinearity, we simply check whether the ratios of x, y, z components are the same or not,
![[Pasted image 20231105114021.png]]

![[Pasted image 20231105114603.png]]

![[Pasted image 20231105115041.png]]
![[Pasted image 20231105115050.png]]

![[Pasted image 20231106134811.png]]

![[Pasted image 20231106135525.png]]

![[Pasted image 20231107160444.png]]

