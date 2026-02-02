Links: [[03 Theorems from Sine and Cosine Law]]
___
# Sine and Cosine Rule
## Sine Rule
aka **Law of Sines**

![[Pasted image 20231120091538.png]]
(M is mid point of BC)

In $\Delta BOM$,
$$
\begin{split}
\sin A &= \frac{ a /2 }{ R } \\
a &= 2R \sin A \\
\text{Similarly}, \\
b &= 2R \sin B \\
c &= 2R \sin C 
\end{split}
$$

Thus,
$$
\begin{split}
a &= 2R \sin A \\
b &= 2R \sin B \\
c &= 2R \sin C 
\end{split}
$$

Alternatively we can write,
$$
\begin{split}
\frac{ a }{ \sin A } &= \frac{ b }{ \sin B } &= \frac{ c }{ \sin C } &= 2R
\end{split}
$$

#### Point to Remember 
Using sine law, we can always convert $a$ to $\sin A$ and vice versa. I.e. $a \ce{ <-> } \sin A$

Similarly, $a\cos A \ce{ <-> } \sin 2A$. 
And, $\frac{a}{\cos A} \ce{ <-> } \tan A$.

We can write,
$$
\begin{split}
a^{2} - b^{2} &= 4R^{2} (\sin ^{2}A - \sin ^{2}B) \\
&= 4R^{2} \sin(A+B)\sin(A-B) \\
&= 4R^{2} \sin C \sin (A-B) 
\end{split}
$$

Also,
$$\frac{ k_{1}a + k_{2}b }{ k_{3}c } = \frac{ k_{1}\sin A + k_{2}\sin B }{ k_{3}\sin C }$$

If sides of a triangle ABC are in AP, then,
$$
\begin{split}
a, b, c &\to AP \\
\sin A, \sin B, \sin C &\to AP
\end{split}
$$

Using this we have,
$$
\begin{split}
2\sin B &= \sin A + \sin C \\
2 \sin \left( \frac{B}{2} \right) \cos \left( \frac{B}{2} \right) &= 2 \sin \left( \frac{ A+C }{ 2 } \right) \cos \left( \frac{ A - C }{ 2 } \right) \\
\sin \frac{ B }{ 2 } &= \cos \left( \frac{ A - C }{ 2 } \right)
\end{split}
$$

We can interchange side and angle if they are in product,
$$a \sin B = b\sin A$$
$$b \sin C = c\sin B$$

### Examples 
![[Pasted image 20231120093326.png]]

![[Pasted image 20231120093629.png]]

![[Pasted image 20231120094747.png]]

![[Pasted image 20231120095607.png]]

Application of Sine Rule to find side of a triangle,
![[Pasted image 20231120100307.png]]

## Cosine Rule 
![[Pasted image 20231120172526.png]]

In $\Delta ADC,$
$$
\begin{split}
AD^{2} + DC^{2} &= AC^{2} \\
(c\sin B)^{2} + (a - c\cos B) &= b^{2} \\
c^{2} \sin ^{2}B + a^{2} + c^{2}\cos ^{2}B - 2ac \cos B &= b^{2} \\
c^{2} + a^{2} - 2ac \cos B &= b^{2} 
\end{split}
$$
Thus we can write,
$$
\begin{split}
a^{2} &= b^{2} + c^{2} - 2b c \cos A \\
b^{2} &= a^{2} + c^{2} - 2a c \cos B \\
c^{2} &= a^{2} + b^{2} - 2a b \cos C \\
\end{split}
$$

Or we can write,
$$
\begin{split}
\cos A &= \frac{ b^{2} + c^{2} - a^{2} }{ 2bc } \\
\cos B &= \frac{ a^{2} + c^{2} - b^{2} }{ 2ac } \\
\cos C &= \frac{ a^{2} + b^{2} - c^{2} }{ 2ab } \\
\end{split}
$$

Or we can write,
$$
\begin{split}
2ab \cos C &= a^{2} + b^{2} - c^{2} \\
2bc \cos A &= b^{2} + c^{2} - a^{2} \\
2ac \cos B &= a^{2} + c^{2} - b^{2}
\end{split}
$$

#### Point to Remember 
If sides are involved in a question, then we can think of using cosine rule. 

We can use cosine rule to find whether triangle is acute or obtuse angled. We will check for sign of $\cos C$ (c/C being largest side/angle) using sign of $a^{2} + b^{2} - c^{2}$.

If $A = 60^{\circ}$,
$$
\begin{split}
\cos A &= \frac{ 1 }{ 2 } = \frac{ b^{2} + c^{2} - a^{2} }{ 2bc } \\
a^{2} &= b^{2} + c^{2} - bc
\end{split}
$$
If $c^{2} = a^{2} + b^{2} - ab$, then $C = 60^{\circ}$. 

If $B = 120^{\circ}$,
$$
\begin{split}
\cos B &= -\frac{ 1 }{ 2 } = \frac{ a^{2} + c^{2} - b^{2} }{ 2ac } \\
b^{2} &= a^{2} + c^{2} + ac
\end{split}
$$
If $c^{2} = a^{2} + b^{2} + ab$, then $C = 120^{\circ}$. 


We have,
$$\cos A = \frac{ b^{2} + c^{2} - a^{2} }{ 2bc }$$
Dividing by $\sin A$ both sides,
$$
\begin{split}
\cot A &= \frac{ b^{2} + c^{2} - a^{2} }{ 2bc \sin A } \\
&= \frac{ b^{2} + c^{2} - a^{2} }{ 4 \Delta } \\
\end{split}
$$
Now, if we sum cot of all three angles,
$$
\begin{split}
\sum \cot A &= \frac{ b^{2} + c^{2} - a^{2} }{ 4 \Delta } + \frac{ a^{2} + c^{2} - b^{2} }{ 4 \Delta } + \frac{ a^{2} + b^{2} - c^{2} }{ 4 \Delta } \\
&= \frac{ a^{2} + b^{2} + c^{2} }{ 4 \Delta } \\
&= \frac{ \sum a^{2} }{ 4 \Delta }
\end{split}
$$

### Examples 
![[Pasted image 20231120181025.png]]

![[Pasted image 20231120181644.png]]

![[Pasted image 20231120182344.png]]

![[Pasted image 20231120182819.png]]

![[Pasted image 20231123085024.png]]










