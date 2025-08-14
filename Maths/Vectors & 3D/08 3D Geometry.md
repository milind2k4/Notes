Links: [[00 Vectors]], [[09 Straight Line]], [[11 Plane]]
___
# 3 Dimensional Geometry

#### Conversion between Vector and 3D

| Vector          | 3D               |
| --------------- | ---------------- |
| Position Vector | Coordinates      |
| Free Vector     | Direction Ratio  |
| Unit Vector     | Direction Cosine |
| $\vec{r}$        | $(x,y,z)$         |


### Formulas
If coordinates of the points A, B, C are given as, $(x_{i}, y_{i}, z_{i})$, then
1. **Distance Formula:**
   $$d = \sqrt{ (x_{1} - x_{2})^{2} + (y_{1} - y_{2})^{2} + (z_{1} - z_{2})^{2} }$$

2. **[[01 Section Formula|Section Formula:]]**
	Coordinates of a point which divides AB internally in a ratio $\lambda:\mu$,
	$$P: \left( \frac{ \lambda x_{2} + \mu x_{1} }{ \lambda + \mu }, \frac{ \lambda y_{2} + \mu y_{1} }{ \lambda + \mu }, \frac{ \lambda y_{2} + \mu y_{1} }{ \lambda + \mu }, \right)$$
	
	For external division, put either of $\lambda$ or $\mu$ as -ve.
	
	Mid point,
	$$M: \left( \frac{ x_{1}+x_{2} }{ 2 }, \frac{ y_{1}+y_{2} }{ 2 }, \frac{ z_{1}+z_{2} }{ 2 } \right)$$

3. **Area of triangle ABC:**
	$$A = \frac{ 1 }{ 2 } |(x_{2} - x_{1}, y_{2} - y_{1}, z_{2} - z_{1}) \times (x_{3} - x_{1}, y_{3} - y_{1}, z_{3} - z_{1})|$$
	I.e. simply take cross of the sides of triangle.
	
	For example,
	![[Pasted image 20231107163023.png]]

##### In Triangle ABC
[[05 Notations and Results in a Triangle]]

- **Centroid:** 
	$$G: \left( \frac{ \sum x_{1} }{ 3 }, \frac{ \sum y_{1} }{ 3 }, \frac{ \sum z_{1} }{ 3 } \right)$$

- **Orthocentre:** 
  $$H: \left( \frac{ \sum x_{1}\tan A }{ \sum \tan A }, \frac{ \sum y_{1}\tan A }{ \sum \tan A }, \frac{ \sum z_{1}\tan A }{ \sum \tan A } \right) $$

- **Circumcentre:**
$$K:\left( \frac{ \sum x_{1}\sin(2A) }{ \sum \sin(2A) }, \frac{ \sum y_{1}\sin(2A) }{ \sum \sin(2A) }, \frac{ \sum z_{1}\sin(2A) }{ \sum \sin(2A) } \right)$$

- **Incentre:**
$$I:\left( \frac{ \sum ax_{1} }{ \sum a }, \frac{ \sum ay_{1} }{ \sum a }, \frac{ \sum az_{1} }{ \sum a } \right)$$

### Direction Ratio and Cosine
If, $A: (x_{1},y_{1},z_{1})$ and $B:(x_{2},y_{2},z_{2})$ then a **direction ratio** parallel to the line connecting A and B is
$$d.r. = (x_{2}-x_{1}, y_{2}-y_{1}, z_{2}-z_{1})$$

This direction ratio can be used to form a vector AB,
$$\overline{AB}= (x_{2}-x_{1})\hat{i} + (y_{2}-y_{1})\hat{j}  + (z_{2}-z_{1})\hat{k}$$

And **direction cosine** can be given as,
$$\left( \frac{ x_{2} - x_{1} }{ \sum (x_{2} - x_{1})^{2} }, \frac{ y_{2} - y_{1} }{ \sum (x_{2} - x_{1})^{2} }, \frac{ z_{2} - z_{1} }{ \sum (x_{2} - x_{1})^{2} } \right)$$
Which is nothing but the unit vector for $\overline{AB}$.

![[Pasted image 20231109145809.png]]
![[Pasted image 20231109145817.png]]

![[Pasted image 20231109150346.png]]
![[Pasted image 20231109150354.png]]

