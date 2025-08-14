Links: [[09 Definite Integration]], [[00 Conic Sections]]
___
# Area Under the Curve

#### Between Function and Axis
Area under the graph of $y = f(x)$ and x-axis between x = a and x = b can be given as,
$$A = \int_{a}^{b} |f(x)| \, dx$$

![[Pasted image 20231009160848.png]]

Area under the graph of $x = f(y)$ and y-axis between y = a and y = b can be given as,
$$A = \int_{a}^{b} |f(y)| \, dy$$

![[Pasted image 20231009160854.png]]

#### Between Two Functions 
Area bounded by $y = f(x)$ and $y = g(x)$ between the limits x = a and x = b can be given as,
$$A = \int_{a}^{b} |f(x) - g(x)| \, dx$$
$$A = \int_{a}^{b} \text{Upper - Lower Curve} \, dx$$

![[Pasted image 20231009161143.png]]

Area bounded by $x = f(y)$ and $x = g(y)$ between the limits y = a and y = b can be given as,
$$A = \int_{a}^{b} |f(y) - g(y)| \, dx$$
$$A = \int_{a}^{b} \text{Right - Left Curve} \, dx$$

![[Pasted image 20231009161156.png]]

### Multiple Curves 
Area bound by multiple curves will be one which has all the curves as its boundary. 

$$A = \int_{a}^{b} f_{1}(x) - f_{4}(x) \, dx + \int_{b}^{c} f_{1}(x) - f_{3}(x) \, dx + \int_{c}^{d} f_{2}(x) - f_{3}(x) \, dx$$

We go along the upper curve from the left most point to the right most point. Then we go along the lower curve and subtract it. 
$$A = \int_{a}^{c} f_{1}(x) \, dx + \int_{c}^{d} f_{2}(x) \, dx - \int_{a}^{b} f_{4}(x) \, dx - \int_{b}^{d} f_{3}(x) \, dx$$

![[Pasted image 20230210143802.png]]

In the absence of the proper bounded area, the contribution of one of the curves may be of one point only. I.e. if a 5th curve passes through any of the points of intersection of curves in the above diagram. 

If there is no area which has all the functions as its boundary, then it is said that there is no bound area. 

##### Some Notes 
If required or possible make rough graph of area. 

There is no area bounded by the curves $y = f(x)$, $y = 0$ and $x = a$. But if it is not an option, then we will give the shaded area.

![[Pasted image 20231009163545.png]]

If area bounded by a curve is required then that curve will have a loop in its graph. 

In some cases, when the equations are complicated, we just need to know which of the two functions lies above and which lies below. 

If we interchange x and y in entire question the area bound remains unchanged.

### Area of Region 
#important 

Equality represents the curve while an inequality represents the region for which the curve is dividing boundary. 

![[Pasted image 20231010083136.png]]

For the property written in inequality form, first put equality and identify the curve and then identify the region. 

![[Pasted image 20231010083554.png]]

We might also be able to find area using simple geometry.
![[Pasted image 20231010084239.png]]

If the equations are given in compact form,
$$R = \{ (x,y) \in R^{2} : 4x^{2} \leq y \leq 8x+12 \}$$

It means,
$$y \geq 4x^{2}\ \&\ y \leq 8x+12$$
Make regions of both and find area of the intersection of both region. 

### Maxima - Minima 
If $f(x)$ is monotonic function between x = a and x = b, then the area bounded by $y = f(x)$ and $y = k$ between x = a and x = b will be minimum when $k = f\left( \frac{a+b}{2} \right)$. 

> Proof:
> ![[Pasted image 20231011083835.png]]
> ![[Pasted image 20231011084031.png]]


For Example,
![[Pasted image 20231011084810.png]]
![[Pasted image 20231011084826.png]]

## Examples 
![[Pasted image 20231009160655.png]]

![[Pasted image 20231009162010.png]]

![[Pasted image 20231009164649.png]]

![[Pasted image 20231009173432.png]]

![[Pasted image 20231009174324.png]]

![[Pasted image 20231009174652.png]]

![[Pasted image 20231010085031.png]]

![[Pasted image 20231010085303.png]]
![[Pasted image 20231010085510.png]]

![[Pasted image 20231010090542.png]]
![[Pasted image 20231010090555.png]]

![[Pasted image 20231010091607.png]]

Sometimes we can find the area without knowing how the curves look or which one is above,
![[Pasted image 20231011082235.png]]

![[Pasted image 20231011082918.png]]
![[Pasted image 20231011083213.png]]

![[Pasted image 20231011091345.png]]
![[Pasted image 20231011091358.png]]
![[Pasted image 20231011091417.png]]

![[Pasted image 20231011092004.png]]

#### Determination of Parameters 
![[Pasted image 20231011085626.png]]
![[Pasted image 20231011085636.png]]

#### Determination of Function in Area
![[Pasted image 20231011090255.png]]