Links: [[01  Law of Mass Action]], [[03 Applications of Eq. Constant]]
___
# Characteristics of Equilibrium Constant 
If the reaction is changed, the k changes. And if the reaction is reversed, k becomes reciprocal 
$$\ce{ A + B <=> C + D }$$
$$\ce{ k_{c} = \frac{ [C] [D] }{ [A] [B] } }$$
$$\ce{ C + D <=> A + B }$$
$$\ce{ k'_{c} = \frac{ [A] [B] }{ [C] [D] } } = \frac{ 1 }{ k_{c} }$$

If a factor is multiplied with a factor, k changes, k is raised to the factor,
$$\ce{ N_{2}O_{4} <=> 2NO_{2} }$$
$$\ce{ k_{p} = \frac{ p_{NO_{2}}^{2} }{ p_{N_{2}O_{4}} } }$$
$$\ce{ 1/2N_{2}O_{4} <=> NO_{2} }$$
$$\ce{ k'_{p} = \frac{ p_{NO_{2}} }{ p_{N_{2}O_{4}}^{1/2} } = (k_{p})^{1/2} }$$

If two reactions are added, the respective ks are multiplied,
$$\ce{ A <=> C, k_{c_{1}} = \frac{ [C] }{ [A] } }$$
$$\ce{ B <=> D, k_{c_{2}} = \frac{ [D] }{ [B] } }$$
Adding them,
$$\ce{ A + B <=> C + D }$$
$$\ce{ k_{c} = \frac{ [C] [D] }{ [A] [B] } = k_{c_{1}} . k_{c_{2}} }$$

### Effect of temp. on k
#important 
From Chemical Kinetics, Arrhenius equation,
$$k = Ae^{ -E_{a}/RT }$$
where,
$k \to$ rate constant
$A \to$ Arrhenius constant
$E_{a} \to$ Activation energy of reaction
$T \to$ temp. in kelvin

A and $E_{a}$ are independent of temp. 

Enthalpy of reaction is, 
$$\Delta H_{r} = E_{af} - E_{ab}$$
where f and b are forward and backward.

The equilibrium constant and thus be written as,
$$
\begin{split}
k_{eq} &= \frac{ A_{f} e^{ -E_{af}/RT } }{ A_{b} e^{ -E_{ab}/RT } } \\
k_{eq} &= \frac{ A_{f} }{ A_{b} } \times e^{ -(E_{af} - E_{ab})/RT }
\end{split}
$$

Giving,
$$\ce{ k_{eq} = \frac{ A_{f} }{ A_{b} }\times e^{ \Delta H_{r}/RT } }$$

Taking ln,
$$\ce{ \ln k_{eq} = \ln \frac{A_{f}}{A_{b}} - \frac{ \Delta H_{r} }{ RT } }$$

Taking $\ln k_{eq} = y$ and $1 /T = x$, we get,
$$c = \ln \frac{ A_{f} }{ A_{b} }$$
$$m = \frac{ -\Delta H_{r} }{ R }$$

![[Pasted image 20230612205340.png]]

From the graph we can see that,
1. For Exothermic, $T \uparrow \implies k_{eq} \downarrow$
2. For Endothermic, $T \uparrow \implies k_{eq} \uparrow$

Rate constant, $k_{f}, k_{b}$, however, always increases on increase in temp. irrespective of endo or exothermic reaction. 

### Van't Hoff Equation
#### Integral form
$$\ce{ \ln k_{eq} = \ln \frac{A_{f}}{A_{b}} - \frac{ \Delta H_{r} }{ RT } }$$

At temp. $T_{1}$,
$$\ln k_{eq(T_{1})} = \ln \frac{ A_{f} }{ A_{b} } - \frac{ \Delta H_{r} }{ RT_{1} }$$

At temp. $T_{2}$,
$$\ln k_{eq(T_{2})} = \ln \frac{ A_{f} }{ A_{b} } - \frac{ \Delta H_{r} }{ RT_{2} }$$

Subtracting 2 from 1,
$$\ln \frac{ k_{eq(T_{2})} }{ k_{eq(T_{1})} } = \frac{ \Delta H_{r} }{ R } \left[ \frac{ 1 }{ T_{1} } - \frac{ 1 }{ T_{2} } \right]$$
This is called the integral form of Van't Hoff equation. 

Converting this to base 10,
$$\log_{10} \frac{ k_{eq(T_{2})} }{ k_{eq(T_{1})} } = \frac{ \Delta H_{r} }{ 2.303 R } \left[ \frac{ 1 }{ T_{1} } - \frac{ 1 }{ T_{2} } \right]$$

#### Differential form
$$\ce{ \ln k_{eq} = \ln \frac{A_{f}}{A_{b}} - \frac{ \Delta H_{r} }{ RT } }$$
Differentiating this, wrt T,
$$\frac{ d(\ln k_{eq}) }{ dT } = 0 - \frac{ \Delta H_{r} }{ R }\left[ \frac{ -1 }{ T^{2} } \right]$$
$$d(\ln k_{eq}) = \frac{ \Delta H_{r} }{ RT^{2} }dT$$

### Examples
Here to find whether the process is endo or exo, we find the k at different temp.. If at the larger k is lower, then the reaction is exothermic otherwise endothermic. 
![[Pasted image 20230612212009.png]]

## Relation between $k_{p}$ and $k_{c}$
With of without pure solids/liquids

$$\ce{ aA {}_{(g)} + bB {}_{(g)} <=> cC {}_{(g)} dD {}_{(g)} }$$

$$k_{c} = \frac{ [C]^{c} \cdot [D]^{d} }{ [A]^{a} \cdot [B]^{b} }$$

$$k_{p} = \frac{ p_{C}^{c} \cdot p_{D}^{d} }{ p_{A}^{a} \cdot p_{B}^{b} }$$

For a gas,
$$\ce{ p_{A} = [A]RT }$$
Thus,
$$\ce{ k_{p} = \frac{ [C]^{c}(RT)^{c} [D]^{d}(RT)^{d} }{ [A]^{a}(RT)^{a} [B]^{b}(RT)^{b} } }$$
$$\ce{ k_{p} = k_{c} (RT)^{c+d-a-b} }$$

Giving,
$$k_{p} = k_{c}(RT)^{\Delta n_{g}}$$

Where,
$$\Delta n_{g} = \sum \text{st. coeff. of gaseous prod.} - \sum \text{st. coeff. of gaseous react.}$$
thus,
$$\Delta n_{g} = (c+d) - (a+b)$$

Now, at constant temp.,
$$\Delta n_{g} = 0 \implies k_{p} = k_{c}$$
$$\Delta n_{g} > 0 \implies k_{p} > k_{c}$$
$$\Delta n_{g} < 0 \implies k_{p} < k_{c}$$