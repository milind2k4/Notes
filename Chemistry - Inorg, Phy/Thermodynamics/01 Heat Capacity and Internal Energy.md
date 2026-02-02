Links: 
___
# Heat Capacity and Internal Energy
### Molar Heat Capacity (C)
[[03 Molar Heat Capacity]]

Heat required to raised temp. of 1 mol of substance through 1 K. It is a path function. 

$$C = \frac{ q }{ ndT }$$
Thus, heat is,
$$q = nCdT$$

If C is constant,
$$
\begin{split}
Q &= \int_{1}^{2} nC \, dT \\
&= n \int_{1}^{2} C \, dT \\
&= nC\Delta T  
\end{split}
$$

Heat capacity is of two types,
1. **Constant Volume ($C_{V}$)**
	$$C_{V} = \frac{ q_{v} }{ ndT }$$
1. **Constant Pressure ($C_{P}$)**
	$$C_{P} = \frac{ q_{p} }{ ndT }$$
	And, $C_{P} > C_{V}$ for a gas.


Except monoatomic gas, $C_{P}$ or $C_{V}$ or $C$ depends on temp. for any substance. 

Heat given at constant volume is used to change internal energy. 
$$q_{v} = dU$$

For solids and liquids, $C_{P}$ and $C_{V}$ are almost equal as there is no significant effect of pressure on them.

##### Poisson's Ratio 
$$\upgamma = \frac{ C_{P} }{ C_{V} } = \frac{ C_{Pm} }{ C_{Vm} }$$

From Meyer's Equation,
$$
\begin{split}
\upgamma - 1 &= \frac{R}{C_{V}} \\
C_{V} &= \frac{ R }{ \upgamma - 1 } \\
C_{P} &= \frac{ \upgamma R }{ \upgamma-1 }
\end{split}
$$

##### For an ideal gas
$$C_{P} - C_{V} = R$$

| Gas                | $C_{V}$            | $C_{P}$            | $\upgamma$               |
| ------------------ | ------------------ | ------------------ | ------------------------ |
| Monoatomic         | $\frac{ 3 }{ 2 }R$ | $\frac{ 5 }{ 2 }R$ | $\frac{ 5 }{ 3 } = 1.67$ |
| Diatomic or (P nl) | $\frac{ 5 }{ 2 }R$ | $\frac{ 7 }{ 2 }R$ | $\frac{ 7 }{ 5 } = 1.4$  |
| Polyatomic (nl)    | $\frac{ 6 }{ 2 }R$ | $\frac{ 8 }{ 2 }R$ | $\frac{ 4 }{ 3 } = 1.33$ |

#### Relation b/w C and $C_{V}$ for an ideal gas
Ideal gas undergoes a process,
$$PV^{x} = c$$

From here,
$$
\begin{split}
\frac{ nRT }{ V }V^{x} &= c \\
TV^{x-1} &= c \\
T(x-1) V^{x-2} dV + V^{x-1}dT &= 0 \\
\frac{ dV }{ dT } &= - \frac{ V }{ T(x-1) }
\end{split}
$$

Then,
$$
\begin{split}
\frac{ dU }{ dT } &= \frac{ q }{ dT } + \frac{ W }{ dT } \\
C_{V} &= C - \frac{ pdV }{ dT } \\
C &= C_{V} + p \frac{ dV }{ dT } \\
&= C_{V} - \frac{ p V }{ T(x-1) } \\
&= C_{V} - \frac{ R }{ x-1 }
\end{split}
$$

Thus, general molar heat capacity,
$$C = C_{V} - \frac{ R }{ x-1 }$$

### Internal Energy (U or E)
[[00 KTG & Thermodynamics#Internal Energy of Gas]]

Energy possessed by molecules at rest and in absence of any external force field. 

Absolute value of U cannot be found. We only need change in internal energy in a process.

It includes,
- **Kinetic Energy:** Translational + Rotational + Vibrational 
- **Potential Energy:** Due to intermolecular forces. For ideal gas, PE = 0.
- **Bond Energy**
- **Nuclear Energy**
etc.

For a substance,
$$U = f(T,P)\ or\ f(T,V)$$

For an ideal gas,
$$U = f(T)$$
I.e. internal energy depends only on temp.

We can write,
$$
\begin{split}
dU &= \left( \frac{ \partial U }{ \partial T } \right)_{V} dT + \left( \frac{ \partial U }{ \partial V } \right)_{T}dV \\
&= C_{V}dT + \left( \frac{ \partial U }{ \partial V } \right)_{T}dV \\
\\
\text{Since T is const.}, \\
\left( \frac{ \partial U }{ \partial V } \right)_{T} &= 0 \\
\\
\text{Thus,} \\
dU &= C_{V}dT \\
&= nC_{V}dT
\end{split}
$$

If $C_{V}$ is independent of T,
$$\Delta U = nC_{V}\Delta T$$

This is applicable for every process for an ideal gas.
