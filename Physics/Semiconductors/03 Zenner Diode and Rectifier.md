Links: [[02 PN Junction]]
___
# Zenner Diode and Rectifier
## Zener Diode
It is a PN diode with reverse bias. 

Zenner diode is a heavily doped PN junction with thin depletion layer.

It can be used to stabilise potential difference across it.

![[Pasted image 20240128200812.png]]

#### ZD as Voltage Stabiliser
Voltage Stabilizer is a device which does not allow voltage to become more than a certain value. 

We connect a ZD in parallel with the load, due to this, the potential across the load cannot cross $V_{Z}$.

If the voltage gets  higher than the Zener voltage, the extra current flows through the diode thus limiting the potential difference across the load.

If applied voltage is small, the current will flow only across the load. 
If we increase the potential to $V_{Z}$, the PN diode will breakdown and thus all the extra current will flow through the diode. 

The potential across load will remain $V_{Z}$ even if $V > V_{Z}$.

![[Pasted image 20240128201332.png]]

Example,
![[Pasted image 20240128204958.png]]

## Rectifier
It is a PN diode based device, which converts AC to DC.

### Half-Wave Rectifier
When the diode is forward biased, i.e. the current is in +ve phase, the diode will allow current to flow through it. 

When the diode is reverse biased, i.e. the current is in -ve phase, the diode will not allow the current to flow through it.

Due to this, across the load, the current is unidirectional. 

Since it allows only half the wave to go to the load, it is Half Wave. 

Efficiency%,
$$
\begin{split}
\eta &= \frac{P_{out}}{P_{in}} \times 100 \\
&= \frac{ 40.6 }{ 1 + \frac{ R_{D} }{ R_{L} } } \% \\
&= 40.6 \frac{ R_{L} }{ R_{D} + R_{L} }
\end{split}
$$

If diode is ideal, 
$$\eta =40.6\%$$

![[Pasted image 20240128202503.png]]

### Full-Wave Rectifier
We connect two diodes  this time. 

For the +ve phase of the current, the top diode is in forward bias. At the same time the lower diode is in reverse bias. 

For the -ve phase of the current, the top diode is in reverse bias. At the same time the lower diode is in forward bias. 

Since the load has current all the time, this rectifier converts the full wave into DC and thus, it is Full Wave rectifier.

Efficiency% is double that of Half-Wave. 
$$
\begin{split}
\eta &= \frac{P_{out}}{P_{in}} \times 100 \\
&= \frac{ 81.2 }{ 1 + \frac{ R_{D} }{ R_{L} } } \% \\
&= 81.2 \frac{ R_{L} }{ R_{D} + R_{L} }
\end{split}
$$

If diode is ideal, 
$$\eta = 81.2\%$$

![[Pasted image 20240128203127.png]]

An alternate way of making a FWR is,
![[Pasted image 20240128203825.png]]