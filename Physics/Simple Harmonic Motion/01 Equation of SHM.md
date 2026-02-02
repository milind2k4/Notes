Links: [[00 Simple Harmonic Motion]], [[01 Equations of Motion]]
___
# Equation of SHM

![[Pasted image 20230825155615.png]]

### x, v and a
$$\begin{split}
x & = A \sin (\omega t + \phi) \\
\\
v & = A \omega \cos (\omega t + \phi) \\
v & = \omega \sqrt{A^{2}-x^{2}} \\
\\
a & = -\omega ^{2}A \sin (\omega t + \phi )\\
a & = -\omega ^{2}x
\end{split}$$
Thus, $v$ is ahead of $x$ by a phase of $\displaystyle \frac{\pi}{2}$.

Thus, $a$ is ahead of $v$ by a phase of $\displaystyle \frac{\pi}{2}$.

$x$ and $a$ have phase difference of $\pi$. They are out of phase. 

![[Pasted image 20230825161347.png]]


### Differential Equation of SHM
> $$\begin{split}
> f & = -kx = ma \\
> a & = \frac{-k}{m} x \\
> \text{Let } & \frac{k}{m} = \omega ^{2} \\
> a & = -\omega ^{2} x \\
> \frac{d^{2}x}{dt^{2}} & = -\omega ^{2}x \\\\
> \frac{d^{2}x}{dt^{2}} + \omega ^{2}x &= 0 
> \end{split}$$

If we have to prove that an equation is SHM or not, we check if it satisfies this equation. #important 

### Velocity
> $$\begin{split}
> a & = v \frac{dv}{dx} = \frac{-k}{m}x \\
> \\
> v dv & = \frac{-k}{m} xdx \\
> \\
> \int_{0}^{v} vdv & = \frac{-k}{m} \int_{A}^{x} xdx \\
> \\
> v^{2} & = \frac{-k}{m} (x^{2} - x^{2}) \\
> \\
> v & = \omega \sqrt{A^{2} - x^{2}}\\
> \end{split}$$

### Displacement
> $$\begin{split}
> \frac{dx}{dt} & = \omega \sqrt{A^{2} - x^{2}} \\
> \frac{dx}{\sqrt{A^{2} - x^{2}}} & = \omega dt \\
> \int \frac{dx}{\sqrt{A^{2} - x^{2}}} & = \omega \int dt \\
> \sin^{-1} \frac{x}{A} & = \omega t + \phi \\\\
> x & = A \sin (\omega t +\phi )
> \end{split}$$

### General solution
> $$\frac{d^{2}x}{dt^{2}} + \omega ^{2}x = 0 \implies x  = A \sin (\omega t +\phi)$$

Here, 
$A \to$Amplitude
$\omega t + \phi \to$ phase. 
$\omega \to$ Angular frequency with unit, $\ce{ rad\ s^{-1} }$

Thus we can write, 
$$\omega = \frac{2\pi}{T}$$
$$\omega = 2\pi f$$

$\phi \to$ phase constant or initial phase. It tells location at $t=0$. 
To find the initial position, put $t = 0$ and evaluate the expression. From here we can find $\phi$.

#### From Position
From the expression of position, velocity,
> $$\begin{split}
> x & = A \sin (\omega t + \phi) \\
> \frac{dx}{dt} & = A \omega \cos (\omega t + \phi) \\
> v & = A \omega \cos (\omega t + \phi) \\
> \\
> v & = A \omega \sqrt{1-\sin^{2} (\omega t + \phi)} \\
> v & = A \omega \sqrt{1- \frac{x^{2}}{A^{2}}} \\
> v & = \omega \sqrt{A^{2} - x^{2}} \\
> \end{split}$$

Both $v = +A \omega$ and $v = -A \omega$ are at the mean position. 

From the expression for velocity, acceleration, 
> $$\begin{split}
> v & = A \omega \cos (\omega t + \phi) \\
> \frac{dv}{dt} & = -A \omega ^{2} \sin (\omega t + \phi) \\
> a & = -A \omega ^{2} \sin (\omega t + \phi) \\
> a & = - \omega^{2} x \\
> \frac{d^{2}x}{dt^{2}} & = -\omega ^{2}x
> \end{split}$$
