Links: [[00 KTG & Thermodynamics]]
___
# Thermodynamics 
Ideal gas law,
$$PV = nRT$$

Universal gas constant,
$$R = 8.314 = \frac{ 25 }{ 3 }\ \ce{ mol^{-1} K^{-1} }$$

Work Done by Gas,
$$W = \int P \, dV$$

#### Maxwell Boltzmann Dist.
Average speed,
$$v_{avg} = \sqrt{ \frac{ 8RT }{ \pi M } }$$

RMS speed,
$$v_{rms} = \sqrt{ \frac{ 3RT }{ M } }$$

Most probable speed,
$$v_{mp} = \sqrt{ \frac{ 2RT }{ M } }$$

#### Degree of Freedom
Monoatomic, $f = 3$.

Diatomic, $f = 5$ 

Polyatomic, $f = 6$

#### Internal energy of gas 
Each DOF has equal energy.

For 1 molecule,
$$E = \frac{ f }{ 2 }kT$$

For 1 mole,
$$E = \frac{ f }{ 2 }RT$$

For n moles,
$$E = \frac{ f }{ 2 }nRT$$

Using molar heat capacity,
$$\Delta U = nC_{V}dT$$

First Law of thermodynamics,
$$\Delta Q = \Delta U + W$$

#### Processes
**Isochoric,**
$$
\begin{split}
W &= 0 \\
\Delta U &= \frac{ f }{ 2 }V(\Delta P) \\
&= \Delta Q
\end{split}
$$

**Isobaric,**
$$
\begin{split}
W &= nR\Delta T \\
\Delta U &= \frac{ f }{ 2 }P\Delta V \\
\Delta Q &= \frac{ f }{ 2 }P\Delta V + P\Delta V 
\end{split}
$$

**Isothermal,**
$$
\begin{split}
nRT &= \text{const.} \\
PV &= \text{const.} \\
W &= nRT \ln \frac{ V_{f} }{ V_{i} } \\
&= nRT \ln \frac{ P_{i} }{ P_{f} } \\
\Delta U &= 0 \\
\Delta Q &= W 
\end{split}
$$

**Adiabatic,**
$$
\begin{split}
\frac{ P_{i}V_{i} }{ T_{i} } &= \frac{ P_{f}V_{f} }{ T_{f} } \\
\\
PV^{\upgamma} &= c \\
TV^{\upgamma-1} &= c \\
P^{1-\upgamma}T^{\upgamma} &= c \\
\\
W &= \frac{ nR\Delta T }{ 1 - \upgamma } \\
&= \frac{ \Delta (PV) }{ 1 - \upgamma } \\
\end{split}
$$

#### Molar Heat Capacity 
Molar heat capacity,
$$C = \frac{ \Delta Q }{ n\Delta T }$$

Specific heat capacity,
$$S = \frac{ \Delta Q }{ m\Delta T }$$

In isochoric process,
$$C_{V} = \frac{ f }{ 2 }R = \frac{ R }{ \upgamma - 1 }$$

In isobaric process,
$$C_{P} = \frac{ f }{ 2 }R + R = \frac{ \upgamma R }{ \upgamma - 1 }$$

Ratio of specific heats,
$$\upgamma = 1 + \frac{ 2 }{ f }$$


