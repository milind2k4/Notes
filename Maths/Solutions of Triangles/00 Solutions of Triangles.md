Links: [[01 Trigonometric Properties]]
___
# Solutions of Triangle (SOT)
aka Properties of Triangle 

#### [[05 Notations and Results in a Triangle|General Notation]]

R is Circumradius which is radius of circumcircle.
![[Pasted image 20231117202137.png]]

r is inradius which is radius of incircle (circle which touches sides internally). 
![[Pasted image 20231117202330.png]]

Excircle is one which touches one side externally and the other 2 internally. There are 3 in one triangle.
The excircle opposite to A will be $(I_{1},r_{1})$ and so on. 

#### Results in a Triangle 
Sum of angles is $\pi$,
$$A + B + C = \pi$$

If angles of a triangle ABC are in AP, then $\angle B = 60^{\circ}$.


Sum of two sides will be greater than the third side. 
$$
\begin{split}
a + b &> c \\
b + c &> a \\
c + a &> b 
\end{split}
$$

Difference of two sides will be less than the third side. 
$$
\begin{split}
a \sim b &< c \\
b \sim c &< a \\
c \sim a &< b 
\end{split}
$$

Angle opposite to the greatest side will be the biggest.

Triangles made on same base and height will have equal areas. 
Triangles made on same base but different heights will have areas in the ratio of their heights. 

If two triangles are similar, then ratio of corresponding sides will be equal. 

$$\frac{ a }{ a_{1} } = \frac{ b }{ b_{1} } = \frac{ c }{ c_{1} } = \frac{ h }{ h_{1} } = \sqrt{ \frac{ [ABC] }{ [A_{1}B_{1}C_{1}] } }$$

![[Pasted image 20231117203905.png]]

##### Mid point theorem
The line joining mid points of two sides will be parallel and half of the third side. This is the **Mid point theorem.**

The four triangles formed are similar and all the small triangles will have area equal to 1/4th that of the big triangle.
The 3 small triangles (the G triangles) formed also have same area. 

![[Pasted image 20231117204119.png]]

#### Apollonius's Theorem
[[05 Notations and Results in a Triangle#Apollonius's Theorem]]

In ABC, let M be mid point of BC, then
$$
\begin{split}
AB^{2} + AC^{2} &= 2(AD^{2} + CM^{2}) \\
&= 2(AM^{2} + BM^{2}) 
\end{split}
$$

Using this we can find length of median form A,
$$
\begin{split}
AB^{2} + AC^{2} &= 2(AM^{2} + BM^{2}) \\
c^{2} + b^{2} &= 2\left( AM^{2} + \frac{ a^{2} }{ 4 } \right) \\
AM &=  \frac{ \sqrt{ 2(b^{2} + c^{2}) - a^{2} } }{ 2 } 
\end{split}
$$
Similarly, length of median through B,
$$BM = \frac{ \sqrt{ 2(a^{2} + c^{2}) - b^{2} } }{ 2 }$$
And length of median through C,
$$CM = \frac{ \sqrt{ 2(a^{2} + b^{2}) - c^{2} } }{ 2 }$$

Now, since AG is 2/3 of AM,
$$AG = \frac{ \sqrt{ 2(a^{2} + b^{2}) - c^{2} } }{ 3 }$$
which is nothing but distance of centroid from vertex A.
And,
$$GM = \frac{ \sqrt{ 2(a^{2} + b^{2}) - c^{2} } }{ 6 }$$

![[Pasted image 20231117205810.png]]

#### [[01 Trigonometric Properties]]

#### Sum of sides 
$$
\begin{split}
s &= \frac{ a + b + c }{ 2 } \\
s - a &= \frac{ b + c - a }{ 2 } \\
s - b &= \frac{ a + c - b }{ 2 } \\
s - c &= \frac{ a + b - c }{ 2 } \\
\end{split}
$$
and all three will be +ve. 

And, summing over them,
$$
\begin{split}
\sum (s-a) &= (s-a) + (s-b) + (s-c) \\
&= s 
\end{split}
$$


#### For 3 numbers 
Let 3 numbers be a, b, c, then,

$$
\begin{split}
\sum a &= a + b + c \\
\sum (a + b) &= 2(a + b + c) \\
\sum (a - b) &= 0 \\
\sum a(b - c) &= 0 \\
\\
\prod a &= abc \\
\prod ab &= a^{2}b^{2}c^{2} \\
\prod \frac{ a }{ b } &= 1
\end{split}
$$

#### Difference of Squares 
**Square of sum of two sides - square of third side,**
$$
\begin{split}
(a + b)^{2} - c^{2} &= (a + b - c)(a + b + c) \\
&= 2s (2(s - c)) \\
&= 4 s(s - c) \\
\end{split}
$$
Similarly, we get,
$$
\begin{split}
(a + b)^{2} - c^{2} &= 4s(s - c) \\
(b + c)^{2} - a^{2} &= 4s(s - a) \\
(c + a)^{2} - b^{2} &= 4s(s - b) \\
\end{split}
$$

**Square of third side - square of difference of two sides,**
$$
\begin{split}
a^{2} - (b-c)^{2} &= (a + b - c)(a - b + c) \\
&= 4(s - c)(s - b) \\
c^{2} - (a-b)^{2} &= 4(s - a)(s - b) \\
b^{2} - (a-c)^{2} &= 4(s - a)(s - c)
\end{split}
$$

### Area of Triangle 
Area of triangle can be given by,
$$
\begin{split}
[ABC] &= \sqrt{ s(s-a)(s-b)(s-c) } \\
&= \frac{ 1 }{ 2 }ab \sin C = \frac{ 1 }{ 2 }bc \sin A = \frac{ 1 }{ 2 } ca \sin B \\
&= 2R^{2} \sin A \sin B \sin C \\
&= \frac{ abc }{ 4R }
\end{split}
$$

The last one can be used to get circumradius,
$$R = \frac{ abc }{ 4 \Delta }$$

##### Perpendicular and Base
![[Pasted image 20231120090531.png]]

Area of triangle ABC,
$$[ABC] = \frac{ 1 }{ 2 } p_{1} a = \Delta$$
Giving, length of altitude from vertex A,
$$p_{1} = \frac{ 2\Delta }{ a }$$
Similarly,
$$p_{2} = \frac{ 2\Delta }{ b }$$
$$p_{3} = \frac{ 2\Delta }{ c }$$


##### Perpendicular and Base using Projection
![[Pasted image 20231120174359.png]]

Using projection formula,
$$AD = c\sin B = b\sin C$$
Giving area,
$$
\begin{split}
[ABC] &= \frac{ 1 }{ 2 } ab \sin C \\
&= \frac{ 1 }{ 2 } bc \sin A \\
&= \frac{ 1 }{ 2 } ca \sin B
\end{split}
$$

Converting both a and b to sin using Sine Law,
$$\Delta = 2R^{2} \sin A \sin B \sin C$$

Converting the sin to side,
$$\Delta = \frac{ abc }{ 4R }$$



### Projection Formula 
Using trigonometry, we have,
$$a = c \cos B + b \cos C$$
$$b = a \cos C + c \cos A$$
$$c = b \cos A + a \cos B$$
i.e. sum of projections of two sides on the third side will be equal to the length of the third side.

![[Pasted image 20231120172040.png]]

## [[02 Sine and Cosine Law]]


## Misc. Examples 
![[Pasted image 20231117211328.png]]

![[Pasted image 20231120090745.png]]







