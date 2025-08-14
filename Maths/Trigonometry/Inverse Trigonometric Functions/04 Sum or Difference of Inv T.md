Links: [[00 Inverse Trigonometric Functions]], [[03 Formulae Related to Inv-T]]
___
# $T^{-1}(x) \pm T^{-1}(y)$
#formula , #important

(Make $x,y > 0$)

Let, $T^{-1}(x) = A\ \&\ T^{-1}(y) = B$

Now, 
$$A \in \left( 0, \frac{\pi}{2} \right)$$
$$B \in \left( 0,\frac{\pi}{2} \right)$$
$$-B \in \left( -\frac{\pi}{2}, 0 \right)$$


Then,
$$0 < A+B < \pi$$
i.e.,
$$0 < T^{-1}(x) + T^{-1}(y) < \pi$$

Similarly,
$$\frac{-\pi}{2} < A-B < \frac{\pi}{2}$$
i.e.,
$$\frac{-\pi}{2} < T^{-1}(x) - T^{-1}(y) < \frac{\pi}{2}$$


Thus,
$\sin ^{-1}x + \sin ^{-1}y \to$ 2 definitions.
$\cos ^{-1}x + \cos ^{-1}y \to$ 1 definitions.
$\tan ^{-1}x + \tan ^{-1}y \to$ 2 definitions.

$\sin ^{-1}x - \sin ^{-1}y \to$ 1 definitions.
$\cos ^{-1}x - \cos ^{-1}y \to$ 2 definitions.
$\tan ^{-1}x - \tan ^{-1}y \to$ 1 definitions.

### Sum
For $x,y > 0$,
$$
\begin{split}
\sin ^{-1}x + \sin ^{-1}y &=  \sin ^{-1}(x\sqrt{ 1-y^{2} } + y\sqrt{ 1-x^{2} }),\ x^{2} + y^{2} \leq 1 \\
&= \pi - \sin ^{-1}(x\sqrt{ 1-y^{2} } + y\sqrt{ 1-x^{2} }), x^{2}+y^{2} > 1 \\
\\
\cos ^{-1}x + \cos ^{-1}y &= \cos ^{-1}(xy - \sqrt{ 1-x^{2} }\sqrt{ 1-y^{2} }) \\
\\
\tan ^{-1}x + \tan ^{-1}y &= \tan ^{-1}\left( \frac{ x+y }{ 1-xy } \right),\ xy < 1 \\
&= \pi + \tan ^{-1}\left( \frac{ x+y }{ 1-xy } \right),\ xy>1 \\
&= \frac{\pi}{2},\ xy = 1
\end{split}
$$

### Difference
For $x,y > 0$,
$$
\begin{split}
\sin ^{-1}x - \sin ^{-1}y &= \sin ^{-1}(x\sqrt{ 1-y^{2} } - y\sqrt{ 1-x^{2} }) \\
\\
\cos ^{-1}x - \cos ^{-1}y &= \cos ^{-1}(xy + \sqrt{ 1-x^{2} }\sqrt{ 1-y^{2} }),\ x \leq y \\
&= -\cos ^{-1}(xy + \sqrt{ 1-x^{2} }\sqrt{ 1-y^{2} }),\ x > y \\
\\
\tan ^{-1}x - \tan ^{-1}y &= \tan ^{-1}\left( \frac{ x-y }{ 1+xy } \right)
\end{split}
$$

### If x = y in Sum
$$
\begin{split}
2\sin ^{-1}x &= \sin ^{-1}(2x\sqrt{ 1-x^{2} }),\ x \leq \frac{ 1 }{ \sqrt{ 2 } } \\
&= \pi - \sin ^{-1}(2x\sqrt{ 1-x^{2} }),\ x > \frac{1}{\sqrt{ 2 }} \\
\\
2\cos ^{-1}x &= \cos ^{-1}(2x^{2}-1) \\
\\
2\tan ^{-1}x &= \tan ^{-1}\left( \frac{ 2x }{ 1-x^{2} } \right),\ x < 1 \\
&= \pi + \tan ^{-1}\left( \frac{ 2x }{ 1-x^{2} } \right),\ x > 1 \\
&= \frac{\pi}{2},\ x = 1
\end{split}
$$

