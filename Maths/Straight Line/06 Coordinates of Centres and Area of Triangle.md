Links: [[05 Notations and Results in a Triangle]]
___
# Coordinates of Different Centres of a Triangle
Let coordinates of vertices of triangle ACB are, $A:(x_{1},y_{1}), B:(x_{2},y_{2}), C:(x_{3},y_{3})$.

Centroid,
$$G:\left( \frac{ x_{1} + x_{2} + x_{3} }{ 3 }, \frac{ y_{1} + y_{2} + y_{3} }{ 3 } \right) = \left( \frac{ \sum x_{1} }{ 3 }, \frac{ \sum y_{1} }{ 3 } \right)$$

Orthocentre,
$$H:\left( \frac{ \sum x_{1}\tan A }{ \sum \tan A }, \frac{ \sum y_{1}\tan A }{ \sum \tan A } \right)$$

Incentre,
$$I:\left( \frac{ \sum ax_{1} }{ \sum a }, \frac{ \sum ay_{1} }{ \sum a } \right)$$

Excentres,
$$I_{1}:\left( \frac{ -ax_{1} + bx_{2} + cx_{3} }{ -a + b + c }, 
\frac{ -ay_{1} + by_{2} + cy_{3} }{ -a + b + c } \right)$$

$$I_{2}:\left( \frac{ ax_{1} - bx_{2} + cx_{3} }{ a - b + c }, 
\frac{ ay_{1} - by_{2} + cy_{3} }{ a - b + c } \right)$$

$$I_{3}:\left( \frac{ ax_{1} + bx_{2} - cx_{3} }{ a + b - c }, 
\frac{ ay_{1} + by_{2} - cy_{3} }{ a + b - c } \right)$$

![[Pasted image 20230706075432.png]]

Circumcentre,
$$O:\left( \frac{ \sum x_{1}\sin 2A }{ \sum \sin 2A }, \frac{ \sum y_{1}\sin 2A }{ \sum \sin 2A } \right)$$

Thus we can see that, all the centres are of the type,
$$K:\left( \frac{ \sum \lambda_{1}x_{1} }{ \sum \lambda_{1} }, \frac{ \sum \lambda y_{1} }{ \sum \lambda_{1} } \right)$$
where K is any of the centres.
Now, $\lambda$ is,

| Centre       | $\lambda$ |
| ------------ | --------- |
| centroid     | 1         |
| orthocentre  | tan A     |
| circumcentre | sin 2A    |
| incentre     | a         | 

Also,
$$\frac{ AK }{ KD } = \frac{ \lambda_{2} + \lambda_{3} }{ \lambda_{1} }$$

![[Pasted image 20230706080321.png]]

## Area
Let coordinates of vertices of triangle ACB are, $A:(x_{1},y_{1}), B:(x_{2},y_{2}), C:(x_{3},y_{3})$.

$$[ABC] = |\Delta|$$
(here the | | means absolute value not determinant)
where,
$$\Delta = \frac{1}{2} 
\begin{vmatrix}
x_{1} & y_{1} & 1 \\
x_{2} & y_{2} & 1 \\
x_{3} & y_{3} & 1 
\end{vmatrix}$$

![[Pasted image 20230706080955.png]]

If points A, B, C are present in anti clockwise directional sense, then the value of $\Delta$ will be +ve. 

If the area is zero, the points are collinear. This is also called *condition for collinearity.*
