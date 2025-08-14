Links: [[05 Maxima and Minima]], [[01 Partial Differentiation]]
___
# Multivariable Maxima and Minima

Aka, extreme of multivariable function. 

**Maximum value:** A function $f(x,y)$ is said to have a maximum value at $x=a, y=b$ if there exist a small neighborhood of $(a,b)$ such that,
$$f(a,b) > f(a+h,b+k)$$

**Minimum value:** A function $f(x,y)$ is said to have a minimum value at $x=a, y=b$ if there exist a small neighborhood of $(a,b)$ such that,
$$f(a,b) < f(a+h,b+k)$$

### Working Rule 
To find extreme values. 

1. Differentiate $f(x,y)$ and find out,
   $$\underbrace{ \frac{ \partial f }{ \partial x } }_{ p }, 
   \underbrace{ \frac{ \partial f }{ \partial y } }_{ q }, 
   \underbrace{ \frac{ \partial^{2} f }{ \partial x^{2} } }_{ r }, 
   \underbrace{ \frac{ \partial^{2} f }{ \partial x \partial y } }_{ s }, 
   \underbrace{ \frac{ \partial^{2} f }{ \partial y^{2} } }_{ t }$$

2. Then put, 
   $$\frac{ \partial f }{ \partial x } = 0$$
   $$\frac{ \partial f }{ \partial y } = 0$$
   Solving these two, find point(s) $(a,b)$
   $\\$

3. Find, $r,s,t$ at the point(s).
   $\\$

4. Find,
	$$rt-s^{2}$$

Based on this value, we have three cases,
- **Case 1:**
	$$rt-s^{2} > 0$$
	Then,
	$r < 0 \implies$ $f(x,y)$ has max. value. 
	$r > 0 \implies$ $f(x,y)$ has min. value. 
	$\\$

- **Case 2:**
	$$rt - s^{2} < 0$$
	Then, $f(x,y)$ has no extremum value at $(a,b)$ and it is called a *saddle point.*
	$\\$

- **Case 3:**
	$$r t - s^{2} = 0$$
	Then the case fails and we cannot find the extremum using this. 
	Thus we reject such points. 


