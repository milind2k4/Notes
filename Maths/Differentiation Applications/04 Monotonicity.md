Links: [[05 Maxima and Minima]]
___
# Monotonicity
(Increasing and decreasing function)

A function $f(x)$ is called an **increasing function** in an interval $(a,b)$ if for any $x_{1},x_{2} \in (a,b)$ **if $x_{1} > x_{2}$ then $f(x_{1}) \geq f(x_{2})$.** 

**Increasing** means $f(x_{1}) \geq f(x_{2})$ i.e. *does not decrease. *
**Strictly increasing** means $f(x_{1}) > f(x_{2})$ i.e. *does not decrease or stagnate.* All strictly increasing are increasing function. 

Similarly $f(x)$ is decreasing in $(a,b)$ if $x_{1} > x_{2} \implies f(x_{1}) \leq f(x_{2})$.

Constant function are simultaneously *both increasing and decreasing* function, but not strictly either. 

A function $f(x)$ is said to be increasing/strictly increasing/decreasing/strictly decreasing at $x = a$ if there exists a small +ve number $h$ such that $f(x)$ is increasing/strictly increasing/decreasing/strictly decreasing in the interval $(a-h,a+h)$ respectively. 

I.e. *check monotonicity around that point in a small interval around the point.* The length of the interval is immaterial. 

Any point where the function "turns", the function cannot be said to be any of increasing/strictly increasing/decreasing/strictly decreasing

![[Pasted image 20230916112835.png]]

**Monotonic** function means that it is *entirely increasing or entirely decreasing.*
**Non monotonic** function means it will *increase as well as decrease.* 

To check monotonicity, we are supposed to **analyse sign of $f'(x)$.** We are not supposed to check sign of $f(x)$ or monotonicity of $f'(x)$. 

#### Inequality
If function $f(x)$ is strictly increasing, then, (direction of inequality does not change)
$$x_{1} > x_{2} \iff f(x_{1}) > f(x_{2})$$
If function $f(x)$ is strictly decreasing, then, (direction of inequality changes)
$$x_{1} > x_{2} \iff f(x_{1}) < f(x_{2})$$

### Interval of Increase and Decrease 
The interval in which the function increasing is called interval of increase. Similarly for others.  

While giving interval we should not use union between two intervals. We write them using "and".

This is because the definition may not fit if we use union. 

Here we can see that $f(x_{2}) > f(x_{1})$ while $x_{2} < x_{1}$.
![[Pasted image 20230916112917.png]]

Differentiability does not matter.
![[Pasted image 20230916112957.png]]

If $f(x)$ increases in two non overlapping intervals (say $k_{1},k_{2}$), then we cannot relate value of function at two arguments one from each of the intervals. #important 

I.e. if $x_{1} \in k_{1}$ and $x_{2} \in k_{2}$ and $x_{1} > x_{2}$, then we cannot say $f(x_{1}) > f(x_{2})$. 

![[Pasted image 20230916113031.png]]

For an strictly increasing function $f(x)$, $a > b \iff f(a) > f(b)$ only if $f(x)$ increasing in entire $(a,b)$. I.e. there should be no point in between where the function is undefined or is not increasing.


#### Differentiable function
A differentiable function, in an interval $(a,b)$ is,
1. Increasing if $f'(x) \geq 0,\forall\ x \in (a,b)$
1. S. Increasing if $f'(x) \geq 0,\forall\ x \in (a,b)$ and $f(x)$ should not be constant in any interval.  (i.e. $f'(x)$ is zero at discrete points)
1. Decreasing if $f'(x) \leq 0,\forall\ x \in (a,b)$
1. S. Decreasing if $f'(x) \leq 0,\forall\ x \in (a,b)$ and $f(x)$ should not be constant in any interval.  (i.e. $f'(x)$ is zero at discrete points)

![[Pasted image 20230916113129.png]]

To find interval in which function 
1. Decreases solve $f'(x) \leq 0$
2. S. Decreases solve $f'(x) \leq 0$ and leave the interval in which function is constant (if any). 
1. Increases solve $f'(x) \geq 0$
2. S. Increases solve $f'(x) \geq 0$ and leave the interval in which function is constant (if any). 

## Examples: Monotonicity 
![[Pasted image 20230916113320.png]]

![[Pasted image 20230916113304.png]]

![[Pasted image 20230916113155.png]]

![[Pasted image 20230916113413.png]]

![[Pasted image 20230916113525.png]]

![[Pasted image 20230916113542.png]]

![[Pasted image 20230916113720.png]]
![[Pasted image 20230916113730.png]]

![[Pasted image 20230916113741.png]]

![[Pasted image 20230916113819.png]]

![[Pasted image 20230916113838.png]]

![[Pasted image 20230916113854.png]]
![[Pasted image 20230916113908.png]]

![[Pasted image 20230916113928.png]]

![[Pasted image 20230916113953.png]]

![[Pasted image 20230916114033.png]]

![[Pasted image 20230916114053.png]]
![[Pasted image 20230916114103.png]]
