Links: 
___
# Magnetic Force on a Charged Particle
It is experimental. 

If the charged particle is at rest then there is no force. 

Experimentally, it was found that,
$$
\begin{split}
f_{m} &\propto q \\
&\propto v \\
&\propto B \\
&\propto \sin \theta \\
\\
\vec{f}_{m} &\perp \vec{B} \\
\vec{f}_{m} &\perp \vec{v} 
\end{split}
$$

Thus, we get,
$$f_{m} = q\ vB \sin \theta$$

In vector form,
$$\vec{f}_{m} = q(\vec{v} \times \vec{B})$$
Thus, $\vec{f}_{m}$ is perpendicular to the plane containing $\vec{v}$ and $\vec{B}$.

![[Pasted image 20240112204505.png]]

Now, we have
$$P = \vec{f}_{m} . \vec{v} = 0$$
Since, power is zero, $W = 0$ and thus $\Delta K = 0$ if there is no other force. 

Since kinetic energy is constant, the speed is constant. Thus, magnetic force only changes the direction of velocity and not its magnitude. 

### [[04 Motion of Charge in Magnetic Field]]

## Lorentz Force 
Or simply Electromagnetic Force. 

It is Electric Force + Magnetic Force. 

$$
\begin{split}
\vec{f} &= \vec{f}_{e} + \vec{f}_{m} \\
&= q \vec{E} + q(\vec{v} \times \vec{B})
\end{split}
$$
this net force is called **Lorentz force.** 

Here, 
$\vec{f}_{e}$ can change KE and speed of particle. 
$\vec{f}_{m}$ can't change the magnitude of velocity, only it's direction. 

![[Pasted image 20240112215905.png]]

When both magnetic and electric fields are in the question, we apply [[03.1 Kinetic Energy#Work Energy Theorem|WET]] or [[03 Energy#Total Mechanical Energy Conservation Theorem|TMEC.]] 

![[Pasted image 20240112215918.png]]
![[Pasted image 20240112220310.png]]

### Some Cases of Motion 
#### E, B, v are parallel
Since v and B are in the same direction, the magnetic force will be zero. 

Thus the only force will be electric. 
And we can write,
$$
\begin{split}
f_{x} &= QE \\
a_{x} &= \frac{ QE }{ m } \\
v_{x} &= \frac{ QE }{ m } t \\
x &= \frac{ 1 }{ 2 } \frac{ QE }{ m }t^{2}
\end{split}
$$
Thus it is the case of straight line motion with uniform acceleration. 

![[Pasted image 20240115172731.png]]

Similarly if the particle already has some velocity. 

![[Pasted image 20240115172906.png]]
![[Pasted image 20240115173003.png]]

#### E, B are parallel and v is perpendicular 
Magnetic field will govern motion in yz plane. 
Electric field will govern motion along x axis. 

Along x axis,
$$
\begin{split}
f_{x} &= QE \\
a_{x} &= \frac{ QE }{ m } \\
v_{x} &= 0 + \frac{ QE }{ m } t \\
x &= \frac{ 1 }{ 2 } \frac{ QE }{ m }t^{2}
\end{split}
$$

![[Pasted image 20240115173333.png]]

In YZ plane,

The motion will be circular with centre on the -ve z axis. 

![[Pasted image 20240115173631.png]]

Thus the net motion will again be helical which will have x axis as tangent and non uniform pitch. 

![[Pasted image 20240115173818.png]]

#### E, B are parallel and v is at an angle
Here we will break the velocity into two components, one along x and another along y. 

![[Pasted image 20240115174031.png]]
![[Pasted image 20240115174045.png]]


## Hall Effect 
It is an experiment used to find free election density in conductor, drift velocity etc. 

We apply a potential difference across the conductor slab so that current passes through it.

Then we apply a uniform magnetic field perpendicular to the direction of the current.

Due to the magnetic field, the electrons experience a force which changes their trajectory. The top surface will get a -ve charge and the bottom will get a +ve charge. 

Electric field will be created due to this charge difference. This electric field will apply another force which is opposite to the direction of magnetic force. 

At some point, both the forces will cancel each other.
That is,
$$
\begin{split}
ev_{d}B &= eE \\
v_{d} &= \frac{ E }{ B } \\
E &= Bv_{d}
\end{split}
$$

The potential difference between the top surface and the bottom surface of the conductor is called **Hall Voltage.**
$$V_{H} = EH = Bv_{d}H$$
And thus we can easily find the drift velocity. 
$$v_{d} = \frac{ V_{H} }{ BH }$$

Now, current is given as,
$$i = nAev_{d}$$
And thus we can find $n$,
$$
\begin{split}
i &= \frac{ nWHeV_{H} }{ BH } \\
&= \frac{ nWeV_{H} }{ B } \\
n &= \frac{ iB }{ WeV_{H} }
\end{split}
$$

![[Pasted image 20240115172418.png]]
