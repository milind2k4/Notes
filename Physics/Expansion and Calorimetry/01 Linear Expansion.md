Links: 
___
# Linear Expansion 
[[01 Ohm's Law#Dependence of R on Temp.]]

As we increase temp. from  $\ce{ T^{\circ}C }$ to $\ce{ (T + \Delta T) ^{\circ}C }$ the length of a rod will increase from $l_{o}$ to $l_{o} + \Delta l$. 

This change in length is given as,
$$\Delta l = \alpha l_{o} \Delta T$$
where $\alpha$ is called *coefficient of linear thermal expansion* and its unit is $\ce{ 1/^{\circ}C }$.

Thus the final length is,
$$l = l_{o} (1 + \alpha \Delta T)$$

Fractional change in length,
$$\frac{ \Delta l }{ l_{o} } = \alpha \Delta T$$

![[Pasted image 20240213212600.png]]

#### Change in Time Period of Simple Pendulum
[[05 Angular SHM#Simple Pendulum]]

Let the temp. change from $\theta_{o} ^{\circ}C$ to $(\theta_{o} + \Delta\theta)^{\circ}C$, then the fractional change in time period is,
$$\frac{ T' - T }{ T } = \frac{ 1 }{ 2 }(\alpha \Delta \theta)$$

![[Pasted image 20240213212617.png]]
![[Pasted image 20240213212651.png]]

#### Measuring Length using Metallic Scale 
Let the object be of length $l_{o}$ and has coefficient of expansion $\alpha_{o}$. 
The scale has coefficient of expansion $\alpha_{s}$.

Originally at temp. T, the scale will give measuring value,
$$\ce{ MV = \frac{ l_{o} cm }{ 1 cm } } = l_{o}$$

Now if we increase the temp. from T to T + $\Delta$T, both the scale and the object will expand. 

The length of the object will become,
$$l = l_{o}(1+\alpha_{o} \Delta T)$$
And the 1 cm on the scale will become,
$$1\ce{ cm' } = 1\ce{ cm }(1+\alpha_{s}\Delta T)$$

Thus the scale will give measuring value,
$$\ce{ MV = \frac{ l_{o}(1+\alpha_{o}\Delta T) cm }{ 1 cm(1 + \alpha_{s}\Delta T) } } = l_{o}\frac{ 1+\alpha_{o}\Delta T }{ 1+\alpha_{s}\Delta T }$$

Now, if the object and scale are made of the same material, the reading will be the same as  the previous one at temp. T.

Using binomial approximation,
$$
\begin{split}
\ce{ MV } &= l_{o}(1+\alpha_{o}\Delta T)(1+\alpha_{s}\Delta T)^{-1} \\
&= l_{o}(1+\alpha_{o}\Delta T)(1-\alpha_{s}\Delta T) \\
&= l_{o}(1+(\alpha_{o}-\alpha_{s})\Delta T) \\
\end{split}
$$

![[Pasted image 20240213205043.png]]

#### Effect of Temp. on Moment of Inertia 
At temp. T, the moment of inertia is $I_{o}$.

At temp. $T + \Delta T$,
![[Pasted image 20240213210707.png]]

### Thermal Stress 
Initially the wire of Young's Modulus $y$ is bound by two ends and has no tension. 

Now, we decrease the temp, and thus the length will be decreased. Due to this decrease, the ends will exert a force and produce tension. 

Here, strain is,
$$
\begin{split}
\text{strain} &= \frac{ \Delta l }{ l } \\
&= \frac{ l_{o}\alpha \Delta T }{ l_{o}(1-\alpha \Delta T) } \\
&= \frac{ \alpha \Delta T }{ 1 - \alpha \Delta T }
\end{split}
$$

And the stress is,
$$\text{stress} = \frac{ F }{ A }$$

Now, by definition of Young's Modulus,
$$
\begin{split}
y &= \frac{ \text{stress} }{ \text{strain} } \\
&= \frac{ F /A }{ \alpha \Delta T /(1-\alpha \Delta T) } \\
&\approx \frac{ F }{ A\alpha \Delta T }
\end{split}
$$

Thus the tension in the wire comes out to be,
$$F = yA\alpha \Delta T$$

![[Pasted image 20240213210150.png]]

### Bimetallic Strip 
When two metals are welded parallel to each other. 

We assume that the joint between them will not become undone and they will stick together on heating. 

Let the top strip has $\alpha_{1}$, and the bottom one has $\alpha_{2}$. 

If $\alpha_{1} > \alpha_{2}$, the top strip will increase more in length that the bottom one. 

Thus on heating, the bimetallic strip will form an arc with the top strip being farther away. 

![[Pasted image 20240214100033.png]]

At temp. $T + \Delta T$, the top strip will have length,
$$l_{1} = l_{o}(1 + \alpha_{1} \Delta T)$$
And the bottom strip will have length,
$$l_{2} = l_{o}(1 + \alpha_{2}\Delta T)$$

We can write,
$$
\begin{split}
\left( R + \frac{ d }{ 2 } \right)\theta &= l_{o}(1 + \alpha_{1}\Delta T) \\
\left( R - \frac{ d }{ 2 } \right)\theta &= l_{o}(1 + \alpha_{2}\Delta T) 
\end{split}
$$

On dividing, we get R,
$$R = \frac{ d + \frac{ d }{ 2 }(\alpha_{1} + \alpha_{2}) \Delta T }{ (\alpha_{1} - \alpha_{2})\Delta T }$$
On approximation,
$$R = \frac{ d }{ (\alpha_{1}-\alpha_{2})\Delta T }$$

On subtracting, we get $\theta$,
$$\theta = \frac{ l_{o}(\alpha_{1} - \alpha_{2})\Delta T }{ d }$$

![[Pasted image 20240214100838.png]]