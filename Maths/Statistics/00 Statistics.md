Links: [[01 Mathematical Average]], [[02 Positional Mean]], [[03 Deviation]]
___
# Statistics
#### Representation of Data
1. **Ungrouped Data:** each value is written separately, or no clubbing of data is done. 

2. **Grouped Data with single Class Value:** data points with same value are written together (or once) with associated frequency.

1. **Grouped Data with Class Value as Intervals:** data is represented in the form of frequency of a class value range. 

## Measures of Central Tendency
or Measurement of the Location

It is measurement of representative value of the given data set.  

e.g.
![[Pasted image 20230217113431.png|400]]


### [[01 Mathematical Average]]


### [[02 Positional Mean]]


## [[03 Deviation]]
 
## Combination of Series
Series 1, $\bar{x}_{1}, \sigma_{1}, \sigma_{1}^{2}, n_{1}$ with entries, say, $a_{1},a_{2},a_{3},a_{4} \dots a_{n_{1}}$
Series 2, $\bar{x}_{2}, \sigma_{2}, \sigma_{2}^{2}, n_{2}$ with entries, say, $b_{1},b_{2},b_{3},b_{4} \dots b_{n_{2}}$

The combined series, Series 1 + Series 2, 
Mean,
$$
\begin{split}
\bar{x}_{1} &= \frac{ \sum a_{i} }{ n_{1} } \\
\text{Giving,} \\
\sum a_{i} &= n_{1}\bar{x}_{1} \\
\\
\sigma_{1}^{2} &= \frac{ \sum (a_{i} - \bar{x}_{1})^{2} }{ n_{1} } \\
\text{Giving,} \\
\sum (a_{i} - \bar{x}_{1})^{2} &= n_{1}\sigma_{1}^{2} \\
\end{split}
$$

Similarly for series 2,
$$
\begin{split}
\sum b_{i} &= n_{2}\bar{x}_{2} \\
sum (b_{i} - \bar{x}_{2})^{2} &= n_{2}\sigma_{2}^{2}
\end{split}
$$

Then for the combined series,
$$
\begin{split}
\bar{x} &= \frac{ \sum a_{1} + \sum b_{2} }{ n_{1} + n_{2} } \\
\bar{x} &= \frac{ n_{1}\bar{x}_{1} + n_{2}\bar{x}_{2} }{ n_{1}+n_{2} }
\end{split}
$$

And for the combined variance, we consider,
$$
\begin{split}
\sum (a_{i} - \bar{x})^{2} &= \sum (a_{i} - \bar{x}_{1} + \bar{x}_{1} - \bar{x})^{2} 
\\
&= \sum \left( (a_{i}-\bar{x}_{1})^{2} + (\bar{x}_{1} - \bar{x})^{2} + 2(a_{i}-\bar{x}_{1})(\bar{x}_{1}-\bar{x}) \right) 
\\
\text{Let,} \bar{x}_{1} - \bar{x} = d_{1},
\\
&= \sum (a_{i}-\bar{x}_{1})^{2} + n_{1}d_{1}^{2} + 2d_{1} \sum (a_{i}-\bar{x}_{1}) 
\\
&= n_{1}\sigma_{1}^{2} + n_{1}di^{2} + 0 
\\
\sum (a_{i} - \bar{x})^{2} &= n_{1}(\sigma_{1}^{2} + d_{1}^{2}) 
\\
\\
\text{Similarly,} 
\\
\sum (b_{i} - \bar{x})^{2} &= n_{2}(\sigma_{2}^{2} + d_{2}^{2}) 
\end{split}
$$
Thus, the variance for the combined series,
$$
\begin{split}
\sigma^{2} &= \frac{ \sum (x_{i} - \bar{x})^{2} }{ n_{1} + n_{1} } \\
&= \frac{ \sum (a_{i}-\bar{x})^{2} + \sum (b_{i} - \bar{x})^{2} }{ n_{1} + n_{2} } \\
\sigma^{2} &= \frac{ n_{1}(\sigma_{1}^{2} + d_{1}^{2}) + n_{2}(\sigma_{2}^{2} + d_{2}^{2}) }{ n_{1} + n_{2} }
\end{split}
$$
where,
$$d_{1} = \bar{x}_{1} - \bar{x}$$
$$d_{2} = \bar{x}_{2} - \bar{x}$$

Thus, for the combined series,
$$\bar{x} = \frac{ n_{1}\bar{x}_{1} + n_{2}\bar{x}_{2} }{ n_{1}+n_{2} }$$
$$\sigma^{2} = \frac{ n_{1}(\sigma_{1}^{2} + d_{1}^{2}) + n_{2}(\sigma_{2}^{2} + d_{2}^{2}) }{ n_{1} + n_{2} }$$

## For First n natural number
Mean,
$$
\begin{split}
\bar{x} &= \frac{ n(n+1) }{ 2(n) } \\
\bar{x} &= \frac{ n+1 }{ 2 }
\end{split}
$$

Variance,
$$
\begin{split}
\sigma^{2} &= \frac{ \sum x_{i}^{2} }{ n } - \bar{x}^{2} \\
&= \frac{ n(n+1)(2n+1) }{ 6n } - \left( \frac{ n+1 }{ 2 } \right)^{2} \\
&= \frac{ n^{2}-1 }{ 12 }
\end{split}
$$
































