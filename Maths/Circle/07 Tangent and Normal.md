Links: [[01 Equation of a Circle]]
___
# Tangent and Normal

### Tangent
Equation of tangent to the circle $x^{2} + y^{2} = r^{2}$ can be given as,

- At point $P:(x_{1},y_{1})$ on the circle,
  $$xx_{1} + yy_{1} = r^{2}$$

- At point $\theta$, $P:(r\cos \theta, r\sin \theta)$ on the circle,
	$$x\sin \theta + y\sin \theta = r$$

- With slope m,
	$$y = mx \pm r\sqrt{ 1 + m^{2} }$$
	To find the point of contact, assume it as $(x_{1},y_{1})$. Write equation of tangent,
	$$x x_{1} + yy_{1} = r^{2}$$
	Then compare coefficients. 

	$$\frac{ x_{1} }{ m } = \frac{ y }{ -1 } = \frac{ \pm r }{  \sqrt{ 1 + m^{2} } }$$
	Giving,
	$$x_{1} = \pm \frac{ rm }{ \sqrt{ 1 + m^{2} } }$$
	$$y_{1} = \mp \frac{ r }{ \sqrt{ 1 + m^{2} } }$$

	![[Pasted image 20230724081420.png]]
	$\\$

##### Point of Intersection of Tangents drawn at $\theta_{1}$ and $\theta_{2}$ 

$$K: \left( \frac{ r\cos \left( \frac{ \theta_{1} + \theta_{2} }{ 2 } \right) }{ \cos \left( \frac{ \theta_{1} - \theta_{2} }{ 2 } \right) }, \frac{ r\sin \left( \frac{ \theta_{1} + \theta_{2} }{ 2 } \right) }{ \cos \left( \frac{ \theta_{1} - \theta_{2} }{ 2 } \right) } \right)$$

Tangent at P,
$$T_{P} = x\sin \theta_{1} + y\sin \theta_{1} = r$$
Tangent at Q,
$$T_{Q} = x\sin \theta_{2} + y\sin \theta_{2} = r$$

Solving for x and y, by eliminating (cross multiplying their coefficients and subtracting) we get the above point. 

Alternatively, 
Take $K:(a,b)$. Now for K, PQ will be chord of contact,
$$PQ \equiv ax + by = r^{2}$$

Also, PQ is chord joining $\theta_{1}$ and $\theta_{2}$ on the circle,
$$PQ \equiv x \cos\left( \frac{ \theta_{1} + \theta_{2} }{ 2 } \right) + y \sin \left( \frac{ \theta_{1} + \theta_{2} }{ 2 } \right) = r \cos \left( \frac{ \theta_{1} - \theta_{2} }{ 2 } \right)$$

Comparing coefficients,
$$\frac{ a }{ \cos\left( \frac{ \theta_{1} + \theta_{2} }{ 2 } \right) } = \frac{ b }{ \sin\left( \frac{ \theta_{1} + \theta_{2} }{ 2 } \right) } = \frac{ r^{2} }{ r \cos\left( \frac{ \theta_{1} - \theta_{2} }{ 2 } \right) }$$
Thus giving K.

### Normal 
To find equation of normal at point P on the circle, simply find equation of line joining centre and the point. 

If equation of tangent to a circle is given then to find point of tangency we can,

- Assume $P:(h,k)$, write T = 0 and then compare coefficients with given line. 
- Using slope of tangent we can find slope of normal and hence its equation (using centre). Now solve tangent and normal for point of intersection and thus point of tangency.
- Find  [[04 Line, Line and Line, Point#Foot and Length of Perpendicular|foot of perpendicular]] from centre to the line. This point will be the point of tangency.