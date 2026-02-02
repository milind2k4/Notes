Links: [[00 Differentiation]]
___
# Application of Differentiation

## [[01 Tangents and Normals]]


## Angle Between Curves
[[00  Circle#Orthogonal Intersection]]
[[04 Line, Line and Line, Point#Angle between two lines]]
aka Angle of Intersection

It is defined as the angle between their tangents at their point of intersection. 

![[Pasted image 20230824151637.png]]

To find angle of intersection between two curves,
1. Solve them to find point of intersection. 
2. Find dy/dx at P for both the curves (say $m_{1},m_{2}$).
3. Required angle of intersection at P is,
   $$\theta = \tan ^{-1} \left| \frac{ m_{1} - m_{2} }{ 1 + m_{1}m_{2} } \right| $$


If $m_{1}.m_{2} = -1$, then intersection is orthogonal (i.e. 90$^{\circ}$) and the curves are said to intersect orthogonally at the point.

Two curves are called **orthogonal** curves if they *intersect at 90$^{\circ}$* at each of their point of intersections.

If while solving for point of intersection, we get very complicated equation, then either the solution can be found using hit and trial or the point of intersection is not needed, in which case, assume POI as $(x_{1},y_{1})$ and then calculate angle in terms of $x_{1},y_{1}$.


#### Touching Curves
To show that two curves touch each other at some point (say P), show that the tangent is the same
I.e. **both curves have same value of dy/dx at that point.**

![[Pasted image 20230824164613.png]]

If tangent to a curve which has polynomial equation in x and y is solved with the curve itself, then corresponding to the point of contact, **repeated roots will be obtained.** 

If degree of curve is even, then there will be even number of repetitions of root (at least 2). 

If degree of curve is odd, then there will be odd number of repetitions of root (at least 3).

![[Pasted image 20230824154200.png]]

![[Pasted image 20230824155228.png]]

## [[02 Rate Change]]

## [[03 Approximations and Error]]

## [[04 Monotonicity]]

## [[05 Maxima and Minima]]

## [[06 Solving and Proving Inequalities]]

## [[07 Concavity and Curve Sketching]]

## Distance between Curves 
If P is a fixed point and Q is a variable point on the curve $y = f(x)$ then local min. or local max. distance between the points P and Q will occur when PQ is normal to the curve. 

![[Pasted image 20230916094610.png]]

The local min. or max. distance between curves is obtained along common normal. 

![[Pasted image 20230916094626.png]]

Drawn tangents at $P_{o}, Q_{o}$ will be parallel. 

If curves are intersecting, then min. distance between them will be zero. 

If any one of the curve goes to infinity, then max. distance will not exist. 

#### To find min. distance
If one curve is a straight line, 
- Find point where drawn tangent is parallel to the line. 
- Find length of perpendicular from this point to line. 

If one of the curve is circle,
- Assume a point on other curve in parametric form (if possible), say P.
- Write equation of normal at P and substitute coordinates of centre of circle. 
- This will give coordinates of P.
- Find required min. or max. distance. 


If both curves are general,
- Assume a point on each of the curves and then write equation of normal at each curve and then we can compare coefficients to find points. 
- Then find the distance using distance formula. 

### Triangle Inequality
If A, B are fixed points, and P is a variable point, then
$$PA + PB \geq AB$$

Equality holds when P lies on line segment AB. 

![[Pasted image 20230916094703.png]]

$$|PA - PB| \leq AB$$
Equality holds when P lies outside line segment AB on the line AB.

![[Pasted image 20230916094723.png]]
![[Pasted image 20230916094740.png]]

## Examples: Distance between Curves 


![[Pasted image 20230916094814.png]]

![[Pasted image 20230916094902.png]]
![[Pasted image 20230916094918.png]]

![[Pasted image 20230916094934.png]]

![[Pasted image 20230916094949.png]]
![[Pasted image 20230916095001.png]]

#important 
![[Pasted image 20230916095018.png]]
![[Pasted image 20230916095031.png]]
![[Pasted image 20230916095050.png]]

## [[08 Rolle's Theorem and LMVT]]

## [[09 Cubic Analysis]]

