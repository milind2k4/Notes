Links: [[02 Properties of Log]], [[03 Base Changing Theorem]]
___
# Logarithms
$\log _{b}(a)$ is read as "$\log$ $a$ to the base $b$" and is a number when raised on $b$ will produce $a$. Also, both $a, b > 0$ and $b \neq 1$.

- $a$ is called argument and $b$ is the base.

Log converts multiplication to addition and division to subtraction. 
It is used to simplify calculation.

If base of log is $e$ then it is called **Natural Log** and it is denoted as $\ln x$ i.e. $\log_{e}x$.
put x = 1 in expansion of e, [[02 Formula and Expansions#Expansions]]

 Let $\log _{b}(a)  = k$, then $a = b^{k}$
 ($k$ could be $+ve$ as well as $-ve$)

$-3^{3}= -27$ cannot be represented as log.

-  If $b > c$
	- $\log_{a}b > \log_{a}c$
	- $\log_{b}a < \log_{c}a$
- If defined, $\log_{a}b = \log_{a}c \implies b = c$
	Since log is one one function, we can do this. 
- To remove log we must have same base for both logs and coefficient of each log must be same. 

**Note:** while solving questions involving logs, cross check the solutions with the original expression. 

For example,
![[Pasted image 20230426082954.png|300]] 
![[Pasted image 20230426083035.png|300]]

### Domain of Logarithms
$\log _{b}(a)$, $a \in (0, \infty)$ & $b \in (0,1) \ \cup \ (1, \infty)$

#### In case we need to find domain
Take three inequalities $a > 0,\ b > 0\ \&\ b \neq 1$ and find the intersection of their solutions.
i.e. $(a > 0)\ \&\ (b > 0)\ \&\ (b \neq 1)$

## Logarithm Inequality 
#important 

1. Find domain of inequality (the original one).
	- In case of multiple $\log$s we need to find domain according to the last log (i.e. the outermost one). Make whatever is inside of it more than 0.  

	- We can solve without finding domain when it is an equality. In that case we need to put the values obtained back into the original expression to see if it is satisfied.  
	- From consideration of base, calculation may be reduced. 
	- It could also be that within the domain, the variable expression is always +ve. 

3. Remove $\log$ and solve obtained inequality.
	> If the base of $\log$ is smaller than 1, the direction of inequality is changed. [[04 Sign of Logarithm]]
	
	> **Proof:**
	> $$\begin{flalign}
	> \text{Let,}\ & \log_{\frac{1}{a}}b \geq \log_{\frac{1}{a}}c \\
	> \implies & -\log_{a}b  \geq -\log_{a}c \\
	> \implies & \log_{a}b  \leq \log_{a}c
	> \end{flalign}$$
	
	- If the base is also a variable, we need to use cases. 
		- Find the value for which the base is 1.
		- The base is less than 1 before this value and more than 1 after this value. 
		- Take cases accordingly, solve them and for the final solution, take the intersection of the solutions with the cases and the union of the intersections. As mentioned in [[00 Basic Mathematics#General Question Solving|General Question Solving]]

3. Take intersection of the solution in 2 with the domain.

## Sign of Logarithm:
- If both $b\ \&\ a$ are on the same side of 1, then $\log_{b}a > 0\;\; \text{i.e. } +ve$. If they are on either side, then it is $-ve$.

- If $b$ is greater than 1 and 
	- $a>b$, then $\log_{b}a > 1$.
	- $a<b$, then $\log_{b}a < 1$.

- If $b$ is less than 1 and 
	- $a>b$, then $\log_{b}a < 1$.
	- $a<b$, then $\log_{b}a > 1$.

![[Sign and comp w 1 of log.png]]

## Solving Questions
$$\log_{a}b = \alpha, \log_{c}d = \beta. \text{Find},\ \log_{e}f$$

1. Find all the primes involved in the question

2. Take one of those primes as the base and convert all $\log$ into that base using [[03 Base Changing Theorem]]

3. Take variables like $x,y$ when needed and express $\alpha\ \&\ \beta$ in terms of $x\ \&\ y$. 

4. Make $\log_{e}f$ in terms of the chosen prime as in step 2. And express it in terms of previously chosen $x\ \&\ y$.

5. Express this result in terms of $\alpha\ \&\ \beta$

Example,
![[Pasted image 20230427074643.png]]

- In equation we can solve normally and then finally cross check with the original equation.
- In inequality, we have to find domain and solution and take their intersection for final answer. 
  

## Expansion

$$\log_{e}(1+x)= x - \frac{x^{2}}{2} + \frac{x^{3}}{3} - \frac{x^{4}}{4} + \dots \infty$$

## Comparison between Logs
If argument is the same, the one with smaller base is larger as we have to raise that small number to a higher power to get the same argument. 
i.e. if $b > c$ then $\log_{b}a < \log_{c}a$

If base is same, the one with greater argument is the bigger number. Because we need to raise the same number to a higher power to get the greater argument. 
i.e. if $b > c$ then $\log_{a}b > \log_{a}c$

In case of both the argument and base being different, make the base of both as close as possible. Then use the previous two properties to compare.

![[Pasted image 20230428085220.png]]