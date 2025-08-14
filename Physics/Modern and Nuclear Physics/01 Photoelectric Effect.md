Links: [[00 Modern Physics]]
___
# Photoelectric Effect
#important 

When EM radiation of high E (low $\lambda$ or high $f$) are incident on a metallic surface then the free e of the metal absorb the photon and can come out of the metal. 

This phenomenon is called the **Photoelectric Effect.**

![[Pasted image 20240122181110.png]]

##### Laws of Photoelectric Emission
- The number of photoelectrons emitted per second is directly proportional to the intensity of incident radiation. 
  $\\$
- Velocity of electrons emitted is independent of the intensity of incident light and only depends on the frequency of it.
  $\\$
- For a certain metal, there exists a certain minimum frequency below which no emission of e takes place. This is called the threshold frequency of the metal. 
  $\\$
- Photoelectric emission is an instantaneous process. There is no time delay between the incident of light and the emission of electrons. ($10^{-9}$ s)
  $\\$
- For a given frequency of the incident radiation, the stopping potential is independent of its intensity. 
  $\\$
- The stopping potential varies linearly with the frequency of incident radiation.

#### Work Function 
The minimum energy required to eject e from metal.

It is denoted by $\phi\ or W$.

The energy of the photon should be more than the work function of the metal for it to eject out a free e. 

For example, for Caesium, $W = 1.9\ eV$. And it is the lest work function.  

![[Pasted image 20240122181530.png]]

### Einstein's Equation
The e which has most KE (fastest photo e) is the e which has absorbed all the E from photon and using it overcame the attractive forces of the metal. 
It has not dissipated any energy in the metal lattice. 

This fastest photon has kinetic energy,
$$
\begin{split}
K_{max} &= E - W \\
&= \frac{ hc }{ \lambda } - W
\end{split}
$$

The other e will have less KE then this max. value. 
$$0 \leq K \leq K_{max}$$
And the exact KE will depend on energy lost by e in collision in the lattice. 

The no. of e ejected with max. or zero KE will be very less. 

![[Pasted image 20240122182358.png]]

### Quantum Efficiency 
aka Photoelectric Efficiency.

Let $n_{p}$ no. of photons hit the surface of the metal, and due to this $n_{e} (< n_{p})$ no. of photo e ejected from the metal.

Then, quantum efficiency is, no. of photo e emitted per no. of photons incident, 
$$\eta = \frac{ n_{e} }{ n_{p} } \times 100$$

### Threshold Frequency ($f_{th}$)
The minimum frequency of photon which can just produce photoelectric effect.

Thus,
$$
\begin{split}
hf_{th} &= W \\
f_{th} &= \frac{ W }{ h }
\end{split}
$$
The KE of the fastest e can thus be written as,
$$K_{max} = hf - hf_{th}$$

![[Pasted image 20240122183401.png]]

### Threshold Wavelength
Just like threshold frequency. 

The maximum wavelength of photon which can produce photoelectric effect.

Thus,
$$
\begin{split}
\frac{ hc }{ \lambda_{th} } &= W \\
\lambda_{th} &= \frac{ hc }{ W }
\end{split}
$$
And,
$$\lambda_{th} f_{th} = c$$

Now, the energy of the fastest e is,
$$
\begin{split}
K_{max} &= \frac{ hc }{ \lambda } - W \\
&= \frac{ hc }{ \lambda } - \frac{ hc }{ \lambda_{th} }
\end{split}
$$

![[Pasted image 20240122183905.png]]

![[Pasted image 20240122185144.png]]

### Experiment of Photoelectric Effect
**Formation of Photoelectric Current or Photocurrent**

In this experiment, Heinrich Hertz irradiated a piece of metal in vacuum to produce photocurrent. 

![[Pasted image 20240122185512.png]]
![[Photoelectric current.png]]

#### Current vs Voltage Curve
There is some current flowing without applying any voltage because due to photoelectric effect, some electrons are ejected and start circulating. 

On increasing the potential of anode and decreasing that of cathode increases the photocurrent due to presence of electric field between the plates. 

After one point, all the e emitted by the cathode due to photoelectric effect go to the anode and thus contribute to the current. This max. current is called **Saturation Current.**

Now, if we increase the potential in the opposite direction, i.e. increase the potential of cathode and decrease that of anode, there will be electric field in the opposite direction and less and less e will reach anode. 

At one point the photocurrent will completely stop. This potential is called **Stopping Potential.**

![[Pasted image 20240122190024.png]]

#### Saturation Current 
Let the quantum efficiency be $\eta$% and we hit the cathode with radiation of power P and wavelength $\lambda$.

Per second, no. of photons hit on the cathode is,
$$n_{p} = \frac{ P\lambda }{ hc }$$
No. of e emitted per second,
$$n_{e} = \frac{ \eta n_{p} }{ 100 } = \frac{ \eta P\lambda }{ 100hc }$$

Now, saturation current,
$$
\begin{split}
i_{s} &= \frac{ q }{ t } \\
&= \frac{ n_{e}(e) }{ 1 } \\
&= \frac{ \eta P\lambda e }{ 100hc }
\end{split}
$$
Since saturation current depends on Power, it also depends on Intensity of radiation. 

![[Pasted image 20240122190839.png]]

![[Pasted image 20240122191127.png]]

#### Stopping Potential 
The minimum -ve potential at which the photocurrent becomes zero. 

The potential should be that much so that the fastest e turns just before hitting the anode. 

![[Pasted image 20240122191623.png]]


Using TMEC,
$$
\begin{split}
K_{max} + (-e).0 &= 0 + (-e)(-V_{s}) \\
K_{max} &= eV_{s}
\end{split}
$$
Thus we can write,
$$V_{s} = \frac{ K_{max} }{ e }$$
And,
$$
\begin{split}
V_{s} &= \frac{ K_{max} }{ e } \\
&= \frac{ E - W }{ e } \\
&= \frac{ hf }{ e } - \frac{ W }{ e } \\
&= \frac{ hc }{ e\lambda } - \frac{ W }{ e }
\end{split}
$$
thus, 
$$
\begin{split}
V_{s} &\propto f \\
&\propto \frac{1}{\lambda}

\end{split}
$$

- Stopping potential varies linearly with the frequency in incident radiation for a given photosensitive material.
- There exists a certain minimum frequency $v_{o}$ (threshold frequency) for which the stopping potential is zero. 

![[Pasted image 20240122192124.png]]

For different wavelengths/frequencies,
![[Pasted image 20240122192612.png]]

For same power but different frequencies,
![[Pasted image 20240122193855.png]]







