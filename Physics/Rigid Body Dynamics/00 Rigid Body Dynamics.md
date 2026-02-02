Links: [[00 Circular Motion]]
___
# Rigid Body Dynamics

Rigid body is one whose shape size and geometry are fixed. I.e. separation between any pair of point on the rigid body remains constant. 

![[Pasted image 20230710125202.png]]

This fixedness means that there is no relative velocity between two, or all the relative velocity is perpendicular to the line joining the points.
I.e. B is at rest wrt A or B is performing circular motion about A. 

We can thus define $\omega$,
$$\omega = \frac{ v_{BA} }{ r }$$

A rigid body has only one angular velocity and all the particles on it perform circular motion about each other with the same angular velocity. 

Here,  since $\theta$ is fixed,
$$\omega_{1} = \omega_{2}$$

![[Pasted image 20230710130123.png]]

This is the same for angular acceleration,
![[Pasted image 20230710130237.png]]

Every point does circular motion wrt every other particle with the same $\omega$ even if it does not seem so at first sight,
![[Pasted image 20230710130629.png]]

### Pure Translational Motion 
There is no rotation of the body and thus, displacements, velocities, acceleration of every point is the same, which is also the same as those of [[01 Centre of Mass]]. 

Here we can write KE simply as,
$$KE = \frac{ 1 }{ 2 } Mv^{2}$$

![[Pasted image 20230710131412.png]]

## Pure Rotational Motion
There is no translation of the body and thus there is only circular motion.

Axis is a line (actual or imaginary) on which each point is at rest. 

Since there is no translational motion, the velocities of particles farther from the axis will be more. The angular velocity however, will be the same for all the particles. 

Here, the kinetic energy (aka *Rotational KE*), can be given as,
$$
\begin{split}
K &= \sum  \frac{ 1 }{ 2 } m_{1}v_{1}^{2} \\
&= \sum  \frac{ 1 }{ 2 } m_{1}\omega^{2}r_{1}^{2} \\
&=  \frac{ 1 }{ 2 } \omega^{2} \sum  m_{1}r_{1}^{2} \\ 
&= \frac{ 1 }{ 2 } I \omega^{2}
\end{split}
$$

Where I is **Moment of Inertia** i.e.,
$$I = \sum _{i=1}^{n} m_{i}r_{i}^{2} = \int dm \, r^{2} $$
And is analogous to mass in translational motion. 

![[Pasted image 20230710132238.png]]

### Moment of Inertia 
When there are discrete particles,
$$I = \sum _{i=1}^{n} m_{i}r_{i}^{2}$$

Where there is continuous distribution,
$$I = \int dm \, r^{2} $$

Its unit is kg m$^{2}$ and is a non negative *scalar* quantity. 

It depends on the distribution of mass about axis. In general, the farther away is the mass from the axis, the more I will be.

It also depends on the axis, shape, geometry and density. 

For two particles, we have a term **Reduced mass** which is,
$$\mu = \frac{ m_{1}m_{2} }{ m_{1} + m_{2} }$$

For example, I about COM of two particles,
![[Pasted image 20230710133323.png]]

### [[01 MI of Cont. Bodies]]

## Radius of Gyration
If I is written as,
$$I = mk^{2}$$
Then Radius of Gyration is k.
$$k = \sqrt{ \frac{ I }{ m } }$$

It is a scalar quantity with unit $m$. 

This radius represents the distance from the axis at which if all the mass of the body is  to be assumed, the MI will be the same. 

![[Pasted image 20230712171636.png]]
![[Pasted image 20230712171630.png]]

For example, for a hollow sphere,
![[Pasted image 20230712171724.png]]

for a solid sphere,
![[Pasted image 20230712171820.png]]

Example,
![[Pasted image 20230712172049.png]]

## Toppling
For a block to be at equilibrium on an inclined plane, there should be a torque by normal which counters the torque by frictional force. Thus the normal is shifted down the inline.

![[Pasted image 20230824131015.png]]

*In case of toppling, normal passes through the edge.*

![[Pasted image 20230824131846.png]]

If force passes through COM, there will be no toppling as there is no tendency of rotation.
![[Pasted image 20230824132320.png]]

If however, the force does not pass through the COM, there is tendency of rotation and the object can topple.
![[Pasted image 20230824132603.png]]

![[Pasted image 20230824133230.png]]

## Examples
Questions related to MI are closely related to [[01 Centre of Mass]],
![[Pasted image 20230712115242.png]]

We can use "completing the shape" method to calculate MIs of various objects. Take care when taking the mass.
![[Pasted image 20230712162850.png]]

Sometimes we have to take many shapes to complete the shape. For example here we have to take 3 extra triangular plates. 
![[Pasted image 20230712163201.png]]
![[Pasted image 20230712163516.png]]


Take care to divide mass when dissecting a shape.
![[Pasted image 20230712165212.png]]
![[Pasted image 20230712165246.png]]

