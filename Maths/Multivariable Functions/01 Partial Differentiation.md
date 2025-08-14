Links: 
___
# Partial Differentiation

When a function has 2 or more independent variables, then it's derivative w.r.t any one of them is called its **Partial Derivative** and the process is called **Partial Differentiation.**

If,
$$z = f(x,y)$$
Then,
$$\frac{ \partial z }{ \partial x } = f_{x}$$
is called the partial derivative of $z$ w.r.t $x$.

#### Finding PD
To find $\displaystyle \frac{ \partial z }{ \partial x }$ we simply do $\displaystyle \frac{ dz }{ dx }$ treating $y$ as constant.

For example,
$$
\begin{split}
z &= x^{2} + y^{2} \\
\frac{ \partial z }{ \partial x } &= 2x \\
\frac{ \partial z }{ \partial y } &= 2y\\
\\
z &= 2x^{3}y^{2} \\
\frac{ \partial z }{ \partial x } &= 6x^{2}y^{2} \\
\frac{ \partial z }{ \partial y } &= 4x^{3}y^{2} 
\end{split}
$$

### Higher Order Derivative
If,
$$z = f(x,y)$$
Then,
$$
\begin{split}
f_{xx} &= \frac{ \partial^{2} z }{ \partial x^{2} } = \frac{ \partial  }{ \partial z } \left( \frac{ \partial z }{ \partial x } \right) \\
f_{xy} &= \frac{ \partial^{2} z }{ \partial x \partial y } = \frac{ \partial  }{ \partial x } \left( \frac{ \partial z }{ \partial y } \right) 
\end{split}
$$

And, in general,
$$\frac{ \partial^{2} z }{ \partial x \partial y } = \frac{ \partial^{2} z }{ \partial y \partial x }$$

Again, if,
$$u = f(x,y,z)$$
Then,
$$
\begin{split}
f_{x x x} &= \frac{ \partial^{3} u }{ \partial x^{3} } \\
f_{xyz} &= \frac{ \partial^{3} u }{ \partial x \partial y \partial z } \\
f_{x x y} &= \frac{ \partial^{3} u }{ \partial x^{2} \partial y }   
\end{split}
$$

