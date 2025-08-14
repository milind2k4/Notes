Links: 
___
# Magnetism 

Consists of 3 parts:
1. Magnetic Effects of Current
	- [[01 Magnetic Field]]
	- [[02 Ampere's Law]]
1. Electro Magnetic Forces
	   - [[03 Magnetic Force on Charge]]
	   - [[04 Motion of Charge in Magnetic Field]]
	   - [[05 Magnetic Force on Wire]]
2. Magnetic Properties of Matter 
	   - [[06 Magnetic Properties of Matter]]

Magnetic forces are also by virtue of charge, except for magnetic forces, the charge needs to be mobile. 

Stationary charge only creates electric field. 
Moving charge can create magnetic field also. It can also experience both magnetic and electric forces. 

Magnetic forces can be attractive as well as repulsive. 
Bodies which exert magnetic forces on each other are said to be magnetic. 

#### Bar Magnet 
Bar magnet is called **Magnetic Dipole.**
Magnetic monopole do not exist unlike electric monopoles. 

North is represented as +m and South as -m.
$m$ is called Pole Strength and it is dictates the strength of magnetic effects around it.

Its unit Ampere Meter, $\ce{ Am }$ and Dimensions are $\ce{[IL]}$. 

Pole strength is a *scalar.* +ve (N) and -ve (S).

Bar magnet is the combination of N and S. And thus is a dipole. 
The magnetic dipole moment is similar to electrical one, being,
Magnetic Dipole Moment,
$$\vec{M} = m\vec{l}$$
where $l$ is the separation between the poles. 

It is a vector and has direction **from S to N.** 
*Unit:* $\ce{ Am^{2} }$
*Dimensions:* $\ce{ [IL^{2}] }$

![[Pasted image 20240110205649.png]]

If we cut a bar magnet, it automatically becomes another smaller bar magnet. 

And,
![[Pasted image 20240110205654.png]]
#### Bar Magnet in Uniform Magnetic Field
[[09 Dipole in Field]]

The bar magnet experiences no net force, but does experience torque which wants to align the magnetic dipole moment with the magnetic field. 

$$f_{net} = 0 \implies a_{com} = 0$$

Torque is,
$$
\begin{split}
\tau &= mB l\sin \theta \\
&= M B \sin \theta \\
\vec{\tau}&= \vec{M} \times \vec{B}
\end{split}
$$

Potential energy is,
$$U = -\vec{M} . \vec{B}$$

If angle is very small,
$$
\begin{split}
\tau &= MB \theta \\
I \alpha &= MB \theta \\
\alpha &= \frac{ MB }{ I } \theta \\
\omega &= \sqrt{ \frac{ MB }{ I } }
\end{split}
$$

Thus the time period is,
$$T = 2\pi \sqrt{ \frac{ I }{ MB } }$$

![[Pasted image 20240110210729.png]]

##### Derivation for Boards
Torque on the magnet,
$$\tau = mB\sin \theta$$
To make the magnet oscillate we apply an external torque, $-\tau$.

For very small angles $\sin \theta \approx \theta$,
Thus,
$$
\begin{split}
\tau &= -mB\theta \\
I\alpha &= -mB\theta \\
I(-\omega ^{2}\theta) &= -mB\theta \\
\omega ^{2} &= \frac{mB}{I} \\
2\pi f &= \frac{ mB }{ I } \\
T &= 2\pi \sqrt{ \frac{ I }{ mB } }
\end{split}
$$

## Magnetic Flux
[[10 Electric Flux & Gauss Law]]

Represents the number of magnetic lines of force passing through an area.

$$d\phi = \vec{B}.d\vec{s}$$

Thus,
$$\phi = \int \vec{B}.d\vec{s}$$
Which is surface integral of magnetic field. 

If B is uniform,
$$\phi = \vec{B}.\vec{S} = BS\cos \theta$$

Its unit is $\ce{ Tm^{2} }$ or Weber (Wb) and dimensions are $\ce{ [ML^{2}T^{-2}I^{-1}] }$

It is a scalar and can be +ve, 0 or -ve.

![[Pasted image 20240115212416.png]]

## M and L
Magnetic Dipole Moment and Angular Momentum. 

**For a non conducting ring having charge Q and radius R rotating with angular momentum $\omega$,**
The current passing through any cross sectional area is given as,
$$i = \frac{ Q }{ T } = \frac{ Q\omega }{ 2\pi }$$

Since there is current, there will be magnetic dipole moment,
$$M = iA = \frac{ Q\omega R^{2} }{ 2 }$$

Now, the ratio M/L comes out to be,
$$
\begin{split}
\frac{ M }{ L } &= \frac{ M }{ I\omega } \\
&= \frac{ Q\omega R^{2} }{ 2 . mR^{2} \omega } \\
&= \frac{ Q }{ 2m }
\end{split}
$$
This ratio is constant for any system which has uniform charge and mass distribution. 

![[Pasted image 20240116120543.png]]

For a non conducting rod also, the ratio of M/L is the same as that of a ring. 
![[Pasted image 20240116120833.png]]

This result is useful for finding magnetic dipole moment by,
$$M = \frac{ QL }{ 2m }$$

![[Pasted image 20240116121018.png]]


## Electro vs Permanent Magnet

| Electromagnet                                                            | Permanent magnet                           |
| ------------------------------------------------------------------------ | ------------------------------------------ |
| Strength can be adjusted with the amount of current                      | Strength depends on the nature of material |
| Removal of magnetic property is temporary                                | Removal of magnetic property is permanent  |
| Poles can be altered with the current                                    | Poles cannot be changed                    |
| Magnetic properties are only displayed when current is passed through it | Magnetic properties are shown always                                           |

















