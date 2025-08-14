Links: [[01 Acids and Bases]]
___
# Buffer Solution
Solution which resist change in its pH on addition of small amount of an acid , base or water. 

The pH change in buffer solution is very small on addition of small amount of acid, base or water.

Buffer solutions are stable solutions and pH does not change on standing. 

Examples of buffer solutions are: 
- aqueous solution of borax ($\ce{ Na_{2}B_{4}O_{7}.10H_{2}O }$)
- animal blood is buffered due to dissolved $\ce{ CO_{2} }$ i.e. $\ce{ H_{2}CO_{3} + NaHCO_{3} }$
- aqueous solution of $\ce{ CH_{3}COOH + CH_{3}COONa }$

### Types of Buffer Solution
1. Mixed Buffer:
	1. Acidic Buffer 
	2. Basic Buffer
2. Simple Buffer

#### Mixed Buffer
Buffer of mix of weak acid/base and its conjugate base/acid.

Since conjugate acid or base cannot stay in ion form in the solution, they form salts. 
##### Acidic Buffer
A solution of weak acid and its conjugate base. 

Some common examples are,
$$\ce{ \underset{ weak acid }{ CH_{3}COOH } + \underset{ conjugate base }{ CH_{3}COONa } }$$
$$\ce{ \underset{ weak acid }{ H_{2}CO_{3} } + \underset{ conjugate base }{ NaHCO_{3} } }$$
$$\ce{ \underset{ weak acid }{ H_{3}PO_{4} } + \underset{ conjugate base }{ NaH_{2}PO_{4} } }$$

**Note:** *Strong acid and its conjugate base do not form buffer solution.*

##### Basic Buffer
A solution of weak base and its conjugate acid. 

Some examples are,
$$\ce{ \underset{ weak base }{ NH_{4}OH } + \underset{ conjugate acid }{ NH_{4}Cl } }$$
$$\ce{ \underset{ weak base }{ C_{6}H_{5}NH_{3}OH } + \underset{ conjugate acid }{ C_{5}H_{5}NH_{3}+Br- } }$$

**Note:** *Strong base and its conjugate acid do not form buffer solution.*

#### Simple Buffer
Solution of salt of WA and WB. 

Example, aq. soln. of $\ce{ CH_{3}COO- NH_{4}+ }$

### Buffer Action
Since water is not buffered, adding even 1 ml, of 1 M HCl to it changes its pH from 7 to 3. 

Let us consider an acidic buffer of $\ce{ CH_{3}COOH + CH_{3}COONa }$

Now if a small amount of acid (HCl) is added, the externally added $\ce{ H+Cl- }$ is used up by $\ce{ CH_{3}COONa }$,
$$\ce{ CH_{3}COONa + HCl -> CH_{3}COOH + NaCl }$$
Now, since $\ce{ CH_{3}COOH }$ is a weak acid, $\ce{ [H+] }$ offered by it is negligible and the pH does not change by any considerable amount. 

Now if a small amount of base (NaOH) is added, the externally added base is used up by $\ce{ CH_{3}COONH }$,
$$\ce{ CH_{3}COOH + NaOH -> CH_{3}COONa + H_{2}O }$$

## [[07.5 pH of Buffer Solution]]

## Buffer Capacity
Measure of effectiveness of buffer solution. The higher is the buffer capacity, the more effective the buffer solution is.

It is defined as number of moles of acid or base to be added into 1 l of a buffer solution to change its pH by 1 unit, keeping (a+s) or (b+s) to be constant. 

For example, an acidic buffer, HA + NaH (a + s) is constant = k.
Now pH will be,
$$
\begin{split}
pH &=  pk_{a} + \log \frac{ s }{ a }\\
&= pk_{a} + \frac{ 1 }{ 2.303 } \ln \frac{ s }{ k -s } \\
\frac{ dpH }{ ds } &= 0 + \frac{ 1 }{ 2.303 } \frac{ k-s }{ s } \times \frac{ (k-s) - s(-1) }{ (k-s)^{2} } \\
&= \frac{ 1 }{ 2.303 } \frac{ 1 }{ s } \times \frac{ k }{ k - s } \\
\frac{ ds }{ dpH } &= \frac{ 2.303 s(k-s) }{ k } 
\end{split}
$$
This term, $\displaystyle \frac{ ds }{ dpH }$ is the buffer capacity.

Thus for acidic buffer, buffer capacity is, (-ve sign as adding acid decreases pH)
$$-\frac{ da }{ dpH } = \frac{ ds }{ dpH }$$
which is,
$$\frac{ ds }{ dpH } = 2.303 \frac{ s(k-s) }{ k }$$
$$\frac{ ds }{ dpH } = 2.303 \frac{ as }{ a+s }$$

For basic buffer buffer capacity is,
$$\frac{ db }{ dpH } = -\frac{ ds }{ dpH }$$

For most effective buffer, we find the maxima of $\displaystyle \frac{ ds }{ dpH }$,
$$\frac{ \displaystyle d\left( \frac{ ds }{ dpH } \right) }{ ds } = 0$$
Which gives,
$$a = s = \frac{ k }{ 2 }$$
Thus the best buffer is when the concentration of salt and acid is the same. 

However, the buffer is effective in a range around the max buffer capacity.

Buffer is effective when,
$$0.1 \leq \frac{ s }{ a } \leq 10$$
it is most effective when,
$$\frac{s}{a} = 1$$

(for basic buffer change a to b)
![[Pasted image 20230707205948.png]]

For the same mixes, and if concentrations of both the salt and the acid is the same, the one with more concentration will be better buffer.
![[Pasted image 20230707210548.png]]