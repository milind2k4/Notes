Links: [[00 Matrix]]
___
# Algebra of Matrices
If A and B have same order then they are comparable matrix. 

### Equality of Matrices
If their order are same and their corresponding elements are equal.

If two matrices are cannot be equal, then there is no sense in saying the value of a variable. 

For example, in this question, there is no sense in saying that the value of z is -1. If matrices cannot be equal, every relation involving variables are void. 
![[Pasted image 20230624083421.png]]


### Addition
Defined if both the matrices have the same order. 
Matrices which can be added are called *conformable for addition*.

Sum the corresponding elements if addition is defined. 

- **Properties of addition:**
	- Commutative
	- Associative
	- A matrix is called the additive inverse of another if their sum is null matrix. $A+(-A) = O$
	- $A + O = O + A = A$
	- $|A + B| \neq |A| + |B|$, in general
	- $tr(A+B)= tr(A) + tr(B)$

### Scalar Multiplication
if $A = [a_{ij}]$
then, $kA = [ka_{ij}]$

Each element is multiplied. And thus if we take common from a matrix, it will be taken common from all elements. 

- **Properties of multiplication:**
	- $|kA| = k^{n}|A|$, if $A$ is a sq. matrix of order $n$. 
	- $\lambda(A+B) = \lambda A + \lambda B$
	- $(\lambda_{1} + \lambda_{2})A = \lambda_{1} A + \lambda_{2} A$
	- $tr(kA) = k.tr(A)$

### Matrix Multiplication
If $A$ is of the order $m \times n$ and $B$ is of the order $p \times q$, then,
- The number of rows of one should be equal to the number of columns of the other. 
  $\\$

- for $AB$ to be defined $n=p$, and the order of $AB$ will be $m \times p$
  ($m \times \boxed{n\;\; p} \times q \implies m \times q$)

- for $BA$ to be defined $m=q$, and the order of $AB$ will be $p \times n$
  ($p \times \boxed{q\;\; m} \times n \implies p \times n$)

- if both $AB$ and $BA$ are defined, the order of $A$ is $m \times n$ and of $B$ is $n \times m$. And, $AB \to m \times m$, $BA \to n \times n$
  $\\$

- For $A^k$ to be defined, $A$ has to be a square matrix. 

The $(i,j)^{th}$ element of $AB$ is obtained by taking $i^{th}$ row from $A$, $j^{th}$ column from $B$, multiplying corresponding elements and summing them. (i.e. multiply row by column)

$$A \times B = C$$
$$
\begin{bmatrix} 
 {a_1}& {a_2} \\ 
 \underline{b_1}& \underline{b_2} \\ 
 {c_1}& {c_2} \\ 
\end{bmatrix}_{3 \times 2}
\times 
\begin{bmatrix} 
 \alpha_{1} & \alpha_{2} & \underline\alpha_{3} \\
 \beta_{1} & \beta_{2} & \underline\beta_{3} \\
\end{bmatrix}_{2 \times 3}
= 
\begin{bmatrix}  
 ... & ... & ... \\
 ... & ... & \boxed{\phantom{A}} \\
 ... & ... & ... \\
\end{bmatrix}_{3 \times 3}
$$

$$\boxed{\phantom{A}} = b_{1} \cdot \alpha_{3} + b_{2} \cdot \beta_{3}$$
$$c_{23} = a_{21} \cdot b_{13} + a_{22} \cdot b_{23}$$

$$2 \implies \text{row 2 from A}$$
$$3 \implies \text{column 3 from B}$$

The product can be written as:

$$c_{ij} = \sum\limits_{k=1}^{n}a_{ik}b_{kj}$$


#### [[01.5 Properties of MM and Some PTR]]

### Inverse of a Matrix
aka **Reciprocal of Matrix**
If A is a square matrix of order n, then Inverse of A is a matrix, which when multiplied with A, gives $I$. 
i.e. if $AB = I = BA$ then $B$ is  said to be the inverse of $A$, and denoted as $A^{-1}$.

$A^{-1}$ exists only if $A$ is non-singular. i.e. $|A| \neq 0$.

##### $\det$ of Inverse 
If A is non-singular,
$$
\begin{split}
AA^{-1} &= I \\
|A A^{-1}| &= |I| \\
|A||A^{-1}| &= 1\\
|A^{-1}| &= \frac{ 1 }{ |A| }
\end{split}
$$
#### Pre-cancellation Law
If $A$ is non-singular, then $AB = AC \implies B = C$ (pre-multiply by $A^{-1}$)

  - **Proof:**
> $$\begin{split}
> AB & = AC \\
> A-B & = O\\
> A(B-C) & = O\\
> \centernot\implies A = O& \text{ or } (B-C) = O\\
> \end{split}
> $$
> 
> Thus we cannot use this method.
> We can use:
> $$\begin{split}
> AB & = AC\\
> (A^{-1}A)B & = (A^{-1}A)C \\
> & \text{ (since A is non-singular)}\\
> IB & = IC \\
> B & = C
> \end{split}
> $$
> Which gives the desired result.

#### Post-cancellation Law
If $A$ is non-singular, then $BA = CA \implies B = C$ (post-multiply by $A^{-1}$)

**Note:**
- $BA = AC \centernot\implies B = C$
  - Except when either A and C or A and B commute.
