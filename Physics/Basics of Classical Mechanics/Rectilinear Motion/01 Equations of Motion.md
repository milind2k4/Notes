Links: [[00 Kinematics]]
___
# Equations of Motion
$r,\ s,\ v,\ u\ \&\ a$ are vectors. 

## Uniform Motion
Constant velocity.
$v = \text{constant}$

Displacement,
> $$\begin{split}
> \frac{dx}{dt} & = v \implies dx = vdt \\
> \int_{x_{i}}^{x_{f}} dx & = v \int_{0}^{t}dt \\
> x_{f} - x_{i} & = vt\\
> x_{f} & = x_{i} + vt \\\\
> s & = x_{f} - x_{i} \\
> s & = vt 
> \end{split}$$

![[Graph of Uniform Motion.png]]


## Uniformly accelerated Motion
Constant acceleration.
$a = \text{constant}$
Jerk is zero. 

### The 7 Equations of Motion
> $$\begin{split}
> v & = u + at \\\\
> s & = ut + \frac{1}{2}at^{2} \\\\
> v^{2} & = u^{2} + 2as \\\\
> s & = vt - \frac{1}{2}at^{2} \\\\
> s & = \frac{(u+v)t}{2} \\\\
> v_{av} & = \frac{u+v}{2} \\\\
> s_{n} & = u + \frac{1}{2}a(2n-1)
> \end{split}$$


### Their Proofs
Velocity,
> $$\begin{split}
> a & = \frac{dv}{dt} \implies dv = adt \\
> \int_{u}^{v}dv & = a \int_{0}^{t}dt \\
> v - u & = at \\
> v & = u + at
> \end{split}$$

Displacement,
> $$\begin{split}
> v = u + at & = \frac{dr}{dt} \\
> dr & = udt + atdt \\
> \int_{r_{i}}^{r_{f}} dr & = u \int_{0}^{t}dt + a \int_{0}^{t} tdt \\\
> r_{f} - r_{i} & = ut + \frac{1}{2}at^{2} \\
> r_{f} & = r_{i} + ut + \frac{1}{2}at^{2} \\
> s & = ut + \frac{1}{2}at^{2} 
> \end{split}$$

Eliminating $t$,
> $$\begin{split}
> s & = u \left( \frac{v-u}{a} \right) + \frac{1}{2}a \left( \frac{v-u}{a} \right)^{2} \\
> v^{2} & = u^{2} + 2as
> \end{split}$$

Eliminating $u$,
> $$\begin{split}
> s & = (v-at)t + \frac{1}{2}at^{2} \\
> s & = vt - at^{2} + \frac{1}{2}at^{2} \\
> s & = vt - \frac{1}{2}at^{2}
> \end{split}$$

Adding both expressions for $s$,
> $$\begin{split}
> 2s & = ut + vt \\
> s & = \frac{(u+v)t}{2}
> \end{split}$$

Now, average velocity,
> $$\begin{split}
> v_{av} & = \frac{s}{t} \\
> v_{av} & = \frac{u+v}{2} 
> \end{split}$$

$s_{t} - s_{t-1},$ i.e. $n^{th}$ second. 
> $$\begin{split}
> s_{t} & = ut + \frac{1}{2}at^{2} \\
> s_{t-1} & = u(t-1) + \frac{1}{2}a(t-1)^{2} \\
> s_{t} - s_{t-1} & = u + \frac{1}{2} a(2t-1)\\\\
> \text{Let t = n}, & \text{ then, in nth second} \\
> s_{n} & = u + \frac{1}{2}a(2n-1)
> \end{split}$$
> This gives displacement in the nth second, not distance travelled.
> If the distance travelled is asked and the answer comes out to be zero, draw v-t graph and use area for distance travelled. 