## Homogeneous Function
[[00 Functions#Homogeneous Expression]]

A function $f(x,y)$ is said to be homogeneous of degree (order) $n$, if ti can be expressed in the form,
$$x^{n} f\left( \frac{ y }{ x } \right) \ or\ y^{n} f\left( \frac{ x }{ y } \right)$$

Alternatively, if we put $x = tx$, and $y = ty$, then for a homogeneous function,
$$f(tx,ty) = t^{n}f(x,y)$$
where $n$ is the degree. 

For example,
$$
\begin{split}
u &= \frac{ x^{3} + y^{3} }{ x + y } \\
&= \frac{ x^{3}( 1 + (y /x)^{3}) }{ x(1 + y /x) } \\
&= x^{2} \frac{ 1 + (y /x)^{3} }{ 1 + (y /x) } \\
&= x^{2} f(x,y)\\
\\
\text{Alternatively,} \\
u(tx,ty) &= \frac{ (tx)^{3} + (ty)^{3} }{ (tx) + (ty) } \\
&= t^{2} u(x,y) \\
\end{split}
$$

Thus the function is a homogeneous function of degree 2.

However,
$$
\begin{split}
u &= \sec^{-1} \frac{ x^{8} + y^{8} }{ x^{3} + y^{3} }\\
\sec u &= \frac{ x^{8} + y^{8} }{ x^{3} + y^{3} }
\end{split}
$$
is not a homogeneous function because the $u$ on LHS is not "alone" i.e. it is of the form $F(u)$.

### Euler's Theorem on Homogeneous Functions
If $u$ is a homogeneous function of degree $n$ in $x, y$, then,
$$x \frac{ \partial u }{ \partial x } + y \frac{ \partial u }{ \partial y }  = nu$$
This is valid always. 

> Proof:
> Since $u$ is a homogeneous function,
> $$
> \begin{split}
> u &= x^{n} f\left( \frac{ y }{ x } \right) \\
> \frac{ \partial u }{ \partial x } &= x^{n}f'(y /x) \frac{ -y }{ x^{2} } + f\left( \frac{y}{x} \right) nx^{n-1} \\
> x\frac{ \partial u }{ \partial x } &= -yx^{n-1} f'\left( \frac{y}{x} \right) + nx^{n} f\left( \frac{y}{x} \right) \\
> \\
> \frac{ \partial u }{ \partial y } &= x^{n}f'\left( \frac{y}{x} \right) \frac{ 1 }{ x } \\
> &= x^{n-1} f'\left( \frac{y}{x} \right) \\
> y\frac{ \partial u }{ \partial y } &= yx^{n-1} f'\left( \frac{y}{x} \right) \\
> \\
> \text{Adding them,} \\
> x\frac{ \partial u }{ \partial x } + y\frac{ \partial u }{ \partial y } &= nx^{n}f\left( \frac{ y }{ x } \right) \\
> &= nu\\
> &\text{Hence Proved.}
> \end{split}
> $$

#### Deductions
If $u$ is a homogeneous function of degree $n$ in $x,y$ then,
$$x^{2}\frac{ \partial^{2} u }{ \partial x^{2} } + 2xy \frac{ \partial^{2} u }{ \partial x \partial y } + y^{2} \frac{ \partial^{2} u }{ \partial y^{2} } = n(n-1)u$$

If $F(u) = V(x,y)$ where $V$ is homogeneous function in $x,y$ of degree $n$, then,
$$
\begin{split}
x\frac{ \partial u }{ \partial x } + y\frac{ \partial u }{ \partial y } &= n \frac{ F(u) }{ F'(u) } \\
\\
x^{2}\frac{ \partial^{2} u }{ \partial x^{2} } + 2xy \frac{ \partial^{2} u }{ \partial x \partial y } + y^{2} \frac{ \partial^{2} u }{ \partial y^{2} } &= g(u)[g'(u)-1] 
\end{split}
$$
where,
$$g(u) = n \frac{ F(u) }{ F'(u) }$$

### Implicit Functions
If,
$$u = f(x,y) = c$$

Then,
$$
\frac{ dy }{ dx } = -\frac{ \displaystyle \frac{ \partial f }{ \partial x } }{ \displaystyle \frac{ \partial f }{ \partial y } }
$$

### Composite Function 
If $u$ is a function of $x,y$ and $x,y$ are functions of $t$, then $u$ is said to be a composite function of $t$. 

$$\ce{ u -> f(x,y) -> t }$$

Then, we can write,
$$\frac{ du }{ dt } = \frac{ \partial u }{ \partial x } \frac{ dx }{ dt } + \frac{ \partial u }{ \partial y } \frac{ dy }{ dt }$$

Again, if,
$$\ce{ u -> f(x,y,z) -> t }$$

Then we can write,
$$\frac{ du }{ dt } = \frac{ \partial u }{ \partial x } \frac{ dx }{ dt } + \frac{ \partial u }{ \partial y } \frac{ dy }{ dt } + \frac{ \partial u }{ \partial z } \frac{ dz }{ dt }$$

This is also called **Total Derivative** if $x, y, z$ are functions of a single variable. 

If $x, y, z$ are also multivariable functions,
$$\ce{ u -> f(x, y, z) -> s,t }$$

Then,
$$
\begin{split}
\frac{ \partial u }{ \partial s } &= \frac{ \partial u }{ \partial x } \frac{ \partial x }{ \partial s } + \frac{ \partial u }{ \partial y } \frac{ \partial y }{ \partial s } + \frac{ \partial u }{ \partial z } \frac{ \partial z }{ \partial s } \\
\\
\frac{ \partial u }{ \partial t } &= \frac{ \partial u }{ \partial x } \frac{ \partial x }{ \partial t } + \frac{ \partial u }{ \partial y } \frac{ \partial y }{ \partial t } + \frac{ \partial u }{ \partial z } \frac{ \partial z }{ \partial t }  
\end{split}
$$


## Taylor's Theorem
It is used to expand a function in the neighborhood of a point $(a,b)$. 

$$
\begin{split}
f(x,y) &= f(a,b) \\
&+ [(x-a)f_{x}(a,b) + (y-b)f_{y}(a,b)] \\
&+ \frac{ 1 }{ 2! } [(x-a)^{2}f_{xx}(a,b) + 2(x-a)(y-b)f_{xy}(a,b) + (y-b)^{2}f_{yy}(a,b)]\\
&+ \frac{ 1 }{ 3! }[(x-a)^{3}f_{xxx}(a,b) + (y-b)^{3}f_{yyy}(a,b) + 3(x-a)^{2}(y-b)f_{xxy}(a,b) + 3(x-a)(y-b)^{2}f_{xyy}(a,b)] \\
&+ \dots
\end{split}
$$

If the point $(a,b)$ is $(0,0)$ then the series is called Maclaurin series. 


