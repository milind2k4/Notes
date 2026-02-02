Links:  [[00 Simple Harmonic Motion]], [[01 Equation of SHM]]
___
# Angular SHM
![[Pasted image 20231011160140.png]]

Here instead of restoring force, we have restoring torque which is directly proportional to angular displacement. 

Here instead of amplitude, we have Angular Amplitude, $\theta_{o}$.

Torque,
$$\tau = -c \theta_{o}$$

Differential equation,
$$
\begin{split}
I \frac{ d^{2} \theta }{ d t^{2} } &= - c \theta \\
\frac{ d^{2} \theta }{ d t^{2} } + \frac{ c }{ I }\theta &= 0 \\
\frac{ d^{2} \theta }{ d t^{2} } + \omega^{2}\theta &= 0
\end{split}
$$

#### Angular Position $(\theta)$
Solution of the differential equation is,
$$\theta = \theta_{o} \sin(\omega t + \phi)$$
where,
$\theta \to$ angular position which varies from $[-\theta_{o}, \theta_{o}]$
$\omega = c/I \to$ angular frequency.
$\omega t + \phi \to$ phase
$\phi \to$ initial phase/phase constant 

For different values of $\phi$, we get different starts to the angular SHM,
![[Pasted image 20231011161852.png]]

#### Angular Velocity $(\Omega)$
Differentiating angular position wrt time,
$$\Omega = \theta_{o} \omega \cos(\omega t + \phi)$$
Thus the max. value of $\Omega = \theta_{o}\omega$. 

Converting the cos to sin,
$$
\begin{split}
\Omega &= \theta_{o} \omega \sqrt{ 1 - \sin ^{2}(\omega t + \phi) } \\
&= \theta_{o} \omega \sqrt{ 1 - \frac{ \theta^{2} }{ \theta_{o}^{2} } } \\
&= \omega \sqrt{ \theta_{o}^{2} - \theta^{2} }
\end{split}
$$
which is the same as $v = \omega\sqrt{ A^{2} - x^{2} }$

Thus at extreme positions $\Omega$ will be zero and at mean it will be max..

#### Angular Acceleration $(\alpha)$ 
Differentiating angular velocity wrt time,
$$\alpha = -\theta_{o}\omega^{2}\sin(\omega t + \phi)$$
Thus,
$$\alpha = -\omega^{2} \theta$$
The max. value of $\alpha$ will be $\omega^{2}\theta_{o}$ at extremes and the min. value will be zero at mean position.

### Simple Pendulum
![[Pasted image 20231011165438.png]]

The hinge is smooth, the string massless and the bob dense so that in a small volume there is enough mass. 

Now,
$$\tau = -mgl\sin \theta$$
For sufficiently small $\theta$,
$$\tau = - mgl\theta $$
Thus the bob performs angular SHM.  

For time period,
$$
\begin{split}
I\alpha &= -mgl\theta \\
ml^{2}\alpha &= -mgl\theta 
\\
\alpha &= -\frac{ g }{ l }\theta 
\\
-\omega ^{2} &= - \frac{ g }{ l }
\\
\upomega &= \sqrt{ \frac{ g }{ l } } 
\\
T &= 2\pi \sqrt{ \frac{ l }{ g } }
\end{split}
$$

Alternatively, we can assume that the SHM is linear for very small angles. 
![[Pasted image 20231011170244.png]]

If the pendulum is inside a lift or is accelerating, then we use $g_{eff}$,
![[Pasted image 20231011170722.png]]


#### Second Pendulum
Time period = 2 seconds.

One second to reach one extreme from another mean position. 

$$
\begin{split}
T &= 2\pi \sqrt{ \frac{ l }{ g } } \\
2 &= 2 \pi \sqrt{ \frac{ l }{ g } } \\
l &= 1
\end{split}
$$

Thus, Length of string = 1 m.

### Very Long Pendulum 
When the length of string is in order of radius of earth. 

We displace the string by small angle $\theta$ and the displacement cause is small, being $x$.

