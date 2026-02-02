Links: [[02 Youngs Double Slit Experiment]]
___
# Modifications of YDSE
## Polychromatic Light 
The source light has more than one wavelength. 

At the centre, there will be maxima for all wavelengths as this point has zero path difference for all of them. 
Thus the central maxima will have white colour. 

Now, since wavelength is different, the fringe width will be different for all of them. Violet will have smallest $\beta$ and thus the first maxima will be of violet. 

Red will have largest $\beta$ and thus the last maxima of the pattern will be of red. 

At some points, some maxima of violet and some maxima of red will coincide. 

![[Pasted image 20240208100335.png]]

![[Pasted image 20240208101027.png]]

## Oblique Incidence of Light
The central maxima will not be at the centre, but a distance $D\theta_{o}$ below it.

This is because there will already be some path difference when the light is incident on the slits. 

The net path difference will be,
$$\Delta x = d\sin \theta + d\sin \theta_{o}$$
If both $\theta$ and $\theta_{o}$ are small, we will get,
$$\Delta x = d\theta_{o} + \frac{ dy }{ D }$$

For central maxima, path difference should be zero, 
$$
\begin{split}
0 &= d \theta_{o} + \frac{ dy }{ D } \\
y &= -D\theta_{o}
\end{split}
$$

For nth maxima,
$$
\begin{split}
d \theta_{o} + \frac{ dy }{ D } &= n\lambda \\
y &= \frac{ n\lambda D }{ d } - D\theta_{o} \\
&= n\beta - D\theta_{o}
\end{split}
$$

For nth minima,
$$y = (n-0.5)\beta - D\theta_{o}$$

Thus fringe width will remain the same. 

The whole pattern will be shifted down by $D\theta_{o}$.


![[Pasted image 20240208102119.png]]

![[Pasted image 20240208101924.png]]
![[Pasted image 20240208101938.png]]

## Transparent Medium 
Between the slits and the screen, we insert a transparent medium of refractive index n. 

Light of wavelength $\lambda_{o}$ in air is incident on the slits.
And,
$$c = \lambda_{o} f$$

Now, in this medium,
$$
\begin{split} 
v &= \frac{ c }{ n } \\
\frac{ c }{ n } &= \lambda f \\
\lambda &= \frac{ c }{ fn } \\
&= \frac{ \lambda_{o} }{ n }
\end{split}
$$
Thus wavelength becomes $1 /n$ times. 

The fringe width thus becomes,
$$
\begin{split}
\beta &= \frac{ \lambda D }{ d } \\
&= \frac{ \lambda_{o}D }{ nd } \\
&= \frac{ \beta_{o} }{ n }
\end{split}
$$
Thus fringe width also decreases to 1/n times. 

The rest pattern will be the same.

![[Pasted image 20240208103033.png]]

## Insertion of Transparent Slab
[[00 Wave Optics#Optical Length]]

Transparent parallel slab of thickness t and refractive index $\mu$ is put in front of one of the slits. 

At P, the path difference will be,
$$
\begin{split}
\Delta x &= S_{2}P - (S_{1}P)' \\
&= S_{2}P - (S_{1}P - t + \mu t) \\
&= S_{2}P - S_{1}P - (\mu-1)t \\
&= d\sin \theta - (\mu - 1)t \\
&= \frac{ dy }{ D } - (\mu - 1)t
\end{split}
$$

The central maximum will be at,
$$
\begin{split}
\Delta x &= 0 \\
\frac{ dy }{ D } - (\mu - 1)t &= 0 \\
y &= \frac{ Dt(\mu-1) }{ d }
\end{split}
$$
This is the shift of pattern. 
$$y_{o} = \text{shift} = \frac{ Dt(\mu-1) }{ d }$$

nth maxima will be,
$$
\begin{split}
\Delta x &= n\lambda \\
\frac{ dy }{ D } - (\mu - 1)t &= n\lambda \\
y &= \frac{ n\lambda D }{ d } + \frac{ Dt(\mu-1) }{ d } \\
&= n\beta + \text{shift}
\end{split}
$$

![[Pasted image 20240208104503.png]]
