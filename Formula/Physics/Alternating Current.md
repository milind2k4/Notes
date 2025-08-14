Links: [[00 Alternating Current]]
___
# Alternating Current

RMS Value of AC,
$$i_{rms} = \frac{i_{o}}{\sqrt{ 2 }}$$
Power:
$$P_{avg} = V_{rms} i_{rms} \cos \theta$$
##### AC Generator
$$\varepsilon = -NBA\omega \sin\omega t$$
Max emf,
$$\varepsilon_{o} = NBA\omega$$

#### Circuits
Resistive Circuit: Current is with voltage.
$$
\begin{split}
i_{o} &= \frac{ V_{o} }{ R } \\
P_{avg} &= \frac{ i_{o}^{2}R }{ 2 } = \frac{ V_{o}^{2} }{ 2R } 
\end{split}
$$

Capacitive circuit: Current is ahead of voltage.
$$
\begin{split}
X_{C} &= \frac{ 1 }{ \omega C } \\
i_{o} &= \frac{ V_{o} }{ X_{C} } \\
P_{avg} &= 0 
\end{split}
$$

Inductive circuit: Current is behind voltage.
$$
\begin{split}
X_{L} &= \omega L \\
i_{o} &= \frac{ V_{o} }{ X_{L} } \\
P_{avg} &= 0 
\end{split}
$$

#### Dual Circuits 
RC Circuit,
$$
\begin{split}
Z &= \sqrt{ R^{2} + X_{C}^{2} } \\
&= \sqrt{ R^{2} + \left( \frac{ 1 }{ \omega C } \right)^{2} } \\
i_{o} &= \frac{ V_{o} }{ Z } \\
P_{avg} &= \frac{ i_{o}^{2}R }{ 2 } 
\end{split}
$$

LR Circuit,
$$
\begin{split}
Z &= \sqrt{ R^{2} + X_{L}^{2} } \\
&= \sqrt{ R^{2} + (\omega L)^{2} } \\
i_{o} &= \frac{ V_{o} }{ Z } \\
P_{avg} &= \frac{ i_{o}^{2}R }{ 2 }
\end{split}
$$

LC Circuit,
$$
\begin{split}
Z &= |X_{L} - X_{C}| \\
&= \left| \omega L - \frac{ 1 }{ \omega C } \right| \\
i_{o} &= \frac{ V_{o} }{ Z } \\
P_{avg} &= 0 
\end{split}
$$
Resonance frequency,
$$\omega_{r} = \frac{ 1 }{ \sqrt{ LC } }$$
#### LCR Circuit 
$$
\begin{split}
Z &= \sqrt{ R^{2} + (X_{L} - X_{C})^{2} } \\
i_{o} &= \frac{ V_{o} }{ Z } \\
\cos \theta &= \frac{ R }{ Z } \\
\end{split}
$$

Resonance,
$$
\begin{split}
X_{C} &= X_{L} \\
\omega_{r} &= \frac{ 1 }{ \sqrt{ LC } } \\
V &= iR = V_{R} \\
\cos \theta &= 1 \\
P_{avg} &= i_{rms}^{2}R 
\end{split}
$$

Bandwidth,
$$\Delta\omega = \frac{ R }{ L }$$

Quality Factor,
$$Q = \frac{ \omega_{r} }{ \Delta\omega } = \frac{ 1 }{ R }\sqrt{ \frac{ L }{ C } }$$
#### Transformer 
$$
\begin{split}
\frac{ \varepsilon_{s} }{ \varepsilon_{p} } &= \frac{ n_{s} }{ n_{p} } \\
\varepsilon &\propto n \\
\\
\frac{ i_{p} }{ i_{s} } &= \frac{ n_{s} }{ n_{p} } \\
i &\propto \frac{ 1 }{ n } 
\end{split}
$$
Step up means stepping up voltage. 
Step down means stepping down voltage. 






