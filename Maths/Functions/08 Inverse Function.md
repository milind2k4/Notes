Links: [[06 Domain of Functions]], [[07 Range of Functions]]
___
# Inverse Function
$$f:A \to B$$

If$f$ is [[00.2 One-One & Many One|One-One]] and [[00.1 Into & Onto|Onto]] (i.e. it is **bijective**) then there exist a unique function $g: B \to A$ such that if $f(a) = b$, then $g(b) = a\ \forall\ a \in A$.

$g(x)$ is called the inverse of $f(x)$ and is denoted by $f^{-1}(x)$.

For f to be invertible, it should be One-One (injective) and Onto (surjective) and if so, then it is called **Bijective.**


Range and Domain of $f$ are flipped in $f^{-1}$. 
$$D_{f} = R_{f^{-1}}$$
$$R_{f} = D_{f^{-1}}$$

Note: If in question co-domain is not given, we check for one-one and assume that the function is onto. 

For $f$ and $f^{-1}$,
$$(f^{-1})^{-1}=f$$
$$f(f^{-1})=x$$

Graph of f and $f^{-1}$ are symmetric about the line y = x. As if (a, b) lies on y = f(x) then (b, a) will lie on $y = f^{-1}(x)$, and we know that (a, b) and (b, a) are reflections of each other on y = x.

Thus, taking reflection of graph of y = f(x) on y = x will give the graph of $y = f^{-1}(x)$.  

It can also be obtained by interchanging x and y axes and rotating it by 90 degrees clockwise and then flipping the graph along the y axis.  

![[Pasted image 20230601092237.png]]

### To find Inverse functions
Given $f(x)$.
1. **Check for one-one and onto.**
2. If bijective then interchange x and y.
3. Express y in terms of x.
4. Obtained expression will be the required inverse. 

If after solving for y we get two definitions, then verify the correct definition with the help of a point on f(x). 

![[Pasted image 20230601094702.png]]


### Derivatives

For derivatives of inverse functions,
$$\begin{split}
f(f^{-1}(x)) &= x \\
f'(f^{-1}(x))(f^{-1}(x))' &= 1\\
(f^{-1}(x))' &= \frac{1}{f'(f^{-1}(x))}\\
&=  \left.\frac{1}{f'(x)}  \right|_{x=f^{-1}(x)}
\end{split}$$
replace $x$ in the derivative of the non-inverse function with $f^{-1}(x)$


To find derivative of an inverse function at a point we can take the reciprocal of the derivative of the function at that point,
$$\left((f^{-1}(x))' \right)_{A'} = \frac{ 1 }{ (f'(x))_{A} }$$
Or,
$$\tan \beta = \frac{ 1 }{ \tan \alpha } = \cot \alpha = \tan(90 - \alpha )$$
this means that if the graph of the function makes an angle $\alpha$ with the x-axis at a point, the graph of inverse function will make angle $\alpha$ with the y-axis at the corresponding point.

For example,
![[Pasted image 20230602074440.png]]

### Some Results
Composite of $f$ and $f^{-1}$,
$$f(f^{-1}(x)) \equiv x,\ \forall\ x \in D_{f^{-1}}$$
$$f^{-1}(f(x)) \equiv x,\ \forall\ x \in D_{f}$$
$$f(f^{-1}(x)) \centernot\equiv f^{-1}(f(x))$$
$$f(f^{-1}(x)) = f^{-1}(f(x)),\ \forall\ x \in D_{f} \cap D_{f^{-1}}$$

Inverse of composite function,
$$(fog)^{-1} = g^{-1}of^{-1} = g^{-1}(f^{-1}(x))$$
Similarly, for any number of compositions,
$$f(x) = h\ o\ g\ o\ k\ o\ p$$
$$f^{-1}(x) = p ^{-1}(k^{-1}(g^{-1}(h^{-1}(x))))$$

Point of intersection of $y=f(x)$ and $y =f^{-1}(x)$ is the point of intersection of $y= f(x)$ and $y=x$

If A is point of intersection of $y = x$ and $y = f(x)$ then it will also lie on $y = f^{-1}(x)$. 

The graphs of $y = f(x)$ and $y = f^{-1}(x)$ may intersect at a point which does not lie on the line y = x. For example y = -x, which is a self inverse. 
$1 - x^{5}$ and $(1-x)^{1/5}$ intersect at (0, 1) and (1, 0) which do not lie on y = x.

Thus, to solve $f(x) = f^{-1}(x)$ we cannot solve $f(x) = x$, as some solutions may be lost.  But if $f(x)$ is an invertible function and $a$ is a solution of $f(x) = x$, then it will also satisfy $f(x) = f^{-1}(x)$.

However, if we can show (either graphically or otherwise) that the graphs only intersect at points which are on y = x,

![[Pasted image 20230602081443.png]]

