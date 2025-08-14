Links: [[00 Determinants]], [[01 Expansion]]
___
# Solving Linear Equations
#important 

This is the determinant method, for matrix method, see [[06 Solution of Equations]].

### 2 Linear Equations in 2 variables

$$a_{1}x + b_{1}y = c_{1}$$
$$a_{2}x + b_{2}y = c_{2}$$
These two equations represent two straight lines in a 2d plane. 
The coordinates of their intersection is the solution of the system.

In a 2d plane. there can only be 3 possibilities,
1. **Exactly one point of intersection:** Unique solution
   $$\frac{ a_{1} }{ a_{2} } \neq \frac{ b_{1} }{ b_{2} }$$
   
2. **Parallel and distinct:** No solution and the equations are called *Inconsistent.*
   $$\frac{ a_{1} }{ a_{2} } = \frac{ b_{1} }{ b_{2} } \neq \frac{ c_{1} }{ c_{2} }$$
   
3. **Coincident Lines:** infinite solutions
   $$\frac{ a_{1} }{ a_{2} } = \frac{ b_{1} }{ b_{2} } = \frac{ c_{1} }{ c_{2} }$$
   To find the solutions, we put either of the variables as $\lambda$.
   $\\$ 

4. **Perpendicular Lines:** one solution
	$$a_{1} a_{2} + b_{1}b_{2} = 0$$

	As, for perpendicular lines, $m_{1} m_{2} = -1$ and here,
	$$m_{1} = \frac{ -a_{1} }{ b_{1} }$$
	$$m_{2} = \frac{ -a_{2} }{ b_{2} }$$
	[[00 Straight Line#Slope]]

\
Is there is unique solution, it can be found by,
$$\Delta = \begin{vmatrix}
a_{1} & b_{1}  \\
a_{2} & b_{2}
\end{vmatrix},\ 
\Delta_{x} = \begin{vmatrix}
c_{1} & b_{1}  \\
c_{2} & b_{2}
\end{vmatrix},\
\Delta_{y} = \begin{vmatrix}
a_{1} & c_{1} \\
a_{2} & c_{2}
\end{vmatrix}$$

$$x = \frac{\Delta_{x}}{\Delta}, y = \frac{\Delta_{y}}{\Delta}$$

## 3 Linear Equations in 3 variables

$$a_{1}x + b_{1}y + c_{1}z = d_{1}$$
$$a_{2}x + b_{2}y + c_{2}z = d_{2}$$
$$a_{3}x + b_{3}y + c_{3}z = d_{3}$$

$\\$
$$\Delta = \begin{vmatrix}
a_{1} & b_{1} & c_{1}  \\
a_{2} & b_{2} & c_{2}  \\
a_{3} & b_{3} & c_{3}
\end{vmatrix}
$$

Replacing corresponding columns by $d_{1},d_{2},d_{3}$,
$$
\Delta_{x} = \begin{vmatrix}
\boldsymbol{d_{1}} & b_{1} & c_{1}  \\
\boldsymbol{d_{2}} & b_{2} & c_{2}  \\
\boldsymbol{d_{3}} & b_{3} & c_{3}
\end{vmatrix}
$$

$$ 
\Delta_{y} = \begin{vmatrix}
a_{1} & \boldsymbol{d_{1}} & c_{1}  \\
a_{2} & \boldsymbol{d_{2}} & c_{2}  \\
a_{3} & \boldsymbol{d_{3}} & c_{3}
\end{vmatrix}
$$

$$ 
\Delta_{z} = \begin{vmatrix}
a_{1} & b_{1} & \boldsymbol{d_{1}}  \\
a_{2} & b_{2} & \boldsymbol{d_{2}}  \\
a_{3} & b_{3} & \boldsymbol{d_{3}}
\end{vmatrix}
$$



### Cramer's Rule
1. Unique solutions
	$$\Delta \neq 0$$
	Solutions will be,
	$$x = \frac{\Delta_{x}}{\Delta},\ y = \frac{ \Delta_{y} }{ \Delta },\ z = \frac{ \Delta_{z} }{ \Delta }$$

2. Infinite or no solution.
	$$\Delta = \Delta_{x} = \Delta_{y} = \Delta_{z} = 0$$
	This is because writing this is similar to writing $5 = 7$ and then multiplying 0 both sides.
	
	To check, we use this condition and find the value of the parameter, and then cross check with the original set of equations. 
	$\\$

3. No solution and the system will be *Inconsistent.*
	$$\Delta = 0 \ce{\ \& atleast one of \Delta_{x}, \Delta_{y}, \Delta_{z} } \neq 0$$

For Example, see here that we put the value p = 2 back into the equations and then analysed from there. 
![[Pasted image 20230703092751.png]]

![[Pasted image 20230703092805.png]]

#### Explanation of Cramer's Rule
$$a_{1}x + b_{1}y + c_{1}z = d_{1} \dots (1)$$
$$a_{2}x + b_{2}y + c_{2}z = d_{2} \dots (2)$$
$$a_{3}x + b_{3}y + c_{3}z = d_{3} \dots (3)$$

Now,
$$\Delta = \begin{vmatrix}
a_{1} & b_{1} & c_{1}  \\
a_{2} & b_{2} & c_{2}  \\
a_{3} & b_{3} & c_{3}
\end{vmatrix}
$$
Giving cofactor of $a_{1}$,
$$C_{a_{1}} = b_{2}c_{3} - b_{3}c_{2}$$

And,
$$
\Delta_{x} = \begin{vmatrix}
\boldsymbol{d_{1}} & b_{1} & c_{1}  \\
\boldsymbol{d_{2}} & b_{2} & c_{2}  \\
\boldsymbol{d_{3}} & b_{3} & c_{3}
\end{vmatrix}
$$
Giving Cofactor of $d_{1}$,
$$C_{d_{1}} = b_{2}c_{3} - b_{3}c_{2} = C_{a_{1}}$$

Now consider, 
$$C_{a_{1}}(1) + C_{a_{2}}(2) + C_{a_{3}}(3)$$
$$\left( \sum a_{1}C_{a_{1}} \right)x + \left( \sum b_{1}C_{a_{1}} \right)y + \left( \sum c_{1}C_{a_{1}} \right)z = \sum d_{1}C_{a_{1}}$$
$$\Delta . x = \sum d_{1}C_{d_{1}} = \Delta_{x}$$
Thus,
$$\Delta x = \Delta_{x}$$

Similarly, we get y and z,
$$\Delta y = \Delta_{y}$$
$$\Delta z = \Delta_{z}$$

Now if $\Delta \neq 0$, then we will get unique solutions,
$$x = \frac{\Delta_{x}}{\Delta},\ y = \frac{ \Delta_{y} }{ \Delta },\ z = \frac{ \Delta_{z} }{ \Delta }$$

And if $\Delta = 0$ and at least one of $\Delta_{x},\Delta_{y},\Delta_{z} \neq 0$ then equations will be inconsistent and there will be no solutions. 
This is because if $\Delta_{x} \neq 0$ (say) the equation will be,
$$0. x = \Delta_{x} \implies \ce{ zero = non-zero }$$

Finally if $\Delta = 0$ and $\Delta_{x} = \Delta_{y} = \Delta_{z} = 0$ then either no solution or infinite solutions.

### Homogeneous system of Equations
When the constants are all zero. 

$$a_{1}x+ b_{1}y + c_{1}z = 0$$
$$a_{2}x+ b_{2}y + c_{2}z = 0$$
$$a_{3}x+ b_{3}y + c_{3}z = 0$$

$$\Delta = \begin{vmatrix}
a_{1} & b_{1} & c_{1} \\
a_{2} & b_{2} & c_{2} \\
a_{3} & b_{3} & c_{3}
\end{vmatrix}$$

And,
$$\Delta_{x} = \Delta_{y} = \Delta_{z} = 0$$

Now, if
$$\Delta \neq 0$$
the system has unique solution. $(0,0,0)$

And, if 
$$\Delta = 0$$
the system has infinite solutions.


#### Trivial and Non Trivial solutions
Trivial when the solutions are $(0,0,0)$
Also called zero solution. 

Non-trivial when there are infinite solutions. (including $(0,0,0)$)
Non zero solutions also exist. 

## 3 Linear Equations in 2 Variables

$$a_{1}x + b_{1}y = c_{1}$$
$$a_{2}x + b_{2}y = c_{2}$$
$$a_{3}x + b_{3}y = c_{3}$$

How to check if the system is consistent or not:
1. Solve any 2 equations for x and y. 
2. If this x, y satisfies the third equation then it is a consistent system. 
3. It it does not satisfy then the system is inconsistent. 

Alternatively,

$$\Delta = \begin{vmatrix}
a_{1} & b_{1} & c_{1} \\
a_{2} & b_{2} & c_{2} \\
a_{3} & b_{3} & c_{3}
\end{vmatrix}$$
If $\Delta\neq 0$ then inconsistent. 
If $\Delta=0$ then consistent, this is called **Condition of Concurrency.** However, this is *not sufficient condition* for solution. 
That is, $\Delta=0$ does not imply that the solution will exist. However if solution exists, then $\Delta$ will be zero.

Three lines in 2 variables would be consistent only if they intersect at one point. This is called concurrency. If the 3 lines don't intersect at one point then the system is inconsistent. 

