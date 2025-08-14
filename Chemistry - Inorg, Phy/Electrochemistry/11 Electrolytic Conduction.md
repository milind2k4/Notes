Links: [[08 Electrolytic Cell]], [[12 Kohlrausch's Law and Titration]]
___
# Electrolytic Conduction
Movement of ions in molten or aqueous electrolyte under electric field. 

| Metallic Conduction                                                                                                                     | Electrolytic Conduction                                                                                                |
| --------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| Due to movement of e in metals under E field.                                                                                           | Due to movement of ions under E field.                                                                                 | 
| Composition of metallic conductor remains unchanged.                                                                                    | Composition of electrolytic solution may change after conduction due to [[08 Electrolytic Cell\|electrolysis]].        |
| Depends on type of metal, its crystal structure, no. of valence e per metal atom, length and area of cross section of wire, temp.  etc. | Depends on nature of electrolyte (strong or weak), concentration, viscosity of solution, nature of solvent, temp. etc. |

Viscosity because it is kind of resistance against mobility of e. 

As temperature increases *electrolytic conduction increases* as mobility of ions increases (due to decrease in viscosity) but *metallic conduction decreases.* 

#### Terms 
[[01 Ohm's Law]]

**Conductance** is the inverse of resistance,
$$G = \frac{1}{R} = \frac{1}{\rho} \frac{ A }{ l }$$
$$G = \kappa\frac{ A }{ l }$$
Its unit is $\ohm ^{-1}$ or mho ($\mho$) or Siemens (S)

**Conductivity** (or Specific Conductance) is inverse of resistivity,
$$\kappa = \frac{1}{\rho} = G\frac{ l }{ A }$$
Its unit is $\ce{ \ohm^{-1} cm^{-1} or S cm^{-1} }$

The $l /A$ is called **Cell Constant** and has unit $\ce{ cm^{-1} or m^{-1} }$.

$l$ is the separation between the electrodes and $A$ is the common surface area of the plate dipping in the solution. 

Common surface area means the area of the plate dipped in solution common in both the plates. 
Thus if half of plate is dipped in solution, A becomes A/2. If one of the plates is taken half out of the cell, A becomes A/2.

If one of the plates is fully taken out of the solution, A becomes 0.

![[Pasted image 20240222162353.png]]

#### Conductivity 
$$
\begin{split}
\kappa &= G \frac{ l }{ A } \frac{ l }{ l } \\
&= G \frac{ l^{2} }{ V } \\
\end{split}
$$
If $l = 1\ cm$ (i.e. unity) and A is taken as $A = 1\ cm^{2}$ then V becomes $V = 1\ cm^{3}$ i.e. unit volume of the solution. 
Then,
$$\kappa = G$$

Conductivity is the conductance of unit volume of solution filled between two parallel electrodes unit distance apart.

Conductivity is additive property. I.e. total conductivity is the sum of individual conductivities in the cell.

$$
\begin{split}
\kappa_{T} &= \kappa_{1} + \kappa_{2} + \kappa_{3} + \dots + \kappa_\text{water} \\
G_{T} \frac{ l }{ A } &= G_{1} \frac{ l }{ A } + G_{2} \frac{ l }{ A } + G_{3} \frac{ l }{ A } + \dots + G_\text{water} \frac{ l }{ A } \\
G_{T} &= G_{1} + G_{2} + G_{3} + \dots + G_\text{water} \\
\frac{ 1 }{ R_{T} } &= \frac{ 1 }{ R_{1} } + \frac{ 1 }{ R_{2} } + \frac{ 1 }{ R_{3} } + \dots \frac{ 1 }{ R_\text{water} } + 
\end{split}
$$

This indicates that various electrolytes in solution are connected in parallel. 

$\kappa _\text{water}$ is very small for pure water due to extremely low self ionisation. Thus it can be ignored in questions if its data is not given. 

If two solutions are mixed, their conductivity is taken to vary linearly and we write,
$$\kappa_{f} = \frac{ \kappa_{1}V_{1} + \kappa_{2}V_{2} }{ V_{1} + V_{2} }$$

### Molar Conductivity 
or **Molar Conductance**

$\Lambda_{m}$ is used for complete electrolyte. 
$\lambda_{m}$ is used for individual electrolyte. 

It is the conductance of solutions which contains one mole of electrolyte filled between filled between electrodes unit distance apart and large enough to accommodate complete volume.

In molar conductance, volume can be whatever, but in conductivity, the volume needs to be unit volume.

$$
\begin{split}
\kappa &= G \frac{ l^{2} }{ V } \\
G &= \kappa \frac{ V }{ l^{2} } 
\end{split}
$$
If $l = 1$ and 1 mole of electrolyte is taken,
$$
\begin{split}
\Lambda_{m} &= G \\
&= \kappa V
\end{split}
$$
where V is the volume of solution having 1 mole of electrolyte. 

Concentration is given as c mol/lit.

- In CGS units, we can write,
	$$
	\begin{split}
	\ce{ 
	c mol &-> 1 lit (10^{3} cc) \\
	1 mol &-> \frac{ 1000 }{ c } cc = V
	 }
	\end{split}
	$$

	Thus,
	$$\Lambda_{m} = \frac{ \kappa \times 1000 }{ \text{Molaity} }$$
	where $\kappa$ is in $\ce{ S cm^{-1} }$.

	And unit of $\Lambda_{m}$ in CGS units is $\ce{ \ohm^{-1}cm^{2} mol^{-1} }$
	$\\$

- In SI units, we can write,
	$$
	\begin{split}
	\ce{ 
	c mol &-> 1 lit (10^{-3} m^{3}) \\
	1 mol &-> \frac{ 1 }{ 1000 \times c } m^{3} = V
	 }
	\end{split}
	$$
	
	Thus,
	$$\Lambda_{m} = \frac{ \kappa }{ 1000 \times \text{Molaity} }$$
	where $\kappa$ is in $\ce{ S m^{-1} }$.
	
	And unit of $\lambda_{m}$ in SI units is $\ce{ \ohm^{-1}m^{2} mol^{-1} }$

### Equivalent Conductivity
The same as Molar Conductivity just that "1 mole" is replaced by 1 gram equivalent of electrolyte.

Thus, "Molarity" will be replaced by "Normality".

$$\Lambda_{eq} = \frac{ \kappa \times 1000 }{ \text{Normality} }$$
when $\kappa$ is in $\ce{ S cm^{-1} }$ giving unit of $\Lambda_{eq}$ as $\ce{ S cm^{2} eq^{-1} }$

$$\Lambda_{eq} = \frac{ \kappa }{ 1000 \times \text{Normality} }$$
when $\kappa$ is in $\ce{ S cm^{-1} }$ giving unit of $\Lambda_{eq}$ as $\ce{ S m^{2} eq^{-1} }$

From this we can see that,
$$
\begin{split}
\frac{ \Lambda_{eq} }{ \Lambda_{eq} } &= \frac{ 1000\kappa /N }{ 1000\kappa /M } \\
&= \frac{ M }{ N } \\
&= \frac{ M }{ M \times vf } \\
\Lambda_{eq} &= \frac{ \Lambda_{m} }{ vf }
\end{split}
$$

Where valency factor of electrolyte is the total +ve charge or total -ve charge per formula unit.

## Effect of Concentration Variation 
Dilution is the reciprocal of concentration. 
$$\ce{ dilution \propto \frac{ 1 }{ concentration } }$$

#### Conductivity 
Since conductivity is the conductance of unit volume of solution, as we decrease conc., the conductivity decreases as the no. of ions in the unit volume decreases.

$$\ce{ \kappa \propto concentration }$$

#### Molar or Equivalent Conductivity 
[[02 Arrhenius Theory and Ostwald's Law#Ostwald Dilution Law]]

$\Lambda_{m}$ is the conductance of solution having 1 mole of electrolyte. 

**For a weak electrolyte solution,** dilution means greater degree of dissociation ($\alpha$) of weak electrolyte and hence no. of current carrying ions increases and thus $\Lambda_{m}$ increases sharply. (Ostwald's Law)

**For a strong electrolyte solution,** increasing dilution the no. of current carrying ions do not increase, but the frictional resistance between the ions moving towards electrodes decreases and hence mobility ions increases. As a result of this, $\lambda_{m}$ increases gradually on dilution.

$\Lambda^{o}_{m}$ is the molar conductivity at infinite dilution, called *Limiting Molar Conductivity.*

Strong electrolytes follow Debye-Huckel-Onsager equation,
$$\Lambda_{m} = \Lambda^{o}_{m} - b\sqrt{ c }$$
$b$ is a constant which depends on viscosity of medium, nature of electrolyte and temp.. $b$ is same for all 1:1 electrolytes of similar types. (like KCl and NaCl or $\ce{ BaCl_{2} and SrCl_{2} }$)

![[Molar Cond of Weak and Strong Elec.png]]
![[Pasted image 20240222172613.png]]

From this graph, we can find the conductivity of strong electrolyte at 0 concentration by extrapolating the graph. 

However, we cannot extrapolate the graph of weak electrolyte and thus we cannot determine $\Lambda^{o}_{m}$ for it. 

Since variation of $\Lambda_{m}$ is very small for strong electrolytes, it can be taken constant in numerical questions. 