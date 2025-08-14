Links: [[00 KTG & Thermodynamics]]
___
# Molar Heat Capacity
It is the heat given to change temp. of 1 mole gas by 1 unit. 

$$C = \frac{ \Delta Q }{ n\Delta T }$$
Its unit is $\ce{ J mol^{-1}K^{-1} }$.

Since $\Delta Q$ is different for each process, C depends on the type of process. 

 We also define Specific Heat,
$$S = \frac{ \Delta Q }{ m\Delta T }$$
Its unit is $\ce{ J kg^{-1}K^{-1} }$

##### Isothermal Process 
Since $dT = 0$, C for isothermal process is not defined. 

However, it is written as $\infty$ in many places. 

##### Adiabatic Process 
Since $dQ = 0$, C for isothermal process is zero. 

##### Polytrophic Process
Molar Heat Capacity,
$$
\begin{split}
C &= \frac{ \Delta U + W }{ n\Delta T }\\ 
&= \frac{ \frac{f}{2}nR\Delta T + \frac{ nR\Delta T }{ 1-a } }{ n\Delta T } \\
&= \frac{f}{2}R + \frac{ R }{ 1-a } \\
&= C_{V} + \frac{ R }{ 1-a }
\end{split}
$$

#### Isochoric Process 
$$
\begin{split}
C_{V} &= \frac{ \Delta Q }{ n\Delta T } \\
&= \frac{ \Delta U + \cancelto{ 0 }{ W } }{ n\Delta T } \\
&= \frac{ \frac{f}{2}nR\Delta T }{ n\Delta T } \\
&= \frac{ f }{ 2 }R
\end{split}
$$

Thus,
$$
\begin{split}
\text{Monoatomic} &: C_{V} = \frac{3}{2}R \\
\\
\text{Diatomic} &: C_{V} = \frac{5}{2}R \\
\\
\text{Polyatomic} &: C_{V} = \frac{6}{2}R 
\end{split}
$$

And we can write, change in internal energy,
$$\Delta U = \frac{ f }{ 2 }nR\Delta T = nC_{V}\Delta T$$

#### Isobaric Process
$$
\begin{split}
C_{P} &= \frac{ \Delta Q }{ n\Delta T } \\
&= \frac{ \Delta U + W }{ n\Delta T } \\
&= \frac{ \frac{ f }{ 2 }nR\Delta T + nR\Delta T }{ n\Delta T } \\
&= \frac{ f }{ 2 }R + R \\
&= \left( \frac{ f }{ 2 } + 1 \right)R
\end{split}
$$

Here, we see that,
$$C_{P} - C_{V} = R$$
This is called **Meyer's Equation**

Thus,
$$
\begin{split}
\text{Monoatomic} &: C_{V} = \frac{5}{2}R \\
\\
\text{Diatomic} &: C_{V} = \frac{7}{2}R \\
\\
\text{Polyatomic} &: C_{V} = \frac{8}{2}R 
\end{split}
$$

### Ratio of Specific Heats
[[01 Heat Capacity and Internal Energy#Poisson's Ratio]]

$$
\begin{split}
\upgamma &= \frac{ C_{P} }{ C_{V} } \\
&= \frac{ (f /2 +1)R }{ (f /2)R } \\
&= 1 + \frac{2}{f}
\end{split}
$$

Thus,
$$
\begin{split}
\text{Monoatomic} &: C_{V} = \frac{5}{3}  \\
\\
\text{Diatomic} &: C_{V} = \frac{7}{5} \\
\\
\text{Polyatomic} &: C_{V} = \frac{8}{6}
\end{split}
$$

- Monoatomic: $\upgamma = \frac{5}{3} = 1.67$
- Diatomic: $\upgamma = \frac{7}{5} = 1.5$
- Polyatomic: $\upgamma = \frac{4}{3} = 1.33$

Also,
$$C_{V} = \frac{ R }{ \upgamma - 1 }$$
$$C_{P} = \frac{ \upgamma R }{ \upgamma - 1 }$$

And internal energy,
$$\Delta U = nC_{V}\Delta T = \frac{ nR\Delta T }{ \upgamma-1 }$$

#### Mixture of Gases
Let two gases be,
- Gas 1: $n_{1},\ C_{V_{1}},\ C_{P_{1}},\ f_{1}$
- Gas 2: $n_{2},\ C_{V_{2}},\ C_{P_{2}},\ f_{2}$

Molar Heat Capacities,
$$C_{V_{mix}} = \frac{ n_{1}C_{V_{1}} + n_{2}C_{V_{2}} }{ n_{1} + n_{2} }$$
$$C_{P_{mix}} = \frac{ n_{1}C_{P_{1}} + n_{2}C_{P_{2}} }{ n_{1} + n_{2} }$$

Degree of Freedom,
$$f_{mix} = \frac{ n_{1}f_{1} + n_{2}f_{2} }{ n_{1} + n_{2} }$$

Ratio of specific heats,
$$\upgamma_{mix} = \frac{ n_{1}C_{P_{1}} + n_{2}C_{P_{2}} }{ n_{1}C_{V_{1}} + n_{2}C_{V_{2}} }$$

$$\upgamma_{mix} = 1 + \frac{2}{f_{mix}}$$