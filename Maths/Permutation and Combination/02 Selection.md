Links: [[03 Distribution]], [[04 Grouping]]
___
# Selection 
##### Different Objects
No. of ways of selecting r objects from n different objects,
$$= {}^{n}C_{r}$$

No. of ways of selecting *at least* r objects from n different objects,
$$= {}^{n}C_{r} + {}^{n}C_{r+1} + {}^{n}C_{r+2} + \dots {}^{n}C_{n}$$

No. of ways of selecting *at most* r objects from n different objects,
$$= {}^{n}C_{0} + {}^{n}C_{1} + {}^{n}C_{2} + \dots {}^{n}C_{r}$$

No. of ways of selecting *at least* 1 object from n different objects, (sum of binomial coefficients)
$$= {}^{n}C_{1} + {}^{n}C_{2} + {}^{n}C_{3} + \dots {}^{n}C_{n} = 2^{n} - 1$$

This we can explain using two boxes "selection" and "rejection". Each object will have two options, thus $2^{n}$ and we remove the case when all are rejected, thus $-1$. 

##### Identical Objects
No. of ways of selecting r objects from n identical objects,
$$= 1$$

No. of ways of selecting *at least* r objects from n identical objects,
$$= 1 + 1 + 1 + \dots + 1 = n - (r - 1) = n - r + 1$$

![[Pasted image 20231213090232.png]]

No. of ways of selecting *at least* 1 object from n identical objects,
$$= 1 + 1 + 1 + \dots + 1 = n$$

#### Examples 
![[Pasted image 20231213091229.png]]
![[Pasted image 20231213092537.png]]

![[Pasted image 20231213141544.png]]
![[Pasted image 20231213142121.png]]