Links: [[01 Newton's Laws]]
___
# Dynamics
#### Force
Any push or pull is called a Force. It is a vector quantity. 

SI unit: Newton (N), $\ce{ kg m s^{-2} }$
CGS unit: Dyne $\ce{ g cm s^{-2} }$

$1\ \ce{ N } = 10^{5}\ \ce{ dyne }$
$1\ \ce{ kgf } = 9.8 \ce{ N } \approx 10\ \ce{ N }$

Dimensionally, $\ce{ [MLT^{-2}] }$

#### Effects of Force
1. It can change magnitude of velocity
2. It can change direction of velocity
3. It can change the shape and size of an object. 

### Two categories of Force
1. Field Force: Forces which does not require contact. eg. Electromagnetic force. 
2. Contact Force: Forces which require contact. eg. Normal force, frictional force. 

### There are 4 fundamental Forces
[[02 Forces#Gravitational force]]
[[02 Forces#Electromagnetic force]]
[[02 Forces#Strong Nuclear Force]]
[[02 Forces#Weak Nuclear Force]]


## Free Body Diagram
Diagram in which all the forces all the forces on body are shown. The forces exerted by the body are not shown. We can show the body by a dot. 

For example, for a body on an inclined plane,  the normal is at an angle $\theta$ from the vertical. 
![[Pasted image 20230526121859.png]]

This works everywhere,
![[Pasted image 20230526122220.png]]   

FBD for a non-ideal string,
![[Pasted image 20230526122826.png]]

### Equilibrium
When the net force on the body is zero and thus the acceleration is zero. 

It is of two types, 
1. **Static:** $\vec{v} = 0, \vec{a} = 0, \vec{f} = 0$: *Rest*
2. **Dynamic:** $\vec{v} \neq 0, \vec{a} = 0, \vec{f} = 0$: *Uniform motion*

We can use this to find normal forces,
![[Pasted image 20230526123734.png]]

In a system, all the internal forces cancel out and thus are ignored. If a system is in equilibrium, then all the forces in every direction cancel out. 

We can get the answer using triangle law of vector addition and Sine law also. But there should be 3 forces,
![[Pasted image 20230527124921.png]]

- **Lami's Theorem:** #formula 
	It is a modified version of Sine law, and thus only applies when there are 3 forces, and the net force is zero. 
	
	It says that,
	$$\frac{ f_{1} }{ \sin \alpha } = \frac{ f_{2} }{ \sin \beta } = \frac{ f_{3} }{ \sin\upgamma }$$
	where $\alpha, \beta, \upgamma$ are angles opposite to the forces. 
	
	![[Pasted image 20230527125204.png]]


## NLM on a System
If there is a system with n particles with forces on each, those being $f_{1} = m_{1}a_{1}, f_{2} = m_{2}a_{2}, f_{3} = m_{3}a_{3}, f_{4} = m_{4}a_{4} \dots f_{n} = m_{n}a_{n}$. Then the net force on ths system is,
$$f_{net} = \sum_{i=1}^{n} m_{i}a_{i}$$

This net force is made up of internal and external forces. The internal forces cancel each other out, due to action reaction pairs. Thus,
$$f_{ext} = \sum_{i=1}^{n} m_{i}a_{i}$$

We can also apply this along specific directions,
$$
\begin{split}
(f_{ext})_{x} &= \sum_{i=1}^{n} m_{i}a_{ix} \\
(f_{ext})_{y} &= \sum_{i=1}^{n} m_{i}a_{iy} \\
(f_{ext})_{z} &= \sum_{i=1}^{n} m_{i}a_{iz} \\
(f_{ext})_{ip} &= \sum_{i=1}^{n} m_{i}a_{i(ip)}
\end{split}
$$

Example,
![[Pasted image 20230601131432.png]]

## Atwood Machine
If the pulley is smooth, then the tension at all the points on the string wound on it will be the same. And the bodies will have the same net force, but in opposite directions. 

$$a = \frac{ (m_{1} - m_{2})g }{ m_{1} + m_{2} }$$
$$T = \frac{ 2m_{1}m_{2}g }{ m_{1} + m_{2} }$$

![[Pasted image 20230529130933.png]]

We can also prove this using [[03 Energy#Work Energy Theorem]],
![[Pasted image 20230614121303.png]]

To apply newtons laws along the string, straighten it. 
![[Pasted image 20230529132817.png]]

Corner of Table situation,
![[Pasted image 20230529133253.png]]