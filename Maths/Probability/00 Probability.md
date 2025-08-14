Links: [[00 Permutation and Combination]], [[01 Set Theory]]
___
# Probability
Mathematical calculation of chance of occurrence of an event E is called its probability and it is denoted as $P(E)$.

$P(E)$ is a real number between $[0,1]$

If $P(E) = 0$ then it is called *Impossible* and if $P(E) = 1$ then it is called *sure* event. 

If an experiment is conducted, then all possible outcomes are called *Sample Points* and the collection of all sample points is called *Sample Space.*

![[Pasted image 20231217105620.png]]

A collection of sample points is called an *Event.* It is a subset of sample space. 

##### Types of Events
Two outcomes or events are called **Equi-probable or Equally-likely** if their chance of occurrence is the same.

Two events are called **Disjoint or Incompatible or Mutually Exclusive (ME)** if they cannot occur simultaneously. 

Two events are called **Independent** if occurrence or non occurrence of one does not affect the chance of occurrence of the other. 

A set of events is called **Exhaustive (SOEE)** if their union is sample space, i.e. SOEE will cover all sample points. 
(SOEE = Set of Exhaustive Events)

![[Pasted image 20231217110837.png]]

#### Classical Definition of Probability 
If an experiment can result in total $p + q$ equally likely outcomes out of which exactly $p$ favours the occurrence of event $E$, then, probability of occurrence of $E$,
$$P(E) = \frac{ p }{ p+q } = \frac{ \text{no. of favourable outcomes} }{ \text{total no. of outcomes} }$$

**Some things to note,**
1. To apply above formula, all the outcomes must be equally likely. 
2. *Odds in favour of E* are defined as $p:q$ 
3. *Odds against event E* are defined as $q:p$


The probability is calculation of frequency of occurrence of an event if experiment is performed a large number of times.

Even same objects are treated differently in probability because they are *distinct* objects.

## Independent Events 
Event A is called independent of event B if occurrence or non occurrence of B does not change the probability of occurrence of A.

I.e. if A is independent of B then,
$$P(A|B) = P(A)$$

That is,
$$
\begin{split}
\frac{ P(A \cap B) }{ P(B) } &= P(A) \\
P(A \cap B) &= P(A). P(B)
\end{split}
$$
This is the condition to check whether two events are independent or not. 

Since this result is symmetric in A and B, if A is independent of B, B is also independent of A.

If A is independent of B, events C and D will also be independent of each other where C = A or $\bar{A}$ and D = B or $\bar{B}$.

$$P(A \cap \bar{B}) = P(A) . P(\bar{B})$$
$$P(\bar{A} \cap \bar{B}) = P(\bar{A}) . P(\bar{B})$$

Now,
$$
\begin{split}
P(A \cup B) &= P(A) + P(B) - P(A \cap B) \\
&= P(A) + P(B) - P(A). P(B)
\end{split}
$$

If three events A, B, C are independent then the required set of conditions are,
$$
\begin{split}
P(A \cap B) &= P(A). P(B) \\
P(B \cap C) &= P(B). P(C) \\
P(C \cap A) &= P(C). P(A) \\
P(A \cap B \cap C) &= P(A).P(B).P(C)
\end{split}
$$

In general, for n events to be independent, the no. of conditions which must be met will be,
$${}^{n}C_{2} + {}^{n}C_{3} + {}^{n}C_{4} + \dots {}^{n}C_{n} = 2^{n} - {}^{n}C_{0} - {}^{n}C_{1}$$
That is,
$$= 2^{n} - 1 - n$$

If we cannot tell at a glance, we will have to satisfy these conditions,
![[Pasted image 20231221171114.png]]

## Addition and Multiplication Rule 
If events A and B are mutually exclusive, then,
$$P(A \cup B) = P(A) + P(B)$$

If an experiment is performed, then the probability of simultaneous occurrence of A and B,
$$P(A \cap B) = P(A). P(B|A)$$
i.e. probability of first event times probability of 2nd event assuming first has occurred. 

If A and B are independent,
$$P(A \cap B) = P(A).P(B)$$

![[Pasted image 20231221172146.png]]

If an experiment is performed, then the probability that events A and B and C and D etc. occurs,
$$P(A \cap B \cap C \cap D \dots) = P(A) . P(B|A) . P(C|A \cap B) .  P(D|A \cap B \cap C) \dots$$
And if they are independent,
$$P(A \cap B \cap C \cap D \dots) = P(A).P(B).P(C).P(D)\dots$$

## Truth of the Statement 
aka **Coincidence Testimony**

They are basically questions of Bayes' Theorem. 

If A and B speak truth with probability $p$ and $q$ respectively, then if,
1. Both agree on a statement then the probability that statement is actually true is,
	$$P(SIT|BSS) = \frac{ p.q }{ p.q + (1-p)(1-q) }$$
	
	![[Pasted image 20231226204932.png]]
	
	The more probability they have of saying the truth, the closer this ratio is to 1.
	![[Pasted image 20231226205238.png]]
	P(Tony Ate Burger | Both Said So)
	$\\$

2. Both say that event E occurred and we know that probability of occurrence of E is $\alpha$, then the probability that event E has actually occurred will be,
	$$P(E|BSS) = \frac{ \alpha p q }{ \alpha pq + (1-\alpha)(1-p)(1-q) }$$
	
	![[Pasted image 20231226205956.png]]
	
	![[Pasted image 20231226210346.png]]
	![[Pasted image 20231226210357.png]]
	$\\$

3. If in case 2, the probability that their lies coincides $\beta$ (i.e. there are multiple ways of saying a lie) is then, then the probability that event E actually occurred, given both said so,
	$$P(E|BSS) = \frac{ \alpha pq }{ \alpha pq + (1-\alpha)(1-p)(1-q).\beta }$$
	
	![[Pasted image 20231226211638.png]]
	![[Pasted image 20231226212108.png]]


## [[04 Probability Dist. and Expected Value]]