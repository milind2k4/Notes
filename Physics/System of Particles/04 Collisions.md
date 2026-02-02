Links: [[03 Impulse]]
___
# Collisions
Collision is redistribution of linear momentum between interacting bodies due to some internal force.

- **[[04.1 Head on Collision|Head-on Collision:]]** Line of motion and line of impact coincides. i.e. after collision, the line of motion is the same. 
- **[[04.2 Oblique Collison|Oblique Collision:]]** Line of motion and line of impact may not coincide. Line of motion before and after collision may be different. 

Depending on nature of Colliding bodies, we divide collision into 3 parts,
- **Elastic Collision:** Shape, size and geometry of elastic bodies remain the same after the collision. 
  There is no deformation in the body after collision. 
  $\\$
  
- **Inelastic Collision:** Inelastic bodies deform during collision, tries to regain its original shape, size and geometry but cannot regain it exactly. 
  Finally inelastic bodies will have some deformation after collision.
  $\\$
  
- **Perfectly Inelastic Collision:** PI bodies deform during collision and does not try to regain its original shape, size or geometry. 
  There is max. deformation after collision.

#### Lines
**Line of Motion:** Line along which the object is moving. 

**Line of Impact:** Line along which interacting bodies are applying force on each other. It may or may not be the same as the line of motion. If geometry is given, then line of impact is along common normal.

![[Pasted image 20230706120656.png]]

### Process of Collision
It consists of Process of Deformation then Process of Reformation. 

There is max. deformation when the velocity of both the objects is the same. 

Using momentum conservation,
$$m_{1}u_{1} + m_{2}u_{2} = m_{1}v_{1} + m_{2}v_{2}$$
For common velocity,
$$m_{1}u_{1} + m_{2}u_{2} = (m_{1} + m_{2})v$$
$$v = \frac{ m_{1}u_{1} + m_{2}u_{2} }{ m_{1} + m_{2} }$$

![[Pasted image 20230706123802.png]]

We cannot conserve total mechanical energy in general. This is because energy is consumed when the bodies are deformed. 
We can only conserve total mechanical energy in the case of Elastic Collision. 

For other collisions, the initial TME is more than final TME. The loss in TME is the heat dissipate in the form of heat, sound, light etc. This loss in TME is called **Deformation Potential Energy.**

**Coefficient of Restitution (e)** is defined as the ratio of impulses during reformation and deformation,
$$e = \frac{ \text{impulse of reformation} }{ \text{impulse of deformation} }$$
$$e = \frac{ \int N_{r} \, dt  }{ \int N_{d} \, dt  }$$
Using impulse momentum theorem,

$$
\begin{split}
e &= \frac{ m_{2}v_{2} - m_{2}v_{com} }{ m_{2}v_{com} - m_{2}u_{2} } \\
&= \frac{ v_{2} - v_{com} }{ v_{com} - u_{2} } \\ 
\\
&= \frac{ v_{2} - \displaystyle \frac{ m_{1}u_{1} - m_{2}u_{2} }{ m_{1} + m_{2} } }{ \displaystyle \frac{ m_{1}u_{1} - m_{2}u_{2} }{ m_{1} + m_{2} } - u_{2} } \\
&= \frac{ m_{1}v_{2} + m_{2}v_{2} - m_{1}u_{1} - m_{2}u_{2} }{ m_{1}u_{1}+m_{2}u_{2} - m_{1}u_{2} - m_{2}u_{2} } \\
\\
&= \frac{ m_{1}v_{2} + m_{2}v_{2} - m_{1}v_{1} - m_{2}v_{2} }{ m_{1}u_{1} - m_{1}u_{2} } \\
&= \frac{ v_{2} - v_{1} }{ u_{1} - u_{2} }
\end{split}
$$

Thus, coefficient of restitution will be,
$$e = \frac{ v_{2} - v_{1} }{ u_{1} - u_{2} }$$
This can also be written as,
$$e = \frac{ \text{velocity of sep. after collision} }{ \text{velocity of appr. before collision} }$$

### Elastic Collision 
Here coefficient of restitution is always 1. That is, the reformation impulse is the same as deformation impulse. 

There is no deformation in the end and thus the body regains its shape, size and geometry. Thus the deformation potential energy is zero. 

Thus we can conserve total mechanical energy. 
$$K_{i} = K_{f}$$

![[Pasted image 20230706131951.png]]
(the second one is refr not defr and the time interval is very small)

Velocity of separation after collision is the same as velocity of approach before collision.

### Inelastic Collision 
Here, $0 < e < 1$. 

Thus impulse of reformation is less than impulse of deformation but is not zero. 

There will be some deformation finally after collision. Thus there is some deformation potential energy (DPE). And thus, we cannot conserve TME,
$$K_{i} > K_{f}$$
$$K_{i} - K_{f} = DPE = \text{heat, sound etc.}$$

![[Pasted image 20230706132525.png]]

Velocity of separation is less than velocity of approach.

### Perfectly Inelastic Collision 
Here e is zero. Thus there is no impulse of reformation and the bodies stay deformed. 

Here the deformation and thus DPE is the max.. 
Loss in KE is max..
$$K_{i} - K_{f} = DPE$$

![[Pasted image 20230706132926.png]]

Velocity of separation is zero. And thus the bodies stick together. 
