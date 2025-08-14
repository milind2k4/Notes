Links: [[00 Matrix]], [[03 Adjoint]]
___
# Inverse Matrix

We know that, for a square matrix,
$$A \text{ adj } A = |A|I_{n}$$
Thus, if $|A| \neq 0$,
$$A\left( \frac{ \text{adj }A }{ |A| } \right) = I$$

Therefore, $\displaystyle \frac{ \text{adj }A }{ |A| }$ is the inverse of A if A is Non-Singular.
$$A^{-1} = \frac{ \text{adj }A }{ |A| }$$

Thus here A must be non singular for it to have an inverse. 
[[00 Matrix#Singular and Non-Singular]]

Thus for inverse to exist, $|A| \neq 0$ is  the only required condition. 

### Properties of Inverse of Matrix
Inverse of Inverse,
$$(A^{-1})^{-1} = A$$

Adjoint can be written as,
$$A^{-1} = \frac{ \text{adj }A }{ |A| }$$
$$\text{adj }A = |A|A^{-1}$$

Determinant of Inverse,
$$
\begin{split}
A.A^{-1} &= I \\
|A|.|A^{-1}| &= 1 \\
|A^{-1}| &= \frac{ 1 }{ |A| } \\
&= (|A|)^{-1} 
\end{split}
$$
(the last -1 is for reciprocal)

Exponent,
$$A^{-2} = (A^{-1})^{2}$$
$$A^{-3} = (A^{-1})^{3}$$
and so on.


The result was derived using $|A| \neq 0$, however, this result is always valid. 
If A is null matrix, then $\text{adj }A$ is also null matrix. 
If A is not null matrix but $|A|=0$, then using [[01.5 Properties of MM and Some PTR#Product Zero]] we get, $|\text{adj }A| = 0 = |A|$. 

This result is also parallel to the [[01 Expansion#Some results|one in determinant,]] 
$$\Delta_{C} = \Delta^{n-1}$$

Multiplication by scalar,
$$
\begin{split}
(kA)(kA)^{-1} &= 1 \\
k. A(kA)^{-1} &= 1 \\
\\
\text{Premultiply by } A^{-1}, \\
k(kA)^{-1} &= A^{-1} \\
(kA^{-1}) &= \frac{ A^{-1} }{ k } \\
&= A^{-1} k^{-1}
\end{split}
$$

Reversal law,
$$(AB)^{-1} = B^{-1}A^{-1}$$
$$(ABCD)^{-1} = D^{-1}C^{-1}B^{-1}A^{-1}$$

Exponent,
$$(A^{k})^{-1} = (A^{-1})^{k}$$

Transpose,
$$(A^{-1})' = (A')^{-1}$$
If A is symmetric, then $A^{-1}$ will also be symmetric. 

Inverse of Adjoint,
$$(\text{adj }A)^{-1} = \text{adj }(A^{-1})$$

Inverse of Diagonal matrix,
$$A^{-1} = diag\left( \frac{ 1 }{ a_{11} }, \frac{ 1 }{ a_{22} }, \frac{ 1 }{ a_{33} } \dots \right)$$

## Examples
![[Pasted image 20230703082545.png]]

