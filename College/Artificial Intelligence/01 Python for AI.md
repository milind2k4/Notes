Links:
___
# Python for AI

## NumPy (Numerical Python)

### The Foundation of AI Math

**NumPy** is the fundamental package for scientific computing in Python. It provides support for large, multi-dimensional arrays and matrices, along with a collection of high-level mathematical functions to operate on these arrays.

### Why is it fast?

Standard Python lists are flexible but slow because they store pointers to objects scattered in memory.
**NumPy Arrays (`ndarray`)** are:

1.  **Contiguous Memory:** Elements are stored side-by-side in memory blocks.
2.  **Homogeneous:** All elements are of the same type (e.g., `int32`), removing type-checking overhead.
3.  **Vectorized:** Operations are applied to the entire array at once (SIMD - Single Instruction, Multiple Data) in C-level speed.

### Key Operations

```python
import numpy as np

# 1. Creating Arrays
arr = np.array([1, 2, 3, 4, 5])
matrix = np.zeros((3, 3))  # 3x3 matrix of zeros

# 2. Vectorization (No loops!)
# Traditional Python: [x * 2 for x in arr]
# NumPy:
doubled = arr * 2

# 3. Broadcasting (Magic of dimensions)
# Adding a scalar to a matrix
result = matrix + 10  # Adds 10 to EVERY element
```

### Example: Image Manipulation (as Arrays)

Images are just 3D arrays (Height, Width, RGB Channels).

```python
# Pseudo-code for concept
import numpy as np

# Create a random 100x100 image with 3 color channels
image = np.random.randint(0, 255, (100, 100, 3))

# Turn it grayscale (Average the channels)
# axis=2 means average across the color depth
grayscale = np.mean(image, axis=2)

print(f"Original Shape: {image.shape}") # (100, 100, 3)
print(f"Grayscale Shape: {grayscale.shape}") # (100, 100)
```

### NumPy vs Lists

| Feature      | Python List              | NumPy Array                |
| :----------- | :----------------------- | :------------------------- |
| **Memory**   | High overhead (pointers) | Compact (contiguous)       |
| **Speed**    | Slow (interpreted loops) | Fast (compiled C)          |
| **Types**    | Mixed types allowed      | Fixed type (e.g., float64) |
| **Use Case** | General programming      | Math, Matrix Algebra, AI   |

## Pandas

### Excel for Python

**Pandas** is built on top of NumPy and provides high-level data structures and tools for data analysis. It excels at handling tabular data (rows and columns) with heterogeneous types.

### Series and DataFrames

1.  **Series:** A one-dimensional labeled array (like a single column).
2.  **DataFrame:** A two-dimensional labeled data structure (like a SQL table or Excel sheet). It is essentially a collection of Series sharing the same index.

### Data Manipulation

```python
import pandas as pd

# 1. Creating a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Salary': [50000, 60000, 70000]
}
df = pd.DataFrame(data)

# 2. Filtering
# Select people older than 28
seniors = df[df['Age'] > 28]

# 3. Handling Missing Data
# Fill NaN values with the mean
df['Age'] = df['Age'].fillna(df['Age'].mean())
```

### Example: Preprocessing Pipeline

```python
# Loading a CSV
df = pd.read_csv('dataset.csv')

# Summary Statistics
print(df.describe())

# One-Hot Encoding (Categorical to Numerical)
# Converts 'Color' column (Red, Blue) into columns 'Color_Red', 'Color_Blue' (0 or 1)
df_encoded = pd.get_dummies(df, columns=['Name'])
```

### When to use Pandas?

Use Pandas when you have **structured, tabular data** (SQL dumps, CSVs, Excel files). Do not use it for unstructured data like images or audio (use NumPy/TensorFlow).

## Scikit-learn (sklearn)

### The ML Toolbox

**Scikit-learn** is the industry standard for classical machine learning. It provides simple and efficient tools for data mining and data analysis.

### The Estimator API

Sklearn follows a consistent API design:

1.  **Estimator:** An object that learns from data (e.g., `LinearRegression`).
    - `model.fit(X_train, y_train)`: Trains the model.
2.  **Transformer:** An object that modifies data (e.g., `StandardScaler`).
    - `scaler.fit_transform(X)`: Learns parameters and modifies data.
3.  **Predictor:** An object that predicts new data.
    - `model.predict(X_test)`: Generates predictions.

### A Complete Workflow

```python
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import numpy as np

# 1. Mock Data
X = np.random.rand(100, 5) # 100 samples, 5 features
y = np.random.randint(0, 2, 100) # Binary target (0 or 1)

# 2. Split Data (80% Train, 20% Test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 3. Preprocessing (Scaling)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test) # Note: Only transform test data!

# 4. Train Model
model = LogisticRegression()
model.fit(X_train_scaled, y_train)

# 5. Evaluate
predictions = model.predict(X_test_scaled)
accuracy = accuracy_score(y_test, predictions)
print(f"Model Accuracy: {accuracy:.2f}")
```

### Sklearn vs Deep Learning

- **Use Sklearn for:** Small to medium datasets, structured data, when explainability is key (Decision Trees).
- **Use DL (PyTorch/TF) for:** Massive datasets, unstructured data (Images, Text), complex perceptual tasks.
