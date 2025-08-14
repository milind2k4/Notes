Links: [[00 Straight Line]]
___
# Pair of Straight Lines (POSL)
To get joint equation of two curves, multiply their equations after making RHS zero. 

E.g. if $C_{1}$ has equation $y = f(x)$ and $C_{2}$ has $g(x)$, then the joint equation of $C_{1}$ and $C_{2}$ can be written as 
$$
\begin{split}
C_{12} &= (y- f(x))(y-g(x)) \\
&= y^{2} - (f(x) + g(x))y + f(x)g(x) = 0
\end{split}
$$

Every point on either of the terms will always satisfy the joint equation. 

Note that joint equation is not $y^{2} = f(x)g(x)$. This is because a point not on both the curves will not satisfy this equation. 

#### Equation of Pair of Straight Lines
For joint equation of two lines,
$$L_{1} \equiv y = m_{1}x + c_{1}$$
$$L_{2} \equiv y = m_{2}x + c_{2}$$

$$(m_{1}x - y + c_{1})(m_{1}x - y + c_{2})$$
Which is,
$$m_{1}m_{2}x^{2} - xy(m_{1} + m_{2}) + y^{2} + \dots = 0$$
Thus a pair of straight lines will have an equation of degree two. But the reverse is not true. I.e. a two degree equation may or may not be equation of pair of straight lines. 

#### Conic Curves
aka Conic Curves. 

These are Pair of straight lines, circle, parabola, ellipse and hyperbola.

Equation of conic curve is of degree two and vice versa. 

A general 2 degree equation can be defined as,
$$ax^{2} + by^{2} + 2hxy + 2gx + 2fy + c$$
We define $\Delta$ or D here which is,
$$D = \begin{vmatrix}
a & h & g \\
h & b & f \\
g & f & c
\end{vmatrix}
= abc + 2fgh - af ^{2} - bg^{2} - ch^{2}$$

Now, the equation will represent,
- POSL if $\Delta = 0$
- Everything else if $\Delta \neq 0$ 
	- Circle if $a = b$ and $h = 0$ 
	- Parabola if $h^{2} = ab$
	- Ellipse if $h^{2} < ab$ 
	- Hyperbola if $h^{2} > ab$

![[Conic Sections.png]]
(1 is parabola, 2 is circle and ellipse, 3 is hyperbola)

### POSL with Any POI
The equation,
$$ax^{2} + by^{2} + 2hxy + 2gx + 2fy + c$$
Will represent a pair of straight lines when $\Delta = 0$,
$$abc + 2fgh - af ^{2} - bg^{2} - ch^{2} = 0$$

Angle between lines is given as,
$$\theta = \tan ^{-1} \left| \frac{ 2\sqrt{ h^{2} - ab } }{ a + b } \right| $$
If $h^{2} = ab \implies \theta = 0$ the lines will be parallel.

For the point of intersection of lines, differentiate the equation partially wrt x and y and solve them together.

Partially differentiating wrt x,
$$ax + hy + g = 0$$
Partially differentiating wrt y,
$$hx + by + g = 0$$
Solving them we get point of intersection,
$$A: \left( \frac{ hf - bg }{ ab - h^{2} }, \frac{ gh - fa }{ ab - h^{2} } \right)$$

Note that the lines which are obtained from partial differentiation are not $L_{1}$ and $L_{2}$ but have the same POI.

To find separate equation of lines $L_{1}$ and $L_{2}$ when their joint equation is given, we can solve the equation as quadratic in x or in y (treat the other as constant).
I.e. if solving for y, solve,
$$by^{2} + y(2hx + 2f) + ax^{2} + 2fx + c = 0$$
The two straight lines will be obtained by taking +ve and -ve sign. 

### 
#### Examples 
![[Pasted image 20230713085238.png]]
![[Pasted image 20230713085248.png]]

![[Pasted image 20230713092153.png]]

![[Pasted image 20230713092924.png]]

If one of the angular bisector is x axis, the other will be y axis as they are mutually perpendicular. If one of the angular bisectors is y = x then the other will be y = -x.
![[Pasted image 20230713093632.png]]
![[Pasted image 20230713093645.png]]