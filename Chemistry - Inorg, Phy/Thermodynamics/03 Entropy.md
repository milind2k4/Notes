Links: [[01 Heat Capacity and Internal Energy]]
___
# Entropy (S)
It is a state function. It is an extensive property. 

It is a measure of the **Randomness** of the system. The higher is the randomness, the higher is the entropy. 
The more are the no. of possible orientation or arrangements, the greater will be the randomness and thus entropy. 

Mathematically,
$$dS = \frac{ q_{rev} }{ T }$$
Note that we cannot calculate entropy from irreversible heat.

And, we get,
$$\Delta S = \int_{1}^{2} \frac{ q_{rev} }{ T }$$

$\Delta S$ is change in state function and thus does not depend on path.
Thus, 
$$\Delta S = S_{2} - S_{1}$$

##### Comparison of Entropy
For same substance, comparison of molar entropy,
$$\ce{ Solid < Liquid < Gas }$$

For gas, 
$$S \propto n$$

If moles of gas are constant,
$$S \propto T\ (V = \text{const.})$$
$$S \propto V\ (T = \text{const.})$$
Thus, $S \propto T$ but $dS \propto 1 /T$

If $n,V,T$ are constant for gas,
$$\ce{ misture > pure }$$

If $n,V,T$ are the same, then for pure gas,
$$S \propto \ce{ Atomicity }$$
This for more complex molecule, entropy will be higher. 

If $n,V,T$ and atomicity are same, 
$$E \propto \ce{ Molar Mass }$$

For ionic solid,
$$S \propto \frac{1}{\ce{ lattice energy }}$$

For identical metal blocks,
$$S \propto T$$

Molar entropy of amorphous form is greater than that of crystalline form.

For chemical reaction,
- If $\Delta n_{g} = +ve, \Delta S_{r} = +ve$
- If $\Delta n_{g} = -ve, \Delta S_{r} = -ve$

### Second Law of Thermodynamics 
It deals with feasibility or spontaneity of a reaction under given conditions. It also addresses extent of reaction.

#### Statements of Second Law
**Statement 1: Kevin Plank Statement**
> *It is not possible for a heat engine working in a cyclic process whose sole effect is to convert heat into work completely.* 
> Heat cannot be completely converted into work in a cyclic process. 
> Note that work can be completely converted into heat.

![[Pasted image 20240315164325.png]]

**Statement 2:**
> *Entropy of the universe is continuously increasing.*
> $$or$$ 
> *Entropy of universe increases in a spontaneous (or irreversible) process, but remains constant in reversible process.* 

Mathematically,
- If, $\Delta S_{sys} + \Delta S_{sur} > 0$, then the process is spontaneous or irreversible. 
- If, $\Delta S_{sys} + \Delta S_{sur} = 0$, then the process is reversible. I.e. equilibrium state.
- If, $\Delta S_{sys} + \Delta S_{sur} < 0$, then the process is non-spontaneous or non occurring. 

These 3 statements are called *criteria of spontaneity.*

## [[04 Calculation of Entropy Change]]

## Third Law of Thermodynamics 
*For a perfectly crystalline substance, entropy approaches zero when temperature approaches absolute zero (o K).*

Thus,
$$S \text{ at 0 K} = 0$$
This is because there are no motions at absolute zero. 

### Application of Third Law 
#### Calculation of abs. entropy 
of a substance at any temp.

![[Entropy vs Temp.jpg]]

From, this graph we see that,
$$\Delta S_{vap} > \Delta S_{fus}$$

![[Pasted image 20240315170619.png]]

From this graph and third law, assuming that the substance is perfectly crystalline,
$$
\begin{split}
\Delta S &= S_{T} - S_{0} \\
S_{T} &= \Delta S_{AB} + \Delta S_{BC} + \Delta S_{CD} + \Delta S_{DE} + \Delta S_{EF} 
\end{split}
$$
Thus we get,
$$
\begin{split}
S_{T} &= \int_{0}^{T_{mp}} \frac{ nC_{V(s)}dT }{ T } + \frac{ \Delta H_{fus} }{ T_{mp} } + \int_{T_{mp}}^{T_{bp}} \frac{ nC_{V(l)}dT }{ T } + \frac{ \Delta H_{vap} }{ T_{bp} } + \int_{T_{bp}}^{T} \frac{ nC_{V(g)}dT }{ T } 
\end{split}
$$

#### To Calculate entropy change of reaction 
$$\ce{ aA + bB -> cC + dD }$$

Then,
$$
\begin{split}
\Delta S_{r} &= \sum S_{prod} - \sum S_{reac} \\
&= (cS_{C} + dS_{D}) - (aS_{A} + bS_{B} )
\end{split}
$$
where $S_{X}$ is molar entropy of X.
