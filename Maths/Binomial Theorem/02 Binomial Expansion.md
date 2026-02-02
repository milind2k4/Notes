Links: [[01 Binomial Coefficient]]
___
# Binomial Expansion
**Binomial Expression** is one which contains two parameters (x, y). 
Similarly, trinomial contains 3 parameters and multinomial contains many.

The rule with which we can expand some exponent of a binomial expression is called *binomial theorem.* 

For any $n \in N$,
$$(x+y)^{n} = {}^{n}C_{0}.x^{n} + {}^{n}C_{1}.x^{n-1}.y + \dots + {}^{n}C_{r}. x^{n-r}.y^{r} + \dots + {}^{n}C_{n}.y^{n}$$
In sigma notation,
$$(x+y)^{n} = \sum_{r=0}^{n} {n \choose r}. x^{n-r} . y^{r}$$

#### Points to Remember 
There will be a total of n+1 terms in the expansion. 

Coefficients which are equidistant from the edges will be equal. Because ${}^{n}C_{0} = {}^{n}C_{n}$, ${}^{n}C_{1} = {}^{n}C_{n-1}$ etc.

The sum of exponents of x and y in each terms will be n.

The general terms will be (r+1)th terms of the expansion.
$$T_{r+1} = {}^{n}C_{r} . x^{n-r}. y^{r}$$

rth term from LHS is equal to $(n+2-r)$th term from RHS.

The expansion will be symmetric about the middle term (or + sign if even no. of terms). 
![[Pasted image 20231127155052.png]]

##### Middle Term
**If n is even,** then there will be odd number of terms in the expansion. Hence, there will be one middle term which will be $(n+2)/2$ th term i.e. the (n/2 + 1)th term. 
This terms will be,
$$T_{(n/2 + 1)} = {n \choose \frac{n}{2}}. x^{n/2}. y^{n/2}$$

If n is odd, then there will be even number of terms in the expansion. Hence there will be two middle terms which will be (n+1/2)th and ((n+1/2)+1)th term. 
I.e. $T_{(n+1) /2}\ \&\ T_{(n+3) /2}$
which will be,
$$T_{(n+1) /2} = {n \choose \frac{ n-1 }{ 2 }}. x^{(n+1)/2} . y^{(n-1)/2}$$
$$T_{(n+3) /2} = {n \choose \frac{ n+1 }{ 2 }}. x^{(n-1)/2} . y^{(n+1)/2}$$

##### More Expansions
We have,
$$(x+y)^{n} = {}^{n}C_{0}.x^{n} + {}^{n}C_{1}.x^{n-1}.y + {}^{n}C_{2}.x^{n-2}.y^{2} + \dots$$

If we put $y= -y$, alternate terms will become -ve. 
$$(x-y)^{n} = {}^{n}C_{0}.x^{n} - {}^{n}C_{1}.x^{n-1}.y + {}^{n}C_{2}.x^{n-2}.y^{2} - \dots$$

Now adding them,
$$(x+y)^{n} + (x-y)^{n} = 2({}^{n}C_{0}. x^{n} + {}^{n}C_{2}. x^{n-2}.y^{2} + \dots)$$
And subtracting them,
$$(x+y)^{n} - (x-y)^{n} = 2({}^{n}C_{1}. x^{n-1}.y + {}^{n}C_{3}. x^{n-3}.y^{3} + \dots)$$

![[Pasted image 20231127164841.png]]

Putting y = 1,
$$(1+x)^{n} = {}^{n}C_{0} + {}^{n}C_{1}.x + {}^{n}C_{2}.x^{2} + {}^{n}C_{3}.x^{3} + \dots$$

$$(1+x)^{n} = {}^{n}C_{0}.x^{n} + {}^{n}C_{1}.x^{n-1} + {}^{n}C_{2}.x^{n-2} + {}^{n}C_{3}.x^{n-3} + \dots$$
In sigma notation,
$$(1+x)^{n} = \sum_{r=0}^{n} {n \choose r}. x^{r}$$

