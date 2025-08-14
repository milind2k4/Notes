Links: [[00 Sound Waves]], [[01 Displacement and Pressure Waves]]
___
# Speed of Sound
$$v_{w} = \sqrt{ \frac{ \text{elasticity} }{ \text{inertia} } }$$

#### Solids
$$v_{w} = \sqrt{ \frac{ y }{ \rho } }$$
where,
$y \to$ Young's Modulus,
$\rho \to$ density.

#### Fluids
$$v_{w} = \sqrt{ \frac{ B }{ \rho } }$$
where,
$B \to$ Bulk Modulus,
$\rho \to$ density.

#### Air
In air, the bulk modulus is,
$$B = \upgamma P$$
where,
$P \to$ Pressure
$\upgamma \to$ ratio of specific heats
$$\upgamma = \frac{ C_{P} }{ C_{V} } = 1 + \frac{2}{f}$$
($f$ is degree of freedom)
[[03 Molar Heat Capacity#Ratio of Specific Heats]]

Also,
$$
\begin{split}
PV &= nRT \\
PM &= \frac{ m }{ V } RT \\
\frac{ P }{ \rho } &= \frac{ RT }{ M }
\end{split}
$$

Thus,
$$
\begin{split}
v_{air} &=  \sqrt{ \frac{ B }{ \rho } } \\
&= \sqrt{ \frac{ \upgamma P }{ \rho } } \\
&= \sqrt{ \frac{ \upgamma RT }{ M } }
\end{split}
$$
where M is molar mass in kg per mol.

#### Derivation of B of Air 
Laplace said that the propagation of sound is so fast, that there is no time for an air column to exchange heat from the surroundings. 

Thus propagation of sound is adiabatic process.
Thus,
$$PV^{\upgamma} = \text{const.}$$

Now, we know that,
$$
\begin{split}
B &= - \frac{ dP }{ dV /V } \\
&= -\frac{ dP }{ dV } V
\end{split}
$$
Thus, differentiating the previous equation,
$$
\begin{split}
P\upgamma V^{\upgamma-1}dV + V^{\upgamma}dP &= 0 \\
V^{\upgamma-1}(\upgamma PdV + VdP) &= 0 \\
VdP &= -\upgamma PdV \\
\frac{ dP }{ dV } &= \frac{ -\upgamma P }{ V }
\end{split}
$$

Thus the bulk modulus of air will be,
$$B = -\left( -\frac{ \upgamma P }{ V } \right)V = \upgamma P$$
This formula will work for other gases as well.

#### Dependency of Speed
1. **On Temperature:** As T increases, v also increases.
	$$
	\begin{split}
	v_{w} &= \sqrt{ \frac{ \upgamma RT }{ M } } \\
	v_{w} &\propto \sqrt{ T }
	\end{split}
	$$
	where T is in K.
	
	For small change, we take log,
	$$
	\begin{split}
	v &= kT^{1/2} \\
	\ln v &= \ln k + \frac{ 1 }{ 2 } \ln T \\
	\frac{ dv }{ v } &= \frac{ 1 }{ 2 } \frac{ dT }{ T } \\
	\frac{ dv }{ v } \times 100\% &= \frac{ 1 }{ 2 } \frac{ dT }{ T } \times 100\%
	\end{split}
	$$
	
	$\\$
	
1. **On Humidity:** As humidity increases, v also increase.
   The average molar mass of air is about 29.
   Now, if we increase humidity, the water concentration, i.e. $\ce{ H_{2}O }$ molecules are increases. 
   
   Now, since the molar mass of water is less than 29, the average molar mass decreases. 
   And since $v \propto 1 /\sqrt{ M }$, the velocity increases. 

![[Pasted image 20240207192922.png]]
![[Pasted image 20240207192933.png]]
