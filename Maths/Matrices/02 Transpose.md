Links: [[00 Matrix]], [[02 Properties]]
___
# Transpose
$$A = \begin{bmatrix}
a_{1} & a_{2} & a_{3}  \\
b_{1} & b_{2} & b_{3} 
\end{bmatrix}$$

Transpose of A is obtained by interchanging rows and columns. 
$$A^{T} = A' = \begin{bmatrix}
a_{1} & b_{1}  \\
a_{2} & b_{2}  \\
a_{3} & b_{3} 
\end{bmatrix}$$

If the order of A is $m \times n$ then the order of $A'$ will be $n \times m$. 

In taking transpose, the conjugate elements (in case of square matrix) interchange position.

### Properties of Transpose
Transpose of Transpose,
$$(A')' = A$$

Scalar multiplication,
$$(\lambda A)' =\lambda(A)'$$

Addition,
$$(A + B)' = A^{T} \pm B^{T}$$
$$(A_{1}+A_{2} + A_{3} + \dots)' = A_{1}' + A_{2}' + A_{3}' + \dots$$

Multiplication,
$$(AB)' = B'A'$$
$$(A_{1}A_{2}A_{3}\dots A_{n})' = A_{n}'A_{n-1}'A_{n-2}'\dots A_{1}'$$

Exponent,
$$(A^{n})' = (A')^{n}$$

Determinant,
$$|A'| = |A|$$

