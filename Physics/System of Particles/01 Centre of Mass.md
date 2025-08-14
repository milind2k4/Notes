Links: [[00 System of Particles]]
___
# Centre of Mass (COM)
It is the point representation of an extended body. 
If $f_{ext}$ is acting at COM, it will have same translational motion as that of the entire large body. 

This COM can be real or virtual. Real is when there is actual mass there, and virtual when there is no mass. 

To study translational motion of a large body, we assume its entire mass to be concentrated at a single point, which will be COM. 

### Definitions
#### Mass Moment
It is product of mass and the position vector of the mass. 
$$MM = m \vec{r}$$

It is a vector with direction the same as $\vec{r}$, i.e. position vector. 
Its has unit $\ce{ km m }$ and dimensions $\ce{ [ML] }$. 

![[Pasted image 20230629132527.png]]

#### Linear Momentum
[[01 Newton's Laws#2nd Law Law of Acceleration]]

aka simply, **Momentum**

$$\vec{P} = m\vec{v}$$
the direction is along velocity.

## COM of [[01.1 Discrete particles]]

## COM of Continuous Bodies
Here instead of summing, we integrate. 

$$\vec{r}_{com} = \frac{ \int dm \, \vec{r}  }{ \int  \, dm  }$$

$$\int  \, dm = M$$

We can find the separate coordinates also,
$$x_{com} = \frac{ \int dm \, x  }{ \int  \, dm  }$$
$$y_{com} = \frac{ \int dm \, y  }{ \int  \, dm  }$$
$$z_{com} = \frac{ \int dm \, z  }{ \int  \, dm  }$$

### [[01.3 Linear Bodies]]

### [[Physics/System of Particles/01.2 Flat Bodies]]

### [[01.4 Solid Bodies]]

## COM of Objects with Cavity
Cavity is empty space in the object.

We break off the cavity with -ve of the $\sigma$ or density as shown. We consider the COM of this -ve mass as $(x_{1},y_{1})$ and then use the formula for [[01.1 Discrete particles#2 point masses]]

We get,
$$x_{com} = \frac{ (\sigma A)x + (-\sigma A_{1})x_{1} }{ \sigma A + (-\sigma A_{1}) }$$


$$x_{com} = \frac{ Ax - A_{1}x_{1} }{ A-A_{1} }$$
$$y_{com} = \frac{ Ay - A_{1}y_{1} }{ A-A_{1} }$$

![[Pasted image 20230701124419.png]]

We can extend this to a system with more than one cavity also,
$$x_{com} = \frac{ Ax - A_{1}x_{1} - A_{2}x_{2} }{ A - A_{1} - A_{2} }$$
$$y_{com} = \frac{ Ay - A_{1}y_{1} - A_{2}y_{2} }{ A - A_{1} - A_{2} }$$

#### [[Physics/System of Particles/06 Examples#COM]]