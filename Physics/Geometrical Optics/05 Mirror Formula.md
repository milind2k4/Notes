Links: [[03 Spherical Mirror]], [[02 Object and Image]]
___
# Mirror Formula
It relates $x \text{ - coordinates}$ of O and I
It is for paraxial rays. 

> $$\frac{1}{v} + \frac{1}{u} = \frac{1}{f} = \frac{2}{R}$$
> $$\implies v = \frac{u \cdot f}{u-f}$$
> $$\implies f = \frac{u \cdot v}{u+v}$$


where, 
- $u \to$ $x \text{ - coordinate}$ of O
- $v \to$ $x \text{ - coordinate}$ of I
- $f \to$ $x \text{ - coordinate}$ of principal focus
- $R \to$ $x \text{ - coordinate}$ of Centre of Curvature.

**Note:** 
- $f\ \&\ R$ are positive in Convex, negative in Concave.
- We can also use this formula even when the Pole is not in the centre of the picture. As in [[00 Geometrical Optics#Mirror is Cut]]

  
## Proof of Mirror Formula
![[Mirrot Formula Derivation.png]]

> \
> $$\triangle OAF \sim \triangle DPF \text{ i.e. } \triangle 1  \sim \triangle 2,$$
> $$\implies \frac{OA}{PD} = \frac{AF}{FP}$$
> $$\implies \frac{h_{o}}{h_{i}} = \frac{u-f}{f} \text{ .......(1)}$$
> \
> $$\triangle IGF \sim \triangle BPF \text{ i.e. } \triangle 3 \sim \triangle 4$$
> $$\implies \frac{IG}{BP} = \frac{GF}{FP}$$
> $$\implies \frac{h_{i}}{h_{o}} = \frac{v-f}{f}$$
> $$\implies \frac{h_{o}}{h_{i}} = \frac{f}{v-f} \text{ .......(2)}$$
> 
> \
> $$\text{From (1) and (2)}, \phantom{AAAAAAAAA}$$
> $$\phantom{\implies} \frac{u-f}{f} = \frac{f}{v-f}$$
> $$\implies f^{2} = (u-f)(v-f)$$
> $$\implies uv = fv + uf$$
> $$\text{Dividing both sides by } uvf,$$
> $$\phantom {\implies} \frac{1}{f} = \frac{1}{u} + \frac{1}{v}$$

## Graph between u and v
> $$
> \begin{flalign}
> \frac{1}{v} & + \frac{1}{u} = \frac{1}{f} && \\
> \frac{1}{v} & = \frac{-1}{u} + \frac{1}{f} \\
> \text{Let, }\  & \frac{1}{v} = y\; \&\; \frac{1}{u}  = x \\
> \implies y & = -x + \frac{1}{f} \\
> \end{flalign}
> $$

![[graph bw 1_u and 1_v.png]]

### Observations
- The graph of Convex is in 1st, 2nd & 4th quadrant.
	- There will never be a situation where both the [[02 Object and Image|object and image]] are in front of the mirror.
	- For convex, both $u\ \&\ v$ cannot be $-ve$ at the same time.
	- There will never be a real image of a real object.

- The graph of Concave is in 2nd, 3rd & 4th quadrant.
	- There will never be a situation where both the [[02 Object and Image|object and image]] are behind the mirror.
	- For concave, both $u\ \&\ v$ cannot be $+ve$ at the same time.
	- There will never be a virtual image of a virtual object.