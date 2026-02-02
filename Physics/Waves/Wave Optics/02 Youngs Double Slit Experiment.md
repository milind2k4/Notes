Links: [[02 Interference]]
___
# Young's Double Slit Experiment (YDSE)
#important 
[[00 Wave Optics#Interference of 2 Coherent Waves]]

In 1801, Thomas Young experimented and proved that Light behaves like a wave, using the concept of interference. 

We take a monochromatic source and put a cardboard in front of it with two slits. And we put a screen in front of this setup. 

When light passes through the thin slits, it gets diffracted and spreads. 

As these two waves are coming from the same source, they have no initial phase difference. Thus, according to the path difference, there will be consecutive bright and dark strips on the screen. 

Thus an interference pattern is formed on the screen, proving the wave nature of light. 

![[Pasted image 20240207201639.png]]
![[Pasted image 20240207201740.png]]

#### Calculation of Path Difference 
d is the separation between the slits and D is that between the slits and the screen. And D is much bigger than d.

At centre, the waves coming from both the slits travel the same distance. I.e. $\Delta x = 0$. Thus there will be a bright spot at the centre. This bright fringe is called *Central Maximum.*

We calculate path difference for any other point y distance from the centre.

Since $D \gg d$, the angular position of point P can be assumed $\theta$ from both slits.
Also since the point P is far away, we can assume that $S_{2}P$ is equal to $\perp P$ and the difference in path is just $d\sin \theta$.

$$
\begin{split}
\Delta x &= S_{2}P - S_{1}P \\
&= d\sin \theta \\ 
\end{split}
$$
This path difference, according to the law of sides of a triangle, cannot be more than $S_{1}S_{2}$. I.e.,
$$S_{2}P - S_{1}P \leq S_{1}S_{2}$$

If $y \ll D$, then $\theta$ is very small. 
And we can write,
$$\sin \theta \approx \theta \approx \tan \theta$$

Thus, we get,
$$\Delta x = d\tan \theta = \frac{ dy }{ D }$$

![[Pasted image 20240207202640.png]] 

However, if there is big angle subtended, we cannot use the approximation,
![[Pasted image 20240207205422.png]]

#### Constructive Interference 
$$
\begin{split}
\Delta x &= n\lambda \\
\frac{dy}{D} &= n\lambda \\
y &= \frac{ n\lambda D }{ d }
\end{split}
$$
Thus at these points, we get bright fringes, i.e. maxima and observe constructive interference.

The difference between two consecutive bright fringes is called **Fringe Width**, represented by $\beta$,
$$\beta = \frac{ \lambda D }{ d }$$

Thus at integral multiples of $\beta$ we get bright fringes. And there is always a bright fringe at the central point O, however, it is not the first bright fringe. 

nth maxima is at,
$$y_{n} = n\beta = \frac{ n\lambda D }{ d }$$

![[Pasted image 20240207203409.png]]

##### Highest Order of Maxima 
We know that, for constructive interference,
$$d\sin \theta = n\lambda$$
Now, as $\sin \theta$ cannot be more than or equal to 1 here, we get,
$$
\begin{split}
\Delta x &< d \\
n\lambda &< d \\
n &< \frac{ d }{ \lambda }
\end{split}
$$
Thus the highest order of maxima will be,
$$n = \left[ \frac{ d }{ \lambda } \right]$$
where \[.\] is greatest integer.

And the no. of maxima will be,
$$\text{no. of maxima} = 2\left[ \frac{ d }{ \lambda } \right] + 1$$

![[Pasted image 20240207210009.png]]

However, if $d/\lambda$ is integer, the highest order will be at $[d / \lambda] - 1$. This is because the final maxima will be at infinity, when $\sin \theta = 1$ i.e. $\theta = 90^{\circ}$.

![[Pasted image 20240207211138.png]]

#### Destructive Interference 
$$
\begin{split}
\Delta x &= (2n-1) \frac{\lambda}{2} \\
\frac{dy}{D} &= (2n-1) \frac{\lambda}{2} \\
y &= \left( n - \frac{1}{2} \right) \frac{\lambda D}{d}
\end{split}
$$
Thus at these points, we get dark fringes, i.e. minima and observe destructive interference. 

The difference between two consecutive dark fringes is called **Fringe Width**, represented by $\beta$,
$$\beta = \frac{ \lambda D }{ d }$$

Thus at $n-0.5$ multiples of $\beta$ we get dark fringes. 

nth minima is at,
$$y_{n} = (n - 0.5)\beta = (n-0.5) \frac{ \lambda D }{ d }$$

![[Pasted image 20240207203428.png]]

##### Highest Order of Minima 
We know that, for destructive interference,
$$d\sin \theta = (n - 0.5)\lambda$$
Now, as $\sin \theta$ cannot be more than or equal to 1 here, we get,
$$
\begin{split}
\Delta x &< d \\
(n - 0.5)\lambda &< d \\
n &< \frac{ d }{ \lambda } + \frac{ 1 }{ 2 }
\end{split}
$$
Thus the highest order of maxima will be,
$$n = \left[ \frac{ d }{ \lambda } + \frac{ 1 }{ 2 } \right]$$
where \[.\] is greatest integer.

And the no. of minima will be,
$$\text{no. of minima} = 2n$$

#### Angular Fringe Width 
The angle made by one fringe width on the cardboard is called **Angular Fringe Width.**

$$\alpha = \frac{\beta}{D} = \frac{\lambda}{d}$$

Its unit is radian not degree.

![[Pasted image 20240207204022.png]]

### Intensity of Interference Pattern
Let due to $S_{1}$, the intensity is $I_{1}$, and due to $S_{2}$ it is $I_{2}$.

Now, the phase difference between them is,
$$
\begin{split}
\Delta \phi &= \frac{ 2\pi }{ \lambda } \Delta x \\
&= \frac{ 2\pi }{ \lambda } \frac{ yd }{ D } \\
&= \frac{ 2\pi }{ \beta }y
\end{split}
$$

The resultant intensity at point P will be,
$$
\begin{split}
I_{res} &= I_{1} + I_{2} + 2\sqrt{ I_{1}I_{2} }\cos \Delta \phi \\
&= I_{1} + I_{2} + 2\sqrt{ I_{1}I_{2} }\cos \left( \frac{2\pi}{\lambda} \Delta x \right) \\
&= I_{1} + I_{2} + 2\sqrt{ I_{1}I_{2} }\cos \left( \frac{ 2\pi }{ \beta } y \right) \\
\end{split}
$$

When $y = n\beta$, there will be maxima and intensity will be,
$$I_{max} = (\sqrt{ I_{1} } + \sqrt{ I_{2} })^{2}$$

When $y = (2n+1) \frac{\beta}{2}$, there will be minima and intensity will be,
$$I_{min} = (\sqrt{ I_{1} } - \sqrt{ I_{2} })^{2}$$

The ratio of the min and max intensity is called **Contrast,**
$$\text{contrast} = \frac{ I_{max} }{ I_{min} }$$

![[Pasted image 20240208095452.png]]
![[Pasted image 20240208095507.png]]

#### Equal Intensities 
If $I_{1} = I_{2} = I_{o}$,
$$
\begin{split}
I_{res} &= I_{o} + I_{o} + 2\sqrt{ I_{o}I_{o} }\cos \Delta \phi \\
&= 2I_{o}(1 + \cos \Delta \phi) \\
&= 4I_{o} \cos ^{2} \frac{ \Delta \phi }{ 2 } \\
&= 4I_{o} \cos ^{2} \left( \frac{ \pi }{ \beta }y \right) \\
\end{split}
$$

Thus, 
$$I \in [0, 4I_{o}]$$
The intensity of minima will be zero, and that of maxima will be 4 times that of source.

![[Pasted image 20240208094458.png]]









