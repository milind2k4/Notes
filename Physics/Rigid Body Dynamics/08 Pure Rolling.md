Links: [[07 Combine Motion]]
___
# Pure Rolling
It is also known as *rolling without slipping or skidding.*
Rolling is only defined for surface with circular cross section. 

There should be no relative motion along the surface between the surface and the point of contact of body. 

$$v_{P} = v_\text{surface}$$
$$a_{P} = a_\text{surface}$$

![[Pasted image 20230801154325.png]]

### Pure Rolling on Fixed Surface 
##### Velocity
The velocity of point of contact is zero,
$$\omega R = u$$
$$\omega = \frac{ u }{ R }$$
![[Pasted image 20230801160258.png]]

##### Acceleration 
The acceleration of point of contact is zero,
$$\alpha R = a$$
$$\alpha = \frac{ a }{ R }$$

![[Pasted image 20230801160317.png]]

##### Speed
The speed of any point can be found by,
$$
\begin{split}
v &= |\vec{v} + \vec{v}| \\
&= \sqrt{ 2v^{2} + 2v^{2}\cos(\pi - \theta) } \\
&= 2v\sin \frac{ \theta }{ 2 } \\
&= 2v\sin \frac{ \omega t }{ 2 }
\end{split}
$$
![[Pasted image 20230801162317.png]]

##### Displacement 
The displacement of each point is the same as that of COM for n number of rotations. The distance travelled however, is different for each point. 
$$s = 2n\pi R$$
where n is the number of rotations.

![[Pasted image 20230801161653.png]]

##### Distance Travelled
To find distance travelled, we integrate speed over time. 
$$d = \int_{0}^{t} 2v\sin \frac{ \omega t }{ 2 } \, dt$$

![[Pasted image 20230801162554.png]]

#### One Rotation 
For one rotation,
- Displacement of each particle:
	$$s = 2\pi R$$

- Distance travelled by point of contact,
  $$d = 8R$$

![[Pasted image 20230801162738.png]]

#### Pure Rolling on an Inclined Plane
The inclined plane is enough rough. We release an object of circular cross section of moment of inertia, $I_{com} = mk^{2}$ (k is radius of gyration) from height H.

Since it does pure rolling, at the base the angular velocity is $\omega = v /R$.

For acceleration of COM,
$$
\begin{split}
mg\sin \theta - f_{s} &= ma \\
f_{s}R &= mk^{2} \frac{a}{R} \\
\text{Giving,} \\
a &= \frac{ g\sin \theta R^{2} }{ R^{2} + k^{2} }
\end{split}
$$
Thus as $k$ increases, $a$ decreases. 


The displacement is,
$$s = \frac{ H }{ \sin \theta }$$

For velocity,
$$
\begin{split}
v^{2} &= 0^{2} + 2 \frac{ g\sin \theta R^{2} }{ R^{2} + k^{2} } \frac{ H }{ \sin \theta } \\
v &= \sqrt{ 2gh\frac{ R^{2} }{ R^{2} + k^{2} } } \\
\omega &= \sqrt{ \frac{ 2gh }{ R^{2} + k^{2} } } \\
\end{split}
$$
Translational kinetic energy,
$$TKE = \frac{ mgH R^{2} }{ R^{2} + k^{2} }$$
Thus the one having min. k will have max. TKE. 

Rotational Kinetic energy,
$$RKE = \frac{ mgHk^{2} }{ R^{2} + k^{2} } = \frac{ mgH }{ (R^{2} /k^{2}) + 1 }$$
Thus one having max. k will have max. RKE. 

The net kinetic energy,
$$KE = mgH$$
which is loss is potential. This result is enforced by the fact that $f_{s}$ does no work as the POAF of it has no displacement. 

Time taken to reach the base,
$$
\begin{split}
s &= ut + \frac{ 1 }{ 2 }at^{2} \\
\frac{ H }{ \sin \theta } &= \frac{ 1 }{ 2 } \frac{ g\sin \theta R^{2} }{ R^{2} + k^{2} }t^{2} \\
t &= \frac{ \sqrt{ R^{2} + k^{2} } }{ R\sin \theta } \sqrt{ \frac{ 2H }{ g } }
\end{split}
$$

Frictional force,
$$f_{s} = \frac{ mg\sin \theta k^{2} }{ R^{2} + k^{2} }$$
$$f_{s} = \frac{ mg\sin \theta }{ (R^{2} /k^{2}) + 1 }$$
Thus the more is $k$ the more is $f_{s}$.

Coefficient of frictional force,
$$
\begin{split}
f_{s} &\leq \mu N \\
\frac{ mg\sin \theta k^{2} }{ R^{2} + k^{2} } &\leq mg\cos \theta \\
\mu &\geq \frac{ \tan \theta k^{2} }{ R^{2} + k^{2} }
\end{split}
$$


![[Pasted image 20230808175858.png]]
![[Pasted image 20230808175915.png]]

Comparing all the objects with circular cross section, solid sphere will have max. acceleration and will reach the base first with maximum velocity and thus angular velocity. 

Pure rolling of ring on an inclined plane guarantees pure rolling of others. This is because it requires the most $\mu$.

We can do questions using TMEC also,
![[Pasted image 20230811154959.png]]