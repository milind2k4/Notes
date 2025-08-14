Links: [[00 Matrix]], [[04 Inverse]]
___
# Adjoint of a Matrix
[[01 Expansion#Cofactor]]
[[01 Expansion#Some results]]

Adjoint of a matrix is the transpose of the matrix formed by the cofactor of every element. 

Let A is an n square matrix, then we define its adjoint matrix ($\text{adj } A$) as a square matrix obtained from A by replacing all elements by their corresponding cofactors and then taking transpose. 

If $A = [a_{ij}]_{n\times n}$ then,
$$\text{adj }A = [C_{ij}]_{n \times n}'$$

Which can be written as,
$$\text{adj }A = C'$$

For 2 x 2, if
$$A = \begin{bmatrix}
a_{11} & a_{12} \\
a_{21} & a_{22}
\end{bmatrix}$$

Then,
$$\text{adj }A = \begin{bmatrix}
a_{22} & -a_{12} \\
-a_{21} & a_{11}
\end{bmatrix}$$

For a general matrix,
$$A = \begin{bmatrix}
a_{11} & a_{12} & a_{13} & \dots & a_{1n} \\
a_{21} & a_{22} & a_{23} & \dots & a_{2n} \\
a_{31} & a_{32} & a_{33} & \dots & a_{3n} \\
. \\
. \\
. \\
a_{n1} & a_{n2} & a_{n3} & \dots & a_{nn}
\end{bmatrix}$$

$$\text{adj }A = \begin{bmatrix}
C_{11} & C_{21} & C_{31} & \dots & C_{n 1} \\
C_{12} & C_{22} & C_{32} & \dots & C_{n 2} \\
C_{13} & C_{23} & C_{33} & \dots & C_{n 3} \\
. \\
. \\
. \\
C_{1n} & C_{2n} & C_{3n} & \dots & C_{nn}
\end{bmatrix}$$

When we multiply them, the corresp0nding elements will be multiplied by their corresponding elements which will give the value of determinant. 
The value of multiplication will be determinant for diagonal and zero for all other elements.

$$A.\text{adj }A = \begin{bmatrix}
|A| & 0 & 0 & \dots & 0 \\
0  & |A| & 0 & \dots & 0 \\
0 & 0 & |A| & \dots & 0 \\
. \\
. \\
. \\
0 & 0 & 0 & \dots & |A| 
\end{bmatrix} = |A|I_{n}$$

### Properties of Adjoint 
n is the order of the square matrix A.

Determinant of Adjoint,
$$
\begin{split}
A.\text{adj }A &= |A|I \\
\det A .\det \text{adj }A &= \det |A|I \\
\\
\text{Now if,} |A| \neq 0, \\
|\text{adj }A| &= |A|^{n-1} \\
\end{split} 
$$

Using this property we can also write,
$$
\begin{split}
|\text{adj }(\text{adj }A)| &= (| \text{adj }A |)^{n-1} \\
&= (|A|^{n-1})^{n-1} \\
&= |A|^{(n-1)^{2}}
\end{split}
$$
so on for more number of adj,
$$|\text{adj }(\text{adj }(\text{adj }A))| = |A|^{(n-1)^{3}}$$


Reversal law,
$$\text{adj }(AB) = (\text{adj }B)(\text{adj }A)$$
$$\text{adj }(ABC) = \text{adj }C. \text{adj }B. \text{adj }A$$

Exponent,
$$\text{adj }A^{k} = (\text{adj }A)^{k}$$

Scalar Multiplication,
$$
\begin{split}
\text{adj }(kA) &= |kA|(kA^{-1}) \\
&= k^{n}|A| \frac{ A^{-1} }{ k } \\
&= k^{n-1}|A|A^{-1} \\
\text{adj }(kA) &= k^{n-1}\text{adj }A 
\end{split}
$$

Adjoint of Adjoint,
$$\text{adj }(\text{adj }(A)) = |A|^{n-2}I_{n}$$
$$
\begin{split}
\text{adj }(\text{adj }A) &= |\text{adj }A|(\text{adj }A)^{-1} \\
&= |A|^{n-1}(|A|.A^{-1})^{-1} \\
&= |A|^{n-1} \frac{ (A^{-1})^{-1} }{ |A| } \\
&= |A|^{n-2}A
\end{split}
$$
For more number of adjoint,
$$
\begin{split}
\text{adj }(\text{adj }(\text{adj }A)) &= |\text{adj }A|^{n-2}\text{adj }A \\
&= (|A|^{n-1})^{n-2}.\text{adj }A \\
&= |A|^{n^{2}-3n+2}.\text{adj }A
\end{split}
$$

Transpose of Adjoint,
$$(\text{adj }A)' = \text{adj }A'$$
If A is symmetric, $(\text{adj }A)' = \text{adj }A' = \text{adj }A$ (i.e. the adjoint will also be symmetric)
