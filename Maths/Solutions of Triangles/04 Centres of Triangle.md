Links: [[06 Coordinates of Centres and Area of Triangle]], [[05 Notations and Results in a Triangle]]
___
# Centres of a Triangle 
##### Centroid
Here, $\displaystyle \frac{ AG }{ GD } = \frac{ 2 }{ 1 }$, $FE = \frac{1}{2} BC$ and is parallel to it. 

![[Pasted image 20231124134117.png]]

Centroid of triangle DEF is also G. And, $A_{1},B_{1},C_{1}$ are mid points of the respective sides. 

#### Orthocentre

![[Pasted image 20231124134559.png]]

##### Division of Opposite Side
$$
\begin{split}
\frac{ BD }{ DC } &= \frac{ c \cos B }{  b \cos C } \\
&= \frac{ 2R\sin C \cos B }{ 2R\sin B \cos C } \\
&= \frac{ \tan C }{ \tan B }
\end{split}
$$
Thus an altitude from A divides the opposite side in ratio $\tan C:\tan B$.

##### Distance of Vertex from H
In $\Delta BHD$,
$$
\begin{split}
BH &= BD \csc C \\
&= c \cos B \frac{ 1 }{ \sin C } \\
&= 2R \sin C \cos B \frac{ 1 }{ \sin C } \\
&= 2R \cos B
\end{split}
$$
which is distance of vertex B from orthocentre. 

Hence distances of orthocentre from vertices will be, $2R\cos A, 2R\cos B, 2R\cos C$. 

##### Distance of Opposite side from H
Again, in $\Delta BHD$,
$$
\begin{split}
HD &= BH \cos C \\
&= 2R \cos B \cos C
\end{split}
$$
which is distance of orthocentre from BC side. 

##### Ratio in which H divides Altitude
Dividing the previous two results,
$$
\begin{split}
\frac{ AH }{ HD } &= \frac{ 2R\cos A }{ 2R \cos B \cos C } \\
\\
&= \frac{ \sin A }{ \sin A } \frac{ \cos A }{ \cos B \cos C } \\
\\
&= \frac{ \sin(B+C) }{ \tan A \cos B \cos C } \\
\\
&= \frac{ \tan B + \tan C }{ \tan A }
\end{split}
$$
which is the ratio in which orthocentre divides the altitude. 
Remember that (tan B + tan C) which is the ratio altitude divides the opposite side in, will be on the top. 

Quadrilateral CEHD is cyclic and the circle passing though these 4 points will have CH as diameter, which will be $2R\cos C$. Thus radius of this circle will be $R\cos C$.

![[Pasted image 20231124140343.png]]

#### Circumcentre 

![[Pasted image 20231124140546.png]]

##### Division of Opposite side
In $\Delta ABE$,
$$
\begin{split}
\frac{ AE }{ \sin \left( \frac{\pi}{2} - C \right) } &= \frac{ AB }{ \sin \left( \frac{\pi}{2} - (A-C) \right) } \\
AE &= \frac{ c \cos C }{ \cos (A-C) } \\
\\
\text{Using Symmetry,} \\
CE &= \frac{ a \cos A }{ \cos (C-A) } \\
\\
\text{Thus}, \\
\frac{ AE }{ CE } &= \frac{ c \cos C }{ a \cos A } \\
&= \frac{ 2R \sin C \cos C }{ 2R\sin A \cos A } \\
&= \frac{ \sin 2C }{ \sin 2A } 
\end{split}
$$
which is the ratio in which extension of circumradius from B divides the side AC. 

Similarly,
$$\frac{ BD }{ DC } = \frac{ \sin 2C }{ \sin 2D }$$
This is from where the coordinates of circumcentre in 2D comes.

##### Ratio in which O divides Extension of circumradius
In $\Delta AOM_{2}$,
$$OM_{2} = R \cos B$$

In $\Delta OEM_{2}$,
$$
\begin{split}
OE &= \frac{ OM_{2} }{ \cos (A-C) } \\
&= \frac{ R\cos B }{ \cos (A-C) } 
\end{split}
$$

Now,
$$
\begin{split}
\frac{ BO }{ OE } &= \frac{ R \cos (A-C) }{ R \cos B } \\
&= \frac{ \cos (A-C) }{ \cos B } \\
&= \frac{ 2\sin B \cos (A-C) }{ 2\sin B \cos B } \\
&= \frac{ \sin 2A + \sin 2C }{ \sin 2B }
\end{split}
$$
which is ratio in which O divides BE i.e. extension of circumradius. 

#### Incentre 

![[Pasted image 20231124200242.png]]

##### Division of Opposite Side
Angular bisector cuts the opposite side in the ratio of opposite sides. 
$$\frac{ BD }{ DC } = \frac{ AB }{ AC } = \frac{ c }{ b }$$

