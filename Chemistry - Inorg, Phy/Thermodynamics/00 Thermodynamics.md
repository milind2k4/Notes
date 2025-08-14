Links: [[00 KTG & Thermodynamics]]
___
# Thermodynamics
In thermodynamics, we can predict the feasibility of a reaction. I.e. whether the reaction will take place or not. 

If the reaction takes place then what are the energy changes involved during it, can also be predicted.

### [[00.5 Definitions]]

### Processes
 [[00 KTG & Thermodynamics#Processes]]
 
Path through which system undergoes change of state. 
1. *Isothermal:* T is constant throughout, $dT = 0$. 
1. *Isochoric:* V is constant throughout, $dV = 0$. 
1. *Isobaric:* P is constant throughout, $dP = 0$. 
1. *Adiabatic:* No heat exchange b/w system and surroundings, $Q = 0$. 
1. *Cyclic:* Initial and final states are the same, $\Delta \phi = 0$. 

##### Reversible and Irreversible Process
1. **Reversible process:** (aka Quasi static process)
	- Infinitesimally slow process. 
	- It takes an infinite no. of steps for completing a finite change. 
	- It is an extremely slow, hypothetical process. 
	- dP and dT are infinitesimally small.
	$$P_\text{ext} = P + dP$$
	$$T_\text{ext} = T + dT$$
	- System and surroundings are always in thermodynamic equilibrium during the process. 
	- If path of reversible process is reversed, then both system and surroundings come back to their original state.
	  $\\$


2. **Irreversible:** 
	- Relatively fast process.
	- Completes in a finite no. of steps.
	- All natural or spontaneous processes are irreversible. 
	- $\Delta P, \Delta T$ are finite quantities.
	$$P_\text{ext} = P + \Delta P$$
	$$T_\text{ext} = T + \Delta T$$
	- Equilibrium exists only at initial and final states.
	- If path of irreversible process is reversed, then either system or surrounding or both will not come to their initial state. 

#### Process Table

| Process     | $$W$$                                               | $$q$$     | $$\Delta U$$        | $$\Delta H$$        | $$C$$                                  |
| ----------- | --------------------------------------------------- | --------- | ------------------- | ------------------- | -------------------------------------- |
| Isochoric   | $$0$$                                               | $$q_{v}$$ | $$q_{v}$$           | $$nC_{Pm}\Delta T$$ | $$C_{V}$$                              |
| Isobaric    | $$-P_{ext}\Delta V$$                                | $$q_{p}$$ | $$nC_{Vm}\Delta T$$ | $$nC_{Pm}\Delta T$$ | $$C_{P}$$                              |
| Isothermal  | $$-nRT \ln\left( \frac{ V_{2} }{ V_{1} } \right) $$ | $$-W$$    | $$0$$               | $$0$$               | $$\infty$$                             |
| Isothermal  | $$-P_{ext}(V_{2} - V_{1})$$                         | $$-W$$    | $$0$$               | $$0$$               | $$\infty$$                             |
| Adiabatic   | $$\frac{ nR\Delta T }{ \upgamma - 1 }$$             | $$0$$     | $$W$$               | $$nC_{Pm}\Delta T$$ | $$0$$                                  |
| Polytrophic | $$\frac{ nR\Delta T }{ x-1 }$$                      | $$q$$     | $$nC_{Vm}\Delta T$$ | $$nC_{Pm}\Delta T$$ | $$C_{m} = C_{Vm} - \frac{ R }{ 1-x }$$ |

### Modes of Energy Transfer
Either Heat or Work. 

Heat is when there is temperature difference. 
The temperature difference should be between the system and surrounding. 
Work is when it is anything other than temperature difference.   

Same energy can be called Heat or Work depending on the choice of the system. 

#### Work
[[00 KTG & Thermodynamics#Work Done by Gas]]

1. **Mechanical Work or PV Work or Displacement Work**
2. **Non-Mechanical Work or Non-PV Work** (e.g. electrical work obtained in Galvanic Cell.)

Mechanical work, when ext. P is constant. 
$$
\begin{split}
W &= - \int_{1}^{2} P_\text{ext} \, dV \\
&= - P_{ext} \Delta V
\end{split}
$$

Work done is zero when,
1. Process is isochoric ($\Delta V = 0$)
2. Free Expansion (exp. against vacuum) ($P_{ext} = 0$)

$\ce{1 lit-bar = 100 J }$
$\ce{1 lit-atm = 101.33 J }$

##### IUPAC Sign Convention
In chemistry,

- Any heat liberated is -ve.
- Any heat absorbed is +ve. 

Thus, for work,
- Work done on the system (compression) is +ve.
- Work done by the system (expansion) is -ve.

Opposite of Physics.

#### Heat (Q) 
Energy that flows b/w system and surrounding due to temp. difference. 

Heat given to system is +ve and heat taken from system is -ve.

Heat is low grade and random form of energy. 
Work is high grade and organised form of energy. 

### First Law of Thermodynamics
[[00 KTG & Thermodynamics#First Law]]

It is the law of conservation of energy. It indicated that energy of the universe is constant.

The change in internal energy is equal to the amount of work done on the system plus the amount of heat provided to it. 

For a closed system,
$$dU = q + W$$
q and W should be put with signs. 

At constant volume,
$$
\begin{split}
dU &= q_{V} + PdV \\
&= q_{V} + 0 \\
dU &= q_{V}
\end{split}
$$

Thus, heat given at constant volume is equal to change in internal energy.

And we have,
Thus,
$$
\begin{split}
Q_{P} &= \Delta H \\
Q_{V} &= \Delta U
\end{split}
$$

## Enthalpy (H)
State function and Extensive property. 

It is defined as,
$$H = U + PV$$

Thus,
$$dH = dU + PdV + VdP$$

At constant pressure,
$$
\begin{split}
dH &= q_{P} + W + PdV \\
&= q_{P} - PdV + PdV \\
&= q_{P} \\
&= nC_{P}dT
\end{split}
$$

Thus, heat given at constant pressure is equal to enthalpy change of system.

$$\Delta H = n \int_{1}^{2} C_{P} \, dT$$

If $C_{P}$ is constant,
$$\Delta H = nC_{P}\Delta T$$

It is applicable for any process for ideal gas. 

##### Relation b/w $\Delta H$ and $\Delta U$
$$
\begin{split}
H &= U + PV \\
\Delta H &= \Delta U + \Delta(PV) \\
&= \Delta U + (P_{2}V_{2} - P_{1}V_{1})
\end{split}
$$

Note that the $\Delta(PV)$ term is ignored for solids and liquids in comparison to gases.

For ideal gases, for constant temp., **(approximation)**
$$
\begin{split}
PV &= nRT \\
\Delta(PV) &= \Delta n_{g} RT
\end{split}
$$

Thus,
$$\Delta H = \Delta U + \Delta n_{g} RT$$
where $\Delta n_{g}$ is,
$\Delta n_{g} =$ sum of st. coef. of gas prod. - sum of st. coef. of gas react.

This equation cannot be applied if gases show sig. deviations from ideal behaviour. 

![[Pasted image 20240312213737.png]]






















