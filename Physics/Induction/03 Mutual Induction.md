Links: [[02 Self Induction]]
___
# Mutual Inductance 
If there are two loops close to each other and we pass current through loop 1, it will create a magnetic field which will pass through loop 2, thus passing a flux through it. 

This flux is directly proportional to the current in loop 1. The proportionality constant is called mutual inductance. 

$$\phi_{2} \propto i_{1}$$
$$\phi_{2} = M i_{1}$$
where M is called the coefficient of mutual induction or **Mutual Inductance.**

Similar to self inductance, its unit is H. 

It depends on area of loops, their relative orientation, geometry, number of turns, current in the loop and medium.

![[Pasted image 20240117212552.png]]

The property of a coil which affects or changes the current and voltage in a secondary coil is called mutual inductance. 

##### Reciprocity Theorem 
It states that for one pair of loops, only one mutual inductance is defined. 

That is,
$$
\begin{split}
\phi_{2} &= Mi_{1} \\
\phi_{1} &= Mi_{2}
\end{split}
$$ 

#### Emf Induced 
Let, at time $t$ current through loop 1 is $i_{1}$ and at $t + \Delta t$ is $i_{1} + \Delta i_{1}$. 

Thus, at time t, flux through loop 2 is,
$$\phi_{2} = Mi_{1}$$
And at time $t + \Delta t$ it is,
$$\phi_{2} + \Delta \phi_{2} = Mi_{1} + M\Delta i_{1}$$

Due to this change there will be emf induced,
$$\varepsilon_{avg} = \frac{ \Delta \phi_{2} }{ \Delta t } = M \frac{ \Delta i_{1} }{ \Delta t }$$

for a small time interval $t \to t + dt$, current change is $i_{1} + di_{1}$, and the emf induced is,
$$\varepsilon = -\frac{ d\phi_{2} }{ dt } = -M \frac{ di_{1} }{ dt }$$

![[Pasted image 20240117213400.png]]

##### Examples
![[Pasted image 20240117213827.png]]

![[Pasted image 20240117214243.png]]
![[Pasted image 20240117214537.png]]

#### Derivation of M between two Coaxial Solenoids 
*(for boards)*

Consider two long co-axial solenoids each of length l. Area of inner solenoid $S_{1}$ is $A_{1}$ and that of solenoid $S_{2}$ is $A_{2}$. $n_{1},n_{2}$ are the number of turns per unit length of the solenoids. 

If $\phi_{21}$ is the flux linked with $S_{2}$ due to current in $S_{1}$, then,
$$\phi_{21} \propto I_{1}$$
$$\phi_{21} = M_{21}I_{1}$$
$M_{21}$ is the coefficient of mutual induction of the two solenoids. 

Magnetic field inside $S_{1}$ when current $I_{1}$ is passed through it,
$$B_{1} = \mu_{o}n_{1}I_{1}$$
Total magnetic flux linked with $S_{2}$,
$$\phi_{21} = B_{1}A \times n_{2}l = \mu_{o}n_{1}n_{2}AlI_{1}$$
Thus,
$$M_{21} = \mu_{o}n_{1}n_{2}Al$$

Similarly, when current is passed through $S_{2}$, mutual inductance of $S_{1}$ wrt $S_{2}$,
$$M_{12} = \mu_{o}n_{1}n_{2}Al$$

Thus,
$$M_{12} = M_{21} = M$$

##### Factors Affecting
1. Number of Turns
2. Cross-sectional Area
1. Separation between coils: More is the separation, less is the magnetic flux linked with the secondary coil.
2. Relative Orientation of Coils
   - M is minimum when they are perpendicular to each other because in this flux through the secondary coil is small.
   - When axes of the coils are the same then M has intermediate value.
   - When primary completely envelopes the secondary, the flux linkage is the max and thus M is max.
5. Permeability of core material
6. **Coefficient of coupling:** it gives the measure of the extent to which the coils are coupled together. It lies between 0 and 1.
	$$k = \frac{ M }{ \sqrt{ L_{1}L_{2} } }$$
	- When K = 1, there is perfect coupling and the entire flux of P is linked with S.

### Relation between M and Ls 
Mutual inductance is less than or equal to the geometric mean of the self inductances. 

$$M \leq \sqrt{ L_{1}L_{2} }$$

It will be equal when there is perfect coupling between them. 

Perfect coupling is when all the MLOF created by loop 1 passes through loop 2. 

We can write,
$$M = k\sqrt{ L_{1}L_{2} }$$
and $k$ is called coupling constant and is less than or equal to 1.

It will be zero when no MLOF created by loop 1 passes through loop 2. Or when they are perpendicular to each other. 

![[Pasted image 20240117214914.png]]

