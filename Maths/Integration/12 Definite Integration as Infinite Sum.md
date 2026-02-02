Links: [[00 Sequence and Series]], [[09 Definite Integration]] 
___
# DI as a limit of an Infinite Sum
We divide the interval $b - a$ in $\int_{a}^{b} f(x) \, dx$ into n parts of h width. I.e. $nh = b - a$

![[Pasted image 20231006075254.png]]

Area of shaded region,
$$
\begin{split}
A &= h.f(a) + h.f(a + h) + \dots h.f(a+ (n-1)h) \\
&= h \left( \sum_{r = 0}^{n-1} f(a + rh) \right)
\end{split}
$$

For finite values of n, according to given diagram, $I > A$.

If we take the 2nd height and then make rectangles, 
$$
\begin{split}
A' &= h(f(a+h) + f(a+2h) + \dots + f(a+nh)) \\
&= h \left( \sum _{r = 1}^{n} f(a+rh) \right)
\end{split}
$$
Thus the integral, $I < A'$

From this, for an **increasing function,**
$$A < I < A'$$
$$h\left( \sum _{r = 0}^{n-1} f(a+rh) \right) < I < h\left( \sum _{r = 1}^{n} f(a+rh) \right)$$

For a **decreasing function,**
$$A > I > A'$$
$$h\left( \sum _{r = 0}^{n-1} f(a+rh) \right) > I > h\left( \sum _{r = 1}^{n} f(a+rh) \right)$$

Now, as we keep increasing the value of n, the width of strips gets smaller and smaller and thus the error between the integral and the area $A$ keeps decreasing. 

As $n \to \infty$, $A \to I$ and $A' \to I$. 

Thus we can say,
$$\int_{a}^{b} f(x) \, dx = \lim_{ n \to \infty } A = \lim_{ n \to \infty } A'$$
$$\int_{a}^{b} f(a) \, dx = \lim_{ n \to \infty } h \sum _{r=0}^{n-1} f(a+rh) = \lim_{ n \to \infty } h \sum _{r=1}^{n} f(a+rh)$$
Also, as $nh = b - a$, $n \to \infty \implies h \to 0$

Finding an integral by evaluating the limit is called **1st principle or ab initio** method. 

#### Examples 
![[Pasted image 20231006082349.png]]
![[Pasted image 20231006082359.png]]



## Expressing Limit As DI
Converting an infinite sum into definite integral. #important 

1. Express the given sum in $\sum$-form. 
	$\\$
	
1. Club sum variable say $'r'$, in the form of $\displaystyle \frac{r}{n}$.
	$\\$

2. After 2, we must have one $1 /n$ outside $\sum$. Otherwise the question will not be done using DI. 
	$\\$

3. Now convert the sum into integration by replacing 
	   - $\displaystyle \frac{1}{n} \ce{ -> } dx$
	   - $\displaystyle \sum \ce{ -> } \int$
	   - $\displaystyle \frac{r}{n} \ce{ -> } x$
	   - For limits,
	     $$\text{Lower Limit of } \int = \lim_{ n \to \infty } \frac{ \text{L.L of } \sum }{ n } $$
	     $$\text{Upper Limit of } \int = \lim_{ n \to \infty } \frac{ \text{U.L of } \sum }{ n } $$

#### Some PTR
We have to take care of the limits of sum.

We should also pay attention to the terms in the answer. I.e. if there is a term of $\tan ^{-1}x$ in the answer but the sum if algebraic. We should think that the question will be done using definite integration as $\tan^{-1}x$ cannot be generated in a limit of sum. 

### Examples 
![[Pasted image 20231006083132.png]]

If there is product, then we can use $\exp(\ln(\dots))$,
![[Pasted image 20231006084752.png]]
![[Pasted image 20231006084801.png]]

![[Pasted image 20231006085436.png]]

![[Pasted image 20231006090001.png]]

![[Pasted image 20231006090421.png]]