Links: [[01 Ohm's Law]], [[06 Instruments]]
___
# Current Electricity
Rate of flow of charge. 
$$i_{avg} = \frac{ \Delta q }{ \Delta t }$$

$$i = \frac{ dq }{ dt } $$

Its unit is C/s = Ampere and its dimension is $\ce{ [I] or [A] }$. 

Current is considered a scalar even though it has direction because it follows scalar algebra. 

Current has direction along flow of +ve charge or opposite to flow of -ve charge.

![[Pasted image 20231219162254.png]]

Also,
$$
\begin{split}
dq &= i dt \\
Q &= \int i \, dt 
\end{split}
$$
Thus area under i-t curve gives charge.

#### Conductors 
[[00 Electrostatics#Conductor]]

They have large no. of free electrons.

Due to this charge and electrical energy can transfer from one place to another. 

**Free electron density** is no. of free electrons per unit volume. The more it is, the better conductor it is. 

### Current Density
Current per unit cross sectional area. It is a vector quantity along current.  

$$J = \frac{i}{S}$$

Its unit is $\ce{ A/m^{2} }$. 

![[Pasted image 20231219162642.png]]

If current and surface are not mutually perpendicular,
$$
\begin{split}
di &= \vec{J} . d\vec{s} \\
&= J ds \cos \theta \\
\end{split}
$$

![[Pasted image 20231219162912.png]]

Using this we can write,
$$i = \int \vec{J}. d\vec{s}$$
Which is the surface integral of current density. 

![[Pasted image 20231219163256.png]]

### Motion of free e in Conductor 
Under no electric field, the motion of e is random and thus there is no current as there is no $v_{avg}$. 

If we take a cross section in the material, the amount of net charge passing through it will be zero. 

![[Pasted image 20231219164003.png]]

When an electric field is applied across the conductor, all the e start moving in the direction opposite to the direction of the field. Now there is a net charge passing through any cross sectional area and thus there is current. 

The common velocity of all the e on applying the field is called **Drift Velocity.** 

Now, the charge passing through a cross section in time dt can be given as,
$$dq = (nAv_{d} dt) e$$
And thus the current in terms of drift velocity is given by,
$$i = nAe\ v_{d}$$
where,
$n \to$ free electron density
$A \to$ cross sectional area 
$e \to$ charge on electron
$v_{d} \to$ drift velocity 

![[Pasted image 20231219165627.png]]

This drift velocity,
$$
\begin{split}
v_{d} &\propto E \\
&\propto \frac{ V }{ l } 
\end{split}
$$

We can write, (K is any constant)
$$i = V \frac{ A }{ l } K$$
And thus,
$$i \propto V$$

Thus we get [[01 Ohm's Law]].

### Electromotive Force (EMF)
It is not a force but a potential difference.

It is defined for a battery. 

It is the work done by battery per unit charge given by it.

$$\varepsilon = \frac{ W }{ Q }$$

Its unit is J/C = Volt. 

We can write,
$$
\begin{split}
\varepsilon &= \frac{ W }{ q } \\
&= \frac{ \smallint q\vec{E}.d\vec{l} }{ q } 
\end{split}
$$
If charge does not change with electric field,
$$
\begin{split}
\varepsilon &= \oint \vec{E}.d\vec{l}
\end{split}
$$

![[Pasted image 20231219211449.png]]
