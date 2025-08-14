
Links: [[13 Prism]]
___
# Dispersion of Light
It is angular splitting of white light into its constituents (VIBGYOR) and spreading in different directions. This also works for any combination of any number of the 7 colours. 

In vacuum or air all the colours have same speed but in other media speed of different colours is slightly different. Due to this a medium will have different refractive indices for different colours. The difference however, is very very small. 

### Cauchy's Formula
It states that refractive index of a medium also depends on wavelength of light passing through it. 
$$n = f(\lambda) = a + \frac{ b }{ \lambda^{2} }$$
($\lambda$ is wavelength)

for vacuum, a = 1 and b = 0, thus n = 1 for all colours. 
for any other medium, b = +ve, thus $\lambda \uparrow \implies n \downarrow$

Thus, the refractive index for violet is the highest and for red is the lowest for any medium. 
$$n_{v} > n_{r}$$
Yellow being between them, and considered the refractive index of the medium. 
$$n_{avg} = n_{y} = \frac{ n_{v} + n_{r} }{ 2 }$$

Dispersion works for both rarer to denser and denser to rarer. And the angle between the two extreme rays is called the **Dispersion Angle.**
![[Pasted image 20230520130036.png]]
![[Pasted image 20230520130323.png]]


## Dispersion in Prism
![[Pasted image 20230520130517.png]]

#### For Small Angled Prism

The maximum deviation is of violet and the minimum is of red. 
$$\delta_{v} = (n_{v}-1)A$$
$$\delta_{r} = (n_{r}-1)A$$

The dispersion angle will be,
$$
\theta = (n_{v} - n_{r})A = dnA
$$


Yellow is considered the average and the deviation in yellow is said to be mean deviation. If just the deviation is asked, then give the deviation of yellow.
$$\delta_{y} = (n_{y}-1)A$$
$$\delta_{y} = (n-1)A$$

**Dispersive Power** is,
$$\upomega = \frac{ \text{angle of dispersion} }{ \text{mean deviation} } = \frac{ \theta }{ \delta_{y} } = \frac{ n_{v}-n_{r} }{ n_{y}-1 }$$
It is a property of the medium.

![[Pasted image 20230520130825.png]]


##### Combination of Prisms
If they are placed upright,
$$\delta_{net} = \delta_{1} + \delta_{2}$$
$$\theta_{net} = \theta_{1} + \theta_{2}$$

![[Pasted image 20230301194128.png]]


If they are placed opposite each other,
$$\delta_{net} = |\delta_{1} - \delta_{2}|$$
$$\theta_{net} = |\theta_{1} - \theta_{2}|$$

![[Pasted image 20230301194141.png]]

#### Direct View Combination
Dispersion without Deviation ($\delta_{avg} = 0, \theta_{net} \neq 0$)

The deviation of yellow light is zero. 

$$
\begin{split}
\delta_{1} - \delta_{2} &= 0 \\
(n_{y} - 1)A &= (n_{y}' - 1)A' \\
\end{split}
$$
This is the condition for Direct View Combination. 

In this case, the dispersion will be,
$$
\begin{split}
\theta_{net} &= \theta_{1} - \theta_{2} \\
&= \delta \upomega_{1} - \delta \upomega_{2}\\
&= \delta |\upomega_{1} - \upomega_{2}|
\end{split}
$$
If prisms are of different medium, then if mean deviation is zero, the net dispersion cannot be zero. 

![[Pasted image 20230522120525.png]]

#### Achromatic Combination
Deviation without Dispersion ($\delta_{net} \neq 0, \theta_{net} = 0$)

$$
\begin{split}
\theta_{net} &= 0 \\
(n_{v}-n_{r})A &= (n_{v}' - n_{r}')A'
\end{split}
$$
This is the condition for achromatic combination. 

The net deviation, 
$$
\begin{split}
\delta &= \frac{ \theta }{ \upomega_{1} } - \frac{ \theta }{ \upomega_{2} } \\
&= \theta \left| \frac{ 1 }{ \upomega_{1} } - \frac{ 1 }{ \upomega_{2} } \right| 
\end{split}
$$
If 2 prisms are of different medium, then if net dispersion is zero, the net deviation cannot be zero. 


![[Pasted image 20230522115916.png]]

### Chromatic Aberration in Lens
The incapability of a lens to focus parallel beam of white light into a single point.

Since $n_{v} > n_{r}$, $f_{v} < f_{r}$. 
The separation between the focal lengths of red and violet is called **Longitudinal Chromatic Aberration. (LCA)**

$$LCA = f_{r} - f_{v} = -df$$
-df is because as n increases, f decreases, so df comes out -ve, so we add a -ve to make it +ve. 

$$
\begin{split}
\frac{ 1 }{ f } &= (n-1) \left( \frac{ 1 }{ R_{1} } - \frac{ 1 }{ R_{2} } \right) \dots (1) \\
\text{Diff. this,} \\
\frac{ -1 }{ f^{2} }df &= dn \left( \frac{ 1 }{ R_{1} } - \frac{ 1 }{ R_{2} } \right) \dots (2) \\
\\
\text{Dividing 2 by 1,} \\
\frac{ -df }{ f } &= \frac{ dn }{ n-1 } \\
\frac{ -df }{ f } &= \upomega  \\
-df &= \upomega f
\end{split} 
$$

Thus LCA is,
$$-df = \upomega f$$

![[Chromatic Aberration.png]]

An example,
![[Pasted image 20230522123308.png]]

#### Removal
For converging lens, the LCA is +ve, and that of diverging is -ve. 

Thus we use a combination of lenses so that the LCA cancels out. 

$$
\begin{split}
\frac{ 1 }{ f_{eq} } &= \frac{ 1 }{ f_{1} } + \frac{ 1 }{ f_{2} } \\
\text{Diff. this,} \\
\frac{ df_{eq} }{ f_{eq}^{2} } &= \frac{ df_{1} }{ f_{1}^{2} } + \frac{ df_{2} }{ f_{2}^{2} } \\
&= \frac{ -\upomega_{1}d_{1} }{ f_{1}^{2} } - \frac{ \upomega_{2}f_{2} }{ f_{2}^{2} } \\
\frac{ df_{eq} }{ f_{eq}^{2} } &= \frac{ -\upomega_{1} }{ f_{1} } - \frac{ -\upomega_{2} }{ f_{2} } \\
\\
\text{Since } df_{eq} = 0,\\
\frac{ f_{1} }{ f_{2} } &= \frac{ -\upomega_{1} }{ \upomega_{2} }
\end{split}
$$

![[Pasted image 20230522124204.png]]