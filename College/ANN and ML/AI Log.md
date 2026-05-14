Milind Pushp - 202401100500105
Misty Jangid - 202401100500106

analyse 15_electricity_theft.csv for anomalities and "traps"

> I have completed the analysis of the 15_electricity_theft.csv dataset!
> Here is a quick summary of the biggest "traps" and anomalies that I found:
> Massive Data Leakage (The Fatal Trap): There is a perfect mathematical mapping between the variables. If you subtract annual_billed_kwh from the sum of the 12 month columns, the normal accounts hover around a difference of 0 (variance between -151 and 163). In stark contrast, every single theft case has a difference of over +1,500 kWh! This means the target label is effectively hard-coded into the annual_billed value. Including annual_billed_kwh as a feature will cause an ML model to completely overfit to this subtraction rule and not learn anything real.
>
> Extreme Class Imbalance: There are exactly 28 cases of theft in a dataset of 3000 rows (0.93%). A naive model that guesses "No Theft" will get 99% accuracy off the bat but naturally find 0 frauds. You will need to use F1-Score or Precision/Recall as metrics and employ techniques like SMOTE to balance the dataset.
>
> Imputed / Hardcoded "50"s: The value 50.0 repeatedly appears as the absolute minimum value for consumption across various months and occurs unusually frequently. This typically signifies that "50" is either a baseline system value when no reading is available or an imputation for broken meters, so you may need to treat it similarly to a generic NaN depending on what you're trying to model.
>
> Both the leakage variable (annual_billed_kwh) and the extreme imbalance are precisely the defining traps to watch out for if you intend on using this dataset for supervised learning. Let me know if you need any code written to fix these for a pipeline!

are there any values in the dataset "around" 50? And what is this 50 anyways? Is it mean or median etc??

> I wrote a quick python script to inspect the exact distribution behind that 50.0 value and the results perfectly answer both your questions!
> Are there any values "around" 50? There is absolutely nothing below 50. 50.0 is the absolute mathematical floor. There are a few fractional values slightly above it (like 52.5, 53.7, and 54.0), but exactly 50.0 appears 31 times out of nowhere.
> What is it? Is it a mean or median? It is definitely not a statistical average. The actual mean of electricity consumption in the dataset is 300.12 and the median is 300.70.
> Because 50.0 is a solid mathematical floor entirely disconnected from the mean/median, this points to it being a hardcoded billing threshold. In utilities, this is typically called a "Minimum Fixed Charge" (e.g., if a house consumes only 12 kWh, they get billed a minimum floor of 50 kWh), or it's a default "null" value inserted when a smart meter fails to transmit data for the month.
> I updated the artifact section with those exact details! If you feed those exact 50s into a neural network expecting continuous variable consumption trends, you'll be feeding it a false plateau. You might want to consider replacing the 50.0s with NaN and imputing them using the historic median usage of that specific house instead!

what will be the problems if i just use 50 as is, without imputing over it?

> If you choose to leave the 50.0 values exactly as they are without imputing them, you are introducing what we call "Artificial Variance" or "Spurious Correlations" into your model.
> 
> Depending on the algorithm you use (especially for Artificial Neural Networks), here are the specific problems you will run into:
> 
> Learning False Behavioral Patterns: Let's say a customer normally uses 350 kWh a month. One month their meter breaks, and the system inserts a default 50.0. If you feed this to a Neural Network, it doesn't know the meter broke—it literally believes the customer went on a massive vacation and shut down their entire house, only to mysteriously surge back to 350 kWh the next month. The model will adjust its weights to learn this "crash" as a real human behavior.
> 
> Spurious Correlations: If, completely by chance, houses with broken meters (the 50s) happen to be slightly more likely or less likely to steal electricity, the model will just lock onto the 50 as a primary indicator. It will learn: "Ah! Whenever I see the number 50 exactly, I predict fraud." You will have trained a model to detect broken hardware, not thieves.
> 
> Skewing Gradient Descent: Algorithms sensitive to magnitude and scale (like ANNs, KNNs, and SVMs) will be heavily skewed by sudden, massive numerical drops to an artificial floor. It creates massive, jagged gradients that confuse the optimizer trying to find a smooth pattern for normal consumption.
> 
> The Verdict: Decision Trees or Random Forests are somewhat immune to this because they can just isolate 50 into a separate branch, but if you are building an ANN (Artificial Neural Network), leaving these artificial plateaus in the data will inject highly misleading noise into your training process!

