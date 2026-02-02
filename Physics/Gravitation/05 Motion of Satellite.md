Links: [[03 Planetary Motion]]
___
# Motion of Satellite 
It is just like [[03 Planetary Motion]], except here we consider the planet to be fixed. 

The velocity with which satellite does UCM around the earth is called its *Orbital Velocity, $v_{o}$.*

$$
\begin{split}
\frac{ GMm }{ r^{2} } &= \frac{ mv_{o}^{2} }{ r } \\
v_{o} &= \sqrt{ \frac{ GM }{ r } }
\end{split}
$$

Here, the escape velocity comes out to be,
$$v_{e} = \sqrt{ \frac{ 2GM }{ r } }$$

Thus we can say that,
$$v_{o} = \frac{ v_{e} }{ \sqrt{ 2 } }$$

The angular velocity and time period is,
$$
\begin{split}
\omega &= \sqrt{ \frac{ GM }{ r^{3} } } \\
T &= 2\pi \sqrt{ \frac{ r^{3} }{ GM } }
\end{split}
$$
which is the same as planetary motion. 

![[Pasted image 20231219112032.png]]

#### Energy of System
Kinetic energy of the system is,
$$K = \frac{ GMm }{ 2r }$$

Potential energy is,
$$U = \frac{ -GMm }{ r }$$

And total energy is,
$$TE = \frac{ -GMm }{ 2r }$$

The -ve indicates that the system is bounded. 

![[Pasted image 20231219112051.png]]

Now, to bring the satellite to $\infty$ again the attractive force, we will have to provide the system with energy. This energy is called the system's **Binding Energy.** BE is -ve of TE. 

### Geostationary Satellite 
Which do not appear to be moving. 

They have the same $\omega$ and T as of earth. 

Earth has $\omega$,
$$\omega = \frac{ 2\pi }{ 24 \times 60 \times 60 }\ \ce{ rad/s }$$

The satellite needs to have the same sense of rotation (moves from west to east) and it should be on the equatorial plane. 

Now the $\omega$ of the satellite will be the same as that of earth,
$$
\begin{split}
\omega_{s} &= \frac{ v_{o} }{ r } \\
\sqrt{ \frac{ GM }{ r^{3} } } &= \omega_{e} \\
&= \frac{ 2\pi }{ 24 \times 60 \times 60 } \\
r &= 6.6 R_{e}
\end{split}
$$

Thus the orbit of the satellite should be 6.6 times the radius of earth.

And it should move with orbital velocity,
$$v_{o} = \sqrt{ \frac{ GM }{ 6.6R } }$$

![[Pasted image 20231219113246.png]]

![[Pasted image 20231219114452.png]]

### Paths of Satellite
$v$ is velocity of satellite. 

- $v = v_{o}$
	TE is -ve. Thus the system is bounded.
	The motion is **Circular.**
	$\\$

- $v < v_{o}$
	TE is still -ve, and it is more -ve than before as KE is less. Thus the system is bounded.
	The motion is **Elliptical.**
	$\\$

- $v_{o} < v < v_{e}$
	TE is less than 0 because when $v = v_{e}$, TE becomes zero. Thus the system is bounded.
	The motion is **Elliptical.** 
	$\\$

- $v = v_{e}$
	TE becomes zero. Thus the system is unbounded. 
	The motion is **Parabola.** 
	$\\$

- $v > v_{e}$
	TE is +ve. Thus system is unbounded.
	The motion is **Hyperbola.**

![[Pasted image 20231219115714.png]]

### Region Covered by a Satellite 
If the satellite is emitting EM waves, then what area of earth it reaches. 

Now, here,
$$
\begin{split}
\cos \theta &= \frac{ R }{ r }\\
\theta &= \cos ^{-1} \frac{ R }{ r }
\end{split}
$$
$\theta$ is the max. latitude at which EMW is reaching. 

To find the area of region, we need the solid angle,
$$
\begin{split}
\Omega &= 2\pi (1 - \cos \theta) \\
&= 2\pi \left( 1 - \frac{ R }{ r } \right)
\end{split}
$$

The area can be found by,
$$
\begin{split}
A &= \Omega R^{2} \\
&= 2\pi R^{2} \left( 1 - \frac{ R }{ r } \right)
\end{split}
$$

![[Pasted image 20231219120443.png]]
