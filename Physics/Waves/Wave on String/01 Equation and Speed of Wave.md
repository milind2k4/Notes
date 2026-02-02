Links: 
___
# Equation and Speed of Wave
## Equation of Wave
Any wave satisfies the equation,
$$y = f(ax \pm bt)$$
Or satisfies,
$$\frac{ \partial^{2} y }{ \partial t^{2} } = v_{w}^{2} \frac{ \partial^{2} y }{ \partial x^{2} }$$

#### Travelling/Progressive Wave 
Equation of a wave is the function which tells the $y$-position of a particle at position $x$ and at a time instant $t$.

$$y = f(x,t)$$
$$y = f\left( t - \frac{ x }{ v } \right)$$
where v is the velocity of wave. 

This can be written as,
$$y = f(x - vt)$$
If at any time equation of y is given and we are asked to find velocity, we will replace $x$ by $x - vt$ and  then compare with the other data given. 

#### Simple Harmonic Wave 
aka Sinusoidal Wave.

We replace t with $t - x /v_{w}$ in equation of position of initial particle. 

We get,
$$
\begin{split}
y &= A\sin \left( \omega t - \frac{ \omega }{ v_{w} }x + \theta \right) \\
&= A\sin( \omega t - kx + \theta )
\end{split}
$$
where, k is angular wave no.,
$$k = \frac{ \omega }{ v_{w} }$$

Thus velocity of wave is,
$$v_{w} = \frac{ \omega }{ k }$$

![[Pasted image 20240126203507.png]]

##### Velocity of Particle
Differentiating y coordinate wrt time, we get velocity of particle along y direction,
$$
\begin{split}
\frac{ \partial y }{ \partial t } &= A\omega \cos(\omega t - kx + \theta) \\
&= A\omega \sqrt{ 1 - \frac{ y^{2} }{ A^{2} } } \\
v_{p} &= \omega \sqrt{ A^{2} - y^{2} }
\end{split}
$$
Thus,
$$
\begin{split}
y &= 0 \implies v_{p} = A\omega \\
y &= A \implies v_{p} = 0
\end{split}
$$
Just like SHM.

##### Acceleration of Particle 
Differentiating it again, we get acceleration of particle,
$$
\begin{split}
a_{p} &= -A\omega^{2}\sin (\omega t - kx + \theta) \\
&= -\omega^{2}y
\end{split}
$$

![[Pasted image 20240126203804.png]]

##### Slope
Differentiating $y(t,x)$ wrt x,
$$
\begin{split}
\frac{ \partial y }{ \partial x } &= -Ak\cos(\omega t - kx + \theta) \\
&= \text{slope}
\end{split}
$$
And it has max value, 
$$\text{slope}_{max} = Ak$$

![[Pasted image 20240126203718.png]]

Differentiating it again wrt x,
$$
\begin{split}
\frac{ \partial^{2} y }{ \partial x^{2} } &= -Ak^{2} \sin (\omega t - kx + \theta) \\
&= -k^{2}y
\end{split}
$$

And, 
$$
\begin{split}
\frac{ \partial y / \partial t }{ \partial y / \partial x  } &= \frac{ -\omega }{ k } \\
&= \frac{ v_{p} }{ \text{slope} } \\
&= -v_{w} \\
v_{p} &= -v_{w} \times \text{slope} 
\end{split}
$$

![[Pasted image 20240126203822.png]]

Again,
$$
\begin{split}
\frac{ \partial^{2} y / \partial t^{2} }{ \partial^{2} y / \partial x^{2} } &= \frac{ \omega^{2} }{ k^{2} } \\
&= v_{w}^{2} 
\end{split}
$$


## Speed of Wave on String
Rate at which disturbance in a wave is travelling. 

$$
\begin{split}
v_{w} &= \sqrt{ \frac{ \text{Tension} }{ \text{mass per unit length} } } \\
v_{w} &=  \sqrt{ \frac{ T }{ \mu } }\\
\end{split}
$$
where $\mu$ is mass per unit length,
$$\mu = \frac{m}{l}$$

This can also be written as,
$$v_{w} = \sqrt{ \frac{ \text{elasticity} }{ \text{inertia} } }$$

![[Pasted image 20240123211753.png]]

To find tension, we may need to use [[00 Rigid Body Dynamics|RBD]] and [[00 Dynamics|Newton's Laws.]]
![[Pasted image 20240123212345.png]]

#### Velocity of Wave in Rope 
Vertically suspended rope of mass m and length l.

Here, the velocity of wave is more near the top than near the bottom. This is because the mass of string adds up at the top increasing the tension. 

![[Pasted image 20240123212703.png]]

![[Pasted image 20240123213902.png]]


#### Speed of Wave on Stretchable String

$$\text{strain} = \frac{x}{l}$$
$$\text{stress} = \frac{T}{A}$$

![[Pasted image 20230213125039.png]]

Young's Modulus, $y$,
$$y = \frac{ \text{stress} }{ \text{strain} } = \frac{ Tl }{ Ax }$$

Thus, tension,
$$T = \frac{ yAx }{ l }$$

Hence velocity of wave,
$$v_{w} = \sqrt{ \frac{ yAx }{ l \mu } }$$


#### % Change in Velocity (small)

$$
\begin{split}
v &= T^{1/2}\mu^{1/2} \\
\log v &= \frac{1}{2}\log T - \frac{1}{2}\log \mu \\
\frac{dv}{v} &= \frac{1}{2} \frac{dt}{T} - \frac{1}{2} \frac{d\mu}{\mu} \\
\frac{dv}{v} \times 100 &= \frac{1}{2} \frac{dT}{T} \times 100 - \frac{1}{2} \frac{d\mu}{\mu} \times 100
\end{split}
$$