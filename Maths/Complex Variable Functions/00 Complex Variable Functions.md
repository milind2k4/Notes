Links: [[00 Complex Numbers]]
___
# Complex Variable Functions

If corresponding to each value of a complex variable $z$, there in a given region $\mathbb{R}$, there corresponds one ore more values of another complex variable, $w = u + iv$, then $w$ is called a function of complex variable $z$. 

$$
\begin{split}
w &= f(z) \\
&= u + iv \\
&= u(x,y) + iv(x,y)
\end{split}
$$

#### Single and Multi Valued Function
If to each value of $z$, there corresponds only one value of $w$, then $w$ is a **Single valued function of $z$.** 

If to each value of $z$, there corresponds more than one value of $w$, then $w$ is a **Multi valued function of $z$.** 

### Limit, Continuity and Differentiability
Limit,
$$
\begin{split}
\lim_{ z \to z_{o} } f(z) &= l \\
\lim_{ x,y \to 0,0 } [u(x,y) + iv(x,y)] &= l
\end{split}
$$

Continuity,
$$\lim_{ z \to z_{o} } f(z) = f(z_{o})$$

Differentiability,
$$
\begin{split}
\frac{ dw }{ dz } &= f'(z) \\
&= \lim_{ \delta z \to 0 } \frac{ f(z + \delta z) - f(z) }{ \delta z } 
\end{split}
$$

Provided the limit exists and is independent of the manner in which $\delta z \to 0$. 