Links: [[04 Monotonicity]], [[05 Maxima and Minima]], [[07 Concavity and Curve Sketching]]
___
# Rolle's Theorem (RT) 
It is a specific case of LMVT. 

*If $f(x)$ is a continuous function in $[a,b]$ and is a differentiable function in $(a,b)$ and if $f(a) = f(b)$ then there exist a number $c \in (a,b)$ such that $f'(c) = 0$.* 

The continuity is in closed interval and differentiability is in open interval. I.e. function can be non differentiable at a and b. 

The end points should be at same y level. 

This theorem guarantees the existence of at least one horizontal tangent b/w a and b. There can be more than one points where tangent is horizontal.

![[Rolle's theorem.png]]

### Applications of RT
It can be used to show existence of root of an equation. $f(x) = 0$.

Note that in RT we verify condition on a function and if all conditions are fulfilled over an interval, then the theorem asserts that the derivative of function will have a root in that interval. 

To prove that equation $f(x) = 0$ in $(p,q)$, 
1. Assume $g(x) = \int f(x) \, dx$
2. Verify conditions of RT on $g(x)$. 
3. If it satisfies all three conditions, then using RT, $g'(x) = 0$ and thus $f(x) = 0$ will have a root in $(p,q)$.
4. If conditions are not satisfied, then RT fails, so try some other method. 

#### Polynomial Function
Let $f(x)$ be polynomial function and has 2 roots, say $a,b$, i.e.
$$f(a) = f(b) = 0$$
Now $f(x)$ is continuous and differentiable, thus using RT, 
$$f'(x) = 0$$
will have a root in $(a,b)$.

That is, between any two roots of polynomial, its derivative will also have at least one real root.

![[Pasted image 20230916150446.png]]

If $f(x) = 0$ has n roots, then $f'(x) = 0$ will have at least n-1 roots. 

If $f(x)$ is differentiable function and $f^{(r)}$ exist, then, if $f(x) = 0$ has n real roots, then $f^{(r)}$ will have **at least** n-r real roots. 

Going in reverse, if $f(x)$ has n real roots, then 
$\int f(x) \, dx$ will have **at most** n+1 real roots, 
$\int (\int f(x) \, dx) \, dx$ will have **at most** n+2 real roots, and so on.

Example,
![[Pasted image 20230916150610.png]]
(the original q has $10x^{5} + x^{4}$)

If $f(x) = 0$ has repeated roots $\alpha$, then it will also be a root of $f'(x) = 0$. Thus to prove that polynomial has repeated roots, we show that $f(x) = 0$ and $f'(x) = 0$ have one common root. 

![[Pasted image 20230916151051.png]]

## Examples 
![[Pasted image 20230916150511.png]]

![[Pasted image 20230916150527.png]]
![[Pasted image 20230916150537.png]]


## Lagrange's Mean Value Theorem (LMVT)
It is a more general case of Rolle's Theorem. 

*If $f(x)$ is continuous in $[a,b]$ and is differentiable in $(a,b)$ then there exist a number $c \in (a,b)$ such that 
$$f'(c) = \frac{ f(a) - f(b) }{ a - b }$$*

If $f(a) = f(b)$, then $f'(c) = 0$ i.e. Rolle's Theorem. 


Graphically, it means that there will be one point where the slope of the tangent will be the same as that of the chord formed by joining the two points. 

![[LMVT.png]]

**Proof:**
> $$
> \begin{split}
> \text{We have to show,} \\
> f'(x) &= \frac{ f(b) - f(a) }{ b - a } = 0 \\
> \text{has root in (a,b).} \\
> \text{Condider,} \\
> g(x) &= f(x) - \left( \frac{ f(b) - f(a) }{ b - a } \right)x = 0 \\
> \text{Now,} \\
> g(a) - g(b) &= f(a) - f(b) - \left( \frac{ f(b) - f(a) }{ b - a } \right)(a - b) \\
> &= f(a) - f(b) - f(a) - f(b) \\
> &= 0\\
> g(a) &= g(b) \\
> \text{Using Rolle's Theorem,} \\
> g'(c) &= 0,\ c \in (a,b) \\
> f'(c) - \frac{ f(b) - f(a) }{ b - a } &= 0 \\
> f'(c) &= \frac{ f(b) - f(a) }{ b - a }
> \end{split}
> $$

There can be more than one c between a and b. We cannot tell the location of c in the interval. 

If in the interval $(a,b)$ we are applying LMVT twice on two different functions, then take $c_{1},c_{2}$ instead of c both the times. Also, we cannot find a relation between them using LMVT alone.

Hint of application of LMVT can be obtained by the presence of $f(a) - f(b)$ type expression. 

#### Alternative Interpretations
In alternate language we can say,
*There exist a point c in interval $(a,b)$ where the instantaneous rate change of function is the same as the average value change of it over the interval.*
$\displaystyle \frac{ f(a) - f(b) }{ a - b }$ is the average change of function over the interval $(a,b)$.

There exists a number $\eta \in (0,1)$ such that,
$$
\begin{split}
f'(c) &= \frac{ f(b) - f(a) }{ b - a } \\
f(b) &= f(a) + (b-a) f'(c) \\
&= f(a) + l.f'(a + \eta l)
\end{split}
$$

#### Inequalities
We can prove some inequalities using LMVT. And in doing so, we can get rid of c by analysing monotonicity of $f'(x)$.

If $f'(x)$ is increasing function in $(a,b)$, then, $a < c < b$ implies,
$$f'(a) < f'(c) < f'(b)$$
$$f'(a) < \frac{ f(b) - f(a) }{ a - b } < f'(b)$$

### Cauchy's Mean Value Theorem 
It is the general case of LMVT. CMVT is LMVT when $g(x) = x$.

*If $f(x), g(x)$ are continuous in $[a,b]$ and are differentiable in $(a,b)$ then there exist a number $c \in (a,b)$ such that 
$$\frac{f'(c)}{g'(c)} = \frac{ f(a) - f(b) }{ g(a) - g(b) }$$*

**Proof:**
> $$
> \begin{split}
> \text{Consider,} \\
> h(x) &= f(x) - \left( \frac{ f(a) - f(b) }{ g(a) - g(b) } \right)g(x) \\
> \text{Now, as h(x) is cont. \& diff. and} \\
> h(a) - h(b) &= f(a) - f(b) - (f(a) - f(b)) \\
> &= 0 \\
> h(a) &= h(b) \\
> \text{Using Rolle's Theorem,} \\
> h'(c) &= 0,\ c \in (a,b) \\
> f'(c) - \left( \frac{ f(a) - f(b) }{ g(a) - g(b) } \right)g'(c) &= 0 \\
> \frac{f'(c)}{g'(c)} &=\frac{ f(a) - f(b) }{ g(a) - g(b) }
> \end{split}
> $$

### Examples 
![[Pasted image 20230916150904.png]]

![[Pasted image 20230916150922.png]]
![[Pasted image 20230916150937.png]]

![[Pasted image 20230916150951.png]]
![[Pasted image 20230916151000.png]]
