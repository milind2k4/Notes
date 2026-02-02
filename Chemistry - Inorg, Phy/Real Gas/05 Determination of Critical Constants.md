Links: [[02 VdW's Equation of State]]
___
# Determination of Critical Constants in terms of a and b
Slope of P vs $V_{m}$ is zero at the critical point. 

$$\left. \frac{ dP }{ dV_{m} } \right|_{T = T_{c}} = 0$$

The slope is also the max at this point,
$$\left. \frac{ d^{2}P }{ dV_{m}^{2} } \right|_{T = T_{c},\ P} = 0$$

Using Van der Waal's equation,
$$
\begin{split}
\left( P + \frac{ a }{ V_{m}^{2} } \right)(V_{m} - b) &= RT \\
P &= \frac{ RT }{ V_{m}-b } - \frac{a}{V_{m}^{2}} \\
\left( \frac{ dp }{ dV }  \right)_{T} &= \frac{ -RT }{ (V_{m}-b)^{2} } + \frac{ 2a }{ V_{m}^{3} } \\
\\
\left( \frac{ d^{2} P }{ d V_{m}^{2} }  \right)_{T} &= \frac{ 2RT }{ (V_{m}-b)^{3} } - \frac{ 6a }{ V_{m}^{4} } \\
\\
\text{At critical point, } & \\
\frac{ RT_{c} }{ (V_{c}-b)^{2} } &= \frac{ 2a }{ V_{c}^{3} } \dots (1) \\
\\
\frac{ 2RT }{ (V_{m}-b)^{3} } &= \frac{ 6a }{ V_{m}^{4} } \dots (2) \\
\\
\text{Divinding them,} & \\
\frac{ V_{c} - b }{ 2 } &= \frac{ V_{c} }{ 3 } \\
V_{c} &= 3b \\
\\
\text{Putting this in (1),} & \\
T_{c} &= \frac{ 8a }{ 27Rb } \\
\end{split}
$$

Using Van der Waal's equation at critical point and putting the values of $T_{c}, V_{c}$,
$$
\begin{split}
\left( P_{c} + \frac{ a }{ V_{c}^{2} } \right)(V_{c} - b) &= RT_{c} \\
\\
\left( P_{c} + \frac{ a }{ 9b^{2} } \right)(3b - b) &= R \frac{ 8a }{ 27b } \\
\\
P_{c} &= \frac{ a }{ 27b^{2} }
\end{split}
$$

Thus, critical constants are,
$$
\begin{split}
P_{c} &= \frac{a}{27b^{2}} \\
V_{c} &= 3b \\
T_{c} &= \frac{ 8a }{ 27Rb }
\end{split}
$$

Compressibility factor at critcal point,
$$
\begin{split}
P_{c}V_{c} &= Z_{c} \times RT_{c} \\
\frac{ a }{ 27b^{2} } 3b &= Z_{c} \times R \frac{ 8a }{ 27Rb } \\
Z_{c} &= \frac{ 3 }{ 8 } < 1
\end{split}
$$

Thus, 
$$Z_{c} = \frac{3}{8} < 1$$
and thus we can say that attractive forces are dominant at critical point. 

For every Van Der Waal's gas, Z at critical point is a constant value.  

Higher is $T_{c}$ greater will be the liquifiability and compressibility of the gas, as $a$ is the measure of attractive forces. 
In general, molar mass $\uparrow$, $a \uparrow$, (except $\ce{ H_{2}, He }$ where it is opposite), for non polar gases. 

Increasing a and hence $T_{c}$ value,
$$\ce{ He < Ne < Ar < Kr < Xe }$$
$$\ce{ F_{2} < Cl_{2} < Br_{2} < I_{2} }$$
$$\ce{ a_{He} < a_{H_{2}} }$$
a value is lowest for He. 

For comparison of a value between polar and non polar molecules, a is higher for polar for nearly same molar mass. 

$$\ce{ CH_{4} < NH_{3} < H_{2}O }$$
as water is more polar. 

### Alternative Derivation of Critical Constants
We convert the Van der Waal's equation into a cubic in $V_{m}$ and then use the fact that all three roots of that will be the same and equal to $V_{c}$

![[Pasted image 20230515213132.png]]

Comparing coefficients,
![[Pasted image 20230515213310.png]]

#### Roots of Vander Waal's Equation
All three roots of $V_{m}$ are equal and real at critical point. All three are real and distinct below $T_{c}$. Only one root is real when $T > T_{c}$.

![[Pasted image 20230515213931.png]]
