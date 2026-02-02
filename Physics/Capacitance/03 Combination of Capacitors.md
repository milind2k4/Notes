Links: [[01 Capacitor]], [[04 Equivalent Resistance]], [[05 Combination of Inductors]]
___
# Combination of Capacitors
We connect a battery to the combination and then find out how much charge it provided. Then we divide the charge by the emf of the battery. 

$$C_{eq} = \frac{ Q }{ V }$$

![[Pasted image 20240110132904.png]]

### Series
Capacitors are connected end to end and they *have the same charge.* 

Potential differences across each capacitor,
$$
\begin{split}
V_{1} &= \frac{ Q }{ C_{1} } \\
V_{2} &= \frac{ Q }{ C_{2} } \\
V_{3} &= \frac{ Q }{ C_{3} } \\
\end{split}
$$

That is,
$$V \propto \frac{ 1 }{ C }$$

Applying [[02 Circuit solutions of RC Circuit#Kirchhoff's Voltage Law|KVL,]]
$$
\begin{split}
V - \frac{ Q }{ C_{1} } - \frac{ Q }{ C_{2} } - \frac{ Q }{ C_{3} } &= 0 \\
\frac{ V }{ Q } &= \frac{ 1 }{ C_{1} } + \frac{ 1 }{ C_{2} } + \frac{ 1 }{ C_{3} } \\
\frac{ 1 }{ C_{eq} } &= \frac{ 1 }{ C_{1} } + \frac{ 1 }{ C_{2} } + \frac{ 1 }{ C_{3} } 
\end{split}
$$

Which is the same as [[04 Equivalent Resistance#Parallel Combination]]

Energy stored in each capacitor,
$$
\begin{split}
U_{1} &= \frac{ Q^{2} }{ 2C_{1} } \\
U_{2} &= \frac{ Q^{2} }{ 2C_{2} } \\
U_{3} &= \frac{ Q^{2} }{ 2C_{3} } \\
\end{split}
$$
Thus,
$$U \propto \frac{ 1 }{ C }$$

The net energy stored,
$$
\begin{split}
U_{net} &= \frac{ Q^{2} }{ 2 } \left( \frac{ 1 }{ C_{1} } + \frac{ 1 }{ C_{2} } + \frac{ 1 }{ C_{3} } \right) \\
&= \frac{ Q^{2} }{ 2C_{eq} }
\end{split}
$$

![[Pasted image 20240110133625.png]]

### Parallel 
When the potential difference across each is the same. 

Charge on each capacitor,
$$
\begin{split}
Q_{1} &= C_{1} V \\
Q_{2} &= C_{2} V
\end{split}
$$
That is,
$$Q \propto C$$

The net charge,
$$
\begin{split}
Q &= Q_{1} + Q_{2} \\
&= (C_{1} + C_{2}) V 
\end{split}
$$

Thus equivalent capacitance,
$$C_{eq} = \frac{ Q }{ V } = C_{1} + C_{2}$$
which is the same as [[04 Equivalent Resistance#Series Combination]]

The charge on each capacitor,
$$
\begin{split}
Q_{1} &= \frac{ C_{1} }{ C_{1} + C_{2} } Q \\
Q_{2} &= \frac{ C_{2} }{ C_{1} + C_{2} } Q \\
\end{split}
$$

Energy stored in each capacitor,
$$
\begin{split}
U_{1} &= \frac{ 1 }{ 2 } C_{1} V \\
U_{2} &= \frac{ 1 }{ 2 } C_{2} V \\
\end{split}
$$
That is,
$$U \propto C$$

Total energy stored,
$$
\begin{split}
U_{net} &= \frac{ 1 }{ 2 }(C_{1} + C_{2}) V \\
&= \frac{ 1 }{ 2 } C_{eq} V
\end{split}
$$

![[Pasted image 20240110135531.png]]

### Examples
![[Pasted image 20240110134857.png]]
![[Pasted image 20240110134904.png]]

![[Pasted image 20240110140317.png]]
![[Pasted image 20240110140324.png]]

![[Pasted image 20240110141942.png]]
![[Pasted image 20240110141958.png]]
(the values are wrong for $Q_{1}$ but the concept is the same as previous question)

### Wheatstone Bridge 
[[04 Equivalent Resistance#Wheatstone Bridge]]

Under balanced condition the middle capacitor has no charge.
$$
\begin{split}
V - x = \frac{ Q }{ C_{1} } &= \frac{ q }{ C_{3} } \\
x = \frac{ Q }{ C_{2} } &= \frac{ q }{ C_{4} } 
\end{split}
$$

From these two equations,
$$\frac{ Q }{ q } = \frac{ C_{1} }{ C_{3} } = \frac{ C_{2} }{ C_{4} }$$

Cross multiplying,
$$C_{1}C_{4} = C_{2}C_{3}$$

![[Pasted image 20240110142846.png]]

We can remove the middle capacitor, and the net capacitance comes out to be,
$$C_{net} = \frac{ C_{1}C_{2} }{ C_{1} + C_{2} } + \frac{ C_{3}C_{4} }{ C_{3} + C_{4} }$$

![[Pasted image 20240110143133.png]]

### Combination of Plates 
1. Number all the plates. 
2. Take two points A and B between which we have to find capacitance. 
3. Connect plate accordingly.

![[Pasted image 20240110194309.png]]

![[Pasted image 20240110194812.png]]