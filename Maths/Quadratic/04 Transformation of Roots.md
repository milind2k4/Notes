Links: [[01 Roots of a Quadratic]]
___
# Transformation of Roots
Forming a quadratic equation from a given quadratic. 

i.e. Let $ax^2+bx+c=0$ has roots, $\alpha\ \&\ \beta$, find the quadratic whose roots are some modification of $\alpha\ \&\ \beta$, like $\alpha+3\ \&\ \beta+3$.

The required equation should come in terms of $a,b,c$, the known coefficients.


1. Let $\gamma = p(\alpha)$ and $\delta = q(\beta)$ where $p(\alpha)\ \&\ q(\beta)$ are the expressions of $\alpha\ \&\ \beta$

2. Find $\gamma + \delta$ & $\gamma \cdot \delta$ in terms of $\alpha \beta$ & $\alpha + \beta$

3. Put the values of $\alpha \beta$ & $\alpha + \beta$, i.e. $\displaystyle \frac{-b}{a}$ and $\displaystyle \frac{c}{a}$ respectively in the obtained equation. 

4. Finally write the required equation as $\lambda[x^{2} - (\gamma + \delta)x + \gamma \delta] = 0$.

## Some Special Cases
When the expressions of $\alpha\ \&\ \beta$ are of the type:
> $$\frac{a\ \alpha + b}{c\ \alpha + d}\ \&\ \frac{a\ \beta + b}{c\ \beta + d}$$

### Steps
1. Assume,
>    $$y = \frac{a\ x + b}{c\ x + d}$$ 

2. Find expression of $x$ in terms of $y$. 
   i.e. find $p(y)$ in 
>    $$ x = p(y)$$

3. Substitute this $x$, i.e. $p(y)$, into the original equation. 

4. The expression obtained will be the required expression in terms of $y$. (we can just put $x$ in place of $y$)
   $\\$

- **The Limitations of this method:** 
	1. The expressions for $\alpha$ should contain only $\alpha$ and the expression for $\beta$ should contain only $\beta$.
	1. Both the expressions for $\alpha\ \&\ \beta$ should be symmetric.
	1. Both the expressions for $\alpha\ \&\ \beta$ should be of the form $\displaystyle \frac{\text{Linear}}{\text{Linear}}$.


#### Why it works?
> - (Let $p(\alpha)=\gamma\ \&\ q(\beta)=\delta$)
> 
> - We have $\alpha$ as the root of $ax^2+bx+c=0$
>   $\implies$ $\alpha$ satisfies the equation. 
> 
> - Now, putting $x = \alpha$ in 
> >  $$y = \frac{a\ x + b}{c\ x + d}$$ 
> 
>   gives, 
> >   $$y = \gamma \text{ [as } p(\alpha) = \gamma]$$
> 
>   $\implies$ putting $y = \gamma$ gives $x = \alpha$. 
>   
> - Now, putting $y=\gamma$ in 
>  > $$ay^2+by+c=0$$ 
>  
>   will give, 
>   > $$a \alpha^{2} + b \alpha + c = 0$$
>  
>  Thus, $\gamma\ i.e.\ p(\alpha)$ is a root of $ay^2+by+c=0$.
>  
>  - That is $\gamma$ is a root of $a \cdot p(y)^2+b\cdot p(y)+c=0$ where $x = p(y)$ gotten in step 2 in the [[04 Transformation of Roots#Steps|steps above.]]

### Simple Changes
If roots of $ax^{2}+bx+c = 0$ are $\alpha, \beta$
then the roots of,

1. $ax^{2}-bx+c=0$ are $-\alpha,-\beta$

2. $aq^{2}x^{2} + bqx + c = 0$ are $\displaystyle \frac{ \alpha  }{ q }, \frac{ \beta  }{ q }$ 

3. $ax^{2} + qbx + q^{2}c = 0$ are $q\alpha, q\beta$ 

4. $a(x+q)^{2} + b(x+q) + c = 0$ are $\alpha-q, \beta-q$

5. $cx^{2} + bx + a = 0$ are $\displaystyle \frac{1}{\alpha }, \frac{1}{\beta }$

5. $cx^{2} - bx + a = 0$ are $\displaystyle -\frac{1}{\alpha }, -\frac{1}{\beta }$

5. $cq^{2}x^{2} - bqx + a = 0$ are $\displaystyle \frac{1}{q\alpha }, \frac{1}{q\beta }$


### When one Root is the Square of another
![[Pasted image 20230507081003.png|400]]












