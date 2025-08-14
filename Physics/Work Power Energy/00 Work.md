Links: [[03 Energy]]
___
# Work
Work is the method of energy transfer via the application of force. 
It is a scalar.

There are two requirements of work,
1. Force
2. Displacement of point of application of force. (POAF) in any direction other than $\perp$ the force

Because there is displacement, the work done is dependent on reference frame. 

#### Units and Dimensions of Work
Newton Meter ($\ce{ Nm }$) = Joule ($\ce{ J }$) (SI)
CGS unit is $\ce{ erg }$ which is $\ce{ 10^{-7} J }$
$$\ce{ 1 J = 10^{7} erg }$$
Electron Volt ($eV$) ($1eV = 1.6 \times 10^{-19}$)

Dimensions are, $\ce{ [ML^{2}T^{-2}] }$

## Magnitude of Work

Work can be +ve (supply), -ve (extract), zero.
Small work due to small displacement of POAF,
$$dW = \vec{f} \cdot d\vec{s}$$
$$dW = fds \cos \theta$$
where,
$\vec{F}$ is the force for which work done is being calculated. 
$d \vec{s}$ displacement of point of application of force. 

i.e. Force times displacement in the direction of force. 
![[Pasted image 20230610113950.png]]

or Displacement times force in the direction of displacement. 
![[Pasted image 20230610114017.png]]

Thus,
$$0 \leq \theta \leq \frac{\pi}{2} \implies \ W \to +ve$$

$$\theta = \frac{\pi}{2} \implies \ W \to 0$$

$$\theta > \frac{\pi}{2} \implies \ W \to -ve$$


## [[01 Work done by Constant Force]]

## Work done by Variable Force

$$\vec{f} = f_{x} \hat i + f_{x} \hat j + f_{x} \hat k$$
$$d\vec{s} = dx \hat i + dy \hat j + dz \hat k$$

$$
\begin{split}
W &=\int \vec{f} \cdot d \vec{s} 
\\
&= \int (f_{x} \hat i + f_{x} \hat j + f_{x} \hat k) \cdot (dx \hat i + dy \hat j + dz \hat k) 
\\
&= \int f_{x}dx + f_{y}dy + f_{z}dz 
\\
&= \int_{x_{1}}^{x_{2}}  f_{x}dx + \int_{y_{1}}^{y_{2}} f_{y}dy + \int_{z_{1}}^{z_{2}} f_{z}dz 
\end{split} 
$$

I.e. Work done = area under $f_{x}-x$ graph + area under $f_{y}-y$ graph + area under $f_{z}-z$ graph +

Example,
![[Pasted image 20230612121619.png]]

#### Work done by Spring Force
$$
\begin{split}
dW_{s} &= kxdx \cos \pi = -kx . dx \\
W_{s} &= \int_{0}^{x} -kx \, dx \\
&= - \frac{1}{2}kx^{2} 
\end{split}
$$
This is the work done for both the compression and extension by length x. 

Work done due to coming from extension or compression to natural length is the same but positive.
$$W_{s} = \frac{1}{2} kx^{2}$$

And work done on wall is zero. 

It is also equal to the difference in PE,
$$W_{s} = U_{i} - U_{f}$$
where,
$$U_{s} = \frac{ 1 }{ 2 } k(\text{ext. or comp})^{2}$$

#### Work done by Kinetic Friction
When the direction changes, but the magnitude of $f_{k}$ is fixed. 

$$
\begin{split}
W_{f} &= \int \vec{f}_{k} \, d\vec{s} \\
&= \int f_{k} \, ds\cos \theta \\
&= \int f_{k} \, ds\cos \pi \\
&= -f_{k} \int ds \\
&= -f_{k}l    
\end{split}
$$
here, we are not integrating $d\vec{s}$ but $ds$ therefore, the integration comes out to be $l$, path length. 
I.e.
$$
\begin{split}
\int d\vec{s} &= \text{displacement} \\
\int ds &= \text{path length}
\end{split}
$$

![[Pasted image 20230612123351.png]]

For particle moving on a non uniform path up a height, 
$$W_{f} = -\mu mgl$$
![[Pasted image 20230614130320.png]]
