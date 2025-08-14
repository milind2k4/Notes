Links: [[01 Logarithms]], [[01 Algebraic Inequalities]], [[02 Properties of Log]], [[03 Base Changing Theorem]]
___
# Basic Maths
### General

Number just greater (or less)  than a given number $'\alpha'$ does not exist.

Also, $1.\bar{9} = 2$. 
This is because we cannot find any numbers between those two. 

$\pm \infty$ is not a number, it is a notion.
$$
\begin{split}
\frac{1}{0} &\neq \infty \\
&=  \text{Undefined} \\
\frac{1}{\infty} &\neq 0 \\
&= \text{Undefined}
\end{split}
$$

**Symbols,**
- $\forall$ is "for all".

- $\exists$ is "there exists".

- $\implies$ is "implies".

- $\iff$ is "implies and is implied by"

- $\equiv$ is "identical".

- $\subseteq$ is "either subset of or equal to"

- $\sim$ is "difference" (it means $|a-b|$)

- $a|b$ is "a divides b" i.e. "b is divisible by a"

- $iff$ is "if and only if", it is the same as $\iff$


### Roots and Squares
$\sqrt{x}$ is always non-negative. $i.e.\sqrt {x} \geq 0$ if defined.


$\sqrt[a]{x^{a}} \neq x,$
-   $\sqrt[a]{x^{a}} = |x|$ if a is even 
-   $\sqrt[a]{x^{a}} = x$, if a is odd


- $\sqrt[m]{ x }$ can only be written when $m \in N - \{ 1,2 \}$.

- For $x^{1/m}$ to be defined m can only be integer or rational number.
	$\\$
	
- If we square any equation then extra root may come in the solution. Hence we need to check final solution with the original equation. 

### Inequalities, general
- $A > B \implies A +k > B + k$
- $A > B \implies kA > kB$ if $k > 0$ & $kA < kB$ if $k < 0$
- $A > B \implies \displaystyle \frac{1}{A} < \frac{1}{B}$
	$\\$
	
- $a^{x_{1}} > a^{x_{2}} \iff x_{1} > x_{2}$ if $a > 1$
- $a^{x_{1}} > a^{x_{2}} \iff x_{1} < x_{2}$ if $a \in (0,1)$
	$\\$
	
- If we are uncertain about the sign of a number in [[01 Algebraic Inequalities| an inequality]], we cannot perform multiplication.
- $AB > AC \centernot\implies B > C$
- $A+B > A+C \implies B > C$
	$\\$
	
- $(A > B) + (C > D) \implies A+C > B+D$ 
  Subtraction and division is not valid. Multiplication is only valid when all quantities are $+ve$
	$\\$
	
- If there are two inequalities and all the numbers involved are +ve, then we can multiply them. 

## General Question Solving

- If we are solving a question by splitting it into cases and the solution of Case-1 comes to be S-1, then we will have to take the intersection between Case-1's condition and the solution S-1. 
- To get the final answer, we have to take the union of all the Case - Solution intersections.
	**Eg:**
	- Case-1: S-1
	- Case-2: S-2
	- Final answer: (Case-1 $\cap$ S-1) $\cup$ (Case-2 $\cap$ S-2)
	$\\$
	  
- An equation true for all $x$  is an identity. 
	- If an expression is an identity, then we can equate the coefficients of variables.
	$\\$
	
- If the question uses *at least* or *at most*, convert the question into *exactly* and then add the results for each case. 
	$\\$
	
- Do not cancel a term from both sides as by doing so a root might be lost which might be in the answer.
	$\\$
	
- If there is a cubic, then the root of the cubic will be of the type p/q where p will divide the constant term and q will divide the coefficient of $x^{3}$.
	$\\$
	
