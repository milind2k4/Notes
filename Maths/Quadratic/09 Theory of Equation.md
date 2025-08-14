Links: [[00 Quadratic Equations and Expressions]]

___
# Theory of Equation
#important 

Let
$$f(x) = a_{n}x^{n} + a_{n-1}x^{n-1} + a_{n-2}x^{n-2} +.......+a_{1}x + a_{o} = 0$$
where $a_{i} \in R\ , i = 0,1,2, ....... n$ 


- If $a_{n} \neq 0$ then $f(x)$ is a polynomial of degree $n$ and has exactly $n$ roots. Say $\alpha_{1}\ ,\alpha_{2}\ ,\alpha_{3}\ .......\alpha_{n}.$
- $a_{n}$ is called leading coefficient. 

## Identity Conversion

$$f(x) \equiv a_{n}(x - \alpha_{1})(x - \alpha_{2})(x - \alpha_{3}).......(x - \alpha_{n})$$

> This can be multiplied and written as:
> $$\begin{split}
> f(x) & = x^{n-1} \sum \alpha_{i} \\
> &\ + x^{n-2} \sum \alpha_{i}\alpha_{j} \\
> &\ + x^{n-3} \sum \alpha_{i}\alpha_{j}\alpha_{k} \\
> &\ \ \ . \\
> &\ \ \ . \\
> &\ \ \ . \\
> &\ (-1)^{n}\ x^{0} \alpha_{i}\alpha_{j}\alpha_{k}.......\alpha_{n}
> \end{split}$$

This is an identity hence coefficients can be compared 
> $$\begin{split}
> a_{n} & = a_{n} \\
> a_{n-1} & = a_{n} \sum \alpha_{i} \\
> a_{n-2} & = a_{n} \sum \alpha_{i}\alpha_{j}\ (i < j) \\
> a_{n-3} & = a_{n} \sum \alpha_{i}\alpha_{j}\alpha_{k} 
\ (i < j< k)\\
> &\; \; . \\
> &\; \; . \\
> a_{o} & = a_{n}\ \alpha_{i}\alpha_{j}\alpha_{k}.......\alpha_{n}
> \end{split}$$
	
Therefore, 
> $$\begin{split}
> a_{n} & = a_{n} \\
> -\frac{a_{n-1}}{a_{n}} & = \sum \alpha_{i} \\
& = \text{ Sum of roots taken 1 at a time} \\
> \frac{a_{n-2}}{a_{n}} & = \sum \alpha_{i}\alpha_{j} \\
& = \text{ Sum of roots taken 2 at a time} \\
> -\frac{a_{n-3}}{a_{n}} & = \sum \alpha_{i}\alpha_{j}\alpha_{k} \\
& = \text{ Sum of roots taken 3 at a time} \\
> &\; \; . \\
> &\; \; . \\
> &\; \; . \\
> (-1)^{n}\frac{a_{o}}{a_{n}} & = \alpha_{i}\alpha_{j}\alpha_{k}.......\alpha_{n} \\
& = \text{ Sum of roots taken n at a time} \\
& = \text{ Product of the roots} \\
> \end{split}$$

#### For a cubic
$$ax^{3} + bx^{2} + cx + d = 0$$
having roots $\alpha,\beta,\gamma$

$$\alpha + \beta + \gamma = \frac{-b}{a}$$
$$\alpha \beta + \alpha \gamma + \beta \gamma = \frac{c}{d}$$
$$\alpha \beta \gamma = \frac{-d}{a}$$

If there is a cubic in the question, put -2,-1,0,1,2 and check if they are its roots. 

#### For a Biquadratic
$$ax^{4} + bx^{3} + cx^{2} + dx + e = 0$$
having roots $\alpha, \beta, \gamma, \delta$,

$$\alpha + \beta + \gamma + \delta = \frac{-b}{a}$$
$$\alpha \beta + \alpha\gamma + \alpha\delta + \beta \gamma + \beta \delta + \gamma \delta = \frac{c}{a}$$

this can be written as,
$$(\alpha + \beta)(\gamma + \delta) + \alpha \beta + \gamma \delta = \frac{c}{a}$$
and it works with any two roots

$$\alpha \beta \gamma + \alpha \beta \delta + \alpha \gamma \delta + \beta \gamma\delta = \frac{-d}{a}$$

$$\alpha \beta \gamma \delta = \frac{e}{a}$$


## Properties of Roots
1. If $f(x)$ is satisfied for more than $n$ distinct values of $x$ then $f(x)$ is an identity i.e. it will be satisfied $\forall\ x$, and also in this case all coefficients are 0. 

2. If $a_{n} \neq 0$ and if coefficients are real, then imaginary roots (if existing) will occur in conjugate pairs. 
   - Any polynomial equation with real coefficients will have even number of imaginary roots. 
   - Any odd degree polynomial with real coefficients will always have at least one real root. (or odd number of real roots.)

	Note that a polynomial equation with rational coefficients can have one irrational root. 
	e.g. $x^{3} = 7$ will have one irrational and 2 imaginary roots. 


3. If the coefficients are integers and if the equation has a rational root, $\displaystyle \frac{p}{q}$ (say) then **$p$ must divide $a_{o}$ and $q$ must divide $a_{n}$**. 
   
   this fact can be used to check if an equation has any integral roots or not,
   ![[Pasted image 20230509075846.png]]
   
### Notes on Question Solving
- If we have to find a condition for something and in any step we find one of the roots in terms of the known quantity, just put the root back in the equation. This will give the required condition. 

- If we see something like $(\alpha - a)(\beta - a)(\gamma - a).......$, try to convert the given equation into the identity as in [[09 Theory of Equation#Identity Conversion|conversion]].









