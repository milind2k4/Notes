Links: [[00 Binomial Theorem]]
___
# Permutation and Combination
### Fundamental Principle of Counting
#### Addition Rule
If a work can be done in $a$ ways using process 1 and in $b$ ways using process 2, then total number of ways in which it can be completed will be $a + b$.  

#### Product or Multiplication Rule
If an event can occur in $p$ ways and other even can occur in $q$ ways, then total number of ways of occurrence of both the events will be $pq$.

#### Bijection Rule
We can either select favourable, or reject unfavourable.

I.e. Favourable = Total - Unfavourable

### Some PTR
Addition means *or/option.*

Product means *and/condition.*

In addition, no. of ways must be non overlapping, i.e. mutually exclusive. 

In multiplication, no. of ways must be independent. 
If no. of ways are dependent, then make mutually exclusive cases. 

If no. of favourable cases keeps on increasing, then try bijection rule. 

In multiplication, if order is possible, then it will be counted (automatically).

Try to satisfy given constraints first in a question.

Convert "at least" or "at most" into exactly. These will be connected by "or".

### Examples 
![[Pasted image 20231206162424.png]]

![[Pasted image 20231206164049.png]]

![[Pasted image 20231206165016.png]]

![[Pasted image 20231206165513.png]]

![[Pasted image 20231208145359.png]]

![[Pasted image 20231208145830.png]]

![[Pasted image 20231208150930.png]]

![[Pasted image 20231208155530.png]]

![[Pasted image 20231208155645.png]]

![[Pasted image 20231208155729.png]]

## [[01 PnC, Gap & Tie method, Like Objects]]

## Inclusion Exclusion Principle (IEP)
When there is nested loop while applying bijection rule, we apply IEP. 

Total no. of cases under some restrictions $R_{1},R_{2}\dots R_{n}$ $=$ 

Total no. of cases without any restrictions 

$- \displaystyle \sum$ No. of cases when restriction $R_{i}$ is violated 

$+ \displaystyle \sum$ No. of cases when restrictions $R_{i}$ and $R_{j}$ are violated 

$- \displaystyle \sum$ No. of cases when restrictions $R_{i}$, $R_{j}$ and $R_{k}$ are violated $+$

![[Pasted image 20231214125439.png]]

From here we get the formula,
$$r ^{n} - {}^{r}C_{1} (r-1)^{n} + {}^{r}C_{2} (r-2)^{n} + \dots$$

![[Pasted image 20231214134359.png]]

#### Derangements 
Let n persons are sitting on n chairs, now all of them get up and are seated again with the condition that none of them sit on their original position, then total no. of ways will be,
$$
\begin{split}
D_{n} &= n! - {}^{n}C_{1}. (n-1)! + {}^{n}C_{2}. (n-2)! - \dots \\
&= n! - \frac{ n!(n-1)! }{ 1!(n-1)! } + \frac{ n!(n-2)! }{ 2!(n-2!) } - \frac{ n!(n-3!) }{ 3!(n-3)! } + \dots \\
&= n!\left( 1 - \frac{ 1 }{ 1! } + \frac{ 1 }{ 2! } - \frac{ 1 }{ 3! } \dots + \frac{ (-1)^{n} }{ n! } \right)
\end{split}
$$

Thus we get,
$$D_{n} = n!\left( \frac{ 1 }{ 2! } - \frac{ 1 }{ 3! } + \frac{ 1 }{ 4! } - \dots + \frac{ (-1)^{n} }{ n! } \right)$$

![[Pasted image 20231214141836.png]]
![[Pasted image 20231214142358.png]]

## Multinomial Theorem 
[[00 Binomial Theorem#Multinomial Expansion]]

To find no. of ways of distributing n identical objects among r persons, we can find no. of non negative integral solutions of the equation,
$$x_{1} + x_{2} + x_{3} + \dots x_{r} = n$$
for which we can find coefficient of $x^{n}$ in,
$$(1 + x + x^{2} + \dots + x^{n})(1 + x + x^{2} + \dots + x^{n})\dots$$

Each way of forming $x^{n}$ in this equation corresponds to a valid distribution. 

The formula ${}^{n+r-1}C_{r-1}$ comes from here. 
Since adding $x^{n+1}$ in any of the brackets does not change the no. of way in which $x^{n}$ can be formed, we can add $x^{n+1}, x^{n+2} \dots \infty$. 

This forms a GP whose sum is $1 /1-x$, and thus we can write,
$$(1-x)^{-r}$$

Now here, the coefficient of $x^{n}$ will be ${}^{n+r-1}C_{r-1}$. 

#### Examples 
![[Pasted image 20231216185659.png]]
![[Pasted image 20231216185707.png]]

![[Pasted image 20231216190608.png]]
![[Pasted image 20231216190615.png]]

![[Pasted image 20231216191136.png]]
![[Pasted image 20231216191143.png]]


## Some Types of Questions 
### Divisors 
![[Pasted image 20231213093241.png]]
![[Pasted image 20231213095158.png]]
![[Pasted image 20231213100247.png]]
![[Pasted image 20231213100255.png]]

### Sum of Numbers
We will use symmetry of position and symmetry of digits along with place value, i.e. the fact that while summing we do 
$$(o_{1} + o_{2} + \dots) + (t_{1} + t_{2} + \dots).10 + (h_{1} + h_{2} +\dots).10^{2} + \dots$$

![[Pasted image 20231213112048.png]]
![[Pasted image 20231213112438.png]]

### Dictionary Problems
![[Pasted image 20231213140849.png]]

### Grid Problems 
![[Pasted image 20231214091047.png]]
![[Pasted image 20231214094839.png]]

![[Pasted image 20231214095618.png]]
![[Pasted image 20231214095932.png]]

### Set Problems 
![[Pasted image 20231216194704.png]]
![[Pasted image 20231216194716.png]]
![[Pasted image 20231216194915.png]]
![[Pasted image 20231216195640.png]]
![[Pasted image 20231216195910.png]]

## Misc. Examples 
![[Pasted image 20231212084648.png]]

![[Pasted image 20231212084735.png]]

![[Pasted image 20231212084745.png]]
![[Pasted image 20231212084804.png]]

![[Pasted image 20231212084829.png]]

![[Pasted image 20231212084911.png]]
(in 14, it would be $a > b > c + a > c  > b + a > b = c$, and the answer will be 285)

![[Pasted image 20231212085719.png]]

![[Pasted image 20231212085736.png]]

![[Pasted image 20231212085801.png]]

![[Pasted image 20231212085835.png]]