what will be the optimal ML models for binary classification where we are essentially, "finding a needle in a haystack"?

> Because of the extreme 1% vs 99% class imbalance and the nature of tabular (spreadsheet) data, standard algorithms like regular Logistic Regression or standard Neural Networks will struggle right out of the box.
> 
> Here are the optimal ML models for this specific dataset, categorized by approach:
> 1. Tree-Based Ensembles (The Best Performers)
> XGBoost / LightGBM
> Random Forest
> 
> Why they are optimal: These are the undisputed kings of tabular data classification. They don't care if you have unscaled data, they are completely immune to the 50.0 artificial plateaus (they'll just carve it out as a rule rather than getting mathematically skewed), and they easily handle heavy imbalance via internal parameters (like setting scale_pos_weight in XGBoost or using class_weight='balanced' in Random Forest).
> 
> 1. Anomaly Detection Models (The Clever Approach)
> Isolation Forest
> One-Class ocsvm
> 
> Why they are optimal: Instead of treating this as a "Class A vs Class B" problem, you treat it as finding needles in a haystack. You train these models exclusively on the 99% normal non-fraud cases so it learns exactly what a "normal" electricity bill looks like. Then, when you feed it a fraud case, it flags it as a severe statistical anomaly. This perfectly bypasses the problem of only having 28 theft examples to train on.
> 
> 3. Artificial Neural Networks (The Coursework Approach)
> Autoencoders (A specific type of Neural Network)
> 
> Why they are optimal: Given your folder is named ANN MSE2, you might be required to use an Artificial Neural Network! A standard MLP (Multi-Layer Perceptron) will likely fail here without heavily oversampling the fraud cases using SMOTE. However! You can build an Autoencoder. Similar to the Isolation Forest, you train the Autoencoder network only on normal houses to reconstruct their month-to-month usage matrix. When you pass a thief's usage through it, the network won't know how to reconstruct it, the "Reconstruction Error" will spike, and you flag that spike as fraud.
> 
> Final Recommendation: If you are required to use ANNs, build an Autoencoder or use SMOTE + an MLP. If you just want the absolute highest F1-Score quickly, use XGBoost.

what is SMOTE?

> What is SMOTE?
> 
> SMOTE stands for Synthetic Minority Over-sampling Technique. When you have an extreme imbalance (e.g., 2972 normal vs. 28 fraud), models tend to completely ignore the 28 frauds because it's mathematically easier to just guess "normal" 100% of the time.
> 
> Normally, to fix this, people use "oversampling"—which just takes the 28 fraud cases and copy-pastes them 100 times to balance the scales. The problem is this causes the model to horribly overfit to those exact 28 cases.
> 
> How SMOTE fixes it: Instead of blindly copying, SMOTE creates brand new, synthetic fraud data. It takes a real fraud case, looks at another real fraud case nearby in the data space, and draws a line between them. It then randomly generates "fake" but hyper-realistic fraud cases along that line. The model gets a perfectly balanced dataset with plenty of varied, unique fraud examples to learn from!
  
Why is the specificity so high? Do i need to subtract the sepecificity from 1 because the class labels are opposite?

> I appreciate the sharp eye, but I don't think we actually need to do that — the current formula is correct. Let me explain why:
> 
> In our dataset:
> - Class 0 = Normal (the "negative" class)
> - Class 1 = Fraud (the "positive" class)
> 
> Specificity is defined as: TN / (TN + FP) — the fraction of actual Normal houses that we correctly left unflagged.
> 
> In print_specificity, we explicitly pass labels=[0, 1] to confusion_matrix, which forces it to treat 0 as the first row/column and 1 as the second. So when we unpack tn, fp, fn, tp = cm.ravel(), it correctly pulls:
> TN = Normal correctly predicted as Normal ✅
> FP = Normal incorrectly predicted as Fraud ❌
> FN = Fraud incorrectly predicted as Normal ❌
> TP = Fraud correctly predicted as Fraud ✅
> 
> The conversion we do on the anomaly model outputs (np.where(y_pred == -1, 1, 0)) maps -1 → 1 (Fraud) and 1 → 0 (Normal), which keeps the labels aligned with y_test before we compute the matrix.
> 
> If we subtracted from 1, we'd actually be computing the False Positive Rate (the fraction of normal houses wrongly flagged as frauds), which is basically the opposite of what we want!
> 
> Let me also quickly check the output from the previous run:
> 
> Random Forest Specificity:    1.0000  → correctly left 100% of normal houses unflagged ✅
> 
> Isolation Forest Specificity: 0.9933  → correctly left 99.3% of normal houses unflagged ✅
> 
> One-Class SVM Specificity:    0.9394  → correctly left 93.9% of normal houses unflagged ✅
> 
> These numbers make intuitive sense — the more aggressive the anomaly detector, the more innocent houses it falsely flags, and the lower the specificity drops. So the values are correct as-is!

