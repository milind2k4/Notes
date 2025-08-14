Links: [[00 Differentiation]]
___
# Algebra of Differentiation 
($f,g,h$ are functions)

1. Addition
   $$(f \pm g)' = f' \pm g'$$

2. Multiplication by Scalar
   $$(kf)' = kf'(x)$$

3. **Product Rule**
   $$(f.g)' = f'g + fg'$$
   $$(fgh)' = f'gh + fg'h + fgh'$$

4. **Quotient Rule** (remember that since denom. decreases something, its derivative comes with -)
   $$\frac{ f }{ g } = \frac{ f'g - fg' }{ g^{2} }$$

### Chain Rule
Let x and y are related by a variable z, then,
$$\frac{ dy }{ dx } = \frac{ dy }{ dz } . \frac{ dz }{ dx }$$

#### Parametric Differentiation
If $y = f(t)$ and $x = g(t)$

then,
$$\frac{ dy }{ dx } = \frac{ dy }{ dt } . \frac{ dt }{ dx } =   \frac{ \displaystyle \frac{dy}{dt}  }{ \displaystyle \frac{dx}{dt} } = \frac{ f'(t) }{ g'(t) }$$

![[Pasted image 20230813190035.png]]

#### Derivative of f wrt g
$f(x)$ and $g(x)$ are two functions,

$$\frac{ df }{ dg } = \frac{ df }{ dx } . \frac{ dx }{ dg } = \frac{ \displaystyle \frac{ df }{ dx }  }{ \displaystyle \frac{ dg }{ dx } } = \frac{ f'(x) }{ g'(x) }$$

Here we have to take care to see if the domain of both functions overlaps or not. If not then the derivative is not defined. 

Also, if the intersection of domains are distinct points, the derivative does not exist. It makes no sense to differentiate a function at one point. 

![[Pasted image 20230813190909.png]]

#### Differentiation of Composite Function 
$f,g,h$ are functions.
$$
\begin{split}
\frac{ d(f(g)) }{ dx } &= \frac{ df(g) }{ g }. \frac{ dg }{ dx } \\
&= f'(g(x)) . g'(x) 
\end{split}
$$

Similarly,
$$\frac{ d(f(g(h))) }{ dx } = f'(g(h)). g'(h) . h'$$
