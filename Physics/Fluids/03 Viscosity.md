Links: [[02 Fluid Dynamics]]
___
# Viscosity 
Viscosity is property of liquid due to which a non conservative resistive force acts in tangential direction (shear) which opposes any relative motion between layers of liquid in contact. 

The force is called **Viscous Force.**

#### Velocity Gradient
As we go away from the bottom, the velocity of the particles increases.

We define velocity gradient as,
$$\frac{ dv }{ dx } = \frac{ v_{o} }{ H }$$

Its unit is $s ^{-1}$. 

![[Pasted image 20240214174348.png]]

#### Viscous Force 
$$f_{v} = \eta A \frac{ dv }{ dx }$$
where $\eta$ is called **Coefficient of Viscosity** which is property of liquid. 

$\eta$ has unit $\ce{ N s/m^{2} }$. 

An alternate unit of $\eta$ is,
$$
\begin{split}
\ce{ 
1 N s/m^{2} &= \frac{ 10^{5} dyne s }{ 10^{4} cm^{2} } \\
&= 10 poise \\
&= 1 deca poise 
 }
\end{split}
$$

![[Pasted image 20240214175151.png]]

![[Pasted image 20240214175822.png]]
![[Pasted image 20240214175834.png]]

![[Pasted image 20240214180215.png]]
![[Pasted image 20240214180546.png]]

### Stoke's Law 
It is for a completely submerged sphere.

It tells the viscous force on the sphere. 

It states that,
$$
\begin{split}
f_{v} &\propto r \\
&\propto v \\
&\propto \eta 
\end{split}
$$

Thus we get,
$$f_{v} = 6\pi \eta rv$$

And if the liquid is flowing, instead of $v$ we put $v_{rel}$. 

![[Pasted image 20240214181046.png]]

The power of this force is,
$$\text{Power} = -f_{v}v = -6\pi \eta rv^{2}$$
The -ve indicates that the system is losing energy. 

### Terminal Velocity 
Consider a sphere of radius R density $\rho$ released in a liquid of density $\sigma$ and viscosity $\eta$. 

If $\rho > \sigma$, the sphere starts sinking with a velocity $v$ and thus experiences a viscous force. 

After some time, the [[01 Buoyancy|buoyancy force]] and the viscous force balance the gravitational pull and the net force becomes zero. After this point, the velocity becomes constant and maximum it can be. 

This max. velocity is called **Terminal Velocity.**

Equating the forces, we get,
$$
\begin{split}
\rho \frac{ 4 }{ 3 }\pi R^{3}g &= \sigma \frac{ 4 }{ 3 }\pi R^{3}g + 6\pi \eta Rv \\
v &= \frac{ 2 }{ 9 } \frac{ (\rho - \sigma)R^{2}g }{ \eta }
\end{split}
$$

![[Pasted image 20240214181907.png]]

##### Velocity vs Time graph 
It is like a logarithmic graph. 

![[Pasted image 20240214182139.png]]

### Reynold Number 
#removed 

$$N = \frac{ \rho vD }{ \eta }$$
where $D$ is diameter of the tube. 

If N < 2000, the motion of the liquid is streamlined. 

If N > 3000, the motion is Turbulent. 

![[Pasted image 20240214182409.png]]

