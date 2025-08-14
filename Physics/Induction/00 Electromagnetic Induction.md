Links: [[01 Induction of EMF]], [[02 Self Induction]]
___
# Electromagnetic Induction
## Faraday's Law
#### Faraday's Observations
If a loop is placed in a magnetic field, and if the field is increased, Faraday observed that current starts to pass through the loop. 

This current is called **Induced Current.** And the emf due to which this current is induced is called **Induced emf.**

Again, if the magnetic field is decreased, current passes through the loop, but in the opposite direction. 

![[Pasted image 20240116162936.png]]

If the loop shrinks or expands, then also current is induced in the loop. 

![[Pasted image 20240116164519.png]]

If the loop is rotated in the magnetic field, then too current is induced in the loop. 

![[Pasted image 20240116164301.png]]

#### Faraday's Statements
*If  [[00 Magnetism#Magnetic Flux|magnetic flux]] through a conducting loop is changing, then some emf and current will be induced in it.*

Magnetic flux can be changed by magnetic field, area or angle between $\vec{B}$ and $\vec{S}$ or a combination of them. 

Faraday's law states that,
> *Induced emf is equal to rate of change of magnetic flux.*

$$\varepsilon_{ind} = \left| \frac{ d\phi }{ dt } \right|$$

![[Pasted image 20240116165247.png]]

We can say that, slope of $\phi$ vs t graph is the induced emf. 

![[Pasted image 20240116165733.png]]

Induced emf is not the effective emf. Effective emf (or average emf) is the rms vale of emf.

$$\varepsilon_{rms} = \frac{ \varepsilon_{o} }{ \sqrt{ 2 } }$$
where $\varepsilon_{o}$ is the max value of emf. Like [[00 Alternating Current]] 

## Lenz's Law
It states that,
> Induced emf and induced current will always oppose the cause which induced them. 

It is based on energy conservation. 

![[Pasted image 20240116170240.png]]

Induced emf and induced current try to maintain magnetic flux passing through the loop. 

Due to this, we get,
$$\varepsilon = -\frac{ d\phi }{ dt } $$
The -ve sign indicates that induced emf opposes change in flux. 

![[Pasted image 20240116171037.png]]

![[Pasted image 20240116171558.png]]
![[Pasted image 20240116171639.png]]

![[Pasted image 20240116172139.png]]
![[Pasted image 20240116172542.png]]

![[Pasted image 20240116173327.png]]
(the disc will rotate in the same sense as the bar magnet)

![[Pasted image 20240116175818.png]]

#### Conversion of Energy
We move a magnet away from a conducting loop with a constant velocity v. This induces a current in the loop which applies a force on the magnet. 

This force reduces the speed of the magnet. Finally bringing it to a stop. 

Now, initially the bar magnet has kinetic energy $\frac{1}{2}mv^{2}$ and finally it has kinetic energy 0. 

Since there are no external forces, mechanical energy lost by magnet is $\frac{1}{2}mv^{2}$. This energy is converted to electrical energy in the wire. 

Thus, *by using concept of electromagnetic induction, we can convert mechanical energy into electrical energy.*

![[Pasted image 20240116180009.png]]

In this case the energy is converted to heat. 
$$H = \int i^{2} R \, dt = \frac{1}{2}mv^{2}$$

## Charge Flown in the Circuit 
We will integrate the current over time. 

We have,
$$
\begin{split}
\varepsilon &= \frac{ d\phi }{ dt } \\
i &= \frac{ \varepsilon }{ R } \\
&= \frac{ d\phi }{ dt } \frac{ 1 }{ R } \\
\\
q &= \int idt \\
&= \int \frac{ 1 }{ R } \frac{ d\phi }{ dt } \, dt \\
&= \frac{ 1 }{ R } \int d\phi  
\end{split}
$$

Thus we get,
$$q = \frac{ \phi_{f} - \phi_{i} }{ R } = \frac{ \Delta \phi }{ R }$$

![[Pasted image 20240117170017.png]]

## E due to Time Varying B
[[00 Current Electricity#Electromotive Force (EMF)]]

A time varying magnetic field induces an electric field in the region. 
The reverse is also true. A time varying electric field induces a magnetic field in the region. They are mutually perpendicular. 

Consider a cylindrical region with uniform time varying magnetic field. This field creates coaxial loops of electric field. 

**Inside the cylinder, $r \leq R$,**

We have emf induced,
$$
\begin{split}
\varepsilon &= \frac{ d\phi }{ dt } \\
&= \pi r^{2} \frac{ dB }{ dt } \\
&= \frac{ EQ 2\pi r }{ Q }
\end{split}
$$

Thus we get,
$$E_{in} = \frac{ r }{ 2 } \frac{ dB }{ dt } $$

Thus, at the centre, the electric field is zero. 

![[Pasted image 20240117190039.png]]

**Outside the cylinder, $r \geq R$**

We have induced emf,
$$
\begin{split}
\varepsilon &= \frac{ d\phi }{ dt } \\
&= \pi R^{2} \frac{ dB }{ dt } \\
&= \frac{ EQ 2\pi r }{ Q } 
\end{split}
$$

Thus giving,
$$E_{out} = \frac{ R^{2} }{ 2r } \frac{ dB }{ dt } $$

![[Pasted image 20240117190353.png]]

![[Pasted image 20240117190845.png]]
![[Pasted image 20240117190856.png]]

#### Potential Across Rod 
If a rod is placed with one of its ends touching the surface and the other at the centre, then there will be no potential difference across its ends. 

This is because the electric field created by the time varying magnetic field has loops and thus we cannot define a potential due to it. 

![[Pasted image 20240117192337.png]]

However, if none of the ends are at the centre,
![[Pasted image 20240117192522.png]]
![[Pasted image 20240117192554.png]]

## Eddy Current 
If we have a surface instead of a wire, and we apply a time varying magnetic field through it, there will be localised currents which will run in small loops. 

These localised currents are called **Eddy Currents.**

Due to these currents, there will be heat loss. This heat loss is called **Eddy Loss.**

To minimise these losses, we make cuts in the surface. These cuts are called Lamination. 

![[Eddy Current.png]]

## Misc. Examples 
![[Pasted image 20240117173512.png]]

#### Circuit Problems 
![[Pasted image 20240117180000.png]]
![[Pasted image 20240117180008.png]]
![[Pasted image 20240117180024.png]]

$\\$
![[Pasted image 20240117180952.png]]
![[Pasted image 20240117181003.png]]
![[Pasted image 20240117181012.png]]

$\\$
![[Pasted image 20240117182505.png]]
![[Pasted image 20240117182513.png]]

$\\$
![[Pasted image 20240117183141.png]]
![[Pasted image 20240117183150.png]]
![[Pasted image 20240117183157.png]]
