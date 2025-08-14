Links: [[01 Equation of a Circle]]
___
# Circles
Circle is a locus of a point which is at a constant distance from a fixed point. This constant distance is called radius and the fixed point is called centre. 

From a fixed point $C:(h,k)$ locus of a point $P$ which is at a distance r from C is given using, 
$$CP = r$$
Using distance formula,
$$r^{2} = (x - h)^{2} + (y-k)^{2}$$
Thus the equation of a circle with centre $C:(h,k)$ and radius r can be given as,
$$(x - h)^{2} + (y - k^{2}) = r^{2}$$

**Note:** in a question of circle, try to use geometry as it may shorten the solution. 

### General Equation of Circle
Opening the previous equation, we get,
$$x^{2} + y^{2} - 2jx - 2ky + h^{2} + k^{2} - r^{2} = 0$$

Thus the **general equation of circle** will be,
$$x^{2} + y^{2} + 2gx + 2fy + c = 0$$
where we have put $h = -g;\ k = -f;\ h^{2} + k^{2} - r^{2} = c$.
Note that the coefficients of both $x^{2},y^{2}$ need to be the same.

Here centre will be,
$$C:(-g, -f)$$
And radius will be,
$$r = \sqrt{ g^{2} + f ^{2} - c }$$

From the general equation, if 
- $g^{2} + f ^{2} - c > 0$ then circle will be real with finite non zero radius.
- $g^{2} + f ^{2} - c = 0$ then circle will be real with zero radius i.e. only C will satisfy the equation. (this is called **Point Circle**). 
  In this case the equation can be written as,
  $$(x + g)^{2} + (y + f)^{2} = 0$$
- $g^{2} + f ^{2} - c < 0$ then circle will be imaginary and no real point on the coordinate plane will satisfy the equation.

For a general 2 degree equation to represent a circle the required conditions are,
1. Coefficient of $x^{2}$ = Coefficient of $y^{2}$
2. Coefficient of $xy = 0$ 

Thus if,
$$ax^{2} + by^{2} + 2hxy + 2gx + 2fy + c = 0$$
is a circle, then $a = b$ and $h = 0$. 

## Finding Equation of Circle 
#### If 3 Points are given
If 3 point on the circle are given, with coordinates as $(x_{i}, y_{i}),\ i = 1,2,3$, then, we can use [] methods to find equation.

1. Assume equation of circle as $x^{2} + y^{2} + 2gx + 2fy + c = 0$ then substitute these points in the equation. Since the points lie on the circle, they satisfy the equation. This gives 3 linear equations in g, f, c which can be solved for their values. 
   $\\$

2. Find equations of any two perpendicular bisectors of sides, say $C_{1}D$ and $C_{1}E$. Solve these to get $C_{1}$. Now find the distance of $C_{1}$ from any of the 3 points. This will be the radius. Now using centre and radius, find equation of circle. 
	$\\$

3. Equation of circle can be given as,
   
$$
\begin{vmatrix}
x^{2}+y^{2} & x & y & 1 \\
x_{1}^{2}+y_{1}^{2} & x_{1} & y_{1} & 1 \\
x_{2}^{2}+y_{2}^{2} & x_{2} & y_{2} & 1 \\
x_{3}^{2}+y_{3}^{2} & x_{3} & y_{3} & 1 \\
\end{vmatrix} = 0
$$

However, we might be able to solve the question very quickly if we observe a property,
![[Pasted image 20230715094937.png]]

But in some cases, just start solving.
![[Pasted image 20230715095004.png]]
![[Pasted image 20230715095017.png]]

#### Two Non Parallel Lines and a point are given
If a circle touches two non parallel lines, then its centre lies on one of the [[08 Angular Bisector|angular bisectors]] of the lines. 

![[Pasted image 20230715095759.png]]

But there will be infinite number of circles like this, so we need a point to determine the circle uniquely. 

Example,
![[Pasted image 20230715095817.png]]

If the radius is given, then we get 4 circles, two on each bisector or 1 in each region. 

Another example,
![[Pasted image 20230717084222.png]]

##### Incircle and Excircle
Number of circles which will touch 3 given non parallel and non concurrent straight lines will be 4. 

![[Pasted image 20230717084332.png]]

The incircle will be the smallest of the 4.

![[Pasted image 20230717084957.png]]

## Orthogonal Intersection

Angle between two curve is defined as the the angle between their tangents at the POI. 

Two curves are said to intersect orthogonally if their angle of intersection is 90$^{\circ}$. 

Let circles,
$$x^{2} + y^{2} + 2g_{i}x + 2f_{i}y + c_{i} = 0,\ i = 1,2$$
intersect orthogonally 

Tangent for one of the circles at POI will be normal to other circle hence will pass through centre of other circle. 

In $\Delta C_{1}C_{2}A$,
$$
\begin{split}
(C_{1}C_{2})^{2} &= r_{1}^{2} + r_{2}^{2} \\
(g_{1} - g_{2})^{2} + (f_{1} - f_{2})^{2} &= (g_{1}^{2} + f_{1}^{2} - c_{1}) + (g_{2}^{2} + f_{2}^{2} - c_{2}) \\
2(g_{1}g_{2} + f_{1}f_{2}) &= c_{1} + c_{2}
\end{split}
$$
This is the condition for orthogonality. 
Note that this equation may be satisfied for imaginary circles also. 

If two circles intersect orthogonally, then length of tangent from centre of one of the circles to other circle will be equal to radius of the first circle. I.e. if we draw tangent from $C_{1}$ to $S_{2}$, then length of tangent $C_{1}A = r_{1}$. 

![[Pasted image 20230729090004.png]]

## Power of a point wrt a Circle 
There are infinite chords passing through an internal point in a circle and,
$$PA.PB = PC.PD = PE.PF = |S_{p}|$$

![[Pasted image 20230729091114.png]]

If the point lies outside,
$$PA.PB = PC.PD = PT^{2} = |S_{p}|$$

![[Pasted image 20230729091332.png]]

$S_{p}$ is called **Power of Point P** wrt given circle. Thus if P lies on the circle, then we say that power of P is zero. 


**Proof:**
Take a point $P:(h,k)$ and a circle,
$$x^{2} + y^{2} + 2gx + 2fy + c = 0$$
Draw a chord on this circle from point P. 

Any point of line AB can be taken as $(h+r\cos \theta, k + r\sin \theta)$. 

Now if this point lies on the circle,
$$(h+r\cos \theta)^{2} + (k+r\sin \theta)^{2} + 2g(h+r\cos \theta) + 2f(K+r\sin \theta) + c = 0$$
$$r^{2} + r(\dots) + h^{2} + k^{2} + 2gh + 2fk + c = 0$$
This will give two values of r, $r_{1},r_{2}$, for two points A and B. 

Now product of roots,
$$h^{2} + k^{2} + 2gh + 2fk + c$$
which is $S_{p}$ and thus independent of $\theta$.

![[Pasted image 20230729092029.png]]

## 


## Examples
![[Pasted image 20230724084156.png]]
![[Pasted image 20230724084203.png]]

![[Pasted image 20230724084218.png]]
![[Pasted image 20230724084230.png]]

![[Pasted image 20230724085336.png]]

![[Pasted image 20230724091941.png]]

![[Pasted image 20230724092313.png]]
![[Pasted image 20230724092323.png]]

![[Pasted image 20230724093119.png]]
![[Pasted image 20230724093137.png]]

![[Pasted image 20230724093748.png]]
![[Pasted image 20230724093803.png]]