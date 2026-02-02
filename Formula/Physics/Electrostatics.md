Links: [[00 Electrostatics]]
___
# Electrostatics
Charge on e,
$$e^{-} = -1.6 \times 10^{-19}\ C$$
Permittivity,
$$
\begin{split}
\varepsilon_{o} &= 8.85 \times 10^{-12}\ \ce{ \frac{ C^{2} }{ N-m^{2} } } \\
\frac{ 1 }{ 4\pi\varepsilon_{o} } &= 9 \times 10^{9}\ \ce{ \frac{ N-m^{2} }{ C^{2} } }
\end{split}
$$
Coulomb's Law,
$$\vec{f} = \frac{ 1 }{ 4\pi\varepsilon_{o} } \frac{ q_{1}q_{2} }{ r^{3} }\vec{r}$$

Relation between E and V,
$$
\begin{split}
dV &= -\vec{E}.d\vec{r} \\
E &= -\nabla V
\end{split}
$$


#### Electric Fields 
Point charge,
$$E = \frac{ kq }{ r^{2} }$$
Ring,
$$
\begin{split}
E_{c} &= 0 \\
E_\text{axis} &= \frac{ kqx }{ (R^{2} + x^{2})^{3/2} } \\
E_{max} &= \frac{ 2kq }{ 3\sqrt{ 3 }R^{2} },\ \text{at}\ r = \frac{ R }{ \sqrt{ 2 } }
\end{split}
$$

Disk,
$$
\begin{split}
E &= \frac{ \sigma }{ 2\varepsilon_{o} } \left( 1 - \frac{ x }{ \sqrt{ R^{2} + x^{2} } } \right) \\
&= \frac{ \sigma }{ 2\varepsilon_{o} }(1 - \cos \theta)
\end{split}
$$
##### Wire
Finitely long wire,
$$
\begin{split}
E_{\perp} &= \frac{ k\lambda }{ r }(\sin \theta_{2} + \sin \theta_{1}) \\
E_{\parallel} &= \frac{ k\lambda }{ r }|\cos \theta_{2} - \cos \theta_{1}|
\end{split}
$$
Semi infinite wire,
$$
\begin{split}
E_{\perp} &= \frac{ k\lambda }{ r } \\
E_{\parallel} &= \frac{ k\lambda }{ r } \\
E_{net} &= \frac{ \sqrt{ 2 }k\lambda }{ r } 
\end{split}
$$
Infinitely long wire,
$$E = \frac{ 2k\lambda }{ r }$$

##### Infinitely large sheet
$$E = \frac{ \sigma }{ 2\varepsilon_{o} }$$
##### Sphere 
Hollow,
$$
\begin{split}
E_{in} &= 0 \\
E_\text{surface} &= \frac{ kQ }{ R^{2} } \\
E_{out} &= \frac{ kQ }{ r^{2} } \\
\end{split}
$$
Solid,
$$
\begin{split}
E_{in} &= \frac{ kQr }{ R^{3} } &= \frac{ \rho r }{ 3\varepsilon_{o} } \\
E_{sur} &= \frac{ kQ }{ R^{2} } \\
E_{out} &= \frac{ kQ }{ r^{2} } 
\end{split}
$$

##### Dipole 
$$
\begin{split}
\vec{E}_\text{axis} &= \frac{ 2k\vec{p} }{ r^{3} } \\
\vec{E}_\text{equa} &= - \frac{ k\vec{p} }{ r^{3} } \\
E_\text{any} &= \frac{ kp }{ r^{3} }\sqrt{ 1 + 3\cos ^{2}\theta }
\end{split}
$$

#### Electric Potentials
Point charge,
$$V = \frac{ kQ }{ r }$$

Ring,
$$
\begin{split}
V_{c} &= \frac{ kQ }{ R } \\
V_\text{axis} &= \frac{ kQ }{ \sqrt{ R^{2} + x^{2} } } 
\end{split}
$$
Disk,
$$
\begin{split}
V &= \frac{ 2kQ }{ \sqrt{ R^{2} + x^{2} } + x } \\
&= \frac{ \sigma }{ 2\varepsilon_{o} }(\sqrt{ R^{2} + x^{2} } - x) 
\end{split}
$$
Infinite sheet,
$$\Delta V = \frac{ \sigma d }{ 2\varepsilon_{o} }$$

Infinite wire,
$$\Delta V = 2k\lambda \log \frac{ r_{b} }{ r_{a} }$$

##### Sphere 
Hollow,
$$
\begin{split}
V_{in} &= \frac{ kQ }{ R } \\
V_{sur} &= \frac{ kQ }{ R } \\
V_{out} &= \frac{ kQ }{ r }
\end{split}
$$

Solid,
$$
\begin{split}
V_{in} &= \frac{ kQ }{ 2R^{3} } (3R^{2} - r^{2}) \\
V_{c} &= \frac{ 3kQ }{ 2R } \\
V_{sur} &= \frac{ kQ }{ R } \\
V_{out} &= \frac{ kQ }{ r }
\end{split}
$$

##### Dipole 
$$
\begin{split}
V_\text{axis} &= \frac{ kp }{ r^{2} } \\
V_\text{equa} &= 0 \\
V_\text{any} &= \frac{ k\vec{p} . \vec{r} }{ r^{3} }
\end{split}
$$

#### Electric Potential Energy 
$$U = qV$$
For a symmetric system,
$$U = \frac{ n }{ 2 } \times (\text{PE of one charge with others})$$
Total EPE of a system,
$$U_{sys} = U_\text{self} + U_\text{inte.}$$
#### Self Energy 
Hollow sphere,
$$U = \frac{ kQ^{2} }{ 2R } = \frac{ 0.5 kQ^{2} }{ R }$$

Solid sphere,
$$U = \frac{ 3kQ^{2} }{ 5R } = \frac{ 0.6 kQ^{2} }{ R }$$

#### Energy Density 
$$\frac{ dU }{ dV } = \frac{ 1 }{ 2 }\varepsilon E^{2}$$
EPE of system,
$$U_{e} = \int \frac{ 1 }{ 2 }\varepsilon E^{2} \, dV$$
#### Dipole in Field 
Torque,
$$\vec{\tau} = \vec{p} \times \vec{E}$$

Time period,
$$T = 2\pi\sqrt{ \frac{ I }{ pE } }$$

Potential energy,
$$U = -\vec{p} . \vec{E}$$
#### E. Flux and Gauss Law
$$\phi_{e} = \vec{E}.\vec{S}$$
Gauss Law,
$$\phi = \frac{ Q_{in} }{ \varepsilon_{o} }$$
#### Electrostatic Pressure
$$P = \frac{ \sigma^{2} }{ 2\varepsilon_{o} }$$

