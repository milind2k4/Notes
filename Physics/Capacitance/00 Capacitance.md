Links: [[02 Circuit solutions of RC Circuit]]
___
# Capacitance
A capacitor is a device which is used to store electrostatic potential energy. 

Capacitance is the capacity of capacitor to store charge. 

Since charge is being stored, electric field is also being stored and thus electric potential is being stored.  

#### Corona Discharge

Metals have a max. limit on how much charge they can store. 
If we try to add more charge, the charge escapes into the surrounding medium in the form of current. 

![[Pasted image 20240108124140.png]]

As we increase charge, the electric field increases. 
Due to this field, the polar molecules get aligned along the field due to forces on the -ve and +ve part of it. 

After a point, if we keep increasing the charge, the force due to the field on the molecule will be so high that it will break the molecule. This breakdown will cause the flow of current. 

![[Pasted image 20240108124743.png]]

This phenomenon is called **Corona Discharge** and the field at which it occurs is called **Dielectric Strength** and the potential is called **Breakdown Potential.**

If the geometry is not uniform, the Corona discharge occurs at the point of least radius of curvature as that will have the most charge.

![[Pasted image 20240108125157.png]]

Thus the capacitance will depend on geometry of body. Therefore, the capacitance of a uniform body will be more than that of a non uniform body. 

##### Dielectric Strength or Breakdown Electric Field
The min. electric field required to break the medium molecules is known as dielectric strength $E_{o}$. 
$$or$$
The min. electric field required to convert dielectric medium into conducting medium is known as dielectric strength $E_{o}$. 

It is property of medium. 

If molecules have strong bonds, $E_{o} \uparrow$.
If molecules have weak bonds, $E_{o} \downarrow$.

![[Pasted image 20240108125859.png]]

##### Breakdown Voltage 
The max. electric potential of a metal at which the medium is just about to breakdown is called Breakdown Voltage/Potential, $V_{o}$. 

![[Pasted image 20240108125907.png]]

### Capacitance of an Isolated Metal
Capacitance depends on,
- shape, size, geometry of body.
- surrounding medium. 

A body which is not charged also has a capacitance. 

As we increase charge, the potential of the conductor increases.
The proportionality constant between Q and V is known as Capacitance. 

$$
\begin{split}
Q &\propto V \\
Q &= CV \\
C &= \frac{Q}{V}
\end{split}
$$
A capacitor which stores more charge with less potential has more capacitance. 

Its unit is C/V or Farad (F) and dimensions are $\ce{ [M^{-1}L^{-2}T^{4}I^{2}] }$

It is a non negative scalar quantity. 

Capacitance does not depend upon V or Q. This is because as we increase charge, the potential also increases at the same rate. 

####  C of Isolated Metallic Sphere 
The potential at the surface of the metal is,
$$V = \frac{ kQ }{ R }$$

Thus, capacitance can be given as,
$$
\begin{split}
C &= \frac{ Q }{ V } \\
&= \frac{ R }{ k }
\end{split}
$$
We can see that it does not depend on charge or potential. 

In air, we can write,
$$C = 4\pi \varepsilon_{o} R$$
And in another medium,
$$C = 4 \pi \varepsilon R = 4 \pi \varepsilon_{o} \varepsilon_{r} R$$

Thus capacitance will depend on surrounding medium. 

![[Pasted image 20240108131004.png]]

### Energy Stored by a Conductor
[[07 Self Energy]]

Let the charge and potential on the surface of the conductor be Q and V respectively.
And,
$$C = \frac{ Q }{ V }$$

Because there is electric field, there is energy stored. 

This energy is,
$$U_\text{self} = \int \frac{1}{2} \varepsilon_{o} E \, dV $$

![[Pasted image 20240108131911.png]]

Bringing a charge of dq from infinity to the surface will require work done,
$$dW = Vdq = \frac{ qdq }{ C }$$
Thus, bringing charge Q will require,
$$W = \frac{ Q^{2} }{ 2C } = U$$

This can be written as,
$$
\begin{split}
U &= \frac{ Q^{2} }{ 2C } \\
&= \frac{ 1 }{ 2 } CV^{2} \\
&= \frac{ 1 }{ 2 } QV
\end{split}
$$

![[Pasted image 20240108131920.png]]

##### Derivation for PPC for Boards
Suppose a displacement of charge q from one plate to the other plate sets up a potential difference V between the plates.
$$V = \frac{q}{C}$$

Work done to displace small additional charge dq,
$$dW = Vdq = \frac{q}{C}dq$$
Total work done in displacing a charge q from one plate to another,
$$
\begin{split}
W &=  \int_{0}^{q} \frac{ q }{ C } \, dq \\
&= \frac{1}{2} \frac{ q^{2} }{ C }
\end{split}
$$
But $q = CV$
$$W = \frac{1}{2}CV^{2}$$
Again,
$$W = \frac{1}{2}qV$$

### Sharing of Charges b/w 2 Conductors 
[[13 Sharing of Charge]]

The charge will flow until both the conductors have same potential. 

By charge conservation, if the initial charges were $Q_{1},Q_{2}$ and final were $q_{1},q_{2}$, 
$$Q_{1} + Q_{1} = q_{1} + q_{2}$$

Common potential, 
$$V = \frac{ q_{1} }{ C_{1} } = \frac{ q_{2} }{ C_{2} }$$
$$\frac{ q_{1} }{ q_{2} } = \frac{ C_{1} }{ C_{2} }$$
Thus the conductor which has more capacitance will have more charge. 

Solving the two we get,
$$q_{1} = \frac{ C_{1} }{ C_{1} + C_{2} } (Q_{1} + Q_{2})$$
$$q_{2} = \frac{ C_{2} }{ C_{1} + C_{2} } (Q_{1} + Q_{2})$$

And the common potential comes out to be,
$$V = \frac{ Q_{1} + Q_{2} }{ C_{1} + C_{2} }$$

![[Pasted image 20240109161211.png]]

Heat dissipated,
$$
\begin{split}
H &= \int i^{2}R \, dt \\
&= U_{i} - U_{f} \\
&= \left( \frac{ Q_{1}^{2} }{ 2C_{1} } + \frac{ Q_{2} }{ 2C_{2} } \right) - \left( \frac{ q_{1}^{2} }{ 2C_{1} } + \frac{ q_{2} }{ 2C_{2} } \right) 
\end{split}
$$

