Links: [[00 Electrochemistry]], [[01 Working of Galvanic Cell]]
___
# IUPAC Representation of Galvanic Cell
Represent anode part to the left side and cathode part to the right side, both sides are separated by a double vertical line representing the presence of Salt Bridge. 
$$\ce{ \underbrace{ Zn {}_{(s)} | ZnSO_{4}  {}_{(aq)} }_{ anode } || \underbrace{ CuSO_{4}  {}_{(aq)} |  Cu {}_{(s)} }_{ cathode } }$$

Single vertical lines (|) represent the interface b/w 2 different phases in contact. Comma is used when 2 species in same phase are in contact.  

$$\ce{  Pt | Fe^{2+} {}_{(aq)}, Fe^{3+} {}_{(aq)} || Cu^{2+}(aq) | Cu(s) }$$
Cell reaction of this cell will be,

$$
\begin{split}
\ce{ 
2Fe^{2+} &-> 2Fe^{3+} + 2e- \\
Cu^{2+} + 2e- &-> Cu \\
\hline
2Fe^{2+} + Cu^{2+} &-> 2Fe^{3+} + Cu
}
\end{split}
$$

Electron carriers (Zn and Cu rods in Daniel Cell) must be represented at the extreme left and the extreme right.

In case of gas half cell (or gas electrode), gas should be represented just after electron carrier in anode part and just before electron carrier in cathode part.
$$\ce{ Pt | \underbrace{ H_{2} {}_{(g)} }_{  } | H+  {}_{(aq)} ||  Cl- {}_{(aq)} | \underbrace{ Cl_{2} {}_{(g)} }_{  } | Pt }$$

The Cell Reaction of which will be, #important 
$$
\begin{split}
\ce{ 
H_{2} &-> 2H+ + 2e- \\
Cl_{2} + 2e- &-> 2Cl- \\
\hline 
H_{2} + Cl_{2} &-> 2H+ + 2Cl-
}
\end{split}
$$
(note here that the first is not converted to the second)


Instead of concentration of $\ce{ H+ }$ ions, it may be written as pH. To find concentration,
$$\ce{ pH = -\log_{10}[H^{+}] }$$

In cell reaction questions, sometimes we will have to balance redox reactions individually first,
![[Pasted image 20230724214151.png]]

Also, we cannot cancel any species like in a normal reaction as the anode and cathode parts are separated. 
![[Pasted image 20240219213252.png]]

## Electrochemical Series
When EP of various half cells are measured under standard condition relative to SHE and arranged in increasing order to form **Electrochemical Series.**

This ECS is also called activity series. 

s-block elements are on top, then 3d series, then Hydrogen, having zero SRP then inert metals like gold and platinum. The minimum is of $\ce{ Li+ }$ and the highest is of $\ce{ F_{2} }$. 

The one having more -ve SRP undergoes oxidation. This is because its SOP will be highly +ve and the $\Delta G$ of oxidisation reaction will be highly -ve.

The one having more -ve SRP is not spontaneous. The one having more +ve SOP is spontaneous. 

![[Electrochemical-Series.png]]

The more complete list,
![[electrochemical-series 1.png]]

We do not need to memorise the EP data. We only need to memorise the positions relative to SHE. 

### Application
1. Metals with high SOP or low SRP are powerful RA. Li is most powerful RA. 
	As we move down the series, the reducing power decreases,
	$$\ce{ Li > K > Na > Mg > Al > Zn > Fe \dots }$$
	
2. Higher is the SRP, greater is the oxidising power. $\ce{ F_{2} }$ is the most powerful OA in periodic table. 
	As we move up the series, the oxidising power decreases,
   $$\ce{ F_{2} > MnO_{4}- > Au^{2+} > Ag+ > Cu^{2+} \dots }$$
   
2. Metals above H are active metals and displace H from dilute acid, i.e. reduce the H. Metals below H are inactive.
	$$\ce{ Li, Na, K, Al, Zn, Pb, Sn, Fe etc ->[dil HCl] H_{2} ^ }$$

	$$\ce{ Cu, Ag, Au, Pt ->[dil HCl] NR }$$

3. Very Highly active metals evolve Hydrogen gas from even cold water. Less active metals evolve hydrogen gas from steam. Inactive metals do not react with even steam.

	$$
	\begin{split}
	\ce{ 
	Li, Na, K, Ca, Ba + H_{2}O {}_{(l)} &-> H_{2} {}_{(g)} \\ 
	Fe, Sn, Ni, Al + H_{2}O {}_{(steam)} &-> H_{2} {}_{(g)} \\
	Cu, Ag, Au, Pt, Hg + H_{2}O {}_{(steam)} &-> NR
	 }
	\end{split}
	$$ 

3. More active metal displaces less active metal from it's salt solution. This is the basis for Daniel Cell.
	$$
	\begin{split}
	\ce{ CuSO_{4} {}_{(aq)} + Zn {}_{(s)} &-> ZnSO_{4} {}_{(aq)} + Cu {}_{(s)} \\ 
	ZnSO_{4} {}_{(aq)} + Cu {}_{(s)} &-> NR }
	\end{split}
	$$
	
	![[Pasted image 20230724221926.png]]

4. As activity of metal decreases, thermal stability of it's oxides also decreases. 
   $$\ce{ MgO, CaO, Al_{2}O_{3}, SiO_{2} ->[\Delta] NR }$$
   $$\ce{ Ag_{2}O {}_{(s)} ->[\Delta] Ag {}_{(s)} + O_{2} ^ }$$
   $$\ce{ HgO {}_{(s)} ->[\Delta] Hg {}_{(l)} + O_{2} ^ }$$

Note: For +ve value of $E_{cell}$, choose cathode (reduction) whose SRP (or RP) is high and anode (oxidation)  whose SRP is low. 

![[Pasted image 20230725122418.png]]
