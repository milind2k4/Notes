Links: [[00 Vectors]], [[04 Dot Product]], [[10 Equation of Line]], [[11 Plane]]
___
# Straight Lines
### Point of intersection of two lines 
$$L_{1} \equiv \frac{ x - x_{1} }{ a_{1} } = \frac{ y - y_{1} }{ b_{1} } = \frac{ z - z_{1} }{ c_{1} } = \lambda_{1}$$
$$L_{2} \equiv \frac{ x - x_{2} }{ a_{2} } = \frac{ y - y_{2} }{ b_{2} } = \frac{ z - z_{2} }{ c_{2} } = \lambda_{2}$$

Let point of intersection is C, then it will lie on both lines. 

Equating coordinates,
$$
\begin{split}
x_{1} + a_{1}\lambda_{1} &= x_{2} + a_{2}\lambda_{2} \\
y_{1} + b_{1}\lambda_{1} &= y_{2} + b_{2}\lambda_{2} \\
z_{1} + c_{1}\lambda_{1} &= z_{2} + c_{2}\lambda_{2} 
\end{split}
$$
We will solve $\lambda_{1}, \lambda_{2}$ from any two equations and then verify with the third. 

![[Pasted image 20231109162512.png]]

#### Coincident, Parallel, Intersecting and Skew Lines
-  $$\frac{a_{1}}{a_{2}} = \frac{ b_{1} }{ b_{2} } = \frac{ c_{1} }{ c_{2} }\ \&\ \frac{ x_{2} - x_{1} }{ a_{1} } = \frac{ y_{2} - y_{1} }{ b_{1} } = \frac{ z_{2} - z_{1} }{ c_{1} }$$
	i.e. $\vec{b} \parallel \vec{d}$ and fixed points satisfy both the lines, 
	then the lines are coincident. 
	$\\$
	
- $$\frac{a_{1}}{a_{2}} = \frac{ b_{1} }{ b_{2} } = \frac{ c_{1} }{ c_{2} }\ \&\ \frac{ x_{2} - x_{1} }{ a_{1} } \neq \frac{ y_{2} - y_{1} }{ b_{1} } \neq \frac{ z_{2} - z_{1} }{ c_{1} }$$
i.e. $\vec{b} \parallel \vec{d}$ and fixed point of one lines does not satisfy the other line, 
then the lines are distinct parallel. 
$\\$

- $$\frac{ a_{1} }{ a_{2} } = \frac{ b_{1} }{ b_{2} } = \frac{ c_{1} }{ c_{2} }$$
does not hold, and we can find unique values of $\lambda_{1}, \lambda_{2}$, then the lines are intersecting. 

- $$\frac{ a_{1} }{ a_{2} } = \frac{ b_{1} }{ b_{2} } = \frac{ c_{1} }{ c_{2} }$$
does not hold, and we cannot find unique values of $\lambda_{1}, \lambda_{2}$, then the lines are skew. 

**In terms of vectors,**

If $\vec{b} \parallel \vec{d}$ then,
- $(\vec{c}-\vec{a})\parallel \vec{b} \implies$ coincident lines
- $(\vec{c}-\vec{a}) \centernot\parallel \vec{b} \implies$ distinct parallel lines

If $\vec{b} \nparallel \vec{d}$ then, they are either intersecting or skew. To find out find the point of intersection of them.

#### Examples 
![[Pasted image 20231109164012.png]]
![[Pasted image 20231109164021.png]]

### Distance between Straight Lines 
Let the two lines be,
$$L_{1} \equiv \vec{r} = \vec{a} + \lambda \vec{b}$$
$$L_{2} \equiv \vec{r} = \vec{c} + \mu \vec{d}$$

#### Parallel Lines
If the lines are parallel, then
$$\vec{b} \times \vec{d} = \vec{0}$$

Distance between parallel lines,
$$
\begin{split}
l &= AC\sin \theta \\
&= \frac{ |(\vec{a} - \vec{c}) \times \vec{b}| }{ |\vec{b}| } \\
&= \frac{ |(\vec{a} - \vec{c}) \times \vec{d}| }{ |\vec{d}| } \\
\end{split}
$$
as $\vec{b}$ and $\vec{d}$ are collinear. 

![[Pasted image 20231110090856.png]]

Also,
![[Pasted image 20231110090916.png]]

#### Skew Lines
The minimum distance between two curves occurs along common normal. 

If $N_{1}N_{2}$ is the line corresponding to minimum distance between $L_{1}$ and $L_{2}$, then $N_{1}N_{2} \perp L_{1}\ \&\ N_{1}N_{2} \perp L_{2}$. 
I.e. $N_{1}N_{2}$ will be along $\vec{b} \times \vec{d}$. 

The least distance between lines $L_{1}$ and $L_{2}$ will be projection of $\overline{AC}$ on $N_{1}N_{2}$ line. 

