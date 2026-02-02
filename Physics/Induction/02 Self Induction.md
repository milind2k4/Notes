Links: [[03 Mutual Induction]]
___
# Self Induction
If we have a wire with many loops in it, and we pass a current through it, a magnetic field is created which passes through the loops. 

Due to this field, there will be flux. This flux will be directly proportional to the current passing through the loop. 

The proportionality constant is called coefficient of self induction. 

$$\phi \propto i$$
$$\phi = Li$$
where L is coefficient of self induction, or **Self Inductance**.

Its unit is Weber/Ampere or **Henry (H)** and its dimensions are $\ce{ [ML^{2}T^{-2}I^{-2}] }$.

It depends on shape, size geometry of loop, number of turns and medium (since B depends on medium). 

![[Pasted image 20240117193039.png]]

It is the property of the current carrying coil that resists the change of current flowing through it. 

### $L$ of an Ideal Solenoid
Solenoid: length $l$, radius $r$, turns per unit length $n$ and current $i$.

Magnetic field due to  this current $i$
$$B = \mu_{o}ni$$

Flux through the  solenoid,
$$
\begin{split}
\phi &= (\mu_{o} ni \pi r^{2})nl \\
&= (\mu_{o} n^{2} \pi r^{2}l) i
\end{split}
$$

Comparing it with $\phi = Li$,
$$L = \mu_{o} n^{2} \pi r^{2}l$$
$$L = \mu_{o} n^{2} . (\ce{ vol })$$

![[Pasted image 20240117193458.png]]

### Inductor
Any current carrying loop can be said to be an inductor.

A coil with self inductance is called inductor. 

![[Pasted image 20240117193703.png]]

#### Emf across Inductor 
If current through it is constant, the flux will be constant and thus the emf will be zero. Thus the inductor will behave like a short wire. 

If the current through the coil is increasing with time, the flux through it is also increasing. Due to this there will be emf induced. 

Now, according to Lenz's law, the induced emf will oppose this increase in current and thus, try to create a current in the opposite direction. 

$$
\begin{split}
\varepsilon &= \left| \frac{ d\phi }{ dt } \right| \\
&= L \left| \frac{ di }{ dt } \right| 
\end{split}
$$

![[Pasted image 20240117194234.png]]

Now, if the current is decreasing with time, the flux will decrease. This will induce an emf in the coil which will try to increase this current. 

![[Pasted image 20240117194417.png]]

If we move in the direction of the current, the potential drops by,
$$V = -L \frac{ di }{ dt }$$
where $di /dt$ is with sign. 

And if we go against the current, the potential increases by the same amount. 

![[Pasted image 20240117194610.png]]

![[Pasted image 20240117195016.png]]
![[Pasted image 20240117195026.png]]

#### Energy Stored in Inductor
Inductor will store magnetic potential energy. 

Since there is magnetic field through the coil, there is magnetic energy stored in it. 

As current increases from 0 to i, and emf is induced in the inductor,
$$\varepsilon = -L \frac{ di }{ dt }$$
Now, this emf acts like a load and converts electrical energy into magnetic potential energy.

The power of the inductor is,
$$P = Vi = L i \frac{ di }{ dt }$$

Thus the energy consumed is,
$$
\begin{split}
W &= \int P \, dt \\
&= L \int_{0}^{i} i \, di \\
U &= \frac{ 1 }{ 2 }Li^{2}  
\end{split}
$$

Now, this energy can be written as,
$$
\begin{split}
U &= \int \left( \frac{ B^{2} }{ 2\mu_{o} } \right) \, dV 
\end{split}
$$

![[Pasted image 20240117195905.png]]

#### Circuit with Inductor 
We will use KVL to find current. 

Inductor does not let current change suddenly in the circuit.

![[Pasted image 20240117200207.png]]