Why did we not use standard scaler in isolation forest and random forest?

> Great question, and it's an important distinction to understand!
> 
> Why Random Forest doesn't need scaling
> 
> Random Forest is tree-based. Every decision it makes is a simple threshold split like: "Is month3_kwh 280?" It only cares about the relative order of values, not their actual magnitude. Whether your data is in kWh, Joules, or any other scale — the threshold comparisons would just shift accordingly, and the tree produces identical results. Scaling changes absolute values but not order, so it has zero effect on any tree-based model.
>   
> Why Isolation Forest doesn't need scaling either
> 
> Isolation Forest is also internally tree-based (it builds random "isolation trees"). It works by counting how many random cuts are needed to isolate a point, and those cuts are based on random threshold splits — exactly the same logic as Random Forest. The number of cuts required to isolate a point doesn't change regardless of what scale your features are on.
> 
> Why One-Class SVM does need scaling
> 
> One-Class SVM with an rbf (Radial Basis Function) kernel works by computing Euclidean distances between data points in a projected feature space. The formula is:
> 
> K(x, y) = exp(-γ * ||x - y||²)
> 
> The term ||x - y||² is the squared Euclidean distance. If month1_kwh ranges from 50–600 and you had another feature in the range 0–1, the distance calculation would be almost entirely dominated by the large-scale feature — the small-scale feature would be practically invisible to the model. StandardScaler normalises everything to mean=0, std=1, so every feature contributes equally to the distance calculation.
> 
> Simple rule of thumb: Anything that computes distances (SVM, KNN, PCA) → must scale. Anything tree-based (Random Forest, Isolation Forest, XGBoost) → no need to scale.

What is gamma in ocsvm? And how is ocsvm different from normal svm?

> Great questions! Let me break both down.
> 
> What is gamma in One-Class SVM?
> gamma is a parameter of the RBF (Radial Basis Function) kernel — it controls how far the "influence" of a single training point reaches.
> 
> The RBF kernel formula is:
> K(x, y) = exp(-γ * ||x - y||²)
> 
> Think of it this way: each training point emits a "bubble" of influence. gamma controls how large that bubble is.
> 
> High gamma: Each point's bubble is tiny. The model becomes very tightly shaped around each training point → the decision boundary is jagged and overfits to exact training samples
> 
> Low gamma: Each point's bubble is huge and overlaps everything → the decision boundary is smooth but too loose, flagging almost nothing as an outlier
> 
> With gamma='scale' (which we used), sklearn automatically sets gamma = 1 / (n_features * X.var()), which self-adjusts based on your data's spread — a sensible default.

How is One-Class SVM different from a normal SVM?

> Normal SVM  One-Class SVM
> 
> Training data   Two labelled classes (e.g., fraud vs normal)    Only one class (just the normal cases)
> 
> Goal    Find a hyperplane that separates Class A from Class B   Find the tightest possible boundary that contains the learned class
> 
> At test time    Classifies as A or B    Classifies as inside the boundary (normal) or outside (anomaly)
> 
> Labels needed   Yes — both classes need labels  No — you never show it what fraud looks like
> 
> Normal SVM draws a line between two groups it has seen during training.
> 
> One-Class SVM is more like drawing a fence around the "normal" territory. Anything that falls outside the fence when you're testing gets flagged as an anomaly. It never needed to be shown a single fraudulent example to do this — which is exactly why it's useful for fraud detection where labeled fraud cases are extremely rare.
> 
> The nu parameter (0.01 in our case) is One-Class SVM's equivalent of a tuning knob for this fence — it sets an upper bound on the fraction of training points it's allowed to leave outside the fence. So nu=0.01 tells it: "at most 1% of my training (normal) data can be mislabelled as outliers."