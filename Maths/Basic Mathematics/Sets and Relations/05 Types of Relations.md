Links: [[04 Relations]]
___
# Types of Relations
$R$ defined from $A$ to $A$ means $R : A \to A$

#### Universal
A relation which is equal to $A \times A$.

$$R = A \times A$$

#### Void
A relation which has no elements. 

$$R = \phi$$

#### Identity
A relation which has all possible elements of the type $(a,a)$ and has no other elements. 

i.e. 
$$
\begin{split}
R(a) &= a \\
R &= \{ (x,y) : x = y \} \\
n(R) &= n(A) 
\end{split}
$$

#### Inverse
If $R:A\to B$
then, the inverse relation of $R$ is denoted as $R^{-1}$ and is defined $R^{-1}:B \to A$ as:

$$R^{-1} = \{ (b,a) : \forall (a,b) \in R \}$$

#### Reflexive
If it contains all elements $(a,a)$ for all $a \in D_{R}$
i.e. 
$$(a,a) \in R\ \forall\ a \in A$$

Every identity relation is a reflexive relation, but every reflexive relation is not an identity relation. 

In reflexive, $(a,b)$ can also be present, but in identity it cannot. 

#### Symmetric
if $(a,b) \in R \implies (b,a) \in R\ \forall\ (a,b) \in R$
i.e. 
$$a\ R\ b \implies b\ R\ a$$


#### Transitive
if $(a,b) \in R,\ (b,c) \in R \implies (a,c)\in R.$
i.e. 
$$a\ R\ b \text{ \& } b\ R\ c \implies a\ R\ c$$

$$\begin{split}
(a, b) & \in R \\
(b, c) & \in R\\
\hline 
(a,c) & \in R
\end{split}$$

While checking transitive, we also have to check the condition that c = a.
For example, this relation is not transitive because $\alpha$ cannot be the bother of $\alpha$.
![[Pasted image 20230526084927.png]]

#### Equivalence
if $R$ is Reflexive, Symmetric and Transitive.

#### Anti-Symmetric
If $(a,b) \in R\ \&\ (b,a) \in R$ then $a = b$. 

If $(a,b) \in R$ and a and b are distinct, then $(b,a)$ must not be present in the relation. 

