Links: 
___
# Double Integration
Let the region $R$ be bounded by the curves $x = x_{1},\ \&\ x = x_{2}$, and $y = y_{1},\ \&\ y = y_{2}$, then to find the area, we have two methods,

### Horizontal Strips (Method 1)
When $x_{1}, x_{2}$ are functions of $y$ and $y_{1}, y_{2}$ are constants. 

Then,
$$
\begin{split}
R &= \iint f(x,y)\ dx\ dy \\
&= \int_{y_{1}}^{y_{2}} \left( \int_{x=\phi_{1}(y)}^{x=\phi_{2}(y)} f(x,y) \, dx \right) \, dy 
\end{split}
$$

Here in the internal integral, we treat $y$ as constant. 

### Vertical Strips (Method 2)
When $y_{1}, y_{2}$ are functions of $x$ and $x_{1}, x_{2}$ are constants. 

Then,
$$
\begin{split}
R &= \iint f(x,y)\ dx\ dy \\
&= \int_{x_{1}}^{x_{2}} \left( \int_{y=\phi_{1}(x)}^{y=\phi_{2}(x)} f(x,y) \, dy \right) \, dx 
\end{split}
$$

Here in the internal integral, we treat $x$ as constant. 

