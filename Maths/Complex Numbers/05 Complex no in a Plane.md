Links: [[00 Complex Numbers]], [[03 Representation of Complex No.]]
___
# Complex No. as Point 
in 2D plane 

If complex no is $x+iy$, then the point will be $(x,y)$
To go from coordinate to complex no., we write,
$$
\begin{split}
x &= \frac{ z + \bar{z} }{ 2 } \\
y &= \frac{ z - \bar{z} }{ 2i } \\
\end{split}
$$

#### Area of triangle 
Area of ABC where complex no associated with A, B, C are $z_{1},z_{2},z_{3}$. 
$$\Delta = \frac{ 1 }{ 4i }
\begin{vmatrix}
z_{1} & \bar{z}_{1} & 1 \\
z_{2} & \bar{z}_{2} & 1 \\
z_{3} & \bar{z}_{3} & 1
\end{vmatrix}
$$

### Equation of straight line
Equation of line passing though $z_{1},z_{2}$ can be given as,
##### Using Area of Triangle
$$
\begin{vmatrix}
z & \bar{z} & 1 \\
z_{2} & \bar{z}_{2} & 1 \\
z_{3} & \bar{z}_{3} & 1 
\end{vmatrix} = 0
$$
As any point on the line (z) will make a triangle whose area will be zero. 

##### Using Collinearity of Vectors 
$$arg\left( \frac{ z - z_{1} }{ z_{2} - z_{1} } \right) = 0\ or\ \pi$$
$$\frac{ z - z_{1} }{ z_{2} - z_{1} } = \frac{ \bar{z} - \bar{z}_{1} }{ \bar{z}_{2} - \bar{z}_{1} }$$

Or we can use complex no. in place of vectors in equation $\vec{r} = \vec{a} + \lambda \vec{b}$. 

$$z = z_{1} + \lambda (z_{2} - z_{1}),\ \lambda \in R$$

![[Pasted image 20231117093555.png]]

##### Standard Equation 
Simplifying the 2nd one in the last header,

$$
\begin{split}
\frac{ z - z_{1} }{ z_{2} - z_{1} } &= \frac{ \bar{z} - \bar{z}_{1} }{ \bar{z}_{2} - \bar{z}_{1} } \\
(\bar{z}_{2} - z_{1})z - (z_{2}-z_{1})\bar{z} - z_{1}(\bar{z}_{2} - \bar{z}_{1}) + \bar{z}_{1} (z_{2} - z_{1}) &= 0 \\
i(\bar{z}_{2} - z_{1})z - i(z_{2}-z_{1})\bar{z} - i[z_{1}(\bar{z}_{2} - \bar{z}_{1}) - \bar{z}_{1} (z_{2} - z_{1})] &= 0 
\end{split}
$$
Thus giving,
$$\bar{a}z + a \bar{z} + b = 0$$
where $a$ will be a vector $\perp$ to line. 

Any line parallel to this can be written as,
$$\bar{a}z + a \bar{z} + \lambda = 0$$

Any line perpendicular to this can be written as,
$$-\bar{a}iz + ai \bar{z} + \lambda = 0$$

![[Pasted image 20231117094005.png]]

However, we should pay attention to [[01 Algebra and Rotation#Rotation|rotation]] while finding the equation.
![[Pasted image 20231117095531.png]]

##### Reflection and Perpendicular 
If $A:z_{1}$ and $B:z_{2}$ are reflection of each other in line, then,
$$\bar{a}z_{1} + a \bar{z}_{2} + \lambda = 0$$
$$\bar{a}z_{2} + a \bar{z}_{1} + \lambda = 0$$
From this we can get $z_{2}$ in terms of $z_{1}$, (i.e. reflection of $z_{1}$ in L)
$$z_{2} = -\left( \frac{ a\bar{z}_{1} + b }{ \bar{a} } \right)$$

Length of perpendicular from $A:z_{1}$ to L,
$$d = \frac{ |\bar{a}z_{1} + a \bar{z}_{1} + b| }{ 2|a| }$$

Foot of perpendicular,
$$z_{N} = \frac{ \bar{a}z_{1} - a\bar{z}_{1} - b }{ 2\bar{a} }$$

![[Pasted image 20231117094536.png]]

For Real intercept, $z = \bar{z}$, giving,
$$z_{re} = \frac{ -b }{ a + \bar{a} }$$

For Imaginary intercept, $-z = \bar{z}$, giving,
$$z_{im} = \frac{ -b }{ \bar{a} - a }$$

### Equation of Circle 
$$|z - z_{o}| = r$$
Opening it,
$$
\begin{split}
|z|^{2} + |z_{o}|^{2} - \bar{z}z_{o} - z\bar{z}_{o} &= r^{2} \\
z\bar{z} - z\bar{z}_{o} - \bar{z}z_{o} + z_{o}\bar{z}_{o} - r^{2} &= 0
\end{split}
$$
Thus finally,
$$z\bar{z} + \bar{z}z + a\bar{z} + b = 0$$
which is the same as equation of line with $z\bar{z}$ added to it.
Here, centre is at $-a$ and radius is $\sqrt{ a\bar{a} - b }$. 

Even if it is argand plane, the circle formed will be real (visible) and thus $a \bar{a} > b$.

![[Pasted image 20231117113029.png]]

##### Diametric Form 
If $A:z_{1}$ and $B:z_{2}$ are ends of diameter of a circle, then, equation of circle can be given as,
$$
\begin{split}
AP^{2} + BP^{2} &= AB^{2} \\
|z - z_{1}| + |z - z_{2}|^{2} &= |z_{1} - z_{2}|^{2} 
\end{split}
$$

Using equation of arc,
$$arg\left( \frac{ z - z_{1} }{ z - z_{2} } \right) = \pm \frac{\pi}{2}$$

Using rotation,
$$\frac{ z - z_{1} }{ z - z_{2} } + \frac{ \bar{z} - \bar{z}_{1} }{ \bar{z} - \bar{z}_{2} } = 0$$
Cross multiplying,
$$(z - z_{1})(\bar{z} - \bar{z}_{2}) + (\bar{z} - \bar{z}_{1})(z - z_{2}) = 0$$

![[Pasted image 20231117113934.png]]

#### Equation of Arc

$$arg\left( \frac{ z - z_{1} }{ z - z_{2} } \right) = \theta$$
Depending on this $\theta$, the arc will be different. 

![[Pasted image 20231117113219.png]]

## Examples
![[Pasted image 20231117114336.png]]

![[Pasted image 20231117130154.png]]
![[Pasted image 20231117130158.png]]

