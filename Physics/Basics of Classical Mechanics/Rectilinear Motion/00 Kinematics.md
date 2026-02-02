Links: [[01 Equations of Motion]]
___
# Kinematics: Definitions
Kinematics is the branch of physics in which we study the motion of objects and not the cause. 

##### Misc. Notes
- When there is a cardinal direction mentioned in the question (like North), then find the acceleration in terms of cardinal directions (like a = 5 $\ce{ m s^{-2} }$ towards South)
- When calculating distance travelled for straight line path with turning back, be careful to include the path before turn twice. (**5 + 5** + 20) 
- Subtract final from initial

#### Rest and Motion
- Properties of object as well as observer.
- Same object can be in rest and motion depending on the observer.
- If position of object with respect to observer remains unchanged then the object is at rest, w.r.t observer. 
- If position of object with respect to observer changes then the object is in motion, w.r.t observer. 


### Position
A vector which locates the object w.r.t observer. 
Generally, it is w.r.t ground.
Represented by $\vec{r}$.

- Vector: Tail at observer, Head at object
- Unit: meter (m)
- Dimensions: $\ce{ [L] }$

### Displacement
Change in position (vector).

$$\vec{s} = \vec{r_{f}} - \vec{r_{i}}$$
$$\vec{r_{f}} = \vec{r_{i}} + \vec{s}$$

- Vector: Tail at initial position, Head at final position
- Magnitude is the shortest distance between $i$ and $f$
- Does not depend on path: only on $i$ and $f$
- $\vec{s}=0$ for a closed path
- Unit: meter (m)
- Dimensions: $\ce{ [L] }$

### Distance
Length of the actual path taken. 

- Scalar
- Always equal to or more than the magnitude of displacement
- Equal when we travel in straight line without turning back
- Unit: meter (m)
- Dimensions: $\ce{ [L] }$

### Velocity
Rate of change of position.

We only take components of actual velocity, the one that affects the body. 

- Unit: m/sec
- Dimensions: $\ce{ [LT^{-1}] }$

#### Average Velocity
$$\vec{v}_{av} = \frac{\vec{s}}{\Delta t}$$

- Vector along $\vec{s}$
- $\vec{v}_{av} = 0$ for a closed path
- Defined for finite time interval

#### Instantaneous Velocity (Velocity)
$$\vec{v}_{in} = \lim_{\Delta t \to 0} \frac{\Delta \vec{r} }{\Delta t} = \frac{d\vec{r}}{dt}$$

- Vector tangential to the path
- Defined for infinitely small time interval

![[Pasted image 20230417115213.png]]

Instantaneous velocity and Average velocity have the same direction at tangential points of the path

### Speed

- Scalar
- Unit: m/sec
- Dimensions: $\ce{ [LT^{-1}] }$

#### Average Speed
$$v_{av} = \frac{s}{\Delta t}$$

- Always equal to or greater than average velocity
- Equal when path is straight line without turning back 
- Defined for finite time interval

#### Instantaneous Speed (Speed)
$$v_{in} = |\vec{v_{in}}| = \lim_{\Delta t \to 0} \frac{\Delta r}{\Delta t} = \frac{dr}{dt}$$

- Is the magnitude of instantaneous speed
- Defined for infinitely small time interval

### Acceleration
Rate of change of velocity.
It could be due to change in magnitude or direction of velocity.

- Unit: $\ce{ m s^{-2} }$
- Dimensions: $\ce{ [LT^{-2}] }$

Differentiating Acceleration gives **Jerk** with unit $\ce{ m s^{-3} }$.

#### Average Acceleration
$$\vec{a}_{av} = \displaystyle \frac{\Delta \vec{v}}{\Delta t}$$

- Vector towards $\Delta \vec{v}$ i.e. along change in velocity
- Defined for finite time interval

#### Instantaneous Acceleration (Acceleration)
$$\vec{a}_{in} = \lim_{\Delta t \to 0} \frac{\Delta \vec{v}}{\Delta t} = \frac{d \vec{v}}{dt}$$

$$\vec{a} = \frac{d}{dt} \left( \frac{d\vec{r}}{dt} \right) = \frac{d^{2}\vec{r}}{dt^{2}}$$

- Vector with direction not fixed
- Defined for an infinitely small interval of time

If the particle is moving in one direction:
$$\vec{a} = \frac{dv}{dt} = \frac{dx}{dx} \cdot \frac{dv}{dt} = \frac{dx}{dt}\cdot \frac{dv}{dx}$$

$$\vec{a} = v \frac{dv}{dx}$$

### Reaction Time
The time taken to observe, analyse and react.

We can do these kind of questions using graph as well. 

![[Pasted image 20230420113922.png]]


### Conversion of Speed

$$\ce{ 1 km h^{-1} = \frac{5}{18} m s^{-1} }$$
$$\ce{ 18 km h^{-1} = 5 m s^{-1} }$$