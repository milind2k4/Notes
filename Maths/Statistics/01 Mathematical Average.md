Links: [[00 Statistics]]
___
# Mathematical Average
**Arithmetic Mean**
aka **Average/Mean**
it is represented by $\bar{x}$ or $\mu$

#### Ungrouped Data
(there are n data points)

$$\bar{x} = \frac{ \displaystyle \sum_{i=1}^{n} x_{i} }{ n }$$

#### Grouped Data
there are n elements and each element has a frequency.

$$\bar{x} = \frac{ \displaystyle \sum_{i = 1}^{n} x_{i}f_{i} }{ \displaystyle \sum_{i = 1}^{n} f_{i} }$$

Or simply,
$$\bar{x} = \frac{ \sum x_{i}f_{i} }{ N }$$
where N is the number of elements i.e. $\sum f_{i}$

#### Grouped Data with Continuous Frequency Distr.
The formula will be the same, i.e.
$$\bar{x} = \frac{ \sum x_{i}f_{i} }{ \sum f_{i} }$$
but here we take $x_{i}$ as the mid value of the ith class interval. 


#### Properties of Mean
1. If we add a constant to every element, the mean also increases by that constant. This is called **Shifting of Origin.**
   $\\$
2. If we multiply every element by a constant, the mean is also multiplied by that constant. This is called **Scaling.**

Thus mean is dependent on both Shift and Scale.

Combining these two,
If
$$y_{i} = ax_{i}+b$$
then,
$$\bar{y} = a\bar{x}+b$$

#### Weighted Mean
The same as grouped data, just replace $f_{i}$ by $w_{i}$, called **Weight** of each observation. 

$$\bar{x}_{w} = \frac{ \sum x_{i}w_{i} }{ \sum w_{i} }$$

### Method of Assumed Mean
If the numbers are very large, then to reduce calculations we can subtract a fixed number, say A, from all of them which is called **Assumed Mean** and then we can adjust calculations accordingly. 

Let the deviation of data values from this assumed mean is, $d_{i}$, i.e.
$$x_{i} - A = d_{i}$$
$$x_{i} = d_{i} + A$$

Giving us the mean,
$$\bar{x} = \frac{ \sum (A + d_{i}) }{ n }$$
$$\bar{x} = \frac{ nA }{ n } + \frac{ \sum (d_{i}) }{ n }$$
$$\bar{x} = A + \frac{ \sum (d_{i}) }{ n }$$
The variance will not change as it does not depend on shifting of origin,
$$\sigma^{2} = \frac{ \sum d_{i} }{ n } - \left( \frac{ \sum d_{i} }{ n } \right)^{2}$$

### Example
The total sum will be the same,
![[Pasted image 20230610094933.png]]

