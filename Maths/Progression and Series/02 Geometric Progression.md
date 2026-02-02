Links: [[00 Sequence and Series]]
___
# Geometric Progression

A sequence in which the ratio of any two consecutive terms is the same. This constant ratio is called the **Common Ratio (CR).** 
A general GP can be given as,
$$a, ar, ar^{2}, ar^{3}, \dots$$

First term: $a$
Common Ratio: $\displaystyle r = \frac{a_{2}}{a_{1}} = \frac{a_{3}}{a_{2}}$
General term:
$$T_{n} = ar^{n-1}$$

No term in a GP can be zero. 

Sum:
$$S_{n} = \frac{ a(1-r^{n}) }{ (1-r) } = \frac{ a(r^{n}-1) }{ (r-1) }$$
Proof:
$$
\begin{split}
S = a +\ &ar + ar^{2} + ar^{3} + \dots ar^{n-1} \\
rS =\ \ \ \ \ &ar + ar^{2} + ar^{3} + \dots ar^{n-1} + ar^{n}
\end{split}
$$
Subtracting them,
$$S(1-r) = a - ar^{n} = a(1-r^{n})$$
$$S = \frac{ a(1-r^{n}) }{ 1-r }$$
provided $r \neq 1$

$$S_{n} = na \text{ (when r = 1)}$$

When, $n \to \infty$, and $|r| < 1$, the sum goes towards a number which is,
$$S_{n} = \frac{a}{ 1 - r }$$

#### Sum of Power Function
$$\sum_{r=1}^{n} a^{r} = a \left( \frac{ r^{n}-1 }{ r-1 } \right)$$


## Properties of GP

- If $a,b,c$ are in GP, then $b^{2} = ac$
  $\\$

- If $a_{1},a_{2},a_{3},a_{4}\dots$ are in GP with CR $r$,
	- Adding a number to each terms results in a series which is not in GP. 
	- Multiplying a number to each term results in a GP with CR $r$
	- Raising each term to some power results in a GP with common ratio $r^{\lambda}$ *(where $\lambda$ is the some power)*
		- Thus the reciprocal of a GP is also a GP, with common ratio $\displaystyle \frac{1}{r}$
	  $\\$


- If there are 2 GPs, $GP_{1}(a,r,n)$ and $GP_{2}(A,R,n)$,
	- The sum (difference) of their consecutive terms will not be in GP in general. If $r = R$, then the sum (difference) is a GP. 
	- If we multiply or divide corresponding terms, the resulting sequence will be GP with CR their product (ratio).
	  $\\$


- $T_{1} \cdot T_{n} = T_{2} \cdot T_{n-1}$ and so on. The distance from both sides should be the same. The sum of the subscripts is always $n+1$
	- In case of odd terms, the middle term will be squared, i.e. $T_{m} \cdot T_{m}$ where $m$ represents the middle term. 

## Selecting terms for a GP
In general we can assume,
$$a, ar, ar^{2}, ar^{3}, \dots$$

#### Odd number of terms
$$\dots\ \frac{a}{r},\ a,\ ar \ \dots$$
**CR: $r$**

#### Even number of terms
$$\dots\ \frac{a}{r^{3}},\ \frac{a}{r},\ ar,\ ar^{3}\ \dots$$
**CR: $r^{2}$**

## Geometric Mean (GM)

 GM of $a_{1},a_{2},a_{3},\dots a_{n-1},a_{n}$ where all are positive, 
   $$GM = \left( \prod_{i=1}^{n}a_{i} \right) ^{\displaystyle \frac{1}{n}}$$


 GM of 2 +ve numbers $a, b$ is $\sqrt{ ab }$ and thus, $a,\sqrt{ ab }, b$ are in GP. 

GM of 2 -ve numbers $a, b$ is $-\sqrt{ ab }$

If a, b, c are 3 numbers in GP, then, $b = \pm \sqrt{ ac }$. If $b = \sqrt{ ac }$ then CR is $r = \displaystyle \sqrt{ \frac{ c }{ a } }$ and if $b = - \sqrt{ ac }$ then CR is $r = \displaystyle -\sqrt{ \frac{ c }{ a } }$. 

If GM is said then we only take the +ve values. 


To find GM the numbers need not be in GP, but if they are then the GM of symmetrically taken terms are equal and constant. 
That is, if the GP is,
$$g_{1}, g_{2},g_{3} \dots g_{n-1}, g_{n}$$
Then,
$$G = \sqrt{ g_{1} . g_{n} } = \sqrt[4]{ g_{2}. g_{3} . g_{n-1} . g_{n-2} }$$ 
$$G = (g_{1}. g_{2}. g_{3}. g_{4} \dots g_{n-1}. g_{n})^{1/n}$$
Which is in turn equal to,
$$G = g_{\frac{ n+1 }{ 2 }},\ n \text{ is odd}$$
$$G = \sqrt{ g_{\frac{n}{2}} . g_{\frac{n}{2}+1} },\ n \text{ is even}$$

#### Inserting n GM between 2 numbers

$$a, G_{1}, G_{2}, G_{3}, \dots, G_{n},b$$ 

are in G  P.
Number of terms = $n+2$

$$
\begin{split}
\prod_{i=1}^{n} G_{i} &=  a^{n} r ^{1+2+3+\dots n} \\
\\
&=  a^{n} \cdot r ^{ \Large \frac{n(n+1)}{2}} 
\\
&=  a^{n} \cdot (r^{n+1} )^{\Large \frac{n}{2}} 
\\
&= a^{n} \cdot \left( \frac{b}{a}  \right) ^{\Large \frac{n}{2}} 
\\
&= a^{\Large \frac{n}{2}} \cdot b ^{\Large \frac{n}{2}} 
\\
&= (\sqrt{ ab }) ^{n} 
\\
&= (\text{GM of a \& b})^{n} \\
\\
\text{As,} 
\\
b &=  T_{n+2} 
\\
 &= ar^{n+1} 
 \\
r^{n+1} &= \frac{b}{a} \\
\\
\text{Thus, } 
\\
r &= \left( \frac{b}{a} \right) ^{\Large \frac{1}{n+1}}
\end{split}
$$

Then kth GM will be,
$$G_{k} = ( a^{n-k+1} b^{k})^{ \large \frac{ 1 }{ n+1 }}$$
(the sum of powers of a and b is n+1)

## Examples
When there are terms like $5 + 55 + 555 + 5555 + \dots$,
![[Pasted image 20230613095639.png]]
![[Pasted image 20230613095647.png]]

The formula in [[02 Formula and Expansions]] are frequently used in GP questions,
![[Pasted image 20230613100600.png]]
![[Pasted image 20230613100614.png]]

![[Pasted image 20230614080944.png]]

![[Pasted image 20230614081406.png]]


![[Pasted image 20230614081708.png]]
![[Pasted image 20230614081718.png]]