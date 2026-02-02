Links: [[05 Solving Linear Equations]]
___
# Solution of Equations
This is the matrix method called **Gauss - Jordan Method Method**, for determinant method, see [[05 Solving Linear Equations]].

A set of equations in 3 variables can be considered planes in 3d space and their point(s) common in all of them is/are called the solution(s).

#### Definitions
Set of Equations is called 
- **Consistent** if at least one solution exists. 
- **Inconsistent** if no solution exists. 
- **Homogeneous** if $B = 0$ (i.e. $d_{1} = d_{2} = d_{3} = 0$). Homogeneous means that the planes are passing through Origin.
- **Non Homogeneous** is $B \neq 0$ i.e. at least one of $d_{1},d_{2},d_{3}$ is non zero.

A solution is
- **Trivial Solution** if $x = y = z = 0$
-  **Non Trivial** if at least one of $x,y,z$ is non zero

### 2 Equations in 3 Variables
Using plane analogy,
$$P_{1} \equiv a_{1}x + b_{1}y + c_{1}z = d_{1}$$
$$P_{2} \equiv a_{2}x + b_{2}y + c_{2}z = d_{2}$$

Then, they are,
- **Same Plane**
  $$\frac{ a_{1} }{ a_{2} } = \frac{ b_{1} }{ b_{2} } = \frac{ c_{1} }{ c_{2} } = \frac{ d_{1} }{ d_{2} }$$
- **Parallel and Distinct**
  $$\frac{ a_{1} }{ a_{2} } = \frac{ b_{1} }{ b_{2} } = \frac{ c_{1} }{ c_{2} } \neq \frac{ d_{1} }{ d_{2} }$$
- **Intersecting on a Line** if any of the two ratios out of $\displaystyle \frac{ a_{1} }{ a_{2} }, \frac{ b_{1} }{ b_{2} }, \frac{ c_{1} }{ c_{2} }$ are not equal. This also means that the planes are non parallel and not coincident. 

### 3 Equations in 3 Variables
$$a_{1}x + b_{1}y + c_{1}z = d_{1}$$
$$a_{2}x + b_{2}y + c_{2}z = d_{2}$$
$$a_{3}x + b_{3}y + c_{3}z = d_{3}$$

Here we define, 

Coefficient matrix,
$$A = \begin{bmatrix}
a_{1} & b_{1} & c_{1} \\
a_{2} & b_{2} & c_{2} \\
a_{3} & b_{3} & c_{3}
\end{bmatrix}$$

Variable matrix,
$$X = \begin{bmatrix}
x \\
y \\
z
\end{bmatrix}$$

Solution Matrix,
$$B = \begin{bmatrix}
d_{1} \\
d_{2} \\
d_{3}
\end{bmatrix}$$

Then the system of equations can be written as,
$$AX = B$$

A system of 3 equations in 3 variables can only have 0, 1 or infinite number of solutions, 
#### Using plane analogy
##### If at least two of the 3 planes are parallel 
1. If $P_{1}$ and $P_{2}$ are coincident,
	- If $P_{3}$ is also coincident then there will be infinite solutions (there is effectively one equation). 
	  Here the number of solutions is more than the the 3rd case here as the solution will come in 2 parameters.
	  $\\$
	- If $P_{3}$ is parallel and distinct then there will be no solutions
	  $\\$
	- If $P_{3}$ is non parallel then they will intersect in a line and there will be 2 equations and thus infinite solutions. 
	  Here the solution will be less than the number of solutions in the first case as the solutions will come in 1 parameter. 
	  $\\$
1. If $P_{1}$ and $P_{2}$ are distinct parallel, there will be no solution irrespective of $P_{3}$. 

![[Pasted image 20230703095906.png]]
##### If no two planes are parallel
If all of them share one line, i.e. they intersect at one line or line of intersection of $P_{1}$ and $P_{2}$ is the same as line of intersection of $P_{2}$ and $P_{3}$, they will have infinite solutions. 

If two planes intersect in a line and the third cuts this line at one point, then there will be one unique solution. 

If lines of intersection of all three are parallel, then there will be no solution.

![[Pasted image 20230703100351.png]]

### Homogenous $(B= O)$
Here trivial solutions will exist. 
$$X = O$$
is a solution.

If $|A| \neq 0$ then $X = O$ will be the only solution which will be the trivial solution.
If $|A| = 0$ then there will be infinite solutions, including trivial solutions. 

If there are infinite solutions, to find the solutions, we take any two equations and then fix one of the variables, then find the solutions. 
![[Pasted image 20230704092803.png]]

Using plane analogy, X = O solution means that all the three planes cut at origin. 
Infinite solutions means that the planes are coaxial and all the solutions lie on this line of intersection of the three planes which passes through origin. 

![[Pasted image 20230704091015.png]]

### Non Homogeneous $(B \neq O)$
If $|A| \neq 0$, $A^{-1}$ exists, then
$$
\begin{split}
AX &= B \\
X &= A^{-1}B 
\end{split}
$$
That is, unique solutions. The planes will intersect at one point which may or may not be origin. 

If $|A| = 0$,
$$
\begin{split}
AX &= B \\
\text{adj }A . AX &= \text{adj }A.B \\
|A|I_{n} X &= \text{adj }A. B \\
O &= \text{adj }A. B
\end{split}
$$
Now again, if
- $\text{adj }A.B \neq O$ then there will be no solution and thus the set will be inconsistent. 
- $\text{adj }A.B = O$ then there either infinite solutions or no solution. (this is like 5 = 4 and then multiplying 0 both sides)

#### Finding Solutions
If $|A| = 0$ then first check if any two planes are parallel,

If they are parallel and distinct, then the set is inconsistent and there is no solution.
If they are parallel and coincident then there may be infinite or unique solution. 

Then check if no two planes are parallel or coincident, then LHS of any one of the planes can be written as a combination of the other two. 
To check if the set is consistent or not, we find the coefficients a, b in 
$$aP_{1} + bP_{2} = P_{3}\ (\text{for LHS only})$$
and then check if those coefficients are consistent with the RHS. 
i.e. check if,
$$ad_{1} + bd_{2} = d_{3}$$
If this condition is true, then the planes are coaxial and there are infinite number of solutions and if it is false, then the planes do not intersect at a point and thus there is no solution. 
![[Pasted image 20230704094235.png]]
![[Pasted image 20230704094249.png]]