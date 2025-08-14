Links: [[00 Probability]]
___
# Probability Distribution
**Random Variable:** It is a function which assigns different numerical values to the all possible obtained outcome, when an experiment is performed. 

**Probability Distribution** is the information of how total probability "1" is distributed among various possible outcomes. It may be in tabular form. 

![[Pasted image 20231226213334.png]]

## Expected Value and Variance 
[[01 Mathematical Average]]

Let in an experiment, a random variable X is defined which can take values $x_{1},x_{2},x_{3} \dots x_{n}$ with probabilities $p_{1},p_{2},p_{3} \dots p_{n}$ respectively, then, if the experiment is performed once, then the mean value or the expected value of X will be (bar represents average not "not"),
$$P(\overline{X}) = \mu = \sum_{i=1}^{n} x_{i}p_{i}$$

The variance of above described distribution will be,
$$
\begin{split}
\sigma^{2} &= \sum_{i=1}^{n} p_{i} (x_{i} - \mu)^{2} \\
&= \sum_{i=1}^{n} p_{i}x_{i}^{2} - 2\mu p_{i} x_{i} + \mu^{2} p_{i} \\
&= \sum p_{i}x_{i} - 2 \mu \sum p_{i} x_{i} + \mu^{2} \sum p_{i} \\
&= \sum p_{i} x_{i} - 2\mu^{2} + \mu^{2}
\end{split}
$$

Thus giving,
$$\sigma^{2} = \sum_{i=1}^{n} p_{i} x_{i}^{2} - \mu^{2}$$
Standard Deviation is found by taking the square root of this. 

Also,
![[Pasted image 20231226215519.png]]

Example,
![[Pasted image 20231226215509.png]]