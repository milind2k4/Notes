Links: [[00 Straight Line]], [[01 Section Formula]]
___
# Line, Line and Line, Point
## Properties of Two Lines
### Intersection of two Lines
To find the point of intersection of two lines, we solve the equations of lines simultaneously. 

If the lines are 
$$l_{1} \equiv a_{1}x + b_{1}y + c_{1} = 0$$
$$l_{1} \equiv a_{2}x + b_{2}y + c_{2} = 0$$

Then their point of intersection will be,
$$P:\left( \frac{ b_{1}c_{2} - b_{2}c_{1} }{ a_{1}b_{2} - a_{2}b_{1} }, \frac{ c_{1}a_{2} - a_{2}a_{1} }{ a_{1}b_{2} - b_{1}a_{2} } \right)$$

To find point of intersection with x axis, put y = 0
To find point of intersection with y axis, put x = 0

### Angle between two lines 
Let angle between $L_{1}$ and $L_{2}$ be $\theta$, then,
$$
\begin{split}
\tan \theta &= \tan (\theta_{2} - \theta_{1}) \\
&= \frac{ \tan \theta_{2} - \tan \theta_{1} }{ 1 + \tan \theta_{1} \tan \theta_{2} } \\
\\
&= \frac{ m_{2} - m_{1} }{ 1 + m_{1}m_{2} }
\end{split}
$$

Angle between $l_{1}$ and $L_{2}$ are $\theta$ and $\pi - \theta$ and usually only acute angle is given. Thus,
$$\theta = \tan ^{-1} \left| \frac{ m_{1} - m_{2} }{ 1 + m_{1}m_{2} } \right| $$



Also, the obtuse angle has tan -ve of the acute angle between the lines,
$$\tan \theta = -\tan(\pi - \theta)$$

![[Pasted image 20230706164644.png]]

If L is a given line with slope $m (= \tan \alpha)$ then to find slopes of lines which are inclined at an angle $\theta$ with original line we can observe that $L_{1}$ and $L_{2}$ will make angles $\alpha - \theta$ and $\alpha + \theta$. Thus, 

Slope,
$$L_{1} = m_{1} = \tan(\alpha - \theta)$$
$$L_{2} = m_{2} = \tan(\alpha + \theta)$$

Which is,
$$m_{1} = \frac{ m - \tan \theta }{ 1 + m\tan \theta }$$
$$m_{2} = \frac{ m + \tan \theta }{ 1 - m\tan \theta }$$

![[Pasted image 20230707091209.png]]

#### Parallel and Perpendicular Lines 
Slopes of parallel lines are equal, or both lines are vertical. 

If $L_{1}$ and $L_{2}$ are perpendicular, then,
$$m_{1}.m_{2} = -1$$
or one line is horizontal and the other is vertical.

Let L be given as $ax + by + c = 0$, then 
- any line parallel to L can be given as, $ax + by + \lambda = 0$
- any line perpendicular to L can be given as, $bx - ay + \lambda = 0$

![[Pasted image 20230707091648.png]]

## Properties of a Line and a Point
### Foot and Length of Perpendicular 
Let line L be,
$$L(x,y) = ax + by + c$$

Drop a perpendicular from a point on the line. Where it touches the line is the foot.
![[Pasted image 20230707094244.png]]

Length of perpendicular from $A:(x_{1},y_{1})$ to L,
$$l = \frac{ |ax_{1} + by_{1} + c| }{ \sqrt{ a^{2} + b^{2} } }$$
In short,
$$l = \frac{ |L(x_{1},y_{1})| }{ \sqrt{ a^{2} + b^{2} } }$$

Foot of perpendicular,
$$N \equiv \frac{ x - x_{1} }{ a } = \frac{ y - y_{1} }{ b } = - \frac{ ax_{1} + by_{1} + c }{ a^{2} + b^{2} }$$

$$N \equiv \frac{ x - x_{1} }{ a } = \frac{ y - y_{1} }{ b } = - \frac{ L(x_{1},y_{1}) }{ a^{2} + b^{2} }$$
From here we solve for x and y. 

We can also find reflection of point in line,
$$B \equiv \frac{ x - x_{1} }{ a } = \frac{ y - y_{1} }{ b } = - \frac{ 2(ax_{1} + by_{1} + c) }{ a^{2} + b^{2} }$$

$$B \equiv \frac{ x - x_{1} }{ a } = \frac{ y - y_{1} }{ b } = - \frac{ 2(L(x_{1},y_{1})) }{ a^{2} + b^{2} }$$

![[Pasted image 20230707094302.png]]

From the origin,
Length of perpendicular,
$$l = \frac{ |c| }{ \sqrt{ a^{2} + b^{2} } }$$

#### Distance between two Parallel Lines
$$L_{1} \equiv ax + by + c_{1} = 0$$
$$L_{1} \equiv ax + by + c_{2} = 0$$

Distance between them,
$$d = \frac{ |c_{1} - c_{2}| }{ \sqrt{ a^{2} + b^{2} } }$$

This can be proved by finding length of perpendicular from origin to the two lines and then adding or subtracting them. 


### Location of a Point wrt a Straight Line 
For points on the line, $L(P) = 0$ i.e. they satisfy the linear equation. 
Points not on the straight line will not satisfy the equation. 

Points not on the line but on the same side will have the same sign. If points lie on  opposite signs then the values obtained will be of opposite sign. 


In the figure,
$$
\begin{split}
L(A) = L(x_{1},y_{1}) &= 0 \\
L(B), L(C), L(D) &\neq 0 \\
\\
L(B).L(C) &> 0 \\
L(B).L(D) &< 0
\end{split}
$$
![[Pasted image 20230708085728.png]]

If we make the coefficient of x +ve in the expression, then the +ve values will lie on the right side as when we move horizontally to the right, the value of x increases and  the value of y remains the same.

If we make the coefficient of y +ve in the expression, then the +ve values will lie above the line as when we move vertically up, the value of y increases and the value of x remains the same.  


Example, In questions which ask to find  the ratio in which the line divides a line joining two points, we find  the coordinates and then substitute it into equation of line.
![[Pasted image 20230708090653.png]]
Alternatively, but here we have to explain the reason for -ve.
![[Pasted image 20230708090924.png]]
