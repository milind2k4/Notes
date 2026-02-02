Links: [[02 Selection]], [[03 Distribution]]
___
# Grouping 
#### Different Group Sizes
If n different objects are to be divided into k groups with group sizes as $n_{1},n_{2},n_{3} \dots n_{k}$ where no two groups have same size (i.e. $n_{i} \neq n_{j}$ if $i \neq j$). And,
$$n = \sum_{i=1}^{k} n_{i}$$

Then no. of ways,
$$= \frac{ n! }{ n_{1}!\ n_{2}!\ n_{3}!\ \dots\ n_{k}! }$$

This is obtained from selecting $n_{1}$ objects out of $n$ and calling it a group and so on.
$$
\begin{split}
N &= {n \choose n_{1}}. {n-n_{1} \choose n_{2}}. {n-n_{1}-n_{2} \choose n_{3}}\dots {n_{k} \choose n_{k}} \\
\\
&= \frac{ n! }{ (n-n_{1})!\ n_{1}! }. 
\frac{ (n-n_{1})! }{ (n-n_{1}-n_{2})!\ n_{2}! }. 
\frac{ (n-n_{1}-n_{2})! }{ (n-n_{1}-n_{2}-n_{3})!\ n_{3}! }\dots \\
\\
&= \frac{ n! }{ n_{1}!\ n_{2}!\ n_{3}!\ \dots\ n_{k}! }
\end{split}
$$

Alternatively, it can be explained by,
![[Pasted image 20231213103524.png]]

Example,
![[Pasted image 20231213104022.png]]

#### Same Group Sizes
If n different objects are divided into k groups such that $p_{i}$ number of groups have same size $n_{i}$, for $i = 1,2,3\dots r$, then required number of ways,
$$= \frac{ n! }{ (n_{1}!)^{p_{1}}\ (n_{2}!)^{p_{2}}\ \dots\ (n_{r}!)^{p_{r}}\ p_{1}!\ p_{2}!\ \dots\ p_{r}! }$$

This is a general formula and it works with different group sizes as well. 

Here,
$$n = \sum_{i = 1}^{r} n_{i}p_{i}$$

This formula can be  found by using the previous one. 
We divide $n!$ by $n_{1}!$, $p_{1}$ times as there are $p_{1}$ groups which have $n_{1}$ objects. Thus giving $(n_{1}!)^{p_{1}}$.

Now, there are $p_{1}$ groups which have the same size, thus we divide by $p_{1}!$ because we counted $n_{1}$ groups $p_{1}$ times due to order. [[01 PnC, Gap & Tie method, Like Objects#Taken all at a time|Using this formula.]]

![[Pasted image 20231213105245.png]]
![[Pasted image 20231213110105.png]]

Example,
![[Pasted image 20231213105722.png]]

If we need to distribute formed r groups among r persons, each getting 1 group, then no. of ways = $n!$. 
This is because all those groups are treated as different objects even if the group sizes are the same. 

In grouping, we will not distribute 2 groups to 1 person in rounds. This is because then there will be order.

![[Pasted image 20231213110858.png]]
