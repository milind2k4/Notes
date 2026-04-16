Links: 
___
# Cleaning and Transforming Incomplete and Noisy Dataset

## Why is Cleaning Important?
Real-world data is rarely clean. It suffers from:
- **Incompleteness:** Lacking attribute values.
- **Noise:** Containing errors or outliers.
- **Inconsistency:** Containing discrepancies in codes or names.

> [!CAUTION] Garbage In, Garbage Out
> If the data is of poor quality, the model will be of poor quality, regardless of how sophisticated the algorithm is.

## Duplicate Records
Duplicate rows can bias the model by giving extra weight to specific data points.
```python
# Remove duplicate rows
df.drop_duplicates(inplace=True)
```

## Outliers
> [!HELP] Why?
> Outliers can skew statistical measures (like Mean/Gradient). If not removed, the model tries to learn from these extreme "errors," leading to poor performance on normal data (Overfitting to noise).

> [!NOTE] Definition
> **Outliers** are data points that differ significantly from other observations. They can be caused by measurement errors or valid extreme variability.

Sometimes, outliers are important as they contain useful information like in Fraud Detection. 

Outliers are also domain dependent. What is considered an outlier in one case, might not be in another domain. 

### Detection Method 1: IQR (Interquartile Range)
- **Robust:** Not affected by extreme outliers.
- **Bounds:** `[Q1 - 1.5*IQR, Q3 + 1.5*IQR]`

```python
Q1 = df['salary'].quantile(0.25)
Q3 = df['salary'].quantile(0.75)
IQR = Q3 - Q1

# Filtering out outliers (keeping valid data)
df_clean = df[~((df['salary'] < (Q1 - 1.5 * IQR)) 
			 | (df['salary'] > (Q3 + 1.5 * IQR)))]
```

### Detection Method 2: Z-Score
- Indicates how many standard deviations a data point is from the mean.
- **Threshold:** Typically, if Z-Score > 3 or < -3, it is an outlier.
- *Assumption:* Data follows a Normal Distribution.

```python
from scipy import stats
import numpy as np

# Keep only rows with Z-score < 3
df = df[(np.abs(stats.zscore(df['salary'])) < 3)]
```

## Inconsistent Formats
Data might be entered differently (e.g., "NY", "ny", "N.Y.").
```python
# Standardize text to lowercase and strip whitespace
df['city'] = df['city'].str.lower().str.strip()
```

## Noise & Smoothing (Binning)
Noisy Data is data that is meaningless or corrupt.
- **Binning:** Converting continuous data into discrete "bins" (e.g., Age 18-25, 26-35).
    - **Fixed Width:** e.g., 0-10, 10-20.
    - **Quantile:** Each bin has the same number of data points.
- **Smoothing:** Using moving averages to reduce noise.

**Example:**
Sorted Data for Price: `[4, 8, 15, 21, 21, 24, 25, 28, 34]`

**1. Partition into Bins (Equi-depth of 3):**
- Bin 1: `[4, 8, 15]`
- Bin 2: `[21, 21, 24]`
- Bin 3: `[25, 28, 34]`

**2. Smoothing by Bin Means:**
- Bin 3 Mean (29): `[29, 29, 29]`

**Using Pandas:**
```python
# 1. Binning (Fixed Width)
# Bins: 0-10, 10-20, ...
df['age_group'] = pd.cut(df['age'], bins=3, labels=["Young", "Mid", "Old"])

# 2. Binning (Quantile/Equi-depth)
# Each bin has same number of people
df['salary_bin'] = pd.qcut(df['salary'], q=4, labels=False)

# 3. Smoothing (Rolling Average)
# Moving average of window size 3
df['price_smooth'] = df['price'].rolling(window=3).mean()
```

## Feature Scaling
> [!QUESTION] Why?
> If one feature has huge values (Salary: 100,000) and another small (Age: 25), distance-based algorithms (KNN) will only see Salary. Gradient Descent will also struggle to converge (takes jagged steps). Scaling puts everyone on a level playing field (0-1).

Standardizing the range of independent variables.

### Normalization (Min-Max Scaling)
Scales values between 0 and 1.
$$ X_{new} = \frac{X - X_{min}}{X_{max} - X_{min}} $$
*Use when:* Data doesn't follow a Gaussian distribution, or for algorithms like Neural Networks / KNN.

```py
from sklearn.preprocessing import MinMaxScaler
norm = MinMaxScaler()
df['Salary_Norm'] = norm.fit_transform(df[['Salary']])
```

### Standardization (Z-Score Scaling)
Scales data to have a mean of 0 and standard deviation of 1.
$$ X_{new} = \frac{X - \mu}{\sigma} $$
*Use when:* Data follows a Gaussian distribution or algorithms assume it (Linear Regression, SVM).

```python
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
df['Age_Scaled'] = scaler.fit_transform(df[['Age']])
```

### Log Transformation
Applies natural log to the data: $log(x)$.
*Use when:* Data is **highly skewed** (e.g., Income data). It compresses large values and spreads small values, making the distribution more normal.






