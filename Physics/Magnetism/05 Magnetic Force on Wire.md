Links: 
___
# Magnetic Force on Current Carrying Wire

Small force on a small current carrying element is,
$$df = idlB\sin \theta$$
where $\theta$ is the angle between current element and B.

In vector form,
$$d\vec{f} = i(\vec{dl} \times \vec{B})$$

Thus the force is perpendicular to the plane containing dl and B. 

![[Pasted image 20240115174448.png]]

If the wire is long, we will integrate forces on small elements. 

$$
\begin{split}
d\vec{f} &= i(d\vec{l} \times \vec{B}) \\
f &= \int i(d\vec{l} \times \vec{B}) \\
&= i \int (d\vec{l} \times \vec{B})  
\end{split}
$$

![[Pasted image 20240115174651.png]]

#### Wire in Uniform Field 
If current carrying wire is in uniform magnetic field, we can take $\vec{B}$ out of the integral. 

$$
\begin{split}
d\vec{f} =&= i(d\vec{l} \times \vec{B}) \\
\vec{f} &= i ( \smallint d\vec{l} ) \times \vec{B}
\end{split}
$$

Now, this $\smallint d\vec{l}$ is the displacement vector connecting the end points of the wire. 

Thus we can write,
$$\vec{f} = i (\vec{l} \times \vec{B})$$

Since $\vec{l}$ is displacement, closed loop will experience no magnetic force in uniform magnetic field. 

![[Pasted image 20240115175013.png]]

![[Pasted image 20240115175400.png]]

### Magnetic Force between 2 Parallel Wires
Force on $i_{2}$ due to $i_{1}$. 

At each point of the 2nd wire, the magnetic field due to the first is the same. 

Thus the force will be,
$$
\begin{split}
f &= |i( \vec{l} \times \vec{B})| \\
&= \frac{ \mu_{o} i_{1}i_{2} }{ 2\pi r }l
\end{split}
$$

And force per unit length comes out to be,
$$\frac{ f }{ l } = \frac{ \mu_{o} i_{1} i_{2} }{ 2\pi r }$$

![[Pasted image 20240115180213.png]]

The force between the wires will be attractive if the currents are in the same direction and will be repulsive if the currents are in the opposite direction. 

![[Pasted image 20240115180228.png]]

### Wire in Non Uniform Field
Force is,
$$f = i \int (d\vec{l} \times \vec{B})$$

![[Pasted image 20240115181341.png]]

![[Pasted image 20240115181735.png]]

![[Pasted image 20240115182435.png]]

![[Pasted image 20240115182809.png]]

### Force and Torque on Loop 
Current carrying loop is placed in uniform magnetic field.

Since the loop is closed, $d\vec{l} = \vec{0}$ and thus $\vec{f} = 0$. 

Here, we will take the current carrying loop to be a bar magnet whose magnetic moment is,
$$\vec{M} = i \vec{A}$$

Thus, the torque will be, [[00 Magnetism#Bar Magnet in Uniform Magnetic Field]]
$$
\begin{split}
\vec{\tau} &= \vec{M} \times \vec{B} \\
&= i (\vec{A} \times \vec{B})
\end{split}
$$

![[Pasted image 20240115183135.png]]

![[Pasted image 20240115183656.png]] 

#### Rectangular Loop of n turns
A rectangular loop of n turns is placed in a uniform magnetic field. 
This loop has magnetic dipole moment,
$$M = ilbn$$

Now, if the angle between $\vec{M}$ and $\vec{B}$ is zero, $\tau = 0$, and potential energy, 
$$U = -MB = -ilbnB$$
which is the min. U, and thus it is a stable equilibrium position. 

Now, if this loop is rotated by a small angle $\theta$, it will experience a torque.
$$
\begin{split}
\tau &= MB\sin \theta \\
&= MB \theta \\
&= ilbnB \theta \\
I\alpha &= ilbnB \\
\alpha &= \frac{ ilbnB }{ I } \theta 
\end{split}
$$

![[Pasted image 20240115211953.png]]

### Examples
![[Pasted image 20240115213523.png]]
![[Pasted image 20240115213545.png]]

## Moving Coil Galvanometer
[[06 Instruments#Galvanometer/Micro-ammeter]]

Its name is on the Italian physicist, Luigi Galvani. 

It detects presence of current in wire and it can measure it if it is very small. 

It is based on the principle of torque on current carrying loop in a magnetic field. 

We take a coil of area A of n turns in a magnetic field which is connected to a spiral spring and pass current through it.

We will make sure that the magnetic dipole moment and field are perpendicular to each other. 

Now, when current passes through this loop, it will experience a torque.

$$
\begin{split}
\vec{\tau} &= \vec{M} \times \vec{B} \\
&= MB\sin 90^{\circ} \\
&= niAB 
\end{split}
$$
Thus,
$$\tau \propto i$$
which is the basic principle of the instrument. 

Now, due to the rotation, the spiral springs will apply a restoring torque which will be, 
$$\tau_{r} = c \theta$$
where c is called **Torsional Constant.**

At equilibrium,
$$
\begin{split}
c \theta &= niAB \\
\theta &= \frac{ niAB }{ c }
\end{split}
$$
That is,
$$i \uparrow \implies \tau_{m} \uparrow \implies \tau_{r} \uparrow \implies \theta \uparrow$$
$$\theta \propto i$$

We can attach a needle with the loop which will tell the amount of current by its rotation. 

And finally, we get current sensitivity, which is deflection/current,
$$\frac{ \theta }{ i } = \frac{ nAB }{ c }$$
(the more deflection per current there is, the more sensitive the galvanometer is)

![[Pasted image 20240115214734.png]]


**Acutual Construction,**
We use cylindrical/horseshoe magnet to create a radial magnetic field. 

We wrap the loop on a soft iron cylinder. 

The spiral springs are connected to the flat surfaces of the cylinder. 

![[Pasted image 20240115215627.png]]
![[Pasted image 20240115215644.png]]



