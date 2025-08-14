Links: [[07 Tangent and Normal]]
___
# Common Tangents 
1. Direct CT
One for which centres of both the circles lies on same side.
	
	![[Pasted image 20230724094124.png]]

2. Transverse CT 
It is the common tangent of two circles for which centres lie on opposite sides. 
	
	![[Pasted image 20230724094134.png]]

### No. of CT and POIs of two Circles 
##### Disjoint Circles
$$C_{1}C_{2} > r_{1} + r_{2}$$
There will be no common point i.e. no point of intersection. 

There will be 4 CTs, two DCTs and two TCTs. 

![[Pasted image 20230724094602.png]]


##### Externally Touching Circles 
$$C_{1}C_{2} = r_{1} + r_{2}$$

There will be one common point. 

There will be 3 CTs. Two DCTs and one TCT. 

![[Pasted image 20230724094618.png]]

##### Intersecting Circles 
$$|r_{1} - r_{2}| < C_{1}C_{2} < r_{1} + r_{2}$$

The circles will be intersecting at two distinct point and thus there will be 2 common points. 

There will be 2 DCTs. There will be no TCT. 

![[Pasted image 20230724094752.png]]

##### Internally Touching Circles 
$$C_{1}C_{2} = |r_{1} + r_{2}|$$

One circle will touch other circle internally. There will be one common point. 

There will be one CT, which will be DCT. 

![[Pasted image 20230724095000.png]]

##### Contained Circles
$$C_{1}C_{2} < |r_{1} - r_{2}|$$

One of the circles will be contained  by another and there will be no common point. 

There will also be no CT. 

![[Pasted image 20230724095435.png]]

### Direct Common Tangent 
The point of intersection of DCTs lies on the line joining centres and divide them externally in the ratio of radii as,
$$
\begin{split}
\Delta PC_{2}T_{2} &\sim \Delta PC_{1}T_{1} \\
\frac{ PC_{1} }{ PC_{2} } &= \frac{ C_{1}T_{1} }{ C_{2}T_{2} } = \frac{ PT_{1} }{ PT_{2} } \\
\frac{ PC_{1} }{ PC_{2} } &= \frac{ C_{1}T_{1} }{ C_{2}T_{2} } = \frac{ r_{1} }{ r_{2} } \\
\end{split}
$$
Thus,
$$\frac{ PC_{1} }{ PC_{2} } = \frac{ r_{1} }{ r_{2} }$$

$C_{2}T_{2}T_{1}N$ is a rectangle. Thus,
$$T_{1}T_{2} = C_{2}N$$
This is called *length of DCT.*
Which is,
$$T_{1}T_{2} = \sqrt{ (C_{1}C_{2})^{2} - (r_{1} - r_{2})^{2} }$$
This will be defined for the first 4 cases. 

If circles touch each other externally, length of DCTs,
$$
\begin{split}
T_{1}T_{2} &= \sqrt{ (C_{1}C_{2})^{2} - (r_{1} - r_{2})^{2} } \\
&= \sqrt{ (r_{1} + r_{2})^{2} - (r_{1} - r_{2})^{2} } \\
&= 2\sqrt{ r_{1}r_{2} }
\end{split}
$$

Angle between DCTs,
$$2\theta = 2 \sin ^{-1} \left( \frac{ |r_{1} - r_{2}| }{ C_{1}C_{2} } \right)$$

![[Pasted image 20230724100330.png]]

#### Finding DCTs
##### Using Slopes
First find point of intersection of DCTs (i.e. point P) using section formula and the fact that,
$$\frac{ PC_{1} }{ PC_{2} } = \frac{ r_{1} }{ r_{2} }$$
Then find slope of $C_{1}C_{2}$ and then find slope of lines inclined at angle $\theta = \sin ^{-1} \left( \frac{ |r_{1} - r_{2}| }{ C_{1}C_{2} } \right)$ with $C_{1}C_{2}$. 

These slopes will be the slopes of DCTs. 

Now using slopes and point P, find equation of DCTs. 

##### Using [[03 Line and Circle|Tangency Condition]]
Find P as previous. 

Then assume DCT as, $y - y_{P} = m(x - x_{P})$. Now apply tangency condition on this line wrt any of the circles. This will get a quadratic in m, solving which will give the slopes of DCTs. 

Example,
![[Pasted image 20230729080848.png]]
![[Pasted image 20230729081223.png]]

### Transverse Common Tangent 
The POI of TCTs lies on the line joining centres and divides it in the ratio of radii internally. 
Thus P (POI of DCTs) and Q (POI of TCTs) are harmonic conjugate of each other. 

Also, 
$$
\begin{split}
\Delta QT_{1}C_{1} &\sim \Delta QT_{2}C_{2} \\
\frac{ QT_{1} }{ QT_{2} } &= \frac{ QC_{1} }{ QC_{2} } = \frac{ C_{1}T_{1} }{ C_{2}T_{2} } \\
\frac{ QC_{1} }{ QC_{2} } &=  \frac{ r_{1} }{ r_{2} }
\end{split}
$$

In Triangle $\Delta C_{2}C_{1}N$,
$$
\begin{split}
C_{2}N &= \sqrt{ (C_{1}C_{2})^{2} - (C_{1}N)^{2} } \\
&= \sqrt{ (C_{1}C_{2})^{2} - (r_{1} + r_{2})^{2} } \\
&= T_{1}T_{2}
\end{split}
$$

*Length of TCT,*
$$T_{1}T_{2} = \sqrt{ (C_{1}C_{2})^{2} - (r_{1} + r_{2})^{2} }$$

Angle between TCTs,
$$2\theta = 2 \sin ^{-1}\left( \frac{ r_{1} + r_{2} }{ C_{1}C_{2} } \right)$$

![[Pasted image 20230729081305.png]]

#### Finding TCTs
Same as link DCT, except find POI (Q) using internal division instead of external. 

Example,
![[Pasted image 20230729082655.png]]
![[Pasted image 20230729082711.png]]

Another example,
![[Pasted image 20230729083158.png]]
