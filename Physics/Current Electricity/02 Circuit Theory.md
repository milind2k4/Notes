Links: [[01 Ohm's Law]]
___
# Circuit Theory
#### Electrical Power 
[[04 Power]]

It is the rate at which electrical energy is generated or consumed. 

$$P = \frac{ \text{electrical energy} }{ \text{time taken} }$$

#### Source
Element in the circuit which converts some form of energy into electrical energy. 

Current enters the source at low potential and exists at high potential. 

![[Pasted image 20231219180536.png]]

Let a charge $dq$ enter the source. 
This charge has energy,
$$U_{i} = (dq) . 0$$
When it exits, it has energy,
$$U_{f} = (dq).V$$

Energy gained,
$$dU = dq V$$

Thus power will be,
$$
\begin{split}
P &= \frac{ dU }{ dt } \\
&= \frac{ dq }{ dt } V \\
&= V\ i 
\end{split}
$$

Thus power in the circuit is,
$$P = V\ i$$
This is a universal formula.

#### Load 
It is an element in the circuit which converts electrical energy into some other form of energy. 

Currents enter at high potential and exits at high potential. 

![[Pasted image 20231219181234.png]]

Here too we can find power,
$$
\begin{split}
U_{i} &= dq V \\
U_{f} &= dq . 0 \\
\\
P &= \frac{ dq .V }{ dt } \\
&= V\ i
\end{split}
$$

### Electrical Power in Resistor
Resistor is always a load in a circuit. 

Power is given as,
$$
\begin{split}
P &= V i\\
&= i^{2} R \\
&= \frac{ V^{2} }{ R }
\end{split}
$$

If all this energy is dissipated in the form of heat,
$$
\begin{split}
dH &= Pdt \\
H &= \int i^{2}R \, dt \\
&= \int \frac{ V^{2} }{ R } \, dt 
\end{split}
$$

If power is constant,
$$H = Pt = i^{2} Rt = \frac{ V^{2}t }{ R }$$

#### Bulb
$$\text{Rating} \to (V,P)$$
It means that on applying a pd of V across it, it will use P watt power. 

Bulb can be considered a resistance in questions.

![[Pasted image 20231219182052.png]]

### Battery 
It is an element which produced constant potential difference. 

In general battery consumes chemical energy and converts it into electrical, and thus it acts as a source in general. 

Ideal battery has no internal resistance and thus it converts 100% of the chemical energy into electrical energy.

Non ideal battery has an internal resistance represented by $r$. It does not convert 100% of the chemical energy into electrical energy. 

![[Pasted image 20231219182531.png]]

When we go from the lower potential to the higher potential in a battery, the potential is increased and when we go from higher to lower, the potential is decreased. 

![[Pasted image 20231219221004.png]]

#### Battery as Source 
When battery is acting as source, the current will enter from lower potential.

Potential difference across a non ideal battery is,
$$V_{A} - V_{B} = \varepsilon - ir$$

![[Pasted image 20231219212445.png]]

Rate at which chemical energy is consumed,
$$\frac{ \varepsilon\ Q }{ t } = \varepsilon i$$

Rate at which internal resistance is wasting energy, $= i^{2} r$

Power output,
$$
\begin{split}
P_{out} &= \varepsilon i - i^{2}r \\
&= (\varepsilon - ir)i \\
&= (V_{A} - V_{B}) i
\end{split}
$$

Efficiency,
$$
\begin{split}
\eta &= \frac{ (\varepsilon - ir)i }{ \varepsilon i } \times 100 \\
&= \frac{ \varepsilon - ir }{ \varepsilon\ } \times 100
\end{split}
$$

![[Pasted image 20231219214145.png]]

Across a load, the output power is, out
$$
\begin{split}
P_{out} &= \frac{ \varepsilon^{2}R }{ (R + r)^{2} }
\end{split}
$$
Now this power is a function of R.
- If R = 0, $P_{out} = 0$.
- If $R \to \infty$, $P_{out} \to 0$

For $R = r$, $P_{out}$ will be max. 

Thus for maximum power transfer the load resistance of the battery should be equal to the internal resistance. 

![[Pasted image 20231219214507.png]]

#### Battery as Load
When battery is acting as load, current will enter from the higher potential.

Potential difference across the battery,

$$V_{A} - V_{B} = \varepsilon - ir$$

![[Pasted image 20231219213130.png]]

Rate at which electrical energy is consumed, 
$$\frac{ \varepsilon Q }{ t } = \varepsilon i$$

Rate at which energy is wasted $= i^{2} r$

Rate at which some source is providing energy,
$$
\begin{split}
P_{in} &= \varepsilon i + i^{2} r \\
&= (\varepsilon - ir) i \\
&= (V_{A} - V_{B}) i
\end{split}
$$

### Short Circuiting 
SC means touching two points in a circuit or connecting them with a zero resistance wire. 

Doing this makes the potential difference between them zero.

![[Pasted image 20231219213616.png]]


![[Pasted image 20231219214833.png]]
![[Pasted image 20231219215338.png]]