Links: [[02 Selection]], [[04 Grouping]]
___
# Distribution
No. of ways of distributing n different objects among n persons giving one object to each is $n!$. 

This is done by first fixing persons and then permuting objects in front of them. 

No of ways of distributing n identical objects among r persons $= {}^{n+r-1}C_{r-1} = \displaystyle {n+r-1 \choose r-1}$

![[Pasted image 20231212094904.png]]

If we are distributing r identical objects among n persons and $r> n$, giving each person at least one object and distributing all objects, then we can do it in rounds as here the order will not matter. 
Thus we distribute n objects and then distribute r-n objects, = $1. {}^{n-r+r-1}C_{r-1} = {}^{n-1}C_{r-1}$.

#### n distribution to r persons 
No. of ways of distributing n different objects to r persons such that,
1. All objects are distributed and a person may get any number of objects = $r.r.r\dots r = r ^{n} = \text{(persons)}^{\text{(objects)}}$ 
   
   We will pick each object, and each object will have r persons to pick from, thus $r ^{n}$. 
	$\\$

1. All objects are distributed and no one should get more than one object, given $r \geq n$, = ${}^{r}C_{n} . n!$
   
   First we will select n persons of r persons and then permute the r objects in front of them. Or we can do this with fundamental principle of counting. 
	$\\$ 

3. All objects are distributed and each persons should get at least one object, given $n > r$, will be,
   $$= r ^{n} - {}^{r}C_{1} (r-1)^{n} + {}^{r}C_{2}(r-2)^{n} - {}^{r}C_{3} (r-3)^{n} + \dots $$

	We first freely distribute the objects, then we remove the cases where one of the r persons did not get any object, from this we remove the cases where one of r-1 persons did not get any object, from this we remove the case where one of r-2 persons did not get any object and so on. 
	
	The formula actually looks like,
	$$N = r ^{n} - [{}^{r}C_{1} (r-1)^{n} - [{}^{r}C_{2}(r-2)^{n} - [{}^{r}C_{3} (r-3)^{n} - \dots ]]]$$
	
	Here we cannot do ${}^{n}C_{r} . r! . r ^{n-r}$. Because there is overcounting due to order. 
	$\\$

4. At least one object is distributed while a person may get any number of objects, 
	$$= \text{exactly one distributed or exactly two distributed or ...}$$
	$$= {}^{n}C_{1}. r + {}^{n}C_{2}. r^{2} + {}^{n}C_{3}. r ^{3} + \dots {}^{n}C_{n}. r ^{n}$$
	This is nothing but binomial expansion.
	$$= (1+r)^{n} - {}^{n}C_{0} = (1+r)^{n} - 1$$
	
	Here we put the distributer among the persons among which objects are to be distributed. Then we distribute freely and finally remove the case where the distributer gets all the objects as we have to give out at least one object. 


### Examples 
![[Pasted image 20231212095725.png]]
![[Pasted image 20231212100618.png]]
![[Pasted image 20231212101011.png]]

![[Pasted image 20231212101923.png]]
![[Pasted image 20231212102328.png]]

![[Pasted image 20231212102936.png]]
![[Pasted image 20231212103250.png]]