Links: [[00 Capacitance]], [[04 Circuit Solutions of LR Circuit]]
___
# Circuit solutions of RC Circuit
[[01 Individual Circuits#Purely Capacitive Circuit]]
[[02 Dual Circuits#RC Circuit]]

If nothing is said, we take the capacitor to be uncharged.

The current through the resistor will be $\varepsilon /R$ just after closing the circuit. 

Thus at t = 0, if the capacitor is uncharged, it will behave like a short wire. 

At any time t, the current through the resistor will be,
$$i = \frac{ \varepsilon - q /C }{ R }$$

As time increases, the charge on the capacitor will increase, $q /C$ increases, the potential difference decreases, and thus current through the resistor decreases. 

![[Pasted image 20240109170026.png]]

At steady state ($t \to \infty$), the wire will capacitor will have no current and the capacitor will be fully charged.

The charge across the capacitor will be,
$$Q = C \varepsilon$$

At $t \to \infty$, (steady state), capacitor will behave like broken wire. 

Example,
![[Pasted image 20240110122807.png]]
![[Pasted image 20240110122814.png]]

#### Work done and heat loss

Work done by battery,
$$W = \varepsilon Q = C \varepsilon^{2}$$
This work done has heated up the resistor and created an electric field between the plates of the capacitor, which has stored electric potential energy in the capacitor. 

Change in potential energy stored in the capacitor,
$$\Delta U = \frac{ 1 }{ 2 } C \varepsilon^{2} - \frac{ 1 }{ 2 } C (0)^{2} = \frac{ 1 }{ 2 } C \varepsilon^{2}$$

Thus, half of the work done by battery is stored in the capacitor. 

The other is used to heat up the resistance.
$$
\begin{split}
W &= \Delta U + \text{loss} \\
\text{heat loss} &= \frac{ 1 }{ 2 } C \varepsilon^{2}
\end{split}
$$

![[Pasted image 20240110122753.png]]

#### Kirchhoff's Current Law
[[03 Kirchhoff's Laws]]

Here instead of current, we think about the initial and final charges on the plates which are connected of the respective capacitors. 

![[Pasted image 20240110131318.png]]

#### Kirchhoff's Voltage Law
The same as that in current electricity. 

![[Pasted image 20240110131602.png]]

![[Pasted image 20240110131918.png]]


### Examples 
![[Pasted image 20240110125100.png]]
![[Pasted image 20240110125108.png]]

![[Pasted image 20240110130055.png]]
![[Pasted image 20240110130106.png]]

![[Pasted image 20240110130812.png]]


### [[02.5 Charging of Capacitor]]
For some complex circuit if the *capacitor is initially uncharged,* we can use the short cut,

Charge on capacitor at any time t,
$$q = Q_{ss} (1 - e^{ -t/\uptau })$$
where $Q_{ss} \to$ charge on capacitor at steady state. 

And we will write,
$$\uptau = R_{eq}C$$
where $R_{eq}$ is the equivalent resistance across capacitor (with the battery short i.e. replace battery by short wire). 

![[Pasted image 20240110173939.png]]
![[Pasted image 20240110174225.png]]
![[Pasted image 20240110175254.png]]

### Discharging of Capacitor 
Initially, the current is,
$$i_{o} = \frac{ Q }{ RC }$$

As time passes, the current decreases the charge on the +ve plate and increases the charge on the -ve plate. 

At any time t, 
$$i = \frac{ q }{ RC }$$
as t increases, q decreases and thus i also decreases. 

At $t \to \infty$, charge on the capacitor will be zero and thus there will be no current in the circuit. 

The energy stored in the capacitor is dissipated by the resistor in the form of heat. 

![[Pasted image 20240110180203.png]]

#### Charge on Capacitor 
At any time t,
![[Pasted image 20240110180610.png]]

Applying KVL,
$$
\begin{split}
- \frac{ -q }{ C } - iR &= 0 \\
i &= \frac{ q }{ RC }
\end{split}
$$

Here, current can be written as,
$$i = - \frac{ dq }{ dt }$$

This gives,
$$
\begin{split}
- \frac{ dq }{ dt } &= \frac{ q }{ RC } \\
\int_{Q}^{q} \frac{ dq }{ q } &= -\int_{0}^{t} \frac{ dt }{ RC } \\
(\ln q)_{Q}^{q} &= \frac{ -1 }{ RC } (t)_{0}^{t} \\
\ln \frac{ q }{ Q } &= \frac{ -t }{ RC } \\
q &= Q e^{ -t/RC }
\end{split}
$$

Thus at any time, charge on capacitor is,
$$q = Q e^{ -t/\uptau }$$
Which is an exponentially decreasing function.

![[Pasted image 20240110181000.png]]

Now, the electric field inside the capacitor can be written as,
$$
\begin{split}
E &= \frac{ q }{ A\varepsilon_{o} } \\
&= \frac{ Qe^{ -t/\uptau } }{ A\varepsilon_{o} } 
\end{split}
$$
Which is an exponentially decreasing function. 

#### Current in Circuit 
At any time t, current is,
$$i = \frac{ Q }{ RC } e^{ -t/\uptau }$$
Which is also a decreasing function. 

![[Pasted image 20240110181250.png]]

Area under the current-time curve will give the charge flown,
$$
\begin{split}
\text{charge flown} &= \int_{0}^{\infty} \frac{ Q }{ RC } e^{ -t/RC } \, dt \\
&= \frac{ Q(-RC) }{ RC } (e^{ -t/RC })_{0}^{\infty} \\
&= -Q (0 - 1) \\
&= Q
\end{split}
$$

#### Power dissipated by Resistor 
$$
\begin{split}
P &= i^{2} R \\
&= \frac{ Q^{2} }{ RC^{2} } e^{ -2t/RC }
\end{split}
$$
Which is decreasing even faster than the current. 

![[Pasted image 20240110181843.png]]

![[Pasted image 20240110181904.png]]

The total heat dissipated,
$$
\begin{split}
H &= \int_{0}^{\infty} P \, dt \\
&= \frac{ Q^{2} }{ RC^{2} } \int_{0}^{\infty} e^{ -2t/RC } \, dt \\
&= \frac{ -Q^{2} }{ 2C } (0 - 1) \\
&= \frac{ Q^{2} }{ 2C }  
\end{split}
$$

This is the energy lost by the capacitor. 
