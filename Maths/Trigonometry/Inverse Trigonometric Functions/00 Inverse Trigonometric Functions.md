Links: [[01 Graphs of Inverse-T functions]], [[03 Formulae Related to Inv-T]]
___
# Inverse Trigonometric Functions
As a whole y = sin(x) is not invertible as it is many-one. To invert it, we restricted its domain as $\displaystyle - \frac{\pi}{2}$ to $\displaystyle \frac{\pi}{2}$. 

Similarly, all other trigonometric functions' domains are restricted,
$$\sin  x \in \left[ \frac{ -\pi }{ 2 }, \frac{\pi}{2} \right]$$
$$\tan  x \in \left( \frac{ -\pi }{ 2 }, \frac{\pi}{2} \right)$$
$$\csc x \in \left[ \frac{ -\pi }{ 2 }, \frac{\pi}{2} \right] - \{ 0 \}$$

$\\$
$$\cos  x \in [ 0, \pi ]$$
$$\cot  x \in ( 0, \pi )$$
$$\sec  x \in [ 0, \pi ] - \left\{  \frac{\pi}{2}  \right\}$$

$T^{-1} (x)$ is an angle T-ratio of which is $x$ and the angle is taken in principal range.

$$T^{-1}(x)= \theta$$
$$T(\theta)=x$$


### Principal Range
$$\sin ^{-1}, \csc ^{-1}, \tan ^{-1}: \left[ \frac{\pi}{2},\frac{-\pi}{2} \right]$$

$$\cos ^{-1}, \sec ^{-1}, \cot ^{-1}: [0,\pi]$$

![[Domain of inv-trig.png]]

If x is +ve, then the value of $T^{-1}x$ will lie in 1st quadrant ($\theta$).

If x is -ve, then the value of,
- $\sin ^{-1}, \csc ^{-1}, \tan ^{-1}$ will lie in in 4th quadrant ($-\theta$).
- $\cos ^{-1}, \sec ^{-1}, \cot ^{-1}$ will lie in 2nd quadrant ($\pi-\theta$).


## Table of Domain and Range

|               | Domain         | Range                                                   | Derivative                                  |
| ------------- | -------------- | ------------------------------------------------------- | ------------------------------------------- |
| $$\sin^{-1}$$ | $$[-1,1]$$     | $$\left[ \frac{-\pi}{2},\frac{\pi}{2} \right]$$         | $$\frac{ 1 }{ \sqrt{ 1-x^{2} } }$$          |
| $$\cos^{-1}$$ | $$[-1,1]$$     | $$[0,\pi]$$                                             | $$\frac{ -1 }{ \sqrt{ 1-x^{2} } }$$         |
| $$\tan^{-1}$$ | $$R$$          | $$\left( \frac{-\pi}{2},\frac{\pi}{2} \right)$$         | $$\frac{ 1 }{ 1+x^{2} }$$                   |
| $$\cot^{-1}$$ | $$R$$          | $$(0,\pi)$$                                             | $$\frac{-1}{1+x^{2}}$$                      |
| $$\csc^{-1}$$ | $$R - (-1,1)$$ | $$\left[ \frac{-\pi}{2},\frac{\pi}{2} \right] - \{0\}$$ | $$\frac{ 1 }{ \| x \| \sqrt{ x^{2}-1 } }$$  |
| $$\sec^{-1}$$ | $$R - (-1,1)$$ | $$[0,\pi]- \left\{ \frac{\pi}{2} \right\}$$             | $$\frac{ -1 }{ \| x \| \sqrt{ x^{2}-1 } }$$ |

## Examples
![[Pasted image 20230603085945.png]]

![[Pasted image 20230603093101.png]]


![[Pasted image 20230605084816.png]]
![[Pasted image 20230605084905.png]]

![[Pasted image 20230605085306.png]]

### Series Related Questions
Difference or $V_{n}$ method.

If possible, convert it into $\tan ^{-1}$, then,
1. Write the general term, say $T_{r}$
2. Write the general term in the form of 
$$\tan ^{-1} \left( \frac{ a-b }{ 1+ab } \right)$$
then express it as $\tan ^{-1}A - \tan ^{-1}B$


Note: If the series is in $\sin ^{-1}$ or $\cos ^{-1}$ then we can try the difference method, i.e. try to write general term in the form of $\sin ^{-1}A - \sin ^{-1}B$ or $\cos ^{-1}A - \cos ^{-1}B$

We find the summation of n terms and then put n = $\infty$ in questions which have infinite sums. 

![[Pasted image 20230607074658.png]]

In some questions we might have to divide by something to make $1 + ab$ in denominator. 
![[Pasted image 20230607074713.png]]

In $\sin ^{-1}$ questions, instead of looking for $a\sqrt{ 1-b^{2} } - b\sqrt{ 1-a^{2} }$, we look for $xy - \sqrt{ 1-y^{2} }\sqrt{ 1-x^{2} }$ and then say that $x=b$ and $\sqrt{ 1-x^{2} } = b$

![[Pasted image 20230607075528.png]]

## Equation Solving
If there is only one term with variable, then take it to LHS and the rest the RHS and then simplify it using [[04 Sum or Difference of Inv T]] formula. 

If there are multiple terms with variable. then take corresponding trigonometric function both sides and finally check the solution obtained with original equation. 

![[Pasted image 20230607080855.png]]

In some cases, we have to move terms so that the question does not become complicated when we take the corresponding trigonometric function,

![[Pasted image 20230607082456.png]]


In questions where we need to express a term as another term, we say the quantity is $\theta$, then take trigonometric function, and then use the graph of [[02 Combination of T and Inv T#Graph of $T {-1}(T(x))$|combination]] to write definitions. 
![[Pasted image 20230607083653.png]]
![[Pasted image 20230607083715.png]]
![[Pasted image 20230607083803.png]]