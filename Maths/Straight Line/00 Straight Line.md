Links: [[02 Equation of a Line]]
___
# Straight Line

##### Quadrants
$$
\begin{split}
\ce{ 
I&: x, y > 0 \\
II&: x < 0, y > 0 \\
III&: x, y < 0 \\
IV&: x > 0, y < 0 \\
 }
\end{split}
$$

#### Some things to Note
Any point on the x axis can be taken as $(a,0)$ i.e. its y coordinate will be zero. 

Any point on the y axis can be taken as $(0,a)$ i.e. its x coordinate will be zero. 

If $A: (a, 0)$ and $B:(b,0)$ are two points on the x axis, then the distance between them will be,
$$AB = |a - b|$$

The reflection of a point $A:(a,b)$ in,
$$
\begin{split}
x&: A_{x}(a,-b) \\
y&: A_{y}(-a, b) \\
O&: A_{o}(-a,-b)
\end{split}
$$
(O is origin)

![[Pasted image 20230705080525.png]]

### Definitions
#### Slope
If a straight line L makes an angle $\theta$ with the +ve direction of the x axis, then $\tan \theta$ is called slope of line L and is represented as $m$.

The slope of a vertical line is undefined. 

Slope of line passing through points $A:(x_{1},y_{1})$ and $B:(x_{2},y_{2})$ and be given as,
$$\tan \theta = m = \frac{ y_{1} - y_{2} }{ x_{1} - x_{2} } = \frac{ \Delta y }{ \Delta x }$$

![[Pasted image 20230706085505.png]]

#### Intercept
If line L intersect x-axis at point M and y axis at point N then x coordinate of N is called x intercept and y coordinate of M is called y intercept.

![[Pasted image 20230706085517.png]]

If a line has equal intercepts then its slope is -1. 

![[Pasted image 20230706085713.png]]

If line has equal lengths of intercepts, then slope is -1 or 1. 

![[Pasted image 20230706085822.png]]

### Distance Formula
If $A:(x_{1},y_{1})$ and $B: (x_{2},y_{2})$ are two points then,
$$AB = \sqrt{ (x_{1}-x_{2})^{2} + (y_{1}-y_{2})^{2} }$$
That is,
$$AB = \sqrt{ \Delta x^{2} + \Delta y^{2} }$$

![[Pasted image 20230705081530.png]]

### [[01 Section Formula]]


## Area of Polygon
[[06 Coordinates of Centres and Area of Triangle]]

Let $A_{1},A_{2},A_{3}\dots$ are n vertices (in order) of a polygon of n sides such that,
$$A_{i}:(x_{i}, y_{i})$$

Then the area of the polygon is given as,
$$\text{Area} = |\Delta|$$
where,
$$\Delta = \frac{1}{2}[(x_{1}y_{2} - y_{1}x_{2}) + (x_{2}y_{3} - y_{2}x_{3}) + \dots (x_{n-1}y_{n} - y_{n-1}x_{n}) + (x_{n}y_{1} - y_{n}x_{1})]$$

![[Pasted image 20230706083026.png]]

We have to go in order because otherwise connecting the points in different orders gives different polygons and thus different areas,
![[Pasted image 20230706083232.png]]


