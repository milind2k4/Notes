Links: [[01 Ohm's Law]], [[03 Kirchhoff's Laws]], [[04 Equivalent Resistance]]
___
# Instruments
## Galvanometer/Micro-ammeter 
It was proposed by Hans Christian Oersted in 1820. 

Galvanometer is used to detect current in circuit. 
It can measure small current (of the order mA or $\mu$A).

It is based on the concept of torque on a current carrying loop in a magnetic field. 

The more the current is, the more the deflection will be.

$$\phi c = inAB$$

And, Current Sensitivity is defined as,
$$\frac{ \phi }{ i } = \frac{ \text{deflection} }{ \text{current} } = \frac{ nAB }{ c }$$

![[Pasted image 20231220173617.png]]

#### Uni and Bi-directional Galvanometer 
The needle's starting position is at the right most point in *Unidirectional* Galvanometer.
The needle's starting position is at the middle in *Bidirectional* Galvanometer.

The current for which the deflection is max. is represented as $i_{g}$. 

If $i \leq i_{g}$, then galvanometer can detect as well as measure the current. 
If $i > i_{g}$, the needle will stay at its max. deflection and we cannot measure the current. 

If $i > i_{g}$, the galvanometer can get damaged. 

![[Pasted image 20231220174528.png]]

## Ammeter
It is a modified galvanometer which is used to measure current in a circuit. 

$R_{g}$ is resistance of galvanometer. Practically, it is $50\ \ohm$.

To modify the galvanometer, we add a resistance S, called **Shunt** in parallel with it. 

Now,
$$
\begin{split}
i_{1} &= \frac{ S }{ S + R_{g} } i \\
i &= \left( \frac{ R_{g} + S }{ S } \right)i_{1}
\end{split}
$$

Here $i_{1}$ will be the current measured by the galvanometer and it will be small. 

We can take S as we need to have the galvanometer measure any current.

This shunt can be given using the fact that the potential difference across both the shunt and the galvanometer is the same,
$$i_{g}R_{g} = (i_{max} - i_{g})S$$

To calibrate the reading, we multiply the readings of galvanometer by $(R_{g} + S) /S$ and replace the markings. 

The max. current measured by the ammeter is,
$$i_{max} = \frac{ R_{g} + S }{ S } i_{g}$$
The lower the shunt is, the more max. current we can measure. 

The resistance of ammeter is,
$$R_{A} = \frac{ R_{g}S }{ R_{g} + S }$$

![[Pasted image 20231220175327.png]]

![[Pasted image 20231220175427.png]]

#### How to use Ammeter 
If we have to measure current in a circuit, then we connect the ammeter in series with the circuit. 

However, when ammeter is connected in series, the actual current is decreased a bit due to its resistance. 

Thus, the lower is the resistance of ammeter, the lower will be error. An ideal ammeter has zero resistance. 

We know that,
$$R_{A} = \frac{ R_{g}S }{ R_{g} + S }$$

Good ammeters have small resistance and for that the value of shunt should be very small. 

If $S \ll R_{g}$,
$$R_{A} = \frac{ R_{g}S }{ R_{g} } = S$$
Since S is small, $R_{A}$ is also small. 

![[Pasted image 20231220180850.png]]

![[Pasted image 20231220181543.png]]

## Voltmeter
It is a modified galvanometer used to measure potential difference.

It is made by connecting a high resistance in series with the galvanometer. The higher the resistance is, the higher $V_{max}$ will be.

Resistance of voltmeter is,
$$R_{V} = R_{g} + R$$

Voltage across voltmeter will be,
$$
\begin{split}
V_{AB} &= i(R_{g} + R) \\
&= iR_{V}
\end{split}
$$

Max. potential difference that voltmeter can measure,
$$V_{max} = i_{g}(R_{g} + R) = i_{g}R_{V}$$

![[Pasted image 20231220195006.png]]

#### How to use Voltmeter 
We connect the voltmeter in parallel with the component across which we want to measure potential difference. 

The reading will have some error however as we are changing the circuit. To minimise this error, the resistance of voltmeter should be high so that very little current passes through it.

An ideal voltmeter has infinite resistance so that no current passes through it.

![[Pasted image 20231220195648.png]]

### Example
![[Pasted image 20231220200554.png]]
![[Pasted image 20231220200940.png]]
![[Pasted image 20231220200948.png]]

## Meter Bridge
It is an experiment to determine unknown resistance. It is based on [[04 Equivalent Resistance#Wheatstone Bridge|Balanced Wheatstone Bridge.]]

There is a uniform wire of 1 m length connected to a battery.
There are three thick metallic strips.

Thick metallic strips are used so that their resistance is as low as possible. 

Between two of the three, a known resistance is attached and between the other two, the unknown resistance is connected. 

There is a galvanometer connected to the middle strip and it is connected to a jockey which moves on the wire. 

The point at which the galvanometer shows zero reading is called the **Null point** and its distance from A is called **Balancing Length.**

![[Pasted image 20231220201753.png]]

The circuit diagram of this is,
![[Pasted image 20231220201830.png]]

Since there is no current in the middle arm,
$$
\begin{split}
\frac{ R\rho (100 - l) }{ A } &= \frac{ X \rho l }{ A } \\
\frac{ X }{ R } &= \frac{ 100-l }{ l } \\
X &= \left( \frac{ 100-l }{ l } \right) R
\end{split}
$$
We can write this as,
$$R(100 - l) = Xl$$

#### Error in Measurement 
In the measurement of l, the max error will be $dl$, which can be 0.1 cm. 
Due to this there will be some error in the measurement of X.

We have,
$$
\begin{split}
X &= \frac{ 100 - l }{ l } R \\
\ln X &= \ln(100 - l) + \ln R - \ln l \\
\end{split}
$$
Differentiating this, 
$$
\begin{split}
\frac{ dX }{ X } &= \frac{ -dl }{ 100 - l } + \cancelto{ 0 }{ \frac{ dR }{ R } } - \frac{ dl }{ l } \\
\\
\text{Since error is always +ve}, \\
\frac{ dX }{ X } &= \frac{ dl }{ 100 - l } + \frac{ dl }{ l } \\
&= \frac{ dl(100) }{ (100-l)l }
\end{split}
$$

Thus, fractional error in unknown resistance,
$$\frac{ dX }{ X } = \frac{ 100 dl }{ (100 - l)l }$$
where dl and l are to be put in cm. 

Now, for least error, since 100dl is fixed, denominator should be the max..
I.e. $100l - l^{2}$ should be max.. 

$$
\begin{split}
f'(l) &= 100 - 2l = 0\\
l &= 50\ cm
\end{split}
$$
Thus, the error will be the min. in the middle region of the wire. The max. error will be at either corner.

## Potentiometer
(not in syllabus)

A device used to measure pd or find the value of potential of a cell. It is more accurate than a Voltmeter. 

Let the potential per unit lenght be $x$,
$$x = \frac{V}{l}$$

![[Pasted image 20230107172709.png|500]]

For $i_{g} = 0$
$$\varepsilon = \varepsilon_{o}$$
$$\varepsilon = \frac{Vd}{l}$$

![[Pasted image 20230107172719.png|300]]

