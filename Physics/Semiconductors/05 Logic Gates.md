Links: [[00 Semiconductors]], [[01 Operations]]
___
# Logic Gates
#important

There are two types of signals,
- **Analog signal** which is a time varying continuous voltage/current which has some message or info.
	![[Pasted image 20240128210924.png]]
	$\\$
	
- **Digital signal** which is discontinuous signal. Only two values are possible. High voltage is represented as 1 and low as 0. 
  
	Digital Signal is better than Analog as it is more efficient, cheaper and flexible. It is also not affected by outside noise. 
	
	All the electronic devices use digital signals. 


**Logic gate** is an electronic device which follows logical relationship between input and output digital signals. 

The no. of input can be either 1 or 2, but there will be only one output. 

There are 3 basic gates,
- NOT
- AND
- OR

The rest gates are made using these basic gates.

**Truth Table** is a table/chart which consists of all possible input combinations and their corresponding output.

#### NOT Gate
[[01 Operations#Negation NOT $( sim{p})$]]

aka **Inverter Gate**

One input one output. The output is represented as $\bar{A}$.

Inverts Input. i.e. 
High Voltage $\to$ Low Voltage 
Low Voltage $\to$ High Voltage

Truth Table:

| $A$ | $\bar{A}$ |
| --- | --------- |
| 0   | 1         |
| 1   | 0         |

It is a reversible or recoverable gate. I.e. if we connect two NOTs, we get the original input back.

![[not.png]]

The IC (Integrated Circuit) of this gate has number 7404 and has internal circuit diagram,

![[IC 7404 internal structure.png]]

##### Circuit
NOT gate can be understood using this circuit,
![[Pasted image 20240128212549.png]]

#### OR Gate
[[01 Operations#Disjunction OR $(p vee q)$]]

Two inputs one output.

If any one of the inputs is high, the output will be high.

Truth Table:

| $A$ | $B$ | $A+B$ |
| --- | --- | ----- |
| 0   | 0   | 0     |
| 0   | 1   | 1     |
| 1   | 0   | 1     |
| 1   | 1   | 1     |

![[or.png]]

The IC of this gate has number 7432 and has internal circuit,

![[IC 7432 internal structure.png]]

##### Circuit
OR gate can be understood using this circuit,
![[Pasted image 20240128212745.png]]

##### Graph 
In graph view, OR can be shown as,
![[Pasted image 20240128213018.png]]

#### AND Gate
Two input one output.

If both inputs are high voltage, then only the output will be high voltage. 

Truth Table:

| $A$ | $B$ | $A \cdot B$ |
| --- | --- | ----------- |
| 0   | 0   | 0           | 
| 0   | 1   | 0           |
| 1   | 0   | 0           |
| 1   | 1   | 1           |

![[and.png]]

The IC of this gate has number 7408 and has internal circuit,

![[IC 7408 internal structure.png]]

##### Circuit
AND gate can be understood using this circuit,
![[Pasted image 20240128213534.png]]

##### Graph 
In graph view, AND can be shown as,
![[Pasted image 20240128213611.png]]

### NOR Gate
OR + NOT
Two input one output.

The output will be 1 when both inputs are 0.

This gate is also called *universal gate* as we can make all other gates using it.

Truth Table:

| $A$ | $B$ | $\overline{A+B}$ |
| --- | --- | ---------------- |
| 0   | 0   | 1                |
| 0   | 1   | 0                |
| 1   | 0   | 0                |
| 1   | 1   | 0                |

![[nor.png]]

The IC of this gate has number 7402 and has internal circuit,

![[IC 7402 internal structure.jpg]]

> [!Caution] 
> The input and output pins of this IC are different from the rest.

##### Graph 
In graph view, NOR can be shown as,
![[Pasted image 20240128213805.png]]

### NAND Gate
AND + NOT
Two input one output.

The output will be 0 when both the inputs are 1.

This gate is also called *universal gate* as we can make all other gates using it.

Truth Table:

| $A$ | $B$ | $\overline{A \cdot B}$ |
| --- | --- | ---------------------- |
| 0   | 0   | 1                      |
| 0   | 1   | 1                      |
| 1   | 0   | 1                      |
| 1   | 1   | 0                      |

![[nand.png]]

The IC of this gate has number 7400 and has internal circuit,

![[IC 7400 internal structure.png]]

##### Graph 
In graph view, NAND can be shown as,
![[Pasted image 20240128213953.png]]

## XOR Gate
[[01 Operations#Inclusive and Exclusive OR]]

Exclusive OR.
Two input one output.

The output will be 0 when both inputs are the same. 

We can write,
$$A \oplus B = (A.\bar{B}) + (\bar{A}.B)$$

Truth Table:

| $A$ | $B$ | $A \oplus B$ |
| --- | --- | ------------ |
| 0   | 0   | 0            | 
| 0   | 1   | 1            |
| 1   | 0   | 1            |
| 1   | 1   | 0            |

![[xor.png]]
![[Pasted image 20240128214610.png]]

The IC of this gate has number 7486 and has internal circuit,

![[IC 7486 internal structure.jpg]]