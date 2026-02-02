Links: [[04 Arithmetic Geometric Progression]]
___
# Difference Method
aka $V_{n}$ method or Telescopic Series


If we can write general term, $T_{r}$ in terms of $V_{r}$ and $V_{r-1}$, then,
$$T_{r} = V_{r} - V_{r-1}$$

Then in the total sum, terms will cancel,
![[Pasted image 20230616095925.png]]

We can also skip this and write the smaller r into the smaller difference term and the bigger into the bigger difference term.

If the series has varying terms in the denominator, and it is not a GP, then it will probably be solved by difference method. 

##### Shortcut to Write Sum
$$T_{r} = V_{r} - V_{r-2} \implies S_{n} = V_{n} + V_{n-1} - V_{-1} - V_{0}$$
put the two smallest values into the smaller r term and the two biggest into the bigger r terms.
Do the same if the difference is of more  than 2 also. In which case we put that many numbers into the respective terms.

Example where the difference is of 3, we put 3 values into each,
![[Pasted image 20230616101818.png]]


#### Different Breaking Methods
If there are terms in the numerator, and they are consecutive in the sense of r (i.e. putting r+1 in the first gives 2nd and so on), then to break them into two parts, in $V_{r}$ write one next term and in $V_{r-1}$, write one previous. 
Check whether they are the same and then if there is some extra constant, divide by it. 

Then check whether putting r $\pm$ k in one of them gives the other.

Example,
![[Pasted image 20230616095829.png]]

If there are terms in denominator and they are consecutive in r, then in the difference terms remove one of the corner terms,

Example,
![[Pasted image 20230616100603.png]]


In questions with factorial,
![[Pasted image 20230617080003.png]]

The formula in [[02 Formula and Expansions]] may be used here also,
![[Pasted image 20230617080219.png]]

Sometimes while trying to break into difference form, we might get extra terms, which we will have to sum using $\sum$ formula,
![[Pasted image 20230617080837.png]]

In trigonometric sum questions, most frequently, this method will be used,
![[Pasted image 20230617081318.png]]
