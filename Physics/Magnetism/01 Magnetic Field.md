Links: 
___
# Magnetic Field $\vec{B}$
The region in which magnetic effects are present is called the Magnetic Field. 

Strength of magnetic field / magnetic induction / magnetic flux density is represented by $\vec{B}$ and is a vector quantity just like Electric Field.

The region where $\vec{B} = 0$, there are no magnetic effects. 

Magnetic field is defined as magnetic force experienced per unit pole strength. 
$$\vec{B} = \frac{ \vec{f}_{m} }{ m }$$

Its unit is Tesla ($\ce{ N A^{-1}m^{-1} }$) or Weber/$m^{2}$. Its dimensions are $\ce{ [MI^{-1}T^{-2}] }$.

![[Pasted image 20240110210351.png]]


A pole $+m$ experiences a force of $m\vec{B}$ *in the direction* of the magnetic field. 
A pole $-m$ experiences a force of $m\vec{B}$ *in the opposite direction* of the magnetic field. 

## B due to Various Objects 
#### B due to Monopole
[[02 Electric Field#E due to Point Charge]]

It follows all the usual laws as in electric field. 
$$
\begin{split}
B &\propto m \\
&\propto \frac{ 1 }{ r^{2} }\\
\\
B &= \frac{ km }{ r^{2} }
\end{split}
$$

Here,
$$k = \frac{ \mu_{o} }{ 4\pi }$$
where $\mu_{o}$ is **Permeability of Free Space** and has value,
$$\mu_{o} = 4\pi \times 10^{-7}\ \ce{ \frac{ N }{ A^{2} } }$$

Thus giving,
$$B = \frac{\mu_{o}}{4\pi} \frac{m}{r^{2}}$$
And in vector form, 
$$\vec{B} = \frac{ \mu_{o} }{ 4\pi } \frac{ m }{ r^{3} } \vec{r}$$

![[Pasted image 20240111162811.png]]

If the pole is South Pole, the field is radially inwards.
![[Pasted image 20240111162831.png]]

#### B due to Bar Magnet 
i.e. B due to Magnetic Dipole 
The formulas are exactly the same as in [[08 Electric Dipole]] with the terms interchanged. 

**At axis,**
$$B_{ax} = \frac{ 2kM }{ r^{3} } = 2 \frac{ \mu_{o} }{ 4\pi } \frac{ M }{ r^{3} }$$
In vector form,
$$\vec{B}_{ax} = 2 \frac{ \mu_{o} }{ 4\pi } \frac{ \vec{M} }{ r^{3} }$$

**On equatorial plane,**
$$B_{eq} = \frac{ kM }{ r^{3} } = \frac{ \mu_{o} }{ 4\pi } \frac{ M }{ r^{3} }$$
In vector form,
$$\vec{B}_{eq} = - \frac{ \mu_{o} }{ 4\pi } \frac{ \vec{M} }{ r^{3} }$$

![[Pasted image 20240111163429.png]]

**At any general point,**
$$B = \frac{ \mu_{o} }{ 4\pi } \frac{ M }{ r^{3} } \sqrt{ 1 + 3\cos ^{2} \theta }$$

![[Pasted image 20240111163447.png]]

![[Pasted image 20240111164150.png]]
(in the final expression it is $r ^{4}$)

#### B due to Moving Charge 
Experimental, thus no proof. 

A moving charge creates magnetic field. 

A point charge creates magnetic field when it moves. There is no magnetic field in the direction of velocity.

$$
\begin{split}
B &\propto q \\
&\propto v \\
&\propto \sin \theta \\
&\propto \frac{ 1 }{ r^{2} }
\end{split}
$$
where $\theta$ is angle between $\vec{r}$ and $\vec{v}$

Finally we get,
$$B = \frac{\mu_{o}}{4\pi} \frac{ qv\sin \theta }{ r^{2} }$$

In vector form,
$$\vec{B} = \frac{\mu_{o}}{4\pi} \frac{ q (\vec{v} \times \vec{r}) }{ r^{3} }$$
(q is with sign)

If charge is +ve, the magnetic field is in the direction of $\vec{v} \times \vec{r}$. I.e. $\perp$ to the plane containing v and r.

To show B going inside the paper, we use $\otimes$ and to show it coming outside, we use $\odot$
$$\underbrace{ \bigodot }_{ out } \underbrace{ \bigotimes }_{ in }$$

![[Pasted image 20240111164650.png]]

### [[01.1 Current carrying Wire]]

### [[01.2 Current Carrying Circular Loop]]

### Solenoid
A non-conducting cylinder wrapped with a wire. 

Total no. of turns is N, turns per unit length is n and the thickness of each turn is t.

We can write,
$$n = \frac{ N }{ l }$$

The length of the solenoid can be given as,
$$l = Nt$$
Thus n can be written as,
$$n = \frac{ N }{ l } = \frac{ l }{ tl } = \frac{ 1 }{ t }$$

![[Pasted image 20240112102313.png]]

Magnetic field inside the solenoid at point P,
$$B = \frac{ \mu_{o}ni }{ 2 } (\cos \theta_{1} + \cos \theta_{2})$$

We can derive this by taking an element of dx thickness x distance from P, writing the field at P due to this element, and then integrating over the length of the solenoid. 

#### Ideal Solenoid 
The length of solenoid is very large as compared to radius. 

The angle subtended by the edges will be close to zero at mid points.

Thus the magnetic field becomes,
$$B = \mu_{o}ni$$

But at the edges, one of the angles will be 0, while the other will be 90. Thus magnetic field is,
$$B_{e} = \frac{\mu_{o}ni}{2}$$
Which is half that of mid points. 

We can say that the middle region has uniform magnetic field, as we get close to the edges, the uniformity is lost. 

![[Pasted image 20240112103211.png]]

## Magnetic Line of Force (MLOF)
[[02 Electric Field#Electric Lines of Force (ELOF)]]

It can be a line or a curve. 

Tangent at any point on the MLOF gives direction of magnetic field. 

Wherever there is more line density, there is more magnetic field.

![[Pasted image 20240112101156.png]]
