Links: [[00 Gravitation]]
___
# Field and Potential 
## Gravitational Field Intensity
Just like we did with [[02 Electric Field|Electric field]] intensity, we will put a test mass near the mass and find the force on it. 

$$\vec{E}_{g} = \frac{ \vec{f}_{g} }{ m_{o} }$$
Its unit is N/kg and it is a vector. 

Thus we have,
$$\vec{f}_{g} = m\vec{E}_{g}$$
Since mass is always +ve, the force is in the direction of the field. 

![[Pasted image 20231217122658.png]]

### Gravitational Field due to Various Objects
We will directly use results from [[02 Electric Field#Electric Fields due to Various Objects]].


#### Point Mass
$$
\begin{split}
f_{g} &= \frac{ GMm_{o} }{ r^{2} } \\
E_{g} &= \frac{ GM }{ r^{2} }
\end{split}
$$

It is always radially inwards, i.e. M acts like -ve charge.

In vector form,
$$\vec{E}_{g} = -\frac{ GM }{ r^{3} } \vec{r}$$

![[Pasted image 20231217122709.png]]

![[Pasted image 20231217123128.png]]

#### Uniform Ring
[[02.1 Ring and Disk]]

$$E_{g} = \frac{ GMx }{ (R^{2} + x^{2})^{3/2} }$$

If $x \ll R$,
$$E_{g} = \frac{ GMx }{ R^{3} }$$

As $x \to 0$ or $x \to \infty$, $E_{g} \to 0$.

$E_{g}$ will be max when $x = R /\sqrt{ 2 }$.

![[Pasted image 20231217123433.png]]

#### Uniform Disk
[[02.1 Ring and Disk]]

$$E_{g} = 2\pi G \sigma (1 - \cos \theta)$$
In terms of mass,
$$E_{g} = \frac{ 2Gm }{ R^{2} } \left( 1 - \frac{ x }{ \sqrt{ R^{2} + x^{2} } } \right)$$

![[Pasted image 20231217123732.png]]

#### Uniform Long Wire
[[03.2 Wire]]

$$E_{g} = \frac{ 2G\lambda }{ r }$$

![[Pasted image 20231217123841.png]]

#### Infinitely Large Sheet
[[03.2 Wire#Infinitely Large Sheet]]

We can use result from uniform disk when $R \to \infty$,

$$E_{g} = 2\pi G \sigma$$

![[Pasted image 20231217124210.png]]

#### Uniform Sphere
[[03.3 Sphere]]

##### Hollow Sphere 
$$
\begin{split}
E_{g,in} &= 0 \\
E_{g,out} &= \frac{ GM }{ r^{2} }
\end{split}
$$

![[Pasted image 20231217124406.png]]

##### Solid Sphere 
#important 

Solid Sphere is akin to planet. 

$$
\begin{split}
E_{g,in} &= \frac{ GMr }{ R^{3} } \\
E_{g,out} &= \frac{ GM }{ r^{2} } 
\end{split}
$$

![[Pasted image 20231217124853.png]]

![[Pasted image 20231217125502.png]]

## Gravitational Potential 
Just like in [[04 Electrostatic Potential]].

We bring a test mass from $\infty$ to point P and find the work done by external force per unit mass.

$$V_{g,p} = \frac{ W_{ext}(\infty \to P)_{\Delta K = 0} }{ m_{o} } = \frac{ -W_{g}(\infty \to P) }{ m_{o} }$$
Thus,
$$V_{g,p} = \frac{ W_{g}(P \to \infty) }{ m_{o} }$$

$V_{g}$ is a scalar and is considered zero at infinity. 
Since gravitational  force is attractive, at point P, potential will be -ve. 

Unit is Joule/kg and dimensions are $\ce{ L^{2} T^{-2} }$

### Potential due to Various Objects 
#### Point Mass 
[[04 Electrostatic Potential#V due to Point Charge]]

$$V = \frac{ -GM }{ r }$$

![[Pasted image 20231217131816.png]]

#### Ring
[[04 Electrostatic Potential#Potential due to Ring]]

$$V = \frac{ -GM }{ \sqrt{ R^{2} + x^{2} } }$$

![[Pasted image 20231217132035.png]]

#### Uniform Disk
[[04 Electrostatic Potential#Potential due to Uniform Disk]]

$$V = \frac{ -2GM }{ R^{2} } (\sqrt{ R^{2} + x^{2} } - x)$$
Rationalising it,
$$V = \frac{ -2GM }{ \sqrt{ R^{2} + x^{2} } + x }$$

![[Pasted image 20231217132259.png]]
![[Pasted image 20231217132358.png]]

#### Sphere
[[04 Electrostatic Potential#Potential Due to Sphere]]

##### Hollow Sphere
$$
\begin{split}
V_{in} &= \frac{ -GM }{ R } \\
V_{out} &= \frac{ -GM }{ r }
\end{split}
$$

![[Pasted image 20231217132532.png]]

##### Solid Sphere 
#important 

$$
\begin{split}
V_{in} &= \frac{ -GM }{ 2R^{3} }(3R^{2} - r^{2}) \\
V_{out} &= \frac{ -GM }{ r^{2} }
\end{split}
$$

![[Pasted image 20231217132706.png]]

### Gravitational Potential Energy 
The potential of interaction between two masses.
$$U_{g} = m. V_{g}$$