In the tangential direction,
$$f_{t} = mg\sin(\theta + \phi)$$
which is the restoring force. 

If $x \to 0$ then $\theta \to 0$ and $\phi \to 0$, and we can write,
$$
\begin{split}
f_{t} &= mg(\theta + \phi) \\
&= mg\left( \frac{ x }{ l } + \frac{ x }{ l } \right) \\
&= mg\left( \frac{ 1 }{ l } + \frac{ 1 }{ l } \right)x \\
\end{split}
$$
Thus SHM is proved. 

Now, 
$$
\begin{split}
f_{t} &= ma \\
a &= g\left( \frac{ 1 }{ l } + \frac{ 1 }{ R } \right)x \\
\omega &= \sqrt{ g\left( \frac{ 1 }{ l } + \frac{ 1 }{ R } \right) }
\end{split}
$$
And thus, time period is,
$$T = \frac{ 2\pi }{ \sqrt{ g\left( \frac{ 1 }{ l } + \frac{ 1 }{ R } \right) } }$$

![[Pasted image 20231011171554.png]]

#### Infinitely Long Pendulum
In this case $l \to \infty$. 

And the time period thus becomes,
$$T = \frac{ 2\pi }{ \sqrt{ \frac{ g }{ R } } } = 2\pi \sqrt{ \frac{ R }{ g } }$$

If we put values of R and g,
$$T = 1600 \pi\ s = 83.73\ \ce{ min }$$

## Torsional Pendulum

![[Pasted image 20231011171916.png]]

Torsional wire is one which tries to regain its original shape, and in its case,
$$\tau \propto \theta$$
for small $\theta$.

We can write,
$$\tau = c \theta$$
where c is **Torsional Constant** and is property of wire. 

Now,
$$
\begin{split}
I\alpha &= c \theta \\
\alpha &= \frac{ c }{ I } \theta \\
\omega &= \sqrt{ \frac{ c }{ I } } \\
T &= 2\pi \sqrt{ \frac{ I }{ c } }
\end{split}
$$

## Physical/Compound Pendulum 
When an extended body is hinged from any other point than its centre of mass.

We will write torque on the body about the hinge and then equate it to $I\alpha$ to find $\alpha$ and thus $\omega$.

![[Pasted image 20231011180828.png]]

For any random body, if $l$ is the distance between hinge and COM, and $I_{h}$ is the moment of inertia of the body about hinge, then for small $\theta$,
$$
\begin{split}
\tau &= mgl\sin \theta \\
I\alpha &= mgl \theta \\
\alpha &= \frac{ mgl }{ I_{h} }\theta \\
\omega &= \sqrt{ \frac{ mgl }{ I_{h} } } \\
T &= 2\pi \sqrt{ \frac{ I_{h} }{ mgl } }
\end{split}
$$

![[Pasted image 20231011181526.png]]


##### Limiting Values of T
We know that,
$$I_{h} = I_{com} + ml^{2}$$
$$I_{h} = mk^{2} + ml^{2}$$
where k is radius of gyration.
Thus we can write,
$$T = 2\pi \sqrt{ \frac{ (k^{2} /l + l) }{ g } }$$

Thus,
$$l \to 0 \implies T \to \infty$$
$$l \to \infty \implies T \to \infty$$
If object is hinged very close or very far from the COM, the time period will be very large. 

##### Min. Time Period
For min. time period, we minimise,
$$
\begin{split}
f(l) &=  \frac{ k^{2} }{ l } + l \\
f'(l) &= -\frac{ k^{2} }{ l^{2} } + 1 = 0 \\
l &= k
\end{split}
$$
Thus the time period is min when $l$ is radius of gyration. 
This time period will be,
$$T_{min} = 2\pi \sqrt{ \frac{ 2k }{ g } }$$

The graph will be,
![[Pasted image 20231011182333.png]]

#### Examples 

![[Pasted image 20231016180007.png]]

![[Pasted image 20231016180408.png]]