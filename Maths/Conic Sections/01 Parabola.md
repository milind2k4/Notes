Links: [[00 Conic Sections]]
___
# Parabola 
It is locus of a point (say P) which is equidistant from a given point (S) and a given line (L).

$$PS = PL$$

For a 2 degree equation to represent parabola, we must have $\Delta \neq 0$ and
$$h^{2} = ab$$
I.e. the 2 degree terms will make a perfect square. 


### [[01.1 Std. Equation, terms and Other Parabola]]


### Parametric Point
A point on $y^{2} = 4ax$ can be taken as,
$$P:(at^{2},2at)$$
This is also called *point 't'.*

Use y coordinate where ever possible to find t. 

If we join this point to origin, the slope of the line formed will be,

$$m_{OP} = \frac{ 2at - 0 }{ at^{2} - 0 } = \frac{ 2 }{ t }$$

### Focal Distance 
For any point of parabola, $PS = PL = a + x_{P}$. Thus focal distance of point P,
$$PS = a + \text{x-coordinate of P}$$

Thus the vertex will be the closest to the focus. 

For parametric point,
$$PS = a + at^{2} = a(1 + t^{2})$$

Also, the sum of distances from focus,
$$\frac{ 1 }{ PS } + \frac{ 1 }{ QS } = \frac{ 1 }{ a(1 + t^{2}) } + \frac{ 1+t^{2} }{ a(1 + t^{2}) } = \frac{ 1 }{ a }$$
i.e.
$$\frac{ 1 }{ PS } + \frac{ 1 }{ QS } = \frac{ 2 }{ 2a }$$
thus PS, 2a and QS are in HP. 

Harmonic mean of length of segments of any focal chord will be semi LR (i.e. 2a).

![[Pasted image 20230918114425.png]]

###  [[01.2 Chord of Parabola]]

### Position of a Point wrt Parabola 
Like [[02 Location of a Point wrt Circle|circle]]. 

![[Pasted image 20230918122215.png]]

### Some other Important Results 

##### Concyclic Points
For 4 concyclic points, the sum of their ordinates or parameters is zero. 
$$\sum t_{A} = \sum y_{A} = 0$$

Or for a general parabola, the sum of the algebraic perpendicular lengths of 4 concyclic points will vanish. 

![[Pasted image 20230919103742.png]]

##### Area of Triangle 
Area of triangle made by any 3 points on the parabola,
$$
\begin{split}
Ar(ABC) &= \frac{1}{2} \begin{vmatrix}
at_{1}^{2} & 2at_{1} & 1 \\
at_{2}^{2} & 2at_{2} & 1 \\
at_{3}^{2} & 2at_{3} & 1 \\
\end{vmatrix} \\
&= \left| a^{2} \prod (t_{1} - t_{2}) \right| 
\end{split}
$$
This can also be written as 
$$Ar(ABC) = \left| \frac{ 1 }{ 8a } \prod (y_{1} - y_{2}) \right|$$
if we substitute $t_{i} = y_{i} /2a$

Area of triangle formed by tangents at the 3 points, 
$$Ar(PQR) = \frac{ a^{2} }{ 2 } \left| \prod (t_{1} - t_{2}) \right| = \frac{ Ar(ABC) }{ 2 }$$

![[Pasted image 20230919104425.png]]

Also, the orthocentre of a triangle formed by any three tangents to a parabola lies on its directrix. 

##### Mutually Perpendicular Tangents 
Tangents at the end points of a focal chord will intersect at directrix and they will intersect at 90$^{\circ}$. 

Tangents drawn from any point on the directrix to the parabola will be mutually perpendicular and chord of contact will be focal chord. 

The foot of perpendicular from the point of intersection to the focal chord will be focus. 

![[Pasted image 20230919104937.png]]

Intercepted portion of the tangent between the point of tangency and directrix will make right angle at focus. 

##### Tangent and related triangles
A tangent at a point is drawn and it intersects the x axis. 
![[Pasted image 20230919105839.png]]

$$\Delta NOT \sim \Delta PQT$$
And thus,
$$\frac{ NO }{ PQ } = \frac{ NT }{ PT } = \frac{ OT }{ TQ } = \frac{ 1 }{ 2 }$$

N is the mid point of PQ. I.e. the tangent at vertex bisects any other tangent which intersects the axis.  
O is the mid point of TQ. 

$SN \perp PT$ i.e. foot of perpendicular from focus to any tangent will lie on tangent at vertex. 

$SP = ST = a(1 + t^{2})$ and thus $\Delta SPT$ is isosceles. 

Circle drawn on any focal radius as diameter, it will touch tangent at vertex. 

Circle drawn on any focal chord as diameter, it will touch directrix.
![[Pasted image 20230919110241.png]]


![[Pasted image 20230919112615.png]]
Here,
$$PS = TS = PK = SN = a(1 + t^{2})$$
Tangent will bisect the angle SPK. The other angular bisector will be the normal at P. 

Focus will be circumcentre of $\Delta PTN$.

Projection of PN on the axis, i.e. QN will always be 2a. If it is a standard parabola, we call this the sub normal. 

##### Reflection Property 
any ray parallel to axis of the parabola will pass through focus after reflection from it. 

![[Pasted image 20230919113638.png]]

## [[01.5 Examples (Parabola)]]