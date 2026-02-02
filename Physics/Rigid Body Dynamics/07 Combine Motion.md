Links: [[02 Torque]], [[00 Dynamics]]
___
# Combined Translational and Rotational Motion (CTRM)
The axis is not fixed. 

## Kinematics of CTRM
#### Velocity 
To find velocity of any point wrt ground, we find the velocity of that particle wrt the point whose velocity is known and then add the velocity like in [[00 Relative Motion]].

Alternatively, we can separate the rotational and translational motion and then add the respective velocities. 

![[Pasted image 20230729175102.png]]

Example,
![[Pasted image 20230729175212.png]]

The velocity can also be found by breaking the motion into translational and rotational motion,
![[Pasted image 20230729175725.png]]
![[Pasted image 20230729175958.png]]
![[Pasted image 20230729180119.png]]

#### Acceleration 
Similar to velocity, we can find acceleration of particle by adding the acceleration of it wrt a point whose acceleration we know and the acceleration of the point. 

Alternatively we can separate the motion and then add the accelerations vectorially. 

![[Pasted image 20230729180427.png]]

Here, the final acceleration will be vector sum of 3 vectors,

![[Pasted image 20230729180643.png]]

### Kinetic Energy 
Total kinetic energy is the sum of translational and rotational kinetic energies. 

$$K = \frac{ 1 }{ 2 }mv^{2} + \frac{ 1 }{ 2 }I_{com}\omega^{2}$$

![[Pasted image 20230801153632.png]]

## Rolling 
It is an example of CTRM. 

### [[08 Pure Rolling|Pure Rolling]]

### Rolling on Inclined Plane with Slipping 
The inclined plane is not enough rough. We release an object of circular cross section of moment of inertia, $I_{com} = mk^{2}$ (k is radius of gyration) from height H.

Acceleration of COM,
$$
\begin{split}
mg\sin \theta - \mu mg\cos \theta &= ma \\
a&= g (\sin \theta - \mu \cos \theta)
\end{split}
$$
Which is independent of $k$. Due to this, all will have same acceleration and will reach the ground at the same time and with same speed. 

Angular Acceleration,
$$
\begin{split}
\tau_{com} &= I_{com}\alpha \\
\mu mg\cos \theta R &= mk^{2}\alpha \\
\alpha &= \frac{ \mu g\cos \theta R }{ k^{2} }
\end{split}
$$
Thus the least is the $k$ the more is $\alpha$. 

Time taken to reach base,
$$
\begin{split}
\frac{H}{\sin \theta} &= 0 + \frac{1}{2}g(\sin \theta - \mu \cos \theta)t^{2} \\
t &= \sqrt{ \frac{ 2H }{ g(\sin ^{2} \theta - \mu \sin \theta \cos \theta) } }
\end{split}
$$

Velocity when it reaches base,
$$
\begin{split}
v^{2} &= 0 + 2g(\sin \theta + \mu \cos \theta) \frac{ H }{ \sin \theta } \\
v &= \sqrt{ 2gH(1 - \mu \cot \theta) }
\end{split}
$$

Angular velocity when it reaches ground,
$$
\begin{split}
\omega &= \omega_{o} + \alpha t \\
\omega &= \frac{ \mu g\sin \theta R }{ k^{2} } \sqrt{ \frac{ 2H }{ g(\sin ^{2} \theta - \mu \sin \theta \cos \theta) } }
\end{split}
$$

Thus the lower is the k, the higher is the angular velocity and thus higher is the kinetic energy. 

![[Pasted image 20230811161725.png]]
![[Pasted image 20230811161739.png]]

Work done by kinetic friction,
![[Pasted image 20230821124923.png]]
Or alternatively we can use WET.
$$W_{g} + W_{N} + W_{f} = K_{f} - K_{i}$$
$$mgH + W_{f} = K_{f}$$

## Dynamics of CTRM
We will write torque about COM,
$$\vec{\tau}_{com} = I_{com} \vec{\alpha}$$
Take care to write the torque of all the forces.

There is an **Instantaneous Axis of Rotation** when there is pure rolling on fixed surface, which will be the point of contact. So we find torque about this point to find $\alpha$ or $a$ quickly. But take care when writing I. 

We will separate KE into two parts,
$$K = \frac{ 1 }{ 2 }mv_{com}^{2} + \frac{ 1 }{ 2 } I_{com}\omega^{2}$$

### Instantaneous Axis of Rotation 
Axis about which a body performing CTRM can be assumed to be performing pure rotational motion. 

![[Pasted image 20230821125708.png]]

To find IAR, we find the point abut which the velocity is zero. 
Or we can draw lines which are perpendicular to the velocities of some points, and where they meet is the IAR. 

![[Pasted image 20230821131147.png]]

### Examples
![[Pasted image 20230801171223.png]]

Alternatively, we can find torque about the point of contact. 
![[Pasted image 20230801171747.png]]

\
![[Pasted image 20230801172418.png]]

\
![[Pasted image 20230808172537.png]]

\
![[Pasted image 20230808173540.png]]
![[Pasted image 20230808173553.png]]

\
![[Pasted image 20230821134247.png]]
![[Pasted image 20230821134302.png]]
![[Pasted image 20230821134342.png]]
![[Pasted image 20230821134312.png]]

## Angular Momentum of Body Performing CTRM
We can divide the motion into two parts, and while adding them, we take care of direction.
$$\vec{L} = \vec{L}_{T} + \vec{L}_{R}$$
For $\vec{L}_{T}$, assume the whole body to be at the COM.

$$\vec{L} = m (\vec{r} \times \vec{v}) + I_{com} \vec{\omega}$$
where r is position vector whose head is at the COM and tail at the point about which AM is to be calculated. 

![[Pasted image 20230821132312.png]]
![[Pasted image 20230824125818.png]]
![[Pasted image 20230824130248.png]]

