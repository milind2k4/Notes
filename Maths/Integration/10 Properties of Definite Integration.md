Links: [[09 Definite Integration]]
___
# Properties of Definite Integrals
1. $$\int_{a}^{b} f(x) \, dx = -\int_{b}^{a} f(x) \, dx $$
	$\\$

2. $$\int_{a}^{b} f(x) \, dx = \int_{a}^{b} f(t) \, dt $$
	$\\$

3. $$\int_{a}^{b} f(x) \, dx = \int_{a}^{c} f(x) \, dx + \int_{c}^{b} f(x) \, dx $$
   Here, c could be outside $(a,b)$ also, but $f(x)$ should be continuous between a to c and between c to b.
   
   This can be used to integrate functions which are discontinuous or undefined at discrete points between a and b. Or a functions which change its definition in the interval of integration.
	$\\$

4. $$\int_{a}^{b} f(x) \, dx = \int_{a}^{b} f(a+b-x) \, dx $$
	This is the most #important property. It is always valid. 
> Proof:
> $$
> \begin{split}
> \int_{a}^{b}& f(x) \, dx \\
> \text{We substitute},\ x &= a + b - t \\
> \text{Which gives,} \\
> dx &= -dt \\
> t &\in (b,a) \\
> \text{Thus,} \\
> \int_{b}^{a} f(a+b - t) \, (-dt) &= \int_{a}^{b} f(a+b - t)  \, dt \\
> \\
> \text{Therefore finally,} \\
> \int_{a}^{b} & f(a+b - x) \, dx 
> \end{split}
> $$

$\\$

5. $$\int_{0}^{2a} f(x) \, dx = \int_{0}^{a} [f(x) + f(2a-x)] \, dx $$
   
	- $f(2a-x) = f(x) \implies I= 2\int_{0}^{a} f(x) \, dx$
	- $f(2a-x) = -f(x) \implies \displaystyle I = 0$
	  
	> Proof:
	> $$
	> \begin{split}
	> \int_{0}^{2a} f(x) \, dx &= \int_{0}^{a} f(x) \, dx + \int_{a}^{2a} f(x) \, dx \\
	> \text{Substitute in the 2nd one},\ x &= 2a - t \\
	> \text{This gives,} \\
	> dx &= -dt \\
	> t &\in (a,0) \\
	> \\
	> \text{Thus,} \\
	> \int_{a}^{2a} f(x) \, dx &= \int_{a}^{0} f(2a - t) \, (-dt) \\
	> &= \int_{0}^{a} f(2a - x) \, dx  
	> \end{split}
	> $$
	
	$\\$

6. $$\int_{-a}^{a} f(x) \, dx = \int_{0}^{a} [f(x) + f(-x)] \, dx $$
	- If $f(x)$ is even (i.e. $f(-x) = f(x)$, $I = 2\int_{0}^{a} f(x) \, dx$
	- If $f(x)$ is odd (i.e. $f(-x) = -f(x)$), $I = 0$
	  
	Proof is just like the previous, just put $x = -t$ in the 1st integral.
	$\\$

7. If $f(x)$ is [[00.4 Periodic & Non-Periodic|periodic]] with period $T,$ then, 
   
	1. $\displaystyle \int_{a}^{a+T} f(x) \, dx$ will be independent of a i.e. we can put any value of a. I.e. the algebraic area of a cycle will be the same regardless of the starting point. 
		> Proof: 
		> $$
		> \begin{split}
		> \int_{a}^{a+T} f(x) \, dx &= \int_{a}^{0} f(x) \, dx + \int_{0}^{T} f(x) \, dx + \int_{T}^{a+T} f(x) \, dx \\
		> \text{Substitute in the 3rd},\ t &= x - T \\
		> \text{This gives,} \\
		> dt &= dx \\
		> t &\in (0,a) \\
		> \\
		> \text{Thus,} \\
		> \int_{a}^{a+T} f(x) \, dx &= \int_{a}^{0} f(x) \, dx + \int_{0}^{T} f(x) \, dx + \int_{0}^{a} f(t) \, dt \\
		> &= \int_{0}^{T} f(x) \, dx 
		> \end{split}
		$$

   $\\$
   
	2. $\displaystyle \int_{0}^{nT} f(x) \, dx = n\int_{0}^{T} f(x) \, dx$
	   Here n has to be integer and T has to be a period. 
	   $\\$
	
	3. $\displaystyle \int_{n_{1}T}^{n_{2}T} f(x) \, dx = (n_{2}-n_{1})\int_{0}^{T} f(x) \, dx$ 
	   $\\$
	
	4. $\displaystyle \int_{a+nT}^{b+nT} f(x) \, dx = \int_{a}^{b} f(x) \, dx$
	   Here we are moving the interval (a, b) by some multiple of period. We can prove this by simply substituting $t= x - nT$ and since function is periodic, $f(t + nT) = f(t)$.
	   $\\$

8. $$\int_{a}^{b} f(x) \, dx = (b-a)\int_{0}^{1} f(a+(b-a)x) \, dx$$
   For Proof we simply substitute $x = a + (b-a)t$.
	- $\displaystyle \int_{a}^{a} f(x) \, dx = 0$

## [[10.5 DI Examples]]