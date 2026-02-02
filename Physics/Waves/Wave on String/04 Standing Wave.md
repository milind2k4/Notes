Links: [[00 Waves]], [[01 Equation and Speed of Wave]]
___
# Standing Wave
Two waves having same frequency travelling in opposite direction and having preferably same amplitude, if superimposed, form a Standing Wave.

Let the two waves be, 
$$y_{1} = A\sin(\omega t - kx)$$
$$y_{2} = A\sin(\omega t + kx)$$

Then the resulting wave is,
$$
\begin{split}
y &= y_{1} + y_{2} \\ 
&= A(\sin(\omega t + kx) + \sin(\omega t - kx)) \\ 
&= A(2\sin\omega t\cos kx) \\ 
y &= 2A\sin\omega t \cos kx
\end{split}
$$
This is not a travelling wave as it is not of the form $y = f(t-x /v)$. 

But it is a wave as it satisfies,
$$\frac{ \partial^{2} y }{ \partial t^{2} } = v_{w}^{2} \frac{ \partial^{2} y }{ \partial x^{2} } $$

These waves are called *standing or stationary waves.* 

![[Pasted image 20240126204938.png]]

$$
\begin{split}
y &= 2A\cos kx \sin \omega t \\
&= A'\sin\omega t
\end{split}
$$

Every particle is doing SHM, but not all of them have the same A. 
$$
\begin{split}
A' &= 2A\cos kx \\
&= 2A \cos \frac{ 2\pi }{ \lambda }x
\end{split}
$$
Thus there will be some particles which do not perform SHM as they will have zero A. 

The points which are fixed, i.e. those which have no amplitude (A' = 0) are called **Nodes.**
For this,
$$
\begin{split}
2A \cos kx &= 0 \\
kx &= \frac{ \pi }{ 2 } + n\pi \\
x &= (2n+1) . \frac{ \lambda }{ 4 }
\end{split}
$$
I.e.,
$$x = \frac{ \lambda }{ 4 }, \frac{ 3\lambda }{ 4 }, \frac{ 5\lambda }{ 4 } \dots$$

The particles which have the most amplitude (A' = $\pm$ 2A) are called **Anti-Nodes.**
$$
\begin{split}
2A\cos kx &= \pm 2A \\
\cos kx &= \pm 1 \\
kx &= n\pi \\
x &= \frac{ n\lambda }{ 2 }
\end{split}
$$
I.e.,
$$x = 0, \frac{ \lambda }{ 2 }, \lambda, \frac{ 3\lambda }{ 2 }, 2\lambda \dots$$

Thus in the middle of two consecutive Anti-Nodes, there is a node and vice versa. 

#### Motion of String
We have, equation of wave,
$$
\begin{split}
y &= 2A\cos kx \sin \omega t \\
&= 2A \cos \left( \frac{ 2\pi }{ \lambda }x \right) \sin \left( \frac{ 2\pi }{ T }t \right)
\end{split}
$$

The particles which are at Anti-Nodes will have the most velocity as they have the most amplitude and we know that,
$$v_{p} = A\omega$$
when particle is at mean position. 

From the below diagram, we can see that the phase difference between two cycles ($\lambda /2$ dist. apart) is $\pi$.

![[Pasted image 20240125214114.png]]

#### Points to Note
Separation between two consecutive nodes or anti nodes is $\lambda /2$.
Separation between consecutive node and anti node is $\lambda /4$.
An anti node will lie at the exact mid point of two consecutive nodes and vice versa. 

The particles in between two nodes are performing SHM in the same phase (i.e. they reach their respective extremes and mean at the same time or they are in phase). 

The loops on either side of a node will oscillate with a phase difference of $\pi$. I.e. they are out of phase. 

The power of nodes is zero as they have no velocity. Thus, the energy of string between any two nodes will be constant.

This can also be understood by the fact that both the two initial waves will carry the same power, but in opposite directions. So, the net power consumed will be zero. 

At extreme, all the energy is Elastic potential, and at mean, all the energy is Kinetic. Thus the total energy is fixed. 



