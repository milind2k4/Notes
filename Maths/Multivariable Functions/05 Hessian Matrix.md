Links: [[01 Partial Differentiation]]
___
# Hessian Matrix


It is a matrix of second order partial derivatives denoted by $H f(x,y, \dots)$. 

For two variables,

$$
\begin{split}
Hf(x,y) &= 
\begin{bmatrix}
\displaystyle  \frac{ \partial^{2} f }{ \partial x^{2} } & \displaystyle  \frac{ \partial^{2} f }{ \partial x \partial y }  \\
\displaystyle  \frac{ \partial^{2} f }{ \partial x \partial y } & \displaystyle  \frac{ \partial^{2} f }{ \partial y^{2} } 
\end{bmatrix}
\end{split}
$$

For three variables,
$$
\begin{split}
H f(x,y,z) &= 
\begin{bmatrix}
\displaystyle \frac{ \partial^{2} f }{ \partial x^{2} } & 
\displaystyle  \frac{ \partial^{2} f }{ \partial x \partial y } &  
\displaystyle  \frac{ \partial^{2} f }{ \partial x \partial z } 
\\
\displaystyle  \frac{ \partial^{2} f }{ \partial y \partial x } &  
\displaystyle  \frac{ \partial^{2} f }{ \partial y^{2} } &  
\displaystyle  \frac{ \partial^{2} f }{ \partial y \partial z }
\\
\displaystyle  \frac{ \partial^{2} f }{ \partial z \partial x } & 
\displaystyle  \frac{ \partial^{2} f }{ \partial z \partial y } &  
\displaystyle  \frac{ \partial^{2} f }{ \partial z^{2} } 
\end{bmatrix}
\end{split}
$$

The determinant of the Hessian is also called the Determinant of $f$. 

Hessian matrix is used for optimization in machine learning, neural networks, deep learning etc..
