Links: [[00 Rigid Body Dynamics]], [[00 Dynamics]]
___
# Torque
Torque is analogue of force in rotational motion. 

It is a physical quantity defined as the rotation effect of force. 
It is represented as $\tau$. 
The more is the $\tau$ the more is the change in rotational motion.

If we apply $\tau$ along $\omega$, $\omega$ increases. 
If we apply $\tau$ against $\omega$, $\omega$ decreases. 
If there is no torque there is uniform rotational motion and thus $\omega$ is constant. 

We need torque to change angular velocity. 

Torque depends on the magnitude of force as well as where it is applied and at what angle.
The line along which force acts is called **Line of Action of Force.**

The same force applied farther from the axis will produce more torque.

### Torque about a Point 
The point can be on the body as well as away from it.

$O \to$ point about which $\tau$ is to be calculated
$P \to$ point of application of force
$\vec{r}\to \overline{OP}$ 
$\theta\to$ angle between $\vec{f}$ and $\vec{r}$

Then torque is defined as,
$$\vec{\tau} = \vec{r} \times \vec{f}$$

![[Pasted image 20230712173451.png]]

Magnitude of torque will be,
$$\tau = rf \sin \theta = rf_{\perp} = r_{\perp}f$$
I.e. $\tau =$ (OP)(force perpendicular to OP)
And, $\tau =$ (force)(perpendicular distance of LOAF from O)
This perpendicular distance is also called **Lever Arm.**
![[Pasted image 20230713174204.png]]

If line of action of force passes through point O, then $\tau$ about point O is zero. 

The direction is perpendicular to the plane containing $\vec{r}$ and $\vec{f}$. 
Torque is an axial vector, just like the vectors in [[00 Circular Motion]] .
Its unit is m-N.

## Torque about an Axis
- Take a point O on axis.
- Find torque about this point.
- Component of this torque along the axis is the **Torque About Axis**

#### Force is Parallel to Axis
If force is acting parallel to axis, the torque about axis will be zero.

The torque is perpendicular to the plane of axis and [[05 ME, force Couple and POAF#Point of Application of Force (POAF)|POAF.]]

![[Pasted image 20230713175159.png]]

#### LOAF is passing through Axis
If LOAF passes through any point on the axis, the torque about axis will be zero.

![[Pasted image 20230713175502.png]]

#### Axis and LOAF are skew lines
Torque about point O,
$$\tau_{o} = rF\sin 90^{\circ} = rF$$

Now torque about axis,
$$\tau_{axis} = \tau_{o} \sin \theta$$
$$\tau_{axis} = rF \sin \theta$$

This can be written as,
$$\tau_{axis} = r_{\perp}F$$
Where $r_{\perp}$ is the distance between axis and LOAF.

![[Pasted image 20230713180036.png]]

Example,
![[Pasted image 20230713180602.png]]

### Torque Due to Weight

For a rod, we take element of length dx and at a distance x from the hinge. This element has mass,
$$dm = \frac{ m }{ l }dx$$
On which there is force,
$$df = \frac{ mg }{ l }dx$$

The torque on this element about the hinge will be,
$$d\tau = \frac{ mg }{ l }xdx$$

Thus the torque on the entire rod,
$$
\begin{split}
\tau &= \int_{0}^{l} \frac{ mg }{ l }x \, dx \\
&= \frac{mgl}{2}
\end{split}
$$

Thus about a hinge, torque on a rod will be,
$$\tau = \frac{mgl}{2}$$

![[Pasted image 20230714170056.png]]

This can also be found by assuming all the mass on the COM of rod.
![[Pasted image 20230714170103.png]]

We can assume all the mass to be at the COM for a uniform mass distribution and then find the torque. 
![[Pasted image 20230714170230.png]]

Also, force exerted by the hinge will have no torque because the LOAF of this force will pass through the axis about which we are calculating torque. 

