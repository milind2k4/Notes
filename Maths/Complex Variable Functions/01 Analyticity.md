Links: [[00 Complex Variable Functions]]
___
# Analyticity

A function $f(z)$ is said to be analytic at a point $z_{o}$, if it is one valued and differentiable not only at $z_{o}$, but also at every point in the neighborhood of $z_{o}$. 

### Conditions for Analyticity

The necessary and sufficient conditions for the function $w = f(z) = u(x,y) + iv(x,y)$ to be analytic in a region $\mathbb{R}$ are,

1. $$\frac{ \partial u }{ \partial x } , \frac{ \partial u }{ \partial y } , \frac{ \partial v }{ \partial x } , \frac{ \partial v }{ \partial y }$$
	are continuous functions of $x,y$ in the region $\mathbb{R}$ 
	$\\$
	
1. Cauchy Reimann Equations, 
   $$\frac{ \partial u }{ \partial x }  = \frac{ \partial v }{ \partial y }\ \& \frac{ \partial u }{ \partial y } = - \frac{ \partial v }{ \partial x }$$
	are satisfied. 


## Cauchy Reimann Equations
In Cartesian form,
$$
\begin{split}
\frac{ \partial u }{ \partial x } &= \frac{ \partial v }{ \partial y } \\
\frac{ \partial u }{ \partial y } &= -\frac{ \partial v }{ \partial x } 
\end{split}
$$

In Polar form,

$$
\begin{split}
\frac{ \partial u }{ \partial r } &= \frac{ 1 }{ r } \frac{ \partial v }{ \partial \theta } \\
\frac{ \partial u }{ \partial \theta } &= -r \frac{ \partial v }{ \partial r } 
\end{split}
$$


Derivatives of $w$ i.e. $f(z)$ in polar coordinates,
$$
\begin{split}
\frac{ dw }{ dz } &= (\cos\theta - i\sin\theta) \frac{ \partial w }{ \partial r } \\
\frac{ dw }{ dz } &= - \frac{ i }{ r } (\cos\theta - i\sin\theta) \frac{ \partial w }{ \partial \theta } 
\end{split}
$$

Where,
$$
\begin{split}
\frac{ \partial w }{ \partial r } &= \frac{ \partial u }{ \partial r } + i\frac{ \partial v }{ \partial r } \\
\frac{ \partial w }{ \partial \theta } &= \frac{ \partial u }{ \partial \theta } + i\frac{ \partial v }{ \partial \theta } 
\end{split}
$$






