Links: [[00 Real Gas]]
___
# Van der Waals' Equation of State

Ideal gas equation ($PV = nRT$) is based on KTG in which the following 2 main assumptions are not valid for real gases under all T and P conditions,
1. No intermolecular forces between gas molecules. 
1. Volume of gas molecules is negligible in comparison to the volume of gas. (Size of molecule is considered negligible)

Van der Waals considered the above assumptions of KTG being faulty and hence does not apply well on real gases. 

He was the first person who applied correction terms (in volume and pressure) to the ideal gas equation. 

#### Correction in Volume
Due to finite size of gas molecules he said that full volume of the vessel is not available for the real gas molecules to ream around. 

Some volume is occupied by gas molecules and hence the free volume should be equal to volume of vessel minus a volume correction term. 

He applied a -ve correction term in volume.

$$V_{f} = V - nb$$
where $b$ is called excluded volume or co-volume per mole of gas. 

Experimental value of b is,
$$\text{ b = 4} \times \text{ volume of 1 mole of gas molecules}$$
$$b = 4 \times \frac{4}{3}\pi r^{3} \times N_{a}$$
r is radius of gas molecule. 

#### Correction in Pressure
Vander Waals applied a +ve correction term in P observed to get ideal pressure. 

A particle about to hit a wall of the container experiences an intermolecular pull away from the wall due to all the surrounding particles. Due to this, the velocity, in turn the momentum, in turn the force and finally the pressure exerted is reduced. 

$$P_{r} = P_{atm} + hdg$$
$$P_{i} = P_{ob} + \text{ a P correction term}$$

Pressure correction term depends on the following factors,
1. *Number of gas molecules per unit volume.* 
   
   Higher is the number of gas molecules per unit volume higher will be the drag force on the gas molecule about to collide with the wall of the container. 
   
   And lesser will be the contribution in pressure. and therefore greater will be the pressure correction term.
   
   $$\text{P correction term} \propto \frac{ N }{ V }\ or\ \frac{ n }{ V }$$
   where N is number of molecules and n is number of moles. 

2. Greater are the Number of Collisions of Gas Molecules with wall of container, greater will be the correction term applied. 
   
   $$\text{P correction term} \propto \frac{ N }{ V }\ or\ \frac{ n }{ V } $$

Considering both correction, the overall correction term,
$$\text{P correction term} \propto \frac{ n^{2} }{ V^{2} }$$
$$\text{P correction term} = a\frac{ n^{2} }{ V^{2} }$$
where $a$ is **Van Der Waal's constant.** It is a measure of attractive force. 

Thus ideal pressure is,
$$P_{i} = P + \frac{ an^{2} }{ V^{2} }$$
here P is the observed pressure i.e. the pressure of the real gas. 

#### Equation of State
Applying both the correction terms to the ideal gas equation, we get,

$$\left( P + \frac{ an^{2} }{ V^{2} } \right)(V - nb) = nRT$$
where $a,b$ are called Van der Waals constants of a gas. It is constant for a given gas and does not depend on P or T. They are characteristic constants for a gas.

This is called **Vander Waal's equation of state.**

Now dividing the equation by n,
$$\left( P + \frac{ a }{ (V /n)^{2} } \right)\left( \frac{V}{n} - b \right) = RT$$
$$\left( P + \frac{ a }{ V_{m}^{2} } \right)\left( V_{m} - b \right) = RT$$
where,
$$V_{m} = \frac{ V }{ n }$$

And,
**$a$ is a measure of attractive forces** between gas molecules
it has unit **$\ce{ atm L^{2} mol^{-2} }$** or **$\ce{ Pa m^{6} mol^{-2} }$** in SI units.

**$b$ is a measure of finite size** of gas molecules. 
it has unit **$\ce{ L mol^{-1} }$** or **$\ce{ m^{3} mol^{-1} }$**
