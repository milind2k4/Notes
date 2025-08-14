Links: [[01 Working of Galvanic Cell]], [[03 IUPAC Rep. of Cell and ECS]]
___
# Types of Half Cells
Any half cell in general can act as either cathode or anode. It depends on the accompanying half cell.

##### Metal-Metal ion
Metal rod is dipped in it's own solution. 

If it acts *as anode,*
$$\ce{ Zn -> Zn^{2+} + 2e- : Zn | Zn^{2+} }$$

If it acts *as cathode,*
$$\ce{ Zn^{2+} + 2e- -> Zn : Zn^{2+} | Zn }$$

##### Redox
An element is present in 2 different oxidation states in solution. 
Pt wire acts as e carrier. 

*At anode,*
$$\ce{ Pt(s) | Fe^{2+},Fe^{3+} }$$
*At cathode,*
$$\ce{  H+, MnO_{4}-, Mn^{2+} | Pt(s)}$$
undergoing reaction, 
$$\ce{ Mn^{2+} + 4H_{2}O -> MnO_{4}- + 8H+ + 5e- }$$

![[Pasted image 20230725202325.png]]

##### Gas
Consists of a gas adsorbed on a metal plate or foil coated with Pt black (powdered platinum for greater surface area and thus better adsorption) and the setup is dipped into an aqueous solution containing ion of gas. 

Adsorption of gas on foil is called *Occlusion*

*At anode,*
$$\ce{ Pt | H_{2}(g) | H+(aq) }$$
*At cathode,* 
$$\ce{ H+(aq) | H_{2}(g) | Pt }$$
Both of these will have zero EP. (SHE)

![[Pasted image 20230725203108.png]]

#### Concentration Cells
A cell in which both the cathode and anode parts are made of the same material. Current flows in the outer circuit due to difference in active mass of constituents in anode and cathode part. 

$E^{o}_{cell}$ is always zero for a concentration cell since at std. conditions if E of oxidation half is x, that of reduction half will be -x. 

$$\ce{ Pt(s) | \underset{ p_{1} }{ H_{2}(g) } | \underset{ C_{1} }{ H+(aq) } || \underset{ C_{2} }{ H+(aq) } | \underset{ p_{2} }{ H_{2}(g) } | Pt(s) }$$

The cell reaction being,
$$
\begin{split}
\ce{ 
H_{2}_{(g)} (p_{2}) &-> 2H+_{(aq)}(C_{1}) + 2e- \\
2H+_{(aq)} (C_{2}) + 2e- &-> H_{2}_{(g)}(p_{2}) \\
\hline 
H_{2}_{(g)}(p_{1}) + 2H+_{(aq)}(C_{2}) &-> H_{2}_{(g)}(p_{2}) + 2H+_{(aq)}(C_{2})
 }
\end{split}
$$

For $E_{cell}$,
$$
\begin{split}
E_{cell} &= E^{o}_{cell} - \frac{ 0.059 }{ n } \log Q \\
E_{cell} &= - \frac{ 0.059 }{ 2 } \log \frac{ p_{2}C_{1}^{2} }{ p_{1}C_{2}^{2} } \\
E_{cell} &= \frac{ 0.059 }{ 2 } \log \frac{ p_{1}C_{2}^{2} }{ p_{2}C_{1}^{2} }
\end{split}
$$
For spontaneity, 

$$
\begin{split}
\frac{ p_{1}C_{2}^{2} }{ p_{2}C_{1}^{2} } &> 1 \\
p_{1}C_{2}^{2} &> p_{2}C_{1}^{2}
\end{split}
$$

If $p_{1} =  p_{2}$, for spontaneity, $C_{2} > C_{1}$

If $C_{1} =  C_{2}$, for spontaneity, $p_{1} > p_{2}$

![[Pasted image 20240221153143.png]]
![[Pasted image 20230725200520.png]]

### [[07.5 M-M insol. Salt anion]]

#### Calomel Half Cell or Calomel Electrode
It is a metal metal insoluble salt anion half cell. 

Calomel is $\ce{ Hg_{2}Cl_{2} }$ (mercurous chloride) which is a water insoluble white solid. 

$$\ce{ Hg_{2}Cl_{2} -> Hg_{2}^{2+} + 2Cl- }$$
$$\ce{ [Hg_{2}^{2+}] [Cl-]^{2} = k_{sp} }$$
$\ce{ Hg_{2}^{2+} }$ is a diamagnetic ion.

Here solution of KCl is always in contact with excess of $\ce{ Hg_{2}Cl_{2} }$ and  thus its solubility product is always satisfied.

![[Pasted image 20230725214541.png]]

If it acts *as cathode* (reduction),
$$\ce{ Hg_{2}Cl_{2} + 2e- -> 2Hg {}_{(l)} + 2Cl- : Cl^{-}|Hg_{2}Cl_{2}|Hg {}_{(l)}|Pt }$$

If it acts *as anode* (oxidation),
$$\ce{ 2Hg {}_{(l)} + 2Cl- -> Hg_{2}Cl_{2} + 2e- : Pt|Hg {}_{(l)}|Hg_{2}Cl_{2}|Cl- }$$

**Standard (normal) Calomel Electrode (NCE or SCE):** when $\ce{ [KCl] = 1 M }$
**Saturated Calomel Electrode:** when KCl solution is saturated with KCl.

In both the conditions, KCl solution is always saturated w.r.t $\ce{ Hg_{2}Cl_{2} }$.
