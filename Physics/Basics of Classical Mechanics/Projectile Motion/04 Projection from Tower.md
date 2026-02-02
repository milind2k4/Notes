Links: [[00 Projectile Motion]]
___
# Projection from Tower

## When projected along x-axis
Along x-axis,
> $$
> \begin{split}
> v_{x} &= u_{x} = u \\
> a_{x} &= 0 \\
> x &= ut 
> \end{split}
> $$

Along y-axis,
> $$
> \begin{split}
> u_{y} &= 0 \\
> a_{y} &= g \\
> v_{y} &= gt &= \sqrt{ 2gy } \\
> y &= \frac{1}{2}gt^{2}
> \end{split}
> $$

![[Pasted image 20230424120852.png]]

### Time of Flight
$$T = \sqrt{\frac{2h}{g}}$$

We can use,
> $$
> \begin{split}
> y &= \frac{1}{2}gt^{2} \\
> h &= \frac{1}{2}gT^{2} \\
> T &= \sqrt{ \frac{ 2h }{ g } }
> \end{split}
> $$

### Range
$$R = u\sqrt{ \frac{ 2h }{ g } }$$

We can use,
> $$x = ut = uT$$
for the whole flight.

### Striking Velocity
> $$v = u\ \hat{i} + \sqrt{2gh}\ \hat{j}$$
> $$v = \sqrt{u^{2} + 2gh}$$
this is always true.

And angle at which it strikes,
> $$\tan \theta = \frac{ v_{y} }{ v_{x} } = \frac{ \sqrt{ 2gh } }{ u }$$

## When projected up at an angle
These types of questions are best done by separating the initial velocity into it's components. 

Along x-axis,
> $$
> \begin{split}
> v_{x} &= u_{x} = u\cos \theta \\
> a_{x} &= 0 \\
> x &= (u\cos \theta) t 
> \end{split}
> $$

Along y-axis,
> $$
> \begin{split}
> u_{y} &= u\sin \theta \\
> a_{y} &= -g \\
> v_{y} &= u\sin \theta - gt \\
> v_{y} &= \sqrt{ u\sin \theta - 2gy } \\
> y &= (u\sin \theta) t - \frac{1}{2}gt^{2}
> \end{split}
> $$

![[Pasted image 20230424121837.png]]

### Time of Flight

$$
\begin{split}
y &= (u\sin \theta) t - \frac{1}{2}gt^{2} \\
-H &= u\sin \theta t - \frac{1}{2}gt^{2} \\
t &= \frac{ u\sin \theta + \sqrt{ u^{2}\sin ^{2}\theta + 2gh } }{ g } = T
\end{split}
$$

We can also think of this time as the sum of time taken to reach max height and time taken to fall to the ground which is just like horizontal projection, just that the h is different,

$$T = \frac{ u\sin \theta }{ g } + \sqrt{ \frac{ 2 \left( h + \frac{ u^{2}\sin ^{2} }{ 2g } \right) }{ g } }$$

### Striking Velocity

$$
\begin{split}
v &=  u\cos \theta \hat{i} - (\sqrt{ u^{2}\sin ^{2}\theta + 2gh }) \hat{j} \\
v &=  \sqrt{ u^{2}\cos ^{2} \theta + u^{2}\sin ^{2}\theta + 2gh } \\ 
v &=  \sqrt{ u^{2} + 2gh }
\end{split}
$$
This is the same as previous case. Thus, at every angle, the striking velocity is the same, 