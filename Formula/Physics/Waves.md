Links: [[00 Waves]], [[00 Sound Waves]], [[00 Wave Optics]]
___
# Waves
Equation of a general travelling wave,
$$y = f(x - vt)$$

Angular wave no.,
$$k = \frac{ 2\pi }{ \lambda }$$
Angular frequency,
$$\omega = 2\pi f$$

Speed of wave,
$$v = \frac{ \omega }{ k } = \lambda f$$

### Wave on String
Equation of sinusoidal wave,
$$y = A\sin(\omega t - kx + \theta)$$

Velocity of particle,
$$
\begin{split}
v_{p} &= \omega \sqrt{ A^{2} - y^{2} } \\
v_{p} &= -v_{w} \times \text{slope}
\end{split}
$$

Acceleration of particle,
$$a_{p} = -\omega^{2}y$$

Slope,
$$\frac{ \partial y }{ \partial x } = -Ak\cos(\omega t - kx + \theta)$$

Acceleration and double differential,
$$\frac{ \frac{ \partial^{2} y }{ \partial t^{2} } }{ \frac{ \partial^{2} y }{ \partial x^{2} } } = \frac{ \omega^{2} }{ k^{2} } = v_{w}^{2}$$

Speed of wave on string,
$$v_{w} = \sqrt{ \frac{ T }{ \mu } }$$
where $\mu$ is mass per unit length,
$$\mu = \frac{ m }{ l }$$

#### Power of Wave
Average power of wave,
$$P_{avg} = 2\pi^{2}f^{2}A^{2}\mu v$$

Intensity of wave,
$$I = 2\pi^{2}f^{2}A^{2}\rho v$$

Energy of wave on string,
$$E = P_{avg}t = 2\pi^{2}f^{2}A^{2}m$$

#### Reflection and Transmission 
Amplitude of transmitted wave,
$$A_{t} = \frac{ 2v_{2} }{ v_{1} + v_{2} }A_{i}$$
Amplitude of reflected wave,
$$A_{r} = \frac{ v_{2} - v_{1} }{ v_{1} + v_{2} }A_{i}$$

If reflection is at rarer to denser, the phase of wave will change by $\pi$. 

Reflection at fixed wall will invert the wave. 

Reflection by free end will no invert the wave. 

#### Interference 
Add the waves using phasors.

Amplitude,
$$A = \sqrt{ A_{1}^{2} + A_{2}^{2} + 2A_{1}A_{2}\cos \theta }$$

Phase difference is,
$$\Delta \phi = k\Delta x + \Delta\theta$$
$\Delta x$ cannot be more than the separation between the waves. 

Intensity,
$$I_{res} = I_{1} + I_{2} + 2\sqrt{ I_{1}I_{2} }\cos \theta$$

Constructive interference,
$$
\begin{split}
\Delta \phi &= 2\pi n \\
A_{res} &= A_{1} + A_{2} \\
I_{res} &= (\sqrt{ I_{1} } + \sqrt{ I_{2} })^{2} 
\end{split}
$$

Destructive interference,
$$
\begin{split}
\Delta \phi &= (2n+1)\pi \\
A_{res} &= |A_{1} - A_{2}| \\
I_{res} &= (\sqrt{ I_{1} } - \sqrt{ I_{2} })^{2}
\end{split}
$$

#### Standing Wave 
$$y = 2A\sin\omega t \cos kx$$

For node,
$$
\begin{split}
kx &= \frac{ \pi }{ 2 } + n\pi \\
x &= (2n+1) \frac{ \lambda }{ 4 }
\end{split}
$$

For anti node,
$$
\begin{split}
kx &= n\pi \\
x &= \frac{ n\lambda }{ 2 } 
\end{split}
$$

#### Vibration of String 
**Both ends fixed,**
Condition for resonance,
$$l = \frac{ n\lambda }{ 2 }$$
Resonance frequencies when both ends are fixed,
$$f = \frac{ nv }{ 2l }$$

**One end Fixed,**
Condition for resonance,
$$l = \frac{ (2n+1)\lambda }{ 4 }$$
Resonance frequencies when one end is free,
$$f = (2n+1) \frac{ v }{ 4l }$$

### Sound Waves 
Equation of displacement wave,
$$s = s_{o}\sin(\omega t - kx + \theta)$$

Equation of pressure wave,
$$p = p_{o}\sin(\omega t - kx + \theta)$$

Excess pressure is written as,
$$p = -B \frac{ \partial s }{ \partial x }$$
Thus,
$$p = Bks_{o}(\sin\omega t - kx + \theta + \pi /2)$$

Pressure wave is ahead of displacement wave. 

#### Speed of Sound 
Solids,
$$v_{w} = \sqrt{ \frac{ y }{ \rho } }$$

