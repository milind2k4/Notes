Links: [[02 Self Induction]], [[02 Circuit solutions of RC Circuit]]
___
# Circuit Solutions LR Circuit
[[02 Dual Circuits#LR Circuit]]

At t = 0, when the circuit is closed, the inductor behaves like an infinite resistance or broken wire. 

When $t \to \infty$ (aka steady state), the inductor behaves like a short wire or zero resistance. 

### Growth of Current
[[02.5 Charging of Capacitor]]

At t = t, applying Kirchhoff's laws,
$$
\begin{split}
\varepsilon - iR - L \frac{ di }{ dt } &=  0 \\
\varepsilon - iR &=  L \frac{ di }{ dt } \\
\int_{0}^{t} dt &= L \int_{0}^{i} \frac{ di }{ \varepsilon - iR } \\
t &= \frac{ L }{ R } \ln \frac{ \varepsilon - iR }{ \varepsilon } \\
\\
i &=  \frac{ \varepsilon }{ R } (1 - e^{ -Rt/L }) \\
\end{split}
$$
Thus, we have,
$$i =  \frac{ \varepsilon }{ R } (1 - e^{ -t/\uptau })$$

where $\uptau = \displaystyle \frac{L}{R}$ is called time constant. 

Voltage across resistor,
$$V_{R} = iR = \varepsilon (1 - e^{ -Rt/L })$$

![[Pasted image 20240117203052.png]]

The current increases exponentially,
![[Pasted image 20240117203106.png]]

Due to presence of inductor, current grows slowly. 


##### Complex Circuit 
[[02 Circuit solutions of RC Circuit#02.5 Charging of Capacitor]]

Current through inductor is given by,
$$i = i_{ss} (1 - e^{ -t/\uptau })$$
where $i_{ss}$ is current through inductor at steady state.

And,
$$\uptau = \frac{ L }{ R_{eq} }$$
where $R_{eq}$ is to be found across L, replacing battery by short wire.

![[Pasted image 20240117204220.png]]
![[Pasted image 20240117204318.png]]

#### Potential Differences 
**Across resistor,**
$$
\begin{split}
V_{R} &= iR \\
&= \varepsilon (1 - e^{ -t/\uptau })
\end{split}
$$

**Across inductor,**
$$
\begin{split}
V_{L} &= L \frac{ di }{ dt } \\
&= \varepsilon\ e^{ -t/\uptau }
\end{split}
$$
Which is an exponentially decreasing function. 

![[Pasted image 20240117203510.png]]

#### Powers of Inductor 
It is the rate at which inductor is storing energy. 

$$
\begin{split}
P &= V_{L} i \\
&= \varepsilon\ e^{ -t/\uptau } \frac{ \varepsilon }{ R } (1 - e^{ -t/\uptau }) \\
&= \frac{ \varepsilon^{2} }{ R } (e^{ -t/\uptau } - e^{ -2t/\uptau }) 
\end{split}
$$

At t = 0, i = 0 and thus, P = 0,
At $t \to \infty$ V = 0 and thus, P = 0

![[Pasted image 20240117203805.png]]

The area under the curve will give the energy which is stored in inductor. 
$$
\begin{split}
U &= \frac{ 1 }{ 2 }L(i_{t \to \infty}) \\
&= \frac{ 1 }{ 2 } \frac{ L\varepsilon^{2} }{ R^{2} }
\end{split}
$$

### Decay of Current 
At $t = 0$, the inductor already has some current, and thus some energy. 

$$U_{i} = \frac{ 1 }{ 2 } L i_{o}^{2}$$

This energy will be dissipated in the form of heat by the resistor. 
$$H = \int_{0}^{\infty} P \, dt = \frac{1}{2}Li_{o}^{2} $$

At any time t, applying KVL,
$$
\begin{split}
-L \frac{ di }{ dt }  - iR &= 0 \\
L \frac{ di }{ dt } &= -iR \\
\frac{ L }{ R } \int_{i_{o}}^{i} \frac{di}{i} &= \int_{0}^{t} dt \\
- \frac{L}{R} \ln \frac{i}{i_{o}} &= i \\
i &= i_{o}e^{-Rt/L} \\  
\end{split}
$$

![[Pasted image 20240117205301.png]]

Thus we can write,
$$i = i_{o}e^{-t/\uptau}$$
Thus current decreases exponentially with time.

![[Pasted image 20240117205333.png]]

And, we have power across resistor,
![[Pasted image 20240117205509.png]]

## LC Oscillations 
[[02 Dual Circuits#LC Circuit]]

Here, since there is no resistance to dissipate the energy, the energy will keep on transforming between electric potential and magnetic potential energies. 

The charge on capacitor and the current in circuit will keep on oscillating. 

If there is charge on the capacitor at first,
![[Pasted image 20240117212151.png]]

Using energy conservation,
$$\frac{ Q^{2} }{ 2C } + 0 = \frac{ q^{2} }{ 2C } + \frac{ Li^{2} }{ 2 }$$

The max. value of current will thus be,
$$i = \frac{ Q }{ \sqrt{ LC } }$$

Applying KVL,
$$
\begin{split}
- \frac{ -q }{ C } - L \frac{ di }{ dt } &= 0 \\
\frac{ q }{ C } - L \frac{ di }{ dt } &= 0
\end{split}
$$

Now, we know that, here,
$$i = -\frac{ dq }{ dt }$$

Putting this into the equation from KVL,
$$
\begin{split}
\frac{ q }{ C } - L \frac{ d }{ dt }\left( -\frac{ dq }{ dt } \right) &= 0 \\
\frac{ q }{ C } + L \frac{ d^{2} q }{ d t^{2} } &= 0 \\
\frac{ d^{2} q }{ d t^{2} } + \frac{ 1 }{ LC }q &= 0 
\end{split}
$$

Using comparison from [[01 Equation of SHM|SHM]], we get,
$$q = Q \sin \left( \frac{ 1 }{ \sqrt{ LC } }t + \theta \right)$$

At t = 0, $q = Q$,
$$
\begin{split}
Q &= Q \sin \theta \\
\theta &= \frac{\pi}{2}
\end{split}
$$

Thus, charge at any time on capacitor,
$$
\begin{split}
q &= Q\sin \left( \frac{ 1 }{ \sqrt{ LC } }t + \frac{\pi}{2} \right) \\
&= Q \cos \left( \frac{ t }{ \sqrt{ LC } } \right)
\end{split}
$$

Differentiating this, we get current,
$$i = -\frac{ dq }{ dt } = \frac{ Q }{ \sqrt{ LC } } \sin \left( \frac{ t }{ \sqrt{ LC } } \right)$$

There being a cos in expression of charge and sin in the expression of current means that charge is zero when current is max and vice-versa. 

The charge and current will thus oscillate. 

Here, the angular frequency is,
$$\omega = \frac{ 1 }{ \sqrt{ LC } }$$
And the time period is,
$$T = 2\pi \sqrt{ LC }$$



