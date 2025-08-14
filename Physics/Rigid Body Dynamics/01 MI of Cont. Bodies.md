Links: [[00 Rigid Body Dynamics]]
___
#  Moment of Inertia of Continuous Bodies
### [[01.1 Linear Bodies]]

### [[01.2 Planar Bodies]]

### [[01.3 Solid Bodies]]

## Perpendicular Axis Theorem
It is only valid for planar (i.e. 1d or 2d) bodies.

Two axes x and y are taken which are perpendicular to each other and in the same plane as that of object. 

A third axis z is taken perpendicular to the plane containing the object. 

The theorem says that,
$$I_{z} = I_{x} + I_{y}$$

**Proof:**
> Consider a small mass dm at position $(x,y)$, then
> $$I_{x} = \int dm \, y^{2} $$
> $$I_{y} = \int dm \, x^{2} $$
> Giving,
> $$I_{x} + I_{y} = \int dm \, (x^{2} + y^{2})$$
> Now, this mass is at distance $\sqrt{ x^{2} + y^{2} }$ form the z axis, thus giving,
> $$I_{z} = \int dm \, (x^{2} + y^{2})$$
> That is,
> $$I_{z} = I_{x} + I_{y}$$ 

![[Pasted image 20230711123124.png]]

## Parallel Axis Theorem 
This theorem is applicable on every body. 

If MI about COM is known and we have to find MI about an axis d distance away from the COM axis and parallel to it.
$$I = I_{com} + md^{2}$$

![[Pasted image 20230711130444.png]]


## MI of Objects with Cavity
We complete the object and then find its MI. Then find the MI of the cavity assuming there is mass in the cavity. 

Finally subtract the MI of the cavity from that of the whole shape. 

$$I = I_{+} + I_{-}$$

![[Pasted image 20230712165909.png]]
![[Pasted image 20230712165926.png]]

For solid bodies its the same deal,
![[Pasted image 20230712171225.png]]
![[Pasted image 20230712171237.png]]





