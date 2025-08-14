Links: [[01 Processes]], [[03 Molar Heat Capacity]]
___
# Adiabatic
There is no exchange of heat by the gas. 
In this case, the walls of the container are insulating.
$$
\begin{split}
dQ &= dU + dW \\
dW &= -dU
\end{split}
$$
I.e. 
if volume increases (W is +ve), temp. decreases (dU is -ve). 
if volume decreases (W is -ve), temp. increases (dU is +ve). 

Thus, adiabatic expansion cools, and compression heats. 

There will be however, change in pressure, volume and temp..

##### Relation between P and V
[[03 Molar Heat Capacity#Ratio of Specific Heats]]
$$PV^{\upgamma} = \text{const.}$$

Differentiating this,
$$
\begin{split}
P\upgamma V^{\upgamma-1}dV + V^{\upgamma}dP &= 0\\
\upgamma P dV + VdP &= 0 \\
\frac{ dP }{ dV } &= -\frac{ \upgamma P }{ V }
\end{split}
$$

As volume increases, P decreases. Thus magnitude of slope decreases. 

Also, to find final temp., we can conserve moles,
$$\frac{ P_{i}V_{i} }{ T_{i} } = \frac{ P_{f}V_{f} }{ T_{f} }$$

![[Pasted image 20240213184947.png]]

Now, we know that,
$$\upgamma = 1 + \frac{ 2 }{ f }$$
Thus, for different gases, PV curve will be different. 

For monoatomic, since $\upgamma$ is max., PV curve will be most steep.
And for polyatomic, since $\upgamma$ is min., PV curve will be least steep. But still steeper than isotherm.

![[Pasted image 20240213192521.png]]

##### Comparison between Adiabatic and Isothermal 
In isothermal,
$$\frac{ dP }{ dV } = - \frac{ P }{ V }$$
In adiabatic,
$$\frac{ dP }{ dV } = - \frac{ \upgamma P }{ V }$$

Thus,
$$\ce{ slope_{a} = \upgamma\ slope_{i} }$$
Since $\upgamma > 1$, slope of adiabatic is more than that of isothermal.

![[Pasted image 20240213185734.png]]
![[Pasted image 20240213192207.png]]

##### Relation between T and V 
$$
\begin{split}
PV^{\upgamma} &= \text{const.} \\
\frac{ nRT }{ V } V^{\upgamma} &= \text{const.} \\
TV^{\upgamma-1} &= \text{const.}
\end{split}
$$

![[Pasted image 20240213192800.png]]

##### Relation between P and T 
$$
\begin{split}
PV^{\upgamma} &= \text{const.} \\
P \left( \frac{ nRT }{ P } \right)^{\upgamma} &= \text{const.} \\
P^{1-\upgamma}T^{\upgamma} &= \text{const.} \\
PT^{\ \upgamma/1-\upgamma} &= \text{const.}
\end{split}
$$

Here,
$$\frac{ dP }{ dT } = \frac{ \upgamma }{ \upgamma-1 } \frac{ P }{ T } > 0$$
Thus the graph will be increasing. 

![[Pasted image 20240213193202.png]]

##### Work Done 
This is just like polytrophic process, just that instead of a, here it is $\upgamma$.

$$W = \frac{ nR\Delta T }{ 1-\upgamma }$$
$$W = \frac{ \Delta PV }{ 1-\upgamma }$$

Also, we know that,
$$
\begin{split}
W &= -\Delta U \\
&= -nC_{V}\Delta T \\
&= - \frac{ nR\Delta T }{ \upgamma-1 } \\
&= \frac{ nR\Delta T }{ 1 - \upgamma } \\
&= \frac{ \Delta(PV) }{ 1 - \upgamma }
\end{split}
$$

##### Example 
![[Pasted image 20240213200833.png]]
![[Pasted image 20240213200935.png]]
![[Pasted image 20240213200948.png]]