Links: 
___
# Elasticity
Any object when deformed, tries to regain its original shape, size and geometry. This property of an object is called *Elasticity.*
$$or$$
It is property of a body due to which a body resists any change in its shape, size and geometry.  

Solids are more elastic than liquids which are more elastic then gases.

The body which resists more is said to be more elastic. Thus, steel is more elastic than rubber. 

Elasticity is due to intermolecular forces. Thus, if we increase temp., elasticity decreases.

**Strain** is change in configuration upon actual configuration. It is a unitless and dimensionless quantity.

**Stress** is force applied per unit area. It has unit N/m$^{2}$.

![[Pasted image 20240215173644.png]]

### Longitudinal Strain and Stress 
A rod is extended by $\Delta l$ from $l$ by applying a force F on its ends of cross section A.

If this force is directed inside the rod, it is called *compressive* if it is directed outside from the rod, it is called *tensile.*

Longitudinal strain is,
$$\text{strain} = \frac{ \Delta l }{ l }$$

Longitudinal stress is,
$$\text{stress} = \frac{ f_{n} }{ A } = \frac{ F }{ A }$$

![[Pasted image 20240215174113.png]]
![[Pasted image 20240215174220.png]]

#### Young's Modulus (y)
It is the ratio of longitudinal stress and strain. 

$$y = \frac{ \text{longitudinal stress} }{ \text{longitudinal strain} }$$

It has unit N/m$^{2}$ and it is a property of material. 

The more elastic an object is, the more $y$ it has.

For a rod, it is,
$$
\begin{split}
y &= \frac{ F /A }{ \Delta l /l } \\
&= \frac{ Fl }{ A\Delta l }
\end{split}
$$

![[Pasted image 20240215140030.png]]

#### Change in Length due to Self Weight 
A uniform rope of mass $m$, length $l$, cross sectional area $A$ and young's modulus $y$ is suspended.

Tension at any point on the rope,
$$T = \frac{ m }{ l }gx$$

To find the change in length, we take an element of length $dx$, $x$ distance from the bottom. 

Due to force on both ends of this element, its length will increase by a small amount $ds$. 

Since the force on both ends are almost the same, we can write,
$$
\begin{split}
y &= \frac{ T /A }{ ds /dx } \\
ds &= \frac{ Tdx }{ Ay } \\
&= \frac{ mgx dx }{ lAy } \\
\\
\Delta l &= \int ds \\
&= \frac{ mg }{ lAy } \int_{0}^{l} x \, dx \\
&= \frac{ mgl }{ 2Ay }
\end{split}
$$

Alternatively, we can write,
$$
\begin{split}
y &= \frac{ T_{avg} /A }{ \Delta l /l } \\
&= \frac{ mgl }{ 2A \Delta l } \\
\Delta l &= \frac{ mgl }{ 2Ay }
\end{split}
$$
But this only works when T varies linearly.

![[Pasted image 20240215101259.png]]
![[Pasted image 20240215101306.png]]


#### Breaking Stress
The max. possible stress in the wire.

![[Pasted image 20240215174545.png]]

### Rod as Spring
We have a wire of cross sectional area A and young's modulus y and length l. 
We apply a force F and change its length by x.

We can write,
$$
\begin{split}
y &= \frac{ Fl }{ Ax } \\
F &= \frac{ yA }{ l }x 
\end{split}
$$
That is,
$$F \propto x$$
which is the same as $F \propto x$ of spring. 
Thus we can replace the rod with a spring whose spring constant is,
$$k = \frac{ yA }{ l }$$

![[Pasted image 20240215165826.png]]

### Elastic Potential Energy
Just like spring. We just put the value of k,
$$k = \frac{ yA }{ l }$$

Thus, we get,
$$U = \frac{ 1 }{ 2 } \frac{ yA }{ l }x^{2}$$

We can write,
$$
\begin{split}
U &= \frac{ 1 }{ 2 }yAl \frac{ x^{2} }{ l^{2} } \\
&= \frac{ 1 }{ 2 } y (V) (\text{strain})^{2} \\
&= \frac{ 1 }{ 2 } \times \text{stress} \times \text{strain} \times \text{volume}
\end{split}
$$

Elastic potential energy density,
$$
\begin{split}
\frac{ U }{ V } &= \frac{ 1 }{ 2 } \times \text{stress} \times \text{strain}
\end{split}
$$

### Poisson's Ratio 
As we increase the length by applying force, the radius will also change. 

Poisson's ratio is the ratio between the fractional change in radius and the fractional change in length. 

$$\sigma = - \frac{ dR /R }{ dl /l }$$

![[Pasted image 20240215174821.png]]

### Stress vs Strain Curve 
At first, stress is directly proportional to strain. This region is called *region of proportionality.* This part follows **Hooke's Law.** The young's modulus will be the slope of this curve. 

After this region, as we increase stress, strain increases, but not linearly. At the end of this part, we have the *elastic limit.* That is, until this point, if we remove the stress, the body will regain its original state.

After B, the object becomes plastic. I.e., if we remove stress after reaching a point after B, the body will not regain its original state. 

After point D, the wire will behave like a fluid. And at point E, the wire will break.

For brittle objects, the region BE is small. 
For malleable objects, the region BE is large. 

![[Pasted image 20240215171245.png]]

### Shear Stress and Strain
We apply a tangential force on an object and its shape changes.

Shear strain is defined as,
$$\text{strain}_{s} = \frac{ x }{ h } = \tan \theta$$

Shear stress is defined as,
$$\text{stress}_{s} = \frac{ f_{t} }{ A }$$

![[Pasted image 20240215174136.png]]
![[Pasted image 20240215174240.png]]

#### Modulus of Rigidity 
It is the ratio of shear stress and shear strain. 

$$\eta = \frac{ \text{stress}_{s} }{ \text{strain}_{s} }$$

![[Pasted image 20240215172222.png]]

### Volumetric Strain and Stress 
The object is being compressed by some external force. 

Volumetric strain is defined as,
$$\text{strain}_{v} = \frac{ dV }{ V }$$

Volumetric stress is defined as the change in pressure that caused the compression,
$$\text{stress}_{v} = dP$$
![[Pasted image 20240215174152.png]]
![[Pasted image 20240215174253.png]]

#### Bulk Modulus (B)
It is the ratio of volumetric stress and strain. 

$$B = -\frac{ dP }{ dV /V } = - \frac{ dP }{ dV } V$$
-ve because as we increase pressure, volume decreases. 

#### Compressibility 
It is the inverse of bulk modulus,
$$
\begin{split}
k &= \frac{ 1 }{ B } \\
&= -\frac{ dV /V }{ P } \\
&= - \frac{ 1 }{ V } \frac{ dV }{ dP }
\end{split}
$$

### Bulk modulus of Gases 
Since for gas, the relation between pressure and volume depends on the process, for different processes, the bulk modulus of the same gas may be different. 


[[01 Processes]]
- **For isochoric process,** B is not defined. 
- **For isobaric process,** B is zero. 

- **For isothermal process,**
	 $$
	\begin{split}
	PV &= c \\
	PdV + VdP &= 0 \\
	\frac{ dP }{ dV } &= - \frac{ P }{ V }
	\end{split}
	$$
	Thus bulk modulus is,
	$$B = P$$
	$\\$

- **For polytrophic process,**
	$$PV^{a} = c$$
	Thus bulk modulus is,
	$$B = aP$$
	$\\$

- **For adiabatic process,**
	$$PV^{\upgamma} = c$$
	Thus bulk modulus is,
	$$B = \upgamma P$$