##### Two Lines
If dr for two lines are $l_{1}:(a_{1},b_{1},c_{2})$ and $l_{2}:(a_{2},b_{2},c_{2})$, then,
- If $l_{1} \parallel l_{2}$ then $\displaystyle \frac{ a_{1} }{ a_{2} } = \frac{ b_{1} }{ b_{2} } = \frac{ c_{1} }{ c_{2} }$
- If $l_{1} \perp l_{2}$ then $a_{1}a_{2} + b_{1}b_{2}+ c_{1}c_{2}= 0$, i.e. the dot product is zero. 
- For Angle between the lines, simply use [[04 Dot Product#Angle between Vectors|dot product.]]
$$\theta = \cos ^{-1} \left| \frac{ \sum a_{1}a_{2} }{ \sqrt{ \sum a_{1}^{2} } \sqrt{ \sum a_{2}^{2} } } \right| = \cos ^{-1}\left| \frac{ \vec{dr}_{1} . \vec{dr}_{2} }{ | \vec{dr}_{1} | | \vec{dr}_{2} | } \right| $$

![[Pasted image 20231107164351.png]]
![[Pasted image 20231107164402.png]]

### Condition for Collinearity of 3 Points 
Three points $A:\vec{a}$, $B:\vec{b}$, $C:\vec{c}$ will be collinear if and only if there exists $\lambda_{1},\lambda_{2}, \lambda_{3} (\in R)$ nor all zero simultaneously such that,
$$\lambda_{1} \vec{a} + \lambda_{2}\vec{b} + \lambda_{3}\vec{c} = \vec{0}$$
and 
$$\lambda_{1} + \lambda_{2} + \lambda_{3} = 0$$

![[Pasted image 20231110103850.png]]

Proof:
> If A, B, C are collinear,
> $$
> \begin{split}
> \overline{AB} &= \lambda \overline{AC} \\
> \vec{b} - \vec{a} &= \lambda(\vec{c} - \vec{a}) \\
> (\lambda - 1) \vec{a} + \vec{b} - \lambda \vec{c} &= 0 \\
> \end{split}
> $$
> here we can see that the sum of coefficients is zero.


For converse,
> If 
> $$\lambda_{1} \vec{a} + \lambda_{2}\vec{b} + \lambda_{3}\vec{c} = \vec{0}$$
> and 
> $$\lambda_{1} + \lambda_{2} + \lambda_{3} = 0$$
> Now dividing by $\lambda_{1}$,
> $$
> \begin{split}
> \vec{a} &= \frac{ -(\lambda_{2} \vec{b} + \lambda_{3} \vec{c}) }{ \lambda_{1} } \\
> \vec{a} &= \frac{ \lambda_{2} \vec{b} + \lambda_{3} \vec{c} }{ \lambda_{2} + \lambda_{3} } 
> \end{split}
> $$
> Now this is a point which divides line BC in the ratio $\lambda_{3}:\lambda_{2}$.
Thus A, B, C are collinear. 

![[Pasted image 20231110104632.png]]

### Coplanarity of 4 Points 
$A:\vec{a}$, $B:\vec{b}$, $C:\vec{c}$ and $D:\vec{d}$ will be coplanar points iff there exists $\lambda_{1}, \lambda_{2}, \lambda_{3},\lambda_{4} (\in R)$ not all zero simultaneously such that,
$$\lambda_{1} \vec{a} + \lambda_{2}\vec{b} + \lambda_{3}\vec{c} + \lambda_{4} \vec{d} = \vec{0}$$
and 
$$\lambda_{1} + \lambda_{2} + \lambda_{3} + \lambda_{4} = 0$$

![[Pasted image 20231110104930.png]]

Proof: 
> If A, B, C, D are coplanar, then, $\overline{AB}, \overline{AC}, \overline{AD}$ are coplanar vectors.
> Thus we can write,
> $$
> \begin{split}
> \overline{AB} &= \overline{AC} + \mu \overline{AD} \\
> (\lambda + \mu - 1)\vec{a} + \vec{b} - \lambda c - \mu \vec{d} &= 0
> \end{split}
> $$
> here we can see that the sum of coefficients is zero.

For converse,
> If
> $$\lambda_{1} \vec{a} + \lambda_{2}\vec{b} + \lambda_{3}\vec{c} + \lambda_{4} \vec{d} = \vec{0}$$
> and 
> $$\lambda_{1} + \lambda_{2} + \lambda_{3} + \lambda_{4} = 0$$
> 
> $$
> \begin{split}
> \lambda_{1} \vec{a} + \lambda_{2} \vec{b} &= -(\lambda_{3} \vec{c} + \lambda_{4} \vec{d}) \\
> \frac{ \lambda_{1} \vec{a} + \lambda_{2} \vec{b} }{ \lambda_{1} + \lambda_{2} } &= \frac{ \lambda_{3} \vec{c} + \lambda_{4} \vec{d} }{ \lambda_{3} + \lambda_{4} } = \vec{P}\\
> \end{split}
> $$
> This means that P divides AB in ratio $\lambda_{2}:\lambda_{1}$ and CD in ratio $\lambda_{4}: \lambda_{3}$. This means that P lies on both lines. 
> Thus both lines are intersecting and thus coplanar. I.e. A, B, C, D are coplanar points.

![[Pasted image 20231110105642.png]]




