Links: [[01 Heat Capacity and Internal Energy]]
___
# Processes
Determination of $\Delta U, \Delta H, Q, W$ in various processes for an ideal gas.

### Isothermal
[[01 Processes#Isothermal]]

For an ideal gas, since $U = f(T), H = f(T)$, thus,
$$
\begin{split}
\Delta U &= 0 \\
\Delta H &= 0
\end{split}
$$

Using first law,
$$
\begin{split}
\Delta U &= q + W \\
q &= -W
\end{split}
$$

#### W in Reversible Isothermal
Equation of reversible isothermal process for ideal gas,
$$PV = nRT = \text{const.}$$

Thus, work done is,
$$
\begin{split}
W_{isoT(rev)} &= - \int_{1}^{2} P_{ext} \, dV \\
&= - \int_{1}^{2} (P \pm dP) \, dV \\
&= - \int_{1}^{2} P \, dV \pm \cancelto{ \text{ignored} }{ \int_{1}^{2} dP \, dV } \\
&= -\int_{1}^{2} \frac{ nRT }{ V } \, dV \\
&= -nRT \ln \frac{ V_{2} }{ V_{1} } \\
&= -nRT \ln \frac{ P_{1} }{ P_{2} }
\end{split}
$$

Thus, for expansion, $W < 0$, for compression $W > 0$.

##### PV Curve for Reversible
Magnitude of work done in any process is equal to the area under the PV curve. We move from left to right, the area is +ve above the x-axis. 

Here the PV curve is rectangular hyperbola.

![[Pasted image 20240313192314.png]]

#### W in Irreversible Isothermal 
In irreversible process (any) no mathematical relation exists between P-T or V-T or P-V. 

Here,
$$P_{ext} = P_{f}$$

And work done is,
$$W = P_{ext}(\Delta V)$$

Work done in irreversible process > work done in reversible process. This is applicable for both expansion and compression.

However, magnitudes can be different. 

![[Pasted image 20240313193230.png]]

##### PV Curve for Irreversible 
Here we cannot find a definite curve as no relation between P-V exists. 

However, we can represent approximately keeping work done in mind. 

![[Pasted image 20240313193629.png]]

Comparison of work done,
![[Pasted image 20240313194039.png]]

### Isobaric
[[01 Processes#Isobaric]]

$$
\begin{split}
W &= -P \Delta V \\
\Delta U &= nC_{V}\Delta T \\
\Delta H &= nC_{P}\Delta T \\
&= q_{P} \\
\end{split}
$$

For ideal gas,
$$
\begin{split}
PV &= nRT \\
P\Delta V &= nR\Delta T\\
W &= -nR\Delta T 
\end{split}
$$

![[Pasted image 20240313195803.png]]

### Isochoric Process
[[01 Processes#Isochoric]]

Since there is no change in volume,
$$W = 0$$

Thus,
$$
\begin{split}
\Delta U &= q + 0 \\
&= q_{V} \\
&= nC_{V}\Delta T
\end{split}
$$

### Adiabatic 
[[02 Adiabatic]]

There is no heat exchange and thus, $q = 0$.

$$
\begin{split}
\Delta U &= W \\
&= nC_{V}\Delta T \\
\Delta H &= nC_{P}\Delta T 
\end{split}
$$

Work done,
$$
\begin{split}
W &= nC_{V}\Delta T \\
&= \frac{ nR\Delta T }{ \upgamma-1 } \\
&= \frac{ \Delta(PV) }{ \upgamma-1 }
\end{split}
$$
This is applicable for both reversible and irreversible.

But the work done in irreversible and reversible will be different as the values of P and V are different.

##### Reversible Adiabatic
$$
\begin{split}
nC_{V}dT &= -PdV \\
n \frac{ R }{ (\upgamma-1) }dT &= - \frac{ nRT }{ V }dV \\
\frac{ dT }{ T } &= -(\upgamma-1) \frac{ dV }{ V } \\
\\
\ln \frac{ T_{2} }{ T_{1} } &= -(\upgamma-1) \ln \frac{ V_{2} }{ V_{1} } \\
\ln \frac{ T_{2} }{ T_{1} } &= \ln \left( \frac{ V_{1} }{ V_{2} } \right)^{(\upgamma-1)} \\
\frac{ T_{2} }{ T_{1} } &= \left( \frac{ V_{1} }{ V_{2} } \right)^{\upgamma-1} 
\end{split}
$$
Thus, finally,
$$T_{2}V_{2}^{\upgamma-1} = T_{1}V_{1}^{\upgamma-1}$$

I.e.,
$$TV^{\upgamma-1} = \text{const.}$$

In terms of P and V,
$$PV^{\upgamma} = \text{const.}$$

And in terms of P and T,
$$P^{1-\upgamma}T^{\upgamma} = \text{const.}$$

##### Irreversible Adiabatic 
$$
\begin{split}
\Delta U &= W \\
nC_{V}\Delta T &= -P_{ext} \Delta V \\
nC_{V}(T_{f} - T_{i}) &= -P_{ext} (V_{f} - V_{i}) \\
nC_{V}(T_{f} - T_{i}) &= -P_{ext} \left( \frac{ nRT_{f} }{ P_{f} } - \frac{ nRT_{i} }{ P_{i} } \right) \\
\end{split}
$$

![[Pasted image 20240313202921.png]]

##### Comparison of Rev. and Irr. Adiabatic
Same as isothermal. i.e.
$$W_{irr} > W_{rev}$$

The final temperature of irreversible process is always more than that of reversible process, if starting with the same temperature. 
$$(T_{f})_{irr} > (T_{f})_{rev}$$

This is applicable for both compression and expansion. 

**Graphical Comparison,**
![[Pasted image 20240313204154.png]]

##### Comparison of Rev. Adiabatic & Rev. Isothermal
[[02 Adiabatic#Comparison between Adiabatic and Isothermal]]

Rev. Isothermal,
$$PV = \text{const.}$$
Rev. Adiabatic,
$$PV^{\upgamma} = \text{const.}$$

Slope of P-V curve in Isothermal,
$$m_{i} = \frac{-P}{V}$$

Slope of P-V curve in Adiabatic,
$$m_{a} = \frac{-\upgamma P}{V}$$

Thus, since $\upgamma > 1$,
$$\ce{ |(slope)_\text{isothermal}| < |(slope)_\text{adiabatic}| }$$
i.e. the steeper curve is Adiabatic. 

![[Pasted image 20240313204604.png]]

##### Examples 
![[Pasted image 20240313205507.png]]

![[Pasted image 20240313205516.png]]

### Cyclic Process
[[01 Processes#Cyclic Process]]

When the system undergoes series of processes and finally returns to its original state. 

Thus, change in state function is,
$$\Delta \phi = 0$$
However, infinitesimally small change need not be zero.
$$d\phi \neq 0$$

Thus,
$$
\begin{split}
\Delta T &= 0 \\
\Delta P &= 0 \\
\Delta S &= 0 \\
\Delta H &= 0 \\
\Delta G &= 0 \\
\Delta U &= 0 \\
\end{split}
$$

Thus, 
$$q = -W$$

If the cycle is Clockwise, $W = -ve$
If the cycle is Anti-clockwise, $W = +ve$

![[Pasted image 20240313210040.png]]

Work done in a cyclic process need not be zero. It can be zero in special case. 

W is zero if there are even no. of loops with equal and there are equal no. of clockwise and anti clockwise loops.

![[Pasted image 20240313210217.png]]

