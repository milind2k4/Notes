Links: [[00 Electromagnetic Induction]]
___
# Induction of EMF
## Motional emf
### Conducting Rod 
If a conducting rod is cutting MLOF, then and emf is induced across its ends. 

In time dt, the rod moves forward a distance $v dt$. Now, since this rod has moved, it has cut some flux. 

The emf induced is thus,
$$
\begin{split}
\varepsilon &= \frac{ d\phi }{ dt } \\
&= \frac{ Blv dt }{ dt } \\
&= vBl
\end{split}
$$

The direction of $\vec{v} \times \vec{B}$ provides higher polarity. 

![[Pasted image 20240117170939.png]]

![[Pasted image 20240117171740.png]]

**If the velocity is not perpendicular to the length, but has an angle $\theta$,**

In time dt, the rod travels a distance $vdt$. 
Thus we have,
$$
\begin{split}
\varepsilon &= \frac{ d\phi }{ dt } \\
&= \frac{ B l vdt \sin \theta }{ dt } \\
&= vBl\sin \theta
\end{split}
$$

And, if any two of $\vec{l}, \vec{v}, \vec{B}$ are parallel, no MLOF will be cut and thus emf induced will be zero. 

![[Pasted image 20240117171328.png]]

For a random shaped rod, we will join the ends of the rod by a straight line and find the emf across it. This will be the emf across the randomly shaped rod. 

![[Pasted image 20240117171550.png]]

#### Emf Induced in Rotating Rod
Small emf generated in a small rod element dx,
$$d\varepsilon = Bvdx = \omega x B dx$$

Thus, for the whole rod,
$$
\begin{split}
\varepsilon &= \int d\varepsilon \\
&= B \omega \int_{0}^{l} x \, dx \\
&= \frac{ B\omega l^{2} }{ 2 } 
\end{split}
$$

This is valid only one one of the ends is fixed. 

![[Pasted image 20240117172140.png]]

**Alternatively, using the basic definition,** 

In a small time interval the rod will travel angle $d\theta = \omega dt$. 

Now, the rod has cut flux in this region. Thus the emf is,
$$
\begin{split}
\varepsilon &= \frac{ d\phi }{ dt } \\
&= \frac{ B l^{2}(\omega dt) }{ 2dt } \\
&= \frac{ B\omega l^{2} }{ 2 }
\end{split}
$$

This is valid when one point is fixed. 

![[Pasted image 20240117172512.png]]

### Rectangular Loop
A conducting loop is moved into a region of magnetic field B with a constant speed v.

When the loop is outside the field, the emf induced is zero. 
As the loop is entering the field, the area passing through the field is increasing and thus the flux is increasing, inducing an emf. 

Let, at some time t, 
$$\phi = Blx$$
then after time dt, the new flux is,
$$\phi + d\phi = Bl(x + v dt)$$

Now, change in flux is,
$$d\phi = Blv dt$$

And thus, the emf induced is,
$$\varepsilon _{ind} = \frac{ d\phi }{ dt } = Blv$$

After the loop is completely inside the field, the induced emf becomes zero as flux becomes constant. 

Then, as the loop is exiting, the flux is decreasing and thus there will be induced emf. This emf will have reverse polarity as that when the loop was entering the field. 

Also, there will be a force while entering and exiting the field which will try to keep the loop from entering or exiting respectively. 

![[Pasted image 20240116174842.png]]

##### Derivation for Boards
The flux associated with the loop is given by,
$$\phi = Blx$$
Now, as the rod is moving, x is constantly changing and thus there is an induced emf in the rod,
$$\varepsilon = -\frac{ d\phi  }{ dt }$$
$$\varepsilon = Bl\frac{ d(-x) }{ dt }$$
$$\varepsilon = Blv$$

### Emf Induced in Rotating Coil
A loop of n turns is placed in a magnetic field and rotated with a constant angular velocity $\omega$. 

The flux is,
$$
\begin{split}
\phi &=  \vec{B}.\vec{A} \\
&= BA \cos\omega t \\
\end{split}
$$
And thus the emf induced is,
$$
\begin{split}
\varepsilon &= \left| \frac{ d\phi }{ dt }  \right| \\
&= BA\omega \sin \omega t 
\end{split}
$$
Thus, 
$$\varepsilon_{max} = BA\omega$$
This is the same as in alternating current. 

The electricity that comes in our house comes through this method. 

![[Pasted image 20240117165000.png]]


### Emf Induced in Rotating Disc
The axis of rotation and magnetic field are perpendicular to the plane of the disc. 

Due to centrifugal and magnetic forces, the e will be pushed towards the periphery of the disc. Due to this movement of e, around the centre, there will be +ve charge. 

Thus there will be charge difference and thus electric field. 

At one point the force on e due to electric field will balance the outward force,
$$
\begin{split}
eE_{ind} &= m\omega^{2}x + e\omega Bx \\
E_{ind} &= \frac{ m\omega^{2}x }{ e } + \omega Bx 
\end{split}
$$

Now, the potential difference will be,
$$
\begin{split}
V &= \int Edx \\
&= \int_{0}^{R} \frac{ m\omega^{2}x }{ e }dx + B\omega xdx \\
\varepsilon &= \frac{ m\omega^{2}R^{2} }{ 2e } + \frac{ B\omega^{2}R^{2} }{ 2 } 
\end{split}
$$

Now, the value of $m /e$ is very very small, and thus we can write,
$$\varepsilon = \frac{ B\omega^{2}R }{ 2 }$$
This is valid when one point is fixed. 

![[Pasted image 20240117174254.png]]
![[Pasted image 20240117174305.png]]


In [[08 Pure Rolling]], we can use the concept of [[07 Combine Motion#Instantaneous Axis of Rotation|IAR.]]
![[Pasted image 20240117174815.png]]