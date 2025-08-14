Links: [[00 Chemical Kinetics]] 
___
# Chemical Kinetics
Rate of appearance or disappearance,
$$\ce{ app = \frac{ d[A] }{ dt },\ disa = - \frac{ d[A] }{ dt } }$$

In a reaction, A $\to$ B
$$\ce{ - \frac{ 1 }{ a } \frac{ d[A] }{ dt } = \frac{ 1 }{ b } \frac{ d[B] }{ dt } }$$

Rate of reaction,
$$\ce{ Rate = - \frac{ 1 }{ a } \frac{ d[A] }{ dt } = \frac{ 1 }{ b } \frac{ d[B] }{ dt } }$$

Rate law,
$$\ce{ Rate = k_{r} [A]^{p}[B]^{q} }$$
And, $k_{A} = ak_{r}$.

#### Kinetics 
**Zero Order,**
$$
\begin{split}
\ce{ 
[A]_{t} &= [A]_{o} - kt \\
t_{1/2} &= \frac{ [A]_{o} }{ 2k } \\
t_{c} &= 2t_{1/2} 
 }
\end{split}
$$

**First Order,**
$$
\begin{split}
\ce{ 
k &= \frac{ 2.303 }{ t } \log_{10} \frac{ [A]_{o} }{ [A]_{t} } \\
t_{1/2} &= \frac{ \ln 2 }{ k } = \frac{ 0.693 }{ k } \\
[A]_{t_{1/2}(n)} &= \frac{ [A]_{o} }{ 2^{n} } 
 } 
\end{split}
$$

**Second Order Kinetics with one reactant,**
$$
\begin{split}
\ce{ 
\frac{ 1 }{ [A]_{t} } &= \frac{ 1 }{ [A]_{o} } + kt \\
t_{1/2} &= \frac{ 1 }{ k[A]_{o} } 
 }
\end{split}
$$

**Second Order Kinetics with two reactant,**
$$
\begin{split}
\ce{ 
t &= \frac{ 1 }{ k(a-b) } \ln \frac{ b(a-x) }{ a(b-x) } \\
Pseudo, \\
t &= \frac{ 1 }{ ka } \ln \frac{ [B]_{o} }{ [B]_{t} }
 } 
\end{split}
$$

#### Determination of Order 
Half life,
$$t_{1/2} \propto \frac{ 1 }{ a^{n-1} }$$

Integrated Law method, try to find rate constants at various steps assuming various rate laws. 

Pressure measurement,
$$
\begin{split}
\ce{ 
k = \frac{ 1 }{ t } \ln \frac{ p_{o}(A) }{ p_{t}(A) } \\
k = \frac{ 1 }{ t } \ln \frac{ p_{\infty} - p_{o}(A) }{ p_{\infty} - p_{t}(A) } 
 }
\end{split}
$$

Titration,
$$
\begin{split}
\ce{ 
k = \frac{ 1 }{ t } \ln \frac{ V_{o} }{ V_{t} } \\
k = \frac{ 1 }{ t } \ln \frac{ V_{\infty} - V_{o} }{ V_{\infty} - V_{t} } 
 }
\end{split}
$$

Optical rotation,
$$
\begin{split}
\theta &= \text{specific rotation} \times [A] \\
k = \frac{ 1 }{ t } \ln \frac{ \theta_{\infty} - \theta_{o} }{ \theta_{\infty} - \theta_{t} } 
k = \frac{ 1 }{ t } \ln \frac{ \theta_{o} }{ \theta_{t} } 
\end{split}
$$

#### Arrhenius Equation
$$\ce{ k = Ae^{ -E_{a}/RT } }$$

Taking log,
$$\ln k = \ln A - \frac{ E_{a} }{ RT }$$

For two different temp.,
$$\ln \frac{ k_{1} }{ k_{2} } = \frac{ E_{a} }{ R } \left( \frac{ 1 }{ T_{1} } - \frac{ 1 }{ T_{2} } \right)$$

Differential form,
$$\frac{ d(\ln k) }{ dT } = \frac{ E_{a} }{ RT^{2} }$$
Thus, sensitivity towards temp $\propto E_{a}$.

#### Nuclear Reactions 
Decay constant,
$$\lambda = \frac{ 1 }{ t } \ln \frac{ N_{o} }{ N_{t} }$$

Half life,
$$t_{1/2} = \frac{ \ln 2 }{ \lambda }$$
