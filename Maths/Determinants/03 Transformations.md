Links: [[01 Expansion]]
___
# Row and Column Transformations

If a constant multiple of any row is added to any other row then the determinant remains the same. (same with subtraction and columns)

$$\begin{vmatrix}
a_{11} & a_{12} & a_{13}  \\
a_{21} & a_{22} & a_{23}  \\
a_{31} & a_{32} & a_{33}
\end{vmatrix} = 
\begin{vmatrix}
a_{11} & a_{12} & a_{13} + 2a_{12} \\
a_{21} & a_{22} & a_{23} + 2a_{22} \\
a_{31} & a_{32} & a_{33} + 2a_{32}
\end{vmatrix}$$

Denoted by,
$$C_{3} \to C_{3} + 2C_{2}$$
The coefficient of the row being changed needs to be 1. 
Thus we cannot write,
$$C_{2} \centernot\to 2C_{2} - C_{1}$$

But we can add multiple rows or columns,
$$R_{3} \to R_{3} - R_{2} - 2R_{1}$$

Transformations are helpful in evaluating determinants,
1. Try to create as many 0s as possible in a row or column and evaluate wrt that row or column. 
2. Try to sum all row wise or column wise to see whether we are getting 0s or same elements or not. 
3. Use transformations to see whether we can get a factor common to all elements or not. 
4. We can think ogf multiplying some number, (say a, b, c) row wise. Especially when ab, bc, ca type terms are involved. 
   
	Some times we will take out those numbers column wise and sometimes a fixed number will come out to be common from a row or column.  

5. If it is taking too long to find which property to apply, start evaluating it normally. 

### Some Transformations
#### If all elements are identical in a Row

$$ \det A =
\begin{vmatrix}
1 & a & b \\
1 & c & d \\
1 & f & e
\end{vmatrix} 
\xrightarrow[R_{3} \to R_{3} - R_{1}]{R_{2} \to R_{2} - R_{1}}
\begin{vmatrix}
1 & a & b \\
0 & c-a & d-b \\
0 & f-a & e-b
\end{vmatrix} 
$$


#### If sum of all elements are identical


$$
\begin{vmatrix}
a & b & c \\
b & c & a \\
c & a & b
\end{vmatrix} 
\xrightarrow{C_{1} \to C_{1} + C_{2} + C_{3}}
\begin{vmatrix}
a+b+c & b & c \\
a+b+c & c & a \\
a+b+c & a & b
\end{vmatrix} 
$$
Then,

$$
\begin{vmatrix}
a+b+c & b & c \\
a+b+c & c & a \\
a+b+c & a & b
\end{vmatrix} 
\longrightarrow 
(a+b+c) 
\begin{vmatrix}
1 & b & c \\
1 & c & a \\
1 & a & b
\end{vmatrix}
$$

Again,
$$
\begin{split}
(a+b+c)\begin{vmatrix}
1 & b & c \\
1 & c & a \\
1 & a & b
\end{vmatrix} &\ce{ ->[R_{2} \to R_{2} - R_{1}][R_{3} \to R_{3} - R_{1}] }
(a+b+c)\begin{vmatrix}
1 & b & c \\
0 & c-b & a-c \\
0 & a-b & b-c
\end{vmatrix} \\ \\
&= (a+b+c)[(c-b)(b-c)-(a-c)(a-b)] \\
&= -(a+b+c)[c^{2} + b^{2} - 2bc + a^{2} - ab - ca + bc] \\
&= -(a+b+c)[a^{2} + b^{2} + c^{2} - ab - bc - ca] \\
&= -\left( \sum a \right)\left( \sum a^{2} + \sum ab \right) \\
&= -(a^{3} + b^{3} + c^{3} - 3abc)
\end{split}
$$
