Links: [[00 Sound Waves]], [[00 Wave Optics]]
___
# Wave
It is a mode of energy transfer in which net displacement of medium particles is not required. 

Wave = Propagation of Momentum = Propagation of Energy = Propagation of Disturbance

##### Mechanical and Non-Mechanical Waves
**Mechanical Waves** are those which require medium. 
E.g. Wave on string, Sound waves

**Non-Mechanical Waves** are those which do not require medium. 
E.g. [[00 EM Wave]]

![[Mechanical vs Non mechanical Wave.gif]]

##### Transverse & Longitudinal Waves
**Transverse Waves** are those in which the particles oscillates perpendicular to the direction of the direction of wave. 
E.g. EM waves, wave on string

**Longitudinal Waves** are those in which the particles oscillates in the same direction as the direction of wave. 
E.g. Sound Waves

**Some notes,**
- Solids can have **both** Transverse and Longitudinal waves.

- Fluids inside the medium can only have Longitudinal waves and on the surface can have both Transverse and Longitudinal waves.

![[Mechanical-waves-transverse-longitudinal.webp]]

#### Some Terms of Wave
**Amplitude (A):** Maximum displacement of the particles.

**Wavelength $(\lambda)$:** Separation between 2 consecutive crests or troughs
And we have angular wave no.,
$$k = \frac{ 2\pi }{ \lambda }$$

**Pulse:** Part of wave which repeats itself. It is also called single cycle of wave.

**Frequency $(f)$:** Number of times medium particle performs its cyclic motion in 1 second. 
And, angular frequency,
$$\omega = 2\pi f$$

**Time Period (T):** The time taken to complete on cycle.
$$T = \frac{1}{f}$$

![[Pasted image 20240123203931.png]]

#### Plane Progressive Wave
Wave in which there is no change in Amplitude, speed of wave and frequency as it progresses. (i.e. No loss of Energy)

![[Pasted image 20240126203323.png]]

##### Simple Harmonic Wave
Plane Progressive Wave in which each particle is performing a [[00 Simple Harmonic Motion|SHM.]]

## Energy and Power of Wave
We take a small element which has length dx at beginning. At time t it makes angle $\theta$ with the horizontal. 
Before it had length h, now it has length $h\sec \theta$. 

Energy will have two terms, kinetic and potential. Kinetic due to motion of particles and elastic potential energy.

Kinetic energy,
$$
\begin{split}
dK &= \frac{ 1 }{ 2 }dm v_{p}^{2} \\
&= \frac{ 1 }{ 2 }dm \left( \frac{ \partial y }{ \partial t } \right)^{2} 
\end{split}
$$
Thus KE at mean will be most and at extremes will be zero. 

![[Pasted image 20240126204009.png]]

Potential energy,
Here, elongation is $dx(\sec \theta - 1)$. Which is max at mean position. 

Thus, PE will be max at mean position, and zero at extreme position, as it has the same length dx. 

And we can say that,
*If some element of string is passing through equilibrium position, its KE, PE and TE is max. When this element reaches extreme position, all become zero.* 

*Thus this element has transported its TE along the wave.* 

![[Pasted image 20240126204021.png]]

##### How Energy Transfers 
![[Pasted image 20240126204033.png]]

### Average Power 
Let the wave have amplitude A, frequency f, velocity v and mass per unit length $\mu$. 

$$P_{avg} = \frac{ U }{ t } = 2\pi^{2}f^{2}A^{2}\mu v$$
I.e., 
$$
\begin{split}
P &\propto f^{2} \\
&\propto A^{2} 
\end{split}
$$

#### Intensity of Wave
Let the cross sectional area be S. 

Then, intensity is defined as power crossing per unit cross sectional area.
$$
\begin{split}
I_{avg} &= \frac{ P_{avg} }{ S } \\
&= \frac{ 2\pi^{2}f^{2}A^{2}\mu v }{ S } \\
&= 2\pi^{2}f^{2}A^{2}\rho v  \\
\end{split}
$$
where, $\rho$ is density of rope.

![[Pasted image 20240126204109.png]]

### Energy of Wave on String 
Time taken for a disturbance to reach end of rope,
$$t = \frac{ l }{ v }$$
Now, all the energy within this time that was supplied to the initial particle. 

Thus we can write,
$$
\begin{split}
E &= P_{avg} t \\
&= 2\pi^{2} f^{2} A^{2} \mu v . \frac{ l }{ v } \\
&= 2\pi^{2} f^{2} A^{2} m \\
&= \frac{ mA^{2}\omega^{2} }{ 2 }
\end{split}
$$

Also, since waves are plane progressive, the total kinetic and potential energies are equal. 

## Superposition of Waves 
[[06 Superposition]]

If two or more waves are superimposed on a string, the the resultant wave will be,
$$y = y_{1} + y_{2}$$
this sum however, is vector. 

![[Pasted image 20240126204129.png]]

![[Pasted image 20240126204152.png]]


## Reflection and Transmission of Waves
At interface, 
- **Reflected wave** will return back into the same medium. 
- **Transmitted wave** will travel into the other medium.

Frequency of wave is source dependent. 

And, if there is no absorbtion,
$$E_{i} = E_{R} + E_{T}$$

![[Pasted image 20240126204802.png]]
($\varepsilon$ here is energy)

### R and T of Wave on String 
The transmitted wave will have amplitude,
$$A_{t} = \frac{ 2v_{2} }{ v_{1} + v_{2} } A_{i}$$

And the reflected wave will have amplitude,
$$A_{r} = \frac{ v_{2}-v_{1} }{ v_{2} + v_{1} } A_{i}$$

![[Pasted image 20240126204816.png]]

The medium in which the wave has more speed is called Rarer and the one in which it has less speed is called Denser. 

If the transmission is from rarer to denser, the reflected wave will have -ve amplitude. This means that we will add a phase of $\pi$ to compensate for that and make it +ve. 

![[Pasted image 20240126204857.png]]

#### Reflection by Fixed Wall 
Since the wall cannot move, $v_{2} \to 0$. 

The reflected wave will have amplitude,
$$
\begin{split}
A_{r} &= \frac{ 0 - v }{ 0 + v } A \\
&= - A \\
\end{split}
$$
Thus the wave will be inverted. 

![[Pasted image 20240126204906.png]]

#### Reflection by Free End 
Since the ring has no mass, $v_{2} \to \infty$. 

The amplitude of the reflected wave will be,
$$
\begin{split}
A_{r} &= \frac{ v_{2} - v_{1} }{ v_{2} + v_{1} } A \\
&= \frac{ v_{2} }{ v_{2} } A \\
&= A 
\end{split}
$$
Thus the wave will not be inverted. 

![[Pasted image 20240126204918.png]]

## Misc. Examples 
![[Pasted image 20240123213238.png]]
![[Pasted image 20240123213422.png]]
![[Pasted image 20240123213437.png]]

