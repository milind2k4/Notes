Links: [[00 Waves]], [[04 Standing Wave]]
___
# Vibration of String
#important

aka **Resonance in String**

## Both ends are Fixed
Since both ends are fixed, they will be nodes. 

Let there be n loops. Since each loop has length $\lambda /2$, then,
$$
\begin{split}
l &= \frac{ n\lambda }{ 2 } \\
\lambda &= \frac{ 2l }{ n }
\end{split}
$$
This is known as **Condition for resonance.**

For frequency,
$$
\begin{split}
\lambda &= \frac{ v }{ f } \\
f &= \frac{ nv }{ 2l }
\end{split}
$$
All these frequencies are known as **Resonance Frequencies or Natural Frequency or Normal Frequency.**

![[Pasted image 20240125215941.png]]

When $n = 1$, the frequency is called **Fundamental Frequency.** The ends will be nodes and $l / 2$ will be anti node. This is also the lowest frequency of transverse vibrations.

$$f = f_{o} = \frac{ v }{ 2l }$$

When $n = 2$, the frequency is called **Second Harmonic.** 
Which is also called **First Overtone.**
$$f = \frac{ v }{ l } = 2f_{o}$$


When $n = 3$, the frequency is called **Third Harmonic.** 
Which is also called **Second Overtone.**

$$f = \frac{ 3v }{ 2l } = 3f_{o}$$

![[Pasted image 20240126181504.png]]


Thus, 
$$\ce{ n^{th} harmonic = (n-1)^{th} overtone }$$
And,

$$
\begin{split}
\text{Anti-nodes} &= n \\
\text{Nodes} &= n+1
\end{split}
$$

![[Pasted image 20240126182323.png]]

### Sonometer/Monochord
It is experimental setup based on resonance in string fixed at both ends and is used to find speed of wave. 

We bring a tunic fork of frequency f near the string. 

Now, if this f is the same as the fundamental f of the string, there will be large oscillations in the string. 

We will put a piece of paper on the string called Rider as indicator. If it falls, we conclude that it is indeed in resonance. 

![[Pasted image 20240126205151.png]]
(that is a hook, not a wave)

The frequency of the tuning fork will be,
$$f = \frac{ nv }{ 2l }$$
Now, here, we can change f by changing,
- v by changing the mass on hook or by changing wire, 
- l by moving bridges.

The frequency thus comes to be,
$$f = \frac{ n \sqrt{ mg /\mu } }{ 2l }$$

![[Pasted image 20240126205208.png]]
![[Pasted image 20240126205217.png]]

#### How to Measure Speed of Wave 
using Sonometer 

Let, at first there is resonance. Then,
$$l = \frac{ \lambda }{ 2 }n$$

Now, as we slowly move one of the bridges away, the resonance breaks. After traveling distance $\Delta l$, the resonance is established again. Thus we can write,
$$l + \Delta l = \frac{ \lambda }{ 2 }(n+1)$$

Subtracting them,
$$\Delta l = \frac{ \lambda }{ 2 }$$

Thus, we get, 
$$
\begin{split}
\lambda &= 2\Delta l \\
v_{w} &= \lambda f \\
&= 2\Delta l . f 
\end{split}
$$

![[Pasted image 20240126205229.png]]

## One End Fixed, other Free
Free end means that it is connected to a light string. Because otherwise, there will be no tension, and thus no wave. 

At the free end, there will be anti-node as the incident amplitude of A and the reflected amplitude of A will be added to form amplitude of 2A.

Thus, the start will be at node, and end will be at anti node. 
And the last loop will be half loop. 

![[Pasted image 20240126205243.png]]

#### Mathematical Interpretation 
Let the equation of the incident wave is,
$$y_{1} = A \sin (kx - \omega t)$$
And that of the reflected wave is,
$$y_{2} = A \sin (kx + \omega t + \theta)$$

![[Pasted image 20240126205300.png]]

The equation of the resultant wave will be,
$$
\begin{split}
y &= y_{1} + y_{2} \\
&= 2A \sin \left( kx + \frac{ \theta }{ 2 } \right) \cos \left( \omega t - \frac{ \theta }{ 2 } \right) \\
&= 2A' \cos \left( \omega t - \frac{ \theta }{ 2 } \right)
\end{split}
$$
This is equation of standing wave. 

Now, at $x = 0$, the amplitude is zero and thus there is node. 
$$
\begin{split}
A' &= 0 \\
2A \sin (\theta /2) &= 0 \\
\frac{ \theta }{ 2 } &= 0, \pi  \\
\theta &= 0, 2\pi
\end{split}
$$

Putting $\theta = 0$, we get,
$$y = 2A\sin kx \cos \omega t$$

Now, at $x = l$, the amplitude is 2A and  thus it is anti node. 
$$
\begin{split}
A' &= \pm 2A \\
2A \sin kl &= \pm 2A \\
\sin kl &= \pm 1 \\
kl &= \frac{ \pi }{ 2 } + n\pi \\
\frac{ 2\pi }{ \lambda } l &= \frac{ \pi }{ 2 } + n\pi \\
(2n+1)\lambda &= 4l 
\end{split}
$$
This is the condition for resonance. 

Now, we get frequency,
$$
\begin{split}
(2n+1)\lambda &= 4l \\
(2n+1) \frac{ v }{ f } &= 4l \\
f &= (2n+1) \frac{ v }{ 4l } \\
&= (\text{odd}) . \frac{ v }{ 4l }
\end{split}
$$
These frequencies are called Resonance Frequencies. 

The smallest frequency which produces resonance is called **Fundamental frequency,** (put n = 0)
$$f_{o} = \frac{ v }{ 4l }$$


Putting $n = 1$,
$$f = \frac{ 3v }{ 4l } = 3 f_{o}$$
This is **Third Harmonic** as it is 3 times $f_{o}$. 
This is also called **First Overtone.**

Putting $n = 2$,
$$f = \frac{ 5v }{ 4l } = 5f_{o}$$
This is **Fifth Harmonic.**
This is also called **Second Overtone.**

Putting $n = 3$,
$$f = \frac{ 7v }{ 4l } = 7f_{o}$$
This is **Seventh Harmonic.**
This is also called **Third Overtone.**

Thus, we see that even harmonics are not possible in this case.
And here,
$$
\begin{split}
\ce{ 
k^{th} overtone &= (2k +1)^{th} harmonic \\
n^{th} harmonic &= \left( \frac{ n -1 }{ 2 } \right)^{th} overtone
 }
\end{split}
$$

No. of loops,
$$\ce{ n^{th} harmonic = \frac{ n }{ 2 } loops }$$

In kth overtone,
$$
\begin{split}
\ce{ 
nodes &= k +1 \\
anti-nodes &= k +1
 }
\end{split}
$$




