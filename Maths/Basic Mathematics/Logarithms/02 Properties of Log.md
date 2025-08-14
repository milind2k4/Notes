Links: [[01 Logarithms]]
___
# Properties of Log
#important 
are basically properties of exponents.

1. $\log_{a}b = c \implies a^{c} = b$
   i.e. Argument = Base$^{RHS}$

3. $\log_{a}a = 1$

4. $\log_{a}1 = 0$

5. $a^{\log_{a}b} = b$

6. $\log_{a}b + \log_{a}c = \log_{a}bc$
   If $a,c > 0$, then this holds
   If $a,c < 0$, then LHS is undefined but RHS is defined
   If $a.c < 0$, then both sides are undefined
> Proof: 
> $$
> \begin{split}
> \text{Let} \log_{a}b = x\ &\&\ \log_{a}c = y.\\
> a^{x} = b\ &\&\ a^{y} = c \hspace{1cm}...(1) \\
> bc &= a^{x} \cdot a^{y} \\
> bc &= a^{x+y} \\
> \log_{a}bc &= x + y \\
> \log_{a}bc &= \log_{a}b + \log_{a}c \hspace{1cm} \text{(from 1)}
> \end{split}
> $$

6. $\log_{a}b^{k} = k \log_{a}|b|$
	If k = 2m then LHS will be undefined but RHS will be defined if b < 0.
> Proof: 
>$$
> \begin{split} 
> \text{Let}\  \log_{a}b  &= c \hspace{2cm} ..(1)\\
> a^{c} &= b \\
> \text{Raising both}\  \text{to k,} \\
> b^{k} &= a^{ck} \\
> \text{Taking log,} \\
> \log_{a}b^{k} &= k\ c \\
> \log_{a}b^{k} &= k\ \log_{a}b^{k} \hspace{1cm} \text{(from 1)}
> \end{split}
> $$

7. $\log_{a}^{k}b = (\log_{a}b)^{k}$

8. $\log_{a}b - \log_{a}c = \log_{a}\frac{b}{c}$
> $-\log_{a}c = +\log_{a}c^{-1}$  and then apply 5.

9. Any positive number $'k'$ can be written as  $k = a^{\log_{a}k}$.
   This can be used to manipulate $\ce{ func^{func} }, \&\ var^{var}$
   $$f^{g} = a^{g\log_{a}f}$$

## Base Changing Theorem
> $$\log_{b}a = \frac{\log_{c}a}{\log_{c}b}$$

Proof:
> $$\begin{split}
> \log_{b}a &= x \\
> b^{x} &= a \\
> \log_{c}b^{x} &= \log_{c}a \\ 
> x\log_{c}b &= \log_{c}a \\ 
> x &= \frac{\log_{c}a}{\log_{c}b} \\ 
> \log_{a}b &= \ \frac{\log_{c}a}{\log_{c}b} \\
> \end{split}
> $$

**Note:** If a = 1 then LHS is defined but RHS is not defined. 

### Formulae derived from BCT

1. $$\log_{b}a = \frac{1}{\log_{a}b}$$
> Proof:
>    $$\begin{split}
>    \log_{b}a &= \frac{\log_{a}a}{\log_{a}b} \\
>    &= \frac{1}{\log_{a}b}
>  \end{split}$$


2. $$\log_{b^{k}a} = \frac{1}{k}\log_{b}a$$
> Proof:
>    $$\begin{split}
>    \log_{b^{k}}a &= \frac{\log_{b}a}{\log_{b}b^k} \\
>    &= \frac{\log_{b}a}{k\log_{b}b} \\
>    &= \frac{1}{k}\log_{b}a
>  \end{split}$$
> Combining this and #6 from [[02 Properties of Log]], we get,
> $$\log_{b^n}a^{m} = \frac{m}{n}\log_{b}a$$

3. $$\log_\frac{1}{b}a = - \log_{b}a = \log_{b}\frac{1}{a}$$

4. $$a^{\log_{b}c} = c^{\log_{b}a}$$
> Proof:
> $$
> \begin{split}
> a^{\log_{b}c} &= a^{^{\displaystyle \frac{ \log_{a}c }{ \log_{c}b }}} \\
> &= (a^{\log_{a}c})^{^{\displaystyle \frac{ 1 }{ \log_{a}b }}} \\
> &= c^{\log_{b}a}
> \end{split}
> $$
> And,
> $$a^{\sqrt{ \log_{a}b }} = b^{\sqrt{ \log_{b}a }}$$