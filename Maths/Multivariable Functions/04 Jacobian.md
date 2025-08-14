Links: [[01 Partial Differentiation]]
___
# Jacobian

It is used to change working planes. I.e. if we want to go from cartesian to polar, we can use Jacobians. 

If $u, v, w$ are the functions of $x, y, z$, then the Jacobian, 
$$J(u,v,w)$$
wrt $x, y, z$ is 
$$
\begin{split}
J(u,v,w) &= \frac{ \partial (u,v,w) }{ \partial (x,y,z) } \\
&= 
\begin{vmatrix}
\frac{ \partial u }{ \partial x } & \frac{ \partial u }{ \partial y } & \frac{ \partial u }{ \partial z } \\
\frac{ \partial v }{ \partial x } & \frac{ \partial v }{ \partial y } & \frac{ \partial v }{ \partial z } \\
\frac{ \partial w }{ \partial x } & \frac{ \partial w }{ \partial y } & \frac{ \partial w }{ \partial z }
\end{vmatrix}
\end{split}
$$

### Properties of Jacobian
**Chain Rule,**
$$\frac{ \partial (u,v) }{ \partial (x,y) } \times \frac{ \partial (x,y) }{ \partial (u,v) } = 1$$

If $u,v$ are functions of $x,y$ and $x,y$ are functions of $r,\theta$, i.e.
$$\ce{ (u,v) -> (x,y) -> (r,\theta) }$$
then,
$$\frac{ \partial (u,v) }{ \partial (r,\theta) } = \frac{ \partial (u,v) }{ \partial (x,y) } . \frac{ \partial (x,y) }{ \partial (r,\theta) } $$

### Jacobian of Implicit Functions
Let,
$$
\begin{split}
F_{1} &= f_{1}(x_{1}, x_{2}, x_{3}, u_{1}, u_{2}, u_{3} \dots) &= 0 \\

F_{2} &= f_{2}(x_{1}, x_{2}, x_{3}, u_{1}, u_{2}, u_{3} \dots) &= 0 \\

F_{3} &= f_{3}(x_{1}, x_{2}, x_{3}, u_{1}, u_{2}, u_{3} \dots) &= 0
\end{split}
$$

Then,
$$
\frac{ \partial (u_{1}, u_{2}, u_{3}) }{ \partial (x_{1}, x_{2}, x_{3}) } = (-1)^{3} 
\frac{ 
\displaystyle \frac{ \partial (F_{1}, F_{2}, F_{3}) }{ \partial (x_{1}, x_{2}, x_{3}) } 
 }{ 
\displaystyle \frac{ \partial (F_{1}, F_{2}, F_{3}) }{ \partial (u_{1}, u_{2}, u_{3}) } 
}
$$

Again, for two variables,
$$
\begin{split}
F_{1} &= f_{1}(x, y, u, v) &= 0 \\
F_{2} &= f_{2}(x, y, u, v) &= 0 
\end{split}
$$
The Jacobian is,
$$
\frac{ \partial (x, y) }{ \partial (u, v) } = (-1)^{2} 
\frac{ 
\displaystyle \frac{ \partial (F_{1}, F_{2}) }{ \partial (u, v) } 
}{ 
\displaystyle \frac{ \partial (F_{1}, F_{2}) }{ \partial (x, y) } 
}
$$

## Functional Relationship
[[10 Functional Equations]]

Let $u_{1}, u_{2}, u_{3}, \dots$ be functions of $x_{1}, x_{2}, x_{3}, \dots$ then the necessary condition for the existence of a relation of the form,
$$F(u_{1}, u_{2}, u_{3} \dots) = 0$$
is that the Jacobian,
$$\frac{ \partial (u_{1}, u_{2}, u_{3} \dots) }{ \partial (x_{1}, x_{2}, x_{3} \dots) }$$
vanishes identically. 

To find the relation, we will use [[03 Formulae Related to Inv-T]], [[Trigonometry]], and hit and trial methods. 