Links: [[00 Semiconductors]], [[02 PN Junction]]
___
# Transistors
#removed from JEE 24

It has 2 p-n junctions. 

**Base:** The middle one. Thinnest. 

**Emitter** & **Collector** have the same type of doping. 
The collector is the thickest one. The emitter is less thick than the collector. 
Emitter is heavily doped. Collector is less heavily doped.

##### NPN Transistor

![[npn transistor.png]]

![[npn transistor current.png]]

The arrow is from P to N.


##### PNP Transistor 

![[pnp transistor.png]]

![[pnp transistor current.png]]

The arrow is from P to N.

### Kirchhoff's Junction Rule:
$$i_{e} = i_{b}+ i_{c}$$
$$\Delta i_{e} = \Delta i_{b} + \Delta i_{c}$$
$$di_{e} = di_{b}+ di_{c}$$

$$i_{b} \to \text{Very small}$$
Thus,
$$i_{c} ≲ i_{e}$$

### Current Gain ($\alpha , \beta$)

Current Gain $\alpha$:
$$\alpha = \frac{i_{c}}{i_{e}} = \frac{ \Delta i_{c} }{ \Delta i_{e} } ≲ 1\ (\text{as } i_{c} ≲ i_{e})$$

Current Gain $\beta$:
$$\beta = \frac{i_{c}}{i_{b}} = \frac{ \Delta i_{c} }{ \Delta i_{b} } \gg 1\ (\text{as } i_{b} \to 0)$$

#### Relation between $\alpha \& \beta$
$$i_{e} = i_{b}+ i_{c}$$
Dividing whole equation by $i_{c}$,
$$\frac{i_{e}}{i_{c}} = \frac{i_{b}}{i_{c}} + \frac{i_{c}}{i_{c}}$$
$$\frac{1}{\alpha} = \frac{1}{\beta} + 1$$
$$\alpha = \frac{\beta}{1+\beta }$$
$$\beta = \frac{\alpha}{1-\alpha}$$


## Common Base Amplifier

![[common base amplifier.png]]

The Emitter Base junction is in forward bias and the Collector Base junction is in Reverse Bias.

Current Amplification,
$$\alpha = \frac{i_{c}}{i_{e}} = \frac{ \Delta i_{c} }{ \Delta i_{e} }$$

Voltage Amplification,
$$A_{V} = \frac{V_{out}}{V_{in}} = \frac{ i_{c}R_{out} }{ i_{e}R_{in} } = \alpha \left( \frac{ R_{out} }{ R_{in} } \right)$$

Power Amplification,
$$A_{P} = \frac{ P_{out} }{ P_{in} } = \frac{ i_{c}^{2}R_{out} }{ i_{e}^{2}R_{in} } = \alpha ^{2} \left( \frac{ R_{out} }{ R_{in} } \right)$$


## Common Emitter Amplifier

![[comon emmiter amplifier.png]]

The Emitter Base junction is in forward bias and the Collector Base junction is in Reverse Bias.

Current Amplification,
$$\beta = \frac{i_{c}}{i_{b}} = \frac{ \Delta i_{c} }{ \Delta i_{b} }$$

Voltage Amplification,
$$A_{V} = \frac{V_{out}}{V_{in}} = \frac{ i_{c}R_{out} }{ i_{b}R_{in} } = \beta \left( \frac{ R_{out} }{ R_{in} } \right)$$

Power Amplification,
$$A_{P} = \frac{ P_{out} }{ P_{in} } = \frac{ i_{c}^{2}R_{out} }{ i_{b}^{2}R_{in} } = \beta^{2} \left( \frac{ R_{out} }{ R_{in} } \right)$$













