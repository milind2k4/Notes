Links: [[00 Indefinite Integration]]
___
# Trigonometric Integrals

##### $\displaystyle \frac{ 1 }{ a\sin ^{2} x + b \cos^{2} x + c\sin x\cos x + d }$
Multiply numerator and denominator by $\sec^{2}x$ and then substitute $\tan x = t$. Then it will become $\frac{ dt }{ Q(t) }$.

Also, here any of a, b, c, d can be zero. 

![[Pasted image 20230930100341.png]]

##### $\displaystyle \frac{ 1 }{ a\sin x + b\cos x + c }$
Substitute $\sin x = \displaystyle \frac{ 2\tan \frac{x}{2} }{ 1 + \tan ^{2} \frac{ x }{ 2 } }$ and $\cos x = \displaystyle \frac{ 1 - \tan ^{2} \frac{x}{2} }{ 1 + \tan ^{2} \frac{ x }{ 2 } }$ and then put $\tan \frac{x}{2} = t$. 

This will again convert integral into $\frac{dt}{Q(t)}$.

![[Pasted image 20230930100546.png]]

##### $\displaystyle \frac{ a_{1}\sin x + b_{1}\cos x + c_{1} }{ a_{2}\sin x + b_{2}\cos x + c_{2} }$
Express, 
$$\ce{ Num = k_{1}(Deno) + k_{2}(Denom)' + k_{3} }$$
Then it can be integrated using substitution and the previous method. 

![[Pasted image 20230930100800.png]]

##### $\sin ^{n}x, \cos ^{n}x, \sin ^{m}x \cdot \cos ^{n}x$
If odd exponent is available, then substitute other term = t. 
i.e. if odd power is present on cos, then put sin = t.

![[Pasted image 20230930101154.png]]
![[Pasted image 20230930101358.png]]

If only even powers are present, then we use trigonometric identities i.e. $\cos 2A, \sin 2A, \sin A\cos B, \cos A\cos B$ etc. 

![[Pasted image 20230930101913.png]]

##### $\tan ^{n}x$
Convert one $\tan ^{2}x$ into $\sec^{2} x$ and keep repeating. 

![[Pasted image 20230930102118.png]]
![[Pasted image 20230930102328.png]]

##### $\tan ^{n} x \cdot \sec^{m}x$
Try, $\tan x = t\ or\ \sec x = t$
Otherwise use [[03 Integration by Parts|by parts.]]

![[Pasted image 20230930102808.png]]
![[Pasted image 20230930102818.png]]

![[Pasted image 20230930103130.png]]

##### If exponents of sin and cos are fractions or -ve
We try substitution $\tan x = t$. 

![[Pasted image 20230930103815.png]]
![[Pasted image 20230930103824.png]]

##### $\sin 2x$ related questions 
Some things to note are:
1. $\sin 2x = (\sin x + \cos x)^{2} - 1 = 1 - (\sin x - \cos x)^{2}$
2. $(\sin x - \cos x)' = \cos x + \sin x$
    $(\sin x + \cos x)' = \cos x - \sin x$
   

![[Pasted image 20230930104139.png]]
![[Pasted image 20230930104213.png]]

![[Pasted image 20230930104616.png]]


##### $\sqrt{ a\tan ^{2}x + b }\ or\ \sqrt{ p\sec^{2} x + q}$

$$
\begin{split}
\sqrt{ a\tan ^{2}x + b } &= \frac{ a\tan ^{2}x + b }{ \sqrt{ a\tan ^{2}x + b } } \\
&= \frac{ a\sec^{2}x }{ \sqrt{ a\tan ^{2}x + b } } + \frac{ (b-a) }{ \sqrt{ a\tan ^{2}x + b } } 
\end{split}
$$
In the first substitute $\tan x = t$ and in the second $\sin x = z$

![[Pasted image 20230930105444.png]]

##### $\tan(a + b)\tan (a) \tan (b)$
I.e. product of 3 tans where one of the angles is the sum of the other 2 or difference of the other 2. 

We will use,
$$tan(a + b)\tan (a) \tan (b) = tan(a + b) - \tan (a) - \tan (b)$$

![[Pasted image 20230930110336.png]]

#### Misc. Examples 
![[Pasted image 20230930112014.png]]




