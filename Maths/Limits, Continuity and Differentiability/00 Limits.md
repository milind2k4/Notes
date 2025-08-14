Links: //
___
# Limits
Limit of a function at $x = a$ is denoted as 
$$\lim_{ x \to a }f(x)$$
and is the finite value (if exists) towards which the function approaches or takes as $x$ is taken towards $a$.

- **Left Hand Limit at $x = a$:** The value towards which the function approaches as $x$ is taken towards $a$ from the left side. In short we will write $f(a^{-})$ for RHL.
  
	$$\lim_{x \to a^{-}} f(x) = l$$
	$$\lim_{h \to 0^{-}} f(a+h) = l$$
	$$\lim_{h \to 0^{+}} f(a-h) = l$$


- **Right Hand Limit at $x = a$:** The value towards which the function approaches as $x$ is taken towards $a$ from the right side. In short we will write $f(a^{+})$ for RHL.

	$$\lim_{x \to a^{+}} f(x) = l$$
	$$\lim_{h \to 0^{-}} f(a-h) = l$$
	$$\lim_{h \to 0^{+}} f(a+h) = l$$


Limit of a function exists if LHL$|_{(x=a)}$ = RHL$|_{(x=a)} =l$ (say)
In any other case, the limit does not exist. 

$$\lim_{x \to a} f(x) = l$$
$$\lim_{h \to 0} f(a+h) = l$$

$l$ is called the value of limit or limiting value and is a finite, exact number.

### Points to Remember
1. $x \to a \centernot \implies x=a.$
2. Limit may or may not exist irrespective of the function being defined at that point.
3. We cannot think about limits at the edges of domain. 
   eg. $\sin^{-1}x$ RHL at $x\to1$ is not defined.
   But to give limit at the end point of domain we give either the LHL or RHL if either exists.
   
4. If the number of terms is variable due to the limiting variable, we cannot expand sum over division. 
   eg.
   $$\lim_{n \to \infty } \frac{1+2+3+...n}{n^{2}} \neq \lim_{n \to \infty} \frac{1}{n^{2}} + \lim_{n \to \infty} \frac{2}{n^{2}} +... \lim_{n \to \infty} \frac{1}{n}$$

1. Sum of infinite *approaching zero*s is not zero. This ties back into the previous note. It becomes the indeterminant form $0 \times \infty$.
2. Do not break a limit into LHL and RHL unless required. 
3. Do not use approximation in argument of function. 
   $$\lim_{ n \to \infty } (7^{n+1} - 7^{n}) \neq \lim_{ n \to \infty } (7^{n} - 7^{n})$$

6. If $x \to \infty$ then,
   $$3^{x}\gg e^{ x } \gg 2^{x} \gg x^{n} \gg \ln x$$
   Due to this,
   $$\lim_{ x \to \infty } \frac{ x^{n} }{ e^{ x } } = 0$$
   $$\lim_{ x \to \infty } \frac{ (\ln x)^{n} }{ x } = 0$$
   $$\lim_{ x \to \infty } x^{m} . |\ln x|^{n} = 0,\ n \in R,\ m \in R^{+}$$

### Reasons of Non-Existence of Limits
1. If RHL or LHL or both do not exist.
1. If RHL & LHL both exist bur are not equal
2. If the value of the function fluctuates. 
   $$\lim_{ x \to 0 } \sin \left( \frac{1}{x^{2}} \right) = DNE$$
   $$\lim_{ x \to 3 } \sin \left( \frac{ 1 }{ x-3 } \right) = DNE$$

### Graphical Representation
If we want to find limit at x = a, then we draw a vertical straight line x = a on the graph. 

Move towards this line over the graph from RHS. If we are approaching a finite point, then the y coordinate of that point will be the limiting value. And as we are moving from RHS, this limiting value will be RHL. 

Similarly LHL can be found.

![[Pasted image 20230731092445.png]]

Collectively,
![[Pasted image 20230731092429.png]]

The point being on the graph has no effect on the limit. (i.e. open circle does not matter)

If we reach different points from RHS and LHS, then the limit does not exist. 

![[Pasted image 20230731092703.png]]

### Some Special Questions/Theories
##### [[00 Trigonometry#Some Misc. Results]]
Using these results, we can do questions involving GIF and FPF,
![[Pasted image 20230809094610.png]]

#### Exponent to $\infty$
If $n \to \infty$ then to analyse $(f(x))^{n}$, solve $f(x) = 1$.

![[Pasted image 20230809100337.png]]
![[Pasted image 20230809100347.png]]


## Examples
In questions, we do not multiply fully, only till the non cancelled term or the dominating term. And we take care to notice $-\infty$ in the question,
![[Pasted image 20230805082827.png]]

Fluctuating value multiplied by $0 \uparrow$ will be zero.
![[Pasted image 20230805083224.png]]

If any one term is $0 \uparrow$, then the only way for it to become indeterminant is if $\pm \infty \uparrow$ is multiplied with it. 
![[Pasted image 20230805084146.png]]
![[Pasted image 20230805084233.png]]

We have to take care when manipulating $\sqrt{ x^{2} }$ as it is $|x|$ not $x$.
![[Pasted image 20230805090953.png]]

![[Pasted image 20230805093640.png]]

![[Pasted image 20230805114912.png]]

![[Pasted image 20230807113327.png]]
![[Pasted image 20230807113337.png]]
![[Pasted image 20230807113348.png]]

![[Pasted image 20230807125534.png]]

![[Pasted image 20230809101217.png]]

![[Pasted image 20230809101722.png]]

![[Pasted image 20230809101751.png]]

![[Pasted image 20230809102944.png]]

### Determining the value of Constants
$$
\begin{split}
\lim_{ x \to 0 } \frac{ A+B\cos x + C\sin x }{ x^{2} } &= 2, \text{find A,B,C} \\
\text{Putting x = 0 in the expression,} & \\
A+B &= 0 \\
\text{Expanding cos,} & \\
\\
\lim_{ x \to 0 } \frac{ \displaystyle -B + B \left( 1 -\frac{ x^{2} }{ 2! } + \frac{ x^{4} }{ 4! } \right) + C \left( x - \frac{ x^{3} }{ 3! } \right)}{ x^{2} } &= 2  \\
\\
\lim_{ x \to 0 } \frac{ C }{ x } + \frac{ -B }{ 2 } + \frac{ -C }{ 3! }x + \frac{ B }{ 4! }x^{2} &= 2 \\
\\
\end{split}
$$
Thus, C = 0 otherwise the first term will not be indeterminate and the limit will be $\pm\infty$. B = -4 and A = 4

We have to analyse the question by taking various cases. 
![[Pasted image 20230809090214.png]]

In some questions we start expanding the terms and then analyse,
![[Pasted image 20230809090708.png]]

