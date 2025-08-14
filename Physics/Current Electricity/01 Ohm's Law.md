Links: [[04 Equivalent Resistance]]
___
# Ohm's Law
The current through a conductor is directly proportional to the  potential difference applied across it. 

Any object which follows ohm's law is called an *Ohmic object.*
$$i \propto V$$

The constant of proportionality is 1/R,
$$i = \frac{ V }{ R }$$
R is called **Resistance** of the object. 

The inverse of resistance is called **Conductance,**
$$\frac{ 1 }{ R } = S$$

### Resistance & Resistivity
![[Pasted image 20231219170334.png]]

$$R = \frac{ V }{ i }$$

Resistance has unit Volt/Amp = Ohm ($\ohm$)

It is proportional to length of wire and inversely proportional to the cross sectional area.
$$
\begin{split}
R &\propto \frac{ l }{ A } \\
&= \rho \frac{ l }{ A }
\end{split}
$$
where $\rho$ is constant of proportionality and is called **Resistivity.**

Resistance depends on shape, size, geometry and material.

Good conductors have low resistance and the bad conductors have high resistance. 

As we increase temp., resistance increases. 

Resistivity has unit: $\ohm\ m$

$\rho$ does not depend on shape, size, geometry of object. It is a property of material and is directly proportional to temp..

##### Examples 
The same object can have different resistances along different directions,
![[Pasted image 20231219171753.png]]

![[Pasted image 20231219172605.png]]
![[Pasted image 20231219172706.png]]

##### Stretching and Squishing of Wire
As we stretch a wire, its cross sectional area decreases and length increases. 

As we squish a wire, its cross sectional area increases and length decreases.

We will find the ratio using the fact that Volume remains constant.

We can say,
$$
\begin{split}
R &= \frac{ \rho l }{ A } \\
&= \frac{ \rho l^{2} }{ Al } 
\end{split}
$$
Thus,
$$R \propto l^{2}$$

![[Pasted image 20231219173658.png]]

#### Conductance & Conductivity
Conductance is the reciprocal of Resistance,
$$S = \frac{1}{R} \ce{\ \mho }$$
It has unit Amp/Volt = Siemens. 

Conductivity is the reciprocal of Resistivity,
$$\sigma = \frac{1}{\rho}$$
And it has unit $\mho\ m^{-1}$

#### Dependence of R on  Temp.
Let resistance be $R_{o}$ at $0^{\circ}$ C, $R$ at $T^{\circ}$ C and $R + dR$ at $(T + dT)^{\circ}$ C.

$$
\begin{split}
dR &\propto R \\
&\propto dT
\end{split}
$$
Thus we get,
$$dR = \alpha RdT$$
where $\alpha$ is the thermal coefficient of resistance.
$\alpha$ depends on material and has unit $1 /^{\circ}C$. 

We can write,
$$
\begin{split}
\int_{R_{o}}^{R} \frac{ dR }{ R } &= \alpha \int_{0}^{T} dT \\
\ln \frac{ R }{ R_{o} } &= \alpha T \\
R &= R_{o} e^{ \alpha T }
\end{split}
$$
If $\alpha \to 0$, then $\alpha \Delta T \ll 1$. Thus we can approximate,
$$e^{ x } = 1 + x$$

Thus giving,
$$R = R_{o} (1 + \alpha \Delta T)$$

Note that we will only use this formula when $\alpha \Delta T$ is very very small. Otherwise we will use the real formula.

![[Pasted image 20231219174827.png]]

### Alternate form of Ohm's Law
$$
\begin{split}
i &= \frac{ V }{ R } \\
&= \frac{ El\ A }{ \rho l } \\
\\
\frac{ i }{ A } &= \frac{ E }{ \rho } \\
J &= \frac{ E }{ \rho } \\
E &= \rho J
\end{split}
$$

In vector form,
$$\vec{E} = \rho\ \vec{J}$$
$$\vec{J} = \sigma\ \vec{E}$$

![[Pasted image 20231219171054.png]]

Using this we can find charge at interface of two materials, 
[[10 Electric Flux & Gauss Law]]
![[Pasted image 20231219171630.png]]

### Ohm's Law in Circuits 
In resistance current is always from higher to lower potential. 

$$V_{1} - V_{2} = iR$$
Thus,
$$i = \frac{ V_{1} - V_{2} }{ R }$$

![[Pasted image 20231219173044.png]]

As we move along current, potential drops. As we move opposite to it, potential increases. Both by $iR$.

![[Pasted image 20231219173052.png]]

![[Pasted image 20231219173257.png]]


