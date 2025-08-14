Links: [[00 Probability]]
___
# Set Theory in Probability 

### For 2 Events 
![[Pasted image 20231221110917.png]]

$$
\begin{split}
1 + 2 &\to \text{A} \\
2 + 3 &\to \text{B} \\
2 &\to A \cap B \equiv \text{A and B} \\
1 &\to A \cap \bar{B} \equiv A - (A \cap B) \equiv \text{A but not B} \\
3 &\to \bar{A} \cap B \\
3 + 4 &\to \bar{A} \equiv \text{not A} \\
1 + 2 + 3 &\to A \cup B \equiv \text{at least one out of A or B} \\ 
4 &\to \bar{A} \cap \bar{B} \equiv \text{neither A nor B} \\
\end{split}
$$


Also, note that "exactly one of A or B" and "A or B" are different as in maths, "or" is inclusive. 

##### Formula 
Using to no. of elements formula, 
$$
\begin{split}
n(A \cup B) &= n(A) + n(B) - n(A \cap B) \\
\\
\frac{ n(A \cup B) }{ n(S) } &=\frac{ n(A) + n(B) - n(A \cap B) }{ n(S) } 
\end{split}
$$
Thus giving us,
$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$

Thus we can find any probability. 

$$
\begin{split}
P(\text{exactly one of A or B}) &= P(1 + 3) \\
&= P(A) + P(B) - 2P(A \cap B)\\
\\
P(\text{atmost one of A or B}) &= P(1 + 3 + 4) \\
&= 1 - P(2) \\
&= 1 - P(A \cap B) \\
\\
P(A \cup \bar{B}) &= P(1 + 2 + 4) \\
&= 1 - P(3) \\
&= 1 - P(\bar{A} \cap B) \\
&= P(A) + P(\bar{A} \cap \bar{B})  
\end{split}
$$

![[Pasted image 20231221112945.png]]

If A and B are mutually exclusive, then,
$$P(A \cap B) = 0$$
Thus we can write,
$$P(A \cup B) = P(A) + P(B)$$

![[Pasted image 20231221113014.png]]

For example,
![[Pasted image 20231221115211.png]]

#### Range of Probability  
#####  Union
In case of Disjoint Events, 
$$P(A \cup B) = P(A) + P(B)$$
In case of non disjoint Events, 
$$P(A \cup B) = [P(A) + P(B),1]$$
In case of subsets, 
$$P(A \cup B) = max\{ P(A),P(B) \}$$

Thus,
$$max\{ P(A),P(B) \} \leq P(A \cup B) \leq min\{ P(A)+P(B),1 \}$$

The first equality will hold when one of the events is subset of the other. 
The second equality will hold when events are either mutually exclusive or exhaustive. 

![[Pasted image 20231221180621.png]]
##### Intersection
In case of Disjoint Events, 
$$P(A \cap B) = 0$$
In case of non disjoint Events, 
$$P(A \cap B) \in (0,1)$$
In case of subsets, 
$$P(A \cap B) = min\{ P(A),P(B) \}$$

Thus, 
$$max\{ P(A) + P(B)-1,0 \} \leq P(A \cap B) \leq min\{ P(A),P(B) \}$$

The equalities will reverse as that of union.

### For 3 Events 
![[Pasted image 20231221113839.png]]

Similar to two events, we will think in terms of regions. 

$$
\begin{split}
P(\text{atleast one of A, B, C}) &= P(A + B + C) \\
&= P(A \cup B \cup C) \\
&= P(1 + 2 + 3 + 4 + 5 + 6 + 7) \\
\\
&= \sum P(A) - \sum P(A \cap B) + P(A \cap B \cap C) \\
&= 1 - P(\bar{A} \cap \bar{B} \cap \bar{C})
\end{split}
$$

![[Pasted image 20231221114544.png]]

## Conditional Probability
$P(A|B)$ is read as *Probability of A given B* and is the probability of event A given B has occurred. 

The occurrence of B has reduced the sample space. 

We need to find the probability of landing in $A \cap B$ provided we already landed in B.
![[Pasted image 20231221161440.png]]

Thus we get,
$$
\begin{split}
P(A|B) &= \frac{ n(A \cap B) }{ n(B) } \\
&= \frac{ \frac{ n(A \cap B) }{ n(S) } }{ \frac{ n(B) }{ n(S) } } \\
&= \frac{ P(A \cap B) }{ P(B) }
\end{split}
$$

$P(A|B)$ is also written as $P(A /B)$.

And $P(A /B) \neq P(A\setminus B)$. 
$$P(A \setminus B) = P(1) = P(A - B)$$
$A \setminus B$ means "A and not B"

If A and B are mutually exclusive, then if B happens, A cannot happen and thus,
$$P(A|B) = P(B|A) = 0$$

If B is a subset of A,
$$P(A|B) = 1$$
$$P(B|A) = \frac{ P(B) }{ P(A) }$$

![[Pasted image 20231221162709.png]]

And, for compliment,
$$P(A|B) + P(\bar{A}|B) = 1$$

![[Pasted image 20231221163213.png]]

![[Pasted image 20231221163910.png]]