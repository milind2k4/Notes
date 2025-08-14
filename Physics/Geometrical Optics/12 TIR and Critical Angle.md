Links: [[09 Refraction of Light]]
___
# Total Internal Reflection and Critical Angle 
#important 

Only occurs when the ray goes from denser to rarer medium.

$$n_{d} > n_{r}$$

When we keep increasing the angle of incidence, there comes a point when the angle of refraction is 90. This angle of incidence is called the **Critical angle.** And the refracted ray grazes the surface of t he denser medium. 

Critical angle is,
$$\sin c = \frac{ n_{r} }{ n_{d} }$$

![[Pasted image 20230221172627.png]]

When the angle of incidence is more than the critical angle, refraction does not happen and the incident ray is reflected back into the the denser medium. This is called **Total Internal Reflection.**

This follows laws of reflection. 

![[Pasted image 20230221172924.png]]

Check TIR in questions where ray goes from rarer to denser medium. 

## Graph between $\delta$ and $i$
$\delta$ between 90 - c and 180 - 2c will occur for only one angle of incident. 
$\delta$ between 0 and 90 - c will occur for two angles of incident.  


![[original_20(b)(14-4-21).jpg]]
![[Pasted image 20230512132904.png]]

## Circle of Illuminance
If there is a source of light in the denser medium, the observer in the rarer medium observes the light coming out of a circle on the surface. This circle is called the *circle of illuminance.*

![[Pasted image 20230513122437.png]]

The radius of this circle,
$$
\begin{split}
R &= H \tan c\\
&= \frac{ H }{ \sqrt{ n^{2} -1} }
\end{split}
$$

Area of the circle,
$$A = \frac{ \pi H^{2} }{ n^{2}-1 }$$

![[Pasted image 20230513122457.png]]

If the outer medium is not air,
$$R = H \tan c = \frac{H n_{r} }{\sqrt{ n_{d}^{2}-n_{r}^{2} }}$$
Area,
$$A = \frac{ \pi H^{2} n_{r}^{2} }{ n_{d}^{2} - n_{r}^{2} }$$

![[Pasted image 20230513123152.png]]

## Optical Fibres
It is used to transmit EM waves from one place to another with minimum loss. (attenuation). It makes use of TIR to keep the ray of light carrying info inside. 

It is very thin transparent wire $(r \sim \mu m)$, and is made of glass or polymer. 

It is mainly used in telecommunication. EM wave enters from one cross section and exits from the other. All the incidences on curved surface should be TIR. 

$$
\begin{split}
\sin i &= n \sin r \\
i' &> c \\
\sin i' &> \sin c \\
\sin (90-r) &> \sin c \\
\cos r &> \sin c \\
\sqrt{ 1 - \sin ^{2}r } &> \frac{ 1 }{ n } \\
\sqrt{ 1 - \frac{ \sin ^{2}i }{ n^{2} } } &> \frac{1}{n} \\
n^{2} &> 1 + \sin ^{2}i \\
\end{split}
$$

The max value of $\sin ^{2}i$, is 1 and thus, if 
$$n > \sqrt{ 2 }$$
then at any value of $i$ the ray will only enter and exit through the ends. 

![[Pasted image 20230513123900.png]]
(here the angle of incident on the wall is $i'$ not $i$)

**Numerical Aperture of OF:** it is the max value of $\sin i$ i.e. $\sin i_{max}$. 

