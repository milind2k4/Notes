Links: [[01 Roots of a Quadratic]], [[05 Common Root Condition]], [[08 Location of Roots]]
___
# Range
## When $a > 0$

$$\text{Range} = \left[ \frac{-D}{4a}, \infty \right) $$


## When $a < 0$

$$\text{Range} = \left( -\infty, \frac{-D}{4a} \right] $$

## For $\displaystyle y = \frac{ax+b}{cx+d}$
$\displaystyle \frac{a}{c} \neq \frac{b}{d}$

$$\text{Domain} = R - \left\{ \frac{-d}{c} \right\} $$
$$\text{Range} = R - \left\{ \frac{a}{c} \right\} $$

## For $\displaystyle y = \frac{L}{Q}, \frac{Q}{L}, \frac{Q}{Q}$
1. If num and denom has a common factor, then remove it. It will turn as above. 
2. Otherwise assume expression = y, cross multiply and make quadratic in x. 
3. Solve $D \geq0$ for this quadratic. 
   If step 1 is the case, then D will be perfect square of linear. 
4. The solution will be the range. Verify the value of y corresponding to coefficient of $x^{2}$ in step 2 being zero specifically. 

### Case 1: One Common root
Check whether they have a common root or not. if there is one, remove it and find range as above and remove value of y corresponding to common root. 

- Split the expressions into their linear factors.
- Cancel out the factor.
- Find the value of $x$ corresponding to that factor.
- Find the value of $y$ corresponding to that $x$
- Remove this value from the range.

### Case 2: No common root


$$
\begin{split}
y &=  \frac{a_{1}x^{2} + b_{1}x + c_{1}}{a_{2}x^{2} + b_{2}x + c_{2}} \\
ya_{2} x^{2} +yb_{2}x + yc_{2} &= a_{1}x^{2} + b_{1}x + c_{1} \\
(ya_{2} -a_{1}) x^{2} + (yb_{2} - b_{1}) x + (yc_{2} - c_{1}) &= 0 \\
\end{split}
$$

Solve for  $D \geq 0$. The solution will be the range. 

If for $\displaystyle y = \frac{a_{1}}{a_{2}}$, there does not come a value of $x$, then remove $\displaystyle \frac{a_{1}}{a_{2}}$ from the range. 


![[Pasted image 20230510081657.png]]



