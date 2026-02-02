Links: [[01 Arithmetic Progression]]
___
# Harmonic Progression

A sequence in which the reciprocals of all the terms is in AP.

General Term:
$$(T_{n})_{HP}= \frac{1}{(T_{n})_{AP}}$$

Thus, an HP is,
$$\frac{ 1 }{ a }, \frac{ 1 }{ a+d }, \frac{ 1 }{ a+2d }, \frac{ 1 }{ a + 3d }, \dots$$

There is no formula for the sum of n terms of an HP.

The AP obtained by taking reciprocals terms of HP is called corresponding AP (CAP). 

For HP to be defined no term of CAP can be zero. 

If, an HP is,
$$x_{1} , x_{2}, x_{3}, \dots $$
Then CAP is,
$$\frac{ 1 }{ x_{1} }, \frac{ 1 }{ x_{2} }, \frac{ 1 }{ x_{3} } \dots$$

Then,
$$d = \frac{ 1 }{ x_{2} } - \frac{ 1 }{ x_{1} }$$
$$d.x_{1}x_{2} = x_{1} - x_{2}$$
$$d x_{2}x_{3} = x_{2} - x_{3}$$
$$\frac{ 1 }{ x_{3} } - \frac{ 1 }{ x_{1} } \implies x_{1} - x_{3} = 2dx_{1}x_{3}$$
$$x_{5} - x_{11} = 6d. x_{5}. x_{11}$$

Thus, for any two general terms,
$$x_{i} - x_{j} = (j-i).d.x_{i}.x_{j}$$


## Harmonic Mean (HM)
HM of two numbers $a,b$ = $H$ (say), then, 
$$\frac{1}{a}, \frac{1}{H}, \frac{1}{b}$$ 
are in AP.
$$\frac{2}{H} = \frac{1}{a} + \frac{1}{b}$$
$$H = \frac{2ab}{a+b}$$

For three numbers, 
$$\frac{3}{H} = \frac{1}{a} + \frac{1}{b} + \frac{1}{c}$$

For n numbers,
$$\frac{n}{H} = \frac{1}{a_{1}} + \frac{1}{a_{2}} + \frac{1}{a_{3}} + \dots + \frac{1}{a_{n}}$$

For HM, the numbers need not be in HP, but if they are then, the HM of terms taken symmetrically from both sides will be equal and constant. 
If HP is,
$$h_{1},h_{2},h_{3} \dots h_{n}$$

Then,
$$H = \frac{ 2 }{ \displaystyle \frac{1}{h_{1}} + \frac{1}{h_{n}} } = \frac{ 4 }{ \displaystyle \frac{ 1 }{ h_{3} } + \frac{ 1 }{ h_{4} } + \frac{ 1 }{ h_{n-2} } + \frac{ 1 }{ h_{n-3} } }$$

$$H = \frac{ n }{ \displaystyle  \frac{ 1 }{ h_{1} } + \frac{ 1 }{ h_{2} } + \frac{ 1 }{ h_{3} } + \dots \frac{ 1 }{ h_{n} } }$$
And,
$$H = h_{\frac{ n+1 }{ 2 }},\ n \text{ is odd}$$
$$H = \frac{ 2 }{ h_{\frac{n}{2}} +  h_{\frac{n}{2}+1} },\ n \text{ is odd}$$

#### Inserting n HM between two numbers
We just flip the numbers, insert n AMs then flip them again to get the terms in HP. 

$$a, H_{1}, H_{2}, H_{3}, \dots, H_{n},b$$ 
are in HP.

Then 
$$\frac{1}{a}, \frac{1}{H_{1}}, \frac{1}{H_{2}}, \frac{1}{H_{3}}, \dots ,\frac{1}{H_{n}}, \frac{1}{b}$$
are in AP.
Number of terms = $n+2$

$$\begin{split}
T_{n+2} &= \frac{1}{b}\\
&= \frac{1}{a} + (n+1)d \\\\
\text{Thus,} \\
d &= \left( \frac{1}{b} - \frac{1}{a} \right) \left( \frac{1}{n+1} \right) 
\end{split}$$

Using formula for AM,
$$\frac{ 1 }{ H_{k} } = \frac{ k \frac{ 1 }{ b } + (n-k+1) \frac{ 1 }{ a } }{ n+1 }$$

Giving,
$$H_{k} = \frac{ (n+1)ab }{ k.a + (n-k+1).b }$$

## Example
![[Pasted image 20230614091524.png]]
![[Pasted image 20230614091537.png]]