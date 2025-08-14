Links: 
___
# Partial Fractions
Aim is to convert a proper polynomial fraction into sum of fractions. 

$$\frac{ \text{Polynomial}_{1} }{ \text{Polynomial}_{2} }$$


The number of terms on RHS will be the same as the degree of the denominator. 

![[Pasted image 20230928185735.png]]

To find the values of $A, B_{1},B_{2}$ etc. we can either take LCM on RHS, cancel the denominator and then compare the coefficients. 

Or we can substitute n different values of x to get n equations and then solve them. n being the degree of denominator polynomial.

Or alternatively, we can multiply with the highest power of  one of the factors in the denominator and then put x = a so that it becomes zero. 
![[Pasted image 20230928190620.png]]

In this way we can find the value of coefficient of the max. power term. 

#### Partial Fractions
**All different linear factors,**
$$\frac{ P(x) }{ (x-a)(x-b)(x-c) } = \frac{ A }{ (x-a) } + \frac{ B }{ (x-b) } + \frac{ C }{ (x-c) }$$
$$A = (x-a) \cdot LHS | _{x=a}$$
(to do this ignore the (x-a) term and put x = a in the rest expression, whatever comes the value is the value of A) 
$$B = (x-b) \cdot LHS | _{x=b}$$
$$C = (x-c) \cdot LHS | _{x=c}$$

**Repeated roots,**
$$\frac{ P(x) }{ (x-a)(x-b)^{3} } = \frac{ A }{ (x-a) } + \frac{ B_{1} }{ (x-b) } + \frac{ B_{2} }{ (x-b)^{2} } + \frac{ B_{3} }{ (x-b)^{3} }$$

For $B_{1}$ and $B_{2}$, substitute any 2 values of x and solve obtained equation. 

**Quadratic,**
$$\frac{ P(x) }{ (x-a)(x-c)(\underbrace{ Q(x) }_{ D<0 }) } = \frac{ A }{ (x-a) } + \frac{ B }{ (x-b) } + \frac{ Ex+F }{ Q(x) }$$

For E and F put 2 values of x and solve the equations. 

### Examples
![[Pasted image 20230928191003.png]]

Pay close attention to the variable in the expression,
![[Pasted image 20230928191530.png]]

![[Pasted image 20230928192257.png]]

![[Pasted image 20230930112107.png]]