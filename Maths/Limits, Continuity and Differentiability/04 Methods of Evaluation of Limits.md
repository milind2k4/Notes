Links: [[00 Limits]], [[03 Evaluation of Limits]] 
___
# Methods of Evaluation of Limits
## Algebraic manipulation
(factorisation, rationalisation, cancellation etc. )

#### By Division by a power of $x$
If the form is of 
$$\displaystyle \lim_{x\to \infty} \frac{\text{polynomial}}{\text{polynomial}}$$
then divide both the polynomials by the degree of expression. 
eg. $x^{3}$ in, $$\frac{x^{2} + 3x + 4}{x^{3}+8x+3}$$

If there are roots, if we divide by $x$, the inside of root will be divided by $x^{2}$
$$\frac{\sqrt{a}}{x} = \sqrt{\frac{a}{x^{2}}}$$

### Points to Remember
1. If $x \to 0$, then for a polynomial the least degree term will be the dominating term and the rest of the terms can be neglected.
   Provided the polynomial is in product form of the whole expression.
	- eg. $x \to 0: 5 + x + 8x^{3} \approx 5$
	  $\\$

2. If $x \to \infty$ then in a polynomial the highest degree term will be the dominating term, and if this polynomial is present in product form of entire expression, then the other lower  degree terms can be neglected. 
	- eg. $x \to \infty: 5x^{4} + 8x^{20} + 25 \approx 8x^{20}$
	  $\\$

3. **Effective Degree:** The exponent of the dominating term. 
	- eg. $x \to 0: x^{2} + 3x$ Effective degree: 1
	- eg. $x \to \infty: x^{2} + 3x$ Effective degree: 2
	  $\\$

4. If effective degree term is getting cancelled in sum form (i.e. $x^{4} - x^{4}$), then we do not use cancellation. 
   
This is allowed,
![[Limits Example.png]]

This is not allowed as the E.D. terms cancel,
![[Limits Example 2.png]]

5. If $x \to 0$ then w.r.t the E.D:
   
	$$
	\begin{split}
	\frac{H}{L} \left(\frac{x^{2}}{x} \right) &= 0 \\
	\frac{L}{H} \left(\frac{x}{x^{2}} \right) &= DNE\, (\to \pm \infty) \\
	\frac{E}{E} \left(\frac{3x^{2}}{5x^{2}} \right) &= a \\
	\end{split}
	$$ 
	where $a$ is a non-zero number.
	$\\$


5. If $x \to \pm \infty$ then w.r.t the E.D:
	$$
	\begin{split}
	\frac{H}{L} \left(\frac{x^{2}}{x} \right) &= DNE\ (\to \pm \infty) \\
	\frac{L}{H} \left(\frac{x}{x^{2}} \right) &= 0 \\
	\frac{E}{E} \left(\frac{3x^{2}}{5x^{2}} \right) &= a
	\end{split}
	$$
	where $a$ is a non-zero number.
	$\\$


1. If $x \to a$ then if $t = x - a \implies t \to 0$
1. If $x \to -\infty$ then if $t = -x \implies t \to \infty$
1. If $x \to \infty$ then if $t = \displaystyle \frac{1}{x} \implies t \to 0^{+}$

## Binomial Expansion
We use Binomial expansion when $x \to 0$ and n can be any rational or -ve number. 

$$(1+x)^{n} = n\in R
\implies 1 + nx + \frac{n(n-1)}{2!}x^{2} + \frac{n(n-1)(n-2)}{3!}x^{3} + \frac{n(n-1)(n-2)(n-3)}{4!}x^{4} +...$$


Expand to the term one after the term that is getting cancelled in sum form. If we write more terms, the answer will be the same, but if we write less, the answer might change. So when in doubt, expand till some extra terms. 

If $n \in N$, then,
$$(1 + x)^{n} = {}^{n}C_{0} + {}^{n}C_{1}x + {}^{n}C_{2}x^{2} + {}^{n}C_{3}x^{3} + \dots {}^{n}C_{n}x^{n}$$

For example, in
$$\lim_{x \to 0} \frac{(1+3x)^{1/4}-1}{x^{2}}$$
the $1$ in the binomial expansion is getting cancelled so we will expand till the $nx$ term. 

![[Pasted image 20230801092656.png]]

If there are cube roots and square roots, we use binomial expansion,
![[Pasted image 20230805081953.png]]


## L' Hôpital's Rule (LH Rule)

If $f(x)$ and $g(x)$ both $\to 0$ or $\to \pm \infty$ as $x \to a$ then,
$$\lim_{ x \to a } \frac{ f(x) }{ g(x) } = \lim_{ x \to a } \frac{ f'(x) }{ g'(x) }$$
Provided limit on RHS exists, which can be found using any method.



This can only for 0/0 or $\infty/\infty$ forms. 
If on RHS LH rule is applied again, we have to check if it is 0/0 or $\infty /\infty$ form. 

- If limit **exists:** LH Rule is applicable
- If limit **does not exist:** 
	- LHL and RHL are both finite but unequal: LH Rule applicable 
	- LHL or RHL or both $\to \pm \infty$: LH Rule applicable 
	- Value of function fluctuates: LH Rule not applicable and solve LHS only without LH rule. 

![[Pasted image 20230807121939.png]]

If on differentiating, the expression increases in size, we do not use LH rule.

![[Pasted image 20230807115228.png]]
![[Pasted image 20230807115241.png]]

## Standard Limits
Try to convert the given expression into one of [[05 Standard Limits#Collectively]]

## Substitution
Convert the limit into $x \to 0$ by substituting $x-a=t$. But put $t+a$ at x's place in the expression. 

If $x \to \infty$, then we substitute $x = 1/t \implies t \to 0^{+}$ 
If $x \to -\infty$, then we substitute $x = -t \implies t \to \infty$ 

![[Pasted image 20230201192544.png]]

## [[04.5 Expansion]]
