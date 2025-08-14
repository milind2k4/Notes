Links: 
___
# Dynamics of Fluids 
Fluid is flowing. 

##### Stream Line 
It is the curve along which the fluid particles are flowing. It is like [[02 Electric Field#Electric Lines of Force (ELOF)|field lines.]]

The velocity of particle at any point of the stream line is tangential to it.

Each particles imitates the particle in front of it in a stream line.

![[Pasted image 20240214215058.png]]
![[Pasted image 20240214215115.png]]

#### Volume Flow Rate
It is the amount of volume flowing per unit time. 

$$\frac{ dV }{ dt } = Av$$
Its unit is $\ce{ m^{3}/s }$.

Similar to this, we have mass flow rate,
$$\frac{ dm }{ dt } = \frac{ \rho dV }{ dt } = \rho Av$$

![[Pasted image 20240214162614.png]]

##### Equation of Continuity 
For pipe of varying cross section to have streamline flow, the volume flow rate should be equal at each point. 

Thus,
$$A_{1}v_{1} = A_{2}v_{2}$$
This equation is known as equation of continuity. 

![[Pasted image 20240214215151.png]]

## Bernoulli's Principle 
It is kind of like [[03.1 Kinetic Energy#Work Energy Theorem|WET]] or[[03 Energy#Total Mechanical Energy Conservation Theorem| TMEC]] of fluid. 

Bernoulli's principle says that the sum of pressure, gravitational energy density and kinetic energy density is constant. 

I.e., throughout the streamline,
$$P + \rho gh + \frac{ 1 }{ 2 }\rho v^{2} = \text{const.}$$

Dividing with $\rho g$, we get,
$$\frac{ P }{ \rho g } + h + \frac{ v^{2} }{ 2g } = \text{const.}$$
where h is called *gravitational head,* $P /\rho g$ is called *pressure head* and $v^{2} /\rho g$ is called *velocity head.*

![[Pasted image 20240214215213.png]]
![[Pasted image 20240214215237.png]]

#### Torricelli's Theorem  
We have a container of cross sectional area $A$ filled with liquid of density $\rho$. There is a hole of area $a$, $H$ height below the top of the container through which fluid is escaping with a velocity of $v$. 

The free surface of the liquid is also coming down with a velocity $u$. 

Now, applying equation of continuity,
$$av = Au$$

And applying Bernoulli's principle,
$$
\begin{split}
P_{atm} + 0 + \frac{ 1 }{ 2 }\rho v^{2} &= P_{atm} + \rho gH + \frac{ 1 }{ 2 }\rho u^{2} \\
v^{2} &= u^{2} + 2gH 
\end{split}
$$

Thus, we get,
$$v = \frac{ A }{ \sqrt{ A^{2} - a^{2} } } \sqrt{ 2gH }$$
$$u = \frac{ a }{ \sqrt{ A^{2} - a^{2} } } \sqrt{ 2gH }$$

Now, if $A \gg a$, we can approximate,
$$v = \sqrt{ 2gH }$$
This is called *velocity of efflux.*

And, 
$$u = \frac{ a }{ A }\sqrt{ 2gH }$$

![[Pasted image 20240214215314.png]]
For max. range of the liquid going out, the hole should be at H/2 height. 

![[Pasted image 20240214215409.png]]
![[Pasted image 20240214215451.png]]

![[Pasted image 20240214215514.png]]
![[Pasted image 20240214215533.png]]

### Application of Bernoulli's Theorem
#### Lift Force on Wing of Airplane
The airplane's wings are shaped in such a way that the air passing over it is compressed. This increases the KE density and thus reduces the pressure above the wing. 

The bottom of the wing has more pressure as it has less KE density. 

Thus there is a difference in pressure, and hence a net upward force on the wing. 

![[Pasted image 20240214215711.png]]

#### Swing of an Old Ball 
The ball will have one side rough, but one side smooth. 

Due to friction by rough side, the speed of air on the rough side will be less than that of the rough side. 

Since one side has more velocity of air, it has more KE density and thus less pressure. 

Due to this difference in pressure, the ball will experience a net force towards the smooth side and thus swing towards it.

![[Pasted image 20240214172333.png]]

### Venturi meter
It is an instrument which measures volume flow rate. 

Applying continuity equation,
$$Au = av$$
Applying Bernoulli's equation,
$$
\begin{split}
P_{1} + \rho gh' + \frac{ 1 }{ 2 }\rho u^{2} &= P_{2} + \rho gh' + \frac{ 1 }{ 2 }\rho v^{2} \\
P_{1} - P_{2} &= \frac{ 1 }{ 2 }\rho(v^{2} - u^{2}) 
\end{split}
$$

We can $P_{1} - P_{2}$ as,
$$
\begin{split}
P_{1} &= P_{atm} + \rho gh_{1} \\
P_{2} &= P_{atm} + \rho gh_{2} \\
P_{1} - P_{2} &= \rho g(h_{1} - h_{2}) \\
&= \rho gh
\end{split}
$$
where $h$ is measured height difference. 

Now, equation $P_{1} - P_{2}$,
$$
\begin{split}
v^{2} - u^{2} &= 2gh \\
\frac{ A^{2}u^{2} }{ a^{2} } - u^{2} &= 2gh \\
u &= \frac{ a }{ \sqrt{ A^{2} - a^{2} } } \sqrt{ 2gh } 
\end{split}
$$

And thus we can find, volume flow rate,
$$\frac{ dV }{ dt } = Au = \frac{ Aa }{ \sqrt{ A^{2} - a^{2} } }\sqrt{ 2gh }$$

![[Pasted image 20240214215603.png]]

