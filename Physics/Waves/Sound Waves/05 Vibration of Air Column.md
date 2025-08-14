Links: [[00 Sound Waves]], [[04 Standing Wave]]
___
# Vibration of Air Column
aka **Resonance of Sound**

### Standing Waves
Wherever there is anti node of pressure, there will be node of displacement wave. 

Standing Sound waves are formed in Organ pipes which are cylindrical pipes made of wood or metal. 

![[Pasted image 20240207175803.png]]
![[Pasted image 20240207175855.png]]

## Open Organ Pipe
[[05 Vibration of String#Both ends are Fixed]]

Let one wave sent by the tuning fork come back and as it is going back by reflection, the fork send another wave. 

Now since there is open end, there will be no phase difference due to initial phase in displacement wave. 
And there will be initial phase difference of $2\pi$ for pressure wave, which can be removed as $2\pi = 0$

Now, if there is constructive interference between these waves, there will be resonance. 
$$
\begin{split}
\Delta \phi &= 2n\pi \\
\frac{ 2\pi }{ \lambda } 2l &= 2n\pi \\
2l &= n\lambda
\end{split}
$$
This is called condition for resonance. 

Now frequency comes out to be,
$$f_{r} = \frac{ nv }{ 2l }$$
Which is the same as in wave on string. 

![[Pasted image 20240207181612.png]]

When $n = 1$, it is called **Fundamental Frequency.**
$$f_{o} = \frac{ v }{ 2l }$$
![[Pasted image 20240207181631.png]]

When $n = 2$, it is called **Second Harmonic.** 
$$f = \frac{ v }{ l } = 2f_{o}$$
aka **First Overtone.**
![[Pasted image 20240207181639.png]]


When $n = 3$, it is called **Third Harmonic.**
$$f = \frac{ 3v }{ 2l } = 3f_{o}$$
 aka **Second Overtone.**
 ![[Pasted image 20240207181647.png]]
 
When $n = 4$, it is called **Fourth Harmonic.**
$$f = \frac{ 2v }{ l } = 4f_{o}$$
 aka **Third Overtone.**
 
## Closed Organ Pipe
(one end is closed)

 [[05 Vibration of String#One End Fixed, other Free]]

Similar to open organ pipe, if there is constructive interference between the wave just released by the fork and the wave which is reflected for the 2nd time, there will be resonance.

$$
\begin{split}
\Delta \phi &= 2n\pi \\
\frac{ 2\pi }{ \lambda }(2l) + \pi &= 2n\pi \\
4l &= (2n-1)\lambda \\
&= (2n+1)\lambda \\
&= \text{odd} \times \lambda
\end{split}
$$
This is condition for resonance.

Now, we get, frequency,
$$f_{r} = (2n-1) \frac{ v }{ 4l } = \text{odd} \times \frac{v}{4l}$$
All these frequencies are known as resonance frequencies. 

![[Pasted image 20240207182659.png]]

When $n = 1$, it is called **Fundamental Frequency.**
$$f_{o} = \frac{ v }{ 4l }$$
![[Pasted image 20240207182819.png]]

When $n = 1$, it is called **Third Harmonic.** 
$$f = \frac{ 3v }{ 4l } = 3f_{o}$$
aka **First Overtone.**
![[Pasted image 20240207182829.png]]

When $n = 2$, it is called **Fifth Harmonic.** 
$$f = \frac{ 5v }{ 4l } = 5f_{o}$$
aka **Second Overtone.**
![[Pasted image 20240207182835.png]]

When $n = 3$, it is called **Seventh Harmonic.** 
$$f = \frac{ 7v }{ 4l } = 7f_{o}$$
aka **Third Overtone.**

Hence,
$$\ce{ k^{th} overtone = (2k +1)^{th} harmonic }$$
and Even Harmonics are not Possible. 

## End Correction
If the question gives the radius of the pipe, we consider the end correction otherwise not. 

Experimentally, when we send a sound wave, the standing wave forms a little bit outside the organ pipe as well.

Experimentally, the pressure node or displacement anti node actually forms a little bit outside the pipe. This distance is called end correction, represented by $e$.

This e depends on radius of organ pipe. 
$$e = 0.6 r$$

![[Pasted image 20240207184136.png]]

Thus, the effective length of an open organ pipe will be,
$$l_{eff, o} = l + 2e = l + 1.2r$$

And that of a closed organ pipe will be,
$$l_{eff, c} = l + e = l + 0.6r$$

![[Pasted image 20240207184238.png]]

## Resonance Column Experiment
It is used to find speed of sound and it is based on resonance in closed organ pipe.

A column is filled with water, and a fork is tuned at the top end of it. 

The water is drained slowly until we hear a good sound. This means that the closed organ pipe so formed is in resonance with the frequency of the tuning fork. 

The distance between the end of the pipe and the prong of fork is $e$.

Let for the 1st time resonance, i.e. fundamental mode, the length is $l_{1}$.

Now, the distance between node and anti node is,
$$\frac{\lambda}{4} = l_{1} + e$$

Let for the 2nd time resonance, i.e. 3rd harmonic mode,
$$\frac{3\lambda}{4} = l_{2} + e$$

Dividing them, we can find end correction.
$$
\begin{split}
3 &= \frac{ l_{2}+e }{ l_{1}+e } \\
e &= \frac{ l_{2} - 3l_{1} }{ 2 }
\end{split}
$$

Subtracting them, we can find wavelength,
$$\lambda = 2(l_{2} - l_{1})$$

Thus velocity of wave,
$$v = \lambda f = 2(l_{2} - l_{1})f$$

![[Pasted image 20240207185451.png]]
