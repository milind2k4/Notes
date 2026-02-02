Links: [[10 Image formation by Refraction]]
___
# Refraction of Light
Light **changes its velocity and wavelength** when it travels from one medium to another, this phenomenon is known as *Refraction*. 

Generally, the ray bends when it travels from one medium to another. It does not bend when it strikes normally to the interface of two media.

![[Refraction.png]]

### Laws of Refraction
![[Refraction of Light.png]]

1. Incident ray, normal and the refracted ray all lie in the same plane. 
   Mathematically,
	- Let incident ray be $\vec{I}$, reflected ray be $\vec{R}$, and normal be $\vec{N}$
	  then, $(\vec{I} \times \vec{R}) \cdot \vec{N} = 0$
	  This is also called [[05 Scalar Triple Product|Box Product]]. 
2. **Snell's Law:** 
   $$\frac{\sin i}{\sin r} = \frac{v_{i}}{v_{r}}$$
   $$\frac{\sin i}{\sin r} = \frac{c/v_{i}}{c/v_{r}} = \frac{n_{2}}{n_{1}}$$
   $$\therefore n_{1}\sin i = n_{2}\sin r$$

Also,
$$n = \sqrt{ \mu_{r}\varepsilon_{r} }$$
[[00 EM Wave#Speed of EM Wave in Vacuum]]

### Fermat Principle
Light will follow the path along which time taken is least when travelling from one point to another. 

#### Proof of Snell's Law using Fermat Principle
![[Proof Snells law.png]]

$$
\begin{split}
\text{Time taken to travel AB},\\
\\
t & = t_{1} + t_{2}\\
\\
t & = \frac{\sqrt{AC^{2} + x^{2}}}{c/n_{1}} + \frac{\sqrt{DB^{2} + (CD-x)^{2}}}{c/n_{2}}\\
\\
\text{Differentiating t wrt } x, & \\
\\
\frac{dt}{dx} & = \frac{n_{1}}{c} \frac{1}{2} \frac{1}{\sqrt{AC^{2} + x^{2}}} 2x \\
\\
& \phantom{...} + \frac{n_{2}}{c} \frac{1}{2} \frac{1}{\sqrt{BD^{2} + (CD-x)^{2}}} 2(CD-x)(-1) \\
\\
\text{Now, to find a minima,} & \\
\\
\frac{dt}{dx} & = 0 \\
\\
\frac{n_{1}x}{\sqrt{AC^{2} + x^{2}}} & = \frac{n_{2} (CD-x)}{\sqrt{DB^{2} + (CD-x)^{2}}} \\
\\
n_{1}\sin i & = n_{2}\sin r \\
\\
\text{Hence prooved.}
\end{split}
$$
 
## Refraction by Spherical Surface
$$\frac{ n_{2} }{ v } - \frac{ n_{1} }{ u } = \frac{ n_{2}-n_{1} }{ R }$$
$$\frac{ 2 }{ v } - \frac{ 1 }{ u } = \frac{ \Delta  }{ R }$$
$$\frac{ \text{to} }{ v } - \frac{ \text{from} }{ u } = \frac{ \text{diff.}  }{ R }$$
where,
$n_{1} \to$ from
$n_{2} \to$ to
$u \to$ x-coordinate of object
$v \to$ x-coordinate of image
$R \to$ x-coordinate of Centre of Curvature

Any point on the centre of curvature of the curved surface will have its image at CoC. 


#### Proof
![[Refraction at Spherical Surface.png]]

Using sign conventions,
$$\alpha = \frac{ AP }{ R }$$
$$\beta = \frac{ AP }{ -u }$$
$$\phi = \frac{ AP }{ v }$$

Now,
$$i = \alpha + \beta $$
$$r = \phi - \alpha$$
Using Snell's Law,
$$
\begin{split}
n_{1} \sin i &= n_{2}\sin r \\
\text{For small angles,} & \\
n_{1}i &= n_{2}r \\
n_{1}(\alpha+\beta) &= n_{2}(\phi - \alpha) \\
n_{1}\left( \frac{ AP }{ R } + \frac{ AP }{ -u } \right) &= n_{2}\left( \frac{ AP }{ v } - \frac{ AP }{ R } \right) \\
\frac{n_{1}}{R} - \frac{ n_{1} }{ u } &= \frac{ n_{2} }{ v } - \frac{ n_{2} }{ R } \\
\frac{ n_{2} }{ v } - \frac{ n_{1} }{ u } &= \frac{ n_{2}-n_{1} }{ R }
\end{split}
$$
This is the required formula.

### Transverse Magnification

$$m = \frac{ h_{i} }{ h_{o} } = \frac{ n_{1}v }{ n_{2}u }$$

### Longitudinal Magnification
Similar to [[06 Magnification#When object is very small]],

$$
\begin{split}
n_{2} v^{-1} - n_{1} u^{-1} &= \frac{ n_{2}-n_{1} }{ R } \\
\frac{ -n_{2} }{ v^{2} }dv + \frac{ n_{1} }{ u^{2} }du &= 0 \\
dv &= \frac{ n_{1}v^{2} }{ n_{2}u^{2} } du \\
\frac{ dv }{ du } &= \frac{ n_{1}v^{2} }{ n_{2}u^{2} }
\end{split}
$$
Thus longitudinal magnification,
$$m_{l} = \frac{ l_{i} }{ l_{o} } = \frac{ dv }{ du } = \frac{ n_{1}v^{2} }{ n_{2}u^{2} }$$

## Velocity of Image
#### O is moving along PA
$$
\begin{split}
n_{2} v^{-1} - n_{1} u^{-1} &= \frac{ n_{2}-n_{1} }{ R } \\
\frac{ -n_{2} }{ v^{2} } \frac{ dv }{ dt }  + \frac{ n_{1} }{ u^{2} } \frac{ du }{ dt }  &= 0 \\
\frac{ dv }{ dt }  &= \frac{ n_{1}v^{2} }{ n_{2}u^{2} } \frac{ du }{ dt } \\
v_{i} &= \frac{ n_{1}v^{2} }{ n_{2}u^{2} } v_{o} \\
v_{i} &= m_{l} v_{o}
\end{split}
$$
Thus velocity of image,
$$v_{i} = \frac{ n_{1}v^{2} }{ n_{2}u^{2} } v_{o} = m_{l} v_{o}$$

#### O is moving $\perp$ PA
The x coordinates of image and object do not change. 

$$
\begin{split}
\frac{ y_{i} }{ y_{o} } &= m_{t} = \frac{ n_{1}v }{ n_{2}u } \\
\frac{ dy_{i} }{ dt } &= \frac{ n_{1}v }{ n_{2}u } \frac{ dy_{o} }{ dt } \\
v_{i} &= \frac{ n_{1}v }{ n_{2}u } v_{o} \\
v_{i} &= m_{t} v_{o} 
\end{split}
$$