- If there are 3 or more variables and we have to find them using one equation, most probably, the equation will be solved on the edge of its range (i.e. the max or the min value). [[00 Inverse Trigonometric Functions#Examples]]

- While comparing coefficients from two equations, if any one of the corresponding coefficients are equal then the remaining coefficients can be equalled. 

## Points to Remember
1. For a mathematical statement to be true, it should always be true, i.e. there should be no exception. If we can show a single case where the statement is false, then the statement is false. 
	$\\$
   
2. $0 . \text{(Anything)} \neq 0,\ 0. \text{(Anything defined)} = 0$.
	$\\$

3. $N \subset W \subset I \subset Q \subset R \subset Q$
	$\\$

6. $\displaystyle \frac{A}{B} = 0$ then $A=0$ and $B \neq 0$. Thus, $\displaystyle \frac{A}{\frac{B}{C}} = \frac{ AC }{ B },\ C \neq 0$. And $\displaystyle \frac{1}{B}$ can never be zero. 
	$\\$

7. For $(f(x))^{g(x)}$ to be defined $f(x)>0$
	$\\$

8. $\sqrt{ ab } = \sqrt{ a }\sqrt{ b }$ if at least one of a,  b is non-negative. 
	$\\$

9. Number of integers between n and m = $m-n-1$ (m > n)


## Elimination
1. To solve n variables we need n equations. 
2. To eliminate n variables, we need (n+1) equations. 
3. The absence of variable in final result/equation may imply elimination of that variable. 

## Misc. Concepts

- In case of equation $|f(x)| \pm |g(x)| = |h(x)|$ first check if $f(x) \pm g(x) = h(x)$. If yes then break it using properties of modulus.
	$\\$

- LCM of Two numbers
	1. LCM(a, b) will be an integral multiple of both the numbers. 
	2. LCM of rational and irrational number does not exist. But of two irrational may exist. 
	   $$\begin{split}
		LCM(\sqrt{ 2 }, \sqrt{ 3 }) &= DNE \\
	   LCM(\sqrt{ 2 }, \sqrt{ 8 }) &= 2\sqrt{ 2 } \\
	   LCM\left( \sqrt{ 2 }, \frac{1}{\sqrt{ 2 }}\right) &=  \sqrt{ 2 } \\ 
		\end{split}
	   $$
	1. LCM of fractions,
	   $$LCM\left( \frac{ p }{ q }, \frac{ r }{ s } \right) = \frac{ \text{LCM of num.} }{ \text{HCF of denom.} }$$


- Values of $e$,
	$$
	\begin{split}
	e &= 2.7 \\
	\frac{1}{e} &= 0.37 \\
	1 - \frac{1}{e} &= 0.63
	\end{split}
	$$

- No of digits in $r, r+1, r+2 \dots n$ = last - first + 1 
  (only works for common difference = 1)


#### Componendo and Divinendo  
If,
$$\frac{a}{b} = \frac{c}{d} = \frac{e}{f} = \lambda$$
then,
$$a = \lambda b,\ c = \lambda d,\ e = \lambda f$$
$$\frac{ a+b }{ a-b } = \frac{ c+d }{ c-d } = \frac{ e+f }{ e-f } = \frac{ \lambda+1 }{ \lambda-1 }$$
$$\frac{ a }{ a+b } = \frac{ c }{ c+d } = \frac{ e }{ e+f } = \frac{ \lambda }{ \lambda+1 }$$
$$\frac{ a^{2}+b^{2} }{ ab } = \frac{ c^{2}+d^{2} }{ cd } = \frac{ e^{2}+f^{2} }{ ef } = \frac{ \lambda^{2}+1 }{ \lambda }$$

Also,
$$\frac{ a+c }{ b+d } = \frac{ a+3c+3e }{ b+2d+3f } = \lambda$$
this also works with subtraction.

And,
$$\displaystyle a = \frac{1-b}{1+b} \iff \displaystyle b = \frac{1-a}{1+a}$$

Example,
![[Pasted image 20230422072840.png]]


#### Symmetric Equations
An expression in $\alpha$ and $\beta$ is called symmetric if interchanging $\alpha$ and $\beta$ has no effect on the expression. 

- We can find an expression in $\alpha, \beta$ using $\alpha+\beta$ and $\alpha \cdot \beta$

For example, 
$\displaystyle \frac{\alpha}{\beta} + \frac{\beta}{\alpha}$ is Symmetric. 
$\alpha^{2} + \beta^{2}$ is Symmetric. 
$\alpha^{2} - \beta^{2}$ is not Symmetric. 
$|\alpha^{2} - \beta^{2}|$ is Symmetric. 

If the expression  is not symmetric, then we take cases, one when $\alpha$ is the +ve one and one when it is -ve. 