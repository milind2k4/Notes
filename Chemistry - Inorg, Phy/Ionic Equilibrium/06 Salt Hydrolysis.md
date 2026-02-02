Links: [[14 Hydrolysis]]
___
# Salt Hydrolysis
Reaction of salt with water. It is the reverse process of Acid Base Neutralisation. Since ABN is exothermic, thus hydrolysis is endothermic. 

$$\ce{ \underset{ salt }{ B+A- } + H_{2}O -> \underset{ acid }{ HA } + \underset{ base }{ BOH }, \Delta H = -ve }$$

E.g.
$$\ce{ NH_{4}+CN- + H_{2}O -> NH_{4}OH + HCN }$$
or,
$$\ce{ NH_{4}+ + H_{2}O -> NH_{4}OH + H+ }$$
$$\ce{ CN- + H_{2}O -> OH- + HCN }$$

Thus salt hydrolysis means the hydrolysis of cation and anion. 

Anion $\to$ Acid $\to$ Solution becomes Basic 
Cation $\to$ Base $\to$ Solution becomes Acidic

### Salt of SA and SB
Strong Acid and Strong Base

Salts like $\ce{ NaCl, KBr, Ba(NO_{3})2, BaCl_{2} etc. }$

$$\ce{ NaCl + H_{2}O <=> NaOH + HCl }$$
Here $k_{eq}$ is very small.

Since NaCl remains in broken form in water, its ions are spectator ions. 
$$\ce{ Na+ + Cl- + H_{2}O <=> Na+ + OH- + H+ + Cl- }$$
$$\ce{ H_{2}O <=> OH- + H+ }$$
Here, $k_{a} = 1.8 \times 10^{-16}$ is such a small value that reaction proceeds negligibly in the forward direction. 

*Salt of Strong Acid and Strong Base do no undergo hydrolysis.*

That is, Cation of SB and Anion of SA do no undergo hydrolysis. #important 
Cations like $\ce{ Na+, K+, Rb+, Cs+, Ba^{2+}, Sr^{2+} etc. }$.
Anions like $\ce{ Cl-, Br-, I-, ClO_{4}-, ClO_{3}-, NO_{3}- etc. }$. 
Note than HF in water is weak acid. 

#### pH
The pH of such salt of SA and SB is 7 at 25$^{\circ}$C.

### Salt of WA and SB
Like $\ce{ CH_{2}COONa, HCOOK, NaCN, NaOCN etc. }$

Only Anion will undergo hydrolysis. 

$$\ce{ A- <=> HA + OH- }$$
where A is the anion of WA. 

Since $\ce{ OH- }$ is generated, such salt solution is basic. 

We define a term called **Hydrolysis Constant,**
$$
\begin{split}
k_{h} &= \ce{ \frac{ [HA] [OH-] }{ [A-] } } \\
k_{h} &= \ce{ \frac{ [HA] [OH-] [H+] }{ [A-] [H+] } } \\
k_{h} &= \frac{ k_{w} }{ k_{a\text{(HA)}} }
\end{split}
$$

Thus the lower is $k_{a}$ the higher is $k_{h}$ and thus the extent of hydrolysis of anion is more. That is, *weaker is the acid, greater will be is anion hydrolysis.*

Now,
![[Pasted image 20230627203800.png]]
here h is *degree of hydrolysis* which is the same as degree of dissociation.

We can write,
$$k_{h} = \frac{ ch^{2} }{ (1-h) }$$

Now, if $k_{h}$ is small, and c is high, such that $h \leq 0.1$ then $h \ll 1$,
$$k_{h} = ch^{2}$$
$$h = \sqrt{ \frac{ k_{h} }{ c } } = \sqrt{ \frac{ k_{w} }{ k_{a} \times c } }$$
Which is the same approximation as [[05.5 Weak Monobasic Acid]]

#### pH
pH can be given as,
$$
\begin{split}
\ce{ 
[OH-] &= ch \\
[OH-] &= c \sqrt{ \frac{ k_{h} }{ c } } \\
[OH-] &= \sqrt{ \frac{ k_{w} }{ k_{a} } \times c } \\
}
\end{split}
$$

And, thus,
$$
\begin{split}
\ce{ 
[H+] &= \frac{ k_{w} }{ \sqrt{ \frac{ k_{w} }{ k_{a} } \times c } } \\
[H+] &= \sqrt{ \frac{ k_{w} \times k_{a} }{ c } } \\
pH &= 1/2 (pk_{w} + pk_{a} + \log c) 
}
\end{split}
$$
(remember this)

