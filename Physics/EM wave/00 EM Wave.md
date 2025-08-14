Links: [[01 Maxwell's Equations]], [[02 Energy Density and Intensity]]
___
# Electromagnetic Wave
They are non mechanical transverse waves, and thus require no medium. 

![[Pasted image 20240119205658.png]]

Velocity of EM waves in vacuum is $c = 3 \times 10^{8}$. 
And in any other medium,
$$v = \frac{ c }{ n }$$
where n is refractive index. 

Examples are radio waves, microwaves, infrared, light, ultrasound, X-rays, $\upgamma$-rays, etc.

The disturbances in EM waves are time varying electric and magnetic waves. 

$$
\begin{split}
E &= f(t,x) \\
B &= f(t,x)
\end{split}
$$

#### Electric - Magnetic Field Coupling 
[[00 Electromagnetic Induction#E due to Time Varying B]]

Since nature is symmetric, time varying E will also induce B. 

This creation of fields is called Electric - Magnetic field coupling.

Below, the magnet will align itself with the magnetic field. 

![[Pasted image 20240119205728.png]]

#### Generation of EM Waves 
A charged particle at rest creates electric field. 
A charged particle moving with constant velocity creates electric as well as magnetic fields. 

A charged particle with acceleration creates EM waves. 

Since the position is varying with time, the EF at a point is also varying with time. This time varying EF will create a time varying MF which will in turn create time varying EF. 

Thus, oscillating charged particles are responsible for EM waves.

![[Pasted image 20240119205916.png]]

### Maxwell's Displacement Current
It is not an actual current. 

Normal current is due to flow of charge and is called **Conduction Current.**
$$i_{c} = \frac{ dq }{ dt }$$

Displacement current is a pseudo current (like pseudo force).
It is not due to any charge flow. It is just a mathematical term. 

It is only present if there is time varying electric field in the region.

We take an arrangement as below and find magnetic field at a point r distance away from the wire. 

Now, we find magnetic field r distance from the centre of the capacitor. 

It was found that the magnetic field at both points is the same.

Thus, we assume a current in between the capacitor plates equal to the conduction current to explain this magnetic field. 

![[Pasted image 20240119205747.png]]
(it will be $d(\varepsilon_{o} \phi_{E})$ not what's written there)

We take a cross section in between the plates. 
The field on this cross section is,
$$E = \frac{ q }{ A\varepsilon_{o} }$$
And the flux will be,
$$\phi_{E} = EA = \frac{ q }{ \varepsilon_{o} }$$
Thus we can write,
$$q = \varepsilon_{o}\phi_{E}$$

Now, we get,
$$
\begin{split}
i_{d} &= i_{c} \\
&= \frac{ dq }{ dt } \\
i_{d} &= \varepsilon_{o} \frac{ d\phi_{E} }{ dt } 
\end{split}
$$

Thus we see that the cause of displacement current is change of electric field.

![[Pasted image 20240119205815.png]]
![[Pasted image 20240119205825.png]]

## Spectrum of EM Waves 
The wave which has more frequency has more energy, and thus penetration power.

Radio waves are produced by rapid acceleration and deceleration of e in aerials. They are received by receiver aerials. 

Micro waves are produced by Klystron Valve or Magnetron Valve. They are received by point contact diodes.

Infrared are produced by vibrations of molecules. They are received by thermopile bolometer or infrared photographic film. 

Light is  created by e jumping between shells in atoms. They are received by eyes or photocells.

Ultraviolet is  created by e jumping between shells in atoms. They are received by photocells.

X rays are created by x-ray tubes. They are received by photographic film or Geiger tubes or ionisation chambers.

$\upgamma$ rays are created by nuclear decay. They are received by photographic film or Geiger tubes or ionisation chambers.

![[Pasted image 20240119220057.png]]