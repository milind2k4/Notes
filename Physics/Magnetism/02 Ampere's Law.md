Links: [[01 Magnetic Field]]
___
# Ampere's Circuital Law
[[10 Electric Flux & Gauss Law#Gauss Law]]

Line integral of magnetic field is always equal to $\mu_{o}$ times the current passing through the loop. 

$$\oint \vec{B}.d\vec{l} = \mu_{o} \cdot i_{in}$$

If the currents are in multiple directions, then
1. Extend your fingers of the right hand in the direction of $d\vec{l}$
2. The currents which are in the direction of the thumb are taken as +ve while the others are taken as -ve. 

![[Pasted image 20240112103725.png]]

![[Pasted image 20240112103904.png]]

#### Proof
From Biot Savart's Law, the magnetic field duet to a long straight wire is,
$$B = \frac{ \mu_{o}i }{ 2\pi r }$$

Since $\vec{B}$ and $d\vec{l}$ are in the same direction for a straight wire,
$$\vec{B}.d\vec{l} = B.dl$$

Therefore,
$$
\begin{split}
\oint Bdl &=  \frac{ \mu_{o} I }{ 2\pi r } \oint dl \\
&= \frac{ \mu_{o} I }{ 2\pi r } . 2\pi r \\
\oint Bdl &= \mu_{o}I
\end{split}
$$

#### Infinitely Long Current Carrying Sheet
Here, we define, current per unit length,
$$k = \frac{ i }{ l }$$

We make an amperian loop of length l. 

$$
\begin{split}
\oint \vec{B}.d \vec{l} &= Bl + 0 + Bl + 0 \\
&= 2Bl \\
&= \mu_{o} (kl) \\
&= \frac{ \mu_{o} k }{ 2 }
\end{split}
$$

Thus, the field does not depend on distance from the sheet. 
The field will be uniform. 

![[Pasted image 20240112104806.png]]

### Ideal Toroid 
It is just an ideal solenoid, the ends of which are joined together. 

N is the total no. of turns. 

The magnetic field is along the curve of the toroid. The magnitude is the same as that at the middle of ideal solenoid. 

$$B = \mu_{o} n i = \frac{ \mu_{o} N i }{ 2 \pi r }$$
where n is no. of turns per unit length and N is the total no. of turns.

![[Pasted image 20240112105131.png]]

### Current Carrying Long Cylinder
#### Hollow Cylinder 
The current is uniformly distributed on the surface. 

**Inside,** 
We make an amperian loop inside the cylinder. 
We have,
$$
\begin{split}
\oint \vec{B} . d\vec{l} &= B 2\pi r \\
&= \mu_{o} (0) \\
&= 0
\end{split}
$$

Thus, there is no magnetic field inside the cylinder.

**Outside,**
We again make an amperian loop outside the cylinder. 

At each point of this loop, the value of magnetic field is the same by symmetry. 

Hence we can write,
$$
\begin{split}
\oint \vec{B}.d\vec{l} &= \int B \, dl \cos 0 \\
&= B \oint dl \\
&= B 2\pi r \\
&= \mu_{o} i 
\end{split}
$$

Thus, we get,
$$B = \frac{ \mu_{o} i }{ 2\pi r }$$
Which is the same as [[01.1 Current carrying Wire#Infinitely Long Wire]].

![[Pasted image 20240112202227.png]]


#### Solid Cylinder 
The current is uniformly distributed. 
Thus we can say,
$$J = \frac{ i }{ \pi R^{2} }$$

Outside, the magnetic field will be the same as that of hollow cylinder. 
$$
\begin{split}
B_{out} &= \frac{ \mu_{o} i }{ 2 \pi r } \\
&= \frac{ \mu_{o} J \pi R^{2} }{ 2\pi r } \\
&= \frac{ \mu_{o} JR^{2} }{ 2r } 
\end{split}
$$

In vector form,
$$\vec{B}_{out} = \frac{ \mu_{o} R^{2} }{ 2r^{2} } (\vec{J} \times \vec{r})$$

##### Inside 
We make an amperian loop inside the cylinder.

Here,
$$
\begin{split}
\oint \vec{B}. d\vec{l} &= B 2\pi r \\
&= \mu_{o} (J \pi r^{2}) \\
B &= \frac{ \mu_{o} Jr }{ 2 }
\end{split}
$$
That is, $B \propto r$.

In vector form,
$$B = \frac{\mu_{o}}{2} (\vec{J} \times \vec{r})$$

![[Pasted image 20240112202857.png]]

![[Pasted image 20240112203802.png]]
