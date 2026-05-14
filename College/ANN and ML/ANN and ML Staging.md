Links: 
___
# ANN and ML Staging

### PCA (Principle Component Analysis)
PCA is not used widely for Data Visualization. 

#### Mean Centering 
The mean of the data should be (0,0).

It makes is so that rotation has no effect on the data. 

$$x_{i} = x_{i} - \bar{x}$$

#### Co Variance Analysis 

$$
\begin{split}
Z &= \begin{bmatrix}
x = a & b \\
y = c & d
\end{bmatrix} \\ \\

cov(x,y) &= \begin{bmatrix}
cov(a,b) & 
\end{bmatrix}
\end{split}
$$

$$cov(M) = \frac{ 1 }{ n-1 }ZZ^{T}$$
Z is the matrix. 

#### Eigen Value Calculation 
The max of the eigen value contains more information about the data than the lower values. 

Eigen Decomposition: 

## Outliers 

There are 3 types of outliers:
#### Global Outliers
Some data points which are different from all the rest of the data. 

aka Point Anomalies 

#### Contextual Outliers 
Outliers relative to a specific context or condition. 

#### Collective Outliers 
A group of relative points which behave anomalously. 

### Outlier Detection 
#### Looking at the Data 

#### Box Plots 

#### Z Score Method 

#### IQR Method 

#### Isolation Forest 

# Clustering 
## K Means 
We want to make K clusters out of the data. 

We will randomly pick K values from the dataset and put them as the centers for K clusters.

Now we will take each point and find the distance from each cluster's center. We will put the point into the cluster which is closest. 

TODO: add a numerical example 

## Decision Tree 

It is classification regression algo. 

## Isolation Forest 
Extremely Randomized Tree Regressor 

The score of the outlier is higher than other normal nodes. 

Unsupervised 

Used to detect outliers 

1. Random Partitioning 
2. Recursive Splitting 
3. Path Length: Outliers begin far and distinct from the main cluster 
4. Anomaly Score: The average path length of a point among all the trees. A score closer to 1 means anomaly. 

Benefits:
Scalability 
No Distribution Assumptions 
Sub sampling 

Applications:

## DBSCAN 

It groups data based on density. 

## Optics

We use it where the density varies. 

Min number of points to make a cluster remains the same. 

The paraments are epsilon, min. number of points, core points, core distance, reachability distance. 

Core Distance: 

Reachability Distance: 

It makes clusters within clusters. It is suitable for complex datasets. 

It can make clusters of varying densities. 

## Hyper Parameter Tuning 
What are Parameters?

What are hyper parameters? 

Why "hyper"?

It avoids overfitting and underfitting. And helps with generalization of the model. 

### Techniques for HPT 

#### Traditional 
Deterministic 
Gradient Required 
Simple, convex problem type 
Fast 
Limited global search 
Low Flexibility 

##### Grid Search CV
We take all possible combinations of all possible values for all the hyperparameters and run the algo for each. Then we "search" for the best result of them. The corresponding values for the parameters are the optimal values. 

CV means cross validation
##### Random Search CV 
Randomly picks a combination of hyperparameters instead of trying all combinations. 

It picks the value of hyperparameters from the given range. 

##### Bayesian Optimization 
Treats the tuning of hyperparameters as a mathematical optimization problem. It learns from past results. 
Convex problem means local minima is global minima 

#### Metaheuristic 
Stocastic 
Gradient Not Required 
Complex, non linear problem type 
slower 
Strong global search 
High Flexibility 

The algorithms here are nature inspired. 

##### Evolutionary Algorithms 
Population 
Fitness Function 
Selection 
Genetic Operators 
Termination 

##### Differential Evolution 



##### Particle Swarm Optimization
Based on the social behaviour of birds and fish. 


##### Ant Colony Optimization 
Based on the behaviour of ants.

##### Manta rays Optimization 

##### Simulated Annealing 
Based on cooling down of metal 

## Ensemble Learning 

Ensemble means that we are using more than one model to generate the prediction and combining all of them to get a better result that one model individually. 

It is simply- asking a group of people for advice, i.e. knwoledge of the crowd. 

Here, mistakes of one model can be reduced by the others. 

#### Bagging
Models are trained individually on random subsets of the training data. 

Their results are then combined, usually, by averaging (for regression) or voting (for classification). This helps reduce variance and prevents overfitting. 

#### Boosting 
Models are trained one after another. Each successive model focuses on fixing the errors made by other models. The prediction of one model is treated as input for the next one. The final prediction is a weighted combination of all models which helps reduce bias (underfitting) and improve accuracy.

#### Stacking 

We train multiple models which are all different types are trained and their predictions are used as inputs for a meta model which then uses these predictions to learn how to best combine these models. The meta model gives better performance than any of the individual models. 

## Bagging 
Bagging classifier can be used for both regression and classification. 

1. Bootstrap Sampling: The dataset is divided into multiple subsets by sampling with replacement, creating diverse training data. 
2. Base model training: A separate model is trained on each subset. 
3. Prediction Aggregation: Predictions from all are combined using majority voting (classification) or averaging (regression).
4. OOB Evaluation: Samples not in any of the subsets are then used for evaluation. 

BaggingClassifier


## Boosting 

Multiple weak models are trained one after another and each new model focues on correcting the errors of the previous one to build a strong model. 

1. Initialize the Weights: Start with equal weights fro each model 
2. Train weak learner 
3. Sequential Learning 
4. Weight Adjustment 

AdaBoostClassifier 

## Random Forest 
It is a ml algo which uses many decision trees to make better predictions. Each tree looks at a different random parts of the data and their results are combined by voting for classification or averaging for regression. 

- Create many decision trees 
- Pick random features 
- Each tree makes a prediction 
- Combine the predictions 

The use of random forest makes it easy to avoid overfitting. 

It works well with datasets which have missing data, big complex data, shows feature importance. It can also be used for classification and regression. 

Adv:
1. Provides accurate predictions 
2. Handle missing data 
3. No need for normalization or standardization 
4. Reduce overfitting 

Disadv:
1. It can be computationally expensive.
2. Time taking 
3. Harder to interpret a model compared to simple model like decision tree. 

## AutoML 
It is a tool which automates the 