### Symmetric and Skew-Symmetrix Matrix
[[01 Expansion#Symmetric and Skew Symmetric Determinant]]

If A is a square matrix such that,
- $A' = A$ then the matrix is called Symmetric.
	i.e. $a_{ij} = a_{ji}$
	$\\$

- $A' = -A$ then the matrix is called Skew-Symmetrix.
	i.e. $a_{ij} = -a_{ji}$ this means $a_{ii} = 0$
	Max. number of unique elements will be 

Determinant value of odd ordered skew-symmetric matrix will be zero. 

If A is a square matrix, then,
1. $(A+A')$ will be a symmetric matrix.
1. $(A-A')$ will be a skew-symmetric matrix.

Thus every matrix can be written as the sum of a symmetric and a skew-symmetric matrix uniquely,
$$A = \left( \frac{ A+A' }{ 2 } \right) + \left( \frac{ A-A' }{ 2 } \right)$$

This is in parallel to [[00.3 Even & Odd]] in functions. 

If A and B are symmetric matrices of same order then,
1. $A'$ will also be symmetric
2. $A+B$ will be symmetric
3. $A^{k}$ will be symmetric 
4. If A and B commutes, then AB will also be symmetric.
   $C = AB$ then $C' = B'A' = BA = AB = C$
4. $PAP'$ will be symmetric where P is any matrix of same order. 
   $D = PAP'$ then $D' = (P')'A'P' = PAP'$ (the reverse law)
5. $AB + BA$ will be symmetric
6. $AB - BA$ will be skew-symmetric


If A and B are skew-symmetric matrices of same order then,
1. $A + B$ will be skew-symmetric
2. $PAP'$ will be symmetric
   $D = PAP'$ then $D' = PA'P' = -PAP'$
3. $A^{2n}$ will be symmetric
4. $A^{2n+1}$ will be skew-symmetric

### Orthogonal Matrix (OM)
If A is square matrix of order n then it is Orthogonal if 
$$AA' = I_{n} = A'A$$
$I$ is an Orthogonal matrix

If A and B are orthogonal, then 
$A'$ will also be orthogonal, and,
$A'$ is the inverse of A

Exponent, $A^{k}$ will be orthogonal.
> Let $P = A^{k}$,
> $$
> \begin{split}
> PP' &= A^{k}(A')^{k} \\
> &= (A.A.A\dots)(A'.A'.A'\dots) \\
> &= I.I.I \dots \\
> &= I 
> \end{split}
> $$

Multiplication, $AB$ will be orthogonal 
> Let, $C = AB$ 
> $$
> \begin{split}
> CC' &= AB(AB)' \\
> &= ABB'A' \\
> &= AIA' \\
> &= AA'\\
> &= I
> \end{split}
> $$

The value of determinant, $|A| = \pm1$
> $$
> \begin{split}
> AA' &= I \\
> |A||A'| &= 1\\
> |A|^{2} &= 1\\
> |A| &= \pm 1
> \end{split}
> $$


#### 2 x 2 OM
If A is 2 x 2 OM, then 
$$\begin{bmatrix}
a & b \\
c & d
\end{bmatrix}
\begin{bmatrix}
a & c \\
b & d
\end{bmatrix} = 
\begin{bmatrix}
a^{2}+b^{2} & ac+bd \\
ac+bd & c^{2}+d^{2}
\end{bmatrix} = 
\begin{bmatrix}
1 & 0 \\
0 & 1
\end{bmatrix}
$$
Thus,
$$a^{2} + b^{2} = 1$$
$$c^{2} + d^{2} = 1$$
$$ac + bd = 0$$

Let $\vec{v}_{1} = a \hat{i} + b \hat{j}$ and $\vec{v}_{2} = c \hat{i} + d \hat{j}$, then
$$a^{2} + b^{2} = 1 \implies |\vec{v}_{1}| = 1$$
$$c^{2} + d^{2} = 1 \implies |\vec{v}_{2}| = 1$$
$$ac + bd = 0 = \vec{v}_{1}. \vec{v}_{2} = 0 \implies \vec{v}_{1} \perp \vec{v}_{2}$$
That is, $\vec{v}_{1}, \vec{v}_{2}$ are mutually perpendicular unit vectors and we can treat rows or columns of an OM as components of mutually perpendicular 2d vectors. 

#### 3 x 3 OM
If A is a 3 x 3 OM,
$$
\begin{bmatrix}
a_{1} & a_{2} & a_{3} \\
b_{1} & b_{2} & b_{3} \\
c_{1} & c_{2} & c_{3}
\end{bmatrix} 
\begin{bmatrix}
a_{1} & b_{1} & c_{1} \\
a_{2} & b_{2} & c_{2} \\
a_{3} & b_{3} & c_{3}
\end{bmatrix}
$$
$$
\begin{bmatrix}
\sum a_{1}^{2} & \sum a_{1}a_{2} & \sum a_{1}a_{3} \\
\sum a_{2}a_{3} & \sum a_{2}^{2} & \sum a_{2}a_{3} \\
\sum a_{1}a_{3} & \sum a_{2}a_{3} & \sum a_{3}^{2}
\end{bmatrix} = 
\begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{bmatrix}
$$

Thus,
$$a_{1}^{2} + b_{1}^{2} + c_{1}^{2} = 1$$
$$a_{2}^{2} + b_{2}^{2} + c_{2}^{2} = 1$$
$$a_{3}^{2} + b_{3}^{2} + c_{3}^{2} = 1$$
$$\sum a_{1}a_{2} = 0$$
$$\sum a_{2}a_{3} = 0$$
$$\sum a_{3}a_{1} = 0$$

If we take 3 vectors, 
$$\vec{v}_{1} = a_{1} \hat{i} + b_{1} \hat{j} + c_{1} \hat{k}$$
$$\vec{v}_{2} = a_{2} \hat{i} + b_{2} \hat{j} + c_{2} \hat{k}$$
$$\vec{v}_{3} = a_{3} \hat{i} + b_{3} \hat{j} + c_{3} \hat{k}$$

Then,
$$|\vec{v}_{1}| = |\vec{v}_{2}| = |\vec{v}_{3}| = 1$$
And,
$$\vec{v}_{1} . \vec{v}_{2} = 0$$
$$\vec{v}_{2} . \vec{v}_{3} = 0$$
$$\vec{v}_{3} . \vec{v}_{1} = 0$$

So if A is OM of order 3, then the elements of rows or columns can be treated as components of 3 mutually perpendicular vectors. 

#### Examples
![[Pasted image 20230701093841.png]]

![[Pasted image 20230701094236.png]]

![[Pasted image 20230701095219.png]]