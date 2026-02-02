Links: [[00 Differential Equation]], [[08 Exact Derivatives]]
___
# Exact Differentials
#important 

Some differential elements,
$$
\begin{split}
d(x^{2}+y^{2}) &= 2(xdx + ydy) \\
\\
d(x^{2}-y^{2}) &= 2(xdx - ydy) \\
\\
d(xy) &= xdy + ydx \\
\\
d\left( \frac{ y }{ x } \right) &= \frac{ xdy - ydx }{ x^{2} } \\
\\
d\left( \frac{ x }{ y } \right) &= \frac{ ydx - xdy }{ y^{2} }
\end{split}
$$
(the denominator tells which one to go to, because numerators are -ves of each other.)


These can also be used to integrate expressions wrt expression written after d,
e.g.
$$\int \frac{\displaystyle d\left( \frac{ y }{ x } \right)}{\displaystyle 1 + \left( \frac{y}{x} \right)^{2}} = \tan ^{-1}\left( \frac{y}{x} \right) + C$$


### Examples 
![[Pasted image 20231018085012.png]]

![[Pasted image 20231018085139.png]]

![[Pasted image 20231018085441.png]]

![[Pasted image 20231018085905.png]]

![[Pasted image 20231018090045.png]]

![[Pasted image 20231018090305.png]]

![[Pasted image 20231018090615.png]]

## Trigonometric or Polar Substitution 
#### $x = r\cos \theta$ and $y = r\sin \theta$
Substitute when $xdx + ydy$ is present in expression. 

Now,
$$
\begin{split}
dx &= \cos \theta dr - r\sin \theta d\theta \\
dy &= \sin \theta dr + r\cos \theta d\theta 
\end{split}
$$

To convert back into x and y,
$$
\begin{split}
r^{2} &= x^{2} + y^{2} \\
\tan \theta &= \frac{ y }{ x }
\end{split}
$$

Differential elements of these will be,
$$
\begin{split}
dr &= xdx + ydy \\
\sec^{2}\theta d\theta &= \frac{ xdy - ydx }{ x^{2} } \\
r^{2} d\theta &= xdy - ydx
\end{split}
$$

#### $x = r\sec \theta$ and $y = r \tan \theta$
Substitute when $xdx - ydy$ is present in expression. 

Now,
$$
\begin{split}
dx &= \sec \theta dr + r\sec \theta \tan \theta d\theta \\
dy &= \tan \theta dr + r\sec^{2}\theta d\theta
\end{split}
$$

To convert back into x and y,
$$
\begin{split}
x^{2} - y^{2} &= r^{2} \\
\sin \theta &= \frac{ y }{ x }
\end{split}
$$

Their differential elements,
$$
\begin{split}
xdx - ydx &= rdr \\
r^{2} \sec \theta d\theta &= xdy - ydx
\end{split}
$$

### Examples 
![[Pasted image 20231018082025.png]]
![[Pasted image 20231018083150.png]]
![[Pasted image 20231018083522.png]]
![[Pasted image 20231018083653.png]]