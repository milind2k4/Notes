Links: [[03 Magnetic Force on Charge]]
___
# Motion of Charged Particle in Uniform Field
Some important charged particles,
![[Pasted image 20240112211742.png]]

#### Velocity is parallel to Field
If velocity is along field, i.e. $\theta = 0$, there is no force, $f_{m} = 0$.

Thus the particle will keep travelling in the same direction with the same velocity. I.e. straight line uniform motion. 

If velocity is against field, i.e. $\theta = 180$, there is no force, $f_{m} = 0$.

Thus the motion will be straight line uniform motion.

![[Pasted image 20240112205311.png]]

#### Velocity is perpendicular to Field
Here, $\theta = 90^{\circ}$.

Now, the magnetic field will be in the plane of the screen. Thus the motion of particle is 2d. 

The force will be perpendicular to the velocity, and thus the motion will be uniform circular motion. 

The magnitude of the force will be,
$$f_{m} = qvB$$

![[Pasted image 20240112210238.png]]

The magnetic force will act as centripetal force. 
$$
\begin{split}
qvB &= \frac{mv^{2}}{R} \\
R &= \frac{ mv }{ qB } 
\end{split}
$$
Thus the radius of the circle will be,
$$R = \frac{ mv }{ qB } = \frac{ p }{ qB }$$

In terms of kinetic energy K,
$$R = \frac{ \sqrt{ 2mK } }{ qB }$$

Now, if q charge is accelerated through potential difference V, it means that its kinetic energy is increased by qV. 

Thus, we can write,
$$R = \frac{ \sqrt{ 2mqV } }{ qB }$$

![[Pasted image 20240112211134.png]]

For the circular motion, we can find all the regular terms. 

Angular velocity,
$$\omega = \frac{v}{R} = \frac{qB}{m}$$

Time period, 
$$T = \frac{2\pi}{\omega} = \frac{2\pi m}{qB}$$
which is independent of velocity. This is because  as we increase v, R also increases.

Frequency,
$$f = \frac{1}{T} = \frac{qB}{2\pi m}$$

![[Pasted image 20240112212659.png]]

![[Pasted image 20240112213023.png]]

#### Velocity is not perpendicular nor parallel to Field 
If the field is along x axis, the force will be in yz plane. 

We break the velocity into two components. 

The velocity along x axis will not change and thus the motion will be uniform. 

And we can write,
$$
\begin{split}
x &= v\cos \theta t \\
v_{x} &= v\cos \theta \\
a_{x} &= 0
\end{split}
$$

![[Pasted image 20240112213618.png]]

The velocity along y axis will change due to the magnetic force. Thus the motion in yz plane will be circular. 

The radius of which will be,
$$R = \frac{ m(v\sin \theta) }{ qB }$$
The centre of this circular motion will be somewhere on the -z axis. Thus the x axis act as a tangent to the motion. 

We can write,
$$
\begin{split}
y &= R\sin \omega t \\
v_{y} &= v\sin \theta \cos \omega t = \frac{ dy }{ dt } \\
a_{y} &= - \omega^{2} R \sin \omega t = \frac{ dv_{y} }{ dt }
\end{split}
$$
And,
$$
\begin{split}
z &= -(R - R \cos \omega t) \\
v_{z} &= -v\sin \theta \sin \omega t  = \frac{ dz }{ dt } \\
a_{z} &= -\omega^{2}R \cos \omega t = \frac{ dv_{z} }{ dt }
\end{split}
$$

![[Pasted image 20240112214659.png]]

Finally, the motion of the particle will be **helical.**

![[Pasted image 20240112214922.png]]

The distance travelled along x axis in one time period is called the **Pitch.** It is given as,
$$p = v_{x} T = v\cos \theta\frac{ 2\pi m}{qB}$$
It will be uniform as the velocity along x axis is constant. 

The particle will touch x axis at (np, 0, 0) after every T.