Links: [[01 Linear Expansion]]
___
# Thermal Expansion 
When we give heat to a gas, the change in volume is drastic. 
Similarly, when we give heat to a solid or a liquid, it also expands, although the change is not much. 

Solids also expand and contract with temp., but the shape will be the same. I.e. there will be photographic enlargement. 

On increasing temp., separation between any pair of points on the object will increase.

### [[01 Linear Expansion]]

### Areal or Superficial Expansion 
At temp. $T_{o}$, the area is,
$$A_{o} = l_{o}b_{o}$$

At temp. $T_{o} + \Delta T$, the new area is,
$$
\begin{split}
A &= l_{o}b_{o}(1+\alpha \Delta T)^{2} \\
&= A_{o} (1 + 2\alpha \Delta T) \\
&= A_{o}(1 + \beta \Delta T)
\end{split}
$$
Where, $\beta$ is called *coefficient of areal expansion,*
$$\beta = 2\alpha$$

Change in area is,
$$\Delta A = A_{o}\beta \Delta T$$

Fractional change in area is,
$$\frac{ \Delta A }{ A_{o} } = \beta \Delta T$$

![[Pasted image 20240213211216.png]]

### Volumetric Expansion 
At temp. T, the volume is,
$$V_{o} = l_{o}b_{o}h_{o}$$

At temp. $T + \Delta T$, the new volume is,
$$
\begin{split}
V &= l_{o}b_{o}h_{o}(1 + \alpha \Delta T)^{3} \\
&= V_{o}(1 + 3\alpha \Delta T) \\
&= V_{o}(1 + \upgamma \Delta T)
\end{split}
$$
where $\upgamma$ is called *coefficient of volumetric expansion,*
$$\upgamma = 3\alpha$$

![[Pasted image 20240213211400.png]]

![[Pasted image 20240214092605.png]]
![[Pasted image 20240214093054.png]]

#### Variation of Density with Temp.
Since as temp. increases, V increases and m is the same, density will decrease. 

At temp. T, the density of the object is,
$$\rho_{o} = \frac{ m }{ V_{o} }$$

At temp $T + \Delta T$, the density is,
$$
\begin{split}
\rho &= \frac{ m }{ V } \\
&= \frac{ m }{ V_{o}(1+\upgamma \Delta T) } \\
&= \frac{ \rho_{o} }{ 1 + \upgamma \Delta T }
\end{split}
$$

Using binomial approximation,
$$\rho = \rho_{o}(1 - \upgamma \Delta T)$$

![[Pasted image 20240214093413.png]]

#### Variation of Buoyancy force with Temp.
##### Solid completely Immersed in Liquid
At temp. T, the buoyancy force is,
$$
\begin{split}
f_{bo} &= m_{l}g \\
&= \sigma V_{o}g
\end{split}
$$

At temp. $T + \Delta T$, the new buoyancy force is,
$$
\begin{split}
f_{b} &= m_{l}'g \\
&= \sigma' V g \\
&= \frac{ \sigma }{ 1 + \upgamma_{l}\Delta T } V_{o} (1 + \upgamma_{s}\Delta T) g \\
&= f_{bo} \cdot \frac{ 1 + \upgamma_{s}\Delta T }{ 1 + \upgamma_{l}\Delta T } \\
&\approx f_{bo}[1 + (\upgamma_{s} - \upgamma_{l})\Delta T]
\end{split}
$$

![[Pasted image 20240214094442.png]]

##### Solid Floating in Liquid 
At T temp., the buoyancy force,
$$f_{bo} = mg$$


At $T + \Delta T$ temp., if the solid is still floating,
$$
\begin{split}
f_{b} &= mg \\
&= f_{bo}
\end{split}
$$

On changing temp., $f_{b}$ will remain unchanged and will be equal to the weight of solid. 

However, the volume inside will change,
Initially,
$$f_{bo} = (V_{in})_{o} \sigma g$$

At increased temp,
$$
\begin{split}
f_{b} &= V_{in} \sigma' g \\
(V_{in})_{o}\sigma &= V_{in}\sigma' \\
&= V_{in} \frac{ \sigma }{ 1 + \upgamma_{l} \Delta T } \\
V_{in} &= (V_{in})_{o} (1 + \upgamma_{l} \Delta T)
\end{split}
$$

![[Pasted image 20240214095322.png]]

### Variation of Density of Water with Temp.
For water, between $\ce{ 0^{\circ}C - 4^{\circ}C }$, the $\upgamma$ is -ve. 

This means that as we increase temp., volume will decrease and thus density increases. 

Between $\ce{ 4^{\circ}C - 100^{\circ}C }$, the $\upgamma$ becomes +ve again and thus water behaves like other normal liquids.

![[Pasted image 20240214095605.png]]