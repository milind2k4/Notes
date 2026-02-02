Links: 
___
# Theorems Derived from Sine and Cosine Law
### Napier's Analogy 
It is another form of sine law.

Consider,
$$
\begin{split}
\frac{ a - b }{ a + b } &= \frac{ \sin A - \sin B }{ \sin A + \sin B } \\
&= \frac{ 
2 \sin \left( \frac{ A - B }{ 2 } \right) \cos \left( \frac{ A+B }{ 2 } \right) 
}{ 
2 \sin \left( \frac{ A+B }{ 2 } \right) \cos \left( \frac{ A-B }{ 2 } \right) 
} \\
&= \frac{ \tan \left( \frac{ A-B }{ 2 } \right) }
{ \tan \left( \frac{ A+B }{ 2 } \right) } \\
&= \frac{ \tan \left( \frac{ A-B }{ 2 } \right) }
{ \cot \left( \frac{ C }{ 2 } \right) } 
\end{split}
$$

Thus giving,
$$
\begin{split}
\tan\left( \frac{ A-B }{ 2 } \right) &= \left( \frac{ a-b }{ a+b } \right) \cot \frac{ C }{ 2 } \\
\tan\left( \frac{ B-C }{ 2 } \right) &= \left( \frac{ b-c }{ b+c } \right) \cot \frac{ A }{ 2 } \\
\tan\left( \frac{ C-A }{ 2 } \right) &= \left( \frac{ c-a }{ c+a } \right) \cot \frac{ B }{ 2 } \\
\end{split}
$$

If question involves difference of angles, then we can think of Napier's analogy.

![[Pasted image 20231120184140.png]]

### Half Angle Formula 
It is derived from cosine rule. 

Breaking $\cos A$ into $1 - 2\sin ^{2} A/2$,
$$
\begin{split}
\cos A &= \frac{ b^{2} + c^{2} - a^{2} }{ 2bc } \\
2\sin ^{2} \frac{ A }{ 2 } &= \frac{ a^{2} - b^{2} - c^{2} + 2bc }{ 2bc } \\
&= \frac{ a^{2} - (b - c)^{2} }{ 2bc } \\
&= \frac{ 4(s - b)(s - c) }{ 2bc } \\
\sin \frac{ A }{ 2 } &= \sqrt{ \frac{ (s-b)(s-c) }{ bc } }
\end{split}
$$
Similarly,
$$
\begin{split}
\sin \frac{ B }{ 2 } &= \sqrt{ \frac{ (s-a)(s-c) }{ ac } } \\
\sin \frac{ C }{ 2 } &= \sqrt{ \frac{ (s-a)(s-b) }{ ab } }
\end{split}
$$

Breaking $\cos A$ into $2\cos ^{2} A /2 - 1$,
$$
\begin{split}
2 \cos ^{2} \frac{ A }{ 2 } &= \frac{ (b + c)^{2} - a^{2} }{ 2bc } \\
&= \frac{ 4s(s-a) }{ 2bc } \\
\cos \frac{ A }{ 2 } &= \sqrt{ \frac{ s(s-a) }{ bc } }
\end{split}
$$
Similalrly,
$$
\begin{split}
\cos \frac{ B }{ 2 } &= \sqrt{ \frac{ s(s-b) }{ ac } } \\
\cos \frac{ C }{ 2 } &= \sqrt{ \frac{ s(s-c) }{ ab } }
\end{split}
$$

To remember,
$$
\begin{split}
\Delta &= \frac{ 1 }{ 2 } ab \sin C \\
\sqrt{ s(s-a)(s-b)(s-c) } &= ab \sin \frac{C}{2} \cos \frac{C}{2} \\
\sqrt{ \frac{ (s-a)(s-b) }{ ab } } \sqrt{ \frac{ s(s-c) }{ ab } } &= \sin \frac{ C }{ 2 } \cos \frac{ C }{ 2 }
\end{split}
$$

For half angle in tan, we divide sin by cos, (remember this)
$$\tan \frac{ A }{ 2 } = \sqrt{ \frac{ (s-b)(s-c) }{ s(s-a) } }$$
Multiplying $(s-b)(s-c)$ in num. and denom.,
$$\tan \frac{ A }{ 2 } = \frac{ (s-b)(s-c) }{ \Delta }$$
Multiplying $s(s-a)$ in num. and denom.,
$$\tan \frac{ A }{ 2 } = \frac{ \Delta }{ s (s-a) }$$

And, cot will be,
$$\cot \frac{ A }{ 2 } = \sqrt{ \frac{ s(s-a) }{ (s-b)(s-c) } } = \frac{ \Delta }{ (s-b)(s-c) } = \frac{ s(s-a) }{ \Delta }$$

Now, summing cot of all half angles,
$$
\begin{split}
\sum \cot \frac{ A }{ 2 } &= \sum \frac{ s(s-a) }{ \Delta } \\
&= \frac{ s }{ \Delta } \sum (s-a) \\
&= \frac{ s^{2} }{ \Delta } \\
&= \frac{ (2s)^{2} }{ 4\Delta } \\
&= \frac{ (a+b+c)^{2} }{ 4\Delta } \\
\end{split}
$$
Thus giving,
$$
\begin{split}
\sum \cot A &= \frac{ \sum a^{2} }{ 4\Delta } \\
\sum \cot \frac{ A }{ 2 } &= \frac{ \left( \sum a \right)^{2} }{ 4\Delta }
\end{split}
$$
From this we can see that,
$$\sum \cot \frac{ A }{ 2 } > \sum \cot A$$
We can also get this result from the fact that cot is a decreasing function and all half angles are acute. 

## Cot m-n Theorem
It is derived from sine rule. 

$$
\begin{split}
(m + n)\cot \theta &= m\cot \alpha - n \cot \beta \\
&= n\cot B - m\cot C 
\end{split}
$$
Here we can see that the angle being used first is an angle of the other triangle. 

![[Pasted image 20231123085340.png]]

**Derivation,**
> $$
> \begin{split}
> \text{Using sine rule in } \Delta ABD, \\
> \frac{ AD }{ \sin(\theta - \alpha) } &= \frac{ BD }{ \sin \alpha } \\
> \\
> \text{Using sine rule in } \Delta ADC, \\
> \frac{ AD }{ \sin(\pi -(\beta + \theta)) } &= \frac{ DC }{ \sin \beta } \\
> \\
> \text{Dividing them,} \\
> \frac{ \sin (\beta + \theta) }{ \sin(\theta - \alpha) } &= \frac{ BD }{ DC } \frac{ \sin \beta }{ \sin\alpha } \\
> &= \frac{ m }{ n } \frac{ \sin \beta }{ \sin\alpha } \\
> \\
> \text{Simplifying}, \\
> (\sin \beta \cos \theta + \cos \beta \sin \theta)n\sin\alpha &= (\sin \theta \cos \alpha - \cos\theta \sin\alpha) m \sin \beta \\
> \\
> \text{Dividing by} \sin\alpha \sin \beta \sin \theta, \\
> n\cot \theta + n \cot \beta &= m\cot \alpha - m\cot \theta \\
> (m+n) \cot \theta &= m\cot\alpha - n\cot \beta
> \end{split}
> $$

#### Some PTR 
If a point on a side and the ratio in which it divides the side are given then we can think of applying cot m-n theorem. 

If median is involved, then we can think of using cot m-n theorem. Here m = n = 1. 

### Examples 
![[Pasted image 20231123091321.png]]

![[Pasted image 20231123093635.png]]

![[Pasted image 20231123093706.png]]

![[Pasted image 20231123093752.png]]
