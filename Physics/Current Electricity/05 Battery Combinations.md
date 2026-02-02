Links: [[02 Circuit Theory]]
___
# Battery Combinations
### Series Combination 
When batteries are connected end to end. 

$$
\begin{split}
V_{A} - V_{B} &= (\varepsilon_{n} - ir_{n}) + \dots + (\varepsilon_{2} - ir_{2}) + (\varepsilon_{1} - ir_{1}) \\
V_{A} - V_{B} &= (\varepsilon_{1} + \varepsilon_{2} + \dots + \varepsilon_{n}) - i(r_{1} + r_{2} + \dots + r_{n})
\end{split}
$$
We can write,
$$V_{A} - V_{B} = \varepsilon_{eq} - ir_{eq}$$

Where,
$$\varepsilon_{eq} = \varepsilon_{1} + \varepsilon_{2} + \varepsilon_{3} + \dots$$
$$r_{eq} = r_{1} + r_{2} + r_{3} + \dots$$

![[Pasted image 20231220115951.png]]

Each emf has to be written with polarity. 

![[Pasted image 20231220120116.png]]

#### m identical cells in series 
And all of them have polarity in same direction. 

Each cell has emf $\varepsilon$ and resistance $r$. 

The whole arrangement can be replaced with a single cell,
$$
\begin{split}
\varepsilon_{eq} &= m\ \varepsilon \\
r_{eq} &= m\ r
\end{split}
$$

![[Pasted image 20231220120424.png]]

Current will be,
$$i = \frac{ m\varepsilon }{ R + mr }$$

If $mr \ll R$,
$$i = \frac{ m\varepsilon }{ R }$$
and thus $i \propto m$. 
I.e. the series combination is beneficial.

If $mr \gg R$.
$$i = \frac{ m\varepsilon  }{ mr } = \frac{ \varepsilon }{ r }$$
and thus $i$ is independent of $m$. 
I.e. the series combination is not beneficial.

In home appliances, cells are connected in series. 
![[Pasted image 20231220120931.png]]

### Parallel Combination 
When the potential difference across them is the same.

Applying KCL at point A,
$$
\begin{split}
\frac{ x - \varepsilon_{1} }{ r_{1} } + \frac{ x - \varepsilon_{2} }{ r_{2} } + \frac{ x - \varepsilon_{3} }{ r_{3} } &= 0 \\
x \left( \frac{ 1 }{ r_{1} } + \frac{ 1 }{ r_{2} } + \frac{ 1 }{ r_{3} } \right) &= \frac{ \varepsilon_{1} }{ r_{1} } + \frac{ \varepsilon_{2} }{ r_{2} } + \frac{ \varepsilon_{3} }{ r_{3} }
\end{split}
$$

Thus, emf,
$$\varepsilon_{eq} = 
\frac{ \displaystyle \frac{ \varepsilon_{1} }{ r_{1} } + \frac{ \varepsilon_{2} }{ r_{2} } + \frac{ \varepsilon_{3} }{ r_{3} } + \dots}
{ \displaystyle \frac{ 1 }{ r_{1} } + \frac{ 1 }{ r_{2} } + \frac{ 1 }{ r_{2} } + \dots }$$
$$\varepsilon_{eq} = \frac{ \varepsilon_{1} /r_{1} + \varepsilon_{2} /r_{2} + \varepsilon_{3} /r_{3} + \dots }{ 1 /r_{eq} }$$

And, resistance,
$$\frac{ 1 }{ r_{eq} } = \frac{ 1 }{ r_{1} } + \frac{ 1 }{ r_{2} } + \frac{ 1 }{ r_{2} } + \dots$$

![[Pasted image 20231220121449.png]]

The emfs in the expression of equivalent emf are with signs,
![[Pasted image 20231220122309.png]]

#### n identical cells in parallel

Equivalent emf will be,
$$
\begin{split}
\varepsilon_{eq} &= \frac{ \frac{ n\varepsilon }{ r } }{ \frac{ n }{ r } } \\
&= \varepsilon 
\end{split}
$$

And equivalent resistance,
$$r_{eq} = \frac{ r }{ n }$$

![[Pasted image 20231220172125.png]]

The current in the circuit will be,
$$i = \frac{ n\varepsilon }{ nR + r }$$

If $nR \ll r$,
$$i = \frac{ n\varepsilon }{ r }$$
I.e. $i \propto n$. 
Parallel combination is beneficial when we need more current. 

If $nR \gg r$,
$$i = \frac{ n\varepsilon }{ nR } = \frac{ \varepsilon }{ R }$$
Thus parallel combination is not viable. 