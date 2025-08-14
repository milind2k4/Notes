Links: 
___
# Using Substitution
Purpose of substitution is to simplify the expression.

$$\begin{split}
\int& f(g(x)).g'(x) \, dx \\
\text{Now,} \\
g(x) &= t\\
d(g(x)) &= dt\\
g'(x).dx &= dt\\
\\
\text{Then,} \\
\int & f(t) \, dt
\end{split}$$


We can also use,
$$\int f(g(x))g'(x) \, dx = \int f(g(x)) \, d(g(x))  $$
i.e. integrate directly with respect to the inside function. 
![[Pasted image 20230926175029.png]]

#### Some more Standard Formula
Using this we have some #important formulae,
$$\begin{split}
\int \tan x \, dx &= \ln |\sec x| + c \\
\int \cot x \, dx &= \ln |\sin x| + c \\
\int \sec x \, dx &= \ln |\sec x + \tan x| + c \\
&= -\ln | \sec x - \tan x | + c \\
&= \ln \left| \tan \left( \frac{ \pi }{ 4 } + \frac{ x }{ 2 } \right)  \right| + c\\
\int \csc x \, dx &= \ln |\csc x - \cot x| + c \\
&= - \ln |\csc x + \cot x| + c 
\end{split}$$

![[Pasted image 20230926175957.png]]
![[Pasted image 20230926180009.png]]

#### Some PTR
If Expression of x are converted into new variable t, then all terms of x must be converted into t for integration. 

Final answer must be expressed in terms of original variable. 

In substitution try to remove radicle sign i.e. $\sqrt{ }, \sqrt[3]{  }$ etc. 
![[Pasted image 20230923154313.png]]

Try to substitute for argument of composite function is present. 

We have to search for $g$ and $g'$.

Presence of $f'(x)$ with $dx$ indicates substitution. 

#### Examples 
![[Pasted image 20230923155309.png]]

![[Pasted image 20230926175324.png]]

![[Pasted image 20230926180529.png]]

![[Pasted image 20230926180815.png]]

![[Pasted image 20230926181437.png]]
(in q-9 there will be -1/2 in exponent)

![[Pasted image 20230926182356.png]]

![[Pasted image 20230926182607.png]]
(here the exponent will be 2 not 3)

![[Pasted image 20230926183033.png]]

![[Pasted image 20230926183907.png]]


