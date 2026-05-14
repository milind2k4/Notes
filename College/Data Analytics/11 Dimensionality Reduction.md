Links: [[00 Data Analytics]], [[10 Clustering]]
___
# Dimensionality Reduction

**Dimensionality Reduction** is the process of reducing the number of input variables (features or "dimensions") in a dataset while simultaneously preserving as much of the original, critical information as possible.

## The Curse of Dimensionality
In machine learning, adding more features initially improves model performance. However, as the number of dimensions continues to increase exponentially, the volume of the space increases so fast that the available data becomes incredibly sparse. 

This causes algorithms (especially distance-based ones like k-NN or K-Means) to fail because the mathematical "distance" between all points starts to look identical in hyper-dimensional space. Dimensionality reduction cures this "curse".

## Principal Component Analysis (PCA)
**PCA** is the most popular technique for Unsupervised dimensionality reduction. It mathematically transforms a large set of correlated variables into a much smaller set of entirely uncorrelated variables called **Principal Components**.

### How PCA Works
1. **Standardization:** PCA is incredibly sensitive to scale. The algorithm must first mathematically scale all features so they contribute equally (e.g., standardizing Age and Income so an income of \$100,000 doesn't overpower an age of 30).
   $$Z = \frac{x - \mu}{\sigma}$$
   *(Where $\mu$ is the mean and $\sigma$ is the standard deviation).*
2. **Covariance Matrix:** It calculates a matrix to understand how the variables in the dataset are varying from the mean with respect to each other.
   $$Cov(X,Y) = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{n-1}$$
   *(A positive covariance means features increase together; negative means they are inversely related).*
3. **Eigenvectors and Eigenvalues:** PCA computes the mathematical "directions" (Eigenvectors, $v$) where the data varies the most, and the "magnitude" of that variance (Eigenvalues, $\lambda$). This is solved using the characteristic equation of the Covariance Matrix ($C$):
   $$\det(C - \lambda I) = 0$$
   *(Where $I$ is the Identity Matrix).*
4. **Principal Components:** The algorithm ranks these new lines (components). 
   - **PC1 (Principal Component 1):** The line that captures the absolute maximum amount of variance (information) in the data (associated with the largest Eigenvalue).
   - **PC2:** The line that captures the second-most variance, and is strictly perpendicular (orthogonal) to PC1.

> [!NOTE] The Result
> Instead of feeding an algorithm 50 highly redundant features, you feed it just the top 2 or 3 Principal Components. You lose a tiny fraction of the original detail, but you massively increase computational speed and visualize hyper-dimensional data perfectly on a standard 2D or 3D graph!

#### Example: 2D to 1D PCA
Imagine a dataset with 4 data points and 2 features ($X$ and $Y$).

| Point  | $X$ | $Y$ |
| ------ | --- | --- |
| **P1** | 1   | 7   |
| **P2** | 7   | 1   |
| **P3** | 13  | 19  |
| **P4** | 19  | 13  |

**Step 1: Calculate the Mean and Center the Data**
First, find the mean of each feature:
$$ \bar{X} = \frac{1 + 7 + 13 + 19}{4} = 10 $$
$$ \bar{Y} = \frac{7 + 1 + 19 + 13}{4} = 10 $$

Subtract the means from every point to center the data around $(0,0)$:

| Point | Centered $X$ ($X - \bar{X}$) | Centered $Y$ ($Y - \bar{Y}$) |
|---|---|---|
| **P1** | -9 | -3 |
| **P2** | -3 | -9 |
| **P3** | 3 | 9 |
| **P4** | 9 | 3 |

**Step 2: Calculate the Covariance Matrix ($C$)**
Using the sample covariance formula $\frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{n-1}$ (where $n-1 = 3$):

$$ Var(X) = \frac{(-9)^2 + (-3)^2 + 3^2 + 9^2}{3} = \frac{180}{3} = \mathbf{60} $$

$$ Var(Y) = \frac{(-3)^2 + (-9)^2 + 9^2 + 3^2}{3} = \frac{180}{3} = \mathbf{60} $$

$$ Cov(X,Y) = \frac{(-9)(-3) + (-3)(-9) + (3)(9) + (9)(3)}{3} = \frac{108}{3} = \mathbf{36} $$

This yields our final symmetric Covariance Matrix:
$$ C = \begin{bmatrix} 60 & 36 \\ 36 & 60 \end{bmatrix} $$

**Step 3: Solve for Eigenvalues ($\lambda$)**
Set the determinant of $(C - \lambda I)$ to $0$:

$$ 
\begin{align*}
\det \begin{bmatrix} 60 - \lambda & 36 \\ 36 & 60 - \lambda \end{bmatrix} &= 0 \\
(60 - \lambda)(60 - \lambda) - (36 \times 36) &= 0 \\
(60 - \lambda)^2 - 1296 &= 0 \\
(60 - \lambda)^2 &= 1296 \\
60 - \lambda &= \pm 36
\end{align*}
$$

Solving for $\lambda$ gives our two eigenvalues (representing the magnitude of variance on each axis):
- $\lambda_1 = 60 + 36 = \mathbf{96}$
- $\lambda_2 = 60 - 36 = \mathbf{24}$

*(Note: PC1 retains $96 / (96+24) = \mathbf{80\%}$ of the data's entire variance!)*

**Step 4: Solve for Eigenvectors ($v$)**
Plug $\lambda_1 = 96$ back into the matrix equation $(C - \lambda I)v = 0$ to find the direction of PC1:

$$
\begin{align*}
\begin{bmatrix} 60 - 96 & 36 \\ 36 & 60 - 96 \end{bmatrix} \begin{bmatrix} v_1 \\ v_2 \end{bmatrix} &= \begin{bmatrix} 0 \\ 0 \end{bmatrix} \\
\begin{bmatrix} -36 & 36 \\ 36 & -36 \end{bmatrix} \begin{bmatrix} v_1 \\ v_2 \end{bmatrix} &= \begin{bmatrix} 0 \\ 0 \end{bmatrix}
\end{align*}
$$

This creates the linear equation $-36v_1 + 36v_2 = 0$, meaning $v_1 = v_2$. 
The raw eigenvector is $\begin{bmatrix} 1 \\ 1 \end{bmatrix}$. 

To normalize it (scale its length to exactly 1), divide by its magnitude $\sqrt{1^2 + 1^2} = \sqrt{2} \approx 1.414$.

$$ \text{Normalized PC1 Eigenvector: } \mathbf{[0.707, 0.707]} $$

**Step 5: Project the Data (Dimensionality Reduction)**
We drop PC2 entirely since PC1 already contains $80\%$ of the information. We project our original 2D points down to a 1D line by calculating the dot product of the *centered* points and the *PC1 Eigenvector*:

$$
\begin{align*}
\text{New 1D P1} &= (-9 \times 0.707) + (-3 \times 0.707) = \mathbf{-8.484} \\
\text{New 1D P2} &= (-3 \times 0.707) + (-9 \times 0.707) = \mathbf{-8.484} \\
\text{New 1D P3} &= (3 \times 0.707) + (9 \times 0.707) = \mathbf{8.484} \\
\text{New 1D P4} &= (9 \times 0.707) + (3 \times 0.707) = \mathbf{8.484}
\end{align*}
$$

> [!NOTE] The Final Result
> The dataset has been successfully compressed from $X, Y$ coordinates into a single mathematical dimension.

### Implementation in Python
Because PCA is mathematically intense, data scientists rely heavily on `scikit-learn` to compute the eigenvectors automatically. Notice how **Standardization** is an explicitly required step before initializing the PCA algorithm:

```python
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Assume 'X' is our massive, 50-dimensional dataset
# X = pd.read_csv('hyper_dimensional_data.csv')

# 1. Standardization (CRITICAL for PCA to work correctly)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 2. Apply PCA to reduce the 50 dimensions down to just 2
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# 3. Check how much of the original information we successfully preserved
print(f"Variance explained by PC1: {pca.explained_variance_ratio_[0]*100:.2f}%")
print(f"Variance explained by PC2: {pca.explained_variance_ratio_[1]*100:.2f}%")
print(f"Total information retained: {sum(pca.explained_variance_ratio_)*100:.2f}%")
```
