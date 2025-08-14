Links: [[00 Complex Numbers]]
___
# Argument, Conjugate, Modulus 
$$z = a + ib,\ a,b \in R$$

Modulus of z,
$$|z| = \sqrt{ a^{2} + b^{2} }$$
which is distance of z from origin. 

Conjugate of z,
$$\bar{z} = a - ib$$
which is reflex of z in real axis. 

Argument of z,
$$arg(z) = \theta = 2n\pi + \theta$$
which is the angle made by radius vector of z with +ve real axis. 
However, argument of origin is not defined. 
$$arg(0) = \text{not defined}$$

Amplitude of z,
$$amp(z) = arg(z) \in (-\pi, \pi]$$
which is principle value of argument.

![[Pasted image 20231113094719.png]]


##### Finding Amplitude 
Let,
$$z = a + ib,\ a,b \in R$$
then find 
$$\theta = \tan ^{-1}\left| \frac{ b }{ a } \right|$$

Now,
$$
\begin{split}
amp(z) = \theta,\ \theta &\in 1^{st}\ Q \\
= \pi - \theta,\ \theta &\in 2^{nd}\ Q \\
= -(\pi - \theta),\ \theta &\in 3^{rd}\ Q \\
= -\theta,\ \theta &\in 4^{th}\ Q 
\end{split}
$$

For example,
![[Pasted image 20231113100812.png]]

#### Some Points to Note
Since $|z|$ is distance,
$$|z| \geq 0$$

If distance from origin is zero, i.e. ff $|z| = 0$ then $z = 0$.

Modulus is not absolute value,
$$|z| = 5 \centernot\implies z = \pm 5$$
There are infinite such points such as $3 + 4i$.

If z is purely real,
$$z = \bar{z}$$
$$arg(z) = 0\ or\ \pi\ or\ \text{undefined}$$   


If z is purely imaginary,
$$z = -\bar{z}$$
$$arg(z) = \pm\frac{\pi}{2}\ or\ \text{undefined}$$

Conjugate of conjugate,
$$\bar{(\bar{z})} = z$$

Distance of z and conjugate from origin,
$$|z| = |\bar{z}|$$

If no. and conjugate are given,
$$
\begin{split}
z &= a + ib \\
\bar{z} &= a - ib \\
Re(z) &= \frac{ z + \bar{z} }{ 2 } \\
Im(z) &= \frac{ z - \bar{z} }{ 2i }
\end{split}
$$

### Properties of Mod, Argument and Conjugate 

#### Properties of Mod
$$
\begin{split}
|z|^{2} &= z. \bar{z} \\
|\bar{z}| &= |z| \\
|z_{1}z_{2}| &= |z_{1}||z_{2}| \\
|z^{k}| &= |z|^{k} \\
\left| \frac{ z_{1} }{ z_{2} } \right| &= \frac{ |z_{1}| }{ |z_{2}| } 
\end{split}
$$

However, we cannot break over sum,
$$|z_{1} + z_{2}| \neq |z_{1}| + |z_{2}|$$
$$|z_{1} + z_{2}| \leq |z_{1}| + |z_{2}|$$
$$|z_{1} - z_{2}| \geq | |z_{1}| - |z_{2}| |$$
For equality,
$$arg(z_{1}) = arg(z_{2})$$
i.e. both are like vectors.

#### Properties of Conjugate
$$
\begin{split}
\overline{(\bar{z})} &= z \\
\overline{(z_{1} + z_{2})} &= \overline{z_{1}} + \overline{z_{2}} \\
\overline{z_{1}z_{2}} &= \overline{z_{1}}.\overline{z_{2}} \\
\overline{(z^{n})} &= (\bar{z})^{n} \\
\overline{\frac{ z_{1} }{ z_{2} }} &= \frac{ \overline{z_{1}} }{ \overline{z_{2}} } \\
\end{split}
$$
If $z_{1} = z_{2}$ then $\bar{z}_{1} = \bar{z}_{2}$.
And,
$$f(z) = 0 \implies \overline{f(z)} = 0$$

#### Properties of Argument 
Since z can be written in as exponential, arg has properties similar to log.

$$
\begin{split}
arg(z_{1}z_{2}) &= arg(z_{1}) + arg(z_{2}) \\
arg(z^{k}) &= k.arg(z) \\
arg\left( \frac{ z_{1} }{ z_{2} } \right) &= arg(z_{1}) - arg(z_{2}) \\
arg(\bar{z}) &= -arg(z) \\
arg(kz) &= arg(z),\ \ce{ if }\ k \in R^{+} \\
&= \pi + arg(z),\ \ce{ if }\ k \in R^{-}
\end{split}
$$
In all of the above the RHS has $+ 2k\pi$ as arg gives angle.

#### Square formula
Using the properties we have,
$$
\begin{split}
|z_{1} + z_{2}|^{2} &= (z_{1} + z_{2}). (\bar{z}_{1} + \bar{z}_{2}) \\
&= z_{1}\bar{z}_{1} + z_{2}\bar{z}_{2} + \bar{z}_{1}z_{2} + z_{1}\bar{z}_{2} \\
\end{split}
$$
Thus,
$$|z_{1} + z_{2}|^{2} = |z_{1}|^{2} + |z_{2}|^{2} + 2Re(\bar{z}_{1}z_{2})$$
$$|z_{1} - z_{2}|^{2} = |z_{1}|^{2} + |z_{2}|^{2} - 2Re(\bar{z}_{1}z_{2})$$
Adding them,
$$|z_{1} + z_{2}|^{2} + |z_{1} - z_{2}|^{2} = 2(|z_{1}|^{2} + |z_{2}|^{2})$$


