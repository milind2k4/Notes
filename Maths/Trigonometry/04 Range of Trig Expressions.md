Links: [[03 T ratio of Sum and Difference of 2 Angles]]
___
# Range of Trig Expressions
#formula 

## Range of $a \sin x + b \cos x$
> $$\begin{split}
> 
> a \sin x + b \cos x &= \sqrt{a^{2}+b^{2}} \left( \frac{a}{\sqrt{a^{2}+b^{2}}} \sin x + \frac{b}{\sqrt{a^{2}+b^{2}}} \cos x \right) \\\\
> 
> &= \sqrt{a^{2}+b^{2}} ( \cos \alpha \sin x + \sin \alpha \cos x) \\\\
> 
> As\ & \left( \frac{a}{\sqrt{a^{2}+b^{2}}} \right)^{2} + \left( \frac{b}{\sqrt{a^{2}+b^{2}}} \right)^{2} = 1 \\\\
> 
> \text{We can take, } & \cos \alpha = \frac{a}{\sqrt{a^{2}+b^{2}}} \ \&\ \sin \alpha = \frac{b}{\sqrt{a^{2}+b^{2}}}  \\\\
> 
> \text{Thus, } & \\\\
> 
> a \sin x + b \cos x &= \sqrt{a^{2}+b^{2}}\ \sin (\alpha + x) \\\\
> 
> \text{When, }& \sin \alpha = \frac{b}{\sqrt{a^{2}+b^{2}}} \ \& \ \cos \alpha = \frac{a}{\sqrt{a^{2}+b^{2}}} \\\\
> 
> or\ &= \sqrt{a^{2}+b^{2}}\ \cos (\alpha - x) \\\\
> 
> \text{When, }& \cos \alpha = \frac{b}{\sqrt{a^{2}+b^{2}}} \ \& \ \sin \alpha = \frac{a}{\sqrt{a^{2}+b^{2}}} \\\\
> \\
> \text{Thus,} & \\\\
> 
> a \sin x + b \cos x &\in \left[ -\sqrt{a^{2}+b^{2}}, \sqrt{a^{2}+b^{2}} \right]
> \end{split}$$

We can use this to manipulate expressions given as a sum of $\sin$ and $\cos$ and convert them into $\sin (\alpha + x)$ or $\cos (\alpha -x)$

Example,
![[Pasted image 20230502074300.png]]

### Some other Important Expressions
$$\begin{split}
\sin x + \cos x &= \sqrt{2} \left( \frac{1}{\sqrt{2}}\sin x + \frac{1}{\sqrt{2}}\cos x \right) \\\\
&= \sqrt{2}\ ( \cos 45 \sin x + \sin 45 \cos x ) \\\\
&= \sqrt{2}\ \sin (45 + x) \\\\
&= \sqrt{2}\ \cos (45 - x)
\end{split}$$

Similarly,
$$\sin x - \cos x = \sqrt{2}\ \sin (45 - x)$$
$$\phantom{\sin x - \cos x} = \sqrt{2}\ \cos (45 + x)$$
$$-\sin x + \cos x = \sqrt{2}\ \sin (x-45)$$
$$\phantom{-\sin x + \cos x} = -\sqrt{2}\ \cos (x+45)$$

And,
$$\sin x \pm \cos x,\ \cos x - \sin x \in \left[ -\sqrt{2}, \sqrt{2} \right] $$