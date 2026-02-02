Links: [[01 Analyticity]]
___
# Harmonic Function

A function of $x,y$ which possesses continuous partial derivatives of the first and second order and satisfies Laplace's equations is called a Harmonic function. 

Laplace's Equation,
$$\frac{ \partial^{2} u }{ \partial x^{2} } + \frac{ \partial^{2} v }{ \partial y^{2} } = 0$$

If a function, $f(z) = u + iv$ is an analytic function, then $u$ and $v$ are both Harmonic functions.

$u$ and $v$ are called ***Conjugate Harmonic*** functions, 

#### Finding Conjugate
If $u$ is given and we need to find $v$, we will first use [[01 Partial Differentiation#Composite Function|total derivatives]] to write,

$$dv = \frac{ \partial v }{ \partial x } dx + \frac{ \partial v }{ \partial y } dy$$

Now, using C-R equations,
$$
\begin{split}
dv &= \left( -\frac{ \partial u }{ \partial y } \right) dx + \frac{ \partial u }{ \partial x } dy \\
v &= \int -\frac{ \partial u }{ \partial y } \, dx + \int \frac{ \partial u }{ \partial x } \, dy + c \\
&= \underbrace{ \int f(x,y) \, dx }_{ \text{treat y terms as constant} }  + \underbrace{ \int f(x,y) \, dy }_{ \text{ignore all terms having x} }  
\end{split}
$$