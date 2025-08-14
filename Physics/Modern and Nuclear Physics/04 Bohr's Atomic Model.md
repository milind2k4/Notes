Links: [[00 Modern Physics]]
___
# Bohr's Atomic Model
#### [[00 Modern Physics#Rutherford's Model|Rutherford's Model]] 
1. Most of the space in an atom is empty. 
2. At the centre there will be nucleus, and it will have all the +ve charge of the atom. Nucleus has almost all the mass of an atom. 
3. Electrons revolve around the protons in circuit motion due to coulombic attraction.

In Rutherford's model, any radius was possible. 
It was later discovered that only some specific radii are possible. Thus Rutherford's model failed.

### Bohr's Model 
Bohr built upon Rutherford's model.

Bohr concluded that the angular momentum of any e is an integral multiple of $h /2\pi$. 

Thus,
$$L = mvr = \frac{ nh }{ 2\pi }$$
where n can be 1,2,3...

Hence, not all radii are possible. And the orbits which are possible are called Stationary Orbits.

This is known as **Bohr's Quantisation Rule.** 
Or Angular Momentum Quantisation Rule (AMQR).

![[Pasted image 20240122213322.png]]

When e goes to an excited state, photons of the energy difference are absorbed and when e goes from higher to lower orbit, photon is emitted having energy the same as the difference of energies of the orbits.

![[Pasted image 20240122213338.png]]

##### Postulates
1. e in an atom can revolve in certain stable orbits without the emission of radiant energy. 
2. e revolves around the nucleus only in those orbits for which the angular momentum is some integral multiple of h/2$\pi$.
3. e might make a transition from one of its specified non-radiating orbits to another of lower energy. During this a photon is emitted having energy equal to the energy difference between the initial and final states. Thus,
	   $$hf = E_{i} - E_{f}$$

This model is only valid for single e atom. 

### [[05 r and v for H-like atoms]]

### Effect of Motion of Nucleus
Like [[04 Double Star System]]

If the mass of nucleus and electron is comparable, then the COM will lie in between them, and they will revolve around COM with constant $\omega$.

The COM will be,
$$
\begin{split}
r_{1} &= \frac{ m }{ M + m } r \\
r_{2} &= \frac{ M }{ M + m } r \\
\end{split}
$$

Now, centrifugal force,
$$\frac{ 1 }{ 4\pi\varepsilon_{o} } \frac{ ze^{2} }{ r^{2} } = m\omega^{2}r_{2}$$

And, angular momentum,
$$(Mr_{1}^{2} + mr_{2}^{2})\omega = \frac{ nh }{ 2\pi }$$

Putting the values, we get, separation between nucleus and electron,
$$
\begin{split}
r &= \frac{ h^{2}\varepsilon_{o} }{ e^{2}\pi \left( \frac{ mM }{ m+M } \right) } \frac{ n^{2} }{ z } \\
&= \frac{ h^{2}\varepsilon_{o} }{ e^{2}\pi \mu } \frac{ n^{2} }{ z } \\
\end{split}
$$
where $\mu$ is reduced mass.
$$\mu = \frac{ mM }{ m + M }$$

Multiplying and dividing by m,
$$
\begin{split}
r &= \frac{ h^{2}\varepsilon_{o} }{ e^{2}\pi m } \frac{ m }{ \mu } \frac{ n^{2} }{ z } \\ 
&= 0.529 \frac{ n^{2} }{ z } \frac{ m }{ \mu }\ \dot{A}
\end{split}
$$

![[Pasted image 20240123134852.png]]

Total energy of the system,
$$
\begin{split}
E &= K + U \\
&= \frac{ 1 }{ 2 }(Mr_{1}^{2} + mr_{2}^{2})\omega^{2} - \frac{ ze^{2} }{ 2\pi \varepsilon_{o} r } \\
&= -\frac{ Mm }{ M + m } \frac{ e^{4} }{ 8h^{2}\varepsilon_{o}^{2} } \frac{ z^{2} }{ n^{2} } \\
&= -\frac{ \mu e^{4} }{ 8h^{2} \varepsilon_{o}^{2} } \frac{ z^{2} }{ n^{2} }
\end{split}
$$

Multiplying and dividing by m,
$$
\begin{split}
E &= -\frac{ m e^{4} }{ 8h^{2} \varepsilon_{o}^{2} } \frac{ \mu }{ m } \frac{ z^{2} }{ n^{2} } \\
&= -13.6 \frac{ z^{2} }{ n^{2} } \frac{ \mu }{ m } 
\end{split}
$$


### Rydberg's Constant 
In nth orbit, the e has energy,
$$E = \frac{ -me^{4} }{ 8h^{2}\varepsilon_{o}^{2} } \frac{ z^{2} }{ n^{2} }$$
Now, multiplying this by $hc /hc$,
$$
\begin{split}
E &= \frac{ -me^{4} hc }{ 8h^{2}\varepsilon_{o}^{2} hc } \frac{ z^{2} }{ n^{2} } \\
&= -Rhc \frac{ z^{2} }{ n^{2} }
\end{split}
$$
where R is called **Rydberg's Constant**
$$
\begin{split}
R &= \frac{ -me^{4} }{ 8h^{3}\varepsilon_{o}^{2} c } \\
&= 10967800 \ m^{-1} \\
\frac{ 1 }{ R } &= 911\ \dot{A}
\end{split}
$$

Thus, at nth orbit,
$$E = -Rhc \frac{ z^{2} }{ c^{2} }$$

## Energies 
### Binding Energy 
aka **Ionisation energy** 

The minimum amount of energy required to bring an e from its nth orbit to infinitely far away. 

In nth orbit, energy is $E_{n}$ and as $n \to \infty$, $E_{n} \to \infty$.

Thus, binding energy is,
$$
\begin{split}
BE &= E_{\infty} - E_{n} \\
&= 0 - ( - 13.6 z^{2} /n^{2}) \\
&= 13.6 \frac{ z^{2} }{ n^{2} }\ eV \\
&= -TE
\end{split}
$$

Since here there is only one e, this binding energy is also the ionisation energy. 

Dividing ionisation energy by e gives *ionisation potential.*

![[Pasted image 20240123123238.png]]

##### What if Photon having more E than BE is incident 
At the ground state, the e has energy,
$$E_{1} = -13.6 z^{2}$$

Now, if we incident a photon having energy more than this, the kinetic energy of the e will not be zero. 

$$
\begin{split}
K &= \Delta E - 13.6z^{2} \ eV \\
&= \frac{ hc }{ \lambda } - 13.6z^{2} \ eV
\end{split}
$$

![[Pasted image 20240123125656.png]]

### Excitation Energy 
The minimum amount of energy to send an e from ground state to nth state. 

$$
\begin{split}
E.E &= E_{n} - E_{1} \\
&= 13.6 z^{2} \left( 1 - \frac{ 1 }{ n^{2} } \right)\ eV
\end{split}
$$
And excitation potential will be excitation energy divided by e. 

![[Pasted image 20240123123637.png]]

## [[06 Spectrum]]

