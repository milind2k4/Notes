Links: [[00 Determinants]]
___
# Matrix
Rectangular array of of $mn$ elements placed in $m$ horizontal rows, and $n$ vertical columns.

$m \times n$ is the order of the matrix. (first one is row, second one is column)

Matrix is not a single value and can be rectangular, unlike [[00 Determinants]]

Usually Matrix is denoted by capital letter and its elements by small letters. 
Matrix $A$ of order $m \times n$ can be represented as:

$$A = [a_{ij}]_{m \times n}$$
$$i \in (1, m)\ \&\ j \in (1,n) $$
$$\text{where,}\ i,j \in N$$

## Types of Matrices
1. **Row matrix** if order $= 1 \times n$, i.e. it has only one row.

1. **Column matrix** if order $= m \times 1$, i.e. it has only one column. 

1. **Horizontal matrix** if order $= m \times n$ where $m < n$

1. **Vertical matrix** if order $= m \times n$ where $m > n$

1. **Zero matrix** if all entries are 0. Denoted by 'O' or **0**

1. **Square matrix** if order $= n \times n$. We find determinants for these matrices. 
	- The elements $a_{ii}$ form a *diagonal.*
	  Some institutes defined $a_{ii}$ as diagonal elements irrespective of matrix being square or not.  
	- **Trace of Matrix:** The sum of all diagonal elements.
	  $$i.e.\; tr(A) = \sum_{i=1}^{n}a_{ii}$$
	- **Conjugate:** Elements symmetric about diagonal. $a_{ij}$ and $a_{ji}$ are conjugate elements.
	- For a square matrix A, the value of its corresponding determinant is called its determinant value and is denoted as $\det A\ or\ |A|$. 

##### Singular and Non-Singular 
If $A$ is a square matrix, then $A$ is:
- **Singular** if $\det A = 0$
- **Non-Singular** if $\det A \neq 0$

### Types of Square Matrix
($n$ is the order of matrix)

1. **Scalar matrix** where, $[a_{ij}] = 0$ and $a_{ii} = k$, i.e. all diagonal elements are equal. 

1. **Identity/Unit matrix** where, $[a_{ij}] = 0$ and $a_{ii} = 1$, i.e. all diagonal entries are one. Also, $tr(I_{n}) = n$

1. **Upper Triangle matrix** where all entries below diagonal are 0. i.e. $[a_{ij}] = 0,\ i>j$
   
	Min. number of zeros: $\displaystyle \frac{n^{2}-n}{2}$
	$n^{2}$ is total number of elements, $n$ is the number of elements in diagonal, $n^{2} - n$ is the number of elements which are not diagonal, the half of this must be zero. 
	
	Max. number of distinct elements: $\displaystyle \frac{n^{2}+n}{2}+1$
	$$\begin{bmatrix}
	a & b & c \\
	0 & d & e  \\
	0 & 0 & f
	\end{bmatrix}$$

1. **Lower Triangle matrix** where all entries above diagonal are 0. i.e. $[a_{ij}] = 0,\ i<j$
	Min. number of zeros: $\displaystyle \frac{n^{2}-n}{2}$
	
	Max. number of distinct elements: $\displaystyle \frac{n^{2}+n}{2}+1$
	$$\begin{bmatrix}
	a & 0 & 0 \\
	b & c & 0 \\
	d & e & f
	\end{bmatrix}$$

#### Diagonal Matrices
Where, $[a_{ij}] = 0$, i.e. only diagonal elements. 
- Min. number of zeros = $n^{2}-n$
- Max. number of distinct entries: $n+1$ ($n$ diagonal elements + $1$ because of zero)
- It is also represented by $A = diag(a_{1},b_{1},c_{1})$. The number of entries in this is the order.
- Diagonal matrix are both UTM and LTM.

To multiply two diagonal matrices, we simply multiply the corresponding elements.
$$A = diag(a_{1},a_{2},a_{3}\dots)$$

To take determinant, we just multiply the diagonal elements,
$$|A| = a_{1}.a_{2}.a_{3}.\dots$$

To take a power, we raise each term to that power,
$$A^{k} = diag(a_{1}^{k},a_{2}^{k},a_{3}^{k}\dots)$$

To take inverse, we reciprocate each element,
$$A^{-1} = diag\left( \frac{ 1 }{ a_{1} }, \frac{ 1 }{ a_{2} }, \frac{ 1 }{ a_{3} } \dots \right)$$

### Some Special Types of Square Matrices
Let A is a square matrix of order n, then, it is called,
1. **Idempotent** if $A^{2} = A$. ("idem" in idempotent is for *Identity*)
	- From this, $A^{k} = A$
	- $|A|^{2} = |A| \implies |A| = 0$
	- If $|A| = 1$ and A is idempotent, then $A = I$. 
	  Thus an idempotent matrix which is non-singular, it has to be identity. 
	  $\\$

2. **Involutory** if $A^{2} = I_{n}$ (remember that in INvolutory, there is $I_{n}$)
	- Using this we get, $A^{2n} = I$ and $A^{2n+1} = A$. I.e. the odd powers are A and the even are I.
	- $|A|^{2} = 1 \implies |A| = -1\ or\ 1$. 
	  Thus an involutory matrix will always be invertible. 
	- $A^{-1} = A$. Thus if A is involutory, then it will be its own inverse. 
	  $\\$
3. **Nilpotent** if $A^{k} = O$ for some k. 
	- The least such value of k is called *Index.* Thus if m is index, then $A^{m} = O$ and $A^{m-1} \neq O$.
	- If $A^{m} = O$ then $A^{k} = O$ for all $k > m$. 
	- $A^{m} =O \implies |A| = 0$.
	  Thus if $|A| \neq 0$ then the matrix cannot be nilpotent. 
	  $\\$
4. **Periodic** if $A^{\lambda+1} = A$. The least possible value of $\lambda$ is called its Period. 
	- Null Matrix is periodic with period undefined. 

## Examples
Questions of matrices are questions of [[00 Permutation and Combination]] most of the time. 
![[Pasted image 20230624083823.png]]
![[Pasted image 20230624083902.png]]

![[Pasted image 20230628090922.png]]

![[Pasted image 20230628090933.png]]

![[Pasted image 20230628091619.png]]

![[Pasted image 20230628092510.png]]

![[Pasted image 20230628092804.png]]

Here we use, [[02 Formula and Expansions#Factorization of Difference]]
![[Pasted image 20230628093039.png]]

![[Pasted image 20230701095156.png]]

In questions where we have to find the max value of determinant, we have to prove that the value is possible,
![[Pasted image 20230701095807.png]]
![[Pasted image 20230701095817.png]]

In some questions, brute force is the only way,
![[Pasted image 20230701100021.png]]





