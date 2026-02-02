Links: 
___
# Processes
#### Isochoric 
When the volume is fixed. i.e. rigid container or fixed piston. 

In this case,
$$P \propto T$$

![[Pasted image 20240213165434.png]]

Since change in volume is zero, the gas does no work.
$$
\begin{split}
dW &= P(dV) \\
&= P(0) \\
W &= 0
\end{split}
$$

The change in internal energy will be,
$$
\begin{split}
\Delta U &= \frac{ f }{ 2 } nR\Delta T \\
&= \frac{ f }{ 2 } (P_{f}V - P_{i}V) \\
\Delta U &= \frac{f}{2}V(\Delta P)
\end{split}
$$

Using first law,
$$
\begin{split}
\Delta Q &= \frac{f}{2}V(\Delta P) + 0 \\
\Delta Q &= \frac{f}{2}V(\Delta P)
\end{split}
$$
Thus, all the heat provided is used to change temp., i.e. internal energy of the gas.

#### Isobaric
When the pressure is constant. 
Gas will expand against constant forces. 

In this case,
$$V \propto T$$

![[Pasted image 20240213165632.png]]

Here, work done,
$$
\begin{split}
W &= \int P \, dV \\
&= P \int dV \\
&= P\Delta V \\
&= nR\Delta T
\end{split}
$$

Change in internal energy, 
$$
\begin{split}
\Delta U &= \frac{f}{2} nR\Delta T \\
&= \frac{ f }{ 2 } (PV_{f} - PV_{i}) \\
&= \frac{ f }{ 2 }P\Delta V
\end{split}
$$

Thus, heat provided,
$$
\begin{split}
\Delta Q &= \frac{f}{2} P\Delta V + P\Delta V \\
&= \left( \frac{f}{2} + 1 \right) P\Delta V \\
&= \left( \frac{f}{2} + 1 \right) nR\Delta T
\end{split}
$$

#### Isothermal 
When the temperature is constant. 

If heat is given, the gas expands.
If heat is taken, the gas contracts.

In this case,
$$P \propto \frac{1}{V}$$
$$PV = \text{constant}$$

![[Pasted image 20240213173323.png]]

Here, work done,
$$
\begin{split}
W &= \int P \, dV \\
&= \int \frac{ nRT }{ V } \, dV \\
&= nRT \int_{V_{i}}^{V_{f}} \frac{ dV }{ V } \\
\\
&= nRT \ln \frac{V_{f}}{V_{i}} \\
&= nRT \ln \frac{P_{i}}{P_{f}} \\
\\
&= P_{i}V_{i} \ln \frac{V_{f}}{V_{i}} \\
&= P_{f}V_{f} \ln \frac{V_{f}}{V_{i}} 
\end{split}
$$

Since change in temp. is zero, internal energy is also zero, 
$$\Delta U = \frac{ f }{ 2 }nR\Delta T = 0$$

Thus, heat provided is used in work done,
$$\Delta Q = nRT \ln \left( \frac{V_{f}}{V_{i}} \right)$$

#### Polytrophic 
In this case,
$$PV^{a} = \text{const.} = k$$
where a is called *polytrophic constant* and it cannot be 1, otherwise it becomes isothermal. 

Here, work done,
$$
\begin{split}
W &= \int P \, dV \\
&= \int \frac{ K }{ V^{a} } \, dV \\
&= \frac{ P_{f}V_{f} - P_{i}V_{f} }{ 1 - a } \\
&= \frac{ nR\Delta T }{ 1-a }
\end{split}
$$

Internal Energy,
$$\Delta U = \frac{f}{2}nR\Delta T$$

Heat provided,
$$\Delta Q = \frac{f}{2}nR\Delta T + \frac{ nR\Delta T }{ 1-a }$$

### [[02 Adiabatic]]

### Cyclic Process 
When the final and initial states are the same. 
I.e. $P_{f} = P_{i}$; $V_{f} = V_{i}$; $T_{f} = T_{i}$

It is not a single process, but combination of a few. 

Since initial and final temp. are the same, change in internal energy is zero. 

By first law,
$$
\begin{split}
\Delta Q &= \cancelto{ 0 }{ \Delta U } + W \\
\Delta Q &= W
\end{split}
$$

In cyclic process, the work done is the area enclosed by PV graph. 
It is +ve if the arrows are clockwise and -ve if they are anti clockwise.

Here, we define efficiency,
$$\eta = \frac{ W }{ Q_{in} } \times 100$$
Using the previous result,
$$\eta = \frac{ Q_{in} - Q_{out} }{ Q_{in} } \times 100$$

![[Pasted image 20240213211843.png]]
