Links: [[01 Arithmetic Progression]], [[02 Geometric Progression]] 
___
# Sequence and Series
#### Sequence
Terms following a pattern. 

#### General Term ($T_{r}$)
Where if we change a variable we can find all the terms of a sequence. 

#### Series
Expression obtained by adding a sequence.

$S_{n}$ is the sum of first n terms. 

To find general term $T_{n} =S_{n}-S_{n-1}$

Cross check with at least one term. 

### Sigma and Pi Notation
$$\ce{ Sigma = \sum = Sum }$$
$$\ce{ Pi = \prod = Product }$$
Both can be used without limits or with limits.

1. **Without Limits:** if the question contains 3 quantities, say x, y, z then $\sum x$ means adding all  terms *like x.* 
   Similarly, $\prod x$ means multiplying all possible terms *like x.*
   \
   For 3 quantities,
$$
\begin{split}
\sum x &= x + y + z\\
\sum (x+y) &= 2(x + y + z) = 2\sum x \\
\sum (x - y) &= 0 \\
\sum x^{2} &= x^{2} + y^{2} + z^{2} \\
\left( \sum x \right)^{2} &= (x + y + z)^{2} \\
\sum x(y-z) &= x(y-z) + y(x-z) + z(x-y) = 0 \\
\sum xy &= xy+yz+zx \\
\\
\prod x &= x y z \\
\prod x^{2} &= \left( \prod x \right)^{2} \\
\prod xy &= \prod x^{2} \\
\prod \frac{ x }{ y } &= 1 \\
\prod \frac{ x^{2} }{ yz } &= 1
\end{split}
$$
   
2. **With Limits:**
   $$\sum_{r=a}^{b} f(r) = f(a) + f(a+1) + f(a+2) + \dots f(b)$$
   $$\prod_{r=a}^{b} f(r) = f(a) . f(a+1) . f(a+2) . \dots f(b)$$

#### Some properties of Sum and Prod
Sum and product,
$$
\begin{split}
\sum (f(x) + g(x)) &= \sum f(x) + \sum g(x) \\
\sum (f(x).g(x)) &\neq \sum f(x) . \sum g(x) \\
\\
\prod (f(x). g(x)) &= \prod f(x) \times \prod g(x) \\
\prod (f(x) + g(x)) &\neq \prod f(x) + \prod g(x) \\
\end{split}
$$

Constant, (n is number of terms)
$$
\begin{split}
\sum k &= n \times k \\
\prod k &= k^{n} \\
\\
\sum k.f(x) &= k\sum f(x) \\
\prod k.f(x) &= k^{n} \prod f(x) 
\end{split}
$$

### Some formula
$$\sum_{r=a}^{b} f(r) = \sum_{r=a}^{b} f(a+b-r)$$
on RHS, the series is just written in reverse. 

#### Examples
![[Pasted image 20230612081110.png]]
(here notice that since limits are from 0 to 40, number of terms is 41)


## Sum of some Special Sequences

$n$ represents natural number.

Sum of first n natural numbers,
$$\sum n = \frac{ n(n+1) }{ 2 }$$

Sum of squares of first n natural numbers,
$$\sum n^{2} = \frac{ n(n+1)(2n+1) }{ 6 }$$
(the 2n+1 is the sum of  n and n+1)

Sum of cubes of first n natural numbers,
$$\sum n^{3} = \left( \frac{ n(n+1) }{ 2 } \right)^{2} = \left( \sum n \right)^{2}$$

Sum of first n odd numbers is n$^{2}$,
$$\sum 2n+1 = n^{2}$$
Sum of first n even numbers is $n^{2}+n$,
$$\sum 2n = n^{2} + n$$

Example,
![[Pasted image 20230615092207.png]]

Using these formula, we can write,
$$(a_{1}+a_{2} + a_{3} + \dots a_{n})^{2} = \sum a_{1}^{2} + 2\sum a_{1}a_{2}$$

Thus for 4 terms,
$$(a+b+c+d)^{2} = a^{2} + b^{2} + c^{2} + s^{2} + 2(ab + ac + ad + bc + bd + cd)$$

And, we can use this result to write the formula for sum of numbers taken 2 at a time,
$$\sum a_{1}a_{2} = \frac{ \left( \sum a_{1} \right)^{2} - \sum a_{1}^{2} }{ 2 }$$
