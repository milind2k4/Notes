Links: [[02 Algebra of Limits]], [[04 Methods of Evaluation of Limits]]
___
# Standard Limits
#formula
These are valid also if $\displaystyle \lim_{ x \to a } f(x) = 0$ and we replace $x$ with $f(x)$. 

1. $$\lim_{x \to a} \frac{x^{n} - a^{n}}{x-a} = n \cdot a^{n-1}$$
   $$\lim_{x \to 1} \frac{x^{n}-1}{x-1} = n $$
   where n $\in R$
> Proof:
> $$\begin{split}
> \lim_{x \to a} & \frac{x^{n} - a^{n}}{x-a} \\
> \\
> \text{Let, } t = x - a &\implies x = t + a\\
> x \to a &\implies  t \to 0 \\
> \\
> &= \lim_{t \to 0} \frac{(t+a)^{n} - a^{n}}{a+t-a} \\
> \\
> &= \lim_{t \to 0} \frac{a^{n}[(1+\frac{t}{a})^{n} - 1]}{t} \\
> \\
> &=  a^{n} \lim_{t \to 0} \frac{1+n(\frac{t}{a}) - 1}{t} \\
> \\
> &= a^{n} \cdot \frac{n}{a} \\
> &= n \cdot a^{n-1} \\
> \\
> & \text{Hence Prooved.}
> \end{split}$$

#### Trigonometric Limits 
2. $$\lim_{x \to 0} \frac{\sin x}{x} = 1 $$


2. $$\lim_{x \to 0} \frac{\tan x}{x} = 1 $$
> Proof:
> $$\begin{split}
> & \lim_{x \to 0} \frac{\tan x}{x} \\\\ 
> = & \lim_{x \to 0} \frac{1}{\cos x} \cdot \frac{\sin x}{x} \\ \\
> = & \lim_{x \to 0} \frac{1}{\cos x} \cdot \frac{\sin x}{x} \\ \\
> = &\ 1 \cdot 1 = 1 \\\\
> & \text{Hence Prooved.}
> \end{split}$$

2. $$\lim_{x \to 0} \frac{1 - \cos x}{x^{2}} = \frac{1}{2} $$
> Proof:
> $$\begin{split}
> \lim_{x \to 0} & \frac{1 + \cos x}{x^{2}} \\ \\
> = & \lim_{x \to 0} \frac{1 + \cos x}{1 + \cos x} \cdot \frac{1 - \cos x}{x^{2}} \\ \\
> = & \lim_{x \to 0} \frac{1}{1 + \cos x} \cdot \frac{1 - \cos^{2} x}{x^{2}} \\ \\
> = & \lim_{x \to 0} \frac{1}{1 + \cos x} \cdot \frac{\sin^{2} x}{x^{2}} \\ \\
> = & \lim_{x \to 0} \frac{1}{2} \cdot 
 \left( \frac{\sin x}{x} \right)^{2}  \\ \\
> = &\ \frac{1}{2} \cdot 1 = \frac{1}{2} \\\\
> & \text{Hence Prooved.}
> \end{split}$$

##### Some Points to Note
For any of the trigonometric limits to be used, $x \to 0$. 

$$\lim_{ x \to 0 } \frac{ \cos x }{ x } = \frac{ 1 }{ 0 } = DNE$$

If $f(x) \to 0$ as $x \to a$ then, 
$$\lim_{ x \to a } \frac{ \sin f(x) }{ f(x) } = 1$$
i.e. all three formula will hold if we replace x with any other expression which tends towards zero. 
Note that at all places of x, we should have same expression. 

I.e. 
If $f(x), g(x) \to 0$ as $x \to a$ then in general,
$$\lim_{ x \to a } \frac{ \sin f(x) }{ g(x) } \neq 1$$

The ratio of any 2 in $x,\ \sin x,\ \sin ^{-1} x,\ \tan x,\ \&\ \tan ^{-1} x$ if $x \to 0$ will be 1.
i.e. let $A, B = x,\ \sin x,\ \sin ^{-1} x,\ \tan x,\ \&\ \tan ^{-1} x$,  then $\displaystyle \lim_{x \to 0} \frac{A}{B} = 1$

If $A \to 0$ and if (the following sin tan cos expressions are) present in product form of entire expression, then #important 
- $\sin A, \sin ^{-1}A, \tan A, \tan ^{-1}A$ can be replaced with A. 
- $1 - \cos A$ can be replaced with $A^{2} /2$.

![[Pasted image 20230805091808.png]]

This will help in questions where there are multiple trig expression involved,
![[Pasted image 20230805092356.png]]

#### Logarithmic & Exponential Limits

5. $$\lim_{ x \to 0 } \frac{ \ln(1+x) }{ x } = 1$$

7. $$\lim_{ x \to 0 } \frac{ \log_{a}(1+x)  }{ x } = \frac{ 1 }{ \ln a }$$
5. $$\lim_{ x \to 0 } \frac{ e^{x}-1 }{ x } = 1$$

6. $$\lim_{ x \to 0 } \frac{ a^{x} - 1 }{ x } = \ln a$$

##### Some Points to Note
If $x \to a \implies f(x) \to 0$ then,
$$\lim_{ x \to 0 } \frac{ \ln (1 + f(x)) }{ f(x) } = 1$$
similar to trigonometric formula. 

If $A\to 0$ and if present in product form, then,
- $\ln(1 + A)$ can be replaced with A.
- $e^{ A } - 1$ can be replaced with A.

If $A \to 1$ and if present in product form, then
- $\ln A$ can be replaced with A-1



## Collectively
1. $$\lim_{ x \to 0 } \frac{ \sin x }{ x } = 1$$

2. $$\lim_{ x \to 0 } \frac{ \tan x }{ x } = 1$$

3. $$\lim_{ x \to 0 } \frac{ \sin ^{-1}x }{ x } = 1$$

4. $$\lim_{ x \to 0 } \frac{ \tan ^{-1}x }{ x } = 1$$

5. $$\lim_{ x \to 0 } \frac{ e^{x}-1 }{ x } = 1$$

6. $$\lim_{ x \to 0 } \frac{ \ln(1+x) }{ x } = 1$$

7. $$\lim_{ x \to 0 } \frac{ 1-\cos x }{ x^{2} } = \frac{1}{2}$$

8. $$\lim_{ x \to a } \frac{ x^{n} - a^{n} }{ x-a } = na^{n-1}$$