Links: 
___
# Solid in Liquid Solution 
**Colligative Properties:** Properties which depend upon no. of solute particles present in solution and are independent of their nature. 

The chief purpose of colligative property is to determine molar mass of solute as all colligative properties can be experimentally measured for dilute solution. 

### Lowering in Vapour Pressure 
When a non volatile solute (like sugar) is dissolved in a volatile liquid, VP decreases. 

As per [[01 Liquid in Liquid#Raoult's Law|Raoult's Law,]] RLVP (Relative Lowering in Vapour Pressure) is equal to the mole fraction of solute in solution.

$p_{o}$ is VP of solvent. 
$p_{s}$ is VP of solution.
$p_{o} - p_{s}$ is the lowering in VP

And RLVP is,
$$\frac{ p_{o} - p_{s} }{ p_{o} }$$

From Raoult's law,
$$
\begin{split}
p_{s} &= x_\text{solute}. p^{o}_\text{solute} + x_\text{solvent} .p^{o}_\text{solvent} \\
p_{s} &= (1 - x_\text{solute}) p_{o} \\
\frac{ p_{o} - p_{s} }{ p_{o} } &= x_\text{solute} \\
&= \frac{ n }{ n + N }
\end{split}
$$
where n is the no. of moles of solute and N is the no. of moles of solvent.

Reciprocating it,
$$
\begin{split}
\frac{ p_{o} }{ p_{o} - p_{s} } &= 1 + \frac{ N }{ n } \\
\frac{ p_{s} }{ p_{o} - p_{s} } &= \frac{ N }{ n } \\
\frac{ p_{o} - p_{s} }{ p_{s} } &= \frac{ n }{ N }
\end{split}
$$
This is useful for solving questions. However, the LHS is not RLVP. 

Again, modifying the formula,
$$
\begin{split}
\frac{ p_{o} - p_{s} }{ p_{s} } &= \frac{ n }{ W_\text{solvent} /1000 } \frac{ M_\text{solvent} }{ 1000 } \\
&= \text{molality} \times \frac{ M_\text{solvent} }{ 1000 }
\end{split}
$$

##### Experimental Measurement of RLVP
aka **Ostwald and Walker method.**

When dry air is passed into a volatile liquid, there occurs a mass loss in liquid and this mass loss is directly proportional to VP of liquid. 

![[Pasted image 20240311203405.png]]
![[Pasted image 20240311203526.png]]

### Elevation in BP and Depression in FP 

$\Delta T_{b}$ is the elevation in BP,
$$\Delta T_{b} = T_{b(\text{soln.})} - T_{b(\text{solv.})} $$

$\Delta T_{f}$ is the depression in FP,
$$\Delta T_{f} = T_{f(\text{solv.})} - T_{f(\text{soln.})} $$

![[Pasted image 20240312163011.png]]

#### Elevation in BP
$$\Delta T_{b} = k_{b} \times m$$
where $k_{b}$ is called *molal elevation constant or Ebullioscopic constant* and it has unit K kg mol$^{-1}$. It is a property of solvent.
$m$ is the molality of solution. 

And.
$$k_{b} = \frac{ RT_{b}^{2} }{ 1000 L_{v} }$$
where $T_{b}$ is the boiling point of pure solvent in K and $L_{v}$ is latent heat of vaporisation in J/g or cal/g. 
R is universal gas constant,
$$\ce{ R = 8.314 J mol^{-1} K^{-1} = 2 cal mol^{-1} K^{-1} }$$

Also,
$$L_{v} = \frac{ \Delta H_{vap} }{ M_\text{solvent} }$$


#### Depression in FP
$$\Delta T_{f} = k_{f} \times m$$
where $k_{f}$ is called *Molal depression constant or Cryoscopic constant* and it has unit K kg mol$^{-1}$. It is a property of solvent.
$m$ is the molality of solution. 

And.
$$k_{f} = \frac{ RT_{f}^{2} }{ 1000 L_{f} }$$
where $T_{f}$ is the freezing point of pure solvent in K and $L_{f}$ is latent heat of fusion in J/g or cal/g. 

Also, 
$$L_{f} = \frac{ \Delta H_{fus} }{ M_\text{solvent} }$$

Example, #important 
![[Pasted image 20240312170035.png]]

This example shows that a solution freezes in a range of temps. 

### Osmotic Pressure
**Osmosis:** Spontaneous flow of solvent molecules from pure solvent to solution (or dilute sol. to conc. sol.) through semi permeable membrane (SPM).

Examples of SPM are Parchment paper, Animal Bladder, $\ce{ Cu_{2}[Fe(CN)6] }$ (artificial SPM) etc.

![[Pasted image 20240312175652.png]]

**Osmotic Pressure ($\pi$):** Hydrostatic pressure developed in on solution when solvent and solution are separated through SPM.
$$or$$
OP is the external pressure to be applied on the solution so that osmosis stops and level of solution and solvent become the same. 

There is a capillary rise in the tube till height h and thus we define Osmotic Pressure as,
$$\pi = hdg$$
where $d$ is the density of solution.

**Reverse Osmosis (RO):** When pressure greater than OP is applied on solution (or impure water) solvent molecules have net flow from solution to solvent through SPM. This is called RO. It is used to clean saline or impure water.

OP is most accurately measured for a dilute solution and hence for the most correct determination of molar mass of colloid particle, bacteria, polymer, protein molecule etc. OP should be used. 

For similar natured solutions (same $i$)(e.g. urea and glucose), on mixing the solutions, OP of final solution is,
$$\pi_{f} = \frac{ \pi_{1}V_{1} + \pi_{2}V_{2} }{ V_{1} + V_{2} }$$

#### Relation b/w Conc. and OP
It is found that,
$$\pi \propto \text{conc. of sol. at given T}$$

And thus, OP comes out to be,
$$\pi = CRT$$
where C is concentration of solution and T is temp. in K.

Using Van't Hoff Factor,
$$
\begin{split}
\pi &= iCRT \\
&= (i_{1}C_{1} + i_{2}C_{2} + \dots) RT \\
&= \frac{ (i_{1}n_{1} + i_{2}n_{2} + \dots) }{ V } RT
\end{split}
$$

### [[04 Van't Hoff Factor]]