Links: [[02 VdW's Equation of State]]
___
# Determination of Z in terms of a & b 
#important 
Determination of Compressibility Factor (Z) in terms of a and b with suitable approximations. 

### Low Pressure
Low P is considered when Z is decreasing. Intermediate is when it increases to 1. High P is when it is more than 1. 

At low P, molar volume of gas is considerably high. and hence $b$ can be ignored relative to $V_{m}$. Thus,
$$V_{m} - b \approx V_{m}$$

The equation then becomes,
$$
\begin{split}
\left( P + \frac{ a }{ V_{m}^{2} } \right)(V_{m}) &= RT \\
PV_{m} + \frac{ a }{ V_{m} } &= RT \\
\frac{PV_{m}}{RT} + \frac{a}{RTV_{m}} &= 1 \\
\\
Z &= 1 - \frac{ a }{ RTV_{m} }
\end{split}
$$

Thus compressibility factor,
$$Z = 1- \frac{ a }{ RTV_{m} }$$
For most gases this explains the variation of Z with P and experimentally matches with the low P region of the graph. 

### High Pressure
At high pressure, molar volume is less so we cannot ignore $b$. But $\displaystyle \frac{a}{V_{m}^{2}}$ can be ignored relative to the high P value.

$$P + \frac{ a }{ V_{m}^{2} } \approx P$$

The equation then becomes,
$$
\begin{split}
P(V_{m} - b) &= RT \\
PV_{m} - Pb &= RT \\
\frac{PV_{m}}{RT} - \frac{ Pb }{ RT } &= 1 \\
\\
Z &= 1 + \frac{ Pb }{ RT }
\end{split}
$$

Thus compressibility factor,
$$Z = 1 + \frac{ Pb }{ RT }$$

This is similar to $y = mx + c$ with slope being $\displaystyle \frac{ b }{ RT }$ and y intercept being $1$

As $Z \propto P$, the graph is linear which is in line with the experimental graph. 


**Note:** At very low pressure (or at very high molar volume), real gas behaves ideally, irrespectively of T. 
i.e. if $P \to 0$, $V_{m} \to 0$ then $Z \to 1$. 
In this case, $PV = nRT$ applies. 

### Low P and High T
At low P and high T conditions are called ideal gas conditions. 

At low P, $V_{m}$ is high and b can be ignored. 
At high T, thermal E is dominant over intermolecular forces and thus the a can be ignored. 

Thus, ideal gas equation, can be applied,
$$PV = nRT$$

### Special Cases
Special cases of $H_{2}$ and He gases. 

a for He and $H_{2}$ are extremely low (in fact, it is lowest for He), and therefore, $\displaystyle \frac{a}{V_{m}^{2}}$ term is ignored under normal T conditions.

Thus Van Der Waals equation becomes,
$$
\begin{split}
P(V_{m} - b) &= RT \\
PV_{m} - Pb &= RT \\
\frac{PV_{m}}{RT} - \frac{ Pb }{ RT } &= 1 \\
\\
Z &= 1 + \frac{ Pb }{ RT }
\end{split}
$$

He shows the closest behaviour to ideal gas. 

![[Pasted image 20230512210916.png]]

For $H_{2}$ and He, Z > 1 for all P. Thus there is +ve deviation from ideal gas.  

$H_{2}$ and He gases, Z vs P graph shows -ve deviation like other gases when T < Boyle's T, i.e. when $T < T_{b}$. Boyle's T is extremely low for He and $H_{2}$. It is lowest for He. 

![[Pasted image 20230512211410.png]]

### Examples
![[Pasted image 20230512212805.png]]
![[Pasted image 20230512213152.png]]
![[Pasted image 20230512213757.png]]

## Physical Significance of $a$ and $b$
#### Low pressure
$$Z = 1 - \frac{ a }{ V_{m}RT } = \frac{ V_{mr} }{ V_{mi} }$$
Thus,
$$\frac{ V_{mr} }{ V_{mi} } < 1 \implies V_{mr} < V_{mi}$$
thus volume occupied is less than ideal gas. 

We conclude that the attractive intermolecular forces are dominant over repulsive forces. Gas in this case (Z < 1, i.e. -ve deviation) is said to be more compressible than an ideal gas. Also, gas is easily liquified. 

**Note:** Ideal gas can never be liquified, this is because intermolecular forces are considered zero

*$a$ is the measure of attractive forces between gas molecules.* 

#### High Pressure
$$Z = 1 + \frac{ Pb }{ RT }$$
$$Z > 1$$
$$V_{mr} > V_{mi}$$

This means repulsive forces are dominant between gas molecules. And deviation is +ve from ideal behaviour. Also, gas is said to be less compressible than ideal gas. And gas is more difficult to liquify. 

*$b$ is the measure of finite size of the gas molecule and indirectly represents repulsive forces.*