$$l = \left| \frac{ (\vec{a} - \vec{c}) . (\vec{b} \times \vec{d}) }{ |\vec{b} \times \vec{d}| } \right| = \frac{ |[\vec{a}-\vec{c} \ \ \ \vec{b} \ \ \ \vec{d}]| }{ |\vec{b} \times \vec{d}| }$$

**Altarnatively,**
Let PV of 
$$N_{1} = \vec{a} + \lambda_{1}\vec{b}$$
$$N_{2} = \vec{c} + \lambda_{2}\vec{d}$$
Now,
$$\overline{N_{1}N_{2}} = \vec{c} - \vec{a} + \lambda_{2} \vec{d} - \lambda_{1} \vec{b}$$

And, 
$$N_{1}N_{2} \perp L_{1} \implies \overline{N_{1}N_{2}}.\vec{b} = 0$$
$$N_{1}N_{2} \perp L_{2} \implies \overline{N_{1}N_{2}}.\vec{d} = 0$$

This will give two equations and two unknowns and hence we can solve and find $N_{1}, N_{2}$ for least distance. 

![[Pasted image 20231110092427.png]]

For example,
![[Pasted image 20231110093137.png]]

### 2 Lines and a Plane
Let 2 lines and a plane be,
$$L_{1} \equiv \vec{r} = \vec{a} + \lambda \vec{b} = \frac{ x - x_{1} }{ a_{1} } = \frac{ y - y_{1} }{ b_{1} } = \frac{ z - z_{1} }{ c_{1} }$$
$$L_{2} \equiv \vec{r} = \vec{c} + \lambda \vec{d} = \frac{ x - x_{2} }{ a_{2} } = \frac{ y - y_{2} }{ b_{2} } = \frac{ z - z_{2} }{ c_{2} }$$
$$P \equiv ax + by + cz + d$$

###### Angle Between Lines
Then angle between the lines,
$$\theta = \cos ^{-1} |\hat{b}.\hat{d}|$$
$$\theta = \cos ^{-1}\left| \frac{ \sum a_{1}a_{2} }{ \sqrt{ \sum a_{1}^{2} } \sqrt{ \sum a_{2}^{2} } } \right| $$

###### Angle Between Plane and Line
The angle between the plane and a line is the least possible angle, as L will make different angles with different directions in the plane P. 
L will make least angle with direction L' which is projection of L on P.

Also, $\vec{n}$, $L$ and $L'$ will be coplanar.
![[Pasted image 20231109160308.png]]

Thus finally, angle between plane and line will be,
$$\theta = 90^{\circ} - \cos ^{-1}|\hat{n}.\hat{b}|$$
$$\theta = 90^{\circ} - \cos ^{-1}\left| \frac{ \sum aa_{1} }{ \sqrt{ \sum a_{1}^{2} } \sqrt{ \sum a^{2} } } \right|$$ 

### Reflection of Point in Line

If there is a line and we take the reflection of a point $P$ in that line, then the vector joining the image $P'$ and point is perpendicular to the line and the mid point of $PP'$  lies on the line. 

i.e., if $P:(x_{1},y_{1},z_{1})$ be the point and $P':(x_{1}',y_{1}',z_{1}')$ be the image,

$$\overline{PP'} \perp \vec{b} \implies \overline{PP'} . \vec{b} = 0$$
$$\left( \frac{ x_{1} + x_{1}' }{ 2 }, \frac{ y_{1} + y_{1}' }{ 2 },\frac{ z_{1} + z_{1}' }{ 2 }  \right) \text{ will statisfy the line}$$

### Intersection of Plane and Line

To find the point of intersection of a line and plane:
1. Find a point on line in terms of $\lambda$.
4. Put this point into the equation of the plane.
5. Find $\lambda$.
6. Find the point.

This will give,
$$\lambda (aa_{1} + bb_{1} + cc_{1}) = - (ax_{1} + by_{1} + cz_{1} + d)$$

Now,
- if $\sum a a_{1} = 0$ and $ax_{1} + by_{1} + cz_{1} + d \neq 0$, then $L \parallel P$ and line does not lie in the plane.
- if $\sum a a_{1} = 0$ and $ax_{1} + by_{1} + cz_{1} + d = 0$, then $L \parallel P$ and line lies in the plane, i.e. every point on line is point of intersection of L and P. 
- if $\sum a a_{1} \neq 0$ there will be unique point on intersection. 

### Equidistant Locus of 3 Points 
If 3 points, A, B and C are given which are non collinear, then locus point P which is equidistant from all three points A, B, C will be a straight line $\perp$ to the plane ABC and will pass through the circumcentre of $\Delta$ABC. 

The direction of line will be along $\vec{a} \times \vec{b} + \vec{b} \times \vec{c} + \vec{c} \times \vec{a}$.

![[Pasted image 20231110095026.png]]

This line will also be the line of intersection the perpendicular bisector plane of AB and perpendicular bisector plane of AC. 

For example,
![[Pasted image 20231110095420.png]]

