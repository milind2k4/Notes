Links: [[00 Circular Motion]]
___
# Equations of Motions in CM
## Uniform Circular Motion
$\upomega, \alpha$ are vectors. 

When the particle moves with constant angular velocity on the circle. 

$\vec{\upomega} = \text{constant}$
And thus there is no angular acceleration, $\alpha = 0$.

Now, angular displacement,
$$
\begin{split}
\frac{ d\theta }{ dt } &= \upomega \\
\int d\theta &= \int \upomega \, dt \\
\Delta \theta &= \upomega t  
\end{split}
$$

Graphs,
![[Pasted image 20230621130153.png]]

The slope of $\theta-t$ curve is the angular velocity, $\upomega$. 

If a point is performing UCM about centre with angular velocity $\upomega$,  its angular velocity about a point on the circumference will be $\displaystyle \frac{ \upomega }{ 2 }$,
![[Pasted image 20230621134758.png]]

We can also find this result by alternatively,
![[Pasted image 20230621134740.png]]

## Uniformly Accelerated Motion
$\alpha$ is constant. 

Replace the [[01 Equations of Motion#The 7 Equations of Uniform Motion:|corresponding terms]] with their angular counterparts. 
### The 7 equations of motion for Circular Motion
> $$
> \begin{split}
> \upomega &= \upomega_{o} + \alpha t \\
> \Delta \theta &= \upomega_{o} + \frac{ 1 }{ 2 } \alpha t^{2} \\
> \upomega ^{2} &= \upomega_{o}^{2} + 2\alpha \Delta \theta \\
> \Delta \theta &= \upomega t - \frac{ 1 }{ 2 }\alpha t^{2} \\
> \Delta \theta &= \frac{ \upomega + \upomega_{o} }{ 2 }t \\
> \upomega_{avg} &= \frac{ \upomega + \upomega_{o} }{ 2 } \\
> \theta_{n} &= \upomega_{o} + \frac{1}{2}\alpha(2n-1)
> \end{split}
> $$

### Their Proofs
Velocity,
> $$
> \begin{split}
> \frac{ d\upomega }{ dt } &= \alpha \\
> \int  \, d\upomega &= \alpha \int  \, dt \\
> \upomega &= \upomega_{o} + \alpha t  
> \end{split}
> $$

Displacement,
> $$
> \begin{split}
> \frac{ d\theta }{ dt } &= \upomega \\
> \int  \, d\theta &= \int (\upomega_{o} + \alpha t) \, dt \\
> \Delta \theta &= \upomega t + \frac{ 1 }{ 2 }\alpha t^{2} 
> \end{split}
> $$

Eliminating t from the above two,
> $$\upomega ^{2} = \upomega_{o}^{2} + 2\alpha \Delta \theta$$

Eliminating $\upomega_{o}$,
> $$\Delta \theta = \upomega t - \frac{ 1 }{ 2 }\alpha t^{2}$$

Adding both the expressions for angular displacement,
> $$\Delta \theta = \frac{ \upomega + \upomega_{o} }{ 2 }t$$
> $$\upomega_{avg} = \frac{ \Delta \theta }{ t } = \frac{ \upomega + \upomega_{o} }{ 2 }$$

Displacement in nth second,
> $$\theta_{n} = \upomega_{o} + \frac{ 1 }{ 2 }\alpha(2n-1)$$

### Relative Motion

![[Pasted image 20230621135044.png]]

We can do this question by relative angular velocity and acceleration also, just like in the case for rectilinear motion,
![[Pasted image 20230621135142.png]]


## Relation between Linear and Angular Terms

#### Displacement
Angular displacement is $\Delta \theta$. 
Distance travelled is the arc length, which is $d = R\Delta \theta$

Displacement is,
$$s = 2R \sin \frac{ \Delta \theta }{ 2 }$$

![[Pasted image 20230621140122.png]]


#### Speed
Angular speed is,
$$\upomega = \frac{ d\theta  }{ dt }$$

Speed is,
$$v = \frac{ Rd\theta }{ dt }$$
$$v = \upomega R$$
i.e. angular velocity times radius

Vectorially,
$$\vec{v} = \vec{\omega} \times \vec{R}$$

In circular motion, the angle between $\vec{\omega}$ and $\vec{R}$ is 90 and thus,
$$v = \omega R$$

![[Pasted image 20230622131015.png]]