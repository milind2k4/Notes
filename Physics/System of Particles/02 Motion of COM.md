Links:  [[01 Centre of Mass]]
___
# Motion of COM
$$\vec{r}_{com} = \frac{ \sum m_{1} \vec{r}_{1} }{ \sum m_{1} }$$

#### Displacement
Differentiating $\vec{r}_{com}$ independently,
$$d\vec{r}_{com} = \frac{ \sum m_{1}d\vec{r}_{1} }{ \sum m_{1} }$$

For bigger displacement,
$$\Delta \vec{r}_{com} = \frac{ \sum m_{1}\Delta \vec{r}_{1} }{ \sum m_{1} }$$

We can also write it in  component form,
$$\Delta x_{com} = \frac{ \sum m_{1}\Delta x_{1} }{ \sum m_{1} }$$
$$\Delta y_{com} = \frac{ \sum m_{1}\Delta y_{1} }{ \sum m_{1} }$$
$$\Delta z_{com} = \frac{ \sum m_{1}\Delta z_{1} }{ \sum m_{1} }$$

#### Velocity 
Differentiating $\vec{r}_{com}$ wrt time,
$$\frac{ d\vec{r}_{com} }{ dt } = \frac{ \displaystyle \sum  m_{1} \frac{ dr_{1} }{ dt } }{ \sum m_{1} }$$
$$\vec{v}_{com} = \frac{ \sum m_{1}\vec{v}_{1} }{ \sum m_{1} }$$

Using Momentum,
$$\vec{v}_{com} = \frac{ \sum \vec{P}_{1} }{ M }$$
$$\vec{v}_{com} = \frac{ \vec{P}_{sys} }{ M }$$

##### Momentum
The net momentum of system can thus be found as,
$$\vec{P}_{sys} = M\vec{v}_{com}$$

To find momentum of a continuous body, we use the same method as we used to calculate COM, i.e. take element, find momentum for that element, then integrate.

![[Pasted image 20230701135659.png]]

Alternatively, we use circular motion and write the velocity of COM, and then multiply it with mass to get momentum,
![[Pasted image 20230701135918.png]]

#### Acceleration 
Differentiating $\vec{v}_{com}$ wrt time,
$$\frac{ d\vec{v}_{com} }{ dt } = \frac{ \displaystyle \sum m_{1}\frac{ d\vec{v}_{1} }{ dt }  }{ \sum m_{1} }$$
$$\vec{a}_{com} = \frac{ \sum m_{1}\vec{a}_{1} }{ \sum m_{1} }$$

Using force,
$$\vec{a}_{com} = \frac{ \sum \vec{f}_{1} }{ M }$$
$$\vec{a}_{com} = \frac{ \vec{f}_{net} }{ M }$$
$$\vec{a}_{com} = \frac{ \vec{f}_{in} + \vec{f}_{ext} }{ M }$$


Now, by [[01 Newton's Laws#3rd Law Action & Reaction|newtons third law,]] $\vec{f}_{1}$ contains the force one 1 by 2 and $\vec{f}_{2}$ contains the force on 2 by 1. These are equal in magnitude and opposite in direction and thus cancel out. Therefore we can write,

$$\vec{a}_{com} = \frac{ \vec{f}_{ext} }{ M }$$

Thus, *acceleration of COM is independent of internal forces.* It is dependent on external forces only. Thus *motion of COM is always external force dependent.* 

##### Force
$$\vec{f}_{ext} = \vec{a}_{com}M$$

#### [[Physics/System of Particles/06 Examples#When COM is not fixed]]