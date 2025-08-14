Links: [[03 Spherical Mirror]]
___
# Velocity of Image for Spherical Mirror
[[00 Geometrical Optics#Velocity of Image]]

- **Note:**
	- $v \to \text{velocity}$
	- $v_{i} \to \text{velocity of image}$
	- $v_{o} \to \text{velocity of object}$
	- $v_{m} \to \text{velocity of mirror}$
	- $\text{v} \to \text{position of image}$
	- $\text{u} \to \text{position of object}$

> $$\text{v}^{-1}  + \text{u}^{-1} = f^{-1} $$
## O is moving along principal axis

Differentiating with respect to time, 
> $$
> \begin{split}
> - \frac{1}{\text{v}^{2}} \frac{d\text{v}}{dt} -\frac{1}{\text{u}^{2}}\frac{d\text{u}}{dt} &= 0 \\
> \frac{d\text{v}}{dt} &= - \frac{\text{v}^{2}}{\text{u}^{2}} \frac{d\text{u}}{dt} \\ 
> v_{im} &= -\frac{\text{v}^{2}}{\text{u}^{2}} v_{om} \\
> v_{i} - v_{m} &= -\frac{\text{v}^{2}}{\text{u}^{2}} (v_{o} - v_{m}) \\
> \end{split}
> $$

From [[06 Magnification#Lateral Magnification Formula|magnification formula]],
> $$
> \begin{align}
> m_{t}  & = \frac{-\text{v}}{\text{u}} \\
> m_{t}^{2} &= \frac{\text{v}^{2}}{\text{u}^{2}}
> \end{align}
> $$

Therefore,

> $$
> \begin{align}
> v_{im} &= -\frac{\text{v}^{2}}{\text{u}^{2}} v_{om} \\
> v_{im} &= -m_{t}^{2}v_{om} = m_{l}v_{om}
> \end{align}
> $$

If $v_{m} = 0$,

> $$
> \begin{align}
> v_{i} &= -\frac{\text{v}^{2}}{\text{u}^{2}} v_{o} \\
> v_{i} &= -m_{t}^{2}v_{o} = m_{l}v_{o}
> \end{align}
> $$

 - W.r.t mirror the velocities of Image and Object are opposite. 

## O is moving $\perp$ to principal axis
> $$
> \begin{align}
> \frac{y_{i}}{y_{o}} &= m &&\\
> y_{i} &= m \cdot y_{o}
> \end{align}
> $$

Differentiating with respect to time, 
> $$
> \begin{split}
> \frac{dy_{i}}{dt} &= m \cdot \frac{dy_{o}}{dt} \\
> v_{i\perp} &= mv_{o\perp}\\
> \end{split}
> $$

Using magnification formula,
> $$
> \begin{split}
> v_{i\perp} &= \frac{-v}{u}v_{o\perp}\\
> v_{i\perp} &= \frac{f}{f-u}v_{o\perp}\\
> \end{split}
> $$

This shows that the farther the image, the bigger and the faster. 

## O is moving in a generic direction 
$v_{x}$ will be the same as along the PA,
> $$v_{ix} = -\left( \frac{f}{f-u} \right)^{2}v_{ox}$$

But there will be some $v_y$ also,
> $$
> \begin{split}
> y_{i} &= m y_{o} = \left( \frac{f}{f-u} \right)y_{o}\\\\
> 
> \frac{dy_{i}}{dt} &= \frac{d\left( \displaystyle \frac{f}{f-u} \right)y_{o}}{dt} = f \cdot \frac{d \left( \frac{y_{o}}{f-u} \right)}{dt }\\\\
> 
> v_{iy} &=  f \left\{ \frac{ \displaystyle (f-u) \frac{dy_{o}}{dt} + y_{o} \frac{du}{dt}}{(f-u)^{2}} \right\} \\\\
> 
> v_{iy} &= f \left[ \frac{(f-u)\ v_{oy} + y_{o}\ v_{ox}}{(f-u)^{2}} \right]
> \end{split}
> $$

Therefore, 

> $$
> \begin{split}
> v_{iy} & = f\ \left[ \frac{(f-u)\ \cdot v_{o y} + y_{o}\ \cdot v_{o x}}{(f-u)^{2}} \right] \\
> v_{ix} & = -\left( \frac{f}{f-u} \right)^{2}v_{ox}
> \end{split}
> $$