Links: [[00 Capacitance]]
___
# Capacitor
aka **Condenser**

When two metals are put close to each other and insulated from each other, the arrangement is called a Capacitor. 

In other words, an arrangement which can store charge, electric field and electrostatic potential energy is known as a Capacitor. 

The capacitance of this arrangement is,
$$C = \frac{ +Q }{ V_{A} - V_{B} }$$

And the electrical potential energy is, 
$$U = \frac{ 1 }{ 2 } C(\Delta V)^{2} = \frac{ Q^{2} }{ 2C } = \frac{ 1 }{ 2 }Q(\Delta V)$$
where $\Delta V = V_{A} - V_{B}$

![[Pasted image 20240109162158.png]]

#### Potential Change Across Capacitor 
In circuit 

If we go along the electric field inside the capacitor, the potential drops by $\displaystyle \frac{ q }{ C }$ and if we go against it, it increases by $\displaystyle \frac{ q }{ C }$.

$$\Delta V = -\frac{ \text{(charge on plate encountered)} }{ C }$$

![[Pasted image 20240109165247.png]]

### Parallel Plate Capacitor 
Two large metallic plates are separated by a small distance. The separation is negligible compared to the dimensions of the plates. 

Area of the plates is $A$ and $d$ is the separation between the plates. 

![[Pasted image 20240109163004.png]]

Using [[13 Sharing of Charge#Induction of Charge]] we find that the charge distribution is on the inside of the plates. 

![[Pasted image 20240109163009.png]]

Between the plates, the electric field is,
$$E = \frac{ Q }{ A \varepsilon_{o} }$$

The potential difference,
$$V = Ed = \frac{ Qd }{ A \varepsilon_{o} }$$

And thus the capacitance,
$$C = \frac{ Q }{ V } = \frac{ QA \varepsilon_{o} }{ Qd }$$

That is, for PPC, capacitance is,
$$C = \frac{ A \varepsilon_{o} }{ d }$$

If the medium between the plates is not air,
$$C = \frac{ A \varepsilon_{o} \varepsilon_{r} }{ d } = C_{air} \times \varepsilon_{r}$$

The electric potential energy between the plates,
$$
\begin{split}
U &= \frac{ dU }{ dV } \\
&= \frac{1}{2} \frac{ \varepsilon_{o} Q^{2} }{ A^{2} \varepsilon_{o}^{2} } Ad \\
&= \frac{ Q^{2}d }{ 2A \varepsilon_{o} } \\
&= \frac{ Q^{2} }{ 2C }
\end{split}
$$
Which is the same as any other capacitor. 

![[Pasted image 20240109164215.png]]

The amount of work done in expanding or contracting the separation between the plates of PPC is stored/removed from the electrostatic potential energy of system.

![[Pasted image 20240109164944.png]]

### Sharing of Charge b/w two Capacitors
We divide the capacitor into two conducting plates. And then use [[00 Capacitance#Sharing of Charges b/w 2 Conductors]]

Using charge conservation, if the common potential is V,
$$C_{1} V_{1} + C_{2} V_{2} = C_{1}V + C_{2}V$$

Thus the common potential comes out to be,
$$V = \frac{ C_{1} V_{1} + C_{2}V_{2} }{ C_{1} + C_{2} }$$

And the final charge on each capacitor comes out to be,
$$
\begin{split}
Q_{1} &= \frac{ C_{1} }{ C_{1} + C_{2} } (C_{1}V_{1} + C_{2}V_{2}) \\
Q_{2} &= \frac{ C_{2} }{ C_{1} + C_{2} } (C_{1}V_{1} + C_{2}V_{2}) \\
\end{split}
$$

Heat loss in the resistor, is the difference is potential energy of the system,
$$\text{heat loss} = \left( \frac{1}{2}C_{1}V_{1}^{2} + \frac{1}{2}C_{2}V_{2}^{2} \right) - \left( \frac{1}{2}(C_{1} + C_{2})V \right)$$
It comes out to be,
$$\text{heat loss} = \frac{ 1 }{ 2 } \frac{ C_{1}C_{2} }{ C_{1} + C_{2} } (V_{1} - V_{2})^{2}$$

![[Pasted image 20240110124148.png]]

If we connect the +ve plate of one capacitor with the -ve plate of the other, the procedure will be same and finally in the formula, instead of $V_{2}$, it will be $-V_{2}$. 