Fluids,
$$v_{w} = \sqrt{ \frac{ B }{ \rho } }$$

Air,
$$v_{air} = \sqrt{ \frac{ \upgamma P }{ \rho } } = \sqrt{ \frac{ \upgamma RT }{ M } }$$

#### Reflection of Sound 
Reflection by closed end will invert the wave. I.e. the displacement of the reflected wave will be opposite that of incident wave. 

Since displacement and pressure are out of phase by $\pi /2$, the reflected pressure wave will be in phase with the incident pressure wave.

Reflection by open end will not invert the wave. I.e. displacement of the reflected wave will be same as that of incident wave. 

Excess pressure of the reflected wave will be opposite that of incident wave. 

#### Intensity and Loudness 
Intensity,
$$
\begin{split}
I &= 2\pi^{2}f^{2}s_{o}^{2}\rho v \\
&= \frac{ p_{o}^{2} }{ 2\rho v } 
\end{split}
$$

Loudness,
$$\beta = 10\log_{10} \frac{ I }{ I_{o} }$$
where $I_{o} = 10^{-12}$ W/m$^{2}$. 

#### Interference 
of Pressure wave

Constructive interference,
$$
\begin{split}
\Delta \phi &= 2n\pi \\
\Delta x &= n\lambda \\
p_{res} &= p_{o1} + p_{o_{2}} \\
I_{res} &= (\sqrt{ I_{1} } + \sqrt{ I_{2} })^{2} 
\end{split}
$$

Destructive interference,
$$
\begin{split}
\Delta \phi &= (2n+1)\pi \\
\Delta x &= (2n + 1) \frac{ \lambda }{ 2 } \\
p_{res} &= |p_{o 1} - p_{o 2}| \\
I_{res} &= (\sqrt{ I_{1} } - \sqrt{ I_{2} })^{2} 
\end{split}
$$

#### Vibration of Air Column 
**Open organ pipe,**
Condition for resonance,
$$l = \frac{ n\lambda }{ 2 }$$

Resonance frequencies for open organ pipe,
$$f_{r} = \frac{ nv }{ 2l }$$

**Closed organ pipe,**
Condition for resonance,
$$l = \frac{ (2n+1)\lambda }{ 4 }$$
Resonance frequencies for one end closed organ pipe,
$$f_{r} = (2n+1) \frac{ v }{ 4l }$$

End correction,
$$e = 0.6r$$

Effective length of organ pipe,
$$
\begin{split}
l_{eff,o} &= l + 2e \\
l_{eff,c} &= l + e 
\end{split}
$$

#### Beats 
If two incoherent waves interfere at a point, the resultant intensity is a function of time. 

The fluctuations of intensity is called Beats. 

$$f_{b} = |f_{1} - f_{2}|$$

Humans can hear beats less than or equal to 14 Hz. 

### Wave Optics 
Optical length,
$$l' = nl$$

#### YDSE 
Path difference,
$$\Delta x = \frac{ dy }{ D }$$

Fringe width,
$$\beta = \frac{ \lambda D }{ d }$$

Phase difference,
$$\Delta \phi = \frac{ 2\pi }{ \beta }y$$

**Constructive interference,**
$$y = \frac{ n\lambda D }{ d } = n\beta$$
No. of maxima,
$$\text{no. of max.} = 2\left[ \frac{ d }{ \lambda } \right] + 1$$
If $d /\lambda$ is integer,
$$\text{no. of max.} = 2\left[ \frac{ d }{ \lambda } \right] - 1$$

**Destructive Interference,**
$$y = (n - 1 /2) \frac{ \lambda D }{ d } = (n- 1 /2)\beta$$

No. of minima,
$$\text{no. of min.} = 2 \left[ \frac{ d }{ \lambda } + \frac{ 1 }{ 2 } \right]$$

Angular fringe width,
$$\alpha = \frac{ \beta }{ D } = \frac{ \lambda }{ d }$$

Contrast,
$$\text{contrast} = \frac{ I_{max} }{ I_{min} } = \frac{ (\sqrt{ I_{1} } + \sqrt{ I_{2} })^{2} }{ (\sqrt{ I_{1} } - \sqrt{ I_{2} })^{2} }$$

Oblique incidence of light will shift the pattern down by $D\theta_{o}$. 

#### Thin Film Interference 
For top surface to appear bright,
$$\lambda = \frac{ 4\mu t }{ 2n+1 }$$

For top surface to appear dark,
$$\lambda = \frac{ 2\mu t }{ n }$$

For bottom surface to appear bright,
$$\lambda = \frac{ 2\mu t }{ n }$$

For bottom surface to appear dark,
$$\lambda = \frac{ 4\mu t }{ 2n+1 }$$

