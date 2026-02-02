Links: [[00 System of Particles]]
___
# Variable mass System (Thrust Force)
A particle of mass $dm$ moving with $v + v_{rel}$ gets embedded into a block of mass m moving with velocity $v$. It is an example of [[04 Collisions#Perfectly Inelastic Collision|perfectly inelastic collision.]] 

![[Pasted image 20230708134430.png]]

The new mass will be, $m + dm$ with velocity $v + dv$.

The momentum of the whole system is conserved,
$$
\begin{split}
mv + dm(\vec{v} + \vec{v}_{rel}) &= (m + dm)(\vec{v} + d\vec{v}) \\
m\vec{v} + dm\vec{v} + dm\vec{v}_{rel} &= m\vec{v} + md\vec{v} + dm\vec{v} + dmd\vec{v} \\
dm\vec{v}_{rel} &= md\vec{v} \\
\\
\text{Dividing by}\ dt,\\
\frac{ dm\vec{v}_{rel} }{ dt } &= \frac{ md\vec{v} }{ dt } 
\end{split}
$$

Thus giving thrust force,
$$\vec{f}_{th} = m \frac{ d\vec{v} }{ dt } = \vec{v}_{rel}\frac{ dm }{ dt }$$
Here, $\displaystyle \frac{ dm }{ dt }$ is the rate at which mass is increasing. It is represented by $\lambda$ and has unit kg/s. 


When mass is increasing, $\displaystyle \frac{ dm }{ dt }$ will be +ve and thus $\vec{f}_{th}$ will be parallel to $\vec{v}_{rel}$. 
When mass is decreasing, $\displaystyle \frac{ dm }{ dt }$ will be -ve and thus $\vec{f}_{th}$ will be anti-parallel to $\vec{v}_{rel}$. 

That is,
$$
\begin{split}
\frac{ dm }{ dt } = +ve &\implies \vec{f}_{th} \upharpoonleft \! \upharpoonright \vec{v}_{rel} \\
\\
\frac{ dm }{ dt } = -ve &\implies \vec{f}_{th} \upharpoonleft \! \downharpoonright \vec{v}_{rel}
\end{split}
$$


Thus if mass is entering or leaving a system with some relative velocity it will apply thrust force,
$$\vec{f}_{th} = \lambda v_{rel}$$
Adding mass will apply force in the direction of relative velocity.
Leaving mass will apply force in the direction opposite to relative velocity.

### Rocket Propulsion
A rocket of mass $m_{o}$ ejects gases $\lambda$ kg/s with relative velocity $u$ opposite to the velocity of rocket. We have to find velocity of rocket at any time t.

#### No Gravity
Mass of rocket at time t,
$$m = m_{o} - \lambda t$$
Thrust force on rocket,
$$f_{th} = \lambda u$$

Thus,
$$
\begin{split}
\lambda u &= (m_{o} - \lambda t) \frac{ dv }{ dt } \\
\lambda u \int_{0}^{t} \frac{ dt }{ m_{o} - \lambda t } &= \int_{0}^{v} dv \\
\frac{ \lambda u }{ -\lambda } \ln(m_{o} - \lambda t) - \ln m_{o} &= v \\
u \ln \frac{ m_{o} }{ m_{o} - ut } &= v
\end{split}
$$

Thus, the velocity of rocket at any time will be,
$$v = u \ln \frac{ m_{o} }{ m }$$
where $m = m_{o} - \lambda t$ i.e. mass of rocket at any time t.

![[Pasted image 20230708140120.png]]

#### With Gravity 
Here too, mass of rocket at any time t,
$$m = m_{o} - \lambda t$$

And thrust force on rocket,
$f_{th} = \lambda u$

Thus,
$$
\begin{split}
\lambda u - (m_{o}-\lambda t)g &= (m_{o} - \lambda t) \frac{ dv }{ dt } \\
\lambda u \int_{0}^{t} \frac{ dt }{ m_{o} - \lambda t } - g \int_{0}^{t} dt &= \int_{0}^{v} dv \\
\frac{ \lambda u }{ \lambda } \ln (m_{o} - \lambda t) - \ln m_{o} - gt &= v \\
-u\ln \frac{ m_{o} }{ m_{o} - \lambda t } - gt &= v 
\end{split}
$$
Thus the velocity can be given by,
$$v = u \ln \frac{ m_{o} }{ m } - gt$$
where $m = m_{o} - \lambda t$ i.e. mass of rocket at any time t.

#### [[Physics/System of Particles/06 Examples#05 Variable Mass System]]