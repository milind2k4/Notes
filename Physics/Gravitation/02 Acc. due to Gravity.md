Links: [[00 Gravitation]]
___
# Acceleration due to Gravity
At surface,
$$
\begin{split}
f &= \frac{ mGM }{ R^{2} } \\
mg &= \frac{ mGM }{ R^{2} } \\
g &= \frac{ GM }{ R^{2} } 
\end{split}
$$

In terms of density,
$$g = G\ \rho \frac{ 4 }{ 3 } \pi R$$

![[Pasted image 20231217125817.png]]

### Variation in $g$
#### With Height
$$
\begin{split}
f &= \frac{ mGM }{ (R + h)^{2} } \\
g' &= \frac{ GM }{ (R + h)^{2} }
\end{split}
$$
As we move away from the planet, g decreases. 

Now, this can be written as,
$$
\begin{split}
g' &= \frac{ GM }{ R^{2} \left( 1 + \frac{h}{R} \right)^{2} } \\
g' &= g \left( 1 + \frac{ h }{ R } \right)^{-2}
\end{split}
$$
For earth, if h is in order of 1,2,3 etc km, we can use binomial approximation,
$$g' = g\left( 1 - \frac{ 2h }{ R } \right)$$

![[Pasted image 20231217130539.png]]

#### With Depth
$$
\begin{split}
f &= \frac{ mGM (R-d) }{ R^{3} } \\
g' &= \frac{ GM(R-d) }{ R^{3} } \\
&= \frac{ GM }{ R^{2} }\left( 1 - \frac{ d }{ R } \right) \\
&= g\left( 1 - \frac{ d }{ R } \right)
\end{split}
$$
Thus g decreases linearly as we go down.

![[Pasted image 20231217130809.png]]

#### Due to Rotation of Earth

$$g' = g - R_{e}\omega ^{2} \cos ^{2}\theta$$