Links: [[00 Circular Motion]], [[03 Dynamics of CM]]
___
# Turning of Vehicle
At any turn the vehicle performs a circular motion. The centripetal force for the motion is provided by friction or banking of the road.

### Friction only
$\mu$ is the coefficient of friction between the tires and the road. 
It is static friction as the tires are rolling on the road and not sliding.

From the ground,
$$
\begin{split}
a_{c} &= \frac{v^{2}}{R} \\
f_{s} &= \frac{ mv^{2} }{ R } \\
\text{Now, we know that,} \\ 
f_{s} &\leq \mu mg \\
\frac{mv^{2}}{R} &\leq \mu mg \\
v &\leq \sqrt{ \mu gR }  
\end{split}
$$

Alternatively, from the car,
$$
\begin{split}
f_{cf} &= f_{s} \\
\frac{mv^{2}}{R} &= f_{s} \leq \mu mg \\
v &= \sqrt{ \mu gR } 
\end{split}
$$

Thus, if the car is moving at a velocity $v$, and
- $$v \leq \sqrt{ \mu gR }$$
	the car will turn safely. 

- $$v > \sqrt{ \mu gR }$$
	then the car will slip outwards. 

![[Pasted image 20230628134358.png]]

### Banking only
The outer side of the road is elevated. The angle at which the road is banked is called banking angle. 

If the car is moving with velocity $v$ and the road is banked at an angle, $\theta$,

From the ground,
$$
\begin{split}
N\cos \theta &= mg \\
N\sin \theta &= \frac{mv^{2}}{R} \\
mg\tan \theta &= \frac{ mv^{2} }{ R } \\
v &= \sqrt{ Rg\tan \theta }
\end{split}
$$

![[Pasted image 20230628135309.png]]

From the car,
$$
\begin{split}
N\cos \theta &= mg \\
N\sin \theta &= \frac{mv^{2}}{R} \\
v &= \sqrt{ Rg\tan \theta }
\end{split}
$$

![[Pasted image 20230628135523.png]]

Thus if the car is moving with velocity $v$,
- $$v < \sqrt{ Rg\tan \theta }$$
then it will slip inwards.

- $$v = \sqrt{ Rg\tan \theta }$$
then it will turn not slip.

- $$v > \sqrt{ Rg\tan \theta }$$
then it will slip outwards.

### Banking with Friction
Here we observe that if $v = \sqrt{ Rg\tan \theta }$ then there will be no friction. If is is more however, there will be tendency to slip outwards and the friction will oppose this tendency. 

From the Car, for max. velocity, the friction will be max and act inwards,
$$f_{s(max)} = \mu N$$

Now,
$$
\begin{split}
N\cos \theta &= mg + \mu N\sin \theta \\
N\sin \theta + \mu N\cos \theta &= \frac{ mv_{max}^{2} }{ R } \\
\text{Dividing them,} \\
\frac{ \mu \cos \theta + \sin \theta }{ \cos \theta - \mu \sin \theta } &= \frac{ v_{max}^{2} }{ Rg } \\
\text{Dividing by } \cos \theta, \\
v_{max} &= \sqrt{ Rg \left( \frac{ \tan \theta + \mu }{ 1 - \mu \tan \theta } \right) }
\end{split}
$$

![[Pasted image 20230628140446.png]]

From the Car, for min. velocity, the friction will be max and act outwards,
$$f_{s(max)} = \mu N$$

Now,
$$
\begin{split}
N(\cos \theta + \mu \sin \theta) &= mg \\
N(\sin \theta - \mu \cos \theta) &= \frac{ mv_{min}^{2} }{ R } \\ 
\frac{ \sin \theta - \mu \cos \theta }{ \cos \theta + \mu \sin \theta } &= \frac{ v_{min}^{2} }{ Rg } \\
v_{min} &= \sqrt{ Rg \left( \frac{ \sin \theta - \mu \cos \theta  }{ \cos \theta + \mu \sin \theta } \right) } \\
\text{Dividing by } \cos \theta, \\ 
v_{min} &= \sqrt{ Rg \left( \frac{ \tan \theta - \mu }{ 1 + \mu \tan \theta } \right) }
\end{split}
$$

![[Pasted image 20230629113219.png]]

Thus the speed should be,
$$\sqrt{ \frac{ Rg( \tan \theta - \mu )}{ 1 + \mu \tan \theta } } \leq v \leq \sqrt{ \frac{ Rg( \tan \theta + \mu )}{ 1 - \mu \tan \theta } }$$

$$v_{min} \leq v \leq v_{max}$$
for no slipping. 

If $v < v_{min}$, the car will slip inwards and if $v > v_{max}$, the car will slip outwards. 