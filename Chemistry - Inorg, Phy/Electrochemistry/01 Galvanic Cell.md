Links: 
___
# Galvanic Cell
### Electrode Potential
When a metal rod is dipped into it's own ion solution there occurs either oxidation or reduction due to which a potential difference exists b/w electrode (metal rod) and solution on interface (on surface of metal), called **Electrode Potential.**
$$or$$
Electrode potential is the tendency to lose or gain electrons when an electrode is dipped into it's own ion solution.

Also as e cannot exist freely in solution, they go into the metal rod.

![[Pasted image 20230721215347.png]]

**NOTE:** Absolute value of electrode potential can't be determined. Rather relative potential of various half cells are measured w.r.t a reference electrode, called **Standard Hydrogen Electrode (SHE)** where std. EP (both red. and oxi.) at all temp. is assigned 0.

For SHE, 
$$\ce{ E^{\circ}_{\text{oxi}} = 0, E^{\circ}_{\text{red}} = 0 }$$
at all temperature. 

- EP (aka Cell Potential or Cell EMF (electromotive force)) is an [intensive property](https://en.wikipedia.org/wiki/Intensive_and_extensive_properties) i.e. it does not depend on the amount of matter. 

Also, writing a reaction in reverse changes the sign of SRP i.e. EP,
![[Pasted image 20230724220346.png]]

### Electrical Work obtained from a Galvanic Cell
$\Delta G$ is the electrical work that can be obtained from a system (non PV work).

$$\ce{ \Delta G = -q\times V = -nFE }$$

where 
$F \to$ *Faraday's Constant,* $(F = 96,500)$  (charge present on 1 mol of electrons)
$n \to$ no. of moles of electrons involved 
$E \to$ electrode potential or cell potential
$\Delta G \to$ change in Gibbs free E

Half cell potential are tabulated usually at 25 $^\circ$C in a series called Electrochemical Series (ECS).

-ve sign is used because this electrical work is obtained from the system. 

From here we get,
$$E = -\frac{ \Delta G }{ nF }$$
Here, $\Delta G$ is extensive property and n is the number of moles. 
Thus E becomes intensive property. 
As whenever we divide an extensive property by number of moles, it becomes intensive. 

##### Efficiency of Galvanic Cell
$$\eta = \frac{|\Delta G|}{|\Delta H|} \times 100
\implies \frac{\text{Electrical Work}}{\text{Heat Released}} \times 100$$


### [[01 Working of Galvanic Cell]]

## Thermodynamic Parameters for Cell Reaction 
Calculation of $\Delta G, \Delta H, \Delta S$.

Consider the cell reaction,
$$\ce{ A + B^{2+} -> A^{2+} + B }$$

Then,
$$\Delta G = -nFE_{cell}$$

Now, we know that,
$$
\begin{split}
\Delta G &= \Delta H - T\Delta S \\
\frac{ d }{ dT }(\Delta G) &= \frac{ d }{ dT }(\Delta H - T\Delta S)
\end{split}
$$
Here we take $\Delta H, \Delta S$ to be independent of temp. and thus,
$$
\begin{split}
-nF \frac{ dE_{cell} }{ dT } &= 0 - \Delta S \\
nF \frac{ dE_{cell} }{ dT } &= \Delta S \\
\end{split}
$$
where $\displaystyle \frac{ dE_{cell} }{ dT }$ is called **Temperature coefficient of Cell EMF.** It has unit V/K or V/$^{\circ}$C. 

And we get, $\Delta H$,
$$\Delta H = -nFE_{cell} + nFT \frac{ dE_{cell} }{ dT }$$

## Misc. Examples
In some questions we have to use two reactions to find the EP of another. This can be done using $\Delta G$,
![[Pasted image 20230724214609.png]]

![[Pasted image 20230725200758.png]]

