Links: [[00  Circle]], [[09 Pair of Straight Lines]]
___
# General Results for Conic Curves
if in the equation of conic curve, we make RHS = 0, then the 2 degree expression present on LHS is denoted by $S$. I.e. $S = 0$ will be the equation of the conic curve. 

If equation of conic is,
$$ax^{2} + by^{2} + 2hxy + 2gx + 2fy + c = 0$$
Then we define S as,
$$S = ax^{2} + by^{2} + 2hxy + 2gx + 2fy + c$$

For a given point $P:(x_{1},y_{1})$ wrt a given conic S = 0, we define two quantities $S_{p}$ and T,
$$S_{p} = S(P) = S(x_{1},y_{1})$$
which will be a number. 

$$T = axx_{1} + b yy_{1} + h(xy_{1} + yx_{1}) + g(x + x_{1}) + f(y + y_{1}) + c$$
which is a linear expression of x and y. 

T can be obtained from S by,
$$
\begin{split}
x^{2} &\to x x_{1} \\
y^{2} &\to y y_{1} \\
xy &\to \frac{xy_{1}+yx_{1}}{2} \\
x &\to \frac{x+x_{1}}{2} \\
y &\to \frac{y+y_{1}}{2} \\
c &\to c
\end{split}
$$

A general conic with centre at origin can be given as,
$$ax^{2} + by^{2} + 2hxy = 1$$

### Tangents and Chords

If point P lies on the conic curve S = 0, then, $S_{p} = 0$. 
If point P lies on the curve then equation of tangent at P is given by,
$$T = 0\ (\text{wrt P})$$
this tangent is curve and point specific. 

If a point P lies inside the curve then equation of the chord which is bisected at point P is given as,
$$T = S_{p} \ (\text{wrt P})$$
If point P is taken as centre in the case of circle, then $T = S_{p}$ will give $0 =0$ as all the chords passing through centre will be bisected at it. 


If point P lies outside the curve S = 0, then from it 2 tangents can be drawn to the conic, then,
- Equation of Chord of Contact of P will be $T = 0\ (\text{wrt P})$
- Joint Equation of Tangents will be given as,
$$SS_{p} = T^{2}$$

To find the mid point of Chord of Contact, we do not have to solve the whole equation,
![[Pasted image 20230720091518.png]]

Seeing from the point P's perspective sometimes makes the question easier. 
![[Pasted image 20230720095142.png]]

### Pole and Polar

Let P is a fixed point and a variable chord AB is drawn through P. Now locus of point of intersection of tangents drawn at A and B will be a straight line and this line is called **Polar** of point P. 
This line has equation,
$$T = 0\ (\text{wrt P}) \equiv L$$

![[Pasted image 20230720100010.png]]

Conversely if tangents are drawn from different points on line L to a conic, then the corresponding chord of contact will pass through a fixed point and that fixed point P is called **Pole of line L**

![[Pasted image 20230722080426.png]]

If line L is polar of point P, then point P is called Pole of Line L/
Pole and polar pair is unique. 
If point P lies outside the curve, its chord of contact will be its polar as both the lines will have same equation, T = 0. 
If point P lies on the curve, then its tangent is its polar as both have equation T = 0.

If pole is given, to find polar write T = 0. 
If polar is given, to find pole assume pole as $P:(h, k)$ write T = 0 for it and then compare coefficients of this equation with given equation of polar to get h, k/ 

![[Pasted image 20230722081625.png]]
![[Pasted image 20230722082302.png]]
(the coordinates of P have x and y reversed)

### Length of Chord 
Let a line L = 0 and a conic curve S = 0 intersect at two points A and B. To find these points solve L = 0 and S = 0 simultaneously. 

Eliminating y, we get a quadratic $Q(x)$ whose roots are $x_{A}, x_{B}$. 
$$|x_{A} - x_{B}| = \frac{ \sqrt{ D } }{ a }$$

Now, 
$$(y_{A} - y_{B}) = m (x_{A} - x_{B})$$

Putting this into the distance formula,
$$
\begin{split}
AB &= \sqrt{ (y_{A} - y_{B})^{2} + (x_{A} - x_{B})^{2} } \\ &= \sqrt{ m^{2}(x_{A} - x_{B})^{2} + (x_{A} - x_{B})^{2} } \\
&= | x_{A} - x_{B} |\sqrt{ m^{2} + 1 } \\
&= \frac{ \sqrt{ D } \sqrt{ m^{2} + 1 } }{ |a| }
\end{split}
$$

Alternatively, if we eliminate x, 
$$AB = |y_{A} - y_{B}| \sqrt{ 1 + \frac{ 1 }{ m^{2} } }$$
$$AB = \frac{ \sqrt{ D } }{ a } \sqrt{ \frac{ 1 }{ m^{2} } + 1 }$$

![[Pasted image 20230722082632.png]]

We can also use geometry, 
![[Pasted image 20230722083620.png]]

Example,
![[Pasted image 20230722084154.png]]