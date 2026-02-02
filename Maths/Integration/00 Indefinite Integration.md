Links: [[00.5 Standard Formulae]]
___
# Indefinite Integration

Integration is the reverse of differentiation. 

i.e. 
$$\begin{split}
\frac{ dF(x) }{ dx } &= f(x) \\
\text{Then, } \int f(x) \, dx &= F(x) + C \\
\end{split}$$
where C is an arbitrary constant.

![[Pasted image 20230921082255.png]]

Answer will be unique but may be in other forms. 
There are infinite functions which are non-integrable. 

#### Differential Element 
[[00 Differentiation#Differential Element]]

$dx$ is called *differential element of x.*

$$d(h(x)) = h'(x)dx$$

In case of composite functions,
$$d(\sin ^{-1}x^{3}) = \frac{ 1 }{ \sqrt{ 1 - x^{6} } }d(x^{3}) = \frac{ 3x^{2} }{ \sqrt{ 1 - x^{6} } }dx$$

### Algebra of Integrals
**Constant multiplication,**
$$\int kf(x) \, dx = k\int f(x) \, dx  $$

**Sum of functions,**
$$\int (f(x)\pm g(x)) \, dx = \int f(x) \, dx \pm \int g(x) \, dx $$

**Variable Change,**
$$\int f(x) \, dx = F(x) + c$$
$$\int f(t) \, dt = F(t) + c$$
Note that $dx \to dt$ then only we can do this. Otherwise we cannot. 
I.e. 
$$\int \sin t \, dt = -\cos t + c$$
$$\int e^{ x^{2} } \, dx^{2} = e^{ x^{2} } + c$$
$$\int \sin t \, dx \neq -\cos t + c$$


**Expression of x as argument,**
$$\int f(x) \, dx = F(x) + c$$
then,
$$\int f(ax+b) \, dx = \frac{ F(ax+b) }{ a } + c$$
The expression in $x$ should be linear. 

This is as,
$$
\begin{split}
\int f(ax + b) \, dx &= \frac{ 1 }{ a } \int f(ax + b) \, d(ax + b) \\
&= \frac{ 1 }{ a } F(ax + b) + c 
\end{split}
$$

### Reduction Formula 
We go till n = 1 or 0 at which point we can simply integrate. 

##### $\int \tan ^{n}x$
$$
\begin{split}
I_{n} &= \int \tan ^{n}x \, dx \\
&= \int \tan ^{n-2}x (\tan ^{2}x) \, dx  \\
&= \int \tan ^{n-2}x\sec^{2}x \, dx - \int \tan ^{n-2} \, dx \\ 
I_{n} &= \frac{ \tan ^{n-1}x }{ n-1 } - I_{n-2}
\end{split}
$$

Example,
![[Pasted image 20231001172801.png]]

##### $\int x \ln^{n}x$
$$
\begin{split}
I_{n} &= \int \underset{ II }{ x } \cdot \underset{ I }{ \ln^{n}x } \, d 
\\
&= \frac{ x^{2} }{ 2 }\ln^{n}x - \frac{ n }{ 2 }\int x^{2}\ln^{n-1}(x) \frac{ 1 }{ x } \, dx 
\\
I_{n} &= \frac{ x^{2} }{ 2 }\ln^{n}x - \frac{ n }{ 2 }I_{n-1} 
\end{split}
$$

##### $\int \sin ^{n}x$
$$
\begin{split}
I_{n} &= \int \sin ^{n}x \, dx 
\\
&= \int \underset{ II }{ \sin x } \cdot \underset{ I }{ \sin ^{n-1}x } \, dx 
\\
&= -\cos x \sin ^{n-1}x + (n-1)\int \cos (x) \sin ^{n-2}(x) \cos (x) \, dx 
\\
&= -\cos x \sin ^{n-1}x + (n-1)\int \sin ^{n-2}x \, dx - (n-1)\int \sin ^{n}x \, dx 
\\
&= -\cos x \sin ^{n-1}x + (n-1)I_{n-2} - (n-1)I_{n} 
\end{split}
$$
Finally giving,
$$I_{n} = \frac{ -\cos x \sin ^{n-1}x }{ n } + \frac{ n-1 }{ n } I_{n-2}$$

#### Examples 
Deriving reduction formula.

![[Pasted image 20231001174825.png]]
![[Pasted image 20231001174840.png]]


## Misc. Examples 
![[Pasted image 20230923145028.png]]

![[Pasted image 20231006091004.png]]


