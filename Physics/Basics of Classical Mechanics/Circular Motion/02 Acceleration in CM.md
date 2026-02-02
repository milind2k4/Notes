Links: [[03 Dynamics of CM]]
___
# Acceleration in CM

### Uniform Circular Motion
Speed is constant, but the direction of velocity changes, there is acceleration. 
This acceleration is responsible for change in direction only. 
Since the acceleration does not change the speed of particle, it must be directed perpendicular to the velocity. 

$$
\begin{split}
|d\vec{v}| &= | \vec{v}_{f} - \vec{v}_{i} | \\
&= \sqrt{ v_{f}^{2} + v_{i}^{2} - 2v_{i}v_{f}\cos \theta } \\
&= \sqrt{ v^{2} + v^{2} - 2v^{2}\cos d\theta } \\
&= v\sqrt{ 2(1-\cos d\theta) } \\
&= v\sqrt{ 2 \times 2 \sin ^{2} \frac{ d\theta  }{ 2 } } \\
|d\vec{v}| &= 2v\sin \frac{d\theta}{2} \\
\text{Since angle is small,} \\
|d\vec{v}| &= vd\theta 
\end{split} 
$$
Now acceleration,
$$|\vec{a}| = \frac{ |d\vec{v}| }{ dt } = v\frac{ d\theta }{ dt }$$
$$a_{c} = \upomega v$$
$$a_{c} = \upomega v = \upomega ^{2}R = \frac{ v^{2} }{ R }$$

This acceleration is called **Centripetal or Radial or Normal Acceleration** because it is always directed towards the centre and is always perpendicular to velocity since the velocity does not change its magnitude. 

The direction of this acceleration will always keep on changing, always pointed towards unit vector, $(-\cos \theta \hat{i} - \sin \theta \hat{j})$

We can also write $a_{c}$ as,
$$\vec{a}_{c} = \vec{\omega} \times (\vec{\omega} \times \vec{R})$$
which is a [[07 Vector Triple Product]]

![[Pasted image 20230622124118.png]]

### Non-Uniform Circular Motion

Position of particle, $\vec{R} = R\cos \theta \hat{i} + R\sin \theta \hat{j}$ with unit vector, $\cos \theta \hat{i} + \sin \theta \hat{j}$.

Thus a radially outward unit vector is $\cos \theta \hat{i} + \sin \theta \hat{j}$.
And a radially inward unit vector is $-\cos \theta \hat{i} - \sin \theta \hat{j}$.

Tangential unit vector in anti clockwise direction is $-\sin \theta \hat{i} + \cos \theta \hat{j}$. 

At some instant the angular velocity is $\vec{\omega} = \omega \hat{k}$ and angular acceleration is $\vec{\alpha} = \alpha \hat{k}$.

Velocity,
$$
\begin{split}
\vec{v} &= \frac{ d\vec{R} }{ dt } \\
&= R\left(  -\sin \theta \frac{ d\theta }{ dt } \hat{i} + \cos \theta \frac{ d\theta }{ dt } \hat{j}  \right) \\ 
&= \omega R ( -\sin \theta \hat{i} + \cos \theta \hat{j}) 
\end{split}
$$
this is along tangential direction with magnitude $\omega R$. 

Now Acceleration,
$$
\begin{split}
\vec{a} &= \frac{ d\vec{v} }{ dt } \\
&= \frac{ d(\omega R [-\sin \theta \hat{i} + \cos \theta \hat{j}]) }{ dt } \\
&= R\left[ \omega \left( -\cos \theta \frac{ d\theta }{ dt } \hat{i} - \sin \theta \frac{ d\theta  }{ dt } \hat{j} \right) + \frac{ d\omega }{ dt } (-\sin \theta \hat{i} + \cos \theta \hat{j}) \right] \\
\\
\vec{a} &= \omega^{2}R (-\cos \theta \hat{i} - \sin \theta \hat{j}) + \alpha R(\sin \theta \hat{i} + \cos \theta \hat{j}) 
\end{split}
$$
Now this acceleration has two parts,
$$
\vec{a} = \underbrace{ \omega^{2}R (-\cos \theta \hat{i} - \sin \theta \hat{j}) }_{ \text{centripetal acceleration} } + \underbrace{ \alpha R(\sin \theta \hat{i} + \cos \theta \hat{j}) }_{ \text{tangential acceleration} } 
$$

![[Pasted image 20230622130634.png]]

##### Centripetal Acceleration
$$\vec{a}_{c} = \omega^{2}R (-\cos \theta \hat{i} -\sin \theta \hat{j})$$
which is **Radially Inwards** or **Towards Centre** and has magnitude $a_{c} = \omega^{2}R$

##### Tangential Acceleration
$$\vec{a}_{t} = \alpha R (-\sin \theta \hat{i} + \cos \theta \hat{j})$$
which is responsible for change in speed or angular velocity and has magnitude $a_{t} = \alpha R$.
Now, 
if it is along velocity, speed will increase, angular velocity increases and thus $\vec{\omega} \parallel \vec{\alpha}$.
if it is against velocity, speed will decrease, angular velocity decreases and thus $\vec{\omega} \upharpoonleft \! \downharpoonright \vec{\alpha}$.

Only tangential acceleration is responsible for change in speed. And thus,
$$| \vec{a}_{t} | = \frac{ d| \vec{v} | }{ dt } $$
i.e. tangential acceleration is  the rate of change of speed. 
Vectorially,
$$\vec{a}_{t} = \vec{\alpha} \times \vec{R}$$


##### Net Acceleration 
$$\frac{ d\vec{v} }{ dt } = \vec{a} = \vec{a}_{c} + \vec{a}_{t}$$
$$a = \sqrt{ a_{c}^{2} + a_{t}^{2} }$$
At angle,
$$\theta = \tan ^{-1} \frac{ a_{t} }{ a_{c} }$$
from the radius. 

$$\phi = \tan ^{-1} \frac{ a_{c} }{ a_{t} }$$
from the tangent. 


