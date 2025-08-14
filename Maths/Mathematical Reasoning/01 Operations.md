Links: [[00 Reasoning]]
___
# Operations
### Negation: NOT $(\sim{p})$
[[05 Logic Gates#NOT Gate]]
[[02 Operations on Sets#Compliment $(', bar{ phantom{ A }}, {} {C})$]]

| $p$ | $\sim{p}$ |
| --- | --------- |
| T   | F         |
| F   | T         |


### Conjunction: AND $(p \wedge q)$
[[05 Logic Gates#AND Gate]]
[[02 Operations on Sets#Intersection $( cap)$]]

It is when we use and, but, yet, through, still, moreover in sentence. We can replace all these with just "and".

| $p$ | $q$ | $p \wedge q$ |
| --- | --- | ------------ |
| T   | T   | T            |
| T   | F   | F            |
| F   | T   | F            |
| F   | F   | F            |

### Disjunction: OR $(p \vee q)$
[[05 Logic Gates#OR Gate]]
[[02 Operations on Sets#Union $( cup)$]]

| $p$ | $q$ | $p \vee q$ |
| --- | --- | ---------- |
| T   | T   | T          |
| T   | F   | T          |
| F   | T   | T          |
| F   | F   | F          |

#### Inclusive and Exclusive OR
When both the statements can be true simultaneously are inclusive OR. Here, both the statements cannot be false. 
e.g. I like tea or coffee.

At most one of the 2 statements can be true is Exclusive OR. Here none cannot be true one of them HAS to be true. 
e.g. 5 February 2023 is Wednesday or  Thursday. 

In maths, we use inclusive OR only. 

### Implications
#### Conditional
$$p \implies q$$
if p then q. 

p is called antecedent and q is called conclusion.

If p is true, then q must be true. If p is false, then it will say nothing about q and we treat this as true. This is just like the structure of a theorem in maths.

| $p$ | $q$ | $p \implies q$ |
| --- | --- | -------------- |
| T   | T   | T              |
| T   | F   | F              |
| F   | T   | T              |
| F   | F   | T              |

1. p is sufficient condition for q
2. q is necessary condition for p
3. $p \to q$ is not the same as $q \to p$
4. $p \implies q \equiv (\sim p) \vee q$ #important 
5. *If p then q* is also written as *p only if q* or *q follows from p*

![[Impication.png]]

#### Converse, Inverse and Contrapositive
Converse of $p \implies q$ is $q \implies p$ (this is region 1, 2, 4)

Inverse of $p \implies q$ is $\sim p \implies \sim q$ (this is region 1, 2, 4)

Contrapositive of $p \implies q$ is $\sim q \implies \sim p$ (this is region 2, 3, 4)

From this,
$$p \implies q \equiv\; \sim q \implies \sim p$$

#### Biconditional
$$p \iff q \equiv (p \to q) \wedge (q \to p)$$

which is the same as,
$$(\sim p \vee q) \wedge (\sim q \vee p)$$
which is the same as,
$$\sim (p \vee q) \wedge (p \wedge q)$$

This is true if both are true or both are false. 

| $p$ | $q$ | $p \iff q$ |
| --- | --- | ---------- |
| T   | T   | T          |
| T   | F   | F          |
| F   | T   | F          |
| F   | F   | T          |

1. $p \iff q \equiv q \iff p$

![[double implication.png]]


