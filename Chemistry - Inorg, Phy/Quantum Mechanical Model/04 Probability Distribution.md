Links: [[00 Quantum Mechanics]], [[01 Orbitals]]
___
# Probability Distribution
#important  

$\psi$ is a function of x,y,z or $r,\theta,\phi$. 

$\psi(r,\theta,\phi)$ can be factorized into parts, radial wave function ($\psi_{r}$) and angular wave function ($\psi_{(\theta,\phi)}$). 
$$\psi(r,\theta,\phi) = \psi_{r} \times \psi_{(\theta, \phi)}$$

Since, $\psi$ has no physical significance, $\psi_{r}$ and $\psi_{(\theta,\phi)}$ also have no physical significance. 

Now,
$$\psi^{2} = \psi_{r}^{2} \times \psi_{(\theta,\phi)}^{2}$$
here,
$\psi^{2} \to$ probability density
$\psi_{r}^{2} \to$ *radial probability density*
$\psi_{(\theta,\phi)}^{2} \to$ *angular probability density*
to find probability, we need to multiply by volume.

Radial probability of finding e in a shell of thickness dr at a radial distance r,
$$= 4\pi r^{2}\psi_{r}^{2}dr$$
This $4\pi r^{2}\psi_{r}^{2}$ is called **radial probability distribution function or radial distribution function**.

The general equation of radial wave function ($\psi_{r}$) for an orbital is 
$$\psi_{r} = kr^{l} \text{ (a polynomial in r with degree }(n-l-1)) e^{-r/k'}$$
where,
$k,k' \to$ constants
$l \to$ Azimuthal Q. No. (number of angular nodes)
$n-l-1 \to$ number of radial nodes

For 1s orbital,
$$\psi_{r(1s)} = ke^{ -r/k' }$$

For 2s orbital,
$$\psi_{r(2s)} = k(k'-r)e^{ -r/k'' }$$

For 2p orbital,
$$\psi_{r(2p)} = kre^{ -r/k' }$$

For 3d orbital,
$$\psi_{r(3d)} = kr^{2}e^{ -r/k' }$$

Max. radial probability of finding e for H for 1s orbital,
![[Pasted image 20230501182542.png]]
This matches with the Bohr's model. Thus we say that Bohr model is suitable for H like species. 

For Angular wave functions,
$$\psi_{(\theta,\phi)} = f(\theta,\phi)$$
we just write instead of the cartesian coordinate, its value in $\theta$ and $\phi$.
Thus,
$$
\begin{split}
\psi_{px} &= k\sin \theta \cos \phi \\
\psi_{py} &= k \sin \theta \sin \phi \\
\psi_{pz} &= k \cos \theta
\end{split}
$$
as 
$x = r\cos \theta \cos \phi$
$y = r\sin \theta \sin \phi$
$z = r\cos \theta$
in [[00 Quantum Mechanics#Wave Function's Solution]]

### Graphs

The graph of $\psi_{r}$ and $\psi_{r}^{2}$ cuts the x-axis number of radial node times. 

![[Probability Distribution.png]]
(R means $\psi_{r}^{2}$(radial probability density) and $r^{2}|R|^{2}$ means radial probability distribution i.e. probability)

![[Probability vs Distance.jpg]]

For 4s,
![[Pasted image 20230501183431.png]]

#### Note
- For ns orbital, $\psi_{r}, \psi_{r}^{2}$ start from a finite distance on vertical axis, whereas $4\pi r^{2}\psi_{r}^{2}$ starts from origin.
- For np and nd orbitals, all three graphs start from the origin.
- Graph will cut the horizontal axis equal the the number of radial nodes. 
- Peak size of $\psi_{r}, \psi_{r}^{2}$ decrease with r whereas it increases for $4\pi r^{2}\psi_{r}^{2}$ with r

## Graphical Comparison of Dist. Func. 
for 3s, 3p and 3d. 
$r_{max}$ is the radial distance from nucleus where radial probability of finding e is maximum. 

**Penetration Power of an Orbital:** the ability of e in orbital to stay close to nucleus.
Order of Penetration Power, 
$$ns > np > nd > nf$$


1. $r_{max(3s)} > r_{max(3p)} > r_{max(3d)}$

1. Due to additional peaks, the e in 3s is closest to nucleus. 

2. Penetration power of 3s is max. among 3s, 3p, 3d.

![[Pasted image 20230501190248.png]]