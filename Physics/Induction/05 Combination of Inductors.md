Links: [[04 Equivalent Resistance]], [[03 Combination of Capacitors]]
___
# Combination of Inductors 
### Inductors is Series 
If they are very far, then we sum their self inductances. 
$$L_{eq} = L_{1} + L_{2}$$

However, if they are close to each other, mutual inductance will be considered and 2 cases will be made. 

##### Aiding Combination 
When the flux is in the same direction. 

They will increase the equivalent inductance. 

$$L_{eq} = L_{1} + L_{2} + 2M$$

![[Pasted image 20240117215519.png]]

##### Opposing Combination 
When the flux is in opposite directions. 

They will decrease the equivalent inductance. 

$$L_{eq} = L_{1} + L_{2} - 2M$$

![[Pasted image 20240117215547.png]]

### Parallel Combinations 
We will not consider mutual inductance in parallel combination. 

Parallel combination will be when the potential differences will be the same across each inductor. 

$$
\begin{split}
V_{A} - V_{B} &= L_{1} \frac{ di_{1} }{ dt } \\
&= L_{2} \frac{ di_{2} }{ dt } \\
&= L_{3} \frac{ di_{3} }{ dt }
\end{split}
$$

And we can write,
$$V_{A} - V_{B} = L_{eq}\frac{ di }{ dt }$$

Using KCL, we have,
$$
\begin{split}
i &= i_{1} + i_{2} + i_{3} \\
\frac{ di }{ dt } &= \frac{ di_{1} }{ dt } + \frac{ di_{2} }{ dt } + \frac{ di_{3} }{ dt } \\
\frac{ V_{A} - V_{B} }{ L_{eq} } &= \frac{ V_{A} - V_{B} }{ L_{1} } + \frac{ V_{A} - V_{B} }{ L_{2} } + \frac{ V_{A} - V_{B} }{ L_{3} } 
\end{split}
$$

Thus we get,
$$\frac{ 1 }{ L_{eq} } = \frac{ 1 }{ L_{1} } + \frac{ 1 }{ L_{2} } + \frac{ 1 }{ L_{3} }$$

And the current will be divided inversely proportional to inductance. 

$$L_{1}i_{1} = L_{2}i_{2} = L_{3}i_{3}$$

![[Pasted image 20240117220832.png]]
