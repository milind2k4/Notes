Links: [[00 Determinants]]
___
# Expansion

### 1 x 1
$$A = [a_{11}]$$

$$\det A = a_{11}$$

### 2 x 2
$$A = \begin{bmatrix}
a_{11} & a_{12}  \\
a_{21} & a_{22} 
\end{bmatrix}$$

$$\det A = \begin{vmatrix}
a_{11} & a_{12}  \\
a_{21} & a_{22}
\end{vmatrix}
= a_{11}a_{22} - a_{21}a_{12}$$

### 3 x 3
$$A = \begin{bmatrix}
a_{1} & a_{2} & a_{3}  \\
b_{1} & b_{2} & b_{3}  \\
c_{1} & c_{2} & c_{3} 
\end{bmatrix}$$

$$\det A = \text{element times it's cofactor }$$

About first row,
$$\det A = a_{1}C_{a_{1}} + a_{2}C_{a_{2}} + a_{3}C_{a_{3}}$$

$$\det A = a_{1} \begin{vmatrix}
b_{2} & b_{3}  \\
c_{2} & c_{3}
\end{vmatrix} 
- a_{2} \begin{vmatrix}
b_{1} & b_{3}  \\
c_{1} & c_{3} 
\end{vmatrix}
+ a_{3} \begin{vmatrix}
b_{1} & b_{2}  \\
c_{1} & c_{2}
\end{vmatrix}$$

#### Minor
Minor of $a_{ij}$ is denoted by $M_{ij}$ and it is a subdeterminant where we remove the corresponding column and row. Remove the $i^{ th }$ row and $j^{ th }$ column. 
It is a determinant of order $n-1$. 

$$M_{a_{1}} = \begin{vmatrix}
b_{2} & b_{3}  \\
c_{2} & c_{3}
\end{vmatrix}$$

#### Cofactor
Denoted as $C_{ij}$ and is defined as,
$$C_{ij} = (-1)^{i+j} M_{ij}$$

Thus, sign of cofactor will be,
$$
\begin{vmatrix}
+ & - & + \\
- & + & - \\
+ & - & +
\end{vmatrix}
$$

#### Some results
The value of determinant is sum of products of elements of any row or column with their corresponding Cofactors. 

If determinant is,
$$\Delta = |a_{ij}|_{n\times n}$$
Then its value will be, evaluating wrt mth row,
$$\Delta = \sum_{i=1}^{n} a_{mi}C_{mi}$$
Then its value will be, evaluating wrt mth column,
$$\Delta = \sum_{i=1}^{n} a_{im}C_{im}$$


The sum of products of elements of any row with the corresponding cofactors of any other row will always be zero. However, doing this with elements of a row and cofactors of a column will neither give zero nor the value of determinant. 

If $\Delta$ is any determinant $\Delta_{C}$ is obtained by replacing all elements by their corresponding cofactors, then,
$$\Delta_{C}\Delta = \Delta^{n}$$
$$\Delta_{C} = (\Delta)^{n-1}$$

#### Symmetric and Skew Symmetric Determinant
$$\Delta = |a_{ij}|_{n\times n}$$

 A determinant is **Symmetric** if $a_{ij}=a_{ji},\ \forall\ i,j$. I.e. it will be symmetric about diagonal. 

A determinant is **Skew Symmetric** if $a_{ij} = -a_{ji},\ \forall\ i,j$. The diagonal elements will all be zero. 

*The value of a skew symmetric determinant of odd order will be zero.*
This can be found by taking -1 common from all rows and interchanging rows and columns. 


### Sarrus' Rule of Determinant Expansion

Multiply each element and write the 'correct' directional diagonals with a +ve sign and write the 'incorrect' directional diagonals with a -ve sign. 

This method is especially useful for expanding determinants with variables. 

![[Pasted image 20230621093659.png]]

Write the determinant like this,
$$
\begin{vmatrix}
a & b & c \\
p & q & r \\
x & y & z
\end{vmatrix} 
\begin{matrix}
\ a & b \\
\ p & q \\
\ x & y
\end{matrix}
$$
and write the elements along correct diagonal with +ve and along the incorrect diagonal with -ve. 
Thus giving,
$$apz + brx + cpy - cqx - ary - bpz$$

And if we interchange geometric diagonals, then the determinant becomes -ve. 