![[Pasted image 20231127170523.png]]

The sum of coefficients of alternate powers of x in the expansion of $(1+x)^{n}$ is $2^{n-1}$, and the sum of all coefficients is $2^{n}$.
![[Pasted image 20231127174057.png]]

### Greatest Binomial Coefficient 
The middle binomial coefficient is the greatest. As we separate from the middle, the coefficients start decreasing. 

Value of binomial coefficient will rise from 1 to middle and then it will fall to 1. Thus the minimum value will always be 1. 

If n is even,
$$\text{max. coef.} = {n \choose \frac{n}{2}}$$
and there will be one middle term. 

If n is odd,
$$\text{max. coef.} = {n \choose \frac{n-1}{2}} = {n \choose \frac{n+1}{2}}$$
and there will be two middle terms. 

![[Pasted image 20231128163923.png]]
![[Pasted image 20231201161155.png]]
(here ${}^{8}C_{4}$ will be ${}^{8}C_{5}$)

### Greatest Term of Expansion 
We have,
$$(1+x)^{n} = {}^{n}C_{0} + {}^{n}C_{1}. x + \dots + {}^{n}C_{r}. x^{r} + \dots + {}^{n}C_{n}. x^{n}$$

Consider,
$$
\begin{split}
|T_{r+1}| &\geq |T_{r}| \\
{}^{n}C_{r} |x^{r}| &\geq {}^{n}C_{r-1} |x^{r-1}| \\
\frac{ n! }{ r! (n-r)! } |x| &\geq \frac{ n! }{ (r-1)!(n-r+1)! } \\
(n-r+1).|x| &\geq r \\
(n+1)|x| &\geq r(1 + |x|) \\
\end{split}
$$
Thus giving,
$$r \leq \frac{ (n+1) }{ 1 + \frac{ 1 }{ |x| } } = y$$
where $x$ is anything after the 1+ with the value of $x$ put into it.

Now, if $y \in N$, then magnitude wise (aka *numerically*) greatest term will be,
$$|T_{y+1}| = |T_{y}|$$

And, if $y \notin N$, then numerically, the greatest term will be,
$$|T_{\alpha + 1}| = |T_{[y] + 1}|$$
where $\alpha = [y]$ ([.] represents GIF)

For above analysis, we should have expansion in the form of $(1+x)^{n}$ only.  

The value of terms (magnitude wise) will keep on decreasing if we move away from the greatest term on either side. 

The previous result of greatest binomial coefficient can be proved by taking x = 1. 

Explanation for why this works,
![[Pasted image 20231128195325.png]]

##### Examples 
![[Pasted image 20231128170957.png]]
![[Pasted image 20231128194323.png]]

**Range of x:**
![[Pasted image 20231201153228.png]]
![[Pasted image 20231201153726.png]]


### Binomial Expansion for -ve and fractional index
If $|x| < 1$, then,

$$(1 + x)^{n} = 1 + \frac{ n }{ 1! }x + \frac{ n(n-1) }{ 2! }x^{2} + \frac{ n(n-1)(n-2) }{ 3! }x^{3} + \dots$$
The expansion goes on till infinity as n is -ve or fraction and thus no term becomes zero. 

We can also think that here, instead of writing in terms of ${}^{n}C_{r}$, we have expanded it as we cannot write ${}^{n}C_{r}$ when n is not a natural number.

Using this, we have,
$$
\begin{split}
(1 + x)^{-1} &= 1 - x + x^{2} - x^{3} + \dots \\
\\
(1 - x)^{-1} &= 1 + x + x^{2} + x^{3} + \dots \\
\\
(1 - x)^{-2} &= 1 + 2x + 3x^{2} + 4x^{3} + \dots 
\end{split}
$$

#### Examples
![[Pasted image 20231201155141.png]]

![[Pasted image 20231201164227.png]]

![[Pasted image 20231201164550.png]]



