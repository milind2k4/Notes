Links: [[01 Deviation from Ideal Gas]]
___
# Real Gas
#removed from jee 24

Every gas that exists is a real gas. 

Actual gases are all real and do not follow ideal gas laws e.g. Boyle's Law, Charles' Law etc., in most P and T conditions. 

However, real gases show very close to the ideal behaviour at low P and high T conditions. 
But, real gases show high deviation from ideal behaviour in high P and low T conditions.

## Virial Equation of State
A general equation of state. 

A real gas can be represented as,
$$Z = \frac{ PV_{m} }{ RT } = 1 + \frac{ B }{ V_{m}^{2} } + \frac{ D }{ V_{m}^{3} } + \dots$$
where B, C, D ... are called 2nd, 3rd, 4th... virial coefficient. 

The second one is most important. 

### Determination of Virial Coefficients
in terms of [[02 VdW's Equation of State|Van Der Waals' constants a and b.]] 

$$
\begin{split}
\left( P + \frac{a}{V_{m}^{2}} \right)(V_{m} - b) &= RT 
\\
P &= \frac{ RT }{ (V_{m} - b) } - \frac{ a }{ V_{m}^{2} }
\\
\frac{ PV_{m} }{ RT } &= \frac{ V_{m} }{ (V_{m} - b) } - \frac{ a }{ RTV_{m} }
\\
Z &= \frac{ 1 }{ 1 - b /V_{m} } - \frac{ a }{ RTV_{m} } 
\\
Z &= \left( 1 - \frac{b}{V_{m}} \right)^{-1} - \frac{ a }{ RTV_{m} } 
\\
Z &= \left( 1 + \frac{ b }{ V_{m} } + \frac{ b^{2} }{ V_{m}^{2} } + \frac{ b^{3} }{ V_{m}^{3} } \dots  \right) - \frac{ a }{ RTV_{m} } \\
\\
Z &= 1 + \frac{ b - a /RT }{ V_{m} } + \frac{ b^{2} }{ V^{2} } + \frac{ b^{3} }{ V_{m}^{3} }
\end{split}
$$

On comparing this with Virial Equation,
**$$B = b - \frac{a}{RT}$$** $$C = b^{2}$$
$$D = b^{3}$$

## Law of Corresponding States
(aka **Reduced equation of state**)

Dimensionless reduced parameters, $P_{r}, V_{r}, T_{r}$ are defined. 

Reduced pressure,
$$P_{r} = \frac{ P }{ P_{c} }$$
Reduced volume,
$$V_{r} = \frac{ V_{m} }{ V_{c} }$$
Reduced temperature,
$$T_{r} = \frac{ T }{ T_{c} }$$

Putting the terms P, V and T in Van der Waal's equation in terms of reduced and critical terms,

![[Pasted image 20230515214947.png]]

Thus **Reduced Equation of State,**
$$\left( P_{r} + \frac{ 3 }{ V_{r}^{2} } \right)(2V_{r}-1) = 8T_{r}$$

Law of Corresponding state, says that if two real gases have same values of $V_{r}, P_{r}$ then their $T_{r}$ values will also be the same. 

An example,
![[Pasted image 20230515220117.png]]

## Liquefaction of Gases
Andrew's Isotherms 
Critical constants: $T_{c}, P_{c}, V_{c}$

In general, liquefaction  is caused by applying pressure and lowering T. 

Andrew performed med experiment to liquify $\ce{ CO_{2} }$

He took a glass vessel and used a piston to pressurise it. This caused liquification of the gas. 

![[Pasted image 20230515200607.png]]

The left point (B for example) liquification starts. Between D and B, there will be both liquid and gas. After D, the gas is liquified. And since liquids are incompressible, we have to apply a lot of pressure for a little change in volume. 

As we increase temperature, liquification becomes harder. 

![[Pasted image 20230515200523.png]]
(T increases as we move up in graph)
(the dotted line represents phase boundary)

Van Der Waal's equation is applicable in liquid and vapour phase but not on the liquid and vapour phase. 

**Critical Temperature ($T_{c}$):** the max. T at which liquefaction occurs. Beyond this T, no liquefaction can occur. 

**Critical Pressure ($P_{c}$):** the min. P required to cause liquefaction at $T_{c}$.

**Critical Pressure ($V_{c}$):** the molar volume of substance at critical point. 

*Critical Point and critical constants ($P_{c}, T_{c}, V_{c}$) are characteristic properties of every substance. They are constant for a substance.*

At critical point there is no distinction between liquid and gas. The density of gas is said to be that of liquid at that point. A substance at critical point is called **Critical Fluid**. 

When $T>T_{c}$ substance at high P is called **Supercritical Fluid.** Density of fluid is greater than density of liquid. 

**Vapour** is used when $T < T_{c}$. 
**Gas** is used when $T > T_{c}$. 
Thus, vapour can be converted into liquid by application of pressure alone, but not gas.  