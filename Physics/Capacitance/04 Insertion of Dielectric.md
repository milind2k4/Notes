Links: [[00 Capacitance]]
___
# Insertion of Dielectric
**Dielectric** is a type of conductor in which the net electric field inside is not zero on applying an external electric field. 

$k$ is dielectric constant or relative permittivity. It is always more than 1. 
- $k = 1$ for air/vaccum
- $k = 81$ for water
- $k = \infty$ for conductor

The capacitance is multiplied by the dielectric constant.

![[Pasted image 20240110183149.png]]

#### If charge is fixed

| Without Dielectric                                                   | With Dielectric                                                                                         |
| -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| $$E_{o} = \frac{ Q }{ A\varepsilon_{o} }$$                           | $$E = \frac{ Q }{ A\varepsilon_{o}\varepsilon_{r} } = \frac{ E_{o} }{ k }$$                             |
| $$V_{o} = E_{o}d = \frac{ Qd }{ A\varepsilon_{o} }$$                 | $$V = Ed = \frac{ Qd }{ A\varepsilon_{o}k } = \frac{ V_{o} }{ k }$$                                     |
| $$C_{o} = \frac{ A\varepsilon_{o} }{ d }$$                           | $$C = \frac{ A\varepsilon_{o}k }{ d } = kC_{o}$$                                                        |
| $$\frac{ dU_{o} }{ dV } = \frac{ Q^{2} }{ 2A^{2} \varepsilon_{o} }$$ | $$\frac{ dU }{ dV } = \frac{ Q^{2} }{ A^{2}\varepsilon_{o}k } = \frac{ 1 }{ k } \frac{ dU_{o} }{ dV }$$ |
| $$U_{o} = \frac{ Q^{2}d }{ 2A\varepsilon_{o} }$$                     | $$U = \frac{ Q^{2} }{ 2A\varepsilon_{o}k } = \frac{ U_{o} }{ k }$$                                      |

Thus, electric field, potential difference, energy density and energy stored decrease, while capacitance increases. 

#### If potential difference is fixed 

| Without Dielectric                                                                          | With dielectric                                                                                             |
| ------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| $$V = V_{o}$$                                                                               | $$V = V_{o}$$                                                                                               |
| $$E_{o} = \frac{ V }{ d }$$                                                                 | $$E = \frac{ V }{ d } = E_{o}$$                                                                             |
| $$C_{o} = \frac{ A\varepsilon_{o} }{ d }$$                                                  | $$C = \frac{ A\varepsilon_{o}k }{ d } = kC_{o}$$                                                            |
| $$Q_{o} = C_{o} V = \frac{ A\varepsilon_{o} }{ d }V$$                                       | $$Q = CV = \frac{ A\varepsilon_{o}k }{ d }V = kQ_{o}$$                                                      |
| $$\frac{ dU_{o} }{ dV } = \frac{ 1 }{ 2 }\varepsilon_{o} \frac{ V^{2} }{ d^{2} }$$          | $$\frac{ dU }{ dV } = \frac{ 1 }{ 2 } \varepsilon_{o}k \frac{ V^{2} }{ d^{2} } = k \frac{ dU_{o} }{ dV } $$ |
| $$U_{o} = \frac{ 1 }{ 2 }C_{o}V^{2} = \frac{ 1 }{ 2 } \frac{ A\varepsilon_{o} }{ d }V^{2}$$ | $$U = \frac{ 1 }{ 2 }CV^{2} = \frac{ 1 }{ 2 }kC_{o}V = kU_{o}$$                                             |

Thus, potential difference and electric field remains the same, while capacitance, charge, energy density and energy stored is increased. 

### Combination of Dielectric 
[[03 Combination of Capacitors]]

The electric field in the dielectrics,
$$
\begin{split}
E_{1} &= \frac{ Q }{ A\varepsilon_{o}k_{1} } \\
E_{2} &= \frac{ Q }{ A\varepsilon_{o}k_{2} }
\end{split}
$$

The potential difference between the plates,
$$
\begin{split}
V &= E_{1}d_{1} + E_{2}d_{2} \\
&= \frac{ Qd_{1} }{  A\varepsilon_{o}k_{1} } + \frac{ Qd_{2} }{ A\varepsilon_{o}k_{2} } 
\end{split}
$$

Thus capacitance comes out to be,
$$
\begin{split}
C &= \frac{ Q }{ V } 
\\
&= \frac{ Q }{ \displaystyle  \frac{ Qd_{1} }{ A\varepsilon_{o}k_{1} } + \frac{ Qd_{2} }{ A\varepsilon_{o}k_{2} } } 
\\
&= \frac{ 1 }{ \displaystyle \frac{ d_{1} }{ A\varepsilon_{o}k_{1} } + \frac{ d_{2} }{ A\varepsilon_{o}k_{2} } }
\end{split}
$$

![[Pasted image 20240110190000.png]]

Alternatively we can do,
$$\frac{ 1 }{ C } = \frac{ d_{1} }{ k_{1}A\varepsilon_{o} } + \frac{ d_{2} }{ k_{2}A\varepsilon_{o} }$$

![[Pasted image 20240110190016.png]]

Similarly, we can convert any combination of dielectrics into combination of separate capacitors. 

![[Pasted image 20240110190303.png]]
![[Pasted image 20240110190642.png]]

![[Pasted image 20240110191028.png]]

### Force on Dielectric 
The net force on the dielectric is towards the centre of the capacitor due to induction of charges and electrostatic force. 

![[Pasted image 20240110193725.png]]

To find the force, we first find the potential energy of the system,
$$
\begin{split}
U &= \frac{ 1 }{ 2 }CV^{2} \\
&= \frac{ 1 }{ 2 } \left( \frac{ (l-x)b \varepsilon_{o} }{ d } + \frac{ kxb\varepsilon_{o} }{ d } \right) V^{2} \\
&= \frac{ 1 }{ 2 } \frac{ b\varepsilon_{o} }{ d } [(k -1)x + l] V^{2} 
\end{split}
$$

Now,
$$
\begin{split}
f_{e} &= \frac{ dU }{ dx } \\
&= \frac{ b\varepsilon_{o} }{ 2d } (k-1)V^{2}
\end{split}
$$
This is the constant dielectric attractive force on the dielectric.

![[Pasted image 20240110193742.png]]


When Q is constant,
$$F = \frac{ Q^{2} }{ 2C^{2} } \left( \frac{ dC }{ dx }  \right)$$
