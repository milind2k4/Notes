Links: [[01 Standard Formula]]
___
# Differentiation
If $y = f(x)$ is a function, then its derivative wrt x can be given as,
$$\frac{ dy }{ dx } = \frac{ df(x) }{ dx } = f'(x) = D(y)$$
where,
$$D() = \frac{ d() }{ dx } $$
which is called differential operator.

$dy /dx$ is called the "differential coefficient of y w.r.t x."

Differentiation of inequality is not allowed. So, we use first principle. 

### First Principle of Differentiation 
[[09 Differentiability]]

Finding derivative of function by evaluating this limit is called First Principle or ab-initio. And we cannot use LH rule to find the limit. 
$$\frac{ dy }{ dx } = \lim_{ h \to 0 } \frac{ f(x+h)-f(x) }{ h } = \lim_{ \Delta x \to 0 } \frac{ f(x + \Delta x) - f(x) }{ \Delta x }$$
This can also be written as,
$$\frac{ dx }{ dy } = \lim_{ \Delta x \to 0 } \frac{ \Delta y }{ \Delta x }$$
which is instantaneous rate of change of y wrt x.

For this limit to exist, $\Delta x \to 0 \implies \Delta y \to 0$.

And, $\Delta y /\Delta x$ is the average change of y wrt x where x is changed quantity $\Delta x$. 

$dy /dx$ also gives slope of tangent. 

One thing to note is that $\Delta y /\Delta x$ is a ratio of numbers, but $dy / dx$ is not and we cannot separate them. 
$$\frac{ dy }{ dx } \neq \frac{ 1 }{ dx }.dy$$

Also,
$$
\begin{split}
\frac{ dy }{ dx } &= \lim_{ \Delta x \to 0 } \frac{ \Delta y }{ \Delta x } \\
&= \lim_{ \Delta x \to 0 } \frac{ 1 }{ (\Delta x /\Delta y) } \\
&= \lim_{ \Delta y \to 0 } \frac{ 1 }{ (\Delta x / \Delta y) } \\
&= \frac{ 1 }{ dx/dy }  
\end{split}
$$
That is,
$$\frac{ dy }{ dx } . \frac{ dx }{ dy } = 1$$

Differentiation of some functions using first principle,
![[Pasted image 20230813182710.png]]
![[Pasted image 20230813182734.png]]
![[Pasted image 20230813182933.png]]

We can find derivative of any function using first principle,
![[Pasted image 20230813183213.png]]

### [[01 Standard Formula]]

## [[02 Algebra of Differentiation]]

### Implicit Differentiation 
$$
\begin{split}
f(y) + g(x) + c &= 0 \\
f'(y) \frac{ dy }{ dx } + g'(x) &= 0
\end{split}
$$

We can change the form of answer using the expression in the question.

### Some Important Points 
$$f(g(x))' = f'(g(x)).g'(x)$$
Here, 
$$f'(g(x)) \neq \frac{df(g(x))}{dx}$$
$$f'(g(x)) = \frac{df(g(x))}{dg(x)}$$
So in $f'(g(x))$ the $'$ represents derivative wrt argument if argument contains variable. If argument contains constant, that means the value of derivative at that constant. 

Thus,
$$f'(z^{3}) = \frac{ df(z^{3}) }{ dz^{3} }$$
$$f'(3) \neq \frac{ df(3) }{ d(3) }$$

#### Differential Element

$$df(x) = f'(x).dx$$

For example,
$$d(t^{2}) = 2tdt$$


## Logarithmic Differentiation 
We use this when there is variable on exponent of variable or if there are many terms in product form. 

$$(\ln f)' = \frac{ f' }{ f }$$

We can use this to find sum of series,
The question is to find sum of series and $|x| < 1$,
![[Pasted image 20230813201755.png]]
![[Pasted image 20230813201826.png]]

#### Product of Functions 
$$
\begin{split}
y &= f.g.h \\
\ln y &= \ln f + \ln g + \ln h \\
\frac{ y' }{ y } &= \frac{ f' }{ f } + \frac{ g' }{ g } + \frac{ h' }{ h } \\
y' &= y\left( \frac{ f' }{ f } + \frac{ g' }{ g } + \frac{ h' }{ h } \right) \\
y' &= fgh \left( \frac{ f' }{ f } + \frac{ g' }{ g } + \frac{ h' }{ h } \right) \\
\end{split}
$$
However, to use this method we have to be careful that none of the functions' value is zero. Otherwise, we cannot take log and we have to use product rule. 

#### Variable raised to Variable
$$
\begin{split}
y &= f^{g} \\
\ln y &= g\ln f \\
\frac{ y' }{ y } &= g'\ln f + \frac{ gf' }{ f } \\
y' &= y\left( g'\ln f + \frac{ gf' }{ f } \right) \\
y' &= f^{g}\left( g'\ln f + \frac{ gf' }{ f } \right) \\
\end{split}
$$
Alternatively,
$$
\begin{split}
y &= f^{g} \\
&= e^{g\ln f} \\
y' &= e^{g\ln f}.\left( g'\ln f + \frac{ gf' }{ f } \right) \\
&= f^{g} \left( g'\ln f + \frac{ gf' }{ f } \right)
\end{split}
$$

Again alternatively, we can differentiate it by first considering as variable raised to constant and then by considering it as constant raised to variable and then adding the results. 
$$
\begin{split}
y &= f^{g} \\
y' &= \underset{ x^{n}\text{ form} }{ gf^{g-1}.f' } + \underset{ a^{x} \text{ form } }{ f^{g}. \ln f . g' } \\
y' &= g \frac{ f^{g} }{ f } f' + f^{g} \ln f . g' \\
&= f^{g}\left( \frac{ gf' }{ f } + g'\ln f \right)
\end{split}
$$

![[Pasted image 20230813214208.png]]

## [[04 Misc. Points]]

## [[Maths/Differentiation/05 Examples]]