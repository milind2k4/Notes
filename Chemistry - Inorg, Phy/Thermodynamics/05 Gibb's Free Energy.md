Links: [[00 Thermodynamics]], [[03 Entropy]]
___
# Gibb's Free Energy (G)
Mathematically,
$$G = H - TS$$

At constant pressure and temp.,
$$q_{p} = dH$$
And, we know that,
$$dS_{sur} = -\frac{ q_{p} }{ T }$$

Thus,
$$
\begin{split}
dG &= dH - TdS - SdT \\
(dG)_{sys, T,P} &= q_{p} - TdS_{sys} \\
&= -TdS_{sur} - TdS_{sys} \\
&= -TdS_{total}   
\end{split}
$$

From this we get,
$$\Delta G_{sys} = -T\Delta S$$

Thus, 
- If $\Delta S = +ve$, then $\Delta G_{sys} = -ve$ and the process is spontaneous. 
- If $\Delta S = 0$, then $\Delta G_{sys} = 0$ and the process is reversible or equilibrium state. 
- If $\Delta S = -ve$, then $\Delta G_{sys} = +ve$ and the process is non-spontaneous.

Hence, $\Delta G_{T,P}$ establishes an alternate criteria for spontaneity.

#### Calculation of $\Delta G$
$$
\begin{split}
G &= H - TS \\
dG &= dH - TdS - SdT \\
\end{split}
$$

At constant temp. and pressure,
$$\Delta G_{sys,T,P} = \Delta H_{sys} - T\Delta S_{sys}$$

If the value of T is more than $\displaystyle \frac{ \Delta H }{ \Delta S }$ the it is high temp otherwise it is low. 

### Physical Signification of $\Delta G_{r}$
$$
\begin{split}
G &= H - TS \\
dG &= dH - TdS - SdT \\
&= d(U + PV) - TdS - SdT \\
&= dU + PdV + VdP - TdS - SdT \\
&= (q_{rev} + W_{rev}) + PdV + VdP - TdS - SdT \\
&= TdS + W_{PV} + W_{non-PV} + PdV + VdP - TdS - SdT \\
&= -PdV + W_{non-PV} + PdV + VdP - SdT \\
&= W_{non-PV} + VdP - SdT
\end{split}
$$
At constant pressure and temp.,
$$(dG)_{T,P} = W_{non-PV}$$
Thus, **change in Gibb's Energy at constant P and T is the measure of max. non-PV work that can be obtained from the system.**

Common example of non-PV work is electrical work.
[[01 Galvanic Cell]]

$(\Delta G_{r}^{o})_{P,T}$ is also called *useful work.*

### Dependence of G on P and T
$$dG = W_{non-PV} + VdP - SdT$$
Considering no non-PV work,
$$dG = VdP - SdT$$
Thus,
$$\left( \frac{ \partial G }{ \partial P } \right)_{T} = V$$
$$\left( \frac{ \partial G }{ \partial T } \right)_{P} = -S$$

For an ideal gas at constant temp.,
$$
\begin{split}
\Delta G &= \int_{1}^{2} (VdP - SdT) \\
&= \int_{1}^{2} \frac{ nRT }{ P } \, dP \\
&= nRT \ln \frac{ P_{2} }{ P_{1} }  
\end{split}
$$

For a solid/liquid at constant temp., since V is nearly constant,
$$
\begin{split}
\Delta G &= \int_{1}^{2} VdP - SdT \\
&= V\Delta P 
\end{split}
$$

### Relation b/w Equilibrium Constant and $\Delta G_{r}^{o}$
[[00 Chemical Equilibrium#Thermodynamics of Equilibrium]]

$$\Delta G_{r} = \Delta G_{r}^{o} + RT\ln Q$$
$$\Delta G_{r} = \Delta G_{r}^{o} + 2.303 RT\log Q$$

$\Delta G^{o}_{r}$ is std. Gibb's Energy of reaction.

At equilibrium, $\Delta G_{r} = 0$, and $Q = k_{eq}$.
$$\Delta G_{r} = -RT\ln k_{eq} = \Delta H_{r}^{o} - T\Delta S_{r}^{o}$$

At equilibrium, $\Delta G_{r} = 0$ but $\Delta G_{r}^{o}$ need not be zero.

### Dependence of Spontaneity on T
$\Delta H_{r}$ and $\Delta S_{r}$ are taken constant, and independent of temp..

| Sign of $\Delta H$ | Sign of $\Delta S$ | Sign of $\Delta G$                     |
| ------------------ | ------------------ | -------------------------------------- |
| -ve                | +ve                | -ve always. Thus rex. is spo. at all T |
| +ve                | -ve                | +ve always. Non-spo. at all T          |
| -ve                | -ve                | -ve at low temp.. +ve at high temp..   |
| +ve                | +ve                | -ve at high temp.. +ve at low temp..                                       |

**Exothermic Process ($\Delta H < 0$):**
1. $\Delta S > 0$, $\Delta G < 0$ i.e. Always spontaneous. 
2. $\Delta S < 0$: 
	- If low temp. then $\Delta G < 0$
	- If high temp. then $\Delta G > 0$

Thus, exothermic process is non-spontaneous at high temperatures. 

**Endothermic Process ($\Delta H > 0$):**
1. $\Delta S < 0$: $\Delta G > 0$ i.e. Always non-spontaneous. 
2. $\Delta S > 0$: 
	- If  low temp. then $\Delta G > 0$
	- If high temp. then $\Delta G < 0$

Thus, exothermic process is non-spontaneous at low temperatures. 

![[Pasted image 20240315210801.png]]