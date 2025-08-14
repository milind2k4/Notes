Links: [[00 Vectors]], [[02 Section Formula and Triangle]]
___
# Vector Geometry
### Tetrahedron
Pyramid with base as triangle. 
It has 4 vertices, faces and 6 edges.
Since all the faces are triangles, we can say any one as a base.  

ABCD is a tetrahedron and PVs of vertices are $\vec{a}, \vec{b},\vec{c},\vec{d}$,

##### Centroid of Tetrahedron 
The PV of centroid of face BCD ($\ce{ G_{1} }$) is given as,
$$\vec{G}_{1} = \frac{ \vec{b} + \vec{c} + \vec{d} }{ 3 }$$
Now let K is a point on $AG_{1}$ dividing it in the ratio, $\lambda:1$, then PV of K is,
$$\vec{K} = \frac{ \lambda \vec{G}_{1} + \vec{A} }{ \lambda + 1 } = \frac{ \vec{a} + \lambda /3(\vec{b} + \vec{c} + \vec{d}) }{ \lambda + 1 }$$

If $\lambda = 3$, then,
$$\vec{K} = \frac{ \vec{a} + \vec{b} + \vec{c} + \vec{d} }{ 4 }$$

As it is symmetric in a,b,c,d, the same point can be obtained on line segments $BG_{2},CG_{3},DG_{3}$. 

Since same point K is obtained on 4 different lines, these lines must but concurrent at K. 

Hence lines joining vertex with opposite faces will be concurrent at a point K called the **centroid of the tetrahedron.**

Also, the centroid divides these lines in the ratio 3:1. 

![[Pasted image 20231103111536.png]]

##### Line Joining Mid point of Opposite Edges
AB and CD are called *pair of opposite edges* (3 such pairs) as they do not have any vertex in common. 

Line joining the mid points of pair of opposite edges (line $M_{1}M_{2}$) will pass through centroid (K) and will be bisected by it. 

![[Pasted image 20231103112204.png]]

##### Centroid of Small Tetrahedron
Centroid of tetrahedron formed by centroids of all triangles,
$$\frac{ \sum \vec{G}_{1} }{ 4 } = \frac{ \vec{a} + \vec{b} + \vec{c} + \vec{d} }{ 4 } = \vec{K}$$
Thus, the centroid of both the big tetrahedron and the small tetrahedrons are the same.

![[Pasted image 20231103113141.png]]

### Parallelepiped
Prism with base as parallelogram. In prism, slant faces are parallelograms. 

Since all faces of parallelepiped are parallelogram, any face can be called base.

It has 8 vertices, 12 edges and face diagonals, 6 faces and 4 body diagonals (main or simple diagonals).

![[Pasted image 20231103114046.png]]

Now, let O be at $A_{1}$, and parallelepiped has 3 co initial edges as $\vec{a}, \vec{b}, \vec{c}$. Then PV of different vertices are,
$$A_{1}: \vec{O},\ \ B_{1}: \vec{a},\ \ C_{1}: \vec{a} + \vec{b} \dots$$
and so on.

![[Pasted image 20231103114600.png]]

##### Centroid of parallelepiped 
We have,
$$\overline{A_{1}C_{2}} = \vec{a} + \vec{b} + \vec{c}$$
Whose mid point is,
$$M_{A_{1}C_{2}} = \frac{ \vec{a} + \vec{b} + \vec{c} }{ 2 }$$

Which is the same for all other body diagonals. 

Thus, the 4 body diagonals meet at one point and this point divides the diagonal into 2 equal parts. This is the centroid of the parallelepiped. 

For parallelepiped which as one vertex as origin,
$$\text{centroid}, \vec{K} = \frac{ \vec{a} + \vec{b} + \vec{c} }{ 2 }$$

![[Pasted image 20231103115331.png]]

Now, by symmetry and observation,
$$C_{1}K = \frac{ -\vec{a} - \vec{b} + \vec{c} }{ 2 }$$
$$A_{2}K = \frac{ \vec{a} + \vec{b} - \vec{c} }{ 2 }$$
and so on.

Also, if origin is not at one of the vertices, then centroid,
$$\overline{OK} = \overline{OA_{1}} + \frac{ \vec{a} + \vec{b} + \vec{c} }{ 2 }$$


##### Opposite Edges and Mid Points
$A_{1}B_{1}$ and $C_{2}D_{2}$ are called pair of opposite edges.

Line joining mid points of pair of opposite edges passes through centroid and is bisected by it.

I.e.
$$\text{mid point of } M_{1}M_{2} = \vec{K}$$


If point of intersection of face diagonals of face $A_{1}B_{1}C_{1}D_{1}$ is $X_{1}$ and that of $A_{2}B_{2}C_{2}D_{2}$ is $X_{2}$, then the mis point of $X_{1}X_{2}$ is also K.

![[Pasted image 20231103120243.png]]


### Sphere 
[[00  Circle]]

It is locus of a point (P) which is at a constant distance (= r) from a fixed point (C).

![[Pasted image 20231110194540.png]]

Equation of sphere with centre at $a,b,c$ and radius $r$ can be given as,
$$PC^{2} = r^{2}$$
$$(x - a)^{2} + (y - b)^{2} + (z - c)^{2} = r^{2}$$

Simplifying it,
$$x^{2} + y^{2} + z^{2} - 2ax - 2by - 2cz + a^{2} + b^{2} + c^{2} - r^{2} = 0$$
Thus **the general equation** comes out to be,
$$x^{2} + y^{2} + z^{2} + 2gx + 2fy + 2hz + c = 0$$
which has centre $(-g,-f,-h)$ and radius,
$$r = \sqrt{ g^{2} + f^{2} + h^{2} - c }$$

##### Equation in Vector Form 
$$
\begin{split}
PC &= d \\
|\vec{r} - \vec{c}| &= d \\
r^{2} + c^{2} - 2\vec{r}.\vec{c} &= d^{2} \\
r^{2} - 2 \vec{c}.\vec{r} + c^{2} - d^{2} &= 0 \\
r^{2} + 2\vec{a}.\vec{r} + \vec{b} &= 0
\end{split}
$$

Here centre is $-\vec{a}$ 
and radius is 
$$d = \sqrt{ |a|^{2} - b }$$

![[Pasted image 20231110210813.png]]

##### Sphere and Plane 

If a plane P intersects a sphere S in a circle K, then, 
- centre of K will be the foot of perpendicular from centre of S to P. 
- radius of K = $r_{1} = \sqrt{ r^{2} - p^{2} }$.
  where r is radius of sphere and p is length of perpendicular from centre of sphere to plane P.

![[Pasted image 20231110201349.png]]

If sphere S and plane P intersect in a circle K, then equation of sphere containing K can be given as,
$$S + \lambda P = 0$$

![[Pasted image 20231110202138.png]]

This is because all points on the circle will satisfy both the sphere and the plane. 

##### Tangential Plane 
If point $A:(x_{1},y_{1},z_{1})$ lies on sphere,
$$S \equiv x^{2} + y^{2} + z^{2} + 2gx + 2fy + 2hz + c = 0$$
Then equation of plane touching S at A is given as,
$$T = 0$$
$$x x_{1} + yy_{1} + zz_{1} + g(x + x_{1}) + f(y + y_{1}) + h(z + z_{1}) + c = 0$$

![[Pasted image 20231110201915.png]]

### Example
![[Pasted image 20231110210522.png]]
![[Pasted image 20231110210533.png]]