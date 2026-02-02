Links: [[06 Graph of Quadratic]], [[07 Sign of Quadratic Expression]]
___
# Location of Roots
Let,
> $$f(x) = ax^{2}+bx + c$$
> where $a \neq 0\ \&\ a,b,c \in R$

then with respect to the equation $f(x) = 0$;
## $k$ lies between the roots
Finding $a$ when a number $k$ lies between the roots. 
i.e. Find $a$ if $k$ lies between the roots of the equation $f(x)$.

We just have to solve the inequality 
> $$a \cdot f(k) < 0$$
> from [[07 Sign of Quadratic Expression#When D > 0]]

![[Pasted image 20230511091243.png]]

## One root lies between $k_1$ and $k_2$
One root lies between two numbers $k_1$ and $k_2$ which themselves are not the roots.
i.e. Find $a$ if $f(x)$ have roots such that $|\alpha| > k$ and $|\beta| < k$. (in this case specifically we have to take $k_{1} = k$ and $k_{2} = -k$)

We just have to solve the inequality 
> $$f(k_1) \cdot f(k_2) < 0$$
> from [[07 Sign of Quadratic Expression#Conditions]]

![[Pasted image 20230511091424.png]]

## $k$ > both the roots
There should be real roots. $k$ should be greater than both the roots. 
i.e. Find $a$ if the roots of $f(x)$ are more than $k$

We just have to take the intersections of the solutions the inequalities
> $$D \geq 0$$
> $$a \cdot f(k) > 0$$
> $$k > \frac{-b}{2a}$$
> from [[07 Sign of Quadratic Expression#When D > 0]]
> (the last one makes sure that $k$ is more than both the roots.)

![[Pasted image 20230511091506.png]]

## $k$ < both the roots
There should be real roots. $k$ should be less than both the roots.   
i.e. Find $a$ if the roots of $f(x)$ are less than $k$

We just have to take the intersections of the solutions the inequalities
> $$D \geq 0$$
> $$a \cdot f(k) > 0$$
> $$k < \frac{-b}{2a}$$
> from [[07 Sign of Quadratic Expression#When D 0]]
> (the last one makes sure that $k$ is less than both the roots.)

![[Pasted image 20230511091536.png]]

#### Note
if we fix the value of a root, (say the fixed value is $\alpha$) we don't have to take inequalities. 
Take $f(\alpha) = 0$, find the value of the parameter, put it back in $f(x)$ and find the 2nd root using product of the roots. (or any other method). Then check if the 2nd root is valid or not. 

- Link to videos:
	- [Example](https://youtu.be/hLCjd5vYiNY?list=PL_A4M5IAkMaf5Ga3nQJe-gg-0zXG77YRB&t=493)
	- [Statement](https://youtu.be/hLCjd5vYiNY?list=PL_A4M5IAkMaf5Ga3nQJe-gg-0zXG77YRB&t=794)

![[Pasted image 20230511094237.png]]

Try to see whether the quadratic can be expressed in the form $x^{2} -Sx + P= 0$. This will reduce the calculations very much.

![[Pasted image 20230511093946.png]]

Convert "at least" and "at most" into exactly and take cases for each. i.e. if it says at least one root more than 2, then we convert it into 2 cases, C-1: exactly one root more than 2 and C-2: both roots more than 2.

If conditions cannot be applied directly, then convert the question into cases. 

## Examples
![[Pasted image 20230511092311.png]]