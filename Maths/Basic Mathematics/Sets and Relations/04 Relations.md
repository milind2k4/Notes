Links: [[00 Sets]]
___
# Relations
## Some Definitions
### Ordered Pair
Listing of two objects in a specific order. 

> Eg: $(a,b), (b,a)$
$(a,b) \neq (b,a)$

$(a,b,c) \to$ Ordered Triplet

### Cartesian Product
Is of two sets and is denoted as $A \times B$ which is

$$A \times B = \{(a,b) : a \in A,\ b \in B\}$$

E.g.
> $A = (1,2)\ \&\ B = (a,b)$
> $A \times B = \{ (1,a), (1,b), (2,a), (2,b) \} .$ 
> $B \times A = \{ (a,1), (a,2), (b,1), (b,2) \} .$ 


#### Properties of Cartesian Product
- $n(A \times B) = n(A) \times n(B)$
- $n(A \times B) = n(B \times A)$
- In general, $A \times B \neq B \times A$
- If any one of $A$ or $B$ is $\phi$ then $A \times B = \phi$

## Relation
A relation defined from a non-empty set $A$ to a non-empty set $B$ is a subset of $A \times B$, i.e. their cartesian product.

$$R : A \to B$$
$$R \subseteq A \times B$$

$(a,b) \in R$ is the same as $a\ R\ b$

![[Pasted image 20230525085929.png]]

- **Domain:** The set of all first elements of ordered pairs. It is a subset of set A.
  $$\text{Domain of R} = \{ a: (a,b) \in R \}$$
- **Co-Domain:** The set $B$.
- **Range:** The set of all second elements of ordered pairs. It is a subset of set B.
  $$\text{Range of R} = \{ b: (a,b) \in R \}$$

#### NOTE
If relation $R$ relates $a\ (\in A)$ with $b\ (\in B)$ then:

1. $(a,b) \in R$
1. $a\ R\ b$
1. $b$ is image of $a$ under $R$
1. $a$ is pre-image of $b$ under $R$

$R$ defined in $A$ means $R : A \to A$

### Number of Elements
If, $n(A) = m$ & $n(B)=n$
then, $n(A \times B) = m \cdot n$
Hence, Number of subsets of $A \times B = 2^{mn}$

Since $R$ is a subset of $A \times B$,
Therefore, Number of Possible Relations from $A \text{ to } B = 2^{mn}$


