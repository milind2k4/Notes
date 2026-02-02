Links: [[01 Orbitals]]
___
# Quantum Mechanics
It is based on the concept that electron has both particle and wave nature. 

Schrodinger developed this model considering the de Broglie nature of e.

Movement of e around nucleus is a bound motion and it's wave nature is analogous to the standing wave formed when a string is stretched. 
([[04 Standing Wave]], [[05 Vibration of String]])

We cannot decide the path of microscopic particles. 
NLM fails completely in the quantum world. 

Schrodinger developed a mathematical equation to describe the movement of e around nucleus, and its wave nature.

$$\frac{ \partial^{2} \psi }{ \partial x^{2} } + \frac{ \partial^{2} \psi }{ \partial y^{2} } + \frac{ \partial^{2} \psi }{ \partial z^{2} } + \frac{ 8\pi^{2}m }{ h^{2} }(E-v)\psi = 0$$

or,

$$\nabla^{2}\psi + \frac{ 8\pi^{2}m }{ h^{2} }(E-v)\psi = 0$$

where,
$\psi \to$ amplitude of electron wave (aka **Wave Function**), it is a function of x, y, z
$m \to$ is mass of e
$E \to$ Total Energy
$v \to$ PE
$x,y,z \to$ cartesian coordinates

$$\nabla^{2} = \frac{ \partial^{2}  }{ \partial x^{2} } + \frac{ \partial^{2}  }{ \partial y^{2} } + \frac{ \partial^{2}  }{ \partial z^{2} }$$
it is a mathematical operator called **Laplacian Operator**

## Wave Function's Solution
Solving this equation for finite continuous and single valued $\psi$, gives 3 number called **Quantum Numbers**.

These 3 are, **Principal Q. Number ($n$), Azimuthal Q. Number ($l$) and Magnetic Q. Number ($m$)** and they are required to designate an orbital in an atom. 

To describe an electron in an orbital, however, we need 4 quantum numbers. This 4th quantum number is called **Spin Q. Number ($s$)**, and is observed experimentally based on the spin of an e about it's own axis. 

Solving Schrodinger's equation in *spherical polar coordinates* $(r, \theta, \phi)$ is simpler than in cartesian coordinates. 
$r \to$ radial distance 
$\theta \to$ polar angle (angle of r with z)
$\phi \to$ azimuthal angle (angle of projection of r in x-y with x)

![[Pasted image 20230427200434.png]]
(P' is projection of P on x-y plane)

Thus,
$z = r\cos \theta$
$y = r\sin \theta \sin \phi$
$x = r\cos \theta \cos \phi$
$x^{2}+y^{2}+z^{2} = r^{2}$

#### Physical Significance of $\psi$
$\psi$ is t he amplitude of e wave, and thus it could be +ve or -ve depending upon the coordinates of a point. 
Thus, $\psi$ has no physical significance.

Max. Born suggested that $\psi^{2}$ is directly proportional to the probability of finding e per unit volume. And thus, $\psi^{2}$ is called **Probability Density** and is always +ve. 

It is similar to how $I \propto A^{2}$ in EM or Sound waves. 

#### Orbital
Orbital is the region of space around nucleus where the probability of finding e is considerably high. (90 to 98%)

That is, $\psi^{2}$ is high in this region. 

But we still cannot determine exactly where the e is.
 
## Magnetic Properties
[[06 Magnetic Properties of Matter]]

$$
\begin{split}
\text{Spin Magnetic Moment} &= \mu_{s} \\
&= \sqrt{ x(x+2) } \frac{ eh }{ 4\pi m_{e} } \\
&=  \sqrt{ x(x+2) }\ \text{B. M.}
\end{split}
$$
where,
$B.M. \to$ Bohr Magneton
$x \to$ no. of unpaired e

While calculating $\mu_{s}$ of ions, make sure to remove e from the outermost shell, and then find the unpaired e. 

#### Diamagnetic
Which are weakly repelled under magnetic field. They contain 0 unpaired e. And thus the spin magnetic moment is 0.

#### Paramagnetic
Which are weakly attracted in magnetic field. They contain at least 1 unpaired e. And thus, spin magnetic moment is not 0.
 
 
