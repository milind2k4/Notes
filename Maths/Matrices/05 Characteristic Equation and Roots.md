Links: [[00 Matrix]]
___
# Characteristic Equation and Characteristic Roots
A Matrix Polynomial Equation of degree n is, 
$$a_{n}A^{n} + a_{n-1}A^{n-1} + \dots a_{1}A + a_{o}I_{m} = O$$

Let A is an n square matrix, then,
$$A = [a_{ij}]_{n \times n}$$

Now consider the matrix, $A - \lambda I$, i.e.
$$a_{ii} - \lambda$$

$$A - \lambda I = \begin{bmatrix}
a_{11} - \lambda  & a_{12} & a_{13} & \dots  \\
a_{21} & a_{22} - \lambda  & a_{23} & \dots \\
a_{31} & a_{32} & a_{33}-\lambda & \dots  \\
\vdots
\end{bmatrix}$$

Then the equation $|A - \lambda I| = 0$ is called **Characteristic Equation** of matrix A and the polynomial, $|\lambda I - A|$ is called **Characteristic Polynomial** of matrix A.

CE of A (of order n) will be a polynomial equation of degree n.
$$a_{n}\lambda^{n} + a_{n-1}\lambda^{n-1} + \dots a_{o} = 0$$

For a 3 x 3 matrix,
$$\lambda^{3} + a_{1}\lambda^{2} + b_{1}\lambda + c_{1} = 0$$
let the roots are $\alpha, \beta, \upgamma$

Now,
$$
\begin{split}
|A - \lambda I| &= 0 \\
|(A - \lambda I)'| &= 0\\
|A' - \lambda I| &= 0
\end{split}
$$
Now, since the $\lambda$ here is unchanged, this equation is also satisfied by all the roots of the original. 

#### CE of Inverse
If we multiply by $|A^{-1}|$ both sides,
$$
\begin{split}
|A^{-1}||A - \lambda I| &= 0 \\
|A^{-1}A - \lambda A^{-1}| &= 0 \\
\left| \frac{ 1 }{ \lambda }I - A^{-1} \right| &= 0\\
\left| A^{-1} - \frac{ 1 }{ \lambda  }I \right| &= 0 \\
|A^{-1} - \mu I| &= 0
\end{split}
$$
Now this equation will have roots, $\displaystyle \frac{ 1 }{ \alpha }, \frac{ 1 }{ \beta }, \frac{ 1 }{ \upgamma }$.

Thus, if CE of A is,
$$\lambda^{3} + a_{1}\lambda^{2} + b_{1}\lambda + c_{1} = 0$$
Then the CE of $A^{-1}$ will be,
$$c_{1}\lambda^{3} + b_{1}\lambda^{2} + a_{1}\lambda + 1 = 0$$

#### CE of adj A
If we multiply by $|\text{adj }A|$,
$$
\begin{split}
|\text{adj }A||A - \lambda I| &= 0\\
|\text{adj }A - \lambda \text{adj }A| &= 0\\
||A|I_{n} - \lambda \text{adj }A| &= 0\\
\left| \text{adj }A - \frac{ |A| }{ \lambda } I_{n} \right| &= 0
\end{split}
$$
Now this equation will have roots, $\displaystyle \frac{ |A| }{ \alpha }, \frac{ |A| }{ \beta }, \frac{ |A| }{ \upgamma }$.

Thus, if CE of A is,
$$\lambda^{3} + a_{1}\lambda^{2} + b_{1}\lambda + c_{1} = 0$$
Then the CE of $\text{adj }A$ will be,
$$|A|^{3} + a_{1}|A|^{2}\lambda + b_{1}|A|\lambda^{2} + c_{1} \lambda^{3} = 0$$


### Cayley Hamilton Theorem (CHT)
Every square matrix will satisfy it's own characteristic equation. i.e. $\lambda$ is a solution of the Characteristic Equation.
$$a_{n}A^{n} + a_{n-1}A^{n-1} + \dots a_{1}A + a_{o}I_{n} = O$$



The values of $\lambda$ (i.e. $\ce{ \lambda 1, \lambda_{2}, \lambda_{3} \dots  }$ or *roots*) are  called **Eigen Values.**

1. Sum of Eigen values = $\displaystyle \sum_{i=1}^{n}\lambda_{i} = t_{r}(A)$
	Sum of roots of CE = $tr(A)$
	$$-a_{1} = tr(A)$$

1. Product of Eigen values = $\displaystyle \prod_{i=1}^{n}\lambda_{i} = \det A$
	Product of roots of CE = $|A|$
	$$(-1)^{n}a_{n} = |A|$$

Verification for a 3 x 3 matrix,
![[Pasted image 20230705073915.png]]
