Links: [[00 Differentiation]]
___
# Higher Order Derivative 
$$y' = \frac{ dy }{ dx }$$
is called *1st order differential coefficient (dc) of y wrt x.* It represents slope.

$$y'' = \frac{ d^{2}y }{ dx^{2} } = \frac{ d }{ dx }\left( \frac{ dy }{ dx } \right)$$
is called *2nd order differential coefficient (dc) of y wrt x.* It represents concavity (concave up if $y'' = +ve$ or down  if $y'' = -ve$).

$$y''' = \frac{ d^{3}y }{ dx^{3} } = \frac{ d^{2} }{ dx^{2} }\left( \frac{ dy }{ dx } \right) = \frac{ d }{ dx }\left( \frac{ d^{2}y }{ dx^{2} } \right)$$
is called *3rd order differential coefficient (dc) of y wrt x.* 

$$y^{(n)} = \frac{ d^{n}y }{ dx^{n} } = \frac{ d^{n-1} }{ dx^{n-1} }\left( \frac{ dy }{ dx } \right) = \frac{ d }{ dx }\left( \frac{ d^{n-1}y }{ dx^{n-1} } \right)$$
is called *nth order differential coefficient (dc) of y wrt x.* 

#### Expressing 2nd order wrt x as wrt y
Expressing 2nd derivative in terms of dcs of x wrt y (i.e. in terms of $dx /dy$ and $d^{2}x /dy^{2}$)

$$
\begin{split}
\frac{ d^{2} y }{ d x^{2} } &= \frac{ d  }{ d y } \left( \frac{ d y }{ d x }  \right) . \frac{ dy }{ dx } \\
&= \frac{ d  }{ d y } \left( \frac{ 1 }{ \frac{dx}{dy} } \right) . \frac{ 1 }{ \frac{dx}{dy} } \\
&= \left( -\frac{ 1 }{ \left( \frac{ dx }{ dy } \right)^{2} } . \frac{ d^{2} x }{ d y^{2} } \right) . \frac{ 1 }{ \frac{ dx }{ dy } } \\
&= \frac{ - \frac{ d^{2} x }{ d y^{2} }  }{ \left( \frac{ dx }{ dy } \right)^{3} } 
\end{split}
$$
Here, we see that it is not reciprocal like in the case with first order derivatives.

Thus,
$$\frac{ d^{2} y }{ d x^{2} } = - \frac{ \displaystyle \frac{ d^{2} x }{ d y^{2} }  }{ \displaystyle \left( \frac{ dx }{ dy } \right)^{3} }$$
Or in short,
$$y'' = \frac{ -x'' }{ (x')^{3} }$$
where $y''$ means wrt x and $x'', x'$ means wrt y. 

#### Expressing 2nd order in terms of dcs of x and y wrt t

$$
\begin{split}
\frac{ d^{2} y }{ d x^{2} } &= \frac{ d }{ d x } \left( \frac{ dy }{ dx }  \right) \\
&= \frac{ d  }{ dt } \left( \frac{ \frac{ dy }{ dt } }{ \frac{ dx }{ dt } } \right) . \frac{ dt }{ dx } \\
&= \left( \frac{ \displaystyle \frac{ d^{2} y }{ d t^{2} } . \frac{ dx }{ dt }  - \frac{ d^{2} x }{ d t^{2} } .\frac{ dy }{ dt } }{ \displaystyle \left( \frac{ dx }{ dt }  \right)^{2} } \right) . \frac{ 1 }{ \frac{ dx }{ dt }  } \\
\\
&= \frac{ \displaystyle \frac{ d^{2} y }{ d t^{2} } . \frac{ dx }{ dt }  - \frac{ d^{2} x }{ d t^{2} } .\frac{ dy }{ dt } }{ \displaystyle \left( \frac{ dx }{ dt }  \right)^{3} }  \\
\end{split}
$$

Thus, in compact,
$$\frac{ d^{2} y }{ d x^{2} } = \frac{ y''x' - x''y' }{ (x')^{3} }$$
where $'$ means wrt t. 

### Points to Remember 
$$\frac{ dx }{ dx } = 1$$
$$\frac{ d^{2} x }{ d x^{2} } = 0$$

#### nth Derivative of Product 
$$\frac{ d^{n} (f.g) }{ d x^{n} } = {}^{n}C_{0} . \frac{ d^{n} f }{ d x^{n} } . g + 
{}^{n}C_{1} . \frac{ d^{n-1} f }{ d x^{n-1} } . \frac{ dg }{ dx } + 
{}^{n}C_{2} . \frac{ d^{n-2} f }{ d x^{n-2} } . \frac{ d^{2} g }{ d x^{2} } + 
\dots {}^{n}C_{r} . \frac{ d^{n-r} f }{ d x^{n-r} } . \frac{ d^{r} g }{ d x^{r} } + \dots + 
{}^{n}C_{n} . f . \frac{ d^{n} g }{ d x^{n} }$$

In short,
$$(fg)^{(n)} = \sum_{r=0}^{n} {}^{n}C_{r} f^{(n-r)}. g^{(r)}$$

This is called **Lebiniz Formula.**

Using this we get,
$$(\sin x)^{(n)} = \sin\left( \frac{ n\pi }{ 2 } + x \right)$$
$$(\cos x)^{(n)} = \cos\left( \frac{ n\pi }{ 2 } + x \right)$$

![[Pasted image 20230822093238.png]]

#### Derivative of Inverse
[[08 Inverse Function#Derivatives]]

$$\frac{ d f^{-1} }{ d x } = \left. \frac{ 1 }{ f'(x) } \right|_{x = f^{-1}(x)} = \frac{ 1 }{ f'(f^{-1}(x)) }$$

Using this,
$$
\begin{split}
\frac{ d^{2} f^{-1} }{ d x^{2} } &= \frac{ d  }{ d x } \left( \frac{ 1 }{ f'(f^{-1}) } \right) \\
&= - \frac{ 1 }{ (f'(f^{-1}))^{2} } . f''(f^{-1}). \frac{ 1 }{ f'(f^{-1}) } \\
\\
&= - \frac{ f''(f^{-1}) }{ (f'(f^{-1})^{3}) }
\end{split}
$$
