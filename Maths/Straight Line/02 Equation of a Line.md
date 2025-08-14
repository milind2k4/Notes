Links: [[00 Straight Line]]
___
# Equation of Straight Line
Equation of a curve in 2d i.e. x-y plane is a relation between x and y which is satisfied for all points on the curve but for no point not on the curve. 

Equation of a straight line in 2d will be linear in both x and y and vice-versa. 
Thus equation of a straight line can always be written as,

$$ax + by + c = 0$$

To define a straight line uniquely we only need two distinct points or we need one point and slope.

##### Special Cases
Equation of x axis is $y= 0$
Equation of y axis is $x= 0$

Equation of vertical line will be of the form $x = a$
Equation of horizontal line will be of the form $y = b$

### Different Forms of Equation of Straight Line
#### Two Point form
Let line L passes through two points $A:(x_{1},y_{1})$ and $B:(x_{2},y_{2})$.

Now consider a point on the line $P:(x,y)$.

Then slope can be given as,
$$m = \frac{ y - y_{1} }{ x - x_{1} } = \frac{ y_{2} - y_{1} }{ x_{2} - x_{1} }$$

Thus the equation can be written as,
$$\frac{ y-y_{1} }{ y_{2} - y_{1} } = \frac{ x - x_{1} }{ x_{2} - x_{1} }$$
$$\frac{ y - y_{1} }{ y_{1} - y_{2} } = \frac{ x - x_{1} }{ x_{1} - x_{2} }$$

Which becomes,
$$y - y_{1} = \frac{ y_{1} - y_{2} }{ x_{1} - x_{2} }(x - x_{1})$$


![[Pasted image 20230706091819.png]]

#### Slope Point form
If L passes through $A:(x_{1},y_{1})$ and has slope m then,

$$m = \frac{ y - y_{1} }{ x - x_{1} }$$
$$y - y_{1} = m(x - x_{1})$$

#### Slope Intercept form
If line L has slope m and y intercept c can be given as,

$$y - c = m(x - 0)$$
$$y = mx + c$$

To find y intercept (x intercept), we substitute $x = 0$ ($y = 0$) in the equation of line. 

#### Intercept form
Equation of a line which has x and y intercepts as $a$ and $b$ respectively can be given as,
$$y - 0 = \frac{ b - 0 }{ 0 - a }(x - a)$$
$$y = \frac{ -b }{ a }(x - a)$$
$$\frac{ y }{ b } + \frac{ x }{ a } = 1$$
$$\frac{ x }{ a } + \frac{ y }{ b } = 1$$

Here we cannot express vertical, horizontal or line passing through origin. 

#### Normal form
If line L is at a distance p form the origin and the perpendicular dropped from origin to the line makes angle $\alpha$ with the +ve x axis then

$$\frac{ x }{ \displaystyle  \frac{ p }{ \cos\alpha } } + \frac{ y }{ \displaystyle \frac{ p }{ \sin\alpha } } = 1$$
$$x\cos \alpha + y\sin \alpha = p$$
where, $\alpha \in [0, 2\pi)$ and $p > 0$. Thus we cannot express a line passing through origin.

![[Normal form straight line.png]]

To convert $ax + by + c = 0$ into normal form, we divide by $\sqrt{ a^{2} + b^{2} }$
![[Pasted image 20230706094156.png]]

#### Standard or General form
General equation of a straight line can be given as,
$$ax + by + c = 0$$
This equation can express every line.

This has slope,
$$m = \frac{ -a }{ b }$$

x intercept,
$$a = \frac{ -c }{ a }$$
y intercept,
$$b = \frac{ -c }{ b }$$

#### Parametric Equation
Parametric point is used to reduce number of variables. 

##### Algebraic form
A point on the line $ax + by + c = 0$ can be taken as,
$$A:\left( t, \frac{ -(at + c) }{ b } \right)$$
where t is parameter

$$A:\left( x, \frac{ -(ax + c) }{ b } \right)$$

##### Trigonometric or Polar form
#important 
Let $A:(h,k)$ be a point on line L which makes angle $\theta$ with the +ve x axis. 

A base point $A:(h,k)$ and slope $m = \tan \theta$ are given, then a point on the line which is r algebraic distance (dist. with sign) from the base point can be given as,
$$P:(h + r\cos \theta, k + r\sin \theta)$$
where r is parameter and $\theta \in [0, \pi)$.


Note than r will be +ve if p lies above A and -ve if it lies below A. 

![[Pasted image 20230706095857.png]]

Example,
![[Pasted image 20230706161836.png]]