Links: [[01 Gravitational Field and Potential]]
___
# Gravitation 
It is very much like [[00 Electrostatics]]. Except here the force and field are due to mass.

Mass, by virtue of itself, attracts other mass.

Some things to note,
- Earth rotates from West to East
- Radius of earth, $R_{e} = 6400 \ce{\ km }$
- Mass of earth, $M_{e} = 6 \times 10^{24} \ce{ \ kg }$

#### Gravitational Force b/w Point Masses 
$$f = G\ \frac{ m_{1}m_{2} }{ r^{2} }$$

Where G is called Universal Gravitational Constant and is equal to,
$$G = 6.67 \times 10^{-11} \ce{\ Nm^{2} kg^{-2} }$$
$$G = \frac{ 20 }{ 3 } \times 10^{-11} \ce{\ Nm^{2} kg^{-2} }$$

In vector form,
$$
\begin{split}
\vec{f} &= G\frac{ m_{1}m_{2} }{ r^{2} } (-\hat{r})
&= -G\frac{ m_{1}m_{2} }{ r^{3} } \vec{r}
\end{split}
$$

![[Pasted image 20231217121654.png]]

### [[01 Gravitational Field and Potential]]

## Escape Velocity
The min. velocity required to escape the gravitational field of a planet. 

Using total mechanical energy conservation,
$$
\begin{split}
\frac{ 1 }{ 2 }mv_{e}^{2} + \frac{ -mGM }{ R } &= 0^{+} + m(0) \\
v_{e} &= \sqrt{ \frac{ 2GM }{ R } } \\
&= \sqrt{ \frac{ 2GM }{ R^{2} }. R } \\
&= \sqrt{ 2gR }
\end{split}
$$

For earth,
$$v_{e} = 11.2\ \ce{ km/s }$$

![[Pasted image 20231218105402.png]]

![[Pasted image 20231218105721.png]]

## Gravitational Pressure
[[12 Electrostatics of Conductors#Electrostatic Pressure]]

The pressure is the highest at the centre and as we move away from it, pressure decreases. 

To find the pressure at a point r distance from the centre, we make a cylinder with uniform cross sectional area. 

This section of earth is being attracted by the rest of the earth but it is at its place due to the force exerted by the mass below it.

If this force exerted is F, then the gravitational pressure is given as,
$$P_{g} = \frac{ F }{ A }$$

Now, on this section, the gravitational force is,
$$
\begin{split}
df &= \rho Adx \frac{ GMx }{ R^{3} } \\
f &= \rho A \frac{ GM }{ R^{3} }\int_{r}^{R} x \, dx \\
&= \frac{ \rho A GM }{ 2R^{3} } (R^{2} - r^{2})
\end{split}
$$
Which is the same as $F$.

Thus gravitational pressure comes out to be,
$$P_{g} = \frac{ \rho GM }{ 2R^{3} } (R^{2} - r^{2})$$

Thus the max pressure is at the centre. 
$$P_{c} = \frac{ \rho GM }{ 2R }$$

And at the surface pressure is zero as there is no mass above it to apply the pressure.

![[Pasted image 20231219121523.png]]

Graph,
![[Pasted image 20231219121654.png]]