Links: [[00 Simple Harmonic Motion]], [[01 Equation of SHM]]
___
# Damped Oscillation 
Practically, amplitude and energy of oscillation decreases with time i.e. it gets *damped* with time. 

There is -ve work done by non conservative force(s) on the system. In general, the non conservative forces are air resistance and kinetic friction.

Air resistance is usually directly proportional to velocity and opposite to it. 
$$\vec{f}_{AR} = -b\vec{v}$$

All the non conservative forces are called *Damping forces* and the proportionality constant is called *damping constant* and is represented by $b$. 
The higher $b$ is, the quicker the energy and amplitude decrease. 

![[Pasted image 20231016191542.png]] 

**Average Life Time** is the time taken for amplitude to become 1/e times its original value. 

### Equation of SHM

Here,
$$F_{r} = -kx - bv$$

And thus,
$$
\begin{split}
ma + kx + bv &= 0 \\
\frac{ d^{2}x }{ dt^{2} } + \frac{b}{m} \frac{ dx }{ dt }  + \frac{k}{m}x &= 0 \\
\end{split}
$$
This is the differential equation of damped oscillatory motion. 
Solution of this is,
$$x = A_{o}e^{ -bt/2m } \cos(\omega_{d}t + \phi)$$

Here, A is a function of time, and is exponentially decreasing. 
$$A = A_{o}e^{ -bt/2m  }$$

And $\omega_{d}$ is damped angular frequency,
$$\omega_{d} = \sqrt{ \frac{ k }{ m } - \left( \frac{ b }{ 2m } \right)^{2} }$$
which is less than the natural angular frequency, $\omega = \sqrt{ k /m }$.

#### Position vs Time Graph 
The graph will be decreasing wave.

![[Pasted image 20231016192857.png]]

Amplitude is exponentially decreasing, meaning that the fractional change in equal time is the same.

![[Pasted image 20231016193427.png]]

#### Energy of Oscillation 
$$
\begin{split}
E &= \frac{ 1 }{ 2 }kA^{2} \\
&= \frac{ 1 }{ 2 }kA_{o}^{2} e^{ -bt/m } \\
&= E_{o} e^{ -bt/m }
\end{split}
$$

Thus the energy is also decreasing exponentially.

![[Pasted image 20231016193201.png]]

### Critical damping 
When $b$ is such that $\omega_{d}$ becomes zero, 
$$
\begin{split}
\omega_{d} &=  \sqrt{ \frac{ k }{ m } - \left( \frac{ b }{ 2m } \right)^{2} } \\
b^{2} &= 4km
\end{split}
$$

The position comes out to be,
$$x = A_{o}e^{ -bt/2m }\cos \phi$$
which is decreasing exponentially zero. 

There will be no oscillation and the block will just come to the mean position slowly. 

![[Pasted image 20231016194243.png]]

### Examples 
![[Pasted image 20231016194652.png]]


## Forced Oscillation 
An external agent does +ve work on the system. I.e. force is applied in the same direction as displacement. 

If $W_{ext} > W_{d}$ then E and A will increase.  
If $W_{ext} = W_{d}$ then E and A will remain the same.  
If $W_{ext} < W_{d}$ then E and A will decrease, but slower.

### Resonance 
If external agent is providing force at a specific angular frequency $\omega$, then only work done by external agent will be always +ve and the TME or A of system will remain constant or increase.

The source frequency is not the same as that of system.

If they have same frequency, then they are said to be *coherent* or in resonance. 

We apply an external force,
$$f_{ext} = f_{o}\sin\omega t$$

$$
\begin{split}
f_{o}\sin\upomega_{d}t - b \frac{ dx }{ dt } - kx &= m \frac{ d^{2} x }{ d t^{2} } \\
\end{split}
$$
This is called the differential equation of *forced oscillatory motion.* 

Due to this the amplitude comes out to be,
$$A = \frac{ f_{o} / m }{ \sqrt{ (\omega^{2} - \omega_{o}^{2})^{2} + \left( \frac{ b\omega }{ m } \right)^{2} } }$$
where, 
$\omega \to$ angular frequency of external agent 
$\omega_{o} \to$ natural angular frequency ($\omega_{d}$)

When $\omega \cong \omega_{o}$, $A$ is very high. 

If there is very less damping, then $b \to 0$ and thus, 
$$A = \frac{ f_{o} }{ m(\omega^{2} - \omega_{o}^{2}) }$$

![[Pasted image 20231016200925.png]]

