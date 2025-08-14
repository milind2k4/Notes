Links: [[00 Rigid Body Dynamics]]
___
# Rigid Body Dynamics
For two particles, we have reduced mass,
$$\mu = \frac{ m_{1}m_{2} }{ m_{1} + m_{2} }$$

#### Moment of Inertia 
Moment of inertia,
$$I = \sum m_{1}r_{1}^{2} = \int dm \, r^{2}$$

Perpendicular axis theorem,
$$I_{z} = I_{x} + I_{y}$$

Parallel axis theorem,
$$I = I_{com} + md^{2}$$

Radius of gyration,
$$
\begin{split}
I &= mk^{2} \\
k &= \sqrt{ \frac{ I }{ m } } 
\end{split}
$$

##### Uniform rod
Axis parallel to rod,
$$I = md^{2}$$

Perpendicular Axis passing through end of rod,
$$I = \frac{ ml^{2} }{ 3 }$$

Perpendicular axis passing through mid point,
$$I = \frac{ ml^{2} }{ 12 }$$

Axis at an angle passing through end of rod,
$$I = \frac{ ml^{2}\sin ^{2}\theta }{ 3 }$$

##### Ring
Perpendicular axis through centre,
$$I = mR^{2}$$

Axis along diameter,
$$I = \frac{ mR^{2} }{ 2 }$$

Tangential axis perpendicular to ring,
$$I = 2mR^{2}$$

Tangential axis in the same plane as ring,
$$I = \frac{ mR^{2} }{ 2 } + mR^{2}$$

##### Rectangular Plate
Axis passes through breadth,
$$I = \frac{ ml^{2} }{ 3 }$$

Axis passes through length,
$$I = \frac{ mb^{2} }{ 3 }$$

Axis passes through centre and is in the same plane and along breadth,
$$I = \frac{ ml^{2} }{ 12 }$$

Axis passes through centre and is in the same plane and along length,
$$I = \frac{ mb^{2} }{ 12 }$$

##### Square Plate
Axis in same plane passing through edge,
$$I = \frac{ ml^{2} }{ 3 }$$

Axis passes through centre in the same plane,
$$I = \frac{ ml^{2} }{ 12 }$$

Axis perpendicular to plane passing through vertex,
$$I = \frac{ 2ml^{2} }{ 3 }$$

Axis perpendicular to plane passing through centre,
$$I = \frac{ ml^{2} }{ 6 }$$

##### Cylinder

**Hollow Cylinder,** perpendicular axis passing through centre,
$$I = \frac{ mR^{2} }{ 3 } + \frac{ ml^{2} }{ 12 }$$

**Solid Cylinder,** perpendicular axis passing through centre,
$$I = \frac{ ml^{2} }{ 4 } + \frac{ ml^{2} }{ 12 }$$

##### Disk 
Perpendicular axis passing through centre,
$$I = \frac{ mR^{2} }{ 2 }$$

Axis along diameter,
$$I = \frac{ mR^{2} }{ 4 }$$

##### Sphere
**Hollow Sphere,** axis passing through centre,
$$I = \frac{ 2mR^{2} }{ 3 }$$

**Solid Sphere,** axis passing through centre,
$$I = \frac{ 2mR^{2} }{ 5 }$$

##### Cone 
**Hollow Cone,** axis passing through height,
$$I = \frac{ mR^{2} }{ 2 }$$

**Solid Cone,** axis passing through height,
$$I = \frac{ 3mR^{2} }{ 10 }$$

##### Solid Cube 
Axis passing through edge,
$$I = \frac{ 2ml^{2} }{ 3 }$$

Axis passing through body centre and face centres,
$$I = \frac{ ml^{2} }{ 6 }$$

#### Angular Momentum 
About a point,
$$\vec{L} = m(\vec{r}\times \vec{v})$$

About an axis,
$$\vec{L} = mvr_{\perp}$$

Of a body performing pure rotational motion,
$$\vec{L} = I\vec{\omega}$$

Angular Momentum Conservation theorem,
$$\vec{L}_{i} = \vec{L}_{f}$$
if there is no external torque. 

#### Torque 
About a point,
$$\vec{\tau} = \vec{r} \times \vec{f}$$

About an axis,
$$\vec{\tau} = r_{\perp}f$$

From angular momentum,
$$\vec{\tau} = \frac{ d\vec{L} }{ dt }$$

Force couple,
$$\vec{\tau} = \vec{l} \times \vec{f}$$

Newton's 2nd Law,
$$\vec{\tau} = I\vec{\alpha}$$

#### Angular Impulse 
$$AI = \int \vec{\tau} \, dt$$

In terms of impulse,
$$AI = Jr_{\perp}$$

Angular Impulse - Angular Momentum theorem,
$$AI = \vec{L}_{f} - \vec{L}_{i}$$

#### Combined Motion 
Kinetic Energy,
$$K = \frac{ 1 }{ 2 }mv^{2} + \frac{ 1 }{ 2 }I_{com}\omega^{2}$$

Instantaneous axis of rotation is the point about which the velocity is zero. Or we can draw lines parallel to the velocity at some points and where they meet will be the IAR. 

##### Pure Rolling
$$
\begin{split}
v_{p} &= v_\text{surface} \\
a_{p} &= a_\text{surface} \\
\end{split}
$$

**On a fixed surface,**
Velocity,
$$\omega R = v$$

Acceleration,
$$\alpha R = a$$

