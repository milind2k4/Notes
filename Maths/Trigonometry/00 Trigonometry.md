Links: [[01 Identities]]
___
# Trigonometry
## Angle Measurement Systems
### Sexagesimal system
One right angle is divided into 90 equal parts and each part is called a degree. $1^{\circ}$

One degree is divided into 60 equal parts and each part is called a minute. $1  ^{\circ} = 60'$
One minute is divided into 60 equal parts and each part is called a second. $1' = 60''$

### Circular (Radian) system
Angle made by an arc made by an arc of length equal to its radius at the centre is called a radian. $1 ^{c}$
Thus, $\displaystyle \theta = \frac{l}{r}$ where $l$ is the arc length. 

For a given angle, if $D$ is degree measurement and $C$ is radian measurement, then,
$$\frac{D}{180} = \frac{C}{\pi }$$


## Misc. Notes
- The value of $\pi$ is $3.14$ and not $\displaystyle \frac{22}{7}$. 

- Cord length which subtends and angle $\theta$ at the centre:
  $$AB = 2r \sin \frac{\theta}{2}$$

- Area of triangle having a chord: 
  $$A  = \frac{1}{2}r^{2}\sin \theta$$

- Area of sector: 
  $$A = \frac{1}{2}r^{2} \theta$$

- Sum of internal angles of a convex polygon (i.e. sum of n angles) $=(n-2) \pi$

- Sum of external angles of a convex regular polygon (i.e. sum of n angles) $=(n+2)\pi$

- Radius of a circle inscribed in a polygon, i.e. **inradius** 
  $$r = \frac{a}{2} \cot \left( \frac{\pi}{n} \right)$$

- Radius of a circle which circumscribes a polygon i.e. **circumradius** 
  $$r = \frac{a}{2} \csc \left( \frac{\pi}{n} \right)$$

- Area of polygon, 
  $$A = \frac{ na^{2} }{ 4 }\cot \frac{ \theta  }{ 2 }$$

- Number of diagonal $=\displaystyle \frac{n(n-3)}{2}$
$\\$

- Angles which are multiples of $\pi$ are on the x-axis.
- Angles which are odd multiples of $\pi / 2$ are on the y-axis.
- Angles corresponding to $+ve$ x-axis will be $2n \pi$
- Angles corresponding to $-ve$ x-axis will be $(2n+1)\pi$
- Angles corresponding to $+ve$ y-axis will be $\displaystyle (4n+1) \frac{\pi}{2}$ or $\displaystyle (4n-3) \frac{\pi}{2}$
- Angles corresponding to $-ve$ y-axis will be $\displaystyle (4n-1) \frac{\pi}{2}$ or $\displaystyle (4n+3) \frac{\pi}{2}$

	![[Sign of T func.png]]

## Table of Trig Values

| Angle/Function | $$0$$     | $$\frac{\pi}{6}$$      | $$\frac{\pi}{4}$$      | $$\frac{\pi}{3}$$      | $$\frac{\pi}{2}$$ |
| -------------- | --------- | ---------------------- | ---------------------- | ---------------------- | ----------------- |
| $$\sin$$       | $$0$$     | $$\frac{1}{2}$$        | $$\frac{1}{\sqrt{2}}$$ | $$\frac{\sqrt{3}}{2}$$ | $$1$$             |
| $$\cos$$       | $$1$$     | $$\frac{\sqrt{3}}{2}$$ | $$\frac{1}{\sqrt{2}}$$ | $$\frac{1}{2}$$        | $$0$$             |
| $$\tan$$       | $$0$$     | $$\frac{1}{\sqrt{3}}$$ | $$1$$                  | $$\sqrt{3}$$           | Undefined         |
| $$\cot$$       | Undefined | $$\sqrt{3}$$           | $$1$$                  | $$\frac{1}{\sqrt{3}}$$ | $$0$$             |
| $$\sec$$       | $$1$$     | $$\frac{2}{\sqrt{3}}$$ | $$\sqrt{2}$$           | $$2$$                  | Undefined         |
| $$\csc$$       | Undefined | $$2$$                  | $$\sqrt{2}$$           | $$\frac{2}{\sqrt{3}}$$ | $$1$$             |

### Domain Range
[[04 Graphs of Trigonometric Functions#Table of Domain, Range, Period & Roots]]

## Points to Remember
- $\sin\ \&\ \cos$ are always defined. 
- $\csc\ \&\ \cot$ are undefined at $n\pi$
- $\tan\ \&\ \sec$ are undefined at $\displaystyle (2n+1)\frac{\pi}{2}$
- $\displaystyle \frac{1}{\sec x}= \cos x\ \forall\ x \neq (2n+1) \frac{\pi}{2}.$
- $\displaystyle \frac{1}{\csc x}= \sin x\ \forall\ x \neq n\pi.$


### Trig Manipulations
IF we see something like $\sin ^{2} + 2 \sin$ then we should add and subtract 1 to make a perfect square.

### Some Misc. Results
$$
\begin{split}
x &> \sin x,\ \forall\ x \in R^{+} \\
x &< \sin x,\ \forall\ x \in R^{-} \\
|x| &> |\sin x|,\ \forall\ x \in R - \{ 0 \} \\
\left| \frac{ \sin x }{ x } \right| &< 1,\ \forall\ x \in R - \{ 0 \} \\
\end{split}
$$
$\sin x = x$ has only one solution i.e. $x = 0$.

$\tan x = x$ has infinite solutions. 

$$
\begin{split}
\tan x &> x, \ \forall\ x \in \left( 0, \frac{\pi}{2} \right) \\
\tan x &< x, \ \forall\ x \in \left( -\frac{\pi}{2}, 0 \right) \\ 
|\tan x| &> |x|, \ \forall\ x \in \left( - \frac{ \pi }{ 2 }, \frac{ \pi }{ 2 } \right) \\
|\frac{ \tan x }{ x }| &> 1, \ \forall\ x \in \left( - \frac{ \pi }{ 2 }, \frac{ \pi }{ 2 } \right) 
\end{split}
$$

For $x \in (0, \pi /2)$, 
$$\sin x < x < \tan x$$
![[Pasted image 20230809092750.png]]

For [[00 Inverse Trigonometric Functions|inverse trig functions]],
In $x \in (0,1)$,
$$\sin ^{-1}x > x > \tan ^{-1} x$$
![[Pasted image 20230809093207.png]]

[[02 Formula and Expansions#Expansions|Expansion of cos,]]
$$\cos x = 1 - \frac{ x^{2} }{ 2! } + \frac{ x^{4} }{ 4! } - \frac{ x^{6} }{ 6! } + \dots$$
This gives,
$$\cos x \geq 1 - \frac{ x^{2} }{ 2 },\ \forall\ x \in R$$
And $\cos x = 1 - x^{2} /2$ has only one solution i.e. $x = 0$.
![[Pasted image 20230809092907.png]]
