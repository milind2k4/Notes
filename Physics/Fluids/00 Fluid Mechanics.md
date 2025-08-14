Links: 
___
# Fluid Mechanics 
Fluid is a substance which can flow. I.e. gases and liquids.

In this chapter, we will study predominantly liquids and gases when they have fixed volume and density. 

Here, we make two assumptions,
1. Fluid is incompressible, i.e. $V$ and $\rho$ is fixed regardless of the pressure applied. 
2. Fluid is non-viscous. I.e. two layers of fluid will only apply forces perpendicular to the common surface. I.e. no force in the tangential direction. 

##### Pressure in Liquid
Pressure in liquids is defined as,
$$P = \frac{ dF }{ dA }$$
where $dF$ is the force perpendicular to the area. 

P is a scalar quantity and has unit N/m$^{2}$ or Pascal (Pa).

Some other units are,
$$
\begin{split}
\ce{ 
1 atm &= 1.013 \times 10^{5} Pa \\
&= 760 mm of Hg \\
&= 760 torrs \\
1 bar &= 10^{5} Pa
}
\end{split}
$$

![[Pasted image 20240214213815.png]]

![[Pasted image 20240214213803.png]]


##### Relative Density or Specific Gravity
The density of an object wrt that of water is called specific gravity of that object.

$$\ce{ sg = \frac{ density of object }{ density of water } }$$

Density of water is,
$$\rho_{w} = \ce{ 1000 kg/m^{3} = 1 g/cm^{3} }$$

sg is unitless and dimensionless as it is a ratio. 

### Variation of Pressure with Height 
Since liquids are dense, the pressure is not the same everywhere in the container. 

We make an imaginary cylinder of cross sectional area A and height h. The top point is x, and the bottom is y. 

Since this cylinder is at equilibrium,
$$
\begin{split}
P_{x}A + \rho ghA &= P_{y}A \\
P_{y} &= P_{x} + \rho gh \\
\Delta P &= \rho gh
\end{split}
$$

Also, pressure gradient,
$$\frac{ \Delta P }{ h } = \rho g$$

![[Pasted image 20240214213910.png]]

When the container is accelerating in vertical direction, we use $g_{eff}$ instead of g. 

If the container is freely falling, the pressure becomes same at every point.

![[Pasted image 20240214213955.png]]
![[Pasted image 20240214214007.png]]

If there is no acceleration along horizontal direction, the pressure at any point at the same horizontal level will be the same. 

I.e. if the liquid is homogeneous, connected and has no acceleration in the horizontal direction, the pressure will be the same at the same height.
![[Pasted image 20240214214041.png]]
![[Pasted image 20240214214121.png]]



![[Pasted image 20240214140517.png]]
![[Pasted image 20240214140526.png]]

![[Pasted image 20240214141303.png]]

### Pressure in Accelerating Container
The acceleration is in horizonal direction.

We consider an imaginary cylinder of cross section A and length l. 

We can write,
$$
\begin{split}
P_{x}A - P_{y}A &= \rho Ala \\
P_{x} - P_{y} &= \rho l a \\
\Delta P &= \rho l a
\end{split}
$$

Thus, as we go in direction opposite to the acceleration, the pressure increases. 

![[Pasted image 20240214214255.png]]

The angle made by water surface from the horizontal when we accelerate it in horizontal direction is,
$$\theta = \tan ^{-1} \frac{ a }{ g }$$

![[Pasted image 20240214214336.png]]
![[Pasted image 20240214214343.png]]

#### Container is Rotated 
Here, we will get,
$$
\begin{split}
\tan \theta &= \frac{ dm\omega x^{2} }{ dmg } \\
&= \frac{ \omega^{2}x }{ g } 
\end{split}
$$

Thus as we go further, the slope increases. 

And we can write,
$$
\begin{split}
\frac{ dy }{ dx } &= \frac{ \omega^{2}x }{ g } \\
y &=  \frac{ \omega^{2}x^{2} }{ 2g } \\
\end{split}
$$
Which is a parabola. 

![[Pasted image 20240214214433.png]]

### Pascal's Law 
If we increase pressure at any point of a connected liquid, then the pressure at every point of that liquid will increase by the same amount. 

![[Pasted image 20240214143248.png]]

#### Hydraulic Lift 
It is based on Pascal's Law.

We have two interconnected tubes, one of which as large and the other has small cross sectional area. This tube is then filled with liquid.

We apply a force f on the thinner tube. This increases the pressure by,
$$P = \frac{ f }{ a }$$

Now, this increased pressure applies a force on the large cross section, which is,
$$
\begin{split}
F &= PA \\
&= f \frac{ A }{ a }
\end{split}
$$
We see that this force is quite larger than the force applied. 

Also, the bigger is the ratio of areas, $A /a$, the more is the increase in the obtained force. 

![[Pasted image 20240214144039.png]]

### [[01 Buoyancy]]

## [[03 Viscosity]]