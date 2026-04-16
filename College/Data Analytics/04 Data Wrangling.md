Links: [[00 Data Analytics]]
___
# Data Wrangling

**Data Wrangling** (or Data Munging) is the process of cleaning, structuring, and enriching raw data into a desired format for better decision-making in less time.

It is a crucial part of the Data Preparation phase in the [[03 Data Analytics Lifecycle]].

## Handling Missing Data
Modern algorithms cannot handle missing (`NaN` or `None`) values mathematically. We must account for them before analysis.

[[02 Data Preprocessing#Handling Missing Values]]

### Dropping Data
[[02 Data Preprocessing#Removing Data]]

If the dataset is large and the missing values are negligible, we can drop the rows or columns.

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Age': [25, np.nan, 22, 29, 28],
    'Salary': [50000, 54000, 50000, np.nan, 60000]
})

# Drop any row containing at least one missing value
df_dropped_rows = df.dropna()

# Drop any column containing at least one missing value
df_dropped_cols = df.dropna(axis=1)
```

### Imputation (Filling Data)
[[02 Data Preprocessing#Imputation (Filling)]]

Replacing missing values with statistical estimates to retain data size.

```python
# Fill missing Age with the Mean (Average)
df['Age'] = df['Age'].fillna(df['Age'].mean())

# Fill missing Salary with the Median (Resistant to outliers)
df['Salary'] = df['Salary'].fillna(df['Salary'].median())
```

## Outliers
[[03 Cleaning and Transforming#Outliers]]

**Outliers** are data points that differ significantly from other observations. They can cause serious problems in statistical analyses and machine learning models (like pulling the Mean far away from the center).

### Detection: Z-Score Method
The Z-Score measures exactly how many standard deviations ($\sigma$) an element ($x$) is from the mean ($\bar{x}$).

$$Z = \frac{x - \bar{x}}{\sigma}$$

**Rule of Thumb:** If $|Z| > 3$, the value is considered an outlier (it lies outside the 99.7% confidence interval of a normal distribution).

```python
from scipy import stats

data = {'Score': [85, 90, 88, 92, 85, 89, 94, 90, 88, 300]} # 300 is obviously an outlier
df_scores = pd.DataFrame(data)

# Calculate Z-Scores
z_scores = np.abs(stats.zscore(df_scores['Score']))

# Filter out the outliers (Keep only if Z < 3)
df_clean = df_scores[(z_scores < 3)]

print(f"Original count: {len(df_scores)}")
print(f"Cleaned count: {len(df_clean)}")
```

### Detection: IQR Method
The **Interquartile Range (IQR)** method does not assume the data is normally distributed, making it highly robust.

1.  **Q1 (First Quartile):** 25th Percentile. The value at the $\left(\frac{n+1}{4}\right)^{th}$ position of the sorted data.
2.  **Q2 (Median):** 50th Percentile. The value at the $\left(\frac{n+1}{2}\right)^{th}$ position of the sorted data.
3.  **Q3 (Third Quartile):** 75th Percentile. The value at the $3\left(\frac{n+1}{4}\right)^{th}$ position of the sorted data.
4.  **IQR:** $Q3 - Q1$
5.  **Lower Bound:** $Q1 - 1.5 \times IQR$
6.  **Upper Bound:** $Q3 + 1.5 \times IQR$

Any value outside the Upper and Lower bounds is considered an outlier.

```python
Q1 = df_scores['Score'].quantile(0.25)
Q3 = df_scores['Score'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Filter using the IQR bounds
df_clean_iqr = df_scores[(df_scores['Score'] >= lower_bound) & (df_scores['Score'] <= upper_bound)]
```

## Noise in Data
**Noise** refers to meaningless or corrupt data, or random variance in a signal. It obscures the underlying pattern or trend, especially in Time Series data (like stock prices).

### Binning
Binning smooths sorted data by referencing its neighborhood (nearby values). 
- **Method:** Sort the data, divide it into equal-frequency "bins" (buckets), and then smooth each bin by finding its mean, median, or boundaries.
- **Example:** Smoothing by Bin Means. If Bin 1 contains `[4, 8, 15]`, the mean is `9`. The bin becomes `[9, 9, 9]`. This brutally aggressively flattens local noise.

```python
# Create 3 equal-width bins and replace values with the bin's intervals/means
df['Binned_Age'] = pd.cut(df['Age'], bins=3, labels=['Young', 'Middle', 'Senior'])

# For mathematical smoothing (replacing with Bin Mean)
# Group the data into 3 quantiles, then transform each value to the mean of its quantile
df['Smoothed_Age'] = df.groupby(pd.qcut(df['Age'], q=3))['Age'].transform('mean')
```

### Filtering & Smoothing
Filtering is a broad concept where we remove unwanted components from a signal.

#### Simple Moving Average Filter (SMA)
Calculates the unweighted mean of the previous $k$ data points to filter out short-term fluctuations.

$$SMA = \frac{p_1 + p_2 + ... + p_k}{k}$$

```python
# Create a noisy time series dataset
np.random.seed(42)
days = pd.date_range('2023-01-01', periods=100)
noisy_sales = np.linspace(10, 50, 100) + np.random.normal(0, 5, 100) # Trend + Noise
df_noise = pd.DataFrame({'Sales': noisy_sales}, index=days)

# Calculate 7-Day Simple Moving Average
df_noise['SMA_7'] = df_noise['Sales'].rolling(window=7).mean()
```

#### Exponential Moving Average (EMA)
Similar to SMA, but gives **more weight** to recent prices, making it react faster to recent changes.

```python
# Calculate Exponential Moving Average (span essentially acts like window)
df_noise['EMA_7'] = df_noise['Sales'].ewm(span=7, adjust=False).mean()
```

#### Regression Smoothing (Trend Filtering)
Instead of looking at local averages window-by-window, Regression Smoothing fits an underlying mathematical curve (like a linear or polynomial line) to the *entire* dataset simultaneously. It highlights the macroscopic "Trend" while ignoring the microscopic deviations (noise).

## Data Distribution & Skewness
Before analyzing, we must understand the shape of our data. Normal data looks like a symmetrical bell curve. **Skewness** is a measure of asymmetry.

1.  **Right Skew (Positive Skew):** The tail extends to the right. The Mean is dragged higher than the Median. (e.g., Salaries in a company: most earn average, but a few executives earn millions, creating a long right tail).
2.  **Left Skew (Negative Skew):** The tail extends to the left. The Mean is dragged lower than the Median.

![[Pasted image 20260306131422.png]]

### Fixing Skewness (Transformations)
Many machine learning algorithms require normally distributed data. We can mathematically "uncrunch" the data.

#### Log Transformation
Particularly effective for heavily **Right-Skewed** data. It compresses large values significantly more than small values, pulling the long right tail inward.

```python
# Convert right-skewed salary data to a normal distribution
df['Log_Salary'] = np.log(df['Salary']) # Or np.log1p(df['Salary']) if there are zeroes
```

#### Square Root Transformation
A milder version of the Log Transform, useful for moderately skewed data or count data.

```python
df['Sqrt_Salary'] = np.sqrt(df['Salary'])
```

## Encoding Categorical Data
[[02 Data Preprocessing#Encoding Categorical Data]]

Computers understand numbers, not text. We must wrangle categorical (text) variables like "Color" or "City" before feeding them into models.

- **Label Encoding:** Assigns an integer to each class ($Red=0, Blue=1, Green=2$). *Warning:* Models might falsely interpret this as ordinal (thinking $Green > Red$ because $2 > 0$).
- **One-Hot Encoding:** Creates a new binary column for every category ($Is\_Red=1$, $Is\_Blue=0$). *Solution:* Prevents ordinal bias, but increases dataset width.

## Transformation and Normalization
[[03 Cleaning and Transforming#Feature Scaling]]

When variables are measured at different scales (e.g., Age in tens, Salary in tens of thousands), algorithms that rely on distance (like KNN or Neural Networks) will be biased towards the larger scale variable.

> [!HELP] Why choose Standardization over Min-Max Scaling?
> **Min-Max Scaling** strictly bounds the data to `[0, 1]`. However, if your data possesses extreme, unhandled outliers, Min-Max will violently compress all your "normal" data points down into a tiny range (e.g., `[0, 0.01]`) just to accommodate the outlier at `1.0`.
> 
> **Standardization**, however, is not bound to a specific range. Because it centers the data mathematically around the mean, it is significantly more robust to the presence of outliers.

### Min-Max Scaling (Normalization)
Rescales data to a fixed range, usually **\[0, 1\]**.

$$X_{norm} = \frac{X - X_{min}}{X_{max} - X_{min}}$$

```python
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
# Assuming we have a DataFrame 'df' with 'Age' and 'Salary'
df_scaled = scaler.fit_transform(df)
```

### Standardization (Z-Score Scaling)
Rescales data to have a **mean of 0** and a **standard deviation of 1**. Best used when the data follows a Gaussian (normal) distribution.

$$X_{stand} = \frac{X - \bar{x}}{\sigma}$$

```python
from sklearn.preprocessing import StandardScaler

std_scaler = StandardScaler()
df_standardized = pd.DataFrame(std_scaler.fit_transform(df))
```
