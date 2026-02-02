Links: 
___
# ANN and ML

### Supervised
- Classification: When the output is a category, like Red Blue, Disease or No disease
	- Random Forest Algo 
	- Decision Tree Algo (ID3)
	- Naive Bayes Algo
	- Support Vector Machine Algo (SVM)
- Regression: When the output variable is a real value. Like dollars or weight. 
	- Simple Linear Regression 
	- Multivariate Regression 

### Data Preprocessing
Cleaning, transforming, preparing raw data.

Why is it important?
If any data is missing, it might affect the final performance.
Real world data is messy, it has missing values.
We might need to convert text to numbers before feeding it into a model.
There might also be inconsistent scaling in the data, so we might need to normalize it.
Algo requires numerical input.

#### Handling Missing Values 
- MCAR: Missing Completely At Random 
- MAR
- MNAR

```py
import pandas as pd 
df = pd.read_csv("data.csv")
```

##### Remove Rows 
Remove the rows which are not important and have missing  values.

```py
# Drop rows with missing values 
# Drop Not Available
df.dropna(inplace=True) 

# Drop columns with missing values 
df.dropna(axis=1, inplace=True)
```

##### Fill with Mean/Median/Mode 
Mean: Affected by Outliers 
Median: Not affected by outliers 
Mode: Not affected by outliers 

```py
df['age'].fillna(df['age'].mean(), inplace=True)
```

##### Imputation (Replacing missing Values)
Same as fill, just that the term for replacing missing values is Imputing.

```py
from sklearn.impute import SimpleImputer 

imputer = SimpleImputer(stratergy='mean')
df['age'] = imputer.fit_transform(df['age'])
```

##### Forward/Backward Fill 

```py 
df.fillna(method='ffill')
df.fillna(method='bfill')
```

### Encoding Categorical Variables 
ML models cannot understand text. 

There are two types of Categorical Variables:
- Nominal: No order 
- Ordinal: Ordered (Low, Medium, High)

#### Label Encoding (Ordinal Data)
```py
from sklearn.preprocessing import LabelEncoder 

le = LabelEncoder()
df['size'] = le.fit_transform(df['size'])
```

We should not use it for nominal data as it can lead to misleading values. 

#### One-Hot Encoding (Nominal Data)

```py
df = pd.get_dummies(df, columns=['city'], drop_first=True)
```

```py
from sklearn.preprocessing import OneHotEncoder 

ohe = OneHotEncoder()
endoded = ohe.fit_transform(df['city'])
```