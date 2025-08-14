Links: [[01 Algebraic Inequalities]]
___
# Modulus Inequalities
#important 
$|x|$ represents the magnitude of x or the distance of x from zero. It is always non-negative, i.e. zero or positive.  

If we move away from $0$ in either direction, the value of $|x|$  always increases.

### Some Properties of Modulus
**Definition,**
$$
\begin{split}
|x| &\neq \pm x \\
&= x,\ x > 0 \\
&= -x,\ x < 0 \\
||x|| &= |x| 
\end{split}
$$

**Algebraic,**
$$
\begin{split}
|-x| &= |x| \\
|x - y| &= |y - x| \\
|xy| &= |x||y| \\
\left| \frac{ x }{ y } \right| &= \frac{ |x| }{ |y| } 
\end{split}
$$

**Power,**
$$
\begin{split}
|a^{n}| &= |a|^{n} \\
x^{2m} &= |x|^{2m} = |x^{2m}| \\
x^{2m+1} &\neq |x|^{2m+1} \neq |x^{2m+1}|
\end{split}
$$

**Implication,**
$$|A| = \alpha\implies A = \alpha \ or\ A = -\alpha$$
If $\alpha$ is -ve, then $A \in \phi$

**Triangle inequalities,**
$$|x+y| \leq |x|+|y|$$ 
equality holds when $xy \geq 0$. I.e. we cannot break mod on addition. 
$$|x-y| \geq ||x|-|y||$$
equality holds when $xy \geq 0$

- For multiple mods on the same term (like $||x-a| + |x-b||$), check the previous two, it might help in reducing the number of cases. 

## Solving Inequalities involving Modulus
$$|x| \geq 0$$

If $a>0$,
$$
\begin{split}
|x| &\geq a \implies x \in ( -\infty,-a] \cup [\ a,\infty\ ) \\
|x| &\leq a \implies x \in [-a,a\ ] \\
|x| &\geq -a \implies x \in R \\
|x| &\leq -a \implies x \in \phi
\end{split}
$$

If there are multiple $|\ |$'s on the same term then split the question into cases then solve as suggested in [[00 Basic Mathematics]]
- For final solution, we can just write all of the intervals with union, there's no need to check intersection as the cases are distinct. 

## Graph of Modulus
We need to bring the function to the form
$$y = |x-x_{1}| + |x-x_{2}| + |x-x_{3}| + .....$$

The critical points will be $x_{1},\ x_{2},\ x_{3}....$. Find the value of y at these point and plot them. Connect then using straight lines.

- Calculate values at critical points and join them using straight lines.
- Calculate values at one next to critical points at edges.
- Join them using straight lines.

![[Pasted image 20230519095815.png|400]]

Graphs are useful in solving inequalities. Bring all of the mods to one side and say that value is y, then find all the points which satisfy the condition. 

![[Pasted image 20230425083145.png]]

When both x and y are indie modulus, the graph is a square or rhombus. 

![[Pasted image 20230216211758.png]]

## Breaking Moduli
Change sign of inequality and $a$. There is always $\cap$ in the middle.  

![[Pasted image 20230216212248.png]]

![[Pasted image 20230216212313.png]]

![[Pasted image 20230216213617.png]]

## Examples
If there are mods on both sides of the inequality, then we can square the inequality as both sides are necessarily +ve.
![[Pasted image 20230425080947.png]]

Using Properties of Mod,
![[Pasted image 20230425081820.png]]

When a = 0 or -ve,
![[Pasted image 20230425083815.png]]