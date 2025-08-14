Links: [[01 Roots of a Quadratic]]
___
# Common Root Condition
#important
Given two equations,
$$a_{1}x^{2} + b_{1}x + c_{1} = 0$$
$$a_{2}x^{2} + b_{2}x + c_{2} = 0$$

## Cases

- Both Roots are common if the ratio of the coefficients is the same.
  i.e.
>   $$\frac{a_{1}}{a_{2}} = \frac{b_{1}}{b_{2}} = \frac{c_{1}}{c_{2}}$$

- One Root is common (say $\alpha$), then,
> $$a_{1}\alpha^{2} + b_{1}\alpha + c_{1} = 0$$
>  $$a_{2}\alpha^{2} + b_{2}\alpha + c_{2} = 0$$
> 
> Using Cross Multiplication: 
> $$\frac{\alpha^{2}}{b_{1}c_{2} - b_{2}c_{1}} = \frac{-\alpha}{a_{1}c_{2} - a_{2}c_{1}} = \frac{1}{a_{1}b_{2} - a_{2}b_{1}}$$
> 
> Now,
> $$ \alpha = \frac{c_{1}a_{2} - c_{2}a_{1}}{a_{1}b_{2} - a_{2}b_{1}} $$
> $$ \alpha = \frac{b_{1}c_{2} - b_{2}1_{1}}{c_{1}a_{2} - c_{2}a_{1}} $$
> 
> Therefore,
> $$\frac{c_{1}a_{2} - c_{2}a_{1}}{a_{1}b_{2} - a_{2}b_{1}} = \frac{b_{1}c_{2} - b_{2}1_{1}}{c_{1}a_{2} - c_{2}a_{1}} $$
> $$\implies (c_{1}a_{2} - c_{2}a_{1})^{2} = (a_{1}b_{2} - a_{2}b_{1}) (b_{1}c_{2} - b_{2}c_{1}) $$
> > This condition is called Common Root Condition. 
> > It is true even if both the roots are common.
> 
> Remember this: $not(b)^{2} = not(c) \cdot not(a)$
> (same order as $b^{2}-4ac$)

To remember, the first terms are (ab)(bc) = (ca),
![[Pasted image 20230507083624.png]]

Or, use matrix,
$$\begin{matrix}
a_{1} & b_{1} & c_{1} & a_{1} \\
a_{2} & b_{2} & c_{2} & a_{2}
\end{matrix}$$

![[Pasted image 20230507083610.png]]

**Note:** If the question has not said "exactly" one root in common, we have to check both the conditions. i.e. when both roots are in common, and when only one root is in common. 

Check discriminant, if it is negative and the coefficients are real, then both the roots will be common.
![[Pasted image 20230507085140.png]]

## Common Root Condition Alternate
Consider,
> $$a_{1}x^{2} + b_{1}x + c_{1} = 0,\ \text{roots are }\ \alpha, \beta$$
> $$a_{2}x^{2} + b_{2}x + c_{2} = 0,\ \text{roots are }\ \alpha, \gamma$$

Now, eliminating $x^{2}$,  by $a_{2}(1) - a_{2}(2)$,
> $$(b_{1}a_{2} - b_{2}a_{1})x + c_{1}a_{2} - c_{2}a_{1} = 0$$

Now as this equation is a combination of the first 2, this should have the common root of the first 2 equations as it's only root (this is a linear, thus it has only one root, it being $\alpha$ in this case).

Thus, 
> $$x = \frac{a_{1}c_{2} - a_{2}c_{1}}{a_{2}b_{1} - a_{1}b_{2}} $$

And Hence, 
> $$\alpha = \frac{a_{1}c_{2} - a_{2}c_{1}}{a_{2}b_{1} - a_{1}b_{2}} $$

To find  the reverse, i.e. check if they have a common root or not, we can find this $\alpha$ and  then if it satisfies any of the two equations, then that root, i.e. $\alpha$ is a common root.




 