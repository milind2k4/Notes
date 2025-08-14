Links: [[01 Expansion]], [[04 Dot Product]], [[06 Cross Product]], 
___
# Scalar Triple Product (STP)

$$(\vec{a} \times \vec{b}) . \vec{c} = \begin{bmatrix}
\vec{a} & \vec{b} & \vec{c}
\end{bmatrix} = \begin{vmatrix}
a_{1} & a_{2} & a_{3}  \\
b_{1} & b_{2} & b_{3} \\
c_{1} & c_{2} & c_{3} 
\end{vmatrix}$$

$$\begin{split}
(\vec{a} \times \vec{b}) . \vec{c} &=  (ab\sin \theta \hat{n}) . \vec{c} \\
&= (ab\sin \theta)(\hat{n}.\vec{c}) \\
&= ab\sin \theta . (c \cos \phi ) \\
&= abc \sin \theta \cos \phi
\end{split}
$$
where $\phi$ is angle between $\vec{a}\times \vec{b}$ & $\vec{c}$ and$\theta$ is the angle between $\vec{a}$ & $\vec{b}$


- $\begin{bmatrix} \vec{a} & \vec{b} & \vec{c} \end{bmatrix} = 0 \implies$ 
	  - either $a=0$ or $b=0$ or $c=0$. 
	  - or 2 of the 3 vectors are collinear
	  - or vectors are coplanar

- If $\vec{a},\vec{b},\vec{c}$ are coplanar then $\begin{bmatrix} \vec{a} & \vec{b} & \vec{c} \end{bmatrix} = 0$

- $\begin{bmatrix} \vec{a} & \vec{b} & \vec{c} \end{bmatrix} = \begin{bmatrix} \vec{b} & \vec{c} & \vec{a} \end{bmatrix} = \begin{bmatrix} \vec{c} & \vec{a} & \vec{b} \end{bmatrix}$

- $\begin{bmatrix} \vec{a} & \vec{b} & \vec{c} \end{bmatrix} = -\begin{bmatrix} \vec{a} & \vec{b} & \vec{c} \end{bmatrix}$

	![[Pasted image 20221231205857.png]]


- $\begin{bmatrix} \vec{a} & \vec{b} & \vec{0} \end{bmatrix} = 0$
  
- $\begin{bmatrix} \vec{a} & k\vec{a} & \vec{b} \end{bmatrix} = 0$
  
- $\begin{bmatrix} \vec{a} & k\vec{b} & \lambda\vec{a} + \mu \vec{b}\end{bmatrix} = 0$
  
- $\begin{bmatrix} \vec{a} + \vec{b} & \vec{c} & \vec{d}\end{bmatrix} = \begin{bmatrix} \vec{a} & \vec{c} & \vec{d} \end{bmatrix} + \begin{bmatrix} \vec{b} & \vec{c} & \vec{d} \end{bmatrix}$
  
- $\begin{bmatrix} \vec{ka} & \vec{b} & \vec{c} \end{bmatrix} = k\begin{bmatrix} \vec{a} & \vec{b} & \vec{c} \end{bmatrix}$
  
- $\begin{bmatrix} \vec{a} - \vec{b} & \vec{b} - \vec{c} & \vec{c} - \vec{a} \end{bmatrix} = 0$
  
- $\begin{bmatrix} \vec{a} + \vec{b} & \vec{b} + \vec{c} & \vec{c} + \vec{a} \end{bmatrix} = 2\begin{bmatrix} \vec{a} & \vec{b} & \vec{c} \end{bmatrix}$

- If a fixed length of $\vec{a},\vec{b},\vec{c}$,
	  - $\begin{bmatrix} \vec{a} & \vec{b} & \vec{c} \end{bmatrix}_{max} = abc$, the three are mutually perpendicular and follow a right handed system.
	  - $\begin{bmatrix} \vec{a} & \vec{b} & \vec{c} \end{bmatrix}_{min}= -abc$, the three are mutually perpendicular  and follow a left handed system. 
	  - $\left| \begin{bmatrix} \vec{a} & \vec{b} & \vec{c} \end{bmatrix} \right|_{max} = abc$, the three are mutually perpendicular.
	  - $\left| \begin{bmatrix} \vec{a} & \vec{b} & \vec{c} \end{bmatrix} \right|_{min}= 0$, when the three are coplanar.


For a general result,
$$
\begin{split}

\begin{bmatrix}
k_{1}\vec{a} + k_{2}\vec{b} + k_{3}\vec{c} & 
k_{4}\vec{a} + k_{5}\vec{b} + k_{6}\vec{c} & 
k_{7}\vec{a} + k_{8}\vec{b} + k_{9}\vec{b} &
\end{bmatrix} \\
=  
\begin{vmatrix}
k_{1} &  k_{2} & k_{3} \\
k_{4} & k_{5} & k_{6} \\
k_{7} & k_{8} & k_{9}
\end{vmatrix}
\begin{bmatrix} \vec{a} & \vec{b} & \vec{c} \end{bmatrix}
\end{split}
$$


STP squared,
$$
\begin{split}
\begin{bmatrix}
\vec{a} & \vec{b} & \vec{c} 
\end{bmatrix}^{2}
&= \begin{bmatrix} \vec{a} \times \vec{b} & \vec{b} \times \vec{c} & \vec{c} \times \vec{a} \end{bmatrix} \\
&= \begin{vmatrix}
\vec{a}.\vec{a} & \vec{b}.\vec{a} & \vec{c}.\vec{a} \\
\vec{a}.\vec{b} & \vec{b}.\vec{b} & \vec{c}.\vec{b} \\
\vec{a}.\vec{c} & \vec{b}.\vec{c} & \vec{c}.\vec{c}
\end{vmatrix} 
\end{split}
$$

## Volume

### Tetrahedron
![[Pasted image 20221231212320.png]]
($\vec{a},\vec{b},\vec{c}$ are coinitial or coterminus (same initial point))

$$\ce{ volume } = \frac{1}{6} \left| \begin{bmatrix} \vec{a} & \vec{b} & \vec{c} \end{bmatrix} \right|$$


### Parallelepiped
![[Pasted image 20221231212539.png]]

$$\ce{volume} = \left| \begin{bmatrix} \vec{a} & \vec{b} & \vec{c} \end{bmatrix} \right| $$

## Examples 
![[Pasted image 20231106140737.png]]

![[Pasted image 20231106140949.png]]