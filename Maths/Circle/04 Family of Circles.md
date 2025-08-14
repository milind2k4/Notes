Links: [[01 Equation of a Circle]]
___
# Family of Circles
### Passing through POIs of two Given Circles 
The two circles are $S_{1} = 0$ and $S_{2} = 0$. 

The circles passing through their intersection will be,
$$S_{1} + \lambda S_{2} = 0$$

![[Pasted image 20230717100008.png]]

From the above equation all circles passing through A, B can be obtained except circle $S_{2}$. 

If coefficient of $x^{2}$ in $S_{1}$ and $S_{1}$ is 1, then for $\lambda = -1$ the equation 1 will become linear and will be equation of line AB i.e. common chord of the circles. 
$$AB \equiv S_{1} - S_{2} = 0$$

This also works when the common chord becomes the common tangent, in both the touching internally and externally cases,
![[Pasted image 20230718082712.png]]
![[Pasted image 20230718082702.png]]

$S_{1} - S_{2} = 0$ will represent,
- common cord, if circles are intersecting
- common tangent at common point, if circles touch each other

Maximum possible length of common chord will be equals to the diameter of the smaller circle. In this case the centre of the smaller circle will lie on the common chord, i.e. $S_{1} - S_{2} = 0$. 

![[Pasted image 20230718093939.png]]
![[Pasted image 20230718093949.png]]

### Passing through POIs of Line and Circle
If a circle $S = 0$ and line $L = 0$ intersect at two points A and B, then equation of the circle passing through the points A and B can be given as,
$$S + \lambda L = 0$$

![[Pasted image 20230718094136.png]]

This also works if the line is tangential to the circle,
![[Pasted image 20230718094420.png]]

### Passing through two Points
Equation of circle passing through two points $A:(x_{1},y_{1})$ and $B:(x_{2},y_{2})$ can be given as,

$$(x-x_{1})(x-x_{2}) + (y-y_{1})(y-y_{2}) + \lambda \left( (y-y_{1}) - \frac{ (y_{2}-y_{1}) }{ (x_{2}-x_{1}) }(x - x_{1}) \right) = 0$$

This result is got by taking a circle whose diameter is AB and the line AB and then using the previous result. 

This can be used to find the equation of a circle passing through 3 points. First find a circle passing through any two and then substitute the third point to find $\lambda$. 

![[Pasted image 20230718094948.png]]

### Touching a Line at a Point
If a line L is given then the equation of circle which touches L at a point $A:(x_{1},y_{1})$ can be given as,

$$(x - x_{1})^{2} + (y - y_{1})^{2} + \lambda L = 0$$
This can be found by using the previous result and taking both A and B the same point.