Links: [[01 Types of SC]]
___
# PN Junction
aka **PN Diode**

When dope half of the material with P-type and the other half with N-type. The junction formed is called PN junction. 
We will not connect a P-type and an N-type SCs.

When we do this kind of doping, there is a diffusion, and the e move from N-type to the P-type. 

Due to this, the P side will be -vely charged and the N side will be +vely charged. 

![[Pasted image 20240128184732.png]]
![[Pasted image 20240128185817.png]]

#### Definitions 

##### Depletion Region
The region blocks the flow of charges from N side to the P side. It has very small thickness. 

The P side is at low potential and the N side is at higher potential. 
Thus there will be an electric field from N to P. 

Due to this field, if there is e or h in the region, they will be pulled to the N or P side. 
There will be no free e or h. 

##### Diffusion Current 
The current due to the diffusion of e and h. 
The diffusion current is from P to N. 
It is present when there is no potential difference across the SC.  


##### Barrier Voltage
aka **Junction Voltage or Knee Voltage or Contact Potential** 

The N side will be at slightly higher potential than P side. This difference is potential is called Potential Barrier. 
$$\Delta V = Ed$$ 

![[Pasted image 20240128190220.png]]

e having KE more than or equal to $e\Delta V$ can cross the barrier.

For Si, $\Delta V = 0.7$ V.
For Ge, $\Delta V = 0.3$ V.

![[Pasted image 20240128191739.png]]

##### Drift Current 
Inside the depletion region, if any e-h pair is generated, the electric field drags the e towards N and h towards P. 

Due to this movement of e and h, there will be a current from N to P. 

This current is called **drift current.** 

At steady state,
$$i_\text{diffusion} = i_\text{drift}$$

![[Pasted image 20240128191346.png]]

## PN Diode 
The P side is the base of triangle and the N side is the flat line. 

![[Pasted image 20240128191450.png]]

### Forward Biasing
When the P side is connected to higher and the N side is connected to the lower potential of a battery. 

The battery should have more potential than $\Delta V$ for current to flow. 

On connecting this battery, we make an external electric field which supports diffusion. 

Due to this, diffusion current will increase. 
$$i_\text{diffusion} \gg i_\text{drift}$$

Also, since P side is at higher potential and N side at a lower potential, h and e will experience force towards the depletion layer.

This will cause the thickness of depletion layer to be decreased, and thus barrier voltage and the resistance will be decreased. 

![[Pasted image 20240128192100.png]]

If the applied potential is less than $\Delta V$, there will be no current. 

We replace non ideal diode with a cell of the same potential and which has its +ve terminal on the P side and the -ve terminal on the N side. 

##### Current vs Potential Graph 
It is not a straight line as resistance is not constant.

The potential at which current just starts flowing is called **Knee Voltage.** This is the same as Barrier Voltage. 

The current is varying exponentially with the potential,
$$i = i_{o} (e^{ eV/kT } - 1)$$
where $i_{o}$ is reverse saturation current and k is Boltzmann's constant.

If V becomes very large,
$$i = i_{o} e^{ eV/kT }$$

![[Pasted image 20240128192442.png]]

### Reverse Biasing
When the P side is connected to lower and the N side is connected to the higher potential of a battery. 

Due to this applied potential, there will be an electric field which will support drift current.

Since N side is at higher potential and P at lower, the h and e are attracted away from the depletion region. 

Thus thickness of depletion layer is increased and the barrier potential increases.

The diffusion current will thus decrease. 
$$i_\text{diffusion} \to 0$$

But there will be drift current in the order of $\mu A$. 

![[Pasted image 20240128193233.png]]

Thus the PN diode will behave like a high resistance. 

The graph will be like,
![[Pasted image 20240128193345.png]]

### Dynamic Resistance
Since resistance is constantly changing, we cannot define resistance as $V = iR$. 

Here, we will define resistance as change in potential over change in current.
$$R_{D} = \frac{ dV }{ di }$$

Now,
$$
\begin{split}
\tan \theta &= \text{slope} \\
&= \frac{ di }{ dV } \\
\end{split}
$$

Thus,
$$R_{D} = \frac{ dV }{ di } = \frac{1}{\text{slope}}$$

Since slope is increasing, the dynamic resistance is decreasing.

We can also define dynamic conductance,
$$
\begin{split}
S_{D} &= \frac{ 1 }{ R_{D} } \\ 
&= \frac{ di }{ dV } \\
&= \tan \theta \\
&= \text{slope}
\end{split}
$$

![[Pasted image 20240128193816.png]]

In Forward vs Reverse biasing, we have, graph,

![[Pasted image 20240128194139.png]]

### Ideal vs Non Ideal Diode 
If nothing is said, we consider the diode to be ideal.

##### Ideal diode
In forward biasing, 
$$R_{D} \to 0 \implies i \to \infty$$
And the diode will behave like a **short wire.**

In reverse basing,
$$R_{D} \to \infty \implies i \to 0$$
And the diode will behave like a **broken wire.**

And the graph will look like,
![[Pasted image 20240128194404.png]]

##### Non-Ideal diode
In forward biasing, 
$$R_{D} \to \text{small} \implies i \to \text{large}$$
And the diode will behave like a **low resistance wire.**

In reverse biasing, 
$$R_{D} \to \text{large} \implies i \to \text{small}$$
And the diode will behave like a **high resistance wire.**

And the graph will look like,
![[Pasted image 20240128195111.png]]

### Breakdown of PN Diode
If we apply a large voltage in reverse bias to a PN diode, the electric field will be so large that it will break out the e from the covalent bond.

As the bonds will break, there will be an increase in free e and holes.

Due to this, there will be a large drift current from N to P. Thus the dynamic resistance will be zero. 

The potential at which this happens is called **Breakdown Voltage or Zenner Voltage or Avalanche Voltage, $V_{Z}$.** 

![[Pasted image 20240128195549.png]]

![[Zenner Breakdown.png]]

### Photodiode 
It is PN diode which is sensitive to light. It only works in reverse bias. 

Here, the small current in reverse bias is called **Dark Current.** It is in $\mu A$.

Now, if we illuminate this photodiode, a lot of new e-h pairs will be generated due to many e crossing the forbidden energy gap.

Due to this, the current will go from $\mu A$ to $mA$. This new current is called **Bright Current.**

But this only happens if the photons have sufficient energy. 

![[Pasted image 20240128205536.png]]

### Light Emitting Diode (LED)
It is a PN junction which works in forward bias. 

The holes and e will recombine. This will release energy in the form of photons. 

This energy lost is converted to photons of certain wavelength,
$$\Delta E_{g} = \frac{ hc }{ \lambda }$$

![[Pasted image 20240128205939.png]]

## Examples 
![[Pasted image 20240128195930.png]]

![[Pasted image 20240128200311.png]]

![[Pasted image 20240128204322.png]]
![[Pasted image 20240128204351.png]]

![[Pasted image 20240128204521.png]]

