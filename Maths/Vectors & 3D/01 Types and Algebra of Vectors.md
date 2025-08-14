Links: [[00 Vectors]], [[09 Straight Line]]
___
# Types and Algebra of Vectors
### Types of Vectors 
##### Unit Vector 
Whose length is one. 

If
$$|\vec{a}| = 1$$
then $\vec{a}$ is a unit vector.

It is denoted by $\hat{a}$.

If we divide any vector by its magnitude, then the resultant is a unit vector in the direction of the original vector. 
$$\hat{a} = \frac{ \vec{a} }{ |\vec{a}| }$$

##### Zero Vector
Vector with zero length and indeterminant direction. 
Denoted by $\vec{0}$. 

And $|\vec{0}| = 0$

Represented by $\cdot$ (dot). 

##### Collinear Vectors
Parallel or anti-parallel vectors. 

- **Like Vectors:** Having same Direction
- **Unlike Vectors:** Having opposite direction. 

##### Free / Fixed Vector
Fixed vectors are those which cannot be moved/translated and by doing so the physical effect is changed. E.g. force is fixed when analysing rotation. 
Also called Bound or Localised vector. 

Free vectors are those which can be translated parallel to itself. 
All vectors in maths are free, except position vector. 

![[Pasted image 20231031140729.png]]

#### Position Vector (PV)
PV of a point is a directed line segment joining origin with the point and is directed towards the point. 

The initial point is always origin. 
PV of any point is unique. 

For any point P it can be written as $\overline{OP}$, O being the origin or simply, $\vec{P}$.

## Algebra of Vectors 
1. Equality: if 2 vectors have same direction as well as magnitude and represent the same physical quantity then they are called equal vectors. 

2. $\displaystyle \frac{1}{\vec{a}}, \frac{ \vec{a} }{ \vec{b} }$ and inequality between vectors is undefined. 

3. $|\vec{a}| \geq 0$, as it represents length.


### Addition

- **Triangle Law:** Addition from tail to head. 
  
	![[Pasted image 20231031141527.png]]
	$\\$

- **Parallelogram Law:** Create a parallelogram from the 2 vectors making their initial points the same. Then the diagonal is the sum. 

	![[Pasted image 20231031141649.png]]
	$\\$

To add multiple vectors we use triangle method.
The order does not matter as addition is associative as well as commutative. 

![[Pasted image 20231031141800.png]]

If we move from point A to point B, then AB vector will represent the sum of all vectors encountered in between. 

![[Pasted image 20231031142103.png]]

To find $\vec{a} - \vec{b}$, find sum of $\vec{a}$ and $-\vec{b}$. 

![[Pasted image 20231031142435.png]]

Alternatively, to find difference, make their initial points the same and then connect their final points going from final point of 2nd vector to final point of 1st.  

The one towards which it is point is the one with + sign.
![[Pasted image 20231031142444.png]]

**Note:** If a parallelogram has two of its consecutive sides as $\vec{a}$ and $\vec{b}$ then one of its diagonals will represent sum and the other will represent difference. 
![[Pasted image 20231031142800.png]]

##### Some things to Note
If for 3 vectors $\vec{a} \pm \vec{b} \pm \vec{c} = \vec{0}$ then they will be either lie on sides of a triangle or they will be collinear.

**Triangle Inequality,**
$$||\vec{a}|- |\vec{b}|| \leq |\vec{a} + \vec{b}| \leq |\vec{a}| + |\vec{b}|$$
for latter equality to hold, $\vec{a}$ and $\vec{b}$ must be like vectors. 
for former equality to hold, $\vec{a}$ and $\vec{b}$ must be unlike vectors. 

![[Pasted image 20231031143721.png]]

### Multiplication by a scalar

The direction does not change but the magnitude changes. Multiplying by $-1$ reverses the direction. 

![[Pasted image 20231031141344.png]]

### Some points to remember
1. If we reach the same point after adding multiple vectors then the resultant is zero vector. 

1. If $\vec{a} \pm \vec{b} \pm \vec{c} = 0$ then they are either the sides of a triangle or are all collinear 

2. If $\vec{a} \ \&\ \vec{b}$ lies on sides of a parallelogram then one diagonal will be along $\vec{a}+\vec{b}$ and the other along $\vec{a}-\vec{b}$. 

3. Coplanar vector means that they lie in one plane. 2 vectors are always coplanar.  
   Collinear vectors mean along the same line. They are also coplanar. 
   
4. 2 [[09 Straight Line#Distance between SLs|lines]] in space may be coincident, parallel, intersecting or skew (when they are not parallel but cannot intersect). Skew lines are always non-coplanar.  

5. Planes can be parallel, coincident or intersecting. Planes intersect in a line. 

6. For a plane and a line, either the line intersects the plane at one point, the plane contains the line or the line is parallel to the plane but not in it. 

## Examples 
![[Pasted image 20231031144641.png]]

![[Pasted image 20231106133040.png]]

![[Pasted image 20231107155920.png]]

