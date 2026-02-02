Links: [[00 Quadratic Equations and Expressions]]
___
# Reduction to a Linear
If $\alpha$ is a root of a quadratic, then any polynomial in $\alpha$ can be reduced to a linear in $\alpha$ using the fact that $a \alpha^{2} + b \alpha + c = 0$.

To solve questions where $\alpha$ is the root of a quadratic, and we have to find the value of $f(\alpha)$, find $\alpha^{2}$ by putting $\alpha$ into the quadratic. Then wherever there is an $\alpha$, put that value. It will reduce the expression into a linear. 


1. Divide the given expression $p(\alpha)$ by the given quadratic $d(\alpha)$ (the one whose root is $\alpha$)

3. Then the given expression can be expressed as 
   $p(\alpha) = d(\alpha)\cdot q(\alpha) + r(\alpha)$, where $q(\alpha)$ is quotient and $r(\alpha)$ is the remainder. 

3. Now $d(\alpha)$ is zero, thus the equation reduces to
   $p(\alpha) = r(\alpha)$.

4. Now, $r(\alpha)$ will be a linear or constant as $d(x)$ is a quadratic. 
   - The degree of $r(x)$ is always 1 less than that of $d(x)$ or 0. And here $d(x)$'s degree is 2. 

6. $p(\alpha) = r(\alpha)$


- **Note:** It may be useful to put $\alpha$ and $\beta$ into the equation and keep it in storage. It can be used to simplify equations of the type 
>   $$\frac{a\ \alpha ^n+ b\ \alpha^m}{c\ \alpha^n + d\ \alpha^m} +  \frac{e\ \beta ^n+ f\beta^n}{g \beta^{m} + h\beta^m}$$
- i.e. keep in mind $a\alpha^{2} + b\alpha + c$ and $a\beta^{2} + b\beta + c$