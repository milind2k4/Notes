Links: [[10 Properties of Definite Integration]]
___
# Definite Integration

If $\int f(x) \, dx = g(x) + c$, then,
$$\int_{a}^{b} f(x) \, dx = g(x)]_{a}^{b} = g(b) - g(a)$$

#### Some points to Remember
1. Limits are the value of integrating variable if not stated otherwise.
	e.g. here -1 and 2 are the values of $\ln x$
	$$\int_{-1}^{2} x^{2} \, d(\ln x)$$
	Here we can write,
	$$\int_{\ln x = -1}^{2} x dx = \int_{-e}^{e^{2}} x \, dx$$

2. If integral has limits a and b then we only need to focus on this interval only i.e. $(a,b)\ or\ (b,a)$. We need not be concerned with anything that happens outside it. 
   $\\$

3. In by parts, integration of 2nd function will be **indefinite only.** We apply limits on the final answer. #important 
   $\\$

4. In substitution limits can be changed accordingly.
   
   ![[Pasted image 20231001181624.png]]
   $\\$

5. In substitution there should be one one relation between new variable and old variable. If there is many one relation, then we break the integral at the point of turning and then integrate. This however, is not generally required in integration. 
   
   ![[Pasted image 20231001182059.png]]

#### Improper Integral 
If $f$ is discontinuous or undefined at $x = a\ or\ b$, both or at some point in the middle of them, then find limiting value of $\int f \, dx$ at that point from appropriate side. #important 

![[Pasted image 20231001180408.png]]

![[Pasted image 20231001180554.png]]

![[Pasted image 20231001183553.png]]


### Geometric Interpretation 
Definite integration $\displaystyle \int_{a}^{b} f(x) \, dx$ (if it exists) gives algebraic area bounded between y = f(x) and x axis.

It will be +ve if $y = f(x)$ lies above x axis and integration is towards right i.e. $b > a$.

![[Pasted image 20231001183030.png]]

### Some Theorems
If $f(a)$ is defined, then 
$$\int_{a}^{a} f(x) \, dx = 0$$

If $f(x) > g(x)$ then,
$$\int_{a}^{b} f(x) \, dx > \int_{a}^{b} g(x) \, dx$$
(i.e. the one whose graph is above will have more algebraic area)
Here we have to take care that we move towards right on x axis i.e. b > a.

If $f(x)$ is continuous in $(a,b)$ and if $\int_{a}^{b} f(x) \, dx = 0$ then $f(x) = 0$ will have at least one root in $(a,b)$

If $f(x)$ is non negative continuous function in $(a,b)$ and if $\int_{a}^{b} f(x) \, dx = 0$ then $f(x) = 0,\forall\ x \in (a,b)$


## Some Definite Integrals
$$\int_{0}^{n} \{ x \} \, dx = \frac{n}{2}$$
$$\int_{0}^{n} [x] \, dx = \frac{ n(n-1) }{ 2 }$$

$$\int_{0}^{\pi/2} \ln(\sin x) \, dx = \int_{0}^{\pi/2} \ln(\cos x) \, dx = -\frac{\pi}{2}\ln 2$$
This can be found using P-5 from [[10 Properties of Definite Integration]].

![[Pasted image 20231002093551.png]]

### Misc. Examples 
![[Pasted image 20231007102147.png]]
![[Pasted image 20231007102158.png]]

![[Pasted image 20231007103220.png]]
![[Pasted image 20231007103235.png]]

![[Pasted image 20231007103729.png]]


## Differentiation of Integrals

$$I(x) = \int_{f(x)}^{g(x)} h(t) \, dt$$

$$I'(x) = g'.h(g) - f'.h(f)$$
Given $h(t)$ does not contain external variable $x$.  

![[Pasted image 20231005082259.png]]

If there is $x$ inside the expression as well,

$$I(x) = \int_{f(x)}^{g(x)} h(x,t) \, dt$$

$$I'(x) = g'. h(x,g) - f'. h(x,f) + \int_{f(x)}^{g(x)} \left( \frac{ \partial h(x,t) }{ \partial x }  \right) \, dt$$
In partial differentiation treat t as constant. 

![[Pasted image 20231005083510.png]]

### Examples
![[Pasted image 20231005084306.png]]

![[Pasted image 20231005084839.png]]


## Reduction Formula
[[00 Indefinite Integration#Reduction Formula]]

$$I_{n} = \int_{0}^{\pi/2} \sin ^{n}x \, dx = \int_{0}^{\pi/2} \cos ^{n}x \, dx,\ n \in N$$

The limits must be $0 \to \pi /2$. 

Then,
$$I_{n} = \left( \frac{ n-1 }{ n } \right)I_{n-2}$$
To remember: $n \to n \to n-1 \to n-2$


Thus,
$$I_{0}=\frac{\pi}{2}\ \&\ I_{1} = 1$$

### Walli's Theorem
$$I_{m,n} = \int_{0}^{\pi/2} \sin ^{m}x \cos ^{n}x \, dx = \int_{0}^{\pi/2} \sin ^{n}x \cos ^{m}x \, dx ,\ m,n \in N$$

Then, 
$$I_{n} = \left( \frac{ [(m-1)(m-3)(m-5)\dots 2\ or\ 1][(n-1)(n-3)(n-5)\dots 2\ or\ 1] }{ (m+n)(m+n-2)(m+n-4)\dots 2\ or\ 1 } \right). \lambda$$

Where,
$$
\begin{split}
\lambda &= 1,\ \text{if at least one of m or n is odd} \\
&= \frac{\pi}{2},\ \text{if both m and n are even}
\end{split}
$$

![[Pasted image 20231005095538.png]]

### Examples 
![[Pasted image 20231005100234.png]]

![[Pasted image 20231005100742.png]]

![[Pasted image 20231005101432.png]]
![[Pasted image 20231005101444.png]]

![[Pasted image 20231005102437.png]]
![[Pasted image 20231005102452.png]]

![[Pasted image 20231005102754.png]]

## Inequalities

If $f(x) > g(x)$ in $(a,b)$ then,
$$\int_{a}^{b} f(x) \, dx > \int_{a}^{b} g(x) \, dx$$
Irrespective of positioning of graphs of y = f(x) and y = g(x) wrt x axis. 

#### Bound between min. and max.
Let min and max values of $y = f(x)$ in the interval $[a,b]$ is $m$ and $M$ respectively. 
Then, 
$$m(b-a) \leq \int_{a}^{b} f(x) \, dx \leq M(b-a)$$

![[Pasted image 20231007092704.png]]

#### Absolute Value 

$$\int_{a}^{b} f(x) \, dx = A_{1} - A_{2} + A_{3}$$

![[Pasted image 20231007093814.png]]

$$\int_{a}^{b} |f(x)| \, dx = A_{1} + A_{2} + A_{3}$$

![[Pasted image 20231007093828.png]]

Thus if $b > a$, 
$$\left|   \int_{a}^{b} f(x) \, dx  \right| \leq \int_{a}^{b} |f(x)| \, dx$$
For equality, the sign of $f(x)$ should not change. 

We have to take care to see which one of the limits is bigger (i.e. the direction of integration)
![[Pasted image 20231007094131.png]]
![[Pasted image 20231007094351.png]]

### Examples 
![[Pasted image 20231007094716.png]]

![[Pasted image 20231007095504.png]]
![[Pasted image 20231007095512.png]]

![[Pasted image 20231007095840.png]]
![[Pasted image 20231007100448.png]]

![[Pasted image 20231007101313.png]]
![[Pasted image 20231007101325.png]]


