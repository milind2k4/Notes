Links: [[02 Data Preprocessing]], [[03 Cleaning and Transforming]]
___
# Feature Engineering and Selection

**Feature Engineering** is the process of selecting, manipulating, and transforming raw data into features that can be used in supervised learning. In short, it is the act of extracting more mathematical meaning from the data we already have.

It is often considered the most important step in the Machine Learning pipeline, taking up to 80% of a Data Scientist's time.

## Importance
- **Boost Accuracy:** Better features directly equate to better performance. A simple model with great features usually beats an incredibly complex model with poor features.
- **Reduce Overfitting:** Stripping out irrelevant or noisy features prevents the model from memorizing useless data.
- **Boost Interpretability:** Simpler, highly correlated features make it easier to explain *why* the model made a decision to stakeholders.

## The 5 Steps of Feature Engineering

### Feature Creation
Generating entirely new features from existing ones to highlight relationships the model might miss.
- **Domain Specific:** A doctor knows that BMI = $Weight / Height^2$. Creating a new `BMI` column might predict diabetes far better than weight and height alone.
- **Data Driven:** Creating an `Is_Weekend` boolean column out of a `Date` column to see if sales spike on weekends.
- **Synthetic:** Using algorithms to generate interactions (e.g., $X_1 * X_2$).

### Feature Transformation
Adjusting the distribution or format of a feature without fundamentally changing its meaning, optimizing it for algorithms.
- **Categorical Encoding:** Label Encoding or One-Hot Encoding (See [[02 Data Preprocessing#Encoding Categorical Variables]]).
- **Mathematical Transformations:** Using Log or Square Root transformations to fix skewed data distributions.
- **Binning:** Transforming continuous variables (Age 18, 45, 60) into discrete categories (Young, Middle, Senior).

### Feature Scaling
A subset of Transformation. It adjusts the *range* of the data without altering the shape of the distribution.
- **Min-Max Scaling (Normalization):** Squeezes data between 0 and 1.
- **Standardization:** Centers data around a mean of 0.

> [!QUESTION] Scaling vs. Transformation
> **Scaling** just changes the bounds of the ruler (e.g., measuring height in Meters instead of Centimeters; the shape of the data stays the exact same). 
> **Transformation** fundamentally curves the ruler (e.g., Log Transform pulls distant outliers closer to the mean, altering the distribution's shape).

### Feature Extraction
Reducing the dimensionality of the dataset by creating *brand new*, condensed features that capture the mathematical essence of the original features. The original features act as raw material.
- **Dimensionality Reduction:** Techniques like **PCA (Principal Component Analysis)**. If you have 100 features, PCA might smash them into 10 newly engineered "components" that retain 95% of the variance.

```python
from sklearn.decomposition import PCA

# Compress 10 input features down to 2 Principal Components
pca = PCA(n_components=2)
reduced_features = pca.fit_transform(X)
```

### Feature Selection
Choosing a subset of the *existing* features and explicitly throwing the rest in the trash. Unlike Extraction, the features selected are exactly the same as they were originally.

- **Filter Methods:** Statistical tests (like Correlation or ANOVA) to drop features with low variance or low correlation to the target.
- **Wrapper Methods:** Training the ML model repeatedly with different subsets of features to find the best combination (e.g., Forward Selection).
- **Embedded Methods:** Algorithms that perform feature selection natively during training (e.g., LASSO Regression penalizes useless features by driving their coefficients to zero).

> [!QUESTION] Extraction vs. Selection
> **Selection** is picking 3 ingredients out of 10 from the fridge and throwing the rest away. 
> **Extraction** is taking all 10 ingredients, throwing them in a blender, and pouring out a single, condensed smoothie.

```python
# Feature Selection Example (Filter Method)
from sklearn.feature_selection import SelectKBest, f_classif

# Keep only the top 3 most statistically relevant features
selector = SelectKBest(score_func=f_classif, k=3)
selected_features = selector.fit_transform(X, y)
```

## Advanced Techniques

### Feature Splitting
Dividing a single composite feature into multiple, granular sub-features to uncover insights.
- **Example:** Splitting a `Name` column ("Mr. John Doe") into `Title` ("Mr."), `First_Name` ("John"), and `Last_Name` ("Doe"). The `Title` feature might be incredibly predictive for survival (e.g., on the Titanic dataset, "Dr." or "Master." had higher survival rates).
- **Dates:** Splitting "2023-10-31" into `Year` (2023), `Month` (10), `Day` (31), and `Is_Holiday` (1).

### Text Data Preprocessing (NLP)
Machine Learning models require numbers. Text paragraphs must be heavily engineered.
1.  **Stop Words:** Removing extremely common, mathematically useless words like "the", "a", "is", "in".
2.  **Stemming/Lemmatization:** Reducing derived words to their core root. (e.g., "Fishing", "Fished", "Fisher" all become "Fish").
3.  **Vectorization (Bag of Words / TF-IDF):** Converting the cleaned text into numerical vectors that track word frequencies.

```python
import nltk
from sklearn.feature_extraction.text import CountVectorizer

# Example texts
corpus = [
    "The fisherman loves fishing in the lake.",
    "He fished all day yesterday."
]

# In practice you would run an NLTK stemmer here to reduce fishing/fished to fish

# Convert text into a matrix of token counts
vectorizer = CountVectorizer(stop_words='english')
X_vectorized = vectorizer.fit_transform(corpus)

print(vectorizer.get_feature_names_out()) 
# Notice "the", "in", "he" are automatically stripped out!
```

## Automated Feature Engineering Tools
Manually combining and testing features is incredibly time-consuming. Modern "AutoML" platforms can brute-force thousands of combinations automatically:
- **Featuretools:** An open-source Python library for automated feature engineering.
- **TPOT:** Uses genetic programming to optimize ML pipelines.
- **DataRobot:** Enterprise automated machine learning platform.
- **Alteryx:** Data blending and advanced analytics software.
- **H2O.ai:** Scalable, open-source machine learning platform with AutoML.
