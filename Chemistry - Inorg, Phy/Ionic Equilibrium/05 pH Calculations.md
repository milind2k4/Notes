Links: [[04 Properties of Water]]
___
# pH calculation
### pH of Strong Acid or Strong Base Solution
The calculations are done while keeping [[02 Arrhenius Theory and Ostwald's Law#Factors Affecting Degree of Ionisation|Common Ion Effect]] in mind.
Thus $\ce{ [H+] < 10^{-7} }$

For monobasic acid like HCl,
![[Pasted image 20230622210020.png]]

$$
\begin{split}
x(x+c) &= k_{w} \\
x^{2} + cx - k_{w} &= 0 \\
x &= \frac{ -c + \sqrt{ c^{2} + 4k_{w} } }{ 2 }
\end{split}
$$
From here we can calculate total concentration of $\ce{ H+ }$ ion,
![[Pasted image 20230622210159.png]]

##### Approximations
1. If $\ce{ [H+] }$ from SA $\geq 10^{-6}$ M, then $\ce{ [H+] }$ contributed by water can be ignored. So, $x \ll c$ and this we can approximate, $x+c \approx c$,
	$$\ce{ [H+] = c + x \approx c }$$

1. If $10^{-8} \ce{ M\leq [H+]_{SA} < 10^{-6} M }$, then $\ce{ [H+] }$ contributed by water cannot be ignored. Now we have to solve quadratic to get x. And $\ce{ [H+] = x + c }$, the calculate pH.
	$\\$

3. If SA solution is very dilute, i.e. $\ce{ [H+]_{SA} < 10^{-8} }$, then $\ce{ [H+] }$ from strong acid can be ignored, and pH may be taken as 7 at 25$^{\circ}$C. 

The above cases are similarly applicable for strong bases. 

If the pH is between 6 and 8, the effect of water is significant,
![[Pasted image 20230623204909.png]]

### Mixture of SAs or SBs
Similar to finding concentration of ions in a mixture of ionic compounds in [[04 Concentration Terms#Mixing of Solution]].

Finally take -log to find pH. 

### [[05.5 Weak Monobasic Acid]]

### Mixture of two weak Monobasic acid or two weak monoacidic base

[[00 Chemical Equilibrium#Simultaneous Equilibrium|Simultaneous Equilibrium]] is used. 

![[Pasted image 20230623205124.png]]

##### Approximations
If $\alpha_{1}$ of HA and $\alpha_{2}$ of HB $\leq 0.1$ (when k is low and c is high),  $x \ll c_{1}$ and $y \ll c_{2}$ thus,
$$k_{a_{1}}. c_{1} = x(x+y)$$
$$k_{a_{2}}. c_{2} = y(x+y)$$
Adding them,
$$(x+y)^{2} = k_{a_{1}}c_{1} + k_{a_{2}}c_{2}$$
$$\ce{ [H+] = (x +y) = \sqrt{ k_{a_{1}}c_{1} + k_{a_{2}}c_{2} } }$$

And dividing we get,
$$x = \frac{ k_{a_{1}}c_{1} }{ \sqrt{ k_{a_{1}}c_{1} + k_{a_{1}}c_{2} } }$$
$$y = \frac{ k_{a_{2}}c_{2} }{ \sqrt{ k_{a_{1}}c_{1} + k_{a_{1}}c_{2} } }$$

Similarly for a mixture of two weak monoacidic bases, just instead of $\ce{ [H+] }$ we get $\ce{ [OH-] }$


We have to take care that the concentrations of acids and bases will change,
![[Pasted image 20230623210638.png]]

### Mixture of Weak Monobasic Acid and a Strong Acid
Similarly for mixture of weak base and strong base. 

![[Pasted image 20230623211613.png]]

$$
\begin{split}
k_{a} &= \frac{ x(a+c_{2}) }{ c_{1}-x } \\
x^{2} + c_{2}x &= c_{1}k_{a} - xk_{a} \\
x^{2} + (c_{2}+k_{a})x - c_{1}k_{a} &= 0
\end{split}
$$
If $k_{a} \ll c_{2},\ c_{2}+k_{a} \approx c_{2}$
$$
\begin{split}
x^{2} + c_{2}x - c_{1}k_{a} &= 0\\
x &= \frac{ -c_{2} + \sqrt{ c_{2}^{2} + 4c_{1}k_{a} } }{ 2 }
\end{split}
$$
If $4k_{a} c_{1} \ll c_{2}^{2},\ c_{2}^{2} + 4c_{1}k_{a}  \approx c_{2}^{2}$, giving,
$$x = \frac{ -c_{2} + c_{2} }{ 2 } \approx 0$$

Total concentration of $\ce{ [H+] }$,
$$\ce{ [H+] = x + c_{2} \approx c_{2} }$$
i.e. it is due to mainly due to strong acid. 

Example,
![[Pasted image 20230623213850.png]]

### Polybasic acid/Polyacidic base 
Polyacidic base like hydrazine ($\ce{ N_{2}H_{4} or N_{2}H_{6}(OH)2 }$)

Polybasic acids ionise in two steps, both with their own k,

![[Pasted image 20230625153731.png]]
$$k_{a_{1}} = \frac{ (x+y)(x-y) }{ c - x }$$
$$k_{a_{2}} = \frac{ (x+y)y }{ x-y }$$


This is again a case of Simultaneous Equilibrium.

##### Approximations
1. For a polyprotic acid, $k_{a_{1}} > k_{a_{2}} > k_{a_{3}} \dots$
   Thus $y \ll x$ and we can ignore y in addition. 
	$$k_{a_{1}} = \frac{ x^{2} }{ c - x }$$
	$$k_{a_{2}} = y = \ce{ [A^{2-}] }$$

2. If $\alpha_{1} = \sqrt{ \frac{ k_{a_{1}} }{ c } } <0.1$ then $x \ll c$ and can be ignored. 
	$$k_{a_{1}} = \frac{ x^{2} }{ c }$$
	$$x = \sqrt{ k_{a_{1}}.c } = \ce{ [H+] }$$
	$$pH = \frac{1}{2}(pk_{a_{1}} - \log c)$$
	Which is the same as that of weak monobasic acid. 
	
	From this we can draw conclusions,
	- This is applicable when $\alpha_{1} \leq 0.1$
	- For calculation of pH of a polybasic acid, only $k_{a_{1}}$ and c are required.

**Note:** for a polyacidic base,
$$\ce{ pOH = \frac{1}{2}(pk_{b_{1}} - \log c) }$$

Example,
![[Pasted image 20230625160128.png]]

### Special case of $\ce{ H_{2}SO_{4} }$
#important 

First ionisation is essentially compete, but 2nd ionisation is not complete though is high. 

![[Pasted image 20230625161629.png]]
$k_{a_{2}}$ is about 0.12.

This 2nd ionisation is 60 - 70% so x cannot be ignored relative to c. And thus we have to solve quadratic. 

if $k_{a_{2}}$ data is not given, then treat $\ce{ H_{2}SO_{4} }$ as strong acid (both ionisation).
