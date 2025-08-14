Links: 
___
# Magnetic Properties of Matter
#### Diamagnetic Substances
E.g. Cu, Zn, Bi, Ag, Au, NaCl etc.

Individual atoms do not have any magnetic dipole moment, and thus the whole body does not have a magnetic dipole moment. 

$$\sum \vec{M} = 0$$

![[Pasted image 20240116121408.png]]

Diamagnetic substances exhibit a property called **Diamagnetism.**

In external magnetic field, there are magnetic dipoles are created opposite to it according to  faraday's laws. 

Due to this, there is an induced magnetic field inside the substance. The net magnetic field inside the substance is thus less than the external one,
$$B_{net} < B_{ext}$$

Due to this, they repel magnetic lines of force and thus magnets.

If a substance is perfectly diamagnetic, the internal magnetic field is opposite to and equal to the external magnetic field and thus the magnetic field inside the substance is zero. 
$$\vec{B}_{ind} = - \vec{B}_{ext}$$
$$\vec{B}_{net} = 0$$
Thus, the magnetic lines of forces will not enter a perfectly diamagnetic substance.

![[Pasted image 20240116122226.png]]

#### Paramagnetic Substances
E.g. FeO, O$_{2}$, Titanium, Al

Individual atoms have magnetic dipole moments. But each atom is aligned randomly thus cancelling the dipole moments,

$$\sum \vec{M} = 0$$

![[Pasted image 20240116121654.png]]


Paramagnetic substances exhibit a property called **Paramagnetism.**

In external magnetic field, the dipoles align themselves along the external magnetic field. Due to this a magnetic field is induced in the direction of the external magnetic field in the substance. 

Thus, the net magnetic field inside is more than the external,
$$B_{net} > B_{ext}$$
Due to this, they attract magnetic lines of forces and thus attracts magnets.

![[Pasted image 20240116122711.png]]

#### [[07 Ferromagnetism|Ferromagnetic Substances]]

### Intensity of Magnetisation $(\vec{I})$
Magnetic dipole moment of the system per unit volume. 
Magnetisation means Intensity of Magnetisation.

$$\vec{I} = \frac{ \vec{M} }{ V }$$

It is a vector quantity along $\vec{M}$.

Its unit is $\ce{ Am^{-1} }$ and dimensions are $\ce{ [IL^{-1}] }$

#### I of Bar Magnet 
$$
\begin{split}
I &= \frac{ M }{ V } \\
&= \frac{ ml }{ lA } \\
&= \frac{ m }{ A }
\end{split}
$$

![[Pasted image 20240116123056.png]]


#### I of Diamagnetic substance 
Here,
$$\vec{M} \upharpoonleft \! \downharpoonright \vec{B}_{ext} \implies \vec{I} \upharpoonleft \! \downharpoonright \vec{B}_{ext}$$

$\vec{I}$ is anti-parallel to the applied magnetic field. 

And the induced magnetic field,
$$
\begin{split}
B_{ind} &\propto I \\
B_{ind} &= \mu_{o} I \\
\end{split}
$$

And in vector form,
$$\vec{B}_{ind} = \mu_{o} \vec{I}$$

The net magnetic field is thus,
$$B_{net} = B_{o} - B_{ind}$$


![[Pasted image 20240116123317.png]]

#### I of Paramagnetic substance 
Here, 
$$\vec{M} \parallel \vec{B}_{ext} \implies \vec{I} \parallel \vec{B}_{ext}$$

$\vec{I}$ is parallel to the applied magnetic field. 

Here too the induced magnetic field is,
$$\vec{B}_{net} = \mu_{o} \vec{I}$$

And the net magnetic field is,
$$B_{net} = B_{o} + B_{ind}$$

![[Pasted image 20240116123454.png]]

### Magnetic Intensity (H)
Since magnetic field depends on the medium, we define magnetic intensity which does not depend on it. H only depends on the source.

It is a vector quantity. And is defined as field per permeability. 

$$\vec{H} = \frac{ \vec{B} }{ \mu } = \frac{ \vec{B} }{ \mu_{o} \mu_{r} }$$

Its unit is $\ce{ Am^{-1} }$ and dimensions are $\ce{ [IL^{-1}] }$

![[Pasted image 20240116124413.png]]

$$H \uparrow \implies \text{magnetisation} \uparrow \implies M \uparrow \implies I \uparrow$$

#### Relation between B and H
Here, $\vec{B}_{ext} = \vec{B}_{o}$
And $\vec{B}$ is the magnetic field inside the substance. 

In vacuum,
$$\vec{H} = \frac{ \vec{B}_{o} }{ \mu_{o} }$$

In other medium, 
$$\vec{H} = \frac{ \vec{B} }{ \mu } = \frac{ \vec{B} }{ \mu_{o} \mu_{r} }$$

![[Pasted image 20240116124833.png]]


And, 
$$\vec{B} = \vec{B}_{o} + \vec{B}_{ind}$$

Thus, we get,
$$
\begin{split}
\vec{H} &= \frac{ \vec{B}_{o} + \vec{B}_{ind} }{ \mu } \\
&= \frac{ \mu_{o} \vec{H} + \mu_{o} \vec{I} }{ \mu_{o} \mu_{r} } \\
\mu_{o}\mu_{r} \vec{H} &= \mu_{o} \vec{H} + \mu_{o} \vec{I} \\
(\mu_{r} - 1)\vec{H} &= \vec{I} 
\end{split} 
$$

Thus, we get,
$$\vec{H} = \frac{ \vec{I} }{ \mu_{r} - 1 }$$


The net magnetic field is,
$$\vec{B} = \mu_{o} \vec{H} + \mu_{o} \vec{I}$$

### Magnetic Susceptibility $(\chi)$
As we increase magnetic intensity H, intensity of magnetisation I increases. 
$$I \propto H$$

The constant of proportionality is called magnetic susceptibility.
$$\vec{I} = \chi \vec{H}$$

It is a unitless and dimensionless quantity and it represents the magnetisation amount. 
i.e.
$$\chi \uparrow \implies \text{more magnetized}$$

In diamagnetic substance, since $\vec{I}$ and $\vec{H}$ are anti-parallel, $\chi = -ve$.
In paramagnetic substance, since $\vec{I}$ and $\vec{H}$ are parallel, $\chi = +ve$.

Now, 
$$
\begin{split}
\chi &= \frac{ I }{ H } \\
&= \frac{ I (\mu_{r} - 1) }{ I } \\
&= \mu_{r} - 1
\end{split}
$$
Thus,  we get,
$$\mu_{r} = 1 + \chi$$

For diamagnetic substance, $0 < \mu_{r} < 1$.
For paramagnetic substance, $\mu_{r} > 1$.

![[Pasted image 20240116130439.png]]

## Curie's Law
$$\chi \propto \frac{ 1 }{ T }$$
here T is in Kelvin.

$$T\uparrow \implies \chi \downarrow \implies I \downarrow$$

As temp. increases, the vibrations of the molecules also increases. This vibration makes it harder to align the magnetic dipoles of the substance to create induced magnetic field. 

Thus,
$$M \propto \frac{1}{T}$$
$$I \propto \frac{1}{T}$$




