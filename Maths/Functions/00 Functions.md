Links: [[01 Terminology]], [[02 Elementary Graphs]], [[04 Graphs of Trigonometric Functions]]
___
# Functions
Function is a rule of correspondence which relates*each* element of a given set A to a *unique* element of another set B. If function f is defined from set A set B then it is denoted as,
$$f: A \to B$$

If f relates element $a \in A$ to element $b \in B$ then it is denoted as,
$$f(a) = b$$
$b$ is called **image** of $a$ and $a$ is called the **pre-image** of $b$. 

A is called *Domain* of function and B is called the *Co-Domain.*
The set containing all images is called *Range.*  It is a subset of the co-domain.

The variable which takes values from set A is called *independent variable* and the variable which takes values from set B is called *dependent variable.*
$$y = f(x)$$
here, x is independent and y is dependent variables. 

![[Pasted image 20230527074036.png]]

Thus we can say that function is a special case of [[04 Relations|relation]] when some extra conditions are imposed,
1. No element of set A must be left without an image. 
2. A given input should have exactly one output. 

Graphically, no vertical line should intersect graph of the function more than once, though a horizontal line may intersect any number of times. 

If $f: A \to B$ and $n(A) = n_{1}, n(B) = n_{2}$, then the number of functions which can be defined from A to B will be,
$$N = n_{2}^{n_{1}}$$
(defining functions from A to B is equivalent to distributing all $n_{1}$ different objects among $n_{2}$ persons)

"Number of Functions" questions are basically questions of [[00 Permutation and Combination]],

![[Pasted image 20230527075957.png]]

### Classification of Functions
- [[00.1 Into & Onto|Into/Onto]]
- [[00.2 One-One & Many One|One-One/Many One]]
- [[00.3 Even & Odd|Even/Odd]]
- [[00.4 Periodic & Non-Periodic|Periodic/Non-Periodic]]


## Composite Function
Function of a function. 

If $f(x): A \to B$ and $g(x): C \to D$ are 2 functions,
$$f(g(x)) = fog(x) = fog:C \to B$$
$$g(f(x)) = gof(x) = gof:A \to D$$

$$D_{fog} \subseteq D_{g}$$
$$R_{fog} \subseteq R_{f}$$

Also, start from the last 2,
$$f\ o \ g\ o\ h = f\ o \ (g\ o\ h) $$

If there are two, functions, then $fog$ and $gof$ both need not be defined,

![[Pasted image 20230531084907.png]]

Finding Composite Functions, i.e. to find $f(g(x))$,
1. Replace x with g(x) in f(x) everywhere, i.e. even in the conditi0n.
2. Substitute expression for g(x) and write associated condition if any, alongside it. 
3. If conditions are present, then solve them. 

Example,
![[Pasted image 20230601084306.png]]

In case there are multiple definitions of any of the two functions, solve outer function's condition for the values of x, and put the values of the inner function according to the value of x.

Example,
![[Pasted image 20230601090006.png]]
![[Pasted image 20230601090310.png]]


## Solving Equations and Inequalities using Graphs
To solve for $x$ in $f(x) = g(x)$, draw $y = f(x)$ and $y=f(x)$ and find the x-coordinate of the intersection of their graphs. This x-coordinate is the solution. To fond the equation we have to solve the equation. In general, the graph will not give the value of solution. 

In some questions we might have to analyse the slope at a point to find which curve goes above which one. And find the value of x for a certain value of y. 


The number of intersections is the number of solutions. Thus if question asks for number of solutions, we can use graphs. 
To find number of solutions we can rearrange the terms but keep in mind that domain should not change.

To solve $f(x) > g(x)$, draw $y = f(x)$ and $y=g(x)$ and  find the intervals of x in which the graph of $f(x)$ is above that of $g(x)$. That will be the solution.

If solutions are obtained in periodic sense then first write solution in one cycle then for general solution, add integral multiple of fundamental period. 

For example, in solving, $\sin x \geq \frac{1}{2}$, we get particular solution, $\displaystyle \left[ \frac{ \pi }{ 6 }, \frac{ 5\pi }{ 6 } \right]$. To write the general solution we write, $\displaystyle \left[ 2n\pi+ \frac{ \pi }{ 6 }, 2n\pi + \frac{ 5\pi }{ 6 } \right]$

Another example,
![[Pasted image 20230520094149.png]]

If we do not know the  value of x corresponding to a particular y in a trigonometric function, then write the value using inverse, take its mod, and then subtract or add to even or odd multiples of half of fundamental period. 

![[Pasted image 20230520093059.png]]
![[Pasted image 20230520093115.png]]

In case of inequality, we add the fundamental period to this itself. 

## Misc. Concepts

- If $f(x)$ is a polynomial satisfying,
  $$f(x) + f\left( \frac{1}{x} \right) = f(x) \cdot f\left( \frac{1}{x} \right)$$
then,
$$f(x) = \pm x^{n}+1$$

- If $f(x)$ is a polynomial satisfying,
  $$f(a+x) = f(a-x)\ or\ f(x) = f(2a-x)$$
then its graph is symmetric about $x=a$

### Identical Function
Two functions are identical only if their domains, ranges and for any given x they produce the same y.

For example $\sqrt{ x^{2} }$ and $(\sqrt{ x })^{2}$ look the same but are different as their domains are different. 

### Homogeneous Expression
[[01 Partial Differentiation#Homogeneous Function]]

$f(x,y)$ is called HE of degree n if $f(tx,ty) = t^{n}f(x,y)$.
n could be anything. 

![[Pasted image 20230602084232.png]]

### Explicit and Implicit 
Explicit is when y = some expression of x.
Implicit is when it is not implicit, i.e. y and x are not separated. 
e.g. $y^{3} + x = 7$ however, we can convert it into explicit as $y = (7-x)^{1/3}$. 

However, there are some implicit functions which cannot be expressed in explicit form. e.g. $y + e^{y} = x^{3}$.

### Symmetry
If $f(x)$ satisfies $f(a-x) = f(a+x)$ or $f(x) = f(2a-x),\ \forall\ x \in D_{f}$, then the graph $y = f(x)$ will be symmetric about x = a. 

If a = 0, then the function is even. 

![[Pasted image 20230602085057.png]]

If $f(a+x) = -f(a-x)$ or $f(2a-x) = -f(x),\ \forall\ x \in D_{f}$ then the graph of f(x) will be symmetric about the point (a. 0). 

If a = 0, then the function is odd. 

![[Pasted image 20230602085108.png]]

For example, 
![[Pasted image 20230602085511.png]]

If $f(a+b) = f(a-x),\ \forall\ x$ and $f(b+a) = f(b-a),\ \forall\ x$, where $a\neq b$  then y = f(x) will be a periodic function and will be symmetric about infinite lines. 