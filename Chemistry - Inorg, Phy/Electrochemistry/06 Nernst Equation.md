Links: [[01 Working of Galvanic Cell]], [[01  Law of Mass Action]]
___
# Nernst Equation
#important 

Effect of concentration/partial pressure on electrode/cell potential. 

Consider a cell reaction,
$$\ce{ aA + bB -> cC + dD }$$
At any instant,
$$\Delta G_{r} = \Delta G^{o}_{r} + 2.303RT \log_{10}Q $$
where Q is reaction quotient,
$$Q = \frac{ [C]^{c}[D]^{d} }{ [A]^{a}[B]^{b} }$$
and $G^{o}_{r}$ is std. Gibbs energy of reaction. 

Now, we know that,
$$\Delta G_{r} = -nFE_{cell}$$
$$\Delta G^{o}_{r} = -nFE^{o}_{cell}$$

Giving,
$$\ce{ E_{cell} = E^{o}_{cell} - \frac{ 2.303RT }{ nF } \log Q }$$
where,
$R \to$ Gas constant
$F \to$ Faraday constant
$n \to$ no. of electrons involved
$T \to$ temperature in K
$Q \to$ reaction quotient

If T = 298 K,
$$\ce{ E_{cell} = E^{o}_{cell} - \frac{ 0.0591 }{ n } \log Q }$$
If $E_{cell}$ is +ve, then we get electrical energy from the cell.

This is also applicable on half cell reactions. Thus, we can write simply,
$$\ce{ E = E^{o} - \frac{ 0.0591 }{ n } \log Q }$$

For high value of E, the numerator of Q should be less and denominator should be high.

For a cell reaction if gases are involved with substance in solution, then for gases take partial pressure and for substance in solution take molar concentration.

Q is $Q_{pc}$ for reaction involving gases and substances in solution phase. 

For example,
$$\ce{ Cl_{2} {}_{(g)} + 2e- -> 2Cl- {}_{(aq)}, Q = \frac{ [Cl-]^{2} }{ p_{Cl_{2}} } }$$
$$\ce{ Cl_{2} {}_{(g)} + H_{2} {}_{(g)} -> 2Cl- {}_{(aq)} + 2H+ {}_{(aq)}, Q = \frac{ [Cl-]^{2} [H+]^{2} }{ p_{Cl_{2}} p_{H_{2}} } }$$

### Applications of Nernst Equation 
1. To determine non standard Potential: 
	$$\ce{ E = E^{o} - \frac{ 0.059 }{ n } \log Q }$$

2. To calculate equilibrium constant of cell reaction,

	At equilibrium, $\Delta G = 0$ i.e. $E_{cell} = 0$ and $Q = k_{eq}$
	
	$$
	\begin{split}
	\ce{ 
	0 &=  E^{o}_{cell} - \frac{ 0.059 }{ n } \log k_{eq} \\
	E^{o}_{cell} &=  \frac{ 0.059 }{ n } \log k_{eq} \\
	k_{eq} &=  10^{nE^{o}/0.059} \\
	 }
	\end{split}
	$$
	
	Note that, at equilibrium $\Delta G$ is zero but $\Delta G^{o}$ need not be zero. 
	If equilibrium state exists at standard conditions, then $\Delta G^{o}$ is also zero and $k_{eq}$ becomes 1.

### Examples
Be careful in writing reaction quotient. 

![[Pasted image 20230725125402.png]]
![[Pasted image 20230725125412.png]]

![[Pasted image 20230725131103.png]]

![[Pasted image 20230725131734.png]]

[[05 pH Calculations]]
![[Pasted image 20230725132857.png]]

![[Pasted image 20230725133302.png]]

#important #revision 
![[Pasted image 20230725133822.png]]

![[Pasted image 20240221150548.png]]







