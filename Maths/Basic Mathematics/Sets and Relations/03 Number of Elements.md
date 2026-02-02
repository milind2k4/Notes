Links: [[02 Operations on Sets]]
___
# Number of Elements
## For 2 sets
![[no of elements 2 sets.png]]

$$\begin{split}
n(A \cup B) & = a + b + c \\
n (A) & = a + b \\
n(B) & = b + c \\
n(A \cap B) & = b\\
&\\
\therefore n(A \cup B) & = n(A) + n(B) - n(A \cap B)
\end{split}$$

Number of elements exactly in one of the two sets,
$$n(A \Delta B) = n(A) + n(B) - 2n(A \cap B)$$

## For 3 sets

![[no of elements 3 sets.png]]

$$\begin{split}
n(A) & = a + b + g+f \\
n(B) & = c+b+g+d \\
n(C) & = e+f+g+d\\
n(A \cap B) & = b+g\\
n(B \cap C) & = d+g\\
n(C \cap A) & = f+g\\
n(A \cap B \cap C) & = g \\
n(A \cup B \cup C) & = a+b+c+d+e+f+g \\
\end{split}$$

$\therefore n(A \cup B \cup C) = n(A) + n(B) + n(C) - n(A \cap B) - n(B \cap C) - n(C \cap A) + n(A \cap B \cap C)$

$\therefore n(A \cup B \cup C) = \sum n(A) - \sum n(A \cap B) + n(A \cap B \cap C)$

For three, add the individuals, subtract the dual intersections and then finally add the triple intersection.

Number of elements exactly in individual sets,
$$n(\text{exactly in one set}) = \sum n(A) - 2\sum n(A \cap B) + 3n(A \cap B \cap C)$$

Number of elements in exactly 2 of the sets,
$$n(\text{exactly 2 sets}) = \sum n(A \cap B) - 3n(A \cap B \cap C)$$

## For any number of sets
$n(A \cup B \cup C \cup D\ \cup ....)$
$= \Sigma n(A) - \Sigma n(A \cap B) + \Sigma n(A \cap B \cap C) - \Sigma n(A \cap B \cap C \cap D) + \Sigma n(A \cap B \cap C \cap D \cap E) .$

Add odd subtract even.