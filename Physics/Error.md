Links: [[Length Measuring Devices]]
___
# Error and Measurement
### Significant Figures
It is the no. of integers in reading which are significant. 

The more is the no. of SF, the more accurate the measurement is. 
I.e., 20.00 $m /s^{2}$ is more accurate than 20 $m /s^{2}$.

SF is no. of digits which we know accurately + 1. +1 is for the last digit and it is not accurate.  

**Rules of Significant Figures,**
1. All non zero digits are always significant.
2. All zeroes between non-zero digits are significant. 
3. Leading zeros are never significant.
4. Trailing zeros without decimal are non-significant.
5. Trailing zero with decimal are significant. (e.g. in 690.00 there are 5 SF)
6. Powers doesn't change significant figures. (e.g. in $20 \times 10^{4}$ there is one SF)
7. Exact values have infinite significant figures. (e.g. 67 students has $\infty$ SF)


We need to change the unit in such a way that it does not affect the no of sig figs. 
E.g. $5.0$ kg = $5.0 \times 10^{3}$ g and not $5 \times 10^{3}$ g.


##### Algebra of SF
The result of the operation cannot be more accurate than the operands. 
The result will have the same accuracy as the least accurate operand. 

1. **Addition/Subtraction**
   The result will have decimals equal to the least no. of decimals among the operands.
   
   E.g., 1.32 + 2.4 = 3.7 (not 3.72)
   $\\$

2. **Multiplication/Division**
   The result will have SF equal to the operand having least SF.
   
   E.g., 1.4 \* 1.4 = 2.0 and not 1.96 
   1.5 \* 1.50 = 2.2 and not 2.250. 
   
##### Rules of Round off
1. If the digit is less than 5, remove it.

2. If the digit is more than 5, add one to the digit before it.

3. If the digit is exactly 5, add one if the number before is odd, remove 5 if the digit before is even. 
   (5 helps odd)

### Error 
Error is the difference between Experimental Value and True Value. 

It is impossible to find the physical true value.

Types:
1. **Random:** Reason is unknown. 
2. **Systematic:** Reason is known.

To minimize random error, experiments are performed n times. 
The more is n the less is the error. 

If the readings are $\ce{ x_{1}, x_{2}, x_{3}, x_{4} \dots }$
Then, for the final reading, we take the average of this,
$$x_{avg} = x = \frac{ \sum x_{i} }{ n }$$

This average reading is taken as the **True Value**.

**Absolute Error** is the difference between true value and the measured value. It can be +ve, -ve or zero.
$$
\begin{split}
\Delta x_{1} &= x - x_{1} \\
\Delta x_{2} &= x - x_{2} \\
.\ \ \ \ & \\
.\ \ \ \ & \\
.\ \ \ \ & \\
\Delta x_{n} &= x - x_{n} 
\end{split}
$$

Mean absolute error,
$$\left< \Delta x \right> = \frac{ \sum | \Delta x_{1} | }{ n }$$

Fractional error is,
$$\text{error} = \frac{ \left< \Delta x \right> }{ x }$$

Percentage error is,
$$\%\ \text{error} = \frac{ \left< \Delta x \right>  }{ x } \times 100$$

Final reading is written as,
$$R = x \pm \left< \Delta x \right>$$
Or simply,
$$R = x \pm \Delta x$$

where $\left< \Delta x \right>$ should be rounded off to the decimals of x. 

**Least Count**: Min value which can be measured by an instrument. 

When writing final value, write the least count with it as, $(7.8 \pm 0.1)\ \ce{ cm }$

#### Maximum Error 
##### Addition and Subtraction
When adding two measurements which have error, we simply add the error for error in final result.

$$
\begin{split}
a &= x + \Delta x \\
b &= y + \Delta y \\
c &= (x+y) + (\Delta x + \Delta y)
\end{split}
$$

When subtracting as well, the error is added.

*Error is always added.* 

##### Multiplication

1. Take log both side
2. Differentiate both side
3. Write the values of the variables. 
4. Find the error (dx). 

This can also be used to calculate fractional change in any quantity. 

##### Division 
Here too, we do the same as multiplication, just that if there is any -ve, we take mod of it.



#### % error in Formula
1. As done in multiplication, take log both sides. 
2. Differentiate both sides. 
3. If there is a -ve sign then convert it into +ve sign. 
4. Put the values and find error. 

This can also be used to calculate % change in any quantity. 

### Zero Error
If when we are not measuring anything the reading is not zero, then that measurement is known as zero error. 

Then,
$$\ce{ Actual Reading = Observed Reading - Zero Error }$$












