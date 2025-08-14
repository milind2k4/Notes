Links: [[03 Entropy]]
___
# Calculation of $\Delta S$
### Surrounding
Sine surrounding is very large, every process wrt surrounding is considered reversible irrespective of the process in the system. 

Due to size, T and P of surrounding is taken constant.

$$
\begin{split}
\Delta S_{sur} &= \int_{1}^{2} \frac{ q_{sur} }{ T_{sur} } \\
&= \frac{ Q_{sur} }{ T_{sur} } \\
&= \frac{ -Q_{sys} }{ T_{sur} } 
\end{split}
$$

$Q_{sys} = -Q_{sur}$ because the heat gained/lost by the system is coming from/going to the surrounding.

### System
For ideal gas undergoing any process,

$$
\begin{split}
\Delta S_{sys} &= \int_{1}^{2} \frac{ q_{rev} }{ T } \\
&= \int_{1}^{2} \frac{ dU - W_{rev} }{ T } \\
&= \int_{1}^{2} \frac{ nC_{V}dT - (-PdV) }{ T } \\
&= n \int_{1}^{2} \frac{ C_{V}dT }{ T } + nR \int_{1}^{2} \frac{ 1 }{ V } \, dV \\
\end{split}
$$

Thus, we get,
$$\Delta S_{sys} = n C_{V}\ln \frac{ T_{2} }{ T_{1} } + nR \ln \frac{ V_{2} }{ V_{1} }$$

If pressure is given,
$$
\begin{split}
\frac{ P_{1}V_{1} }{ T_{1} } &= \frac{ P_{2}V_{2} }{ T_{2} } \\
\frac{ V_{2} }{ V_{1} } &= \frac{ P_{1} }{ P_{2} } \frac{ T_{2} }{ T_{1} } 
\end{split}
$$
Thus,
$$
\begin{split}
\Delta S_{sys} &= nC_{V} \ln \frac{ T_{2} }{ T_{1} } + nR \ln \frac{ P_{1} }{ P_{2} } + nR \ln \frac{ T_{2} }{ T_{1} } \\
&= nC_{P} \ln \frac{ T_{2} }{ T_{1} } + nR \ln \frac{ P_{1} }{ P_{2} }
\end{split}
$$

This is valid for both reversible and irreversible process. 

##### Isothermal Process 
Since $T_{1} = T_{2}$, the first term will becomes zero.

$$\Delta S_{sys} = nR \ln \frac{ V_{2} }{ V_{1} } = nR \ln \frac{ P_{1} }{ P_{2} }$$

##### Isobaric Process 
Since $P_{1} = P_{2}$, the 2nd term from the 2nd formula vanishes. 

$$\Delta S_{sys} = nC_{P} \ln \frac{ T_{2} }{ T_{1} }$$

##### Isochoric Process
Since $V_{1} = V_{2}$, the 2nd term from the 1st formula becomes zero.

$$\Delta S_{sys} = nC_{V} \ln \frac{ T_{2} }{ T_{1} }$$


#### Adiabatic Process 
#important 

**Reversible,**
Since $q_{rev} = 0$,
$$\Delta S_{sur} = \Delta S_{sys} = \Delta S = 0$$

**Irreversible,**
Here $q_{irr} = 0$. 

Thus, 
$$\Delta S_{sur} = \frac{ -Q_{sys} }{ T } = 0$$

But, $\Delta S_{sys} \neq 0$. 

We know that, for irreversible process,
$$\Delta S_{sur} + \Delta S_{sys} > 0$$
Thus,
$$\Delta S_{sys} > 0$$

And the mathematical relation will be the same as normal.
$$\Delta S_{sys} = nC_{V}\ln \frac{ T_{2} }{ T_{1} } + nR\ln \frac{ V_{2} }{ V_{1} }$$


![[Pasted image 20240315164413.png]]
![[Pasted image 20240315164424.png]]

**Note:** Free expansion is an irreversible process.

#### For Solid or Liquid 
PdV term is ignored for solids and liquids because dV is very small.

$$
\begin{split}
\Delta S_{sys} &= \int_{1}^{2} \frac{ q_{rev} }{ T } \\
&= \int_{1}^{2} \frac{ dU - W }{ T } \\
&= \int_{1}^{2} \frac{ nCdT }{ T } \\
&= nC \ln \frac{ T_{2} }{ T_{1} }
\end{split}
$$

Also, for solids and liquids, 
$$C_{P} \approx C_{V} = C$$

##### Phase Change
T and P are constant in phase transformation. Phase change is reversible if occurring at mp or bp or in general, transition temp. at given P.

Transition temp. is the temp. at which phase change occurs at given pressure.

**Melting,**
$$\Delta S_{sys} = \Delta S_{fus} = \frac{ \Delta H_{fusion} }{ T_{mp} }$$

**Vaporisation,**
$$\Delta S_{sys} = \Delta S_{vap} = \frac{ \Delta H_{vap} } { T_{bp} }$$

**In general,**
$$\Delta S_\text{phase change} = \frac{ \Delta H_\text{phase change} }{ T_\text{transition temp.} }$$

![[Pasted image 20240315165001.png]]
