Links: [[02 Radiation]]
___
# Laws
### Kirchhoff's Law
This KL is different from the one in Current Electricity. 
[[02 Radiation#Absorptive Power (a)]]
[[02 Radiation#Emissive Power (E)]]

It states that *any two bodies will have equal ratio of emissive power to absorptive power at the same temperature.*

$$\frac{ E_{1} }{ a_{1} } = \frac{ E_{2} }{ a_{2} }$$

If one of the bodies is a PBB,
$$
\begin{split}
\frac{ E_{1} }{ a_{1} } &= \frac{ E_{o} }{ 1 } \\
a_{1} &= \frac{ E_{1} }{ E_{o} } \\
&= e_{1} 
\end{split}
$$
Thus,
$$a = e$$

I.e. *good absorbers are good emitters.* 

Thus, $a \uparrow \implies e \uparrow \implies E \uparrow$
And, $a \downarrow \implies e \downarrow \implies E \downarrow$

![[Pasted image 20231222132515.png]]

### Wien's Displacement Law
[[02 Radiation#Spectral Emissive Power]]

$\lambda_{m}$ is the wavelength corresponding to max. emission. 

This law states that as temp. increases, the energy of the photons on an average is more and thus the wavelength is less. 

$$T \uparrow \implies \lambda_{m} \downarrow$$

Thus,
$$\lambda_{m} \propto \frac{1}{T}$$
here T is in K. 

And,
$$\lambda_{m} T = b = 2.82 \times 10^{-3} \ce{\ m K }$$
where b is called **Wien's constant**.

![[Pasted image 20231222133206.png]]

Example,
![[Pasted image 20231222133408.png]]

### Stefan-Boltzmann Law
This law states that,
$$
\begin{split}
P_{emit} &\propto e \\
&\propto A \\
&\propto T^{4}
\end{split}
$$

$$
\begin{split}
P_{abs} &\propto a \\
&\propto A \\
&\propto T_{s}^{4}
\end{split}
$$

Thus giving,
$$P_{emit} = \sigma eAT^{4}$$
$$P_{abs} = \sigma aAT_{s}^{4}$$
where, $\sigma$ is Stefan's Constant $(= 5.67 \times 10^{-8} \ce{ \ W/m^{2}K^{4} })$

![[Pasted image 20231222133606.png]]

Now, if the temp. of the body is more than that of the surroundings,
$$
\begin{split}
P_{out} &= P_{emit} - P_{abs} \\
&= eA\sigma T^{4} - aA\sigma T_{s}^{4} \\
&= eA\sigma (T^{4} - T_{s}^{4}) 
\end{split}
$$

Now since heat is going out of the body,
$$-mS \frac{ dT }{ dt } = eA\sigma (T^{4} - T_{s}^{4})$$
and $dT /dt$ can be called the rate of cooling.

![[Pasted image 20231222134056.png]]


### Newton's Law of Cooling
#important 

This is an extension of Stefan-Boltzmann law.

$$\frac{ dT }{ dt } \propto T - T_{s}$$
$$\frac{ dT }{ dt } = -k(T - T_{s})$$
This is known as NLC. But it only works when there is not a huge difference in the temps. 

Let the temp. of body is $T_{o}$ and that of the surroundings is $T_{s}$. We need to find the temp. at any time t. 

$$
\begin{split}
\frac{ dT }{ dt } &= -k(T - T_{s}) \\
\int_{T_{o}}^{T} \frac{ dT }{ T - T_{s} } &= \int_{0}^{t} dt 
\end{split}
$$
Thus, we get,
$$
\begin{split}
\ln \frac{ T - T_{s} }{ T_{o} - T_{s} } &= -kt \\
T  &= T_{s} + (T_{o} - T_{s})\ e^{-kt}
\end{split}
$$

Thus, 
- at $t = 0,\ T = T_{o}$
- at $t= \infty,\ T = T_{s}$
  
The temperature decreases **exponentially**. 

![[Pasted image 20231222135115.png]]

Example,
![[Pasted image 20231222135729.png]]
This question can also be done with approximation,
![[Pasted image 20231222135927.png]]