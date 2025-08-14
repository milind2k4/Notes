Links: [[00 EM Wave]]
___
# Maxwell's EM Wave Equations 
#### Gauss Law of Electrostatics 
[[10 Electric Flux & Gauss Law#Gauss Law]]

$$\phi_{E} = \oint \vec{E} . d\vec{s} = \frac{ Q_{E} }{ \varepsilon_{o} }$$

![[Pasted image 20240119205834.png]]

#### Gauss Law of Magnetism 
Since magnetic field lines make closed loop, through a closed surface, the magnetic flux is always zero. 

$$\phi_{B} = \oint \vec{B} . d\vec{s} = 0$$

![[Pasted image 20240119205843.png]]

#### Faraday's Law of EMI 
[[00 Electromagnetic Induction#Faraday's Law]]
[[00 Electromagnetic Induction#E due to Time Varying B]]

It relates time varying magnetic field to electric field. 

$$\varepsilon = -\frac{ d\phi_{B} }{ dt } = \oint \vec{E}. d\vec{l}$$

![[Pasted image 20240119205852.png]]

#### Maxwell's Ampere's Law
Maxwell added a term of displacement current to ampere's law. 

$$
\begin{split}
\oint \vec{B}.d\vec{l} &= \mu_{o} i_{in} \\
&= \mu_{o} (i_{c} + i_{d})
\end{split}
$$
Thus if there is only time varying electric field,

$$\oint \vec{B}.d\vec{l} = \mu_{o}i_{d} = \mu_{o} \varepsilon_{o} \frac{ d\phi_{E} }{ dt }$$

Here, we can see that 4th (this) and the 3rd are complimentary equations. 

![[Pasted image 20240119205905.png]]

### Equation of EM Wave 
E, B and c are mutually perpendicular. 
I.e. if E is along +ve x axis, B will be along +ve z axis. 

E and B oscillate in a plane perpendicular to the velocity of light.

$\vec{E} \times \vec{B}$ will be along $\vec{c}$.
$\vec{B} \times \vec{c}$ will be along $\vec{E}$.
$\vec{c} \times \vec{E}$ will be along $\vec{B}$.

![[c E B relation.png]]

In terms of E,
$$\vec{E} = E_{o}\sin(\omega t - kx + \theta)\ \hat{j}$$
where,
$E_{o} \to$ Amplitude of wave
$\omega \to$ angular frequency 
$k \to$ Angular Wave no. 
$$k = \frac{ 2\pi }{ \lambda }$$

And,
$$v_{wave} = \frac{ \omega }{ k } = \lambda f$$

In terms of B,
$$\vec{B} = B_{o}\sin(\omega t - kx + \theta)\ \hat{k}$$

Thus, E and B will be in the same phase.

RMS values will be,
$$E_\text{rms} = \frac{E_{o}}{\sqrt{ 2 }}$$
$$B_\text{rms} = \frac{B_{o}}{\sqrt{ 2 }}$$

![[Pasted image 20240119205937.png]]

Also,
$$E = c B$$
In vector form.
$$\vec{B} \times \vec{c} = \vec{E}$$

#### Speed of EM Wave

In vacuum,
$$c = \frac{1}{\sqrt{ \mu_{o} \varepsilon_{o} }} = 3 \times 10^{8}$$

For another medium,
$$\begin{split}
v &=  \frac{1}{\sqrt{ \mu \varepsilon }} \\
&=  \frac{ 1 }{ \sqrt{ \mu_{o}\mu_{r} \epsilon_{o} \epsilon_{r} } }
\\
&= \frac{ 1 }{ \sqrt{ \mu_{o} \epsilon_{o} } \sqrt{  \mu_{r} \epsilon_{r} } }  \\
&= \frac{c}{\sqrt{ \mu_{r} \epsilon_{r} }}\\
v &= \frac{ c }{ n }
\end{split}$$
where $n$ is the refractive index of medium.

$$n = \sqrt{ \mu_{r} \epsilon_{r} }$$

![[Pasted image 20240119212050.png]]
