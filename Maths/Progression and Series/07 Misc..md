Links: [[00 Sequence and Series]], [[01 Arithmetic Progression]], [[02 Geometric Progression]], [[03 Harmonic Progression]] 
___
# Miscellaneous Concepts

### Shortcut to find general term of a series
where kth order difference is in AP or GP


- **If the kth order difference is in AP** 

	![[Pasted image 20230616090833.png]]
	
	Then the nth term of the sequence can be written as,
	$$a_{n} = a_{1}+b_{1}(n-1) + c_{1} \frac{ (n-1))(n-2) }{ 2! } + d_{1} \frac{ (n-1)(n-2)(n-3) }{ 3! } + \dots$$
	
	And sum of first n terms,
	$$S_{n} = a_{1} + a_{2} + a_{3} + \dots + a_{n}$$
	$$S_{n} = a_{1}n + b_{1} \frac{ n(n-1) }{ 2! } + c_{1} \frac{ n(n-1)(n-2) }{ 3! } + d_{1} \frac{ n(n-1)(n-2)(n-3) }{ 4! } + \dots$$
	
	Example,
	![[Pasted image 20230616091458.png]]
	$\\$

- **If the kth order difference is in GP**
  
	![[Pasted image 20230616092642.png]]
   
  then  the general terms  will be,
	$$a_{n} = (k-1)^{th} \text{ order poynomial of n} + \alpha r^{n}$$

	We will have to find all the coefficients of the polynomial and $\alpha$. 
	
	Example,
	![[Pasted image 20230616093041.png]]
	($c. 5^{n-1}$ is written to reduce calculations and the value of c will change accordingly)
	![[Pasted image 20230616093954.png]]

### Questions

##### Sum of n terms of 2 APs are in the ratio, $x(n):y(n)$, find the ratio of their $r$th term. 
> Assume, 
> $$\begin{split}
> AP_{1} &= (a,d,n)  \\
> AP_{2} &= (A,D,n)\\
> \end{split}$$
> 
> Find the ratios of their nth terms, 
> $$\begin{split}
> \frac{ ( S_{n} ) _{1} }{ ( S_{n} ) _{2} } &= \frac{ \frac{n}{2} (2a+(n-1) d ) }{ \frac{n}{2} (2A + (n-1) D ) } = \frac{ x(n) }{ y(n) }\\
>  &= \frac{ a + \left(  \frac{n - 1}{2} \right) d }{ A + \left(  \frac{n - 1}{2} \right) D } 
> \end{split}$$
> 
> Find the ratios of their nth term, 
> 
> $$\begin{split}
> \frac{ ( T_{r} ) _{1} }{ ( T_{r} ) _{2} } &= \frac{ a + (r-1) d }{ A + (r-1) D }
> \end{split}$$
> 
> Equate, 
> $$\begin{split}
> \frac{n-1}{2} &= r- 1
> \end{split}$$
> 
> Find the value of $n$ and put in in $\displaystyle \frac{x(n)}{y(n)}$.

### Misc. Examples
![[Pasted image 20230615093840.png]]

In questions where the general term is not clear, we use something like AGP to find the general term. If in this too we cannot identify the general term, we use the method again. 
![[Pasted image 20230615094702.png]]

Sometimes it could also be that the sum does not match with the general term from the first but the 2nd or 3rd term. In this case, we sum the terms we can using the general term, and then add the remaining terms separately. 

In case the question asks for product, there will be some kind of chain reaction,
![[Pasted image 20230615095954.png]]

