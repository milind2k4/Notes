Links: [[00 Basic Mathematics]], [[00 Functions]]
___
# Domain of Functions
The set containing all the acceptable values of the independent variable is called Domain. 

Graphically it is the portion of x-axis covered by graph. 

Most of the domain questions will be converted into inequalities. 

Domain of the expression should be found in original form. As manipulating may change the domain. 

![[Pasted image 20230522075434.png]]

To solve questions of $^{n}C_{r}$, we have to solve by mostly observation and taking values,
![[Pasted image 20230522084055.png]]

We might also use graphs to solve for domain,

Solving using graphs,
![[Pasted image 20230523071358.png]]


### Domain of Various Expressions

$A$ needs to be defined itself in all the cases below.

| Expression                                   | Domain                                      |
| -------------------------------------------- | ------------------------------------------- |
| $$\frac{1}{A}$$                              | $$A\neq 0$$                                 | 
| $$\sqrt[2n]{ A }$$                           | $$A > 0$$                                   |
| $$\sqrt[2n+1]{ A }$$                         | $$R$$                                       |
| $$\log_{A}B$$                                | $$A> 0 \cap B>O \cap A \neq_{0}$$           |
| $$\sin ^{-1}x, \cos ^{-1}x$$                 | $$-1 \leq A \leq 1$$                        |
| $$\sec^{-1}x, \csc ^{-1}x$$                  | $$A\leq -1 \cup A \geq 1$$                  |
| Any polynomial, $a^{x}, e^{x}, \|x\|$        | $$R$$                                       |
| $$\tan ^{-1}x, \cot ^{-1}x, \sin x, \cos x$$ | $$R$$                                       |
| $$[x], \{ x \}, sng(x)$$                     | $$R$$                                       |
| $$\tan x, \sec x$$                           | $$R - (2n+1) \frac{ \pi }{ 2 }$$            |
| $$\cot x, \csc x$$                           | $$R - n\pi$$                                |
| $${}^{n}C_{r}$$                              | $$n \in N \cap r \in W \cap n \geq r$$      |
| $$\frac{ax+b}{cx+d}$$                        | $$R - \left\{  \frac{ -d }{ c }  \right\}$$ |

## Domain of Combination of 2 functions

Let $f(x)$ and $g(x)$ be two functions,

then the Domain of any of,
$$\begin{split}
f(x) &+ g(x) \\
f(x) &- g(x) \\
f(x)\ &\cdot\ g(x) \\
f(x) &\div g(x) \\
\end{split}$$

is $D_{f} \cap D_{g}$, i.e. the intersection of their domains. 
In case of division, $D_{f} \cap D_{g} \cap \{ x: g(x) \neq 0 \}$

The domain of $f(x) \pm g(x)$ cannot be greater than the domain of $f(x)$ or $g(x)$. This can help in reducing calculations. 

![[Pasted image 20230522075857.png]]

## Domain of Composite Function
Outside to inside

Take intersections of domains of functions from outside to inside.

e.g. Domain of,
$$e^{\sin ^{-1}x} \ce{ -> } x \in[-1,1]$$
as the domain of $e^{x}$ is $R$ and that of $\sin ^{-1}x$ is $[-1,1]$.

## Performing operations on Domain
If any expression belongs in a range, then we can treat the $\in$ as an $=$ and perform operations. 

E.g.,
$$
\begin{split}
\frac{1+x}{x} &\in (-\infty, -1] \cup [1, \infty) \\\\
1+\frac{1}{x} &\in (-\infty, -1] \cup [1, \infty) \\ \\
\frac{1}{x} &\in (-\infty, -2] \cup [0, \infty) \\ \\
x &\in \left( 0, -\frac{1}{2} \right] \cup \left[ \infty, 0 \right) \\ \\
x &\in \left[-\frac{1}{2}, 0 \right) \cup \left( 0, \infty \right) \\ \\
\end{split}
$$
