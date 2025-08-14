Links: [[00 Thermodynamics]]
___
# KTG & Thermodynamics
We consider a large no. of gaseous molecules in a container. All of them are considered perfectly elastic solid spheres. 

These particles are moving in all possible directions without giving preference to any particular direction. This means that the average velocity will be zero. 

Thus, if the container is moving, the velocity of particles is considered to be the same as that of container. 

The speed of any gas particle can be between 0 to c. As temp. increases, the speed increases. 

#### Definitions
##### Pressure of Gas
The force exerted by the gas per unit cross section.

$$P = \frac{ f }{ A }$$

Its unit is N/m$^{2}$ i.e. Pascal (Pa) and it is a scalar.

For small container, we consider the pressure to be same everywhere.

![[Pasted image 20240213152614.png]]

$$1\ce{\ atm }= 1.01 \times 10^{6} \ce{\ Pa }$$

##### No. of Moles
$$n = \frac{m}{M} = \frac{ \text{no of particles of gas} }{ \text{avogadro's number} } =\frac{N}{N_{A}}$$
where,
$m \to$ mass of gas
$M \to$ molar mass
$N_{A} \to 6.023 \times 10^{23}$

##### Temperature of Gas
The more the temp., the more is the random speed, and thus the more is the kinetic energy, which is the internal energy.

Thus, temp. indicates the internal energy of gas.

Its unit is Kelvin (K) and dimension is $\ce{ [K] = [\theta] }$.

$$\ce{ K = 273 + ^{\circ}C }$$

Change in temperature is the same in K and C both. 

##### Volume of Gas
Volume of gas is the same as the volume of the container. 

$$\ce{ 1cm^{3} = 10^{-6} m^{3} }$$
$$\ce{ 1 l = 1000 cm^{3} = 10^{-3} m^{3} }$$

### Ideal Gas Law
Here, we consider that the gas particles do not exert intermolecular forces on each other.

$$PV = nRT$$
where R is *Universal Gas Constant* and T is in K.
$$R = 8.314 \ce{ J mol^{-1} K^{-1} } = \frac{ 25 }{ 3 }$$


Now, we can write,
$$
\begin{split}
PV &= \frac{m}{M}RT \\
PM &= \frac{m}{V}RT \\
PM &= \rho RT
\end{split}
$$
where M is molar mass of gas and $\rho$ is density. 

At STP, one mole gas has volume, *V = 22.4 litre.*

An Example,
![[Pasted image 20240213154354.png]]

### Maxwell Boltzmann Distribution
It describes the distribution of number of particles with their velocity.

Very few particles will have either the max, or 0 speed. 
As speed increases, the most probable speed increases. 

M is in kg/mol in all the following.

Average speed,
$$v_{avg} = \sqrt{ \frac{ 8RT }{ \pi M } } = \sqrt{ \frac{ 8P }{ \pi\rho } }$$

RMS speed,
$$v_{rms} = \sqrt{ \frac{ 3RT }{ M } } = \sqrt{ \frac{ 3P }{ \rho } }$$

Most probable speed,
$$v_{mp} = \sqrt{ \frac{ 2RT }{ M } } = \sqrt{ \frac{ 2P }{ \rho } }$$

Here, we see that,
$$v_{mp} < v_{avg} < v_{rms}$$

![[Pasted image 20240213155025.png]]

### Mean Free Path 
The path length between two consecutive collisions of a gas particle is called *Free Path.*

The average of this is called Mean Free Path and it is independent of temperature. 

$$\lambda = \frac{ 1 }{ \sqrt{ 2 }\pi d^{2}\ N_{v} }$$
where,
$N_{v} \to$ no. of gas molecules per unit volume
$d \to$ diameter of particle 

![[Pasted image 20240213155841.png]]

Thus, from $PV = nRT$,
$$\lambda =  \frac{ V }{ \sqrt{ 2 }\pi d^{2}\ N } = \frac{ V }{ \sqrt{ 2 }\pi d^{2}\ n N_{A} } = \frac{ RT }{ \sqrt{ 2 }\pi d^{2}\ P N_{A} }$$
where,
$N \to$ number of particles  
$n \to$ number of moles

#### Mean Relaxation Time
The amount of time between consecutive collisions is called *Relaxation Time.*

The average of this is called Mean Relaxation Time.

$$\uptau = \frac{ \lambda  }{ v_{rms} } = \frac{ \sqrt{ M } }{ \sqrt{ 2 } \pi d^{2} N_{v} \sqrt{ 3RT } }$$

Thus,
$$\uptau \propto \frac{ 1 }{ \sqrt{ T } }$$

### Barometer
It is used to measure atmospheric pressure. 

We fill a container with mercury and dip a tube filled to the brim with mercury in it.
Now, the mercury of the tube will go out from the tube and then stop. 

This will create a vacuum at the top, and thus the pressure by it is zero. 

We use mercury because it has high density and thus the height of the liquid in the tube is less.

We can thus write,
$$P_{atm} = \rho gH$$
And finally, the atmospheric pressure comes out to be,
$$P_{atm} = 1.013 \times 10^{5}\ \ce{ N m^{-2} }$$

![[Pasted image 20240213161115.png]]

### Degree of Freedom
The number of terms in KE of a gas particle. 

1. Monoatomic:
	- E.g. $\ce{ He,Ne, Ar }$
	- $f = 3$

2. Diatomic or linear polyatomic:
	- E.g. $\ce{ O_{2}, N_{2}, Cl_{2} }$
	- $f = \text{5 (3 TKE + 2 RKE)}$ 

3. Polynomial non linear:
	   - E.g. $\ce{ NH_{3} }$
	   - $f = \text{6 (3 TKE + 3 RKE)}$

When the temperature is very high (2000K) we add $+2$. These 2 are due to PE and KE of vibration.

![[Pasted image 20240213161720.png]]

#### Internal Energy of Gas
A gas can have 2 energies, 
Potential due to attraction between the particles and Kinetic due to its motion. 

**Law of Equipartition of Energy:** Each degree of freedom has equal energy.

For one gas molecule for 1 DOF, the energy will be,
$$E = \frac{ 1 }{ 2 }kT$$
where k is *Boltzmann Constant*
$$k = \frac{ R }{ N_{A} } = 1.38 \times 10^{-33}\ \ce{ J K^{-1} }$$

Thus, 
for 1 molecule with f DOF,
$$E = \frac{ f }{ 2 }kT$$
for 1 mole molecules with f DOF,
$$E = \frac{ f }{ 2 }kTN_{A} = \frac{ f }{ 2 }RT$$

Thus finally, for n mole molecules with f DOF,
$$E = \frac{ f }{ 2 }nRT = \frac{ f }{ 2 }PV$$

In physics we don't consider PE as we assume that  the gas particles have no intermolecular forces.

Thus, internal energy,
$$U = \frac{f}{2}PV = \frac{f}{2}nRT$$

And, change in internal energy,
$$\Delta U = \frac{f}{2} \Delta(PV) = \frac{f}{2} nR \Delta T$$

Using Molar Heat Capacity,
$$
\begin{split}
\Delta U &= \frac{ f }{ 2 }R n\Delta T \\
&= nC_{V}\Delta T \\
dU &= nC_{V}dT
\end{split}
$$

### Work Done by Gas
When gas expands the work done is +ve
When it compresses the work done is -ve. 
It is the opposite in chemistry. 

For a small displacement in the piston,
$$
\begin{split}
dW &= PA(dx) \\
&= P(Adx) \\
dW &= PdV \\
W &= \int P \, dV 
\end{split}
$$
i.e. the work done is the area under PV curve. (the sign is according to arrow)

![[Pasted image 20240213164212.png]]

## Laws of Thermodynamics 
### Zeroth Law
If A and B are in thermal equilibrium, and A is also in thermal equilibrium with another body C, then B and C are also in thermal equilibrium.

![[Pasted image 20240213163236.png]]

### First Law
Any heat given to a gas will be used in increasing its internal energy (U) and in increasing its volume (W). 

$$
\begin{split}
dQ &= dU + dW \\
\Delta Q &= \Delta U + W
\end{split}
$$

If we give heat, $dQ$ is +ve.
If we take away heat, $dQ$ is -ve. 

If gas expands, $dW$ is +ve.
If gas compresses, $dW$ is -ve.

If the temp. decreases, $dU$ is -ve.
If the temp. increases, $dU$ is +ve.

## Free Expansion 
When the container is divided into two parts and one of the parts is vacuum. 

When we stop applying external force $PA$ to keep the piston in place, the piston at once expands to the other side of the container and thus the volume is increased. 

In this case, work done is zero because when the piston moves due to force by the gas, the contact between the gas particles and the piston is removed, thus there is no force, even though there is displacement. 

$$
\begin{split}
W &= 0 \\
\Delta Q &= 0 \\
\Delta U &= 0
\end{split}
$$

The volume is increased, and the pressure is decreased by the same factor. 

![[Pasted image 20240213212214.png]]