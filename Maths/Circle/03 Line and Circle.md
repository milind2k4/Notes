Links: [[00  Circle]]
___
# Line and Circle 
 (Tangency condition and Equation of Tangent are #removed from jee 24)

For points of intersection of,
$$x^{2} + y^{2} = r^{2}\ \&\ y = mx + c$$
We get a quadratic,
$$(1+m^{2})x^{2} + 2cmx + c^{2} - r^{2} = 0$$
Whose D is,
$$
\begin{split}
D &=  4c^{2}m^{2} - 4(1+m^{2})(c^{2}-r^{2}) \\
&= 4(r^{2}(1+m^{2})-c^{2})
\end{split}
$$

- If D < 0, the circle and line do not intersect. 
- If D = 0, the line will be a tangent to circle.
	$$c^{2} = r^{2}(1 + m^{2})$$
	This is called **Tangency Condition.** But this is only valid for standard circle (centre at origin).
	For general circle, use $p = r$ for tangency condition.
	$\\$

- If D > 0, the line will be chord and there will be two distinct points of intersection. The length of chord will be,

	$$
	\begin{split}
	AB &= \frac{ \sqrt{ D } }{ a } \sqrt{ 1 + m^{2} } \\
	&= \frac{ \sqrt{ 4(r^{2}(1+m^{2}) - c^{2}) } }{ 1 + m^{2} } \sqrt{ 1 + m^{2} } \\
	&= 2 \sqrt{ r^{2} - \frac{ c^{2} }{ 1 + m^{2} } } \\
	&= 2 \sqrt{ r^{2} - p^{2} }
	\end{split}
	$$
	
	Since centre of circle is at origin, the perpendicular p comes out to be,
	$$p = \frac{ c }{ \sqrt{ 1 + m^{2} } }$$


To find the equation of tangent at a point, we use tangency condition and put c from it into the equation of line,
$$y = mx \pm r\sqrt{ 1 + m^{2} }$$
which is only valid for standard circle. 

However, for general circle, 
$$(x-a)^{2} + (y - b)^{2} = r^{2}$$
we can used [[00 Straight Line#Shift of Origin|shift of origin]]. 
$$(y - b) = m(x - a) \pm r\sqrt{ 1 + m^{2} }$$

If the tangent given by 
$$y = mx \pm r\sqrt{ 1 + m^{2} }$$
passes through h, k then put h, k in it to find slope m. 
$$
\begin{split}
k &= mh \pm r\sqrt{ 1 + m^{2} } \\
k^{2} + m^{2} h^{2} - 2hkm &= r^{2}(1 + m^{2}) \\
(h^{2} - r^{2})m^{2} - 2hkm + k^{2} - r^{2} &= 0
\end{split}
$$
Now this is a quadratic in m with roots, $m_{1}, m_{2}$. These two values of m tells us that there are a maximum of 2 tangents which can be drawn from point. 
$$m_{1} + m_{2} = \frac{ 2hk }{ h^{2} - r^{2} }$$
$$m_{1} m_{2} = \frac{ k^{2} - r^{2} }{ h^{2} - r^{2} }$$

- If point lies outside, there will be two tangents and D > 0.
- If point lies on the curve, there will be one tangent and D = 0.
- If point lies inside, there will be zero tangents and D < 0. 


If in a question slopes of tangents from a point are related then we should think of equation. 
$$(h^{2} - r^{2})m^{2} - 2hkm + k^{2} - r^{2} = 0$$

If h = r or -r, equation will become linear as in this case one of the tangents will be vertical and hence will have undefined slope (which cannot be solved from any equation) and equation will give slope of non vertical tangent. 

If the equation is solved, we will get two values of slopes (say $m_{1},m_{2}$). Now for these two values, we will get 4 lines from,
$$y = mx \pm r\sqrt{ 1 + m^{2} }$$
Out of which only 2 will pass through point P. One corresponding to $m_{1}$ and other to $m_{2}$. The remaining 2 lines will not pass through P.

![[Pasted image 20230722091834.png]]

Thus we do not use the above equation. We can directly use [[02 Equation of a Line#Slope Point form]].

If tangents drawn from P are mutually perpendicular then,
$$
\begin{split}
m_{1} m_{2} &= \frac{ k^{2} - r^{2} }{ h^{2} - r^{2} } \\
-1 &= \frac{ k^{2} - r^{2} }{ h^{2} - r^{2} } \\
h^{2} + k^{2} &= 2r^{2} \\
\text{Now, putting h, k as x, y,} \\
x^{2} + y^{2} &= 2r^{2}
\end{split}
$$
This is the equation of **Director Circle.**
[[06 Results in Circle using Geometry#Tangent including a Constant Angle from a variable Point]]
