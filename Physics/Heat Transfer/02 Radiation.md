Links: [[00 Heat Transfer]]
___
# Radiation
Any body which has temperature more than 0 K gives off EM waves.
These EM waves are called radiation. 
These radiations can thus travel in vacuum.

The more temp. the object has the more its particles vibrate and  thus give off photons of higher KE, and thus lower $\lambda$ or higher $f$.
$$E = \frac{ hc }{ \lambda } = hf$$

At room temp. a body radiates photons in infrared region.

Rate is measured in terms of power.

#### Prevost Theory of Exchange
If the temp. of the object and the surroundings is the same, 
$$P_{emit} = P_{abs}$$

If the temp. of the object is more than that of the surroundings,
$$P_{emit} > P_{abs}$$

If the temp. of the object is less than that of the surroundings,
$$P_{emit} < P_{abs}$$

![[Pasted image 20231221205641.png]]

**In language,**

> *If the temperature of the body is more than that of surroundings it will lose heat by radiation and as a result get colder.* 
> 
> *If it is lower than that of the surroundings, then it will absorb radiation and as a result get hotter.* 

## Terms 
#### Absorptive Power (a)
By energy conservation,
$$
\begin{split}
P_{a} + P_{r} + P_{t} &= P_{i} \\
\frac{ P_{a} }{ P_{i} } + \frac{ P_{r} }{ P_{i} } + \frac{ P_{t} }{ P_{i} } &= 1 \\
a + r + t &= 1
\end{split}
$$

Where,
$$
\begin{split}
a &= \frac{ P_{abs} }{ P_{in} } = \text{absorbtive power} \\
r &= \frac{ P_{ref} }{ P_{in} } = \text{coefficient of reflection} \\
t &= \frac{ P_{tra} }{ P_{in} } = \text{coefficient of transmission}
\end{split}
$$

a has range,
$$0 \leq a \leq 1$$

![[Pasted image 20231221210136.png]]

### Emissive Power (E)
It is radiated power per unit surface area.

$$E = \frac{ P_{emit} }{ A }$$
where,
$P_{emit} \to$ Power Emitted
$A \to$ surface area

It has unit W/m$^{2}$. 

Also,
$$E \propto T^{4}$$
where T is temp. in kelvin.

![[Pasted image 20231221212426.png]]

#### Spectral Emissive Power 

Let the net emissive power is $E$, over a total of $0 \to \infty$ values of $\lambda$.

Now, for a small range of $\lambda$, i.e. $\lambda \to \lambda + d\lambda$, let the emissive power is $dE$,

Then spectral emissive power is defined as,
$$E_{\lambda} = \frac{ dE }{ d\lambda } $$

Now,
$$dE = E_{\lambda} d\lambda$$
Thus the area under the graph of Spectral emissive power and wavelength gives emissive power.

![[Pasted image 20231222132543.png]]

## Perfectly Black Body
#important 

A body which absorbs all the power incident on it. There is no transmission or reflection. 

I.e. it has a = 1.

$$P_{in} = P_{abs}$$

There will be no reflection or transmission of radiation. 

PBB can emit radiation due to its own temp.
Sun is an almost perfectly black body. 

![[Pasted image 20231221210617.png]]

### Ferry's Black Body
We take a hollow sphere painted charcoal black on the inside. This sphere has a hole and an edge. 

Let this black paint have absorptive power a. 

Now, a ray in incident on the edge through the hole. $aP_{in}$ power is absorbed and since the edge is solid, the rest is reflected.

Inside the sphere there will be many collisions and each time more and more power is absorbed. 

Let after n times the ray comes out, then this ray will have power,
$$P_{out} = (1-a)^{n} P_{o}$$

If n is large, the power reflected back will be almost zero.

Thus the effective absorptive power of the system is,
$$
\begin{split}
a_{eff} &= \frac{ P_{abs} }{ P_{in} } \\
&= \frac{ P_{o} - (1-a)^{n}P_{o} }{ P_{o} } \\
&= 1 - (1 - a)^{n} \approx 1\\
\end{split}
$$

![[Pasted image 20231221212416.png]]

### Emissivity $(e)$
It is the ratio of the Emissive power of a body and a PBB at the same temperature. 

$$e = \frac{ E }{ E_{o} }$$
where $E_{o}$ is the emissive power of a PBB at the same temp.

e has range,
$$0 \leq e \leq 1$$
and it is 1 for PBB.

The bigger the value of e is the better emitter it is and thus e depends on the body.

![[Pasted image 20231221212739.png]]
