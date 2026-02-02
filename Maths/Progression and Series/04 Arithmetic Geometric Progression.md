Links: [[00 Sequence and Series]], [[01 Arithmetic Progression]], [[02 Geometric Progression]]
___
# Arithmetic Geometric Progression

$a_{1}, a_{2}, a_{3}, \dots a_{n}$ are in AP with CD = $d$
$g_{1}, g_{2}, g_{3}, \dots g_{n}$ are in GP with CR = $r$

Then, an AGP is a sequence formed by multiplying their consecutive terms, i.e.
$a_{1}g_{1}, a_{2}g_{2}, a_{3}g_{3} \dots a_{n}g_{n}$ is an AGP.

General term:
$$T_{n} = a_{n} \cdot g_{n}$$

### Sum

To find sum of AGP, we multiply both sides by CR of GP, then shift the series on RHS by one term and then subtract it from original. 

Let the AGP with n terms' sum be,
$$
\begin{split}
S = a.1 +\ (a+d)x& + (a+2d)x^{2}& + (a+3d)x^{3}& + \dots (a+(n-1)d)x^{n-1}& \\
xS = \hspace{2.52 cm} ax& + (a+d)x^{2}& + (a+2d)x^{3}& + \dots (a+(n-2)d)x^{n-1}& + (a+(n-1)d)x^{n}
\end{split}
$$
Subtracting them we get,
$$(1-x)S = a + dx + dx^{2} + \dots dx^{n-1} - (a-(n-1)d)x^{n}$$
This new series has n+1 terms.
Thus the GP (dx terms) has n-1 terms since the first and last are excluded. 

The sum will then be,
$$(1-x)S = a + xd\left( \frac{ 1-x^{n-1} }{ 1-x } \right) - (a-(n-1)d)x^{n}$$
$$S = \frac{ a }{ 1-x } + xd\left( \frac{ 1-x^{n-1} }{ (1-x)^{2} } \right) - (a-(n-1)d)x^{n}$$

Example,
![[Pasted image 20230615090654.png]]

We can also use this method to find the sum of some other series also, like AAGP,
![[Pasted image 20230615090755.png]]