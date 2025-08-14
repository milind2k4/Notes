Links: [[00 Straight Line]], [[02 Equation of a Line]], [[07 Tangent and Normal]]
___
# Tangents and Normals
Equation to the tangent of a curve, $f(x,y) = 0$ at point  $P(x_{1},y_{1})$ can be given as,
$$y - y_{1} = \left. \frac{ dy }{ dx } \right|_{(at\ P)}  (x - x_{1})$$

Similarly, equation of normal can be given as,
$$y - y_{1} = \left. -\frac{ dx }{ dy } \right|_{(at\ P)}  (x - x_{1})$$

As, normal is the line perpendicular to the tangent at the point of tangency.

In equation of tangent, for diff. at point P, we can use differentiation or [[00 Differentiation#First Principle of Differentiation|first principle.]]

Find the limiting value of dy/dx if it becomes undefined or if fluctuates, then use first principle when we substitute coords of P) 

If curve is defined parametrically, then to find diff. use parametric differentiation.

If dy/dx $\to 0$ then tangent will be horizontal, and normal will be vertical. In this case,
$$T_{P} \equiv y = y_{1}$$
$$N_{P} \equiv x = x_{1}$$

If dy/dx $\to \pm \infty$ then tangent will be vertical and normal horizontal,
$$T_{P} \equiv x = x_{1}$$
$$N_{P} \equiv y = y_{1}$$

![[Pasted image 20230823154604.png]]
![[Pasted image 20230823154630.png]]

If a point $P(h,k)$ is assumed on the curve, then substitute it in the equation of the curve. 

If a line is equally inclined with both axes, then its slope will be $\pm 1$. If a line makes equal intercepts with both axes, then slope will be -1. However, if the lengths of intercepts are equal, then slope will be $\pm 1$

y-intercept of tangent is called initial ordinate. 

#### Parametric Point

| Curve                                                     | Parametric Point                               |
| --------------------------------------------------------- | ---------------------------------------------- |
| $$x^{2} + y^{2} = r^{2}$$                                 | $$(r\cos \theta,r\sin \theta)$$                |
| $$\frac{ x^{2} }{ a^{2} } + \frac{ y^{2} }{ b^{2} } = 1$$ | $$(a\cos \theta, b\sin \theta)$$               |
| $$y^{2} = 4ax$$                                           | $$(at^{2}. 2at)$$                              |
| $$\frac{ x^{2} }{ a^{2} } - \frac{ y^{2} }{ b^{2} } = 1$$ | $$(a\sec \theta, b\tan \theta )$$              |
| $$x^{2} = 4by$$                                           | $$(2bt, bt^{2})$$                              |
| $$ax + by + c = 0$$                                       | $$\left( t, \frac{ at + c }{ b } \right)$$     |
| $$\frac{ x^{n} }{ a^{n} } + \frac{ y^{n} }{ b^{n} } = 1$$ | $$(a\cos ^{2/n}\theta, b\sin ^{2/n}\theta)$$   |
| $$x^{m}y^{n} = a^{m+n}$$                                  | $$\left( at^{n}, \frac{ a }{ t^{m} } \right)$$ |
| $$x^{2}y^{2} = x^{2} + y^{2}$$                            | $$(\csc \theta, \sec \theta)$$                   |
| $$x^{2/3} + y^{2/3} = a^{2/3}$$                           | $$(a\cos ^{3} \theta, a\sin ^{3}\theta)$$                                               |

Parametric point is used to reduce number of variables. 
By eliminating the parameter, we get the cartesian equation of the curve. 
For every point, value of parameter is unique. 

We can make parametric form of any curve,

![[Pasted image 20230823162400.png]]

If tangent drawn at point $P(a,b)$ passes through point $Q(x_{1},y_{1})$, then,
$$
\begin{split}
m_{PQ} &= m_{PQ} \\
\left. \frac{ dy }{ dx }  \right|_{at\ P} &= \frac{ y_{Q} - y_{P} }{ x_{Q} - x_{P} } \\
&= \frac{ y_{1} - b }{ x_{1} - a_{0} }
\end{split}
$$

#### Some definitions
For point P on the curve, we define,
**Length of Tangent:** PT
**Length of Normal:** PN
**Subtangent:** TQ = $\displaystyle PQ\cot \theta =  \left| \frac{ y }{ y' } \right|$
**Subnormal:** QN = $PQ \tan \theta = | yy' |$

Length of normal,
$$
\begin{split}
PN &= PQ \sec \theta \\
&= |y\sqrt{ 1 + (y')^{2} }|
\end{split}
$$

Length of tangent,
$$
\begin{split}
TQ &= PQ\csc \theta \\
&= \left| y\sqrt{ 1 + \frac{ 1 }{ (y')^{2} } } \right|
\end{split}
$$

![[Pasted image 20230823161024.png]]

#### Tangent at Point and Tangent through Point 
In the first case, the point lies on the curve and for slope, use diff. 

In the second case it could be that the point is on the curve, or it is not on curve. Also, it could be that the point is on the curve, but the tangent is at another point.

![[Pasted image 20230823155155.png]]

![[Pasted image 20230823170455.png]]

## Condition for Tangency and Normalcy
If a line L and a curve $f(x,y)$ are given, then to find the condition for L being tangent (or normal) of the curve,
1. Assume a parametric point on the curve.
2. Write equation of tangent (or normal) at this point. 
3. Compare coefficients of line obtained in 2 and L. 
4. Eliminate the parameter. The eliminant will be the required condition. 

If parametric point is complicated, then assume point as $(x_{1},y_{1})$ and satisfying it with equation of curve will give one extra equation. 
The remaining process is the same and we eliminate $x_{1},y_{1}$.

In case curve is conic i.e. 2 degree polynomial equation, the tangency condition can also be obtained by solving L with given curve and then the quadratic formed by doing so in x or in y.
This quadratic will have repeated roots corresponding to point of tangency and thus we make $D = 0$ for condition. 

The condition may come out to be complicated.
![[Pasted image 20230824151149.png]]
![[Pasted image 20230824151206.png]]

![[Pasted image 20230824164258.png]]
