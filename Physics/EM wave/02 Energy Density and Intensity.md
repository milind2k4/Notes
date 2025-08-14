Links: [[00 EM Wave]]
___
# Energy Density and Intensity
## Energy Density

Let the equations of the waves be,
$$E = E_{o}\sin(\upomega t-kx + \theta)$$
$$B = B_{o}\sin(\upomega t-kx + \theta)$$

Thus, energy density comes out to be,
$$
\begin{split}
\frac{ dU_{e} }{ dV } &= \frac{ 1 }{ 2 }\varepsilon_{o}E^{2} \\
&= \frac{ 1 }{ 2 }\varepsilon_{o}E_{o}^{2}\sin s^{2}(\upomega t-kx + \theta)
\end{split}
$$
The average value will thus be,
$$
\begin{split}
\frac{ dU_{e} }{ dV } &= \frac{ 1 }{ 4 }\varepsilon_{o}E_{o}^{2} \\
&= \frac{ 1 }{ 2 } \varepsilon_{o} \left( \frac{ E_{o} }{ \sqrt{ 2 } } \right)^{2} \\
&= \frac{ 1 }{ 2 }\varepsilon_{o}E^{2}_{rms}
\end{split}
$$

Similarly, the magnetic energy density,
$$
\begin{split}
\frac{ dU_{b} }{ dV } &= \frac{ B^{2} }{ 2\mu_{o} } \\
&= \frac{ B_{o}^{2} \sin ^{2} (\upomega t-kx + \theta) }{ 2 \mu_{o} } \\ 
\end{split}
$$
The average of which will be,
$$
\begin{split}
\frac{ dU_{b} }{ dV } &= \frac{ 1 }{ 4 } \frac{ B_{o} }{ \mu_{o} } \\
&= \frac{ (B_{o} / \sqrt{ 2 })^{2} }{ 2\mu_{o} } \\ 
&= \frac{ B^{2}_{rms} }{ 2\mu_{o} }
\end{split}$$

##### Electric and Magnetic Energy Densities are Equal 
$$
\begin{split}
\frac{ dU_{e} }{ dV } &= \frac{ 1 }{ 2 } \varepsilon_{o} E^{2} \\
&= \frac{ 1 }{ 4 }\varepsilon_{o}E_{o}^{2} \\
&= \frac{ 1 }{ 4 }\varepsilon_{o} B_{o}^{2} c^{2} \\
&= \frac{ \varepsilon_{o}B_{o}^{2} }{ 4\mu_{o}\varepsilon_{o} } \\
&= \frac{ B_{o}^{2} }{ 4\mu_{o} } \\
&= \frac{ dU_{b} }{ dV }
\end{split}
$$

Thus, magnetic and electric energy densities are equal. 

Total energy density thus is,
$$
\begin{split}
\frac{ dU_{net} }{ dV } &= \frac{1}{4}\epsilon_{o} E_{o}^{2} + \frac{B_{o}^{2}}{4 \mu_{o}} \\
&= \frac{1}{2} \varepsilon_{o} E_{o}^{2} \\
&= \frac{B_{o}^{2}}{2 \mu_{o}}
\end{split}
$$

## Intensity
Intensity is power crossing per unit area. 

$$I = \frac{P}{A} = \frac{ U }{ A\Delta t }$$

Unit is watt/m$^{2}$.

![[Pasted image 20240119213627.png]]

#### I for an EM Wave
We make an imaginary cylinder of length $c.dt$ and area A. 

Now, the energy passed through the area A in time dt is the energy stored in the cylinder. 

![[Pasted image 20240119214306.png]]

Now, this cylinder has energy,
$$
\begin{split}
dU &= \frac{ dU }{ dV } dV \\
&= \frac{ 1 }{ 2 } \varepsilon_{o} E_{o}^{2} . Acdt 
\end{split}
$$
Thus, power through area A,
$$P = \frac{ dU }{ dt } = \frac{ 1 }{ 2 }\varepsilon_{o}E_{o}^{2} . Ac$$

And, intensity through area A,
$$I = \frac{ P }{ A } = \frac{ 1 }{ 2 }\varepsilon_{o}E_{o}^{2}c$$

Thus, we get, intensity,
$$
\begin{split}
I &= \frac{ 1 }{ 2 }\varepsilon_{o}E_{o}^{2} c \\
&= \frac{ B_{o}^{2} }{ 2\mu_{o} }c \\
&= \frac{ dU_{net} }{ dV } . c
\end{split}
$$

Thus, $I \propto E_{o}^{2}$ and $I \propto B_{o}^{2}$

##### Point Source of EM Wave
The energy is spread in a uniform sphere centred at the source. 

At any point of the sphere,
$$I = \frac{P}{4\pi r^{2}}$$

Now, we know  that,
$$I = \frac{ 1 }{ 2 }\varepsilon_{o} E_{o}^{2}c = \frac{ B_{o}^{2} }{ 2\mu_{o} }c$$

Equating them,
$$
\begin{split}
\frac{ P }{ 4\pi r^{2} } &= \frac{ 1 }{ 2 }\varepsilon_{o}E_{o}^{2} c \\
E_{o} &= \sqrt{ \frac{ B }{ 2\pi r^{2}\varepsilon_{o}c } }
\end{split}
$$
Thus,
$$E_{o} \propto \frac{1}{r}, B_{o} \propto \frac{1}{r}$$

And, we get,
$$I \propto E_{o}^{2} \propto B_{o}^{2} \propto \frac{1}{r^{2}}$$

![[Pasted image 20240119215046.png]]

### Poynting Vector 
It is a vector which has magnitude same as  intensity and has direction same as $\vec{c}$, i.e. along the EM wave. 

$$
\begin{split}
I &= \frac{ 1 }{ 2 }\varepsilon_{o}E_{o}^{2} c \\
&= \varepsilon_{o} E^{2} c \\
&= \varepsilon_{o} \frac{ E }{ c } Ec^{2} \\
&= \varepsilon_{o} E B c^{2} \\
&= \frac{ \varepsilon_{o}EB }{ \mu_{o}\varepsilon_{o} } \\
&= \frac{ EB }{ \mu_{o} }
\end{split}
$$
where E and B are RMS values of electric and magnetic fields. 

Thus we can write the Poynting vector as,
$$
\begin{split}
\vec{P} &= \frac{ EB }{ \mu_{o} } \hat{c} \\
&= \frac{ \vec{E} \times \vec{B} }{ \mu_{o} }
\end{split}
$$
here too E and B are RMS value. 
