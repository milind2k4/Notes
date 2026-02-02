Links: [[00 Vectors]], [[09 Straight Line]]
___
# Equation of a Line
The line passes through $A:\vec{a}$ and is parallel to $\vec{b}$ can be given as,
#### In Vector form
$$\vec{r} = \vec{a} + \lambda \vec{b}$$
where $\vec{a}$ is fixed vector which is fixed point and $\vec{b}$ is free vector which is direction of line. 

Every point on the line has a unique value of $\lambda$.

This can also be written as,
$$(\vec{r} - \vec{a}) \times \vec{b} = \vec{O}$$
as $\vec{r} - \vec{a}$ vector will be collinear with $\vec{b}$.

![[Pasted image 20231109151347.png]]

Equation of line passing through $A:\vec{a}$ and $B:\vec{b}$ can be given as,
$$\vec{r} = \vec{a} + \lambda(\vec{b} - \vec{a})$$

![[Pasted image 20231109151656.png]]

Equation of line passing through $A:\vec{a}$ and which is perpendicular to vectors $\vec{b}\ \&\ \vec{c}$ ($\vec{b} \times \vec{c} \neq 0$) can be given as.

$$\vec{r} = \vec{a} + \lambda(\vec{b} \times \vec{c})$$

![[Pasted image 20231109151921.png]]

#### In Coordinate form
##### Symmetric Form
For equation of line passing through a point $A:(x_{1},y_{1},z_{1})$ and having direction ratio parallel to it as $(a,b,c)$ can be given as,

$$
\begin{split}
\vec{r} &= (x,y,z) \\
\vec{a} &= (x_{1},y_{1},z_{1}) \\
\vec{b} &= (a,b,c) 
\end{split}
$$

Thus, $\vec{r} = \vec{a} + \lambda \vec{b}$ can be written as,
$$\frac{ x - x_{1} }{ a } = \frac{ y - y_{1} }{ b } = \frac{ z - z_{1} }{ c } = \lambda$$
Here $(x_{1},y_{1},z_{1})$ are the coordinate of point A and $(a,b,c)$ are dr parallel to the line. Since $(a,b,c)$ is dr, we can multiply it by any number $\mu$.

To find a point on a line,
$$\frac{ x - x_{1} }{ a } = \frac{ y - y_{1} }{ b } = \frac{ z - z_{1} }{ c } = \lambda$$
And then solve for x, y, z individually to get,
$$P:(x_{1} + a\lambda, y_{1} + b\lambda, z_{1} + c\lambda)$$

##### Non Symmetric Form 
A line can also be defined as line of intersection of two planes, say $P_{1} = 0$ and $P_{2} = 0$. I.e. we will write,
$$P_{1} = 0\ \&\ P_{2} = 0$$
$$P_{1} = 0 = P_{2}$$

Line L can also be written as,
$$L \equiv P_{1} = 0 = P_{1} + \lambda P_{2}$$
because $P_{1} + \lambda P_{2}$ passes through the line of intersection of $P_{1}$ and $P_{2}$.

The direction of line of intersection of planes $P_{1}$ and $P_{2}$ will be along $\vec{n}_{1} \times \vec{n}_{2}$.

![[Pasted image 20231109153826.png]]

To find equation of line of intersection of $P_{1}$ and $P_{2}$ in symmetric form, 
- we need a direction parallel to line, which will be $\vec{n}_{1} \times \vec{n}_{2}$.
- we need a point on the line, for which we will solve equations $P_{1} = 0$ and $P_{2} = 0$. To solve the equations, we take any of x, y, z as a fixed number (typically zero). 

![[Pasted image 20231109154602.png]]
![[Pasted image 20231109154619.png]]

> **Note** if a line is given as then to check whether it is same line or not, we first verify  the $(a,b,c)$ ratio of both. 
> If it is same, then both lines may be coincident or parallel. 
> To check, put the fixed point obtained in  the the line which is to be checked. 
> If all the ratios are the same, then both the lines are coincident, and if not they will be different parallel lines.

### Writing Equation of Line in Symmetric Form 
If line is given as $P_{1} = 0 = P_{2}$ then to convert it into symmetric form, 
1. Try to get a point by putting z = 0 and then solving $P_{1} = 0$ and $P_{2} = 0$.
   And direction will be along $\vec{n}_{1} \times \vec{n}_{2}$.
	$\\$

2. From  $P_{1} = 0$ and $P_{2} = 0$ we find $P_{3} = 0$ and $P_{4} = 0$ such that both contain only 2 of x, y, z and then equate the common variable.

![[Pasted image 20231110093846.png]]

For example,
![[Pasted image 20231110094310.png]]