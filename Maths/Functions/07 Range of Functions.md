Links: [[06 Domain of Functions]]
___
# Range of Functions
Set of all values which can be taken by the expression. 

Graphically, range is portion of y-axis covered by the curve.

We have to find the min and the max value of the function. 

Ranges of combinations of functions cannot be found by intersection or union of their individual ranges. 

### Range of Some Functions

| Function                                     | Range                                |
| -------------------------------------------- | ------------------------------------ |
| $$\tan x, \cot x, \ln x, \log_{a}x$$         | $$R$$                                |
| Polynomial of Odd Degree, $\sqrt[2n+1]{ x }$ | $$R$$                                |
| $$\sin x, \cos x$$                           | $$[-1,1]$$                           |
| $$\sec x, \csc x$$                           | $$(-\infty, 0] \cup [1,\infty)$$     |
| $$\{ x \}$$                                  | $$[0,1)$$                            |
| $$[x]$$                                      | $$I$$                                |
| $$\sqrt[2n]{ x }, \|x\|$$                    | $$[0, \infty)$$                      |
| $$\frac{ 1 }{ x^{2n+1} }$$                   | $$R - \{ 0 \}$$                      |
| $$\frac{ 1 }{ x^{2n} }, a^{x}$$              | $$(0,\infty)$$                       |
| $$sgn(x)$$                                   | $$\{ -1,0,1 \}$$                     |
| $$x + \frac{ 1 }{ x }$$                      | $$(-\infty,-2] \cup[2, \infty)$$     |
| $$\frac{ax+b}{cx+d}$$                        | $$R - \left\{ \frac{a}{c} \right\}$$ |

## Methods of Finding Range
#### Using Basic Manipulations
If $A \in [a,b]$, then,

$$
\begin{split}
A + k &\in [a + k, b + k] \\
\\
k \cdot A &\in [ka, kb],\ k > 0 \\
k \cdot A &\in [kb, ka],\ k < 0\\
\\
A^{2} &\in [a^{2}, b^{2}],\ a.b > 0 \\
A^{2} &\in [0, a^{2}],\ a.b < 0,\ \&\ a^{2} > b^{2} \\
A^{2} &\in [0, b^{2}],\ a.b < 0,\ \&\ b^{2} > a^{2} \\
\\
\sqrt{ A } &\in [\sqrt{ a }, \sqrt{ b }],\ a, b > 0 \\
\sqrt{ A } &\in [0, \sqrt{ b }],\ a \leq 0 < b \\
\\
\frac{ 1 }{ A } &\in \left[ \frac{ 1 }{ b }, \frac{ 1 }{ a } \right] ,\ a.b > 0 \\
\frac{ 1 }{ A } &\in \left( -\infty, \frac{1}{a} \right] \cup \left[ \frac{ 1 }{ b }, \infty \right)  ,\ a < 0 < b \\

\end{split}
$$

 
If expression contains only one variable term, and we know its range, then this method may be used. 

![[Pasted image 20230523074304.png]]


To find range of a function which involves an expression we know the range of, we cannot directly substitute the min. and max. value of that expression. 

If function $f(x)$ has min. value $a$ and max. value $b$ then its range may or may not be $[a, b]$, as the graph might not be continuous.

If min. value of function is $a$, and max. value is $b$, and i**f the function is continuous**, then its range will be $[a,b]$

#### Range of $a\sin x + b\cos x$

$$a \sin x + b\cos x \in [-\sqrt{ a^{2}+b^{2} }, \sqrt{ a^{2} + b^{2} }]$$
this is only when x can vary in least the fundamental period. 

#### Using AM $\geq$ GM
We can get a hint for AM-GM if the variable terms' either summation or product is constant. In most cases the product is constant and the sum has variable. 


For a, b > 0,
$$\frac{ a+b }{ 2 } \geq \sqrt{ ab }$$
$$a+b \geq 2\sqrt{ ab }$$

For a, b, c > 0,
$$a+b+c = 3\sqrt[3]{ abc }$$

For n numbers,
$$a_{1} + a_{2} + a_{3} + a_{4} + \dots = n \sqrt[n]{ a_{1}a_{2}a_{3}a_{4}\dots }$$

**Note:**
- For equality, all the numbers must be equal.

- Before giving min or max value using AM-GM, check whether the numbers can be equal or not. 

- It can only be applied on +ve numbers. 

- If a variable term is added with its reciprocal type term (i.e. their product is constant) then AM-GM may be used. 


### Range of Q/Q, L/Q, Q/L
where Q stands for quadratic and L for linear.

[[11 Range]]

For,
$$\frac{ ax+b }{ cx+d },\ \frac{ a }{ b } \neq \frac{ b }{ d }$$
- Range is $R - \{ a / b \}$


## Range of Composite functions
Range in Restricted Domain

To find the range of $f(g(x))$

- Find the range of $g(x)$
- This will act as the domain of $f(x)$
- Draw the graph (if possible) limited to the domain found and thus find the range of the composite function. 
- Otherwise put the ends of the range into $f(x)$ and find the ends of the range that way, if the graph is continuous. 


To find the max value of $f + g$, we cannot add their individual max values, in general. 

$$(f+g)_{max} \neq f_{max} + g_{max}$$

But if those maximum occur at the same point,
$$(f + g)_{max} = f_{max} + g_{max}$$
only if they occur simultaneously. 

![[Pasted image 20230524085243.png]]

## Using Derivatives
If $f'(x)>0$, then $f(x)$ is increasing. 
If $f'(x)<0$, then $f(x)$ is decreasing. 

If $f'(a) = 0, \&\ f'(a^{+}) > 0,\ \&\ f'(a^{-}) < 0$, then there is a local maxima at a.
If $f'(a) = 0, \&\ f'(a^{+}) < 0,\ \&\ f'(a^{-}) > 0$, then there is a local minima at a.

Thus,
1. If $f'(x) > 0$ and $f(x)$ is continuous in the domain $[a,b]$ then it's range will be $[f(a), f(b)]$
1. If $f'(x) < 0$ and $f(x)$ is continuous in the domain $[a,b]$ then it's range will be $[f(b), f(a)]$

**In case of addition of functions,**
increasing + increasing = increasing
decreasing + decreasing = decreasing 
increasing + decreasing = can't say 

**In case of multiplication,**
increasing x increasing  = can't say

**In case of composite functions,**
increasing (increasing) = increasing 
decreasing (decreasing) = increasing 
increasing (decreasing) = decreasing 
decreasing (increasing) = decreasing 

**In case of -ve,**
-increasing = decreasing 
-decreasing = increasing 
