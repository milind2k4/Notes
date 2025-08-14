Links: [[00 Sequence and Series]]
___
# Arithmetic Progression
A sequence in which the next term is obtained by adding a constant value to the previous term. This constant value is called common difference.

Difference of consecutive terms will be constant, and this constant difference is called **Common Difference (CD).**

An AP can be given as, 
$$a, a+d, a+2d, a+3d, \dots$$
First term: $a$
Common difference: $d$
General term: 
$$T_{n} = a+(n-1)d$$

Non-constant AP means $d \neq 0$

*(General term is also called last term $l$ if there are only n terms.)*

Sum,
$$S_{n}= \frac{n}{2} [ 2a + (n-1)d ]$$

$$or$$

$$S_{n} = \frac{n}{2} [ a + l ]$$

### Points to Remember
$$
\begin{split}
T_{n} &= a + (n-1)d \\
&= d.n + (a-d)
\end{split}
$$
Thus, nth terms of an AP will be a linear expression of n and vice-versa. 
And the coefficient of n will be the CD. 

Using this, we can write the general term of an  AP very quickly,
![[Pasted image 20230612084332.png|260]]


The sum,
$$
\begin{split}
S_{n} &= \frac{ n }{ 2 } (2a + (n-1)d) \\
&= \frac{ d }{ 2 } n^{2} + n \left( \frac{ 2a - d }{ 2 } \right)n + 0 \\
&= \alpha n^{2} + \beta n
\end{split}
$$

Thus the $S_{n}$ of a non-constant AP is a quadratic in n with the constant term being zero and vice-versa. 
Thus, $n^{2} + n + 1$ cannot be the $S_{n}$ of an AP.

If $S_{n}$ is given in the question, we can use this and equate the corresponding coefficients. 

## Properties of AP
- If $a,b,c$ are in an AP, 
	$$2b = a + c$$
	$$b - a = c-b$$
	$$(b-a) - (c-b) = 0$$
  $\\$

-  $T_{1} + T_{n} = T_{2} + T_{n-1}$ and so on. The distance from both sides should be the same. The sum of the subscripts is always $n+1$
	In case of odd terms, the middle term will be doubled, i.e. $T_{m} + T_{m}$ where $m$ represents the middle term. 
  $\\$

- If we add something to every term, the resulting series will still be an AP. And the common difference will still be $d$. 
  $\\$

- If we multiply something to every term, the resulting series will still be an AP. And the common difference will become $\lambda d$. *(where $\lambda$ is the something multiplied)*
  $\\$


- If there are 2 APs, $AP_{1}(a,d,n)$ and $AP_{2}(A,D,n)$,
	- The sum (difference) of their consecutive terms will still be an AP. The common difference of the new AP will be $d + D$. ($d-D$)
	- If we multiply or divide consecutive terms, the resulting sequence will not be in an AP.


## Selecting terms for AP
This is useful mainly if the sum is given. Thus if sum is not given, we assume general terms like,
$$a, a+d, a+2d, a +3d \dots $$


#### Odd number of terms
$$\dots\ a - d,\ a,\ a + d\ \dots$$
**CD: $d$**

#### Even number of terms
$$\dots\ a - 3d,\ a - d,\ a + d,\ a + 3d\ \dots$$
**CD: $2d$**

## Arithmetic Mean

AM of $a_{1}, a_{2}, a_{3}, a_{4}\ \dots$ 
$$M =\frac{ \displaystyle \sum_{i = 1} ^{n} a_{i} }{ n }$$

AM of numbers cannot be less than the least number and greater than the greatest of the numbers. 

AM of 2 terms,
$$M = \frac{a+b}{2}$$

$2M= a + b$, thus, $a, M, b$ are in AP. 

AM of the terms taken symmetrically from the left and the right will be constant. 
Thus if the AP is ,
$$a_{1},a_{2},a_{3},a_{4} \dots a_{n-1}, a_{n}$$
Then,
$$\frac{ a_{1}+a_{2} }{ 2 } = \frac{ a_{2}+a_{3} + a_{n-1} + a_{n-2} }{ 4 }$$
And they will be equal to the AM of the whole series,
$$M = \frac{ a_{1} + a_{2} + a_{3} + \dots a_{n-1} + a_{n} }{ n }$$
If the number of terms is odd, $a_{\frac{n+1}{2}}$ will be middle term. Otherwise, there will be two middle terms, $a_{\frac{n}{2}}, a_{\frac{n}{2}+1}$. And,
$$M = a_{\frac{n+1}{2}},\ n \text{ is odd}$$
$$M = \frac{ a_{\frac{n}{2}} + a_{\frac{n}{2}+1} }{ 2 },\ n \text{ is even}$$


#### Inserting n AMs between two numbers
Let $a,b$ are two given numbers and $A_{1}, A_{2}, A_{3} \dots$ are n AMs between them then.
$$a, A_{1}, A_{2}, A_{3}, \dots, A_{n},b$$ 
are in AP.
Number of terms = $n+2$

$$
\begin{split}
\sum_{i=1}^{n}A_{i} &=  na + d (1+2+3+\dots n) \\\\
&=  na + \frac{ n (n+1) }{ 2 }d \\
&= \frac{n}{2} [ a + a + (n+1)d] \\
&= \frac{n}{2} (a + b)  \\
&= n (\text{AM of a \& b})\\\\
\text{Now,} \\
b &=  T_{n+2} \\
 &= a + (n+1)d \\\\
\text{Thus,} \\
d &= \frac{b-a}{n+1} 
\end{split}
$$
Thus the kth AM will be,
$$A_{k} = a + (k+1-1)d = a + kd$$
$$A_{k} = \frac{ (n-k+1)a + kb }{ n+1 }$$
We can also use section formula,
![[Pasted image 20230613094127.png]]


## Examples
To find the term which is the first +ve or first -ve, we take $T_{n} = 0$ and find the value of n. If it is integer, then the term just after it will be first -ve or +ve. If n is not integer, then the $[n]+1$ th term will be the answer. 

Using this we can also find the value of n for which the sum is max. or min. 

Finding common terms and number of common terms,
![[Pasted image 20230612083809.png]]
![[Pasted image 20230612083821.png]]

To prove that something is a perfect square, we try to make it a whole square formula. 

To prove some modification of some terms are in AP,
![[Pasted image 20230613092152.png]]
![[Pasted image 20230613092215.png]]
