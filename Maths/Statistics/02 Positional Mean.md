Links: [[01 Mathematical Average]]
___
# Positional Average
### Median 
Middle data point when the data is arranged in increasing or decreasing order.

Median can be used to nullify the effect of outlier data points. 

#### Ungrouped Data
1. Arrange in increasing order.
1. If number of terms is odd, median is the element at $\displaystyle \frac{ n + 1 }{ 2 }$ position.
2. If the number of terms is even, median is the mean of the elements at $\displaystyle \frac{n}{2}$ and $\displaystyle \frac{n}{2} + 1$ positions.

#### Grouped Data
1. Add a new column, cumulative frequency. 
	- The last number is the sum of all the frequencies, N 
2. Find N/2.
3. Find the column with just bigger cumulative frequency than N/2.
4. The element with this cumulative frequency will be the median.

If N/2 comes out to be exactly one of the cumulative frequency, and N is even, then the median will be the average of that row and the next one,

![[Pasted image 20230608083403.png]]


#### Continuous Frequency Distribution
1. Add a new column, cumulative frequency. 
2. Find the median class (the one with frequency just bigger than N/2)
  
$$M = l + \frac{ N / 2 - C }{ f } \times h$$
where,
$l \to$ Lower Limit of Median Class
$C \to$ Cumulative Frequency of the class preceding Median Class
$f \to$ Frequency of Median Class.
$h \to$ Height of Class (higher - lower limit of a class)

**Note:** The median will *always* lie in the median class.

The $l$ puts us at the beginning of the interval. h tells us how many number of observations are in that interval and $\displaystyle \frac{ N/2 -C }{ f }$ tells us what fraction of the interval we have to travel to reach the median. 

For even numbers, we can take average of the median calculated by first taking N/2 and then taking N/2 + 1.

### Mode
The element with the most frequency. It can be more than one also. 

For discrete data, we need to create frequency distribution. For grouped data, the value which has the most frequency is the mode. 

If the data has multiple modes, then that data is called **Multimodal.**

#### Continuous Frequency Distribution 
Identify the modal class (class with max. frequency)
Mode can be calculated as,
$$\text{Mode} = l + h \left( \frac{ f_{m} - f_{o} }{ (f_{m}-f_{o}) + (f_{m} - f_{1}) } \right)$$
\where,
$l\to$ initial value of class interval corresponding to modal class
$h \to$ height of interval
$f_{m} \to$ frequency of modal class
$f_{o} \to$ frequency of class just before modal class
$f_{1} \to$ frequency of class just after modal class

We find which class is modal class and then depending on the drops on both sides of the modal class, move a fraction of the class length. 

Here, since the drop off after the modal class is not much, the modal value will be towards 40. If on both sides the drop off was the same, the modal value would have been the middle value of the class.
![[Pasted image 20230609074235.png]]

### Relation between Mean, Median and Mode

$$\begin{matrix}
\text{Mean} & \text{Median} & \text{Mode} 
\end{matrix}$$

##### Perfectly Symmetric Distribution
$$\ce{ Mean = Mode = Median }$$

![[Pasted image 20230610082726.png]]

#### Moderately Skewed Distribution
We have an observation, i.e. there is no proof of this,
$$\ce{ Median = \frac{ 2 Mean + 1 Mode }{ 2+1 } }$$
$$\ce{ Mode - Mean = 3(Median - Mean) }$$
$$\ce{ 3 Median = 2 Mean + Mode }$$
