Links: [[01 Operations]], [[03 Algebra of Operations]]
___
# Mathematical Reasoning
We communicate our ideas through sentences. 
There are types of sentences:
- **Assertive or Declarative** e.g. Earth is round.
- **Imperative** (command/request)  e.g. Bring me a glass of water.
- **Interrogative** e.g. What the dawg doin?
- **Exclamatory** e.g. Wow! What a beautiful day.

### Statement or Mathematical Statement 
Sentences which are either true or false. There should be no ambiguousness. They have a truth value. 

True statements are called Valid Statement. 
False statements are called Invalid Statement.

Open statement is a sentence which can be true or false depending upon some conditions which are not given in the sentence. They are not considered mathematical.

$x + 7 = 9$ is an open statement as it is true for $x = 2$ but false otherwise. 

#### Compound Statement 
Multiple statements joined using connectives (or logical connectives) (like "and", "or" etc).

##### Tautology (t)
If a statement is always true, i.e. its truth value is true for all combinations of truth values of component statements. 

Always true.

##### Fallacy (c)
(aka contradiction) 

Always false.

##### Contingency 
If statement pattern takes both values, i.e. true as well as false.

#### Logical Connectives 

| Connective     | Sign          | Term               | 
| -------------- | ------------- | ------------------ |
| and            | $\vee$        | disjunction        |
| or             | $\wedge$      | conjunction        |
| not            | $\sim (\neg)$ | negation           |
| if __ then     | $\implies$    | implication        |
| if and only if | $\iff$        | double implication |

Except not, all other are binary. Not is unary.

### Truth Table
Truth table for a compound statement is the listing for its truth value and the different possible combinations of truth values of component statements. 

If a statement has p component statements and q connectives, then its truth table will have $2^{p}$ rows and $(p+q)$ columns. 

For one statement, 2 rows

| p   |
| --- |
| T   |
| F   |


For two statements, 4 rows

| p   | q   |
| --- | --- |
| T   | T   |
| T   | F   |
| F   | T   |
| F   | F   |

For 3 statements, 8 rows,

| p   | q   | r   |
| --- | --- | --- |
| T   | T   | T   |
| T   | T   | F   |
| T   | F   | T   |
| T   | F   | F   |
| F   | T   | T   |
| F   | T   | F   |
| F   | F   | T   |
| F   | F   | F   |

Instead of making truth table, we can more easily do question using set theory. 

![[Pasted image 20230916151535.png]]

### Logically Equivalent Statements
Statements having same truth table. 
e.g. $\sim (\sim p) \equiv p$

We can also use [[02 Operations on Sets|Venn diagrams]]. 
Replacing $\vee \to \cup,\ \wedge \to \cap,\ \sim\; \to\ \overline{}$
But this only works when only these three are used. 


### Set theoretical Notion
Inside the circle p has truth value T and outside it has F. 

Using this, we can see that inclusive OR is simply OR operator. Exclusive OR is NOR operator. 

### Quantifier and Quantifies Statements 
$\exists$ is **"There Exists"** and it is called *existential quantifier.*
$\forall$ is **"For All"** and it is called *universal quantifier.*

If an open statement is used with a quantifier then it becomes a mathematical statement. 

![[Pasted image 20230916153439.png]]

### Negation of a Statement 


For Negation of a quantified statement replace,
1. Negation of "There Exists" is "For All"
3. Negation of "For All" is "There Exist".

While negating open statements, we negate all the components of the statement. 
![[Pasted image 20230916152851.png]]

For negation of simple statements, use "not".

For compound statement replace $p$ with $\sim p$ etc and $\vee$ with $\wedge$ and $\wedge$ with $\vee$. For statements written in English, first convert it into symbolic form, negate that and then finally convert it back into English. 

Just like De Morgan's Law. 

### Use of Venn Diagram in Logic 
An argument is an assertion that statement $S$ follows from other statements $S_{1},S_{2},S_{3}\dots S_{n}$. Here $S_{i}$ are called *hypothesis* or *premise* and $S$ is called *conclusion.*

![[Pasted image 20230916153017.png]]
![[Pasted image 20230916153000.png]]

## Examples
![[Pasted image 20230916153256.png]]

Negation does not necessarily mean that we write the opposite of the adjective. 
![[Pasted image 20230916152732.png]]

![[Pasted image 20230916152941.png]]

![[Pasted image 20230916153347.png]]




