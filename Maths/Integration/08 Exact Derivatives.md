Links: [[02 Exact Differentials and Trig Subs.]]
___
# Exact Derivatives

$$\int (g \cdot f' + g' \cdot f) \, dx = \int (f \cdot g)' \, dx = f \cdot g + c$$

Alternatively, we can use integration by parts on one of them,
$$
\begin{split}
\int f'.g \, dx + \int g'.f \, dx &= \int f'.g \, dx + g.f - \int g.f' \, dx \\
&= f.g + c
\end{split}
$$

We can think of this when individually the terms in the sum are not integrable easily. 

 We should also try to search for function and its derivative in the question. 

As integral of the first term i.e. $f'g$ is not required, hence it may be non integrable. 

1st and 2nd expressions may be related in the form of $f$ and $f''$ i.e. they may be two derivatives apart.

##### Special cases
If one of the functions is either x, $e^{ x }$ ( #important ) or $e^{ g }$,
$$
\begin{split}
\int (x \cdot f'(x) + f(x)) \, dx &= \int (x \cdot f(x))' \, dx = x \cdot f(x) + c \\ 
\\
\int e^{ x } \cdot (f + f') \, dx &= \int (e^{ x } \cdot f)' \, dx = e^{ x } \cdot f(x) + c \\
\\
\int e^{ g }(g'.f + f') \, dx &= e^{ g }.f + c
\end{split}
$$

### Examples
![[Pasted image 20231001170246.png]]

![[Pasted image 20231001170849.png]]