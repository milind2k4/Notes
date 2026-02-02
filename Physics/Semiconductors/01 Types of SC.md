Links: [[00 Semiconductors]], [[00 Current Electricity]]
___
# Types of Semiconductors 
## Intrinsic
Pure SC. 

They are elements of 14th group, i.e. C family. 3
The most common are Si and Ge. 

For Si,
$$\Delta E_{g} = 1.14\ eV$$
For Ge,
$$\Delta E_{g} = 0.7\ eV$$

At room temp., in Si, the probability of forming an e-h pair is $1 /10^{18}$. I.e. in every $10^{18}$ Si atoms, there is one e-h pair.

As we increase temp., this probability increases. 

In an intrinsic SC, since both holes and free e are formed in the same ration,
$$n_{e} = n_{h} = n_{i}$$
where $n_{i}$ is called intrinsic charge density.

Now, we have,
$$
\begin{split} 
n_{e}n_{h} &= n_{i}^{2} \\
n_{i}^{2} &= AT^{3}e^{ -\Delta E_{g}/kT }
\end{split}
$$

where,
$A \to$ some constant
$T \to$ temperature in constant
$\Delta E_{g} \to$ Forbidden energy gap of element
$k \to$ Boltzmann constant

Thus we can see that,
$$n_{e} = n_{h} = n_{i} \propto T^{3/2}$$

#### Conductivity
An electric field is applied across an SC,
![[Pasted image 20240128175228.png]]

$$
\begin{split}
i &= i_{e} + i_{h} \\
i &=  n_{e} A e v_{e} + n_{h} A e v_{h} \\
\frac{i}{A} = J &=  n_{i}e (v_{e} + v_{h}) \\
\end{split}
$$
And we get, conductivity,
$$
\begin{split}
\sigma &=  \frac{J}{E} = n_{i}e \left( \frac{v_{e}}{E} + \frac{v_{h}}{E} \right) \\ \\
\sigma &=  n_{i}\ e\ (\mu_{e} + \mu_{h})
\end{split}
$$
where,
$n_{e},n_{h}\to$ density of e, h
$v_{e},v_{h}\to$ drift velocity of e, h
$\mu_{e},\mu_{h}\to$ mobility of e, h and it will have unit $\ce{ m^{2} V^{-1} s ^{-1} }$

The inverse of conductivity is resistivity,
$$\rho = \frac{ 1 }{ \sigma }$$

## Extrinsic
Impure SC. 
We mix impurities. The impurities mixed are those which has one less or one more e. Thus impurity cannot be of 14th group. 

We mix such that there is roughly one impurity per $10^{8}$ Si atoms. 

We mix atoms of either 13th or 15th group. 

When we dope with 15th group elements, $n_{e}$ becomes large, and if we do it with 13th group, $n_{h}$ becomes large. 

Due to this increase, conductivity is increased.

### n-Type
Negative Type. However, they do not actually have a -ve charge as the +ve charge is also increased which is the P nucleus. 

Mixing of 15th group elements (nitrogen family). Pentavalent impurities like P or As (arsenic).

The extra e of the impurity is the free e. 

The no of free e is increased, while the no of holes is decreased as the extra e combine with h to neutralize them.

![[Pasted image 20240128175924.png]]

$$n_{e} \gg n_{h}$$

The difference will be so large, that we can write,
$$i = i_{e}$$

On adding pentavalent atoms, another energy band is created which is called the Donor level. This level has a very small energy difference with the conduction band. 

![[Pasted image 20240128180100.png]]

**Mass Action Law,** The multiplication of e and h densities is still the square of intrinsic charge density.
$$n_{e}n_{h}= n_{i}^{2}$$

#### Conductivity
As $n_{e} \gg n_{h}$, the current due to holes will be negligible.

$$
\begin{split}
i &= i_{e} + i_{h} \\
i &=  n_{e} A e v_{e} \\
\end{split}
$$

And conductivity will be,
$$
\begin{split}
\sigma &= n_{e}e\mu_{e} + n_{h}e \mu_{h} n_{h} \\
&= n_{e} e \mu_{e} 
\end{split}
$$
Since $n_{e}$ is large, the conductivity is also large. 

### p-Type
Positive type. However, it is not actually +vely charged. 

Mixing of 13th group elements. Tetravalent impurities are added, like Al, Ga. 

Since there are not enough e, the no. of holes is increased dramatically.  And since there are more holes, they accept free e and the no. of free e is decreased. 

![[Pasted image 20240128181443.png]]

$$n_{h} \gg n_{e}$$
This difference is so high that,
$$i = i_{h}$$

Here too, mass action is valid,
$$n_{e}n_{h}= n_{i}^{2}$$

An extra, acceptor level is created. 
![[band diagram in ptype.png]]

#### Conductivity
As $n_{h} \gg n_{e}$, the current due to free e will be negligible.

$$
\begin{split}
i &= i_{e} + i_{h} \\
i &=  n_{h} A e v_{h} \\
\end{split}
$$

And conductivity,
$$
\begin{split}
\sigma &= n_{e}e\mu _{e} + n_{h} e\mu_{h} \\
&= n_{h} e\mu_{h}
\end{split}
$$

