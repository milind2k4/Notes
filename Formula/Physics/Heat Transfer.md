Links: [[00 Heat Transfer]]
___
# Heat Transfer 
### Conduction 
Thermal current,
$$i_{th} = \frac{ dQ }{ dt }$$
Energy flux,
$$EF = \frac{ i }{ A }$$

Temp. gradient,
$$\frac{ dT }{ dx } = \frac{ T_{L} - T_{H} }{ l - 0 } < 0$$
#### Ohm's Law
$$i_{th} = -kA \frac{ dT }{ dx }$$

Thermal resistance,
$$R_{th} = \frac{ l }{ kA }$$

#### Kirchhoff's Law
$$\sum i = 0$$

#### Combination of Rods
Series combination,
$$R_{eq} = R_{1} + R_{2}$$

Parallel combination,
$$\frac{ 1 }{ R_{eq} } = \frac{ 1 }{ R_{1} } + \frac{ 1 }{ R_{2} }$$

Current division,
$$\frac{ i_{1} }{ i_{2} } = \frac{ R_{2} }{ R_{1} }$$

### Radiation
Solar constant (S) is the intensity on earth. 

Energy conservation,
$$
\begin{split}
\frac{ P_{abs} }{ P_{in} } + \frac{ P_{ref} }{ P_{in} } + \frac{ P_{tra} }{ P_{in} } &= 1 \\
a + r + t &= 1
\end{split}
$$

Absorptive Power,
$$a = \frac{ P_{abs} }{ P_{in} }$$
If there is no transmission,
$$a = 1 - r$$

Emissive power,
$$E = \frac{ P_{emit} }{ A } \propto T^{4}$$

Spectral Emissive power,
$$E_{\lambda} = \frac{ dE }{ d\lambda }$$

#### Perfectly Black Body 
$$P_{in} = P_{abs}$$

Ferry's Black Body,
$$P_{out} = (1-a)^{n}P_{o}$$

Emissivity,
$$e = \frac{ E }{ E_{o} }$$
where $E_{o}$ is the emissive power of a PBB.

#### Laws
Kirchhoff's Law,
$$\frac{ E_{1} }{ a_{1} } = \frac{ E_{2} }{ a_{2} }$$
If one of the bodies is a PBB,
$$a = e$$
This formula is valid for all objects. 

Stefan Boltzmann Law,
$$
\begin{split}
P_{emit} &= \sigma eAT^{4} \\
E_{abs} &= \sigma aAT^{4}
\end{split}
$$
**Newton's Law of Cooling,**
$$\frac{ d[T] }{ dt } = -k(T - T_{s})$$

Wien's displacement law,
$$\lambda_{m} = \frac{ 1 }{ T }$$
$\lambda_{m}$ is the wavelength of the max. emissions. 