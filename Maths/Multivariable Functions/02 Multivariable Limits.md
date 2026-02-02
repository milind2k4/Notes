Links: [[01 Partial Differentiation]]
___
# Multivariable Functions
## Limits 
[[00 Limits]]
A function $f(x,y)$ is said to have a limit L as the point $(x,y)$ approaches $(a,b)$ and is denoted as,

$$\lim_{ (x,y) \to (a,b) } f(x,y) = L$$

#### Evaluation of Limits 
1. Evaluate $f(x,y)$ along path 1: $x \to a$, then $y \to b$. I.e.,
	$$\lim_{ y \to b } (\lim_{ x \to a } f(x,y))$$
1. Evaluate $f(x,y)$ along path 2: $y \to b$, then $x \to a$. I.e.,
	$$\lim_{ x \to a } (\lim_{ y \to b } f(x,y))$$

Limit exists only if the limits along path 1 and 2 are the same, otherwise not. 

If $a = b = 0$, then in addition to evaluating the limit along path 1 and 2, we evaluate limits,
$$\lim_{ x \to 0 } f(x,y)|_{y=mx}$$
$$\lim_{ x \to 0 } f(x,y)|_{y=mx^{2}}$$

For example,
$$
\begin{split}
\lim_{ (x,y) \to (1,2) }& \frac{ x^{2} + 2y }{ x^{2} + y^{2} } \\
\text{Case 1},\\
\lim_{ y \to 2 }& \left( \lim_{ x \to 1 } \frac{ x^{2} + 2y }{ x^{2} + y^{2} } \right) \\
\lim_{ y \to 2 }& \left( \frac{ 1 + 2y }{ 1 + y^{2} } \right) \\ \\
&= 1 \\
\\
\text{Case 2}, \\
\lim_{ x \to 1 } & \left( \lim_{ y \to 2 } \frac{ x^{2} + 2y }{ x^{2} + y^{2} } \right) \\
\lim_{ x \to 1 } & \left( \lim_{ y \to 2 } \frac{ x^{2} + 4 }{ x^{2} + 4 } \right) \\
&= 1 \\
\\
\text{Thus, Limit} &= 1
\end{split}
$$

Another example,
$$
\begin{split}
\lim_{ (x,y) \to (0,0) } & \frac{ x^{2}y }{ x^{4} + y^{2} } \\
\text{Case 1},\\
\lim_{ y \to 0 } & \left( \lim_{ x \to 0 } \frac{ x^{2}y }{ x^{4} + y^{2} } \right) \\
\lim_{ y \to 0 } & (0) \\
&= 0 \\
&= f_{1} \text{ (say)} \\
\\
\text{Case 2},\\
\lim_{ x \to 0 } & \left( \lim_{ y \to 0 } \frac{ x^{2}y }{ x^{4} + y^{2} } \right) \\
\lim_{ x \to 0 } & (0) \\
&= 0 \\
&= f_{2} \\
\\
\text{Case 3, put } y &= mx \\
\lim_{ x \to 0 } & \frac{ mx^{3} }{ x^{4} + m^{2}x^{2} } \\
&= 0 \\
&= f_{3} \\
\\
\text{Case 4, put } y &= mx^{2} \\
\lim_{ x \to 0 } & \frac{ x^{4} }{ x^{4} + m^{2}x^{4} } \\
\lim_{ x \to 0 } & \frac{ m }{ 1 + m^{2} } \\
&= f_{4} \\
\text{Clearly, } \\
f_{1} = f_{2} = f_{3} &\neq f_{4} \\
\text{Thus, limit DNE.}
\end{split}
$$

## Continuity and Differentiability 
[[08 Continuity]] 
[[09 Differentiability]]

A function $f(x,y)$ is said to be continuous at a point $(a,b)$ if,
$$\lim_{ (x,y) \to (a,b) } f(x,y) = f(a,b)$$

A function $f(x,y)$ is said to be differentiable at a point $(a,b)$ if,
$$\lim_{ (h,k) \to (0,0) } \frac{ f(a+h,b+k) - f(a,b) - hf_{x}(a,b) - kf_{y}(a,b) }{ \sqrt{ h^{2} + k^{2} } }$$

If $f(x,y)$ is differentiable, then partial derivatives $f_{x}$ and $f_{y}$ both exist and are finite.

$$
\begin{split}
f_{x} &= \frac{ \partial f }{ \partial x } &= \lim_{ h \to 0 } \frac{ f(x+h, y) - f(x,y) }{ h } \\
f_{y} &= \frac{ \partial f }{ \partial y } &= \lim_{ k \to 0 } \frac{ f(x, y+k) - f(x,y) }{ k } 
\end{split}
$$

To do differentiability questions we first find $f_{x}$ and $f_{y}$. Then we put them into the main (big) formula. 

