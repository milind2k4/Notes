Links: [[01 Equations of Motions in CM]]
___
# Circular Motion
If a point P is moving in a plane such that its separation from a point C is always constant then P is said to be doing Circular Motion about C. C is called Centre and the distance between C and P is radius R. C may or may not be moving itself. 

Wrt C, P has no velocity of separation or approach. Thus all the velocity of P is perpendicular to R. 

### Definitions
#### Angular Position ($\theta$)
It tells the position of particle on the circle. It is generally taken in radian, which is its SI unit. It has no dimensions. 
  
Anticlockwise is taken +ve and clockwise is taken -ve. 

#### Angular Displacement ($\Delta \theta$)
It is the change in angular position. Its unit is radian. 
  
Finite *$\Delta \theta$ is scalar* and if it is infinitely small, i.e. *$d\vec{\theta}$, then it is vector.* This is because $d\vec{\theta}$ follows vector algebra.

Direction of $d\vec{\theta}$ is anticlockwise or clockwise. Mathematically it is outside or inside the plane depending on the direction of motion, use the right hand rule (vector cross product). 

Thus, angular displacement is an axial vector. 
![[Pasted image 20230620125326.png]]

![[Pasted image 20230620125528.png]]


#### Angular Velocity ($\omega$)
Its unit is $\ce{ rad s^{-1} }$ and dimensions are $\ce{ [T^{-1}] }$.

Angular speed is the magnitude of angular velocity, $|\omega|$

It is also defined as,
$$\omega = \frac{ v_{\perp} }{ r }$$
where $v_{\perp}$ is the velocity perpendicular to the line joining the points and $r$ is the length of the line. 

##### Average Angular Velocity ($\upomega_{avg}$)
Rate of change of angular displacement, defined for finite time interval. 

$$\omega_{avg} = \frac{ \Delta \theta }{ \Delta t }$$

It is a scalar. 

The time taken for one complete rotation is **Time Period** and in this interval the angular velocity is,
$$\omega_{avg} = \frac{ 2\pi }{ T }$$
Giving Time period,
> $$T = \frac{ 2\pi }{ \omega_{avg} }$$

The number of cycles per second is **Frequency** and it is,
> $$f = \frac{ 1 }{ T }$$
> Unit is $s ^{-1}$ which is also written as Hertz (Hz) or CPS, cycles per seconds. 

##### Instantaneous Angular Velocity ($\omega$)
(or Angular Velocity)
Rate of change of instantaneous angular displacement. Defined for an instant. 
$$\omega = \frac{ d\vec{\theta} }{ dt } $$

Since $d\vec{\theta}$ is axial vector, $\vec{ \upomega }$ is also axial vector with direction the same as that of $d\vec{\theta}$. 


#### Angular Acceleration ($\vec{\alpha}$)
Rate of change of Angular Velocity.

It is a vector with unit $\ce{ rad s^{-2} }$.

##### Average Angular Acceleration ($\vec{\alpha}_{avg}$)
Defined for finite time interval. 
$$\vec{\alpha}_{avg} = \frac{ \Delta\vec{\omega} }{ \Delta t }$$

Its direction is along the change in angular velocity, and thus it is an axial vector. 

It is zero in uniform circular circular. 

##### Instantaneous Angular Acceleration ($\vec{\alpha}$)
(or Angular Acceleration)
Defined for an infinitely small interval. 

$$\vec{\alpha} = \frac{ d\vec{\omega} }{ dt } $$

If $\vec{\alpha}$ is parallel to $\vec{\omega}$, $|\vec{\omega}|$ increases. 
If $\vec{\alpha}$ is anti-parallel to $\vec{\omega}$, $|\vec{\omega}|$ decreases. 

Now, 
$$
\begin{split}
\vec{\alpha} &= \frac{ d\vec{\omega} }{ dt } . \frac{ d\vec{\theta} }{ d\vec{\theta} } \\
\vec{\alpha} &= \vec{\omega} \frac{ d\vec{\omega} }{ d\vec{\theta} } 
\end{split}
$$
Similar to acceleration in rectilinear motion. 


## Radius of Curvature
A particle moving on a curve moves on an imaginary circle whose arc is part of the curve. 
The circle is called **Circle of Path**, its radius is called *Radius of Curvature* and its centre is called *Centre of Curvature.*

The sharper the curve is the smaller is RoC. 

![[Pasted image 20230623113451.png]]

RoC of a random point on a random path, 
$$
\begin{split}
a_{\perp} &= a_{c} \\
&= \frac{ v^{2} }{ R_{c} } \\
R_{c} &= \frac{ v^{2} }{ a_{\perp} }\\
&= \frac{ \text{(speed)}^{2} }{ \text{component of a } \perp \text{to } v }
\end{split}
$$

If the particle is moving on a path given by $y = f(x)$,

$$R = \frac{\displaystyle \left[ 1 + \left( \frac{ dy }{ dx } \right)^{2} \right]^{\Large \frac{3}{2}}}{ \displaystyle \frac{ d^{2}y }{ dx^{2} } }$$
$$R = \frac{ [1 + (f')^{2}]^{3/2} }{ f'' }$$

## Effect of Earth's Rotation on g
The earth rotates from west to east. 
We can write this $\omega$ as,
$$\omega = \frac{ 2\pi }{ 24 \times 3600 }$$

The $\theta$ form the equator is called *Latitude* and the angle $90 - \theta$ from the pole is called *Co-Latitude.*

The radius of the circle for a particle at an angle $\theta$ from the equator is $r = R\cos \theta$. 

Now, if we make the FBD of the particle with rotating frame of reference, since we are observing from the frame of the object, there will be a centrifugal force on the object. 

![[Pasted image 20230629120139.png]]

$$mg = mg + m\omega^{2}R\cos ^{2} \theta$$
$$N = mg - mR\omega^{2} \cos ^{2} \theta$$

This normal is the apparent weight of the object. 

We can write this normal in terms of g effective,
$$mg_{eff}= mg - m\omega^{2}R\cos ^{2} \theta$$
$$g_{eff} = g - \omega^{2}R \cos ^{2} \theta$$

Thus at the equator, the $g_{eff}$ and apparent weight is the least,
$$g_{eff} = g - \omega^{2}R$$
$$N = mg - m\omega^{2}R$$

And at the pole, there will be no effect and the $g_{eff}$ and apparent weight will be the max.,
$$g_{eff} = g$$
$$N = mg$$

For something to fly off, N or $g_{eff}$ should be zero. 