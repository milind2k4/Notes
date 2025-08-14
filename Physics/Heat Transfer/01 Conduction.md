Links: [[00 Current Electricity]], [[00 Heat Transfer]]
___
# Conduction
Medium is required. 
There will be no heat transfer if the medium is discontinuous. 

There is no net displacement of medium particles. 

#### Thermal Current
Aka Heat Current.

Similar to [[00 Current Electricity|electric current]], it is rate of flow of heat. 

![[Pasted image 20231221193458.png]]

$$i_{th(avg)} = \frac{ \Delta Q }{ \Delta t }$$
$$i_{th} = \frac{ dQ }{ dt } $$

Its unit is J/s = Watt. 

It has a direction but it is a scalar because it follows scalar algebra. The direction is from the higher temp to lower temp. 

![[Pasted image 20231221193544.png]]

**Energy Flux** is $\displaystyle \frac{i}{A}$


#### Steady State 
When the whole rod has the same thermal current.

Since the amount of current coming in is the same as that going out,
$$\frac{ dT }{ dt } = 0$$
I.e. at any point, T does not change with time.

But T is non uniform as it is a function of position. 

![[Pasted image 20231221193718.png]]

#### Non Steady State 
When the current at any two points is not the same. 

If $i_{1} > i_{2}$,
$$
\begin{split}
(i_{1} - i_{2}) &= \frac{ dQ }{ dt } \\
&= ms\frac{ dT }{ dt } \\
\frac{ dT }{ dt } &> 0
\end{split}
$$

Thus the temp. will increase with time.

![[Pasted image 20231221194007.png]]

#### Temperature Gradient
The change in temperature per unit distance. 

It is always negative in the direction of the thermal current.

$$\frac{ dT }{ dx } = \frac{ T_{L} - T_{H} }{ l - 0 }$$

Its unit is $\ce{ ^{\circ}C/m = K/m }$

![[Pasted image 20231221194336.png]]

## Ohm's Law
[[01 Ohm's Law]]

$$\begin{split}
i_{th} &\propto (T_{H} - T_{L}) \\
&\propto A \\
&\propto \frac{1}{l} 
\end{split}$$

Thus,
$$i_{th} = \frac{ kA(T_{H} - T_{L}) }{ l } = -kA \frac{ dT }{ dx } $$

k is called **Thermal Conductivity** and is a property of medium. 
If a medium is good conductor, it will have high k.

It's unit is $\ce{ W/mK }$ and dimensions are $\ce{ [MLT^{-3}K^{-1}] }$.

### Thermal Resistance
[[04 Equivalent Resistance]]

Rearranging the formula for thermal current,
$$i_{th} = \frac{ T_{H} - T_{L} }{ (l / kA) }$$
Comparing this to $i = V/R$
Thus, we get thermal resistance,
$$R_{th} = \frac{ l }{ kA }$$
Its unit is $\ce{ ^{\circ}C/W = K/W }$. 

Thus thermal current becomes,
$$i_{th} = \frac{ T_{H} - T_{L} }{ R_{th} }$$

Example,
![[Pasted image 20231221204222.png]]
![[Pasted image 20231221204228.png]]

## Kirchhoff's Current Law
[[03 Kirchhoff's Laws#Current Law (Junction Law)]]

$$i_{1} = i_{2} + i_{3}$$
At any junction,
$$\sum i = 0$$

Example,
![[Pasted image 20231221201226.png]]
![[Pasted image 20231221201238.png]]

## Combination of Rods
Just like [[04 Equivalent Resistance]]

### Series Combination
The rods are connected end to end.

$$R_{eq} = R_{1} + R_{2} = \frac{ l_{1} }{ k_{1}A } + \frac{ l_{2} }{ k_{2}A }$$

Temp. of the junction,
$$
\begin{split}
i_{th} &= \frac{ T_{H} - T_{L} }{ R_{1} + R_{2} } \\
&= \frac{ T_{H} - T }{ R_{1} } \\
&= \frac{ T - T_{L} }{ R_{2} } 
\end{split}
$$

Thus giving,
$$T = \frac{ T_{H}R_{2} + T_{L}R_{1} }{ R_{1} + R_{2} }$$

To find $k_{eq}$,
$$
\begin{split}
\frac{ l_{1} }{ k_{1}A } + \frac{ l_{2} }{ k_{2}A } &= \frac{ l_{1} + l_{2} }{ k_{eq}A } \\
\frac{ l_{1} }{ k_{1} } + \frac{ l_{2} }{ k_{2} } &= \frac{ l_{1} + l_{2} }{ k_{eq} }
\end{split}
$$

![[Pasted image 20231221201521.png]]

### Slabs in Parallel
The temperature difference should be same across all the rods. 
Just like electric current, thermal current also choses path of least resistance. 

Equivalent Resistance,
$$\frac{ 1 }{ R_{eq} } = \frac{1}{R_{1}} + \frac{1}{R_{2}}$$

And thus giving,
$$
\begin{split}
i_{1} &= \frac{ T_{H} - T_{L} }{ R_{1} } \\
i_{2} &= \frac{ T_{H} - T_{L} }{ R_{2} } 
\end{split}
$$

$$\frac{ i_{1} }{ i_{2} } = \frac{ R_{2} }{ R_{1} }$$
I.e. current will be inversely proportional to the resistance.

Equivalent Thermal Conductivity,
$$
\begin{split}
\frac{ k_{eq}(A_{1} + A_{2}) }{ l } &= \frac{ k_{1}A_{1} }{ l } + \frac{ k_{2}l_{2} }{ l } \\
k_{eq} &= \frac{ k_{1}A_{1} + k_{2}A_{2} }{ A_{1} + A_{2} }
\end{split}
$$

![[Pasted image 20231221203040.png]]

Example,
![[Pasted image 20231221203405.png]]

