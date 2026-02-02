Links: [[00 Indefinite Integration]]
___
# Differential Equation
Equation containing independent variable, dependent variable and differential coefficients (DC). 

$$x \frac{ d^{2} y }{ d x^{2} } + y = x^{3}$$

If all differential coefficients are defined wrt a single variable then the differential equation is called *Ordinary* else *Partial.*

$$y \frac{ \partial^{2} r }{ \partial y \partial x } + \frac{ \partial^{2} y }{ \partial z^{2} } = x + z$$
is partial DE.

DE represent a family of curves. 
E.g. 
$$x^{2} + y^{2} = r^{2}$$
is family of circles with center at origin and r is the parameter. This equation is called cartesian equation. 

This family can also be represented as,
$$x + y \frac{ dy }{ dx } = 0$$
This equation is called differential equation. 

The cartesian equation is called solution or general solution of differential equation and it contains arbitrary parameter, $r^{2}$, but not differential coefficients. 

While differential equation will contain differential coefficients but will not contain arbitrary constant. 

The solution of DE is called *Solution or General Solution or Primitive or Integral Curve.*
If in general solution we substitute all arbitrary constants with fixed values, then equation represents a fixed curve of family of curves and is called a *Particular Solution.*

#### Order and Degree 
The order of highest differential coefficient is called the **Order of the DE**. It is always defined. (or*de*r, so the number after the d). 

The order is the number of independent arbitrary constants in the final solution.

If DE can be expressed in the form of a polynomial of differential coefficients then the exponent of highest order DC is called degree and it may or may not be defined.

Some higher order DE questions can be solved quite simply or are familiar pattern.
![[Pasted image 20231023211913.png]]
![[Pasted image 20231023212219.png]]

## Some PTR
The solution of DE will satisfy it identically. This can be used to check for answers in the options or finding tangent at any point.

![[Pasted image 20231014185625.png]]
![[Pasted image 20231014185815.png]]

#### Tangent and Normal
Equation of tangent at a general point $P:(x,y)$ can be given as,
$$Y - y = \frac{ dy }{ dx } (X - x)$$
Similarly for normal,
$$Y - y = -\frac{ dx }{ dy } (X - x)$$

Point of intersection of tangent with x axis will be found by putting $Y = 0$. 
Similarly the intersection with y axis can be found by putting $X = 0$. 

$$\ce{ T_{P} x x-axis } \equiv \left( x - \frac{ y }{ y' }, 0 \right)$$
$$\ce{ T_{P} x y-axis } \equiv \left( 0, y - xy' \right)$$

Point of intersection of normal with x and y axes,
$$\ce{ N_{P} x x-axis } \equiv \left( x + yy', 0 \right)$$
$$\ce{ N_{P} x y-axis } \equiv \left( 0, y + \frac{ x }{ y' } \right)$$

#### Area Under Curve 
The area bound by $y = f(x)$ and x-axis, between x = a and x = x is given as,
$$
\begin{split}
A(x) &= \int_{a}^{x} |y| \, dx \\
A'(x) &= |y| \\
&= |f(x)| 
\end{split}
$$

![[Pasted image 20231014192937.png]]

#### Length of Curve 
$$
\begin{split}
dl &= \sqrt{ (dx)^{2} + (dy)^{2} } \\
AB &= \int_{A}^{B} \sqrt{ (dx)^{2} + (dy)^{2} } \\
l(x) &= \int_{a}^{x} \sqrt{ 1 + \left( \frac{ dy }{ dx }  \right)^{2} } \, dx \\
l'(x) &= \sqrt{ 1 + \left( \frac{ dy }{ dx }  \right)^{2} }
\end{split}
$$

![[Pasted image 20231014193428.png]]

#### Subtangent, Subnormal, length of tangent and normal 
[[01 Tangents and Normals#Some definitions]]

Subtangent = $\displaystyle \frac{y}{y'}$

Subnormal = $\displaystyle yy'$

Length of tangent = $\displaystyle y \sqrt{ 1 + \left( \frac{ 1 }{ y' } \right)^{2} }$

Length of Normal = $y \sqrt{ 1 + (y')^{2} }$

![[Pasted image 20231014193757.png]]

#### Substitution 
If variable x is present in the form of $f(x)$ only and there is one $f'(x)$ with $dx$ then substitute $f(x) = X \implies f'(x)dx = dX$. 

### Forming Differential Equations
1. Count the number of independent arbitrary constants after clubbing as many as we can (say n). This will be the order of DE. 
   $\\$
3. Differentiate the given equation n times.
   $\\$
4. Eliminate all the arbitrary constants from these n+1 equations. (n obtained in s-2 and 1 given equation)
   $\\$
5. The eliminant will be the required DE.

#### Examples 
![[Pasted image 20231014183010.png]]

![[Pasted image 20231014183415.png]]

![[Pasted image 20231014183949.png]]

![[Pasted image 20231014184835.png]]

## [[01 Solving Differential Equations]]


## [[02 Exact Differentials and Trig Subs.]]

## Higher Degree order 1 DE
**Singular Solution** is a solution without arbitrary constants. 

Usually we will denote $dy /dx$ as p. Thus,
$$p = \frac{ dy }{ dx },\ \frac{ dp }{ dx } = \frac{ d^{2} y }{ d x^{2} }, \text{ and so on.}$$

If we have DE of order 1, then its solution can have only one arbitrary constant.

#### Solvable for p
![[Pasted image 20231023210407.png]]

#### Solvable for x
![[Pasted image 20231023211003.png]]

#### Solvable for y
![[Pasted image 20231023211251.png]]

### Clairaut's Equation
It is of the form,
$$y = px + f(p)$$

![[Pasted image 20231023211530.png]]

## Misc. Examples Relating to Curves

![[Pasted image 20231016124850.png]]
![[Pasted image 20231016125643.png]]
![[Pasted image 20231016125904.png]]

![[Pasted image 20231016130328.png]]

![[Pasted image 20231016130844.png]]

![[Pasted image 20231016131418.png]]
![[Pasted image 20231016131428.png]]

![[Pasted image 20231016131941.png]]

![[Pasted image 20231018092008.png]]
![[Pasted image 20231018092020.png]]

![[Pasted image 20231018092514.png]]
![[Pasted image 20231018092527.png]]

#important 
![[Pasted image 20231023202644.png]]
![[Pasted image 20231023202654.png]]

![[Pasted image 20231023203018.png]]
![[Pasted image 20231023203029.png]]

![[Pasted image 20231023203406.png]]

![[Pasted image 20231023204501.png]]
![[Pasted image 20231023204520.png]]