## Concurrency of 3 Lines
[[05 Solving Linear Equations#3 Linear Equations in 2 Variables]]

Let 3 lines be,
$$L_{i} = a_{i}x + b_{i}x + c_{i} = 0,\ i = 1,2,3$$

If $L_{1}, L_{2}, L_{3}$ are concurrent at a point, then,
$$\Delta = \begin{vmatrix}
a_{1} & b_{1} & c_{1} \\
a_{2} & b_{2} & c_{2} \\
a_{3} & b_{3} & c_{3}
\end{vmatrix} = 0$$

However, vice-versa is not true. I.e. if lines are concurrent then $\Delta = 0$, but if $\Delta = 0$ the lines may or may not be concurrent. They may be parallel also. 


To check we can find the intersection of first two lines (if equations are given) and then check if that point lies on the third line or not. Or we can check whether no two pairs are parallel and then solve the determinant. 

Example,
![[Pasted image 20230708093101.png]]
![[Pasted image 20230708093158.png]]

##### Parallelism and  Perpendicularity of Lines
[[05 Solving Linear Equations#2 Linear Equations in 2 variables]]


## Homogenisation of a 2 Degree Curve 
Let the conic curve be,
$$C \equiv ax^{2} + by^{2} + 2hxy + 2gx + 2fy + c = 0$$
And a line be,
$$L \equiv mx + d$$

Now their POIs are A and B, then we have to find the joint equation of POSL OA and OB which are formed by joining origin to A and B. 

This will homogenise equation of C with the help of L.

![[Pasted image 20230713094238.png]]

We write equation of line as,
$$\frac{ y - mx }{ d } = 1$$

Now we write the equation of curve as,
$$ax^{2} + by^{2} + 2hxy + (2gx + 2fy) . 1 + c. 1^{2} = 0$$
Substituting the value of 1,
$$ax^{2} + by^{2} + 2hxy + (2gx + 2fy) . \left( \frac{ y - mx }{ d } \right) + c. \left( \frac{ y - mx }{ d } \right)^{2} = 0$$
Now this is a homogeneous equation and thus  the lines it represents pass through origin.

Now if POI a has coordinates, $A:(a,b)$ then $L(A) = 1$ and $C(A) = 0$. Putting a and b into the equation above, we see that it indeed is zero. Similarly with B.

Thus this is the joint equation of OA and OB, where A and B are POIs of line and conic curve. 

If there is something like "angle at origin" we can think of homogenisation.

Example,
![[Pasted image 20230714071036.png]]

## Shift of Origin 
( #removed from jee 24)

If origin is shifted to $(a,b)$ and let a point P has coordinates $(x_{o}, y_{o})$ wrt old origin and $(x_{n}, y_{n})$ wrt new origin, then,
$$(x_{n}, y_{n}) = (x_{o} - a, y_{o} - b)$$

![[Pasted image 20230714071635.png]]

To change an equation, we put the value of $x_{o}$ and $y_{o}$ in terms of $x_{n}$, $y_{n}$. 

![[Pasted image 20230714071944.png]]

## Rotation of Axis

Here we use [[01 Algebra#Matrix Multiplication|matrix multiplication.]]

For old coordinates,
$$
\begin{bmatrix}
x_{o} \\
y_{o}
\end{bmatrix}
= 
\begin{bmatrix}
\cos \theta & -\sin \theta  \\
\sin \theta & \cos \theta
\end{bmatrix}
\begin{bmatrix}
x_{n} \\
y_{n}
\end{bmatrix}
$$
which gives,
$$x_{o} = x_{n}\cos \theta - y_{n}\sin \theta$$
$$y_{o} = x_{n}\sin \theta + y_{n}\cos \theta$$



For new coordinates,
$$
\begin{bmatrix}
x_{n} \\
y_{n}
\end{bmatrix}
= 
\begin{bmatrix}
\cos \theta & \sin \theta  \\
-\sin \theta & \cos \theta
\end{bmatrix}
\begin{bmatrix}
x_{o} \\
y_{o}
\end{bmatrix}
$$
which gives,
$$x_{n} = x_{o}\cos \theta + y_{o}\sin \theta$$
$$y_{n} = -x_{o}\sin \theta + y_{o}\cos \theta$$

We can remember where -ve is by taking a point on old x axis and then rotating this axes by 90. This will put the point on the -ve new y axis. Then we can see from where the -ve can be formed. 
We can also remember the expression for old and then put $-\theta$ in place of $\theta$ for the new coordinates.

![[Pasted image 20230714073237.png]] 

## Examples

![[Pasted image 20230705083512.png]]

In triangle questions, we have to take care to take both the +ve and the -ve value of area,
![[Pasted image 20230706082544.png]]

If order of vertices is not given, we have to make cases,
![[Pasted image 20230706082620.png]]

There are many methods to do one question, this is especially true in the case of coordinate geometry,
![[Pasted image 20230707100448.png]]
![[Pasted image 20230707100501.png]]
![[Pasted image 20230707100516.png]]

![[Pasted image 20230707102055.png]]

![[Pasted image 20230708100505.png]]

In short cut method we find the linear relation between the coefficients and then make the coefficients the same. Now comparing the coefficients of the coefficients in the obtained expression will be the point. 
![[Pasted image 20230708100633.png]]

![[Pasted image 20230712091710.png]]
![[Pasted image 20230712091725.png]]

![[Pasted image 20230712092011.png]]

![[Pasted image 20230712092719.png]]

![[Pasted image 20230712093507.png]]


