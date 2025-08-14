Links: [[00 Sound Waves]]
___
# Displacement and Pressure Wave
### Displacement Wave
(all the same as [[01 Equation and Speed of Wave#Simple Harmonic Wave|wave on string]])

The equation of wave in terms of displacement of medium particles is called Displacement Wave.

We will consider wave in which the medium particles are doing [[00 Simple Harmonic Motion|SHM.]]

$$s = s_{o}\sin(\omega t - kx + \theta)$$
where 
$s \to$ longitudinal displacement of particle from mean position
$s_{o} \to$ amplitude of displacement
$\omega \to$ angular frequency
$k \to$ angular wave number 

$$\omega = \frac{ 2\pi }{ T }$$
$$k = \frac{ 2\pi }{ \lambda }$$

Velocity of wave is,
$$v = \frac{ \omega }{ k }$$

![[Pasted image 20240207192416.png]]

##### Velocity of particle
Velocity of medium particles is,
$$
\begin{split}
v_{p} &= \frac{ \partial s }{ \partial t } \\
&= s_{o}\omega \cos(\omega t - kx + \theta) \\
&= \omega \sqrt{ s_{o}^{2} - s^{2} }\\ 
v_{p,o} &= s_{o} \omega
\end{split}
$$
Thus max. speed is at the mean position. 

##### Acceleration of particle
Acceleration of medium particles is,
$$
\begin{split}
a_{p} &= \frac{ \partial v }{ \partial t } \\
&= -s_{o}\omega^{2} \sin(\omega t - kx + \theta) \\
&= -\omega^{2}s \\
a_{p,o} &= \omega^{2} s_{o} 
\end{split}
$$
Thus max. acceleration is at the extreme positions. 

![[Pasted image 20240207192427.png]]

### Pressure Wave
##### Pulses
- **Compression Pulse:** The region created when the medium particles come close to each other.
	The pressure in this region becomes, $P_{atm} + p,\ p > 0$. 
	This $p$ is called **Excess Pressure.**
	
	This compression pulse moves forward with the speed of the sound wave. 
  
	![[Pasted image 20240207192446.png]]
	$\\$
	  
- **Rarefaction Pulse:** The region created when the medium particles are far away from each other.
	The pressure in this region becomes, $P_{atm} + p,\ p < 0$. 
	Here too p is called Excess Pressure. 
	
	This rarefaction pulse also moves forward with the speed of the sound wave. 
	
	![[Pasted image 20240207192519.png]]

#### Equation of Pressure Wave 
It is when sound wave is written in terms of excess pressure.

If the particles move in SHM, the pressure will also vary simple harmonically.

Thus we get, excess pressure p,
$$p = p_{o}\sin(\upomega t - kx + \theta)$$
Excess pressure varies is between,
$$p \in [-p_{o}, p_{o}]$$

Thus the pressure in the region is between,
$$P \in [P_{atm} - p_{o}, P_{atm} + p_{o}]$$
$p_{o}$ however is very small compared to $P_{atm}$.

![[Pasted image 20240207192536.png]]

#### Relation b/w Pressure and Displacement Waves 
Let the bulk modulus of a medium be $B$.

Then we can write, excess pressure,
$$p = -B \frac{ \partial s }{ \partial x }$$

If the displacement is given as,
$$s = s_{o} \sin (\omega t -kx + \theta)$$
Then, the excess pressure comes out to be,
$$
\begin{split}
p &=  Bks_{o} \cos (\omega t - kx + \theta) \\
p &=  Bks_{o} \sin (\omega t - kx + \theta + \pi /2)
\end{split}
$$

Thus pressure amplitude in terms of displacement amplitude is,
$$p_{o} = Bks_{o}$$

Also, we can see that pressure wave is ahead of displacement wave by a phase of $\pi /2$.

![[Pasted image 20240207192806.png]]
![[Pasted image 20240207192828.png]]