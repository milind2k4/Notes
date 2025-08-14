Links: [[00 Indefinite Integration]]
___
# Algebraic Integrals

##### $\displaystyle \frac{L_{1}}{L_{2}}, \frac{ L_{1} }{ \sqrt{ L_{2} } }, L_{1}\sqrt{ L_{2} }$
Write, $L_{1}= kL_{2} + k_{1}$
I.e. express numerator in terms of denominator.

![[Pasted image 20230928193043.png]]

##### $\displaystyle \frac{ \sqrt{ L_{1} } }{ L_{2} }, \frac{ 1 }{ L_{2}\sqrt{ L_{1} } }$
Put, $L_{1}= t^{2}$
I.e. substitute such that the root is removed. 

![[Pasted image 20230928193613.png]]

##### $\displaystyle \frac{ L }{ Q }, \frac{ L }{ \sqrt{ Q } }, L\sqrt{ Q }$
Write, $L = kQ' + k_{1}$
I.e. express linear in terms of derivative of quadratic.

![[Pasted image 20230928193758.png]]

##### $\displaystyle \frac{1}{L\sqrt{ Q }}$
$\text{Put, } L = \frac{1}{t}$
Doing this will create quadratic in terms of t in the denominator. This can be integrated using [[00.5 Standard Formulae#Quadratic and Roots]].

![[Pasted image 20230928194335.png]]

##### $\displaystyle \frac{ Q_{1} }{ Q_{2} }, \frac{ Q_{1} }{ \sqrt{ Q_{2} } }$
Express $Q_{1} = k_{1}Q_{2} + k_{2}Q_{2}' + k_{3}$

![[Pasted image 20230928195543.png]]

##### If 2 linear expressions are involved
We can try the substitution, 
$$\frac{L_{1}}{L_{2}} = t $$
If we write x in terms of t, it will also come out to be linear upon linear. 

Differentiating linear upon linear will give constant upon square of denominator i.e. $k /(L_{2})^{2}$.

![[Pasted image 20230928200043.png]]

##### If Denominator contains a high exponent of Linear,
We can try substituting,
$$L = \frac{1}{t}$$

![[Pasted image 20230928202940.png]]

##### $\displaystyle \frac{ 1 }{ (ax^{2}+b)\sqrt{ cx^{2}+d } }$

$$
\begin{split}
\text{Take } x^{2} \text{ common, }& \frac{ \displaystyle  \frac{1}{x^{3}} }{ \displaystyle \left( a + \frac{b}{x^{2}} \right) \sqrt{ c + \frac{d}{x^{2}} } } \\
\\
\text{Then put, }& c + \frac{d}{x^{2}} = t^{2}
\end{split}
$$

![[Pasted image 20230928203417.png]]


##### $\displaystyle \frac{ P(x) }{ x^{4}+kx^{2}+1 }$
#important 
$P(x)$ can be $x^{2} \pm 1, x^{2}, 1$. i.e. only even powers.

We will take $x^{4}$ common and then use,
$$\begin{split}
x^{2} + \frac{1}{x^{2}} &= \left( x+\frac{1}{x} \right)^{2} - 2 \\ \\
x^{2} + \frac{1}{x^{2}} &= \left( x - \frac{1}{x} \right)^{2} + 2 \\ \\
\left( x - \frac{1}{x} \right)' &= 1 + \frac{1}{x^{2}} \\ \\
\left( x + \frac{1}{x} \right)' &= 1 - \frac{1}{x^{2}} \\
\\
1 &= \frac{ 1 }{ 2 } \left( \left( 1 + \frac{ 1 }{ x^{2} } \right) + \left( 1 - \frac{ 1 }{ x^{2} } \right) \right) \\
\frac{ 1 }{ x^{2} } &= \frac{ 1 }{ 2 } \left( \left( 1 + \frac{ 1 }{ x^{2} } \right) - \left( 1 - \frac{ 1 }{ x^{2} } \right) \right)
\end{split}$$

Using this we can integrate $\sqrt{ \tan x }$,
![[Pasted image 20230928204547.png]]

![[Pasted image 20230928205227.png]]

#### Misc. Examples


**If $x+ \sqrt{ x^{2}+a^{2} }$ is involved,**
$$\begin{split}
x + \sqrt{ x^{2}+a^{2} } &= t \\ 
\sqrt{ x^{2}+a^{2} } &= t - x \\ 
x^{2}+a^{2} &= t^{2} + x^{2} - 2tx \\ 
x &= \frac{1}{2}\left( t - \frac{a^{2}}{t} \right) \\ 
& \text{Put this back into expression.}
\end{split}$$

![[Pasted image 20230928205725.png]]

If numerator and denominator contains algebraic expressions then we can try generating $f'$ in the numerator by shifting some terms from denominator to numerator. 

![[Pasted image 20230928210150.png]]

![[Pasted image 20230928210902.png]]
![[Pasted image 20230928211110.png]]

![[Pasted image 20230930112032.png]]

