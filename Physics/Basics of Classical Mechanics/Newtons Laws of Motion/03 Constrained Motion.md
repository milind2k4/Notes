Links: [[00 Dynamics]], [[02 Forces]]
___
# Constrained Motion
If motion of 2 bodies are dependent on each other, then we say that the motion is constraint. 

## Rod Constraint
The length of the rod is fixed. 

$$
\begin{split}
x^{2} + y^{2} &= l^{2} \\
\text{Diff. wrt t,} \\
2xv_{x} - 2yv_{y} &= 0\ (\text{as y is decreasing}) \\
v_{y} &= \frac{ xv_{x} }{ y } \\
&= v_{x}\cot \theta 
\end{split}
$$

![[Pasted image 20230530132154.png]]

Velocity of the mid point is,
$$v_{cx} = \frac{ v_{x} }{ 2 }$$
$$v_{cy} = \frac{ -v_{x}\cot \theta }{ 2 }$$

Alternatively, the velocity along the rod is zero, 
$$v_{y}\sin \theta = v_{x}\cos \theta $$
$$v_{y} = v_{x}\cot \theta $$

![[Pasted image 20230530132330.png]]


## String Constraint
We assume that the string is extensible, will not break and will not slack.

![[Pasted image 20230530132927.png]]

Due to this, in a pully system, the v/a/x of blocks are same in magnitude and opposite in direction. 

In a pulley-pulley block system, the length of the 2nd string is,

$$l = x_{2} + x_{3} - 2x_{p} + \pi r$$
This is constant. Differentiating it wrt time,
$$0 = v_{2} + v_{3} - 2v_{p} + 0$$
$$2v_{p} = v_{2} + v_{3}$$
$$v_{p} = \frac{v_{2} + v_{3}}{2}$$
$$a_{p} = \frac{a_{2} + a_{3}}{2}$$
but we need to put them with direction.  

![[Pasted image 20230530134047.png]]

If there is an ideal pulley, then the force on the pulley is zero in this situation.
![[Pasted image 20230530143839.png]]


## Wedge Constraint
Wedges are rigid i.e. their shape size and geometry is fixed. 
Wedges which are in contact will remain in contact. 

There is no relative motion along the common normal. Thus, x/v/a of both the blocks along the common normal will be the same. 

- Find common normal 
- Find the value of x/v/a along that normal for both bodies
- Equate them.

If the acceleration of one of the blocks along the horizontal direction is a then the acceleration of another block on top of it, in the vertical direction will be,
$$b = a\tan \theta$$

![[Pasted image 20230531120846.png]]
![[Pasted image 20230531121007.png]]

## Spring Constraint
A spring can push and pull as well. It wants to stay in its natural length. If the spring is massless, the tension at every point of the string will be the same. 

![[Pasted image 20230531121625.png]]

### Hooke's Law
$$T \propto x$$
$$T = kx$$
where x is the compression or extension and k is called **Spring Constant** and depends on the string, with unit $\ce{ N m^{-1} }$ and dimensions $\ce{ [MT^{-2}] }$

Also,
$$k \propto \frac{ 1 }{ \text{natural length of spring} }$$

An example,
![[Pasted image 20230531122735.png]]


### Combination of Strings
#### Parallel Combination
When they are connected in such a way that both their ends touch the same respective thing. 
$$
\begin{split}
k_{1}x + k_{2}x &= k_{eq}x \\
k_{eq} &= k_{1} + k_{2}
\end{split}
$$

![[Pasted image 20230531122836.png]]

#### Series Combination
When they are connected end to end. The tension in the springs should be the same. 

$$
\begin{split}
T &= k_{2}x_{2} \\
T &= k_{1}x_{1} \\
T &= k_{eq}(x_{1}+x_{2}) \\
T &= k_{eq}\left( \frac{ T }{ k_{1} } + \frac{ T }{ k_{2} } \right) \\
\frac{ 1 }{ k_{eq} } &= \frac{ 1 }{ k_{1} } + \frac{ 1 }{ k_{2} }
\end{split}
$$


![[Pasted image 20230531123345.png]]

For n springs of length $l$ and spring constant $k$ connected in series,
$$l_{eq} = nl$$
$$k_{eq} = \frac{ k }{ n }$$

From here, we can see that,
$$k \propto \frac{ 1 }{ l }$$

### Cutting of String vs Spring
When a string is cut, the tension of the string becomes zero instantaneously. 

When an ideal spring is cut, the spring instantaneously comes to its natural length (as the mass is zero), and thus the tension becomes zero. 

![[Pasted image 20230531124317.png]]

In a spring string system, cutting the string does not change the tension in the spring instantaneously. Thus, just after cutting the string, T in spring will not change instantaneously. 

However, if we cut the spring, the tension ins string may change instantaneously. 

![[Pasted image 20230601122042.png]]

### Spring Balance
In general it measures weight or mass. 

In physics, it measures tension. 

A box has a spring with large spring constant, which is connected to a pointer. This pointer moves on a scale which gives the reading of tension. 

![[Pasted image 20230601124328.png]]

Until the extension changes, the reading will be the same. 

