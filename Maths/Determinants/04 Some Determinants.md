Links: [[01 Expansion]], [[02 Properties]], [[03 Transformations]]
___
# Some Important Determinants 
#### Symmetric
$$\begin{vmatrix}
a & h & g \\
h & b & f \\
g & f & c
\end{vmatrix} = abc + 2fgh - af ^{2} - bg^{2} - ch^{2}$$

### Circulants
#### Linear and Circular
![[Pasted image 20230623083020.png]]

$$\begin{split}
\begin{vmatrix}
a & b & c \\
b & c & a \\
c & a & b \\
\end{vmatrix} &=  3ab - a^{3} - b^{3}- c^{3} \\
&= - (a+b+c)\cdot \frac{1}{2} [(a-b)^{2} + (b-c)^{2} + (c-a)^{2}] \\
&= -(a+b+c)(a^{2}+b^{2} +c^{2} - ab - bc - ca)
\end{split}$$
(from [[02 Formula and Expansions]])

If $\det = 0 \implies a+b+c = 0$ or $(a-b)^{2} + (b-c)^{2} + (c-a)^{2} = 0 \implies a=b=c$


#### $a$ and $a^{2}$ type
$$\begin{vmatrix}
1 & a & a^{2} \\
1 & b & b^{2} \\
1 & c & c^{2}
\end{vmatrix} = (a-b)(b-c)(c-a)$$
> **Proof:**
> $$
> \begin{split}
> \begin{vmatrix}
> 1 & a & a^{2} \\
> 1 & b & b^{2} \\
> 1 & c & c^{2}
> \end{vmatrix} &\ce{ ->[R_{2} \to R_{2} - R_{1}][R_{3} \to R_{3} - R_{1}] } 
> \begin{vmatrix}
> 1 & a & a^{2} \\
> 0 & b-a & b^{2}-a^{2} \\
> 0 & c-a & c^{2}-a^{2}
> \end{vmatrix} \\ \\
> &= (b-a)(c-a) \begin{vmatrix}
> 1 & a & a^{2} \\ 
> 0 & 1 & b + a \\
> 0 & 1 & c+a
> \end{vmatrix}\\ \\
> &= (b-a)(c-a)(c-b) 
> \end{split}
> $$

We can also get this by treating this as a cubic in a and then observing that putting b or c in the place of a gives zero, thus making $(a-b)$ and $(a-c)$ its factors, Then by symmetry, we gat $(b-c)$, the three factors. 

This determinant is also equal to,
$$\begin{vmatrix}
1 & a & bc \\
1 & b & ac \\
1 & c & ab
\end{vmatrix} = (a-b)(b-c)(c-a)$$


#### $a$ and $a^{3}$ type

$$\begin{vmatrix}
1 & a & a^{3} \\
1 & b & b^{3} \\
1 & c & c^{3}
\end{vmatrix} = (a+b+c)(a-b)(b-c)(c-a)$$
This should have factors $(a-b)(b-c)(c-a)$. This will get us three degree terms, but we require 4 degree terms. To get this we need a term symmetric in a, b, c, which is $(a+b+c)$. 


#### $a^{2}$ and $a^{3}$ type
$$\begin{vmatrix}
1 & a^{2} & a^{3} \\
1 & b^{2} & b^{2} \\
1 & c^{2} & c^{3}
\end{vmatrix} = (ab+bc+ca)(a-b)(b-c)(c-a)$$

This should have factors $(a-b)(b-c)(c-a)$. This will get us three degree terms, but we require 5 degree terms. To get this we need a term symmetric in a, b, c, which are $k_{1}(a^{2}+b^{2}+c^{2})$ or $k_{2}(ab+bc+ca)$. To find the constants we put a = 0 and compare the coefficients. This gives us $k_{1} = 0, k_{2}=1$. 

#### $a$ and $a^{4}$ type
$$\begin{vmatrix}
1 & a & a^{4} \\
1 & b & b^{4} \\
1 & c & c^{4}
\end{vmatrix} = (a^{2}+b^{2}+c^{2} + ab + bc + ca)(a-b)(b-c)(c-a)$$

#### Skew Symmetric of Odd Order
$$
\begin{vmatrix}
0 & a & b \\
-a & 0 & c \\
-b & -c & 0
\end{vmatrix} = 0
$$