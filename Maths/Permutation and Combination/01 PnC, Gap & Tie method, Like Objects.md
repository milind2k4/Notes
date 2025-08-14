Links: [[00 Permutation and Combination]]
___
# Basic Permutation and Combination 
**Permutation** means *Arrangement.*
**Combination** means *Selection.*

No. of ways in which r objects can be selected from n different objects, i.e. *combination,*
$${}^{n}C_{r} = {n \choose r} = \frac{ n! }{ r!(n-r)! }$$

If there are different objects, and we select two times from the same lot, there will be order. 

No. of ways in which we can arrange n different objects in a row will be $n!$. 

No. of ways of selecting r objects from n identical objects = 1. 

No. of ways of arranging n identical objects in a row = 1. 

No. of ways of arranging r objects in a row selected from n different objects, i.e. *permutation,*
$${}^{n}P_{r} = {n \choose r} \times r! = \frac{ n! }{ (n-r)! }$$
Here we are doing two things, first selecting r objects, and then arranging them. 

In questions, we will use "select and then arrange" and not ${}^{n}P_{r}$. 

We can do some questions using both basic PnC and Fundamental principle of counting,

![[Pasted image 20231208150256.png]]

#### Examples 
![[Pasted image 20231208155600.png]]

![[Pasted image 20231208155615.png]]

![[Pasted image 20231208155625.png]]

![[Pasted image 20231208155710.png]]


## Gap and Tie Method 
in Arrangement

**Tie:** If in the permutation of n different objects we need that r particular objects should be placed together only, then consider them as one unit, permute this unit with the rest and then permute within this unit (intra permutation). 

**Gap:** If in the permutation of n different objects, we want that no two of r particular objects should be placed together, then permute rest of the objects, then in created gaps permute these objects. 

Permutation of n objects creates n+1 gaps.

If we need that in the permutation of n different objects *not all of* r particular objects should be together, then use bijection rule and remove the cases in which all r are together (tie).

#### Examples 
![[Pasted image 20231208161606.png]]


## Permutation of Like Objects 
#### Taken all at a time 

If there are total n objects out of which $n_{1}$ are alike of $T_{1}$, $n_{2}$ are alike of $T_{2}$ ... $n_{r}$ are alike of $T_{r}$, then total no. of ways of arranging these objects in a row will be,
$$= \frac{ n! }{ n_{1}!\ n_{2}!\ n_{3}! \dots n_{r}! }$$

![[Pasted image 20231208164017.png]]

![[Pasted image 20231208164926.png]]

#### Taken some at a time 
![[Pasted image 20231208171925.png]]

## Circular Permutations
Circular means that if the elements on the left and the right are the same then the arrangement is the same. 
Here relative position is of importance rather than absolute position. 

No. of ways of arranging n different objects around a circle,
$$= (n-1)!$$

![[Pasted image 20231213101005.png]]

If in above all places are numbered,
$$= n!$$

If in above clockwise and anticlockwise cannot be distinguished,
$$= \frac{ (n-1)! }{ 2 }$$
Like beads in a necklace. I.e. if it can be flipped.

In below image, if we flip the second necklace, it becomes the same as the first one. 
![[Pasted image 20231213101052.png]]

If one person is seated, then remaining seats will all be distinguishable and for further arrangement we will use linear permutation. 

Using this we can explain circular permutation. 
We first seat one of the n people. He can sit in 1 way. Now, all the seats are different and we have to seat n-1 people. Thus giving $1.(n-1)!$.

If circular permutation there will be n gaps between n placed objects, as opposed to n+1 in linear. The first and last gap in linear are combined when transferring to circular. 

![[Pasted image 20231213102250.png]]
