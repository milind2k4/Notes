Links: [[00 Projectile Motion]], [[01 Equations of Motion]], [[03 Motion Under Gravity]]
___
# Ground to Ground PM

It is when an object is thrown with velocity $u$ making an angle $\theta$ with the ground and it comes back to the ground. 

It is assumed that the earth is flat for small distances.

![[G2G PM.png]]


## Along x-axis
> $$\begin{split}
> a_{x} &= 0 \\
> v_{x} &= u \cos \theta \\
> x &= (u \cos \theta)t
> \end{split}$$

## Along y-axis
(taking up as +ve direction)
> $$\begin{split}
> a_{y} &= -g \\
> v_{y} &= u \sin \theta - gt \\ 
> v_{y}^{2} &= u^{2}\sin ^{2}\theta - 2gy \\
> y &= (u \sin \theta)t - \frac{1}{2}gt^{2} 
> \end{split}$$

### Time of Flight
> $$T = \frac{2 u \sin \theta}{g} = \frac{2u_{y}}{g}$$

Put $y = 0$ in $\displaystyle y = (u \sin \theta)t - \frac{1}{2}gt^{2}$
(or use [[03 Motion Under Gravity#When object is thrown up]])

### Maximum Height
> $$H = \frac{u^{2} \sin ^{2} \theta}{2g} = \frac{u_{y}^{2}}{2g}$$

Put$\displaystyle t = \frac{u \sin \theta}{g}$ into $\displaystyle y = (u \sin \theta)t - \frac{1}{2}gt^{2}$
(or use [[03 Motion Under Gravity#Height Of Ascent]])


### Range
> $$R = \frac{u^{2} \sin 2\theta}{g} = \frac{2u_{x}u_{y}}{g}$$

The displacement along x-axis during time of flight.
Put $\displaystyle t = \frac{2 u \sin \theta}{g}$ into $x = (u \cos \theta)t$

- It is maximum when $\theta = 45 ^{\circ}$ and is equal to $R = u^{2} /g$
- Range when $\theta$ or $(90 - \theta)$ are the same if the velocity is the same, however, the time of flight will be different. 
- *To find angle at which range is max:* Draw two lines, one which is horizontal, one which is opposite to the net acceleration of the object, then the angle at which range is max is the angle bisector of these two lines. 
  
  Below, there are two accelerations, one g vertically down and one g along +ve x axis. The net acceleration is $\sqrt{ 2 }g$ at an angle 45 below the horizontal. We draw a horizontal line and a line along this net acceleration. 
  ![[Pasted image 20230425114021.png]]

If is is said that the ball is moving at and angle $\alpha$ with the horizontal, then that means that it is already in air and

> $$\tan \alpha = \frac{u_{y}}{u_{x}}$$
where $u_{y} = u \sin \theta - gt$  and $u_{x} = u \cos \theta$. 

Relation between H and R,
> $$\frac{H}{R} = \frac{\tan \theta}{4}$$

## Variation of Velocity
Since there is no acceleration along x-axis, 
> $$v_{x} = v\cos \alpha = u\cos \theta$$
Thus,
> $$v = \frac{ u\cos \theta }{ \cos \alpha }$$

Now along y-axis,
> $$
> \begin{split}
> v_{y} &= u_{y} + a_{y}t \\
> v\sin \alpha &= u\sin \theta - gt \\
> v\cos \theta \tan \alpha &= u \sin \theta - gt \\
> t &= \frac{u}{g}(\sin \theta -\cos \theta \tan \alpha)
> \end{split}
> $$

Now, height at which this is the velocity,
> $$
> \begin{split}
> v_{y}^{2} &= u_{y}^{2} + 2a_{y}y \\
> v^{2}\sin ^{2}\alpha &= u^{2}\sin ^{2}\theta - 2gy \\
> u^{2}\cos ^{2}\theta \tan ^{2}\alpha &= u^{2}\sin ^{2}\theta - 2gy \\
> y &= \frac{u^{2}}{2g}(\sin ^{2}\theta - \cos ^{2}\theta \tan ^{2}\alpha)
> \end{split}
> $$

![[Pasted image 20230422120851.png]]


Example,
![[Pasted image 20230422122618.png]]

We can also do this question using vectors,
![[Pasted image 20230422122650.png]]