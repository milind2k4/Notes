Links: [[00 Sequence and Series]]
___
# Inequalities
1. [[02 Modulus Inequalities]]
	$$||a|-|b|| \leq |a+b| \leq |a| + |b|$$
	For the first inequality to hold, $a.b \leq 0$
	For the 2nd inequality to hold, $a.b \geq 0$
	$\\$

2. Triangle Inequality
	In triangle ABC, if a, b, c are the sides then,
	$$a+b > c$$
	$$b+c > a$$
	$$c+a > b$$
	This can also be written as,
	$$a \sim b < c$$
	$$b \sim c < a$$
	$$c \sim a < b$$
	where $\sim$ means difference
	$\\$

3. For any 3 numbers x, y, z $\in R$ then,
	Using square of sum,
	$$
	\begin{split}
	(x+y+z)^{2} &\geq 0 \\
	x^{2} + y^{2} + z^{2} + 2(xy + yz + zx) &\geq 0
	\end{split}
	$$
	Which gives,
	$$\sum x^{2} \geq -2\left( \sum ab \right)$$

	Using sum of square of difference,
	$$
	\begin{split}
	(x-y)^{2} + (y-z)^{2} + (z-x)^{2} &\geq 0\\
	\end{split}
	$$
	Which gives,
	***$$x^{2} + y^{2} + z^{2} \geq xy + yz + zx$$***
	for equality, $x = y = z$
	$\\$

4. If there exists a real solution of quadratic equation $ax^{2} + bx + c =0$ then $D \geq 0$. But this can only be application if the variable can give all real values.

#### Weighted AM-GM
Let $a_{1},a_{2},a_{3},a_{4}\dots$ be n +ve numbers and $w_{1},w_{2},w_{3},w_{4}\dots$ be their corresponding weights which are also +ve. 

Then, we defined their weighted AM, $A^{*}$,
$$A^{*} = \frac{ a_{1}w_{1} + a_{2}w_{2}+a_{3}w_{3} + a_{4}w_{4} + \dots }{ w_{1}+w_{2}+w_{3}+w_{4}\dots }$$
$$A^{*} = \frac{ \sum a_{1}w_{1} }{ \sum w_{1} }$$

Weighted GM, $G^{*}$,
$$G^{*} = (a_{1}^{w_{1}}.a_{2}^{w_{2}}.a_{3}^{w_{3}}\dots)^{1/w_{1}+w_{2}+w_{3}\dots}$$
$$G^{*} = \left( \sum a_{1}^{w_{1}} \right)^{\displaystyle 1/\sum w_{1}}$$


Weighted HM, $H^{*}$,
$$H^{*} = \frac{ w_{1}+w_{2}+w_{3}+\dots }{ \displaystyle \frac{ w_{1} }{ a_{1} } + \frac{ w_{2} }{ a_{2} } + \frac{ w_{3} }{ a_{3} } + \dots }$$
$$H^{*} = \frac{ \sum w_{1} }{ \sum \displaystyle  \frac{ w_{1} }{ a_{1} } }$$

And, 
$$A^{*} \geq G^{*} \geq H^{*}$$
equality holds when all numbers are equal. 

If all weights are equal, then,
$$A^{*} = A$$
$$G^{*} = G$$
$$H^{*} = H$$

If we have linear expression of +ve variables and product of their some exponents involved in the question, then we can think of weighted AM and weighted GM. The exponents of variable will act like weights. 

Example, first decide weights by looking at the powers, then find the required numbers according to the expression(s) given,
![[Pasted image 20230620075150.png]]
![[Pasted image 20230620075206.png]]

#### mth Power Inequality
Let $a_{1},a_{2},a_{3}\dots a_{n}$ are n +ve numbers and $m \in R$, then let,
$$A_{m} = \frac{ \sum a_{1}^{m} }{ n }$$
(AM of mth power of numbers) 
And,
$$A^{m} = \left( \frac{ \sum a_{1} }{ n } \right)^{m}$$
(mth power of AM of numebers)

- If m = 0 or 1 or numbers are equal, then,
  $$A_{m} = A^{m}$$

- If m is +ve fraction, i.e. $m \in (0,1)$, then
	$$A_{m} \leq A^{m}$$
	equality holds when all numbers are equal. 
	$\\$

- If $m \in (-\infty,0) \cup (1,\infty)$, then,
	$$A_{m} \geq A^{m}$$
	equality holds when all numbers are equal. 

Particularly, if $m = \frac{1}{2}$ then,
$$A_{m} \geq A^{m}$$
$$\frac{ \sum \sqrt{ a_{1} } }{ n } \leq \sqrt{ \frac{ \sum a_{1} }{ n } }$$
this is called root mean square. 
Equality holds only if all numbers are equal. 

Example,
![[Pasted image 20230620082149.png]]

### 

### Cauchy's Inequality
Let 
$$a_{1},a_{2},a_{3}\dots a_{n}$$
$$b_{1},b_{2}.b_{3} \dots b_{n}$$
are two sets of real numbers (i.e. they may be negative)
Then,

$$\left( \sum a_{1}^{2} \right)\left( \sum b_{1}^{2} \right) \geq \left( \sum a_{1}b_{1} \right)^{2}$$
Product of sum of squares of both series $\geq$ Square of sum of multiplication of both series.
(here not that dividing $a_{1}b_{1}$ by $a_{1}$ gives $b_{1}$ whose square is written in the 2nd bracket on LHS)

For equality, 
$$\frac{ a_{1} }{ b_{1} } = \frac{ a_{2} }{ b_{2} } = \frac{ a_{3} }{ b_{3} } = \dots = \frac{ a_{n} }{ b_{n} }$$

If question contains linear expression of the variables and sum of their squares, then we can think of applying Cauchy's Inequality. 

> **Proof:**
> $$
> \begin{split}
> (a_{1}x-b_{1})^{2} + (a_{2}x-b_{2}) + \dots (a_{n}x-b_{n}) &\geq 0 \\
> \left( \sum a_{1}^{2} \right)x^{2} - 2\left( \sum a_{1}b_{1} \right)x + \sum b_{1}^{2} &\geq 0 \\
> \\
> \text{Since the quadratic is always +ve,} D \leq 0, \\
> 4\left( \sum a_{1}b_{1} \right)^{2} - 4\left( \sum a_{1}^{2} \right)\left( \sum b_{1}^{2} \right) &\geq 0 \\
> \left( \sum a_{1} \right)^{2}\left( \sum b_{1}^{2} \right)^{2} &\geq \left( \sum a_{1}b_{1} \right)^{2}
> \end{split}
> $$

Example,
![[Pasted image 20230620081007.png]]
