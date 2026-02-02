Links: [[00 Quadratic Equations and Expressions]], [[01 Roots of a Quadratic]], 
___
# Recursion Relation
#important 

> $$\begin{split}
> ax^{2} + bx + c &= 0 \to \alpha, \beta \\\\
> a \alpha ^{2} + b \alpha + c &= 0 \\
> \text{Multiplying by } \alpha ^{n-2}, \\
> a \alpha ^{n} + b \alpha ^{n-1} + c \alpha ^{n-2} &= 0 \\\\
> a \beta ^{2} + b \beta + c &= 0 \\
> \text{Multiplying by } \beta ^{n-2} ,& \\
> a \beta ^{n} + b \beta ^{n-1} + c \beta ^{n-2} &= 0 \\\\
> \text{Adding them,}& \\
> a(\alpha ^{n} + \beta ^{n}) + b(\alpha ^{n-1} + \beta ^{n-1}) &+ c(\alpha ^{n-2} + \beta ^{n-2}) = 0 \\\\
> \text{Subtracting them,}& \\
> a(\alpha ^{n} - \beta ^{n}) + b(\alpha ^{n-1} -\beta ^{n-1}) &+ c(\alpha ^{n-2} - \beta ^{n-2}) = 0 \\
> \\
> \text{Let, } S_{n} &= \alpha ^{n} + \beta ^{n} \text{ then,}\\
> aS_{n} + bS_{n-1} + cS_{n-2} &= 0 \\\\
> \text{Let,} D_{n} &= \alpha ^{n} - \beta ^{n} \text{ then,}\\
> aD_{n} + bD_{n-1} + cD_{n-2} &= 0 \\
> \\
> \text{If } c &\neq 0, \\
> S_{0} &= \alpha ^{0} + \beta ^{0} = 2 \\
> S_{1} &= \alpha + \beta = \frac{-b}{a} \\
> \\
> D_{0} &= \alpha ^{0} - \beta ^{0} = 0 \\
> D_{1} &= \alpha - \beta = \frac{\sqrt{D}}{a}
> \end{split}$$

We can use this to find sum or difference of any power of roots. 
- Find the value of $S_{2}$ by putting the values of $S_{1}$ and $S_{0}$ into the equation. 
- Find the value of $S_{3}$ by putting the value of $S_{2}$ and $S_{1}$.
- Repeat.

As,
![[Recursion Relation Example.png]]