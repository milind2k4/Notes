Links: [[04 Monotonicity]], [[05.5 Word Problems]]
___
# Maxima and Minima

For function $f(x)$ at $x = a$ **Local Maxima** exists if there exists a +ve number $h$ such that for any $x \in (a-h,a+h)$ the value of function, $f(x) \leq f(a)$.

Similarly for **Local Minima,** $f(x) \geq f(a)$

![[Local-Maxima-and-minima-points.png]]

The function needs not to be differentiable or continuous for it to have local maxima or minima. 

![[Pasted image 20230916114245.png]]

When we refer local maxima or minima, then we give value of x, not the value of $f(x)$ which is called the local max. or min. value.

The value of  function at local maxima (minima) need not be the greatest (least) value of function in domain. 

Point of local maxima or minima are also called points of *Relative maxima or minima*. They are also called *Point of extremum/extrema.*

It is also referred to as **Turning Point.**

### Differentiable Function

For a differentiable function if it has,
1. **Local Maxima** at $x = a$ then 
   $$f'(a) = 0\ \&\ f'(a^{-}) > 0 \ \&\ f'(a^{+}) < 0$$
1. **Local Maxima** at $x = a$ then 
   $$f'(a) = 0\ \&\ f'(a^{-}) < 0 \ \&\ f'(a^{+}) > 0$$

If the derivative does not change sign around the point then local minima or maxima does not exist there. 

To find local minima or maxima,
1. Solve $f'(x) = 0$. (say solution is $x = k$)
2. Check the sign of $f'(k^{-}),\ \&\ f'(k^{+})$. 

![[Pasted image 20230916114316.png]]

The points where $f'(x) = 0$ are called *stationary points.* 
the points where $f'(x) = 0$ or $f'(x)$ is not defined are called *critical points.*

### Using Higher Derivatives
Let $f(x)$ is differentiable function and $f', f'', f'''$ exist.

Now, if $f'(a) = 0$, then to verify whether $x = a$ is local maxima, minima or none, we can find $f''(a), f'''(a), f^{(4)}(a), f^{(5)}(a)$ till first non zero value is obtained. 
Say it is obtained at rth derivative. 
That is,
$$f''(a) = f'''(a) = \dots f^{(r-1)}(a) = 0\ and\ f^{(r)} \neq 0$$

If **r is even,** then $x = a$ will be point of *local maxima or minima* according to this non zero value being *-ve or +ve respectively.* 

If **r is odd**, then $x = a$ will be *neither local maxima nor minima.* 

This is because,
![[Pasted image 20230916114419.png]]

### Global Maxima and Minima 
The point (if exists) where function takes its maximum possible value in entire domain is **Global or Absolute Maxima,** simply called Maxima. The corresponding value is called **Absolute/Global Maximum Value** or simply the greatest value.

Similarly, global minima can be defined. 

If exists, the global maxima will be *one of the local maxima.*

![[Pasted image 20230916114435.png]]

#### Finding Global Maxima Minima
1. Find the points where the function is discontinuous or non differentiable. 
1. Find value or limiting value at end points of domain and the points found in 1 and local maxima and minima. 
2. Find the greatest of these values.
3. If this value is non obtainable, then the greatest value does not exist, else if this greatest value is obtained at $x = k$, then it is the point of global maxima or minima.
4. The value at this point is the greatest value. 

Similarly, global minima can be found. 


## Examples: Maxima and Minima 
![[Pasted image 20230916114656.png]]

![[Pasted image 20230916114718.png]]

![[Pasted image 20230916114840.png]]

![[Pasted image 20230916114858.png]]

![[Pasted image 20230916114924.png]]
![[Pasted image 20230916114944.png]]

![[Pasted image 20230916115007.png]]
![[Pasted image 20230916115026.png]]

![[Pasted image 20230916115050.png]]

![[Pasted image 20230916115215.png]]

![[Pasted image 20230916115503.png]]
![[Pasted image 20230916115516.png]]

![[Pasted image 20230916115426.png]]
![[Pasted image 20230916115436.png]]

![[Pasted image 20230916115405.png]]