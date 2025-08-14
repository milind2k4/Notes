Links: [[01 Expansion]]
___
# Properties 

$$\begin{vmatrix}
a_{11} & a_{12} & a_{13}  \\
a_{21} & a_{22} & a_{23}  \\
a_{31} & a_{32} & a_{33}
\end{vmatrix}$$


1. If all elements of a row or column are zero, then the value of determinant is zero. 
   $\\$

1. Value of determinant does not change if rows and columns are interchanged. This is referred to as $\ce{ R <-> C }$.
	$$\det A = \det A^{T}$$
	Due to this property, any property which is applicable to rows will be applicable for columns. 
   $\\$

3. A determinant can be broken into two w.r.t a row or column, but the remaining rows or columns must be the same. We can break in any way we want, but ultimately the sum should be element we are breaking. 
   
   Thus, if in a determinant one row or column is written as the sum of 2 or more elements, we can write, 
	$$\det A_{12(3+4)} = \det A_{123} + \det A_{124}$$
	
	We cannot break simultaneously wrt to two rows,
	$$\det A_{1(2+3)(4+5)} = \det A_{1(2+3)4} + \det A_{1(2+3)5}$$
	Now here, these two can be further broken. 
	
	Using this property, two determinants can be added w.r.t any row or column provided the remaining row or column remain the same in both the determinants. 
	$\\$

1. If all elements of a row or column are multiplied by a number, then the value of determinant gets multiplied by that number. 
   
   From a row or column we can take a number common. 
	$$\det A_{123k} = k \det A_{123}$$
	$\\$
	
1. If any 2 rows or columns of a determinant are identical then the determinant is zero. If a row is multiple of another row, then also the value of determinant will be zero. 
   $\\$

3. If any two rows or columns are interchanged, the value of determinant becomes negative. 
	$$\det A_{123} = -\det A_{213}$$
	
	**Rolling Over:** 
	If a row is rolled over k rows then value of new determinant will be $(-1)^{k}$ times original value. 
	$$\det A_{12345} = (-1)^{3}\det A_{23415}$$
	Here since 1 moves 3 places, k is 3. 
	$$\det A_{23415} = -\det A_{23154}$$
	Here since 4 moves 2 places, k is 2.
	
	Rolling over is different from interchanging in the sense that when we roll over, we perform many interchanges.  
