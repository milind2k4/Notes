Links: [[00 Differential Equation]]
___
# Solving Differential Equation

Do not forget to write arbitrary constant $c$.

### Variable Separable (VS)
If all the expressions containing x can be clubbed with dx and y with dy. We club them and then integrate.

$$f(x) dx = g(y)dy$$

#### Reducible to Variable Separable (RVS)
The DE of the form,
$$\frac{ dy }{ dx } = f(ax + by + c)$$
can be reduced into VS by substitution, 
$$ax + by + c = t$$

Differentiate wrt x,
$$
\begin{split}
a + b\frac{ dy }{ dx } &= \frac{ dt }{ dx } \\
a + b f(t) &= \frac{ dt }{ dx } \\
dx &= \frac{ dt }{ a + bf(t) }
\end{split}
$$
Put the value of t back into the expression. 

### Homogeneous Differential Equation (HDE)
[[01 Partial Differentiation#Homogeneous Function]]

Also, note that the first differential of an HE is y/x and the second differential is zero.

Equations of the form,
$$\frac{ dy }{ dx } = f\left( \frac{ y }{ x } \right)$$

To solve,
$$
\begin{split}
\frac{y}{x} &= t \\
y &= xt \\
\frac{ dy }{ dx } &= t + x \frac{ dt }{ dx } \\
\ce{ Put this back &\ into the equation}. \\
t + x \frac{ dt }{ dx } &= f(t) \\
\frac{dx}{x} &= \frac{dt}{f(t) - t}
\end{split}
$$
For final answer, put the value of t, i.e. y/x back into the solution. 

To save time, jump straight into the last step. 

### Linear by Linear
$$\frac{ dy }{ dx } = \frac{ a_{1}x + b_{1}y + c_{1} }{ a_{2}x + b_{2}y + c_{2} }$$

##### If $c_{1} = c_{2} = 0$
The equation is homogeneous, solve using method above. 

##### If $\displaystyle \frac{a_{1}}{a_{2}} = \frac{b_{1}}{b_{2}}$
The equation is reducible to variable separable. 

Put $a_{1}x + b_{1}y = t$ and then variables will be separated. 

#### If $a_{2} + b_{1} = 0$
Then cross multiple and integrate terms one by one.

Write $a_{2} = -b_{1}$.

Use,
$$d(xy) = x\ dy + y\ dx$$

#### If none of the above 
If none of the above are applicable then we find the point of intersection of the lines and shift the origin to that point. Since line passing through origin has no c, $c_{1},c_{2}$ will disappear. 

I.e. substitute,
$$
\begin{split}
x &= X + h \\
y &= Y + k
\end{split}
$$
Chose h and k such that,
$$a_{1}h + b_{1}k + c_{1} = 0$$
$$a_{2}h + b_{2}k + c_{2} = 0$$

The DE will become,
$$\frac{ dY }{ dX } = \frac{ a_{1}X + b_{1}Y }{ a_{2}X + b_{2}Y }$$
Now this is a HDE and thus can be solved that way. 

### [[01.1 Linear Differential Equations]]

### [[01.2 Reducible to LDE]]

## Examples 
![[Pasted image 20231014195111.png]]

![[Pasted image 20231014195908.png]]

![[Pasted image 20231014200959.png]]

![[Pasted image 20231014202528.png]]

![[Pasted image 20231014202541.png]]

![[Pasted image 20231014203016.png]]



