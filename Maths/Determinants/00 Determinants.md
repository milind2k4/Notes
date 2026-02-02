Links: [[00 Matrix]], [[01 Expansion]]
___
# Determinants
Determinant is arrangement of numbers in square form between two vertical lines. The horizontal are called **Rows** the vertical are called **Columns**

For a determinant, number of rows is the same as number of columns. 

If a determinant has n rows and n columns then its order is given as $n$ or $n \times n$.  The total number of elements will be given as $n^{2}$. 

Determinant corresponds to a value, i.e. determinant is nothing but a value. 

Element in ith-row and jth-column is written as $a_{ij}$. (Row-Column) (opposite of alphabetical order)

Elements $a_{ij}$ and $a_{ji}$ are conjugates of each other. $a_{ii}$ is conjugate of itself. Conjugate elements are symmetric about diagonal. 

Elements $a_{ii}$ are called diagonal elements. $a_{ii}$. And their collection is called **Diagonal.** Thus here, diagonal is not defined in the geometric sense. 

[[01 Expansion]]
[[02 Properties]]
[[03 Transformations]]
[[04 Some Determinants]]
[[05 Solving Linear Equations]]

### Denoting Determinant in Compact Form
$$D = 
\begin{vmatrix}
a_{1} & a_{2} & a_{3} \\
b_{1} & b_{2} & b_{3} \\
c_{1} & c_{2} & c_{3} 
\end{vmatrix}
$$
This is written as,
$$D = 
\begin{vmatrix}
C_{1} & C_{2} & C_{3} 
\end{vmatrix} = 
\begin{vmatrix}
R_{1} \\
R_{2} \\
R_{3}
\end{vmatrix}$$
where, 
$$C_{2} = \begin{matrix}
a_{1} \\
b_{1} \\
c_{1}
\end{matrix}
$$
And, 
$$R_{1} = \begin{matrix}
a_{1} & a_{2} & a_{3}
\end{matrix}$$

For n x n determinant,
$$D = 
\begin{vmatrix}
a_{11} & a_{12} & a_{13} & \dots & a_{1n} \\
a_{21} & a_{22} & a_{23} & \dots & a_{2n} \\
a_{31} & a_{32} & a_{33} & \dots & a_{3n} \\
\vdots  \\
a_{n1} & a_{n2} & a_{n3} & \dots & a_{nn} \\
\end{vmatrix} = |a_{ij}|_{n \times n}
$$
This can be written as,
$$D = 
\begin{vmatrix}
C_{1} & C_{2} & C_{3} & \dots & C_{n}  \\
\end{vmatrix}$$
$$D = 
\begin{vmatrix}
R_{1} \\
R_{2} \\
R_{3} \\
\vdots \\
R_{n}
\end{vmatrix}
$$


### Summation of Determinants
$$\Delta(r) = 
\begin{vmatrix}
f(r) & g(r) & h(r) \\
a & b & c \\
d & e & f
\end{vmatrix}
$$
Then,
$$\sum_{r=1}^{n}\Delta(r) = 
\begin{vmatrix}
\sum f(r) & \sum g(r) & \sum h(r) \\
a & b & c \\
d & e & f
\end{vmatrix}
$$
To apply $\sum$ on determinant,
1. If summation variable (say r) is present only in one row or column, then we can put $\sum$ on that row or column directly. 
2. If it is present in more than one row or column, then first evaluate the determinant and then apply $\sum$. 

This same logic applies to integration. 

Example,
![[Pasted image 20230622081642.png]]

### Product of Determinants 
We can multiply any two determinants, of any order as in the end they are just numbers. 

Let,
$$\Delta_{1} = 
\begin{vmatrix}
a_{1} & a_{2} & a_{3} \\
b_{1} & b_{2} & b_{3} \\
c_{1} & c_{2} & c_{3}
\end{vmatrix}
$$
$$\Delta_{2} =
\begin{vmatrix}
x_{1} & x_{2} & x_{3} \\
y_{1} & y_{2} & y_{3} \\
z_{1} & z_{2} & z_{3}
\end{vmatrix}
$$

We can multiply
- Row $\times$ Column
- Row $\times$ Row 
- Column $\times$ Row
- Column $\times$ Column

I.e. multiply corresponding elements from all elements and write them in order,

Multiplying Row by Row,
$$\Delta_{1}\Delta_{2} = 
\begin{vmatrix}
\sum a_{1}x_{1} & \sum b_{1}x_{1} & \sum c_{1}x_{1} \\
\sum a_{1}y_{1} & \sum b_{1}y_{1} & \sum c_{1}y_{1} \\
\sum a_{1}z_{1} & \sum b_{1}z_{1} & \sum c_{1}z_{1}
\end{vmatrix}
$$
Since transposing has no effect on the value of determinant, we can exchange the elements $\sum a_{1}y_{1}$ and $\sum b_{1}x_{1}$. 

Similarly, multiplying Column by Row,
![[Pasted image 20230623080850.png]]

Let, any two generic determiant be,
$$\Delta_{1} = |a_{ij}|_{n \times n}$$
$$\Delta_{2} = |b_{ij}|_{n \times n}$$

Multiplying them,
$$\Delta_{1}\Delta_{2} = |c_{ij}|_{n\times n}$$
If we multiply Row by Row,
$$c_{ij} = \sum_{r = 1}^{n} a_{jr} . b_{ir}$$

We can also break a determinant into product of two, the fixed value row wise will make the row of the first one and the fixed value of column wise will make the column of the second,
![[Pasted image 20230623082611.png]]

Another example,
![[Pasted image 20230623085121.png]]

We can also write $\cos(a-a)$ if 1 if there in the question,
![[Pasted image 20230623090649.png]]

### Differentiation of Determinants
[[00 Differentiation]]

To differentiate a determinant, we can differentiate it either row wise or column wise.  Also if we differentiate row wise, then do it one row at a time. I.e. differentiate row 1 and write remaining as same, then differentiate row 2 and remaining as it is and so on. 

Finally we add all the determinants.

$$\Delta(x) = 
\begin{vmatrix}
f_{1} & f_{2} & f_{3} \\
g_{1} & g_{2} & g_{3} \\
h_{1} & h_{2} & h_{3}
\end{vmatrix}
$$
$$\Delta'(x) = 
\begin{vmatrix}
f'_{1} & f'_{2} & f'_{3} \\
g_{1} & g_{2} & g_{3} \\
h_{1} & h_{2} & h_{3}
\end{vmatrix} +
\begin{vmatrix}
f_{1} & f_{2} & f_{3} \\
g'_{1} & g'_{2} & g'_{3} \\
h_{1} & h_{2} & h_{3}
\end{vmatrix} +
\begin{vmatrix}
f_{1} & f_{2} & f_{3} \\
g_{1} & g_{2} & g_{3} \\
h'_{1} & h'_{2} & h'_{3}
\end{vmatrix}
$$
$f,g,h$ are functions of x.

## Examples
![[Pasted image 20230621170318.png]]

![[Pasted image 20230622082416.png]]

![[Pasted image 20230622082701.png]]


In "independent of" type questions, open the determinat,
![[Pasted image 20230623090334.png]]

![[Pasted image 20230623091451.png]]