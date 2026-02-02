Links: [[02 Acceleration in CM]]
___
# Dynamics of CM
### Centripetal Force
The force which provides centripetal acceleration. And it is always directed towards centre. 

$$f_{c} = ma_{c} = \frac{mv^{2}}{R} = mR\omega^{2}$$
$$\vec{f}_{c} = m(\vec{\omega} \times \vec{v})$$

This is not a force of it's own. It is a form of another force. 
For example, the tension in the string is acting as $f_{c}$ when an object is doing a circular motion. 
Hence, $\displaystyle T = \frac{mv^{2}}{R}$.

Without it an object cannot perform circular motion as it is responsible for changing  the direction of velocity. 

The work done and power by $f_{c}$ is zero as the displacement and velocity of the particle is always [[00 Work#Magnitude of Work|perpendicular to the force]].
Thus $f_{c}$ cannot change KE or speed. 

In a horizontal plane where there is no other force, the centripetal force is provided by [[00 Friction|friction]].

### Tangential Force
The force that provides tangential acceleration. It is either along or against the velocity and thus is responsible for changing the speed. Thus for UCM there is no tangential force.

$$\vec{f}_{t} = ma_{t} = m\alpha R = m \frac{ d(\text{speed}) }{ dt } $$
$$\vec{f}_{t} = m\vec{a}_{t} = m(\vec{\alpha} \times \vec{R})$$

It always acts tangential to the circle.

Power and thus work done by tangential force is +ve or -ve and thus it can increase or decrease the KE or speed. 


The net force is thus,
$$f_{net} = \sqrt{ f_{t}^{2} + f_{c}^{2} }$$
at an angle,
$$\theta = \tan ^{-1} \frac{ f_{t} }{ f_{c} }$$
from the radius.
$$\phi = \tan ^{-1} \frac{ f_{c} }{ f_{t} }$$
from the tangent.

In UCM, $f_{net} = f_{c}$.

### Centrifugal Force
It is the pseudo force applied to the moving object seen from a non inertial frame. This non inertial frame will be a rotating one in this case. 

This force is only applicable from rotating frame of reference. 
It is always acts radially outwards. 

$$\vec{f}_{cf} = -m\vec{a}_{o}$$
$$\vec{f}_{cf} = -m(\vec{\omega} \times \vec{v})$$
$$\vec{f}_{cf} = m(\vec{v} \times \vec{\omega})$$
Magnitude wise,
$$f_{cf} = ma_{c}$$

![[Pasted image 20230628133649.png]]

## Conical Pendulum
The tension in the string balances the gravity and it is the centripetal force which is required for circular motion.

There is no tangential force as both mg and T are perpendicular to velocity. 

Thus,
$$T\cos \theta = mg$$
$$T\sin \theta = \frac{ mv^{2} }{ R }$$

Dividing them, we get velocity,
$$v = \sqrt{ Rg\tan \theta }$$
$$v = \sqrt{ lg \frac{ \sin ^{2}\theta }{ \cos \theta } }$$

Angular velocity,
$$\omega = \frac{ v }{ R } = \sqrt{ \frac{ g }{ l\cos \theta } } = \sqrt{ \frac{g}{H} }$$

Now, time period,
$$t = \frac{ 2\pi }{ \omega  } = 2\pi \sqrt{ \frac{ H }{ g } }$$

![[Pasted image 20230623125245.png]]


If particles are at the same height, they will have the same time period and thus the same angular velocity. Now since the radius is different, as we increase the radius, the velocity increases. 

![[Pasted image 20230623130119.png]]

## Well of Death
If the bike is not moving, the wall does not push the bike and thus there is no normal and hence no static friction, and thus the bike falls down. 

The mg is balanced by static friction,
$$mg = f_{s}$$

The centripetal force is provided by normal,
$$N = \frac{ mv^{2} }{ R }$$

Now,
$$f_{s} = mg = \mu \frac{ mv^{2} }{ R }$$
Giving, velocity,
$$v \geq \sqrt{ \frac{ Rg }{ \mu } }$$

Thus minimum velocity so that the bike does not fall,
$$v_{min} =  \sqrt{ \frac{ Rg }{ \mu } }$$

Angular velocity,
$$\omega \geq \sqrt{ \frac{ g }{ \mu R } }$$

![[Pasted image 20230623131507.png]]

## Examples
Horizontal Smooth Chain, rotating with constant angular velocity, #important 

![[Pasted image 20230623133327.png]]
![[Pasted image 20230623133535.png]]
