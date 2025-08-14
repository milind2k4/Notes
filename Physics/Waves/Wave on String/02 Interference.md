Links: [[00 Waves]], [[02 SHM as projection of UCM]]
___
# Interference 
of waves having same $\omega$ and same direction.

It is merely the redistribution of energy. 

Let two waves be,
$$
\begin{split}
y_{1} &= A_{1}\sin(\omega t - kx) \\
y_{2} &= A_{2}\sin(\omega t - kx + \theta )
\end{split}
$$
where $\theta$ is the phase difference.

For their resultant wave, we add them using phasors.
$$
\begin{split}
y &= y_{1} + y_{2} \\
&= A \sin(\omega t - kx + \delta)
\end{split}
$$
Where amplitude is,
$$A = \sqrt{ A_{1}^{2} + A_{2}^{2} + 2A_{1}A_{2}\cos \theta }$$


And, the phase constant $\delta$ will be,
$$\tan\delta = \frac{ A_{2}\sin \theta }{ A_{1} + A_{2}\cos \theta }$$

![[Pasted image 20240126204339.png]]

![[Pasted image 20240126204402.png]]
![[Pasted image 20240126204411.png]]

#### Coherent Waves 
Waves having same frequency or $\omega$. 

In same medium, if the waves are coherent, then their wavelength and k will also be the same. 

![[Pasted image 20240126204424.png]]

**Incoherent Waves** are those which have different frequencies. 

## Interference of Coherent Waves
travelling in the same direction. 

Let, due to source $S_{1}$, the wave is,
$$y_{1} = A_{1}\sin(\omega t - kx_{1} + \theta_{1})$$
And due to source $S_{2}$, the wave is,
$$y_{2} = A_{2}\sin(\omega t - kx_{2} + \theta_{2})$$

Here, the wave due to $S_{2}$ travels more distance. Thus, we have path difference,
$$\Delta x = x_{2} - x_{1}$$

And, the phase difference will be,
$$
\begin{split}
\Delta \phi &= k(x_{2} - x_{1}) + (\theta_{1} - \theta_{2}) \\
&= k\Delta x + (\theta_{1} - \theta_{2}) \\ 
&= \frac{ 2\pi }{ \lambda }\Delta x + (\theta_{1} - \theta_{2}) \\ 
\end{split}
$$
Here, $\theta_{1} - \theta_{2}$ is called *phase difference due to initial phases.*
And, $k\Delta x$ is called *phase difference due to path difference.*
Also, the path difference cannot be more than the distance between the sources.

![[Pasted image 20240126204446.png]]

Thus, when both the waves are superimposed, the resultant amplitude is,
$$A_{res} = \sqrt{ A_{1}^{2} + A_{2}^{2} + 2A_{1}A_{2}\cos \Delta \phi }$$
This resultant amplitude depends on individual amplitudes, as well as phase difference between the waves. 

If nothing about initial phase is given, we consider them to be the same,
![[Pasted image 20240126204522.png]]

### Resultant intensity
We know that,
$$I \propto A^{2}$$

Thus, we can write, for some constant k (since other than A all are same),
$$
\begin{split}
I_{1} &= kA_{1}^{2} \\
I_{2} &= kA_{2}^{2}
\end{split}
$$

Now, after interference, the resultant amplitude will be,
$$A_{res}^{2} = A_{1}^{2} + A_{2}^{2} + 2A_{1}A_{2}\cos \Delta \phi $$

Thus, 
$$I_{res} = kA_{res}^{2}$$

Hence we can write,
$$\frac{ I_{res} }{ k } = \frac{ I_{1} }{ k } + \frac{ I_{2} }{ k } + 2 \frac{ \sqrt{ I_{1} } }{ \sqrt{ k } } \frac{ \sqrt{ I_{2} } }{ \sqrt{ k } } \cos \Delta \phi$$

Thus, finally we get,
$$I_{res} = I_{1} + I_{2} + 2\sqrt{ I_{1}I_{2} }\cos \theta$$

#### Constructive Interference 
Where the resultant intensity is more than the algebraic sum of the intensities. 

The points which has max. $I_{res}$ are the points which have constructive interference. 
$$
\begin{split}
I_{res} &= \text{max.} \\
A_{res} &= \text{max.} \\
\cos \Delta \phi &= \text{max.} \\
&= 1
\end{split}
$$

Thus, the phase difference between the waves must be even multiple of pi. 
$$\Delta \phi = 2\pi n$$

And we get, 
$$
\begin{split}
A_{res} &= A_{1} + A_{2} \\
I_{res} &=  I_{1} + I_{2} + 2\sqrt{ I_{1} I_{2} } \\
&=  (\sqrt{ I_{1} } + \sqrt{ I_{2} })^{2}
\end{split}
$$

![[Pasted image 20240126204618.png]]

#### Destructive Interference 
$$\Delta \phi = (2n + 1)\pi$$
Thus, $\cos \Delta \phi = -1$, and,
$$A_{res} = | A_{1} - A_{2} |$$
$$I_{res} = I_{1} + I_{2} - 2\sqrt{ I_{1} I_{2} }$$
$$I_{res} = (\sqrt{ I_{1} } - \sqrt{ I_{2} })^{2}$$

![[Pasted image 20240126204643.png]]