Links: [[00 Projectile Motion]], [[03 Motion Under Gravity]] 
___
# Projection on an Inclined Plane
$\alpha$ is the angle of inclination. 
$\theta$ is angle of projection from the plane (not the ground).

Acceleration due to gravity has a component, $g\sin \alpha$ along the incline in the downward direction and a component $g\cos \alpha$ perpendicular to the incline. 

$g\sin \alpha$ will retard motion up the incline and accelerate motion down the incline. 

![[Pasted image 20230425114807.png]]

## Up the Incline
Assume x-axis along the incline and y-axis perpendicular to it. 

![[Pasted image 20230425120209.png]]

Along x-axis,
> $$
> \begin{split}
> u_{x} &= u\cos \theta \\
> a_{x} &= -g\sin \alpha \\
> \end{split}
> $$

Along y-axis,
> $$
> \begin{split}
> u_{y} &= u\sin \theta \\
> a_{y} &= -g\cos \alpha \\
> \end{split}
> $$


### Time of Flight

> $$T = \frac{2u \sin \theta}{g \cos \alpha} = \frac{2u_{\perp}}{g_{\perp}}$$
$\perp$ means w.r.t plane not ground. 

Using,
> $$
> \begin{split}
> y &= u_{x}t + \frac{1}{2}a_{y}t^{2} \\
> 0 &= (u\sin \theta)t - \frac{1}{2}(g\cos \alpha)t^{2} \\
> T &= \frac{ 2u\sin \theta  }{ g\cos \alpha }
> \end{split}
> $$

### Maximum Height
#### From the Ground
At max height, there will only be the horizontal component of velocity w.r.t ground, i.e. $u\cos(\theta + \alpha)$. 

Thus,
> $$H_{g} = \frac{ u_{v}^{2} }{ 2g } = \frac{ u^{2}\sin ^{2}(\theta + \alpha) }{ 2g }$$
here, $_{v}$ stands for vertical. I.e. velocity in vertical direction w.r.t ground not plane. 


#### From the Plane
Here, the motion is analysed from the perspective of the x and y axes. 

> $$H_{p} = \frac{u^{2} \sin ^{2} \theta}{2g \cos \alpha} = \frac{u_{\perp}^{2}}{2g_{\perp}}$$

Using,
> $$
> \begin{split}
> v_{y}^{2} &= u_{y}^{2} + 2a_{y}y \\
> 0 &= u^{2}\sin ^{2}\theta - 2(g\cos \alpha)y \\
> H_{p} &= \frac{ u^{2}\sin ^{2} \theta }{ 2g\cos \alpha }
> \end{split}
> $$

### Range
 (on the inclined plane)
 
> $$R = \frac{2u^{2}\sin \theta}{g \cos ^{2} \alpha} \cos (\theta + \alpha)$$

Using,
> $$
> \begin{split}
> x &= u_{x}t + \frac{1}{2}a_{x}t^{2} \\
> x &= u\cos \theta \frac{ 2u\sin \theta }{ g\cos \alpha } - \frac{1}{2} g\sin \alpha \frac{ 4u^{2}\sin ^{2}\theta }{ g^{2}\cos ^{2}\alpha } \\
> R &= \frac{ 2u^{2}\sin \theta \cos \theta  }{ g\cos \alpha  } - \frac{ 2u^{2}\sin ^{2}\theta \sin \alpha  }{ g\cos ^{2}\alpha } \\
> R &= \frac{ 2u^{2}\sin \theta }{ g\cos ^{2}\alpha } (\cos \theta \cos \alpha - \sin \theta \sin \alpha) \\
> R &= \frac{ 2u^{2}\sin \theta }{ g\cos ^{2}\alpha } (\cos (\theta + \alpha)) 
> \end{split}
> $$


The range is maximum when we throw the object at
> $$\theta = 45 - \frac{\alpha}{2}$$

![[Pasted image 20230425122551.png]]

Max range is 
> $$R_{max} = \frac{ u^{2} }{ g(1 + \sin \alpha) }$$


## Down the Incline
In this case the parallel component of g will accelerate the motion. 

![[Pasted image 20230425123401.png]]

Along x-axis,
> $$
> \begin{split}
> u_{x} &= u\cos \theta \\
> a_{x} &= g\sin \alpha
> \end{split}
> $$

Along y-axis,
> $$
> \begin{split}
> u_{y} &= u\sin \theta \\
> a_{y} &= -g\cos \alpha
> \end{split}
> $$

### Time of Flight

> $$T = \frac{2u \sin \theta}{g \cos \alpha} = \frac{2u_{\perp}}{g_{\perp}}$$

### Maximum Height 
#### From the Plane
> $$H_{p} = \frac{u^{2} \sin ^{2} \theta}{2g \cos \alpha} = \frac{u_{\perp}^{2}}{2g_{\perp}}$$

### Range
(on the incline)

> $$R = \frac{2u^{2}\sin \theta}{g \cos ^{2} \alpha} \cos (\theta - \alpha)$$

which will be more than that up the plane. 

For max range.
$$\theta = 45^{\circ} + \frac{ \alpha }{ 2 }$$
which is more than that up the plane. 

Max range is,
$$R_{max} = \frac{ u^{2} }{ g(1-\sin \alpha) }$$
which is more than that up the plane.  