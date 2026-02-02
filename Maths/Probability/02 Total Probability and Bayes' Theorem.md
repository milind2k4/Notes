Links: [[00 Probability]], [[01 Set Theory]]
___
# Total Probability Theorem (TPT)

Let $E_{1},E_{2},E_{3} \dots E_{n}$ are mutually exclusive and set of exhaustive events. An event E is defined on the same sample space then,
$$
\begin{split}
P(E) &= P(E \cap E_{1}) + P(E \cap E_{2}) + P(E \cap E_{3}) + \dots P(E \cap E_{n}) \\
&= \sum_{r = 1}^{n} P(E \cap E_{r})
\end{split}
$$

Using conditional probability,
$$P(E|E_{r}) = \frac{ P(E \cap E_{r}) }{ P(E_{r}) }$$
Thus,
$$P(E) = \sum_{r=1}^{n} P(E_{r}) . P(E|E_{r})$$

![[Pasted image 20231225112618.png]]


This is used to find the probability of an event which can occur through multiple paths and each path has some probability of the event occurring. 

Here, $P(E_{r})$ is the probability of the path and $P(E|E_{r})$ the probability of the event if path $E_{r}$ is chosen. 

#### Examples 
![[Pasted image 20231225113451.png]]
![[Pasted image 20231225113603.png]]
![[Pasted image 20231225113931.png]]

## Bayes' Theorem
[[01 Set Theory#Conditional Probability]]

If $E_{1},E_{2},E_{3}\dots E_{n}$ are n mutually exclusive and set of exhaustive events, and an event E is also defined on the same sample space, then if it is given that event E has occurred, then the probability that event $E_{k}$ has also occurred,

$$
\begin{split}
P(E_{k}|E) &= \frac{ P(E \cap E_{k}) }{ P(E) } \\
\\
&= \frac{ P(E_{k}). P(E|E_{k}) }{ P(E) } \\
P(\text{path}) &= \frac{ \text{contribution of path } E_{k} }{ \text{total probability of event} }
\end{split}
$$

(contribution of path means probability of path multiplied by the probability of event occurring through that path, i.e. $P(E_{r}). P(E|E_{{r}})$)

It tells us the probability of the path, given event E has occurred.

#### Examples 
First we treat a question of Bayes theorem like that of TPT and find the probability of the event occurring itself. 

![[Pasted image 20231225120204.png]]

![[Pasted image 20231225120847.png]]

![[Pasted image 20231225121336.png]]

## Revised Probability 
When an event E has occurred and we re do it (say E'), after telling the outcome of previous event E.

We can use the analogy,
$$\text{Past : Present : Future :: Bayes Theorem : TPT : Revised}$$

In this case we will find the probability of each path using Bayes theorem. These probabilities will become the new probabilities of the paths. 

![[Pasted image 20231225122726.png]]
![[Pasted image 20231225122733.png]]

![[Pasted image 20231225123607.png]]
![[Pasted image 20231225123618.png]]

