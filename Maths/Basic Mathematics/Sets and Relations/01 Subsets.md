Links: [[00 Sets]]
___
# Subsets
$A$ is called the subset of $B$ if all elements of $A$ are present in $B$.
It is written as $A \subseteq B$
($\subseteq$ is "either subset of or equal to")

- $A$ is called the subset of $B$ and $B$ is called the superset of $A$.
- If sets $A$ and $B$ are subsets of each other, then they are equal.
  i.e $A \subseteq B\ \&\ B \subseteq A \implies A = B$
	- This is used to show that two sets are equal.
	- i.e. Prove that $x \in A \implies x \in B$ and $x \in B \implies x \in A$.
- If $x \in A$ and $A \subseteq B$ then $x \in B$
- Every set is a subset of itself.
- Null set is the subset of every set.

### Proper and Improper Subset
$A$ is proper subset of $B$ then all elements of $A$ are present in $B$ and $B$ contains at least one extra element. (i.e. $A \subset B, A \neq B, n(B) > n(A)$)

Denoted by $A \subset B$ (like $A < B$ and $A \leq B$)

$A = \{1,2\}$
$B = \{1,2,3\}$
$A$ is subset of $B$.
$A$ is proper subset of $B$.
$A$ is not equal to $B$.

$A = \{1,2\}$
$B = \{1,2\}$
$A$ is subset of $B$.
$A$ is not proper subset of $B$.
$A$ is equal to $B$.

That is, if $B$ is an improper subset of $B$, then $A$ and $B$ are equal.

Number of Proper Subsets: $2^{m}-1$

![[Pasted image 20230418073422.png]]

### Misc.
1. If $n(A)=m$, then number of subsets of $A$ is $2^{m}$.

5. Intervals are subsets of **R**.
	- Open: ()
	- Closed: [] 
	- Length of Interval [a, b]: $b-a$
	  
	  ![[length of intervals.png]]
	- $\infty\ \text{and}\ -\infty$ will always have ().
	


#### Super Set
If A is a subset of B then B is a super set of A.

## Power Set
Power Set of $A$ is denoted as $P(A)$ and is the set containing the subsets of set $A$

$$
\begin{split}
n(A) &= m \\
n(P(A)) &= 2^m
\end{split}
$$

## Venn Diagram
It is a visual representation of different relations between sets.

We use a Rectangle as $U$ and Circles (or Ellipses if more than 3) for sets.

$n$ number of sets divide 2d space in $2^{n}$ regions. 

#### Circles(up to 3 sets)
![[venn diagram circle.png]]

#### Ellipses (any number of sets)
![[venn diagram ellipse.png]]