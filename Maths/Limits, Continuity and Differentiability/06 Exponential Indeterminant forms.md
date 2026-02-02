Links: [[01 Indeterminant form]], [[04 Methods of Evaluation of Limits]], [[05 Standard Limits]]
___
# Exponential Indeterminant forms

## $1^{\infty}$ Form
Standard formula,
$$\lim_{ x \to 0 } (1 + x)^{1/x} = e$$
If power and base are related by same variable, both change simultaneously and base goes to 1, $\displaystyle \lim_{ x \to 0 } a^{x}$ cannot be used.  

> Proof:
> $$
> \begin{split}
> \lim_{ x \to 0 } (1 + x)^{1/x} &= \lim_{ x \to 0 } e^{\ln(1 + x)^{1/x}} \\
> &= \lim_{ x \to 0 } e^{ 1/x \ln(1 + x) } \\
> &= e^{ ^{ \displaystyle \lim_{ x \to 0 } \ln(1+x)/x} } \\
> &= e^{ 1 }
> \end{split}
> $$


Let $x \to a \implies f(x)\to 1$, then,

$$
\begin{split}
\lim_{ x \to a } (f)^{g} &= \lim_{ x \to a } e^{ g \ln f } \\
&= e^{ ^{ \displaystyle \small \lim_{ x \to a } g \ln f } } \\
&= e^{ ^{ \displaystyle \small \lim_{ x \to a } g(f-1) } } \\
&= \exp(\lim_{ x \to a } g(f-1))
\end{split}
$$
$\exp$ means that the expression is on power of e.
Thus,
$$\lim_{ x \to 0 } f^{g} = \exp(\lim_{ x \to 0 } g.(f-1))$$
i.e. exp(lim exponent (base - 1))

If $g \to \pm \infty$ then it will be indeterminant form then it will be indeterminant form. 

If base goes to 1 and exponent to $\pm \infty$ then we will not see whether it is $1^{+}$ or $1^{-}$ as $a^{x}$ is not valid as in this base and exponent are not linked with same variable.

However, if base goes to any other number, we can use $a^{x}$,
![[Pasted image 20230805114122.png]]

If $1^{\infty}$ form is not due to exponent and variable connected, we will use $a^{\infty}$ results. 

![[Pasted image 20230809102610.png]]
Here as the exponent and variable do not depend on each other, we check from which side $\cos ^{2}x$ approaches 1 and since it does so from left side, $(1^{-})^{\infty} = 0$


## $0^{0}\ \&\ \infty^{0}$ Form

$$\lim_{ x \to 0^{+} } x^{x} = 1$$
As,
$$\lim_{ x \to 0^{+} } x^{x} = \lim_{ x \to 0 } e^{x\ln x} = e^{0} = 1$$

Using this we get,
$$\lim_{ x \to 0^{+} } \left( \frac{ 1 }{ x } \right)^{x} = 1$$

1. Separate question into LHL and RHL.
2. If $x\to 0^{-}$ then the Limit Does not Exist as exponential function cannot take -ve values. 
3. For RHL, first take log both sides.
4. Convert the obtained expression into $\displaystyle \frac{0}{0}\ \ce{ or\ } \frac{ \infty  }{ \infty }$ form.
5. Apply L Hospital's Rule.
6. Take anti log for final answer.