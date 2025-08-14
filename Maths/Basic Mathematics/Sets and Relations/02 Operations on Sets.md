Links: [[01 Subsets]]
___
# Operations on Sets
## Union 
Denoted by $A \cup B$ or $A + B$.

A set which contains all the elements and those only which are present in either of the sets.

![[Union.png]]

### Laws
1. Commutative,
	$$A \cup B = B \cup A$$
1. Associative,
	$$(A \cup B) \cup C = A \cup (B \cup C)$$
1. Idempotent,
	$$(A \cup A)= A$$
1. Law of $\phi\ and\ U$: 
	$$A \cup \phi= A$$
	$$A \cup U = U$$

## Intersection 
Denoted by $A \cap B$ or $A . B$.

A set which contains only the elements and those only which are present in both of the sets.

![[Intersection.png]]

If no element is common then they are called "Disjoint Sets"
in this case $A \cap B = \phi$

### Laws
1. Commutative,
	$$A \cap B = B \cap A$$
1. Associative,
	$$(A \cap B) \cap C = A \cap (B \cap C)$$
1. Idempotent,
	$$(A \cap A)= A$$
1. Distributive 
	$$A \cup (B \cap C) = (A \cap B) \cup (B \cap C)$$
	$$A \cap (B \cup C) = (A \cup B) \cap (B \cup C)$$
1. Laws of $\phi\ and\ U$:
	$$A \cap \phi = \phi$$
	$$A \cap U = U$$

## Subtraction
Denoted by $A - B$ or $A \setminus B$

A set which contains only the elements in A which are not present in B.

$$
\begin{split}
A - B &= A \cap \bar{B} \\
&= A - (A \cap B) \\
\end{split}
$$

I.e.,
$$x \in A-B \implies x \in A\ \&\ x \notin B$$

![[Subtraction.png]]

## Symmetric Difference 
$$(\triangle, \oplus,\ominus)$$
It is a set which contains all elements in $A$ or $B$ but not in both.

$$A\ \triangle\ B = (A - B) \cup (B - A)$$
$$A\ \triangle\ B = (A \cup B) - (A \cap B)$$

I.e.,
$$x \in A \Delta B \implies (x \in A\ or\ x \in B)\ \&\ x \notin (A \cap B)$$

![[Symmetric Diff.png]]

## Compliment 
$$(', \bar{\phantom{ A }}, {}^{C})$$
$A$ set containing all elements of universal set which are not present in $A$.

$$A' = U - A$$

![[Compliment.png]]

### Properties:
1. Double,
	$$(A')' = A$$

3. De Morgan's Law: 
	$$(A \cup B)' = A' \cap B'$$
	$$(A \cap B)' = A' \cup B'$$

2. Compliment of $\phi, U$,
	$$\phi' = U$$
	$$U' = \phi$$

3. Union and Intersection with Compliment, 
	$$A \cup A' = U$$
	$$A \cap A' = \phi$$
   