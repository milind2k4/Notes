Links: [[00 Ionic Equilibrium]]
___
# Heterogeneous Equilibrium 
Sparingly soluble salts solution. The solubility is less than $10^{-2}$ M
Salts like AgCl, AgBr, AgI, $\ce{ PbCl_{2}, PbI_{2}, Ag_{2}CrO_{4}, BaSO_{4} }$ etc.

##### Solubility (s)
It is the molar concentration of a substance in solution at saturation point or saturation equilibrium at a given temp.. 
Its unit is mol/lit. 

In general, on increasing temp. solubility increases  as dissolution of most salts in water is endothermic.

Solubility of a sparingly soluble salt increases heavily due to complex formation [[00 Ionic Equilibrium#Complexation Equilibrium]]. It decreases due to common ion effect.  

#### Solubility Product
When a sparingly soluble salt is dissolved in water, there exists an equilibrium between solid salt and aqueous ions. 

$$\ce{ AB {}_{(s)} <=> A+ {}_{(aq)} + B- {}_{(aq)} }$$
This has dissociation constant at equilibrium,
$$
\begin{split}
\ce{ 
k_{diss} &= \frac{ [A+] [B-] }{ [AB {}_{(s)}] } \\
k_{diss} \times [AB {}_{(s)}] &= [A+] [B-] \\
k_{sp} &= [A+] [B-]
 }
\end{split}
$$
Where sp stands for **Solubility Product.** And since this is an equilibrium constant, it does not depend on concentration but does on temp. 

Thus solubility product means the product of concentration of ions in aqueous phase at equilibrium. Thus for a salt $\ce{ A_{x}B_{y} }$ 
$$\ce{ k_{sp} = [A^{y+}]^{ x}\times [B^{x-}]^{y} }$$

#### Solubility of sparingly soluble salt in pure water
Since there is pure water, there is no interference.

$$\ce{ AB {}_{(s)} <=> A+ {}_{(aq)} + B- {}_{(aq)}, k_{sp} = [A+][B-] }$$

Sparingly soluble salts are treated as strong electrolytes because the small amount which is dissolved is 100% dissociated. 

The ions are in equilibrium with the solid undissociated salt. 

Thus for 1:1 salt,
$$s = \sqrt{ k_{sp} }$$
![[Pasted image 20230713132156.png]]

For 2:1 salt,
$$s = \sqrt[3]{ \frac{k_{sp}}{4} }$$
![[Pasted image 20230713132214.png]]

For 1:3 salt, (here we use common ion effect)
![[Pasted image 20230713132307.png]]

For any general salt $\ce{ A_{x}B_{y} }$,
$$s = \left( \frac{ k_{sp} }{ x^{x}.y^{y} } \right)^{1/x+y}$$

![[Pasted image 20230713132448.png]]

#### Solubility in presence of common ionised 
Solubility of sparingly soluble salt decreases in presence of common ion. 
This is because the equilibrium is shifted in the backward direction, making more of the solid salt which is not very soluble. 

![[Pasted image 20230713132738.png]]

##### Examples
![[Pasted image 20230713133615.png]]

![[Pasted image 20230713134441.png]]

In some cases, if the salt is really really insoluble, we have to take the commo ion effect by water too, #important 
![[Pasted image 20230713134839.png]]

### Simultaneous Solubility
This arises when two of more sparingly soluble salts are present in same solution furnishing common ion. 

The solubility of all the salts found is called **Simultaneous Solubility.** This SS is less than the same if pure water is taken. 
![[Pasted image 20230713135357.png]]

Example,
![[Pasted image 20230713200623.png]]

## Applications of Solubility Product 
#### Simple Precipitation
$$\ce{ AB {}_{(s)} <=> A+ + B-, k_{sp} = [A+][B-] }$$

At any instant, a term called **ionic product** or **solubility quotient** is defined as,
$$Q_{ip} = \ce{ [A+]_{t} . [B-]_{t} }$$
t means at any time. 

Now if,
- $Q_{ip} < k_{sp}$: solution is unsaturated and more salt can be dissolved to reach saturation point.
- $Q_{ip} = k_{sp}$: solution is saturated and no more salt can be dissolved. 
- $Q_{ip} > k_{sp}$: solution is supersaturated (unstable solution) and precipitation will occur to reach saturation point i.e. $Q_{ip} = k_{sp}$.

Example,
![[Pasted image 20230713201855.png]]

#### Selective Precipitation
#important 

The one which has lower $k_{sp}$ will precipitate first. But this only happens when there is large difference in $k_{sp}$ values. If the $k_{sp}$ values are close to each other, all the ions will precipitate together. 

![[Pasted image 20230713203200.png]]

### Solubility of Salt in Interfering [[07 Buffer Solution]] 
The concentration of $\ce{ [H+] }$ and $\ce{ [OH-] }$ in buffer solution remains the same even after adding the salt. 

![[Pasted image 20230713204451.png]]

## Effect of Hydrolysis on Solubility 
If any ion undergoes [[06 Salt Hydrolysis|hydrolysis]] then solubility of salt increases. However this increase is not to the extent of [[00 Ionic Equilibrium#Complexation Equilibrium]].

![[Pasted image 20230713211850.png]]

Here we have,
$$s = \ce{ [A-]\left( 1 + \frac{ [H+] }{ [k_{a}] } \right) }$$

Let MA be a sparingly soluble salt with solubility s,
$$\ce{ MA {}_{(s)} <=> M+ + A-, k_{sp} = s \times [A-] }$$

Now, there will be hydrolysis of $\ce{ A- }$,
$$\ce{ A- + H_{2}O <=> HA + OH-, k_{h} = \frac{ k_{w} }{ k_{a(HA)} } = \frac{ [HA][OH-] }{ [A-] } }$$
In this hydrolysis almost all of $\ce{ A- }$ is consumed. 

Now, using POAC, we get,
$$
\begin{split}
\ce{ 
s &=  [A-] + [HA] \\
&= [A-] + \frac{ k_{w} [A-] }{ k_{a} [OH-] } \\
&= [A-]\left( 1 + \frac{ [H+] }{ k_{a} } \right)
 }
\end{split}
$$

Putting this into the expression of $k_{sp}$,
$$k_{sp} = s \times \frac{ s }{ 1 + \frac{ [H^{+}] }{ k_{a} } }$$
$$s = \sqrt{ k_{sp} \left( 1 + \frac{ \ce{ [H+] } }{ k_{a} } \right) }$$
which is more than $s = \sqrt{ k_{sp} }$ and thus the solubility is increased.

![[Pasted image 20230713213426.png]]

Example,
![[Pasted image 20230713213847.png]]