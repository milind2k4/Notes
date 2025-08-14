Links: [[04 Graphs of Trigonometric Functions]]
___
# Trigonometric Equations
If the value of $T(\alpha)$ is +ve, then we use the angle from 1st quadrant, if it is -ve, then for $\sin, \tan$ we use angle from 4th quadrant, i.e. $-\alpha$, and for $\cos$ we use angle from 2nd quadrant i.e. $\pi - \alpha$

If angle corresponding to the value is not know, then use inverse. 

Answer to a question will be unique but, in some cases, it may be expressed in different forms.

If we use manipulation or squaring or express a term in different form then, sometimes, its domain may change. The final solution must satisfy the original equation. We have to check the solution with the original if tan, cot, sec, csc, squaring, are involved or if we cross multiply with denominator. 

We should also not cancel factors from both sides willy-nilly as it might remove a root. But we can cancel from the denominator. 

For example,
![[Pasted image 20230503082144.png]]

For example, when multiplying with denominator,
![[Pasted image 20230503082755.png]]

Avoid the angles in AP formula as it may introduce some extra roots. 

In questions which ask for number of solutions, we have to check for repeated solutions. We use dual inequalities to count. 

For example,
![[Pasted image 20230503090456.png]]

To remove the extra solutions and write final answer, we can write,
$$x = (\text{solution})\ \&\ (x \neq \text{extra solution})$$
Check solution in $[0,\pi]$ and then generalize it by adding the fundamental period of the trig function.  

If there are sum and product of 3 tans in the question, we can use [[03 T ratio of Sum and Difference of 2 Angles#Tangent of sum of many angles|tan for 3 angles.]]

Equations or inequalities which have 2 variables but one equation or inequality are generally solved on the boundary of the range of trig functions. 

## General solutions

1. $$\sin x = \sin \alpha \implies x = n\pi + (-1)^{n}\alpha$$
	where $\alpha \in \displaystyle \left[ \frac{-\pi}{2}, \frac{\pi}{2} \right]$, and $n\in I$
   

1. $$\cos x = \cos \alpha \implies x = 2n\pi \pm \alpha$$
	where $\alpha \in \displaystyle [0, \pi]$, and $n\in I$


1. $$\tan x = \tan \alpha \implies x = n\pi + \alpha$$
	where $\alpha \in \displaystyle \left( \frac{-\pi}{2}, \frac{\pi}{2} \right)$, and $n\in I$


2. $$T^{2}(x) = T^{2}(\alpha) \implies x = n\pi \pm \alpha$$
	where $n \in I$


## Some special cases

1. $$\begin{split}
\sin x &= 0 \implies x = n\pi \\
\sin x &= 1 \implies x = (4n+1)\frac{\pi}{2} \\
\sin x &= -1 \implies x = (4n+3)\frac{\pi}{2} \\
\end{split}$$

1. $$\begin{split}
\cos x &= 0 \implies x = (2n+1) \frac{\pi}{2} \\
\cos x &= 1 \implies x = 2n\pi \\
\cos x &= -1 \implies x = (2n+1)\pi
\end{split}$$

1. $$\begin{split}
\tan x &= 0 \implies x = n\pi \\
\tan x &= 1 \implies x = 2n\pi \\
\tan x &= -1 \implies x = (2n+1)\pi \\
\end{split}$$

## Question Types 

### Which can be factorised

Factorise the equation and equate each term to zero.

### Which can be reduced into a quadratic

Convert all the T ratios into one and form a quadratic. Solve the quadratic and then the trigonometric equation formed of the solutions of the quadratic. 

### Which can be solved by transforming a sum or difference of T ratios into their product and vice versa

Use the formulas from [[05 Sum and Difference of T ratios]].

### Of the form $a \sin x + b \cos x = c$

Divide the whole equation by $\sqrt{a^{2} + b^2}$, then try to convert it into a formula from [[03 T ratio of Sum and Difference of 2 Angles]]


### Which have $(\sin x \pm \cos x)$ and $(\sin x \cos x)$ terms

Let $\sin x \pm \cos x = t$
then squaring both sides,  find the value of $\sin x \cos x$

$$\begin{split}
\sin ^{2}x + \cos ^{2}x \pm 2\sin x \cos x &= t^{2} \\
\sin x \cos x &= \frac{t^{2} \mp 1}{2}x 
\end{split}$$

Put this back into the expression, solve for $t$.

This will convert it into the form of $a \sin x + b \cos x = c$ . Solve using above method for final answer. 













