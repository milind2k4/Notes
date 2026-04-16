Links: 
___
# Types of Machine Learning

Machine Learning algorithms are categorized by how they learn and the type of data they use.

> [!TIP] The Three Types Simplified
> - **Supervised:** Learning with a Teacher (Answer Key provided).
> - **Unsupervised:** Learning by Self-Discovery (No Answer Key).
> - **Reinforcement:** Learning by Trial and Error (Rewards/Punishments).


## Supervised Learning
The model is trained on **labeled data**.

The system is given both the input and the correct output (ground truth). It learns the mapping function from input to output.

**Key Requirement:** A **feature list** where data is already mapped to the target.

> [!EXAMPLE] Labeled Data Example
> Input: Image of a cat.
> Label: "Cat".
> The model learns to associate the pixels with the label "Cat".

```mermaid
graph LR
    S[Supervised Learning] --> C[Classification]
    S --> R[Regression]
    C -->|Discrete| Out1(Category)
    R -->|Continuous| Out2(Number)
```

### Classification
Used when the output variable is a **Category** (Discrete).

**Output:** Class labels (e.g., Spam/Not Spam, Disease/No Disease, Red/Blue).

**Common Algorithms:**
- **Decision Tree (ID3):** Uses a tree-like model of decisions.
- **Random Forest:** A collection (ensemble) of decision trees.
- **Support Vector Machine (SVM):** Finds the best boundary (hyperplane) to separate classes.

#### Naive Bayes Classifier
A family of classification algorithms based on applying Bayes' Theorem (updating probability based on prior evidence). It calculates the probability of a data point belonging to each possible class, and predicts the class with the highest probability.

- **The "Naive" Assumption:** It strictly assumes that all input features are independent of each other (e.g., In a fruit classifier, it assumes "Color=Yellow" and "Shape=Curved" are completely unrelated traits). In the real world, this is rarely true, yet the algorithm still performs shockingly well.

> [!EXAMPLE] Spam Email Filtering
> A classic usecase. The classifier looks at historical data (Prior): 20% of all incoming emails are Spam, 80% are "Ham" (Not Spam).
> 
> A new email arrives containing the words "Free", "Winner", and "Rolex" (Evidence/Likelihood).
> 
> Using Bayes' Theorem, it calculates the **Posterior Probability**: 
> "Given these specific words, what is the probability this is Spam vs Ham?"
> If $P(Spam|Words) > P(Ham|Words)$, it redirects the email to the Junk folder.

### Regression
[[College/ANN and ML/07 Regression Analysis|Regression analysis]]

Used when the output variable is a **Real Value** (Continuous).

**Output:** Numbers (e.g., Price in dollars, Weight, Temperature).

**Common Algorithms:**
- **Simple Linear Regression:** Fits a line to the data.
- **Multivariate Regression:** Uses multiple input variables.


## Unsupervised Learning
The model is trained on **unlabeled data**.

**Goal:** To discover hidden patterns, structures, or groupings within the data without human intervention.
**Use Case:** When we do not have mapped outputs and the machine must find structure itself.

### Clustering
A common unsupervised technique that groups similar data points together. Common algorithms include:
- **K-Means:** Partitions data into 'k' distinct clusters.
- **Mean Shift:** Updates candidates for centroids to be the mean of the points within a given region.
- **DBSCAN:** Density-based spatial clustering that finds core samples of high density.
- **Principal Component Analysis (PCA):** Used for dimensionality reduction (simplifying complex data).

> [!EXAMPLE] Customer Segmentation
> A bank has millions of customers. By clustering them based on spending habits, they find 3 groups: "Students", "High Earners", and "Retirees". They can then target each with different offers.

### Association
Discovering mathematical rules that describe large portions of your data.

**Goal:** Finding relationships between variables in large databases.
**Example:** Market Basket Analysis (e.g., "If a customer buys Bread, they are 80% likely to buy Butter").
**Algorithm:** Apriori.

> [!EXAMPLE] Playlist Generation
> Streaming services use association rules: "Users who listen to *Song A* frequently listen to *Song B*." This builds your "Discover Weekly" playlist.

## Reinforcement Learning (RL)

Learning by interacting with an environment. It is **feedback-based**.

**Mechanism:** An **Agent** performs actions and observes the results.

**Feedback Loop:**
- **Positive Reward:** For a good action (e.g., winning a point).
- **Negative Reward:** For a bad action (e.g., crashing).

**Goal:** To maximize the cumulative reward over time.
**Examples:** Robotics, Game Playing (AlphaGo).

> [!EXAMPLE] Training a Dog
> - **Action:** Dog sits on command.
> - **Reward (+ve):** Treat.
> - **Result:** Probability of sitting increases.
> - **Action:** Dog chews shoes.
> - **Punishment (-ve):** Scolding.
> - **Result:** Probability of chewing decreases.

```mermaid
graph TD
    Agent -->|Action| Env[Environment]
    Env -->|Reward + State| Agent
```
