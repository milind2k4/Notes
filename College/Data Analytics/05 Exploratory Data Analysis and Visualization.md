Links: [[00 Data Analytics]]
___
# Exploratory Data Analysis and Visualization

**Exploratory Data Analysis (EDA)** is an approach to analyzing datasets to summarize their main characteristics, often with visual methods. Before we can visualize or model data, we must understand the fundamental mathematics that describe it.

## Statistics and Probability for Data Analytics
Statistics is the mathematical science involving the collection, analysis, and interpretation of data. Probability deals with predicting the likelihood of future events. In Data Analytics, these two fields merge to allow us to make informed decisions based on historical data.

- **Descriptive Statistics:** Summarizes and describes the features of a dataset (What happened?).
- **Inferential Statistics:** Draws conclusions and makes predictions about a larger population based on a smaller sample (Why it happened/What will happen?).

## Measures of Central Tendency
Central tendency provides a single value that represents the center or typical value of a distribution.

```python
import numpy as np
import pandas as pd
from scipy import stats

data = [10, 15, 15, 20, 100] # 100 is an outlier
df = pd.DataFrame(data, columns=['Values'])

mean = df['Values'].mean()     # 32.0 (Pulled up by the 100)
median = df['Values'].median() # 15.0 (unaffected)
mode = df['Values'].mode()[0]  # 15.0
```

### Mean (Average)
The sum of all values divided by the number of values. Highly sensitive to outliers.

**Formula:** 
$$\bar{x} = \frac{\sum_{i=1}^{n} x_i}{n}$$

### Median
The middle value when the data is sorted. Highly robust against outliers.
- **Odd count:** The exact middle number.
- **Even count:** The average of the two middle numbers.

### Mode
The value that appears most frequently. A dataset can be bimodal (two modes) or multimodal.

## Measures of Dispersion
Dispersion (or variability) describes how spread out the data is around the center.

### Range
The difference between the maximum and minimum values.
$$\symup{Range = Max - Min}$$

### Variance ($\sigma^2$)
Measures how far each number in the set is from the Mean. The average of the squared differences from the Mean.

**Formula (Population Space):**
$$\sigma^2 = \frac{\sum_{i=1}^{N} (x_i - \mu)^2}{N}$$

### Standard Deviation ($\sigma$)
The square root of the variance. This is the most widely used measure because it returns to the original unit of measurement.

**Formula:**
$$\sigma = \sqrt{\frac{\sum_{i=1}^{N} (x_i - \mu)^2}{N}}$$

### Interquartile Range (IQR)
The range of the middle 50% of the data. Extremely robust to outliers. Used in Boxplots.

**Quartile Formulas (for sorted data of size $n$):**
- **$Q_1$ (25th Percentile):** Value at the $\left(\frac{n+1}{4}\right)^{th}$ position.
- **$Q_2$ (Median):** Value at the $\left(\frac{n+1}{2}\right)^{th}$ position.
- **$Q_3$ (75th Percentile):** Value at the $3\left(\frac{n+1}{4}\right)^{th}$ position.

$$IQR = Q_3 - Q_1$$

```python
variance = df['Values'].var()
std_dev = df['Values'].std()
iqr = df['Values'].quantile(0.75) - df['Values'].quantile(0.25)
```

## Probability Distributions
A **Probability Distribution** is a mathematical function that provides the probabilities of occurrence of different possible outcomes in an experiment.

1.  **Probability Density Function (PDF):** For continuous data (e.g., exact height). The probability of a specific exact point is zero; we measure the probability across a *range* (area under the curve).
2.  **Probability Mass Function (PMF):** For discrete data (e.g., rolling a dice). Provides the exact probability for a specific integer value.

### Normal Distribution (Gaussian)
The most important distribution in statistics. It forms a symmetrical, bell-shaped curve.
- The Mean, Median, and Mode are perfectly equal and located at the center.
- Dictated by parameters $\mu$ (Mean) and $\sigma$ (Standard Deviation).

$$f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2}$$

![[Pasted image 20260306134906.png]]

### Standard Normal Distribution
A special case of the Normal Distribution where the **Mean = 0** and the **Standard Deviation = 1**. 
We convert any Normal Distribution to a Standard one using the **Z-score**.

**Z-Score Formula:**
$$Z = \frac{X - \mu}{\sigma}$$

*(This allows us to compare different datasets on the exact same scale).*

```python
import seaborn as sns
import matplotlib.pyplot as plt

# Generate a normal distribution
normal_data = np.random.normal(loc=0, scale=1, size=1000)

# Visualize it
sns.histplot(normal_data, kde=True)
plt.title("Standard Normal Distribution")
plt.show()
```

### Binomial Distribution
A discrete probability distribution representing the number of successes in a sequence of $n$ independent yes/no (binary) experiments (e.g., flipping a coin 10 times and counting "Heads").

- **Parameters:** $n$ (number of trials) and $p$ (probability of success in a single trial).

$$P(X=k) = \binom{n}{k} p^k (1-p)^{n-k}$$

```python
# Simulating 10 coin flips, probability of heads=0.5, repeating experiment 1000 times
binomial_data = np.random.binomial(n=10, p=0.5, size=1000)
```

![[Pasted image 20260306135104.png]]

### Poisson Distribution
A discrete distribution representing the probability of a given number of events occurring in a **fixed interval of time or space**, assuming the events occur with a known constant mean rate and independently.
- **Example:** The number of emails received in an hour.
- **Parameter:** $\lambda$ (Lambda), which is the average rate of value.

**Formula (PMF):**
$$P(k) = \frac{\lambda^k e^{-\lambda}}{k!}$$

```python
# Simulating receiving on average 3 emails an hour, over 1000 hours
poisson_data = np.random.poisson(lam=3, size=1000)
```

![[Pasted image 20260306135249.png]]
(here k is acting as x, i.e. the number of trials)

### Uniform Distribution
A distribution where all outcomes are equally likely. It can be discrete (rolling a fair 6-sided die, probability = $\frac{1}{6}$) or continuous (a random number generator).

$$f(x) = \frac{1}{b - a} \quad \text{for } a \le x \le b$$

```python
# Random floats between 0 and 10
uniform_data = np.random.uniform(low=0, high=10, size=1000)
```

## Central Limit Theorem (CLT)
The **Central Limit Theorem** is a fundamental principle in statistics.

> [!TIP] Central Limit Theorem 
> If you take sufficiently large random samples ($n \ge 30$) from a population with a replacement, the distribution of the **sample means** will approximate a **Normal Distribution**, *regardless* of whether the original population was normally distributed or not.

This is extremely useful in [[06 Inferential Statistics]]

### Importance and Applications
1.  **Simplifies Analysis:** Because sample means form a normal distribution, we can safely apply powerful statistical methods (like Hypothesis Testing, T-tests, ANOVAs) to data that is not normally distributed itself.
2.  **Predictability:** It allows us to infer population parameters (Population Mean) using just a sample mean.
3.  **Foundation of ML:** Many ML algorithms mathematically assume that the underlying inputs or errors are normally distributed. CLT helps justify these assumptions when working with large datasets.

```python
# Demonstrating CLT
# Let's start with a heavily NON-normal distribution (Uniform)
population = np.random.uniform(0, 100, 10000) 

sample_means = []
# Take 1000 random samples. For each sample, take 50 instances and find their mean.
for _ in range(1000):
    sample = np.random.choice(population, size=50)
    sample_means.append(sample.mean())

# If plotted, 'sample_means' will magically form a perfect Bell Curve!
sns.histplot(sample_means, kde=True)
plt.title("Central Limit Theorem in Action")
plt.show()
```