This is only available when $h \leq 0.1$. Otherwise we have to solve quadratic.

### Salt of SA and WB
Like $\ce{ NH_{4}Cl, C_{6}H_{5}NH_{3}Br etc. }$

Only the cation undergoes hydrolysis.

$$\ce{ B+ + H_{2}O <=> BOH + H+ }$$
where B is the cation of WB.

Since $\ce{ H+ }$ is being generated, the final solution becomes acidic. 

$$k_{h} = \frac{ k_{w} }{ k_{b\ce{ (BOH) }} }$$
thus, the weaker the base, the more is the hydrolysis. 

Now,
![[Pasted image 20230627210847.png]]

And using the same approximations as the case above i.e. $h \leq 0.1$, we get,
$$h = \sqrt{ \frac{ k_{h} }{ c } } = \sqrt{ \frac{ k_{w} }{ k_{b} \times c } }$$

#### pH
Similarly to previous case, we get pH,
$$\ce{ [H+] = \sqrt{ \frac{ k_{w} \times c }{ k_{b} } } }$$

$$\ce{ pH = \frac{1}{2} (pk_{w} - pk_{b} - \log c) }$$

### [[06.1 Salt of WA and WB]]

### [[06.2 Salts having Polyvalent ion]]
### Salts containing Amphiprotic Anion
Salts like $\ce{ NaHCO_{3}, NaH_{2}PO_{4}, Na_{2}HPO_{4} etc. }$

Amphiprotic anion has at least one acidic H.

![[Pasted image 20230629200704.png]]
($k_{a_{2}}$ of $\ce{ H_{2}CO_{3} }$)

$$k_{h} = \ce{ \frac{ [H_{2}CO_{3}] [OH-] }{ [HCO_{3}-] } \frac{ [H+] }{ [H+] } } = \frac{ k_{w} }{ k_{a_{1}} }$$

Since here both $\ce{ H+, OH- }$ are formed, both the reactions are pulled forward and the pH does not depend on the concentration. 

Extent of both the reactions 1 and 2 can be taken nearly equal. Thus we can take 
$$\ce{ [H_{2}CO_{3}] \approx [CO_{3}^{2-}] }$$

Now dividing $k_{a_{2}}$ by $k_{h}$,
$$
\begin{split}
\ce{ 
\frac{ k_{a_{2}} }{ k_{h} } &= \frac{ k_{a_{2}} }{ k_{w}/k_{a_{1}} } \\
\\
&= \frac{ \displaystyle \frac{ [H+] [CO_{3}^{2-}] }{ [HCO_{3}-] } }{ \displaystyle \frac{ [H_{2}CO_{3}] [OH-] }{ [HCO_{3}-] } } \\
\frac{ k_{a_{1}} k_{a_{2}} }{ k_{w} } &= \frac{ [H+] [CO_{3}^{2-}] }{ [H_{2}CO_{3}] \frac{k_{w}}{[H+] } } \\
\text{Now, since } [CO_{3}^{2-}] \approx [H_{2}CO_{3}], \\
\frac{ k_{a_{1}} k_{a_{2}} }{ k_{w} } &= \frac{ [H+]^{2} }{ k_{w} } \\
k_{a_{1}} k_{a_{2}} &= [H+]^{2} \\
[H+] &= \sqrt{ k_{a_{1}} \times k_{a_{2}} }
}
\end{split}
$$

Thus pH will be,
$$\ce{ pH = 1/2(pk_{a_{1}} + pk_{a_{2}}) }$$
which is independent of concentration. 

Also, taking concentration,
![[Pasted image 20230704191829.png]]

##### For other Ions
pH:
$$
\begin{split}
\ce{ 
H_{3}PO_{4}: pH &= \frac{ 1 }{ 2 } (pk_{a_{1}} - \log c), when \alpha_{1} \leq 0.1 \\
NaH_{2}PO_{4}: pH &= \frac{ 1 }{ 2 }(pk_{a_{1}} + pk_{a_{2}}) \\
Na_{2}HPO_{4}: pH &= \frac{1}{2}(pk_{a_{2}} + pk_{a_{3}}) \\
Na_{3}PO_{4}: pH &= \frac{1}{2}(pk_{w} + pk_{a_{3}} + \log c)
 }
\end{split}
$$

Example,
![[Pasted image 20230704192357.png]]
