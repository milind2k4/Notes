Links: [[00 Basic Mathematics]]
___
# Some Formula
#### Cyclic Formula
$$\begin{split}
x^{2} + y^{2} + z^{2} - xy - yz - zx &=  \frac{1}{2}[(x-y)^{2} + (y-z)^{2} + (z-x)^{2}] \\
x^{2} + y^{2} + z^{2} - xy - yz - zx &\geq 0 \\
x^{2} + y^{2} + z^{2} &\geq xy + yz + zx
\end{split}
$$
For equality to hold, $x=y=z$.
$$
\begin{split}
x^{3} + y^{3} + z^{3} - 3xyz &=  (x+y+z)(x^{2} + y^{2} + z^{2} - xy - yz - zx) \\
&=  (x+y+z)\cdot \frac{1}{2} [(x-y)^{2} + (y-z)^{2} + (z-x)^{2}]
\end{split}
$$

$$ax + by + xy = (x+b)(y+a) - ab$$

#### Difference of Cubes and its derivatives
$$
\begin{split}
x^{3}-y^{3} &=  (x-y)(x^{2}+xy+y^{2}) \\
x-y &=  (x^{1/3}-y^{1/3}) (x^{2/3}+x^{1/3}y^{1/3}+y^{2/3}) \\
x^{1/3}-y^{1/3} &= \frac{x-y}{x^{2/3}+y^{2/3}+x^{1/3}y^{1/3}} 
\end{split}
$$

#### Biquadratic Expressions
$$x^{4}+4y^{4} = (x^{2}+2xy+2y^{2})(x^{2}-2xy+2y^{2})$$
this can be obtained by adding and subtracting $4x^{2}y^{2}$
If $y=1$, 
$$x^{4} + 4 = (x^{2}+2x+2)(x^{2}-2x+2)$$

$\\$

$$x^{4} + y^{4} + x^{2}y^{2} = (x^{2}-xy+y^{2})(x^{2}+xy+y^{2})$$
if $y=1$
$$x^{4}+x^{2}+1 = (x^{2}-x+1)(x^{2}+x+1)$$

#### Factorization of Difference
If $n \in N-\{ 1 \}$,
$$x^{n}-y^{n} = (x-y)(x^{n-1} + x^{n-2}y + x^{n-3}y^{2} + \dots y^{n-1})$$

If $n$ is odd positive integer > 1,
$$x^{n}+y^{n} = (x+y)(x^{n-1} - x^{n-2}y + x^{n-3}y^{2} + \dots y^{n-1})$$


## Expansions
$$
\begin{split}
a^{x} &=  1 + \frac{ x\ln a }{ 1! } + \frac{ x^{2}\ln^{2}a }{ 2! } + \frac{ x^{3}\ln^{3}a }{ 3! } + \dots (a > 0)
\\ \\
e^{ x } &=  1 + \frac{ x }{ 1! } + \frac{ x^{2} }{ 2! } + \frac{ x^{3} }{ 3! }  +\dots 
\\ \\
\ln(1+x) &=  \frac{ x }{ 1 } - \frac{ x^{2} }{ 2 } + \frac{ x^{3} }{ 3 } - \frac{ x^{4} }{ 4 } + \dots (-1 < x \leq 1)
\\ \\
\sin x &=  \frac{ x^{1} }{ 1! } - \frac{ x^{3} }{ 3! } + \frac{ x^{5} }{ 5! } - \frac{ x^{7} }{ 7! } + \dots
\\ \\
\cos x &=  \frac{ x^{0} }{ 0! } - \frac{ x^{2} }{ 2! } + \frac{ x^{4} }{ 4! } - \frac{ x^{6} }{ 6! } + \dots
\\ \\
\tan x &=  x + \frac{ x^{3} }{ 3 } + \frac{ 2x^{5} }{ 15 } + \dots
\\ \\
\tan ^{-1}x &=  x - \frac{ x^{3} }{ 3 } + \frac{ x^{5} }{ 5 } - \frac{ x^{7} }{ 7 } + \dots
\\ \\
\sin ^{-1}x &=  x + \frac{ 1^{2} }{ 3! }x^{3} + \frac{ 1^{2}.3^{2} }{ 5! }x^{5} + \frac{ 1^{2}.3^{2}.5^{2} }{ 7! }x^{7} + \dots
\\ \\
(1+x)^{n} &=  1 + nx + \frac{ n(n-1) }{ 2! }x^{2} + \frac{ n(n-1)(n-2) }{ 3! }x^{3} + \dots
\\ \\
(1+x)^{n} &=  1 + nx, \ce{\ if\ } x \ll 1
\\ \\
(1+x)^{1/x} &=  e\left( \frac{ x^{0} }{ 1 } - \frac{ x }{ 2 } + \frac{ 11 }{ 24 }x^{2} - \dots \right)
\end{split}
$$