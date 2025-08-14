Links: [[00 Electrochemistry]]
___
# Working of Galvanic Cell
### Daniel Cell
It is a combination of Zn and Cu half cell. 

Here the direction of current is opposite to that of e, i.e. opposite to that show here.

![[galvanic cell b_w.jpg]]

Cathode is where reduction occurs, and anode is where oxidation occurs. 

$$
\begin{split}
\ce{Zn & -> Zn^{+2}(aq) + 2e^{-} &, E_{oxid}}\\
\ce{Cu^{2+}(aq) + 2e^{-} & -> Cu(s) &, E_{redu}}
\end{split}
$$

But this is not a sustainable process, as more and more $\ce{ Zn^{2+} }$ ions will accumulate, making the $\ce{ ZnSO_{4} }$ solution positive, this is called  [[02 LJP and Salt Bridge|Liquid Junction Potential]] which stops fresh $\ce{ Zn^{2+} }$ from coming into the solution.

Similarly, $e^{-}$ will accumulate in the $\ce{ CuSO_4 }$ solution, the solution will become negative and stop accepting electrons.

To counter this, Salt Bridge is used.

##### Types of Electrodes
There are 2 types of Electrodes (e carriers),
1. **Inert:** Those which do not participate in reaction
	   - E.g. Pt, Pd, graphite etc.
2. **Active:** Those which participate in reaction.
	- E.g. Zn, Cu, Ag etc.

### Finding $E_{cell}$
$$
\begin{split}
\ce{ Zn &-> Zn^{2+}{}_{(aq)} + 2e^{-} &,\Delta G_{1} = -2FE_{oxi} \\
Cu^{2+} {}_{(aq)} + 2e^{-} &-> Cu {}_{(s)} &,\Delta G_{2} = -2FE_{red} \\
\hline 
Zn {}_{(s)} + Cu^{2+} {}_{(aq)} &-> Zn^{2+} {}_{(aq)} + Cu {}_{(s)} &, \Delta G_{3} = -2FE_{cell} }
\end{split}
$$
The last reaction is called *cell reaction* and has no electrons.
Also, the number of e involved in either oxidation half, reduction half or the cell reaction are equal and is the number of e, n. 

Now we know  that extensive properties are added when two reactions are added. Thus giving,
$$
\begin{split}
\ce{ \Delta G_{3} &= \Delta G_{1} + \Delta G_{2} \\
-2FE_{cell} &= -2FE_{oxi} + -2FE_{red} \\
E_{cell} &= E_{oxi} + E_{red} }
\end{split}
$$

Also,
$$\ce{ n_{3}E_{3} = n_{1}E^{o}1 + n_{2}E^{o}2 }$$
where $n_{1},n_{2},n_{3}$ represent the number of e involved.

Now, if the e are not cancelled,
$$
\begin{split}
\ce{ 
A &-> A+ + e- &, E_{1}\\
B^{2+} + 2e- &-> B &, E_{2} \\
\hline
A + B^{2+} + e- &-> A^{2+} + B &, E_{3}
 }
\end{split}
$$
Here since e are not cancelled, $E_{3} \neq E_{1} + E_{2}$. 
And this reaction is another Half Cell reaction. 

We can however, find $E_{3}$, using $\Delta G$,
$$
\begin{split}
\Delta G_{3} &= \Delta G_{1} + \Delta G_{2} \\
-1 FE_{3} &= -1 FE_{1} - 2 FE_{3} \\
E_{3} &= E_{1} + 2E_{2} 
\end{split}
$$

For spontaneous working of Galvanic Cell, $\ce{ E_{cell} }$ should be +ve so that $\ce{ \Delta G_{cell} }$ is -ve.
$\Delta G$ is the electrical energy obtained from the system. 
And cell will not deliver any electrical work if $E_{cell}$ is zero or -ve.

#### Dependence of EP
Electrode Potential depends on:
1. Temperature
2. Conc. of Solution or partial pressure of gases involved (active masses)
3. Nature of electrode used

Electrode Potential or Cell Potential are intensive properties and don't depend on:
1. Amount of Solution.
2. Thickness or shape of metal electrode (rod/plate/wire etc), as active mass of solids is constant. 
3. Stoichiometry variation of a given cell reaction. 

	$$
	\begin{split}
	\ce{ 
	A^{2+} + 2e^{-} &-> A(s), E = x volt &, \Delta G = 2y KJ/mol \\
	2A^{2+} + 4e^{-} &-> 2A(s), E = x volt &, \Delta G = 4y KJ/mol \\
	}
	\end{split}
	$$
   - $\Delta G$ is doubled
   - $-n$ is doubled
   - $E$ remains same

##### Under Standard Conditions
- Gases involved are ideal and their pressure is 1 bar. 
- Conc. of solution phase species is 1 molar.
- Solids and Liquids are pure and at 1 bar pressure.
- T is not the part of std conditions, however, the SRP (std reduction potential or std electrode potential) is tabulated at 25 $^\circ$C (ambient T).

If cell is working under standard conditions, cell potential is referred as *standard cell potential,* represented by $\ce{ E^{\circ}_{cell} }$.


### Description of Galvanic Cell

| Criteria                | Anode     | Cathode   |
| ----------------------- | --------- | --------- |
| Reaction                | Oxidation | Reduction |
| Sign                    | -ve       | +ve       |
| Direction of $e^-$ flow | out       | in        |

LOAN: Left Oxidation Anode Negative

**In Daniel Cell with time,**
- mass of $\ce{ Zn }$ rod decreases
- conc. $\ce{ Zn^2+ }$ ions increases
- mass of $\ce{ Cu }$ rod increases
- conc. $\ce{ Cu^2+ }$ ions decreases