We can write,
$$
\begin{split}
BD &= \frac{ c }{ b+c }. BC \\
&= \frac{ ac }{ b+c }
\end{split}
$$
Similarly,
$$DC = \frac{ ab }{ b+c }$$

##### Ratio in which I divides Angular Bisector
In $\Delta BAD$, BI is angular bisector of angle ABD. Thus,
$$\frac{ AI }{ ID } = \frac{ BA }{ BD } = \frac{ b+c }{ a }$$
This is the ratio in which incentre divides angular bisector. 

Similarly,
$$\frac{ BI }{ IE } = \frac{ a+c }{ b }$$

##### Length of Angular Bisector
To find length of AD, we apply sine rule in $\Delta BAD$,
$$
\begin{split}
\frac{ AD }{ \sin B } &= \frac{ BD }{ \sin A /2 } \\
AD &= \frac{ \sin B }{ \sin A/2 } \frac{ ac }{ b+c } \\
&= \frac{ cb\sin A }{ (b+c)\sin A /2 } \\
&= \frac{ bc }{ b+c } \frac{ 2 \sin A /2 \cos A /2 }{ \sin A /2 } \\
&= \frac{ 2bc }{ b+c } \cos \frac{ A }{ 2 } 
\end{split}
$$
Thus giving, length of angular bisector through A,
$$AD = \frac{ 2bc }{ b+c } \cos \frac{ A }{ 2 }$$
Similarly, we will get,
$$BE = \frac{ 2ac }{ a+c } \cos \frac{ B }{ 2 }$$

##### Inradius 
![[Pasted image 20231124202203.png]]

$$
\begin{split}
[ABC] &= [IBC] + [IAC] + [IBC] \\
\Delta &= \frac{ 1 }{ 2 } r c + \frac{ 1 }{ 2 } rb + \frac{ 1 }{ 2 } ra \\
&= \frac{ r }{ 2 } (a + b + c) = \frac{ r(2s) }{ 2 } \\
&= rs
\end{split}
$$
Thus giving,
$$r = \frac{ \Delta }{ s }$$

Also,
$$
\begin{split}
r &= \frac{ \Delta }{ s(s-a) } . (s-a) \\
&= (s-a)\tan \frac{ A }{ 2 } \\
\end{split}
$$

Now, using symmetry,
$$
\begin{split}
r &= (s-a) \tan \frac{ A }{ 2 } \\
&= (s-b) \tan \frac{ B }{ 2 } \\
&= (s-c) \tan \frac{ C }{ 2 }
\end{split}
$$

Also,
$$
\begin{split}
r &= \frac{ 2\Delta }{ 2s } \\
&= \frac{ 2. 2R^{2} \sin A \sin B \sin C }{ a + b + c } \\
&= \frac{ 4R^{2} \prod \sin A }{ 2R \sum \sin A } \\
&= 2R \frac{ \prod 2 \sin A /2 \cos A /2 }{ 4\prod \cos A /2 } \\
&= 4 R \prod \sin A /2
\end{split}
$$

Compiling all the results, we have,
$$r = \frac{ \Delta }{ s } = (s-a) \tan \frac{ A }{ 2 } = 4R \prod \sin \frac{ A }{ 2 }$$

##### Distance of POC of Incircle from Vertex
![[Pasted image 20231124203709.png]]

In $\Delta BIA_{1}$, 
$$
\begin{split}
\tan \frac{ B }{ 2 } &= \frac{ r }{ BA_{1} } \\
BA_{1} \tan \frac{ B }{ 2 } &= (s-b) \tan \frac{ B }{ 2 } \\
BA_{1} &= (s-b)
\end{split}
$$
which is distance of point of contact of incircle from B.
Since $BA_{1}$ and $BC_{1}$ are tangents from the same point B, 
$$BA_{1} = BC_{1} = s-b$$

![[Pasted image 20231124204018.png]]

And, distance of vertex from incentre,
$$AI = r \csc \frac{ A }{ 2 }$$
$$BI = r \csc \frac{ B }{ 2 }$$
$$CI = r \csc \frac{ C }{ 2 }$$

##### Concyclic Points

C, A, I and B are cyclic with CI as diameter. 
Radius of this circle will be,
$$\frac{ CI }{ 2 } = \frac{ r \csc C /2 }{ 2 }$$

A circle can be inscribed in the cyclic quadrilateral formed. Let the radius of this circle be $r_{A}$.
Now, in $\Delta I_{A}ID_{1}$,
$$
\begin{split}
\tan \frac{A}{2} &= \frac{ r - r_{A} }{ r_{A} } \\
r_{A} &= \frac{ r }{ 1 + \tan A /2 }
\end{split}
$$

![[Pasted image 20231124205145.png]]
