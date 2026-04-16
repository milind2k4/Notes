Links: 
___
# Data Analytics Staging
## Distributions of Data 

## Ideas in Probability 
### Random Variables 
### Probability Distributions 
## Bayes Theorem 

## Supervised and Unsupervised Learning 
## Classification 
### Decision Tree

Entropy:

Entropy defines the uncertainty in the data. It is defined by outliers and noise in the data. 

In an unbalanced dataset, the entropy is low. 

Entropy: 
$$E(S) = \sum_{i=1}^{c} -p_{i} \log_{2}p_{i}$$
where c is the total number of classes and $p_{i}$ is the probability of getting that probability as output. 

If there is binary classification, the min entropy is 0 and max is 1.

#### Information Gain 
$$\symup{Information Gain = E(Parent) - (Weighted Average) \times E(Children)}$$

## k-NN

## Naive Byes 

### Conditional Probability 
If two events are independent, 

$$
\begin{split}
P(A \cap B) &= P(A) \times P(B|A) \\
P(B \cap A) &= P(B) \times P(A|B) \\ \\

P(A) \times P(B|A) &= P(B) \times P(A|B) \\ \\

P(B|A) &= \frac{ P(B) \times P(A|B) }{ P(A) }
\end{split}
$$

$$P(y|x_{1}x_{2}x_{3}\dots) = \frac{ P(y) \times P((x_{1}x_{2}x_{3}\dots)|y) }{ P(x_{1}x_{2}x_{3}\dots) }$$

Bernoulli Multinominal Gaussian 

## Clustering 

## K means 

## Hierarchical Clustering

Unsupervised learning algo 

It forms clusters 

It is used for data exploration and pattern discovery. 

It builds a tree like structure (dendogram) that helps visualize the relationships and deicde the optimal no of clusters. 

Does not require predefining the number of clusters. 

### Dendogram 
A tree that shows how clusters are merged step by step. 
We cut the dendogram at certain height to form final clusters. 


TODO: Add figure 

### Approaches 
Agglomerative: Is is most used approach 

Divisive:


### Linkage Criteria 

Single linkage 
Complete Linkage 
Average Linkage 

### Steps to Perform 
Calculate distance between datapoints. 

Find the closest pair of points and merge them 

Recalculate the distance between the new clusters 

Repeat until all points are merged into one. 


Threshold Value: Select the longest vertical line such that no horizontal line passes through it


Add example 

| Point | x   | y   |
| ----- | --- | --- |
| a     |     |     |
| b     |     |     |
| c     |     |     |
| d     |     |     |
| e     |     |     |

## Dimensionality Reduction 
### PCA 

## Association 

## Data Mining 

Process of extracting useful, non trivial and previously unknown patterns from large datasets. 

It focuses on identifying relationships, correlations and structures in data that are not immediately visible. 

Aka Market Basket Analysis 

### Support Measure 
How frequently an itemset appears in 


### Association Rules 

### Confidence Measure 

## Rule Mining 

### Apriori Algorithm 

