Links: [[00 Limits]], [[08 Continuity]]
___
# Differentiability
Function $f(x)$ is said to be differentiable at x = a if the limit,
$$\lim_{ x \to a } \frac{ f(x) - f(a) }{ x - a }$$
exists. 
And if exist, it is denoted by $f'(a)$. I.e.
$$f'(a) = \lim_{ x \to a } \frac{ f(x) - f(a) }{ x - a }$$
The LHL of this limit is called Left Hand Derivative (LHD).
$$LHD = \lim_{ x \to a^{-} } \frac{ f(x) - f(a) }{ x - a }$$
Now, substituting $x= h + a \implies h = x - a$,
$$LHD = \lim_{ h \to 0^{-} } \frac{ f(a + h) - f(a) }{ h }$$
This will be denoted by $f'(a^{-})$

The RHL of this limit is called Right Hand Derivative (RHD).
$$RHD = \lim_{ x \to a^{+} } \frac{ f(x) - f(a) }{ x - a }$$
$$RHD = \lim_{ h \to 0^{+} } \frac{ f(a + h) - f(a) }{ h }$$
This will be denoted by $f'(a^{+})$

For function to be differentiable at x = a we must have,
$$LHD_{x = a} = RHD_{x =a}$$
And if this equal value is a finite number $l$ then,
$$f'(a) = l$$

We will evaluate this limit and it will be broken into LHD and RHD only when required. 

If a is the right most point of domain, then for function to be differentiable at x = a only LHD must exist. 

### Geometrical Explanation 
The derivative of a function is its slope which is the instantaneous rate of change of value of function wrt x at x = a.
$$\frac{ f(x) - f(a) }{ x - a } = \tan \theta$$
![[Pasted image 20230811132432.png]]


As we move towards a, the slopes get more and more accurate at a. 
![[Pasted image 20230811132449.png]]

Here we can see that, $\theta \to \alpha \implies \tan \theta \to \tan \alpha$.
$$\lim_{ x \to a^{+} } \frac{ f(x) - f(a) }{ x -a } = \lim_{ x \to a^{+} } \tan \theta = \tan \alpha$$

The limiting value of slope of chord, one end of which is fixed at x = a, P and other end Q is taken towards P from RHS will be RHD.

Similarly we can defined LHD.

![[Pasted image 20230811133305.png]]

If $PT_{1}$ and $PT_{2}$ are same lines, then $T_{1}T_{2}$ is called tangent to the curve at x = a and its slope will be $f'(a)$.

If a function is differentiable at any point then it has a unique slope at that point. If it is not differentiable then the slope on coming from right will be different from that on coming from left. 

$\displaystyle \lim_{ x \to a } f'(x)$ means that we are moving the point of tangency towards a. 
LHD or RHD means that we are moving the movable point of chord towards the fixed point.

In most cases they are same, but they can be different,
![[Pasted image 20230811134208.png]]
![[Pasted image 20230811134151.png]]

A function is also non-differentiable if the slope of tangent is not defined (i.e. vertical tangent).

Any function is not differentiable at a corner point. 

### Continuity and Differentiability 

If a function is continuous then it may or may not be differentiable. 
If a function is discontinuous, then it will be non-differentiable.
If a function is differentiable then it will be continuous.
If function is non-differentiable then it may or may not be continuous.

C is Continuity, D is differentiability, DC is Discontinuity and ND is Non-Differentiability.  
$$C \centernot\implies D$$
$$D \implies C$$
$$DC \centernot\implies ND$$
$$ND \centernot\implies DC$$

![[Pasted image 20230811134840.png]]

If LHD exists, then LHL of function at x = a will be equal to $f(a)$.
![[Pasted image 20230811135925.png]]

Similarly, if RHD exists, then RHL of function at x = a will be equal to $f(a)$.

If LHD and RHD both exist, then 
$$\lim_{ x \to a^{-} } f(x)= f(a) = \lim_{ x \to a^{+} } f(x)$$
Thus the function will be continuous. 

Now if LHD and RHD both exist but are unequal, then function is continuous but non-differentiable.

Now if LHD and RHD both exist and are equal, then function is continuous and differentiable.

![[Pasted image 20230811140438.png]]

### Differentiability in an Interval
A function $f(x)$ is said to be differentiable in interval $[a,b]$ if it is differentiable at each point of the interval. 

i.e. $f'(a^{+})$, $f'(b^{-})$ and $f'(c^{-}) = f'(c^{+})$ for any point $c \in (a,b)$ must exist. 

#### Points to Check Differentiability 
- Wherever function changes its definition. 
- Wherever one of the involved expression is discontinuous or non differentiable or undefined. 

i.e. 
1. All points where continuity has to be checked
2. At critical points of modulus 


$e^{ x }, a^{x},$ any polynomial function, $\sin x, \cos x, \tan ^{-1}x, \cot ^{-1}x$ are differentiable in R.
$\log_{a} x, \ln x$ are differentiable in $R^{+}$. 
$\tan x, \cot x, \sec x, \csc x, 1 /x^{n}$ are differentiable in their domains. 
$|x|$ is non differentiable at x = 0. 

| Function                                            | Point of Non-Differentiability |
| --------------------------------------------------- | ------------------------------ |
| $abs(x)$                                            | $x = 0$                        |
| $\sin ^{-1}x, \cos ^{-1}x, \sec ^{-1}x,\csc ^{-1}x$ | $x = \pm 1$                    |
| $[x], \{ x \}$                                      | $x = I$                        |
| $sgn(x)$                                            | $x =0$                         |

### [[09.5 Theorems of Differentiability]]

## Examples
We can check differentiability using both first principle and differentiation in the same question. But we will have to check continuity.

Here, we used differentiation for LHD and first principle for RHD. 
![[Pasted image 20230812114130.png]]

![[Pasted image 20230812114605.png]]

![[Pasted image 20230812124413.png]]

![[Pasted image 20230812124638.png]]

![[Pasted image 20230812125132.png]]