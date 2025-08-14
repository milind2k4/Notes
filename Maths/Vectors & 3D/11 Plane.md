Links: [[00 Vectors]], [[09 Straight Line]], [[12 Equation of Plane]], [[04 Dot Product]]
___
# Plane

In 3d, plane is an extrusion of a straight line in 2d. Hence all formula of 2d can be extended to 3d. 

#### Length of perpendicular from Point to Plane
Length of perpendicular from $(x_{1},y_{1},z_{1})$ to Plane
$$l= \frac{ |ax_{1} + by_{1} + cz_{1} + d| }{ \sqrt{ a^{2} + b^{2} + c^{2} } }$$


#### Reflection of Point in Plane

If foot of perpendicular from A to P is N and the reflection of A in P is B then,
$$N \equiv \frac{ x-x_{1} }{ a } = \frac{ y-y_{1} }{ b } = \frac{ z-z_{1} }{ c } = \frac{ -P(x_{1},y_{1},z_{1}) }{ a^{2} + b^{2} + c^{2} }$$
$$B \equiv \frac{ x-x_{1} }{ a } = \frac{ y-y_{1} }{ b } = \frac{ z-z_{1} }{ c } = \frac{ -2P(x_{1},y_{1},z_{1}) }{ a^{2} + b^{2} + c^{2} }$$

#### Family of Planes
Family of Planes passing through the intersection of 2 planes:
$$P_{3} \equiv P_{1} + \lambda P_{2} = 0$$


#### Angle between Planes
Angle between planes is the angle between their normals. 

$$\theta = \cos ^{-1} \left| \frac{\displaystyle \sum_{a_{1}a_{2}}^{c_{1}c_{2}} a_{1}a_{2} }{ \sqrt{ \displaystyle \sum_{a_{1}}^{c_{1}} a_{1}^{2} } \sqrt{ \displaystyle \sum_{a_{2}}^{c_{2}} a_{2}^{2} } } \right| $$

Line of Intersection of $P_{1}$ and $P_{2}$ will be along $\vec{n_{1}} \times \vec{n_{2}}$.

#### Distance between 2 Planes
Distance between planes,
$$d = \frac{ |d_{1}-d_{2}| }{ \sqrt{\displaystyle  \sum_{a}^{c} a^{2} } }$$


### Coincident & Distinct Parallel Planes

Let 2 planes be:
$$P_{1} \equiv a_{1}x + b_{1}y + c_{1}z + d_{1} = 0$$
$$P_{2} \equiv a_{2}x + b_{2}y + c_{2}z + d_{2} = 0$$

If, 
$$\frac{ a_{1} }{ a_{2} } = \frac{ b_{1} }{ b_{2} } = \frac{ c_{1} }{ c_{2} } = \frac{ d_{1} }{ d_{2} }$$
then $P_{1} \equiv P_{2}$ i.e. both are *coincident* planes.

If, 
$$\frac{ a_{1} }{ a_{2} } = \frac{ b_{1} }{ b_{2} } = \frac{ c_{1} }{ c_{2} } \neq \frac{ d_{1} }{ d_{2} }$$
then $P_{1}\ \&\ P_{2}$  are *distinct parallel* planes.

### Angular Bisector Plane
Angular bisecting plane of 2 intersecting Planes:
$$\frac{ P_{1} }{ \sqrt{ \displaystyle \sum_{a}^{c} a_{1}^{2} } } = \pm \frac{ P_{2} }{ \sqrt{ \displaystyle \sum_{a}^{c} a_{2}^{2} } }$$

Take same sign as that of $a_{1}a_{2}+ b_{1}b_{2} + c_{1}c_{2}$ for the obtuse angular bisector. 

If the planes are in vector form,
$$P_{1} \equiv \vec{r}.\vec{n}_{1} = q_{1}$$
$$P_{2} \equiv \vec{r}.\vec{n}_{2} = q_{2}$$
Angular bisecting plane is given by,
$$\left| \frac{ P_{1} }{ \vec{n}_{1} } \right| = \left| \frac{ P_{1} }{ \vec{n}_{2} } \right|$$

### Plane Containing a Line 
If line L is given as 
$$L \equiv \frac{ x - x_{1} }{ a } = \frac{ y - y_{1} }{ b } = \frac{ z - z_{2} }{ c }$$
We can separate two planes from this equation.
$$P_{1} \equiv \frac{ x - x_{1} }{ a } = \frac{ y - y_{1} }{ b }$$
$$P_{2} \equiv \frac{ y - y_{1} }{ b } = \frac{ z - z_{2} }{ c }$$
Now L is nothing but line of intersection of these planes. 

Any plane which contains L will pass through line of intersection of $P_{1},P_{2}$ hence its equation can be given as,
$$P \equiv P_{1} + \lambda P_{2} = 0$$

### Equidistant Plane of 2 points
Locus of all points which are equidistant from 2 points will lie on a plane which will be perpendicular to AB and will pass through AB's mid-point. It is given as,
$$\left(  \vec{r} - \left( \frac{ \vec{a} + \vec{b} }{ 2 } \right) \right). (\vec{a} - \vec{b}) = 0$$
