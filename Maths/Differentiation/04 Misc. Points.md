Links: [[00 Differentiation]]
___
# Misc. Points 
For a straight line, $y' = c$ (constant) and $y'' = 0$. 

To get joint equation of two curves multiply their equations by first making RHS equals to zero. 

Let, 
$$C_{1}: y = x^{2}$$
$$C_{2}: y^{2} + x^{2} = 9$$
Then joint equation of $C_{1}, C_{2}$ can be given as,
$$(y-x^{2})(x^{2} + y^{2} - 9) = 0$$

#### Lines Passing Through Origin
For a line passing through origin,
$$\frac{ dy }{ dx } = \frac{ y }{ x }$$
But this is only true for points on the curve. 

Any homogeneous polynomial equation in x and y, say of degree n, represents n-straight lines (real or imaginary) passing through origin and for any such equation $y' = y /x$ and $y'' = 0$. #important 

We can differentiate identities, but we cannot differentiate equations or inequalities. 
Thus,
$$f > g \centernot\implies f' > g'$$

#### Polynomial Expansion
If polynomial expansion of some function is given like,
$$f(x) = a_{o} + a_{1}x + a_{2}x^{2} + \dots$$
Then coefficient of $x^{r}$,
$$a_{r} = \frac{ f^{(r)}(0) }{ r! }$$

We can see this by differentiating say, 2 times, which gives,
$$f''(x) = 2.1.a_{2} + 3.2.a_{3}.x + 4.3.a_{4}.x^{2}$$
And putting $x = 0$ in this gives,
$$a_{2} = \frac{ f^{(2)}(0) }{ 2! }$$

#### Repeated Roots
If $p(x)$ is a polynomial and if it has a repeated root $\alpha$, with degree of repetition as $r$, i.e.
$$p(x) = (x-\alpha)^{r}. q(x),\ q(\alpha) \neq 0$$
then, 
$$p(\alpha) = p'(\alpha) = p''(\alpha) = \dots = p^{(r-1)}(\alpha) = 0$$
And,
$$p^{(r)}(\alpha) \neq 0$$

So if $\alpha$ is a repeated root,
$$p(\alpha) = p'(\alpha) = 0$$
This can be used to show repetition of root. 

If alpha repeats r times in $p(x)$, then in $p'(x)$ it will repeat $r-1$ and in $p''(x)$ it will repeat $r-2$ times and so on.

#### Equivalency
We have,
$$f \equiv g \implies f' \equiv g'$$
But,
$$f' \equiv g' \implies f \equiv g + c$$
where c is an arbitrary constant which can also be zero. 

Thus if we want to prove that $f \equiv g$ then we can show $f' = g',\ \forall\ x$ and $f(a) = g(a)$ for some $a$. 
