Links: [[01 Centre of Mass#Linear Momentum]]
___
# Angular Momentum
Similar to [[02 Torque]].

#### About a Point 
$$\vec{L} = \vec{r} \times \vec{P}$$
$$\vec{L} = m(\vec{r} \times \vec{v})$$
where $\vec{r}$ is the vector whose head is at the object whose angular momentum is to be calculated and tail is at the point about which it is calculated. 

Thus angular momentum is a vector which is perpendicular to $\vec{r}$ and $\vec{v}$.  I.e. $\vec{L}$ is perpendicular to the plane containing $\vec{r}$ and $\vec{v}$.  

It is an axial vector. 
The direction can be found using right hand thumb rule. 

It has unit $\ce{ kg m^{2} s^{-1} }$ and dimensions, $\ce{ [ML^{2}T^{-1}] }$

![[Pasted image 20230729130157.png]]

##### Magnitude of $\vec{L}$
$$
\begin{split}
L &= |m(\vec{r} \times \vec{v})| \\
&= mrv\sin \theta \\
&= mr_{\perp}v \\
&= mrv_{\perp}
\end{split}
$$
$r_{\perp}$ is the separation between the LOM and the point.

If line of motion passes through the point about which $\vec{L}$ is to be written, then $\vec{L}$ will be zero. 

![[Pasted image 20230729125751.png]]

#### About an Axis 
Find $\vec{L}$ about any point on the axis. The component of this $\vec{L}$ which is parallel will be the angular momentum about the axis. 

If particle is moving parallel to the axis, there is no angular momentum. 
If line of motion intersects the axis, there is no angular momentum. 

If the line of motion and the axis are skew lines, then there will be angular momentum. 
$$\vec{L} = mvr_{\perp}$$

Thus similar to torque. 

## $\vec{L}$ of body performing pure Rotational Motion 
$$
\begin{split}
L &= m_{1}(\omega r_{1})r_{1} + m_{2}(\omega r_{2})r_{2} + \dots \\
&= (m_{1}r_{1}^{2} + m_{2}r_{2}^{2} + \dots)\omega \\
&= I\omega
\end{split}
$$

Thus,
$$\vec{L} = I\vec{\omega}$$
which is analogous to $\vec{P} = m\vec{v}$

Now kinetic energy,
$$
\begin{split}
K &= \frac{ 1 }{ 2 } I\omega^{2} \\
&= \frac{ (I\omega)^{2} }{ 2I } \\
&= \frac{ L^{2} }{ 2I }
\end{split}
$$
which is analogous to $K = P^{2} /2m$

## Angular Momentum Conservation Theorem (AMCT)
Torque is rate of change of angular momentum. 

$$\vec{\tau} = \frac{ d\vec{L} }{ dt } $$
If $\vec{\tau} \parallel \vec{L}$, it will increase $\vec{L}$.
If $\vec{\tau} \upharpoonleft \! \downharpoonright \vec{L}$, it will decrease $\vec{L}$.
$\vec{\tau}$ perpendicular to $\vec{L}$ is responsible for changing the direction of $\vec{L}$.

If torque on a system is zero, $d\vec{L}$ is zero and thus AM is conserved,
$$\vec{L}_{i} = \vec{L}_{f}$$

For example,
![[Pasted image 20230729134855.png]]

### Examples 
When the colliding particle stops,
![[Pasted image 20230729165542.png]]
![[Pasted image 20230729165559.png]]

When the colliding particle sticks,
![[Pasted image 20230729170357.png]]
![[Pasted image 20230729170411.png]]

When e is given,
![[Pasted image 20230729171442.png]]

Bead on rod problem,
![[Pasted image 20230729172912.png]]

![[Pasted image 20230729174331.png]]
![[Pasted image 20230729174345.png]]