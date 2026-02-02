Links: [[01 Ohm's Law]]
___
# Equivalent Resistance 
When there are many resistances in circuit, then we can replace all of them with one resistance. This resistance is known as Equivalent Resistance. 
This $R_{eq}$ will draw the same amount of current from battery as the many resistances combined and produce the same amount of heat. 

$$R_{eq} = \frac{ V }{ i }$$

![[Pasted image 20231220105236.png]]

### Series Combination 
When resistances are joined end to end and they all have the same current. 

Potential will drop at every resistance. 

$$
\begin{split}
V_{1} &= iR_{1}\\
V_{2} &= iR_{2} \\
V_{3} &= iR_{3}
\end{split}
$$
I.e. 
$$V \propto R$$

Applying KVL,
$$
\begin{split}
V - iR_{1} - iR_{2} - iR_{3} &= 0\\
V &= iR_{1} + iR_{2} + iR_{3} \\
\frac{ V }{ i } &= R_{1} + R_{2} + R_{3} \\
\end{split}
$$

Thus giving,
$$R_{eq} = R_{1} + R_{2} + R_{3} + \dots$$

![[Pasted image 20231220105621.png]]

Now, Power dissipated by each resistance,
$$
\begin{split}
P_{1} &= i^{2} R_{1} \\
P_{2} &= i^{2} R_{2} \\
P_{3} &= i^{2} R_{3}
\end{split}
$$
I.e. 
$$P \propto R$$

Net power,
$$
\begin{split}
P_{net} &= i^{2} (R_{1} + R_{2} + R_{3}) \\
&= i^{2} R_{eq}
\end{split}
$$

### Parallel Combination 
When resistances have same potential difference across all of them. 

Current will be divided.

$$
\begin{split}
i_{1} &= \frac{ V }{ R_{1} } \\
i_{2} &= \frac{ V }{ R_{2} } \\
i_{3} &= \frac{ V }{ R_{3} }
\end{split}
$$
I.e.,
$$i \propto \frac{ 1 }{ R }$$

Applying KCL,
$$
\begin{split}
i &= i_{1} + i_{2} + i_{3} \\
\frac{ V }{ R_{eq} } &= \frac{ V }{ R_{1} } + \frac{ V }{ R_{2} } + \frac{ V }{ R_{3} } 
\end{split}
$$

Thus giving,
$$\frac{1}{R_{eq}} = \frac{1}{R_{1}} + \frac{1}{R_{2}} + \frac{1}{R_{3}} + \dots$$

![[Pasted image 20231220111114.png]]

Power dissipated by each resistance,
$$
\begin{split}
P_{1} &= \frac{ V^{2} }{ R_{1} } \\
P_{2} &= \frac{ V^{2} }{ R_{2} } \\
P_{3} &= \frac{ V^{2} }{ R_{3} } 
\end{split}
$$
I.e.,
$$P \propto \frac{ 1 }{ R }$$

#### Division
We have,
$$i_{1} + i_{2} + i_{3} = i_{o}$$
$$i_{1} : i_{2} : i_{3} :: \frac{ 1 }{ R_{1} } : \frac{ 1 }{ R_{2} } : \frac{ 1 }{ R_{3} }$$

Using this we have,
$$
\begin{split}
i_{1} &= \frac{ \frac{ 1 }{ R_{1} } }{ \frac{ 1 }{ R_{1} } + \frac{ 1 }{ R_{2} } + \frac{ 1 }{ R_{3} } } \times i_{o} \\
&= \frac{ \frac{ 1 }{ R_{1} } }{ \frac{ 1 }{ R_{eq} } } i_{o} \\
&= \frac{ R_{eq} }{ R_{1} } i_{o}
\end{split}
$$

Thus we have,
$$
\begin{split}
i_{1} &= \frac{ R_{eq} }{ R_{1} } i_{o} \\
i_{2} &= \frac{ R_{eq} }{ R_{2} } i_{o} \\
i_{3} &= \frac{ R_{eq} }{ R_{3} } i_{o} 
\end{split}
$$

![[Pasted image 20231220111514.png]]


##### Binary Division 
Here,
$$i_{1} + i_{2} = i_{o}$$
$$R_{eq} = \frac{ R_{1} R_{2} }{ R_{1} + R_{2} }$$
$$i_{1} R_{1} = i_{2}R_{2}$$
$$\frac{ i_{1} }{ i_{2} } = \frac{ R_{2} }{ R_{1} }$$

Thus we get,
$$i_{1} = \frac{ R_{2} }{ R_{1} + R_{2} } i_{o}$$
$$i_{2} = \frac{ R_{1} }{ R_{1} + R_{2} } i_{o}$$


![[Pasted image 20231220111530.png]]

Example,
![[Pasted image 20231220112304.png]]

## Wheatstone Bridge 
There are 4 junction, 2 are connected to 2 other and the rest 2 are connected to 3 junctions. 

There are a total of 5 resistors. 

Under balanced condition, the central arm has 0 current. 

Since there is no current through $R_{5}$,
$$V_{C} = V_{D}$$

$$
\begin{split}
i = \frac{ V_{A} - V_{C} }{ R_{1} } &= \frac{ V_{C} - V_{B} }{ R_{2} } \\
\frac{ V_{A} - V_{C} }{ V_{C} - V_{B} } &= \frac{ R_{1} }{ R_{2} } \\
\\
I = \frac{ V_{A} - V_{D} }{ R_{3} } &= \frac{ V_{D} - V_{B} }{ R_{4} } \\
\frac{ V_{A} - V_{D} }{ V_{D} - V_{B} } &= \frac{ R_{4} }{ R_{3} } \\
\end{split}
$$

Equating them,
$$
\begin{split}
\frac{ R_{1} }{ R_{2} } &= \frac{ R_{3} }{ R_{4} } \\
R_{1} R_{4} &= R_{3} R_{2}
\end{split}
$$
This is called **Balanced WSB.**

![[Pasted image 20231220112828.png]]


When the WSB is balanced, the top and bottom two resistances will be in series and they themselves will be in parallel. 

Thus $R_{eq}$ comes out to be,
$$R_{eq} = \frac{ (R_{1} + R_{2})(R_{3} + R_{4}) }{ R_{1} + R_{2} + R_{3} + R_{4} }$$

![[Pasted image 20231220113508.png]]

Example,
![[Pasted image 20231220113753.png]]
