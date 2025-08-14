Links: [[00 Limits]]
___
# Continuity

A function is said to be continuous at x = a if
$$\lim_{ x \to a } f(x) = f(a)$$

If graph of $f(x)$ is present on both sides of x = a, then for continuity,
$$\lim_{ x \to a^{-} } f(x) = \lim_{ x \to a^{+} } f(x) = f(a)$$

If x = b is the right most point of the domain, then for continuity at that point,
$$\lim_{ x \to b^{-} } f(x) = f(a)$$
Similarly if b is left most point,
$$\lim_{ x \to b^{+} } f(x) = f(a)$$

If at x = a, function is not continuous, then the function is called discontinuous at that point.
It at x = a function is discontinuous, then its graph (if exists) will have a break at x = a. 
![[Pasted image 20230202145620.png]]

When we say that function is discontinuous then mention the corresponding point also. 

#### Reasons for Discontinuity
1. Limit does not exit. 
2. Function is undefined at that point. 
3. If limit and value of function are not equal. 

#### Types of Discontinuity 
If the graph of $f(x)$ is discontinuous at x = a and,
1. If Limit at a does not exits then it is called **Non Removable** discontinuity.
	- If LHL or RHL or both $\to \pm \infty$ then it is called *Infinite Type.*
	- If LHL $\neq$ RHL then it is called *Finite Type.* The difference between LHL and RHL is called *Jump of Discontinuity.*
	- If value of function fluctuates then it is called *Oscillatory.*
	  $\\$
3. If Limit does exits, it is called **Removable** discontinuity. 
	1. If $f(a)$ is undefined, then it is called *Missing Point* discontinuity.
	2. If $f(a)$ is defined but is unequal to limiting value, then it is called *Isolated Point* discontinuity.

### Continuity in an Interval
A function is continuous in an interval $(a,b)$ if it is continuous at every point in the interval $(a,b)$. 

For interval $[a,b]$, it should be continuous in $(a,b)$ and
$$\lim_{ x \to a^{+} } f(x) = f(a)$$
$$\lim_{ x \to b^{-} } f(x) = f(b)$$

#### Continuity in Domain and of Graph
If nothing is said, we check continuity of graph. 

If function's graph is discontinuous at some point then there will be break in the graph at that point. This point may or may not be in domain. 

To discuss continuity of a function in its domain, we only check points for which it is defined i.e. which lies in its domain. 

## [[08.5 Theorems of Continuity]]

### Some Points to Note
If there is GIF in the function and if the expression inside it crosses any integer (i.e. can approach that integer from both LHS and RHS), the limit of the function will not exist at that integer.

For limit to exist in GIF function, the expression inside should only approach integer from RHS (or from above). As otherwise the LHL will be I - 1 and functional value will be I. 

If however, the expression inside can only approach an integer from one side, the limit will exist. 
![[Pasted image 20230809135519.png]]
![[Pasted image 20230809140125.png]]
![[Pasted image 20230810130203.png]]

We can also check by making graph,
![[Pasted image 20230810131212.png]]

To check continuity of composite function, check it at all points wherever argument function (inside) is discontinuous and at the points where argument function takes the value at which primary function (outside) is discontinuous. 

i.e. if f is discontinuous at 3 and g at 7, then check continuity of $f(g(x))$ at x = 7 and points where g = 3.

## Examples
![[Pasted image 20230809132222.png]]
To check (at I for example) we use tree diagram, where the left most means LHL, middle means functional value and right most means RHL.
![[Pasted image 20230809132436.png]]

![[Pasted image 20230809132927.png]]
![[Pasted image 20230809132936.png]]

Sometimes we will have to find limit to find the function,
![[Pasted image 20230809133306.png]]
![[Pasted image 20230809133317.png]]

Some functions' graph cannot be made. And in case it changes its definition at every point, we take any generic point and then analyse. 
We analyse by contradiction or non-contradiction. 

In the below question, the graph of function cannot be made and thus this function has only mathematical continuity at x = 5.
![[Pasted image 20230809134131.png]]
![[Pasted image 20230809134147.png]]

In some questions we give answer in terms of parameter,
![[Pasted image 20230809134624.png]]

Some questions are solved easily using graphs,
![[Pasted image 20230810131713.png]]

![[Pasted image 20230811115951.png]]

![[Pasted image 20230811120201.png]]
![[Pasted image 20230811120754.png]]

![[Pasted image 20230811121246.png]]