### Proof of $\sin ^{-1}x + \sin ^{-1}y$
It will have 2 definitions as the principal value branch of sin is different than the addition. 


Let, 
$$\sin ^{-1}x = A \implies x = \sin A \implies \cos A = \sqrt{ 1-x^{2} }$$
$$\sin ^{-1}y = B \implies y = \sin B \implies \cos B = \sqrt{ 1-y^{2} }$$

Here,
$$
\begin{split}
&A,B \in \left( 0,\frac{ \pi }{ 2 } \right)\\
\text{Thus,} \\
& A + B \in (0, \pi)
\end{split}
$$

Consider,
$$\begin{split}
\sin A+B &= \sin A\cos B + \cos A \sin B \\ 
&= x\sqrt{ 1-y^{2} } + \sqrt{ 1-x^{2} }y \\ 
\\
\sin ^{-1}(\sin(A+B)) &= \sin ^{-1}(x\sqrt{ 1-y^{2} } + y\sqrt{ 1-x^{2} }) \\ 
\\
A+B &= \sin ^{-1}(x\sqrt{ 1-y^{2} } + y\sqrt{ 1-x^{2} }), A+B < \frac{\pi}{2} \\ 
\pi - (A+B) &= \sin ^{-1}(x\sqrt{ 1-y^{2} } + y\sqrt{ 1-x^{2} }), A+B \geq \frac{\pi}{2} \\ 
\end{split}$$
These two definitions come [[02 Combination of T and Inv T#$y = sin {-1}( sin x)$|from the two definitions]] of $\sin ^{-1}(\sin(x))$ between $0$ and $\pi$.

For condition in x and y,

$$\begin{split}
A + B &< \frac{\pi}{2} \\
A &< \frac{\pi}{2} - B\\
\sin A &< \sin\left( \frac{\pi}{2}-B \right) \\
\sin A &< \cos B \\
x &< \sqrt{ 1-y^{2} }\\
x^{2} &< 1-y^{2} \\
x^{2} + y^{2} &< 1
\end{split}$$


Therefore,
$$\begin{split}
x^{2}+y^{2} < 1:& \\
&\sin ^{-1}x + \sin ^{-1}y = \sin ^{-1}(x\sqrt{ 1-y^{2} } + y\sqrt{ 1-x^{2} }) \\ 
\\
x^{2}+y^{2} \geq 1:& \\
&\sin ^{-1}x + \sin ^{-1}y = \pi - \sin ^{-1}(x\sqrt{ 1-y^{2} } + y\sqrt{ 1-x^{2} }) 
\end{split}$$

Note:
Use this,
![[Pasted image 20221226131039.png|400]]



### Extra Results to remember
$$
\begin{split}
\tan ^{-1}1 + \tan ^{-1}2 + \tan ^{-1}3 &= \pi \\
\\
\cot ^{-1}1 + \cos ^{-1} \frac{1}{2} + \cot ^{-1} \frac{1}{3} &= \pi \\
\\
\cot ^{-1}1 + \cot ^{-1}2 + \cot ^{-1}3 &= \frac{\pi}{2} \\
\\
\tan ^{-1}1 + \tan ^{-1} \frac{1}{2} + \tan ^{-1} \frac{1}{3} &=  \frac{\pi}{2}
\end{split}
$$



### Example
If there are complicated expressions inside of $\cos ^{-1}$ or $\sin ^{-1}$, then we try to reverse convert them into sum or difference of $\cos ^{-1}$ or $\sin ^{-1}$ or convert it into $\tan ^{-1}$.

![[Pasted image 20230606094148.png]]

