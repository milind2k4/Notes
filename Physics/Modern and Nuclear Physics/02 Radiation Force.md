Links: [[01 Photoelectric Effect]], [[02 Radiation]]
___
# Radiation Force
Here, absorptive power is,
$$a = \frac{ N_{a} }{ N_{i} }$$
And coefficient of reflection,
$$r = 1 - a = \frac{ N_{r} }{ N_{i} }$$

#### Normal Incident 
The light falling on the surface of area A has intensity I and wavelength $\lambda$. 

Power incident on surface,
$$P = \vec{I}. \vec{A} = IA$$

No. of photons incident per unit time,
$$N_{i} = \frac{ P\lambda }{ hc } = \frac{ IA\lambda }{ hc }$$
Thus, absorbed photons,
$$
\begin{split}
N_{a} &= aN_{i} \\
&= \frac{ aIA\lambda }{ hc } \\
&= \frac{ (1-r)IA\lambda }{ hc }
\end{split}
$$
Reflected photons,
$$N_{r} = \frac{ rIA\lambda }{ hc }$$

Now, an incident photon has momentum,
$$p = \frac{ h }{ \lambda }$$

Change in momentum of an absorbed photon,
$$\Delta \vec{p} = \frac{ h }{ \lambda } \uparrow$$

Thus the force on the surface due to absorbed photons,
$$
\begin{split}
f_{a} &= N_{a}\Delta p \\
&= \frac{ (1-r)IA\lambda }{ hc } \frac{ h }{ \lambda } \\
&= \frac{ (1-r)IA }{ c }
\end{split}
$$

Change in momentum of a reflected photon,
$$\Delta \vec{p} = \frac{ 2h }{ \lambda } \uparrow$$

Thus, force on the surface due to reflected photons,
$$
\begin{split}
f_{r} &= N_{r} \Delta p \\
&= \frac{ rIA\lambda }{ hc } \frac{ 2h }{ \lambda } \\
&= \frac{ 2rIA }{ c }
\end{split}
$$

The net force is,
$$
\begin{split}
f &= f_{a} + f_{r} \\
&= \frac{ IA(1+r) }{ c } \\
&= \frac{ P(1+r) }{ c }
\end{split}
$$

![[Pasted image 20240122204554.png]]

![[Pasted image 20240122204605.png]]

#### Perfectly Absorbing Surface 
Here, $a = 1$ and $r = 0$. 
Thus, $N_{a} = N_{i}$. 

The net force thus becomes,
$$f = \frac{ IA }{ c } = \frac{ P }{ c }$$

![[Pasted image 20240122205058.png]]

#### Perfectly Reflecting Surface 
Here, $a = 0$ and $r = 1$. 
Thus, $N_{r} = N_{i}$. 

The net force thus becomes,
$$f = \frac{ 2IA }{ c } = \frac{ 2P }{ c }$$
which is twice that in the case of perfectly absorbing surface. 

### Oblique Incident 
The incident light of intensity $I$ and wavelength $\lambda$ makes angle $\theta$ with the normal of the surface of area A. 

Incident power,
$$
\begin{split}
P &= \vec{I}. \vec{A} \\
&= IA \cos \theta 
\end{split}
$$

No. of incident photons,
$$
\begin{split}
N_{i} &= \frac{ P\lambda }{ hc } \\
&= \frac{ IA\lambda \cos \theta }{ hc } \\
\end{split}
$$
#### Perfectly Absorbing Surface 
Here, $N_{a} = N_{i}$.
Thus,
$$N_{a} = \frac{ IA\lambda \cos \theta }{ hc }$$

Change in momentum of one photon,
$$
\begin{split}
\Delta \vec{p} &= 0 - \frac{ h }{ \lambda } \\
&= \frac{ h }{ \lambda } \ce{\ at angle \theta from normal}
\end{split}
$$

Thus force on the surface,
$$
\begin{split}
f &= N_{a} \Delta p \\
&= \frac{ IA\lambda \cos \theta }{ hc } \frac{ h }{ c } \\
&= \frac{ IA\cos \theta }{ c }
\end{split}
$$

And pressure,
$$
\begin{split}
P_{r} &= \frac{ f_{norm} }{ A } \\
&= \frac{ I\cos ^{2}\theta }{ c }
\end{split}
$$

Shear stress,
$$
\begin{split}
S &= \frac{ f_{tang} }{ A } \\
&= \frac{ I\cos \theta \sin \theta }{ c }
\end{split}
$$

![[Pasted image 20240122205948.png]]

#### Perfectly Reflecting Surface 
Here, $$N_{r} = N_{i}$$
Thus,
$$N_{r} = \frac{ IA\lambda \cos \theta }{ hc }$$

Change in momentum of one photon,
$$
\begin{split}
\Delta \vec{p} &= \left( \frac{ h }{ \lambda }\sin \theta\ \hat{i} + \frac{ h }{ \lambda }\cos \theta\ \hat{j} \right) - \left( \frac{ h }{ \lambda }\sin \theta\ \hat{i} - \frac{ h }{ \lambda }\cos \theta\ \hat{j} \right) \\
&= \frac{ 2h }{ \lambda } \cos \theta\ \hat{j}
\end{split}
$$

Thus the force on the surface,
$$
\begin{split}
f &= N_{r} \Delta p \\
&= \frac{ IA\lambda \cos \theta }{ hc } \frac{ 2h }{ \lambda }\cos \theta \\
&= \frac{ 2IA \cos ^{2}\theta }{ c }
\end{split}
$$
All this force is perpendicular to the surface and thus there is no shear stress. 

Pressure,
$$P_{r} = \frac{ f_{n} }{ A } = \frac{ 2I\cos ^{2}\theta }{ c }$$

