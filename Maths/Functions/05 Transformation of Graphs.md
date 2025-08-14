Links: [[02 Elementary Graphs]]
___
# Transformation of Graphs
When we convert, $y = \sin^{-1}x \longrightarrow y = \sin^{1}|x|$ we are "Transforming" the graph of $\sin^{-1}x$.

### Some Notes
In general, $y = |f(x)|$ and $|y| = f(x)$ are not the same. 

On one equation we can apply multiple transformations. But in that case sequence of transformations matters.

If we are performing any transformation on x, in the expression, only replace x. Nothing else. Thus to get $-|x|$ we first do -ve then mod.
i.e. $x \to -x \to -|x|$

#### Multiple Transformations 
Sequencing is important. 

If multiple transformations are applied on x, or on y, then we will follow the thumb rule ***outside to inside.***

In case of $f(x)$, we apply transformations from ***inside to outside.***

In $y = x$, x is considered a variable not a function. Thus the transformations will be from outside to inside. 

### Replacing $x$ with $-x$
$$y = f(x) \longrightarrow y = f(-x)$$

Take reflection of the entire curve along y-axis. That is, flip the graph along y. 

![[e-x and ex.png]]

### Replacing $y$ with $-y$
$$y = f(x) \longrightarrow -y = f(x)$$

Take reflection of the entire curve along x-axis. That is, flip the graph along x. 

![[ex and -ex.png]]

### Replacing $x$ with $x-a$
$$y = f(x) \longrightarrow y = f(x-a)$$

Shift the entire curve parallel to x-axis $a$ units towards right if $a>0$ and towards left if $a<0$.
Remember this: since we subtracted something from x then x needs to be bigger to reach the same place. 

![[ln(x+3), ln(x) and ln(x-3).png]]

### Replacing $y$ with $y-a$
$$y = f(x) \longrightarrow y - a = f(x)$$

Shift the entire curve parallel to y-axis $a$ units up if $a>0$ and down if $a<0$.

![[ln(x)+3, ln(x) and ln(x)-3.png]]
(here $\ln(x) + 3$ is the $y - 3$ transformation and $\ln(x) - 3$ is the $y + 3$transformation)

### Replacing $x$ with $k \cdot x\ (k>0)$
$$y = f(x) \longrightarrow y = f(k \cdot x)$$

Divide all values on x-axis by $k$.

![[Pasted image 20230518180745.png]]

### Replacing $y$ with $k \cdot y\ (k>0)$
$$y = f(x) \longrightarrow k \cdot y = f(x)$$

Divide all values on y-axis by $k$.

![[Pasted image 20230518180916.png]]


### Replacing $x$ with $|x|$
$$y = f(x) \longrightarrow y = f(|x|)$$

First remove the portion of curve on LHS of y-axis. Then make graph on LHS as present on RHS. This works with any function.

![[e(mod(x)) and ex.png]]

![[sq(mod(x)) and sq(x).png]]

### Replacing $y$ with $|y|$
$$y = f(x) \longrightarrow |y| = f(x)$$

First remove the portion of curve below x-axis. Then make graph below x-axis as present above x-axis.

![[y = ex and mod(y) = ex.png]]
![[Pasted image 20230518191814.png]]

### Replacing $f(x)$ by $|f(x)|$
$$y = f(x) \longrightarrow y = |f(x)|$$

Put the portion of the curve below x-axis above it, by mirroring it.
This only works if function is of form $y = f(x)$ and has only y on LHS. 

![[mod(ln(x)) and ln(x).png]]
