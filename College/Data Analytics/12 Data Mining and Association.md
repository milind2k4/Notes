Links: [[00 Data Analytics]]
___
# Data Mining and Association

**Data Mining** is the computational process of extracting useful, non-trivial, and previously entirely unknown patterns from massive datasets. Instead of testing a specific hypothesis, data mining blindly scours the data focusing on identifying hidden relationships, subtle correlations, and deep structures that are not immediately visible to human analysts.

## Association Rule Mining
A heavily utilized data mining technique—often referred to as **Market Basket Analysis**—that discovers interesting relations between variables in large databases. It is intended to identify strong rules discovered in databases using different measures of interestingness.

> [!EXAMPLE] Market Basket Analysis
> If a customer buys bread and butter, what is the mathematical probability they will also buy milk? By finding these hidden associations, supermarkets can optimize store layouts (putting milk near the bread) or websites can optimize recommendations ("Customers who bought this also bought...").

### Key Measures
To determine if a discovered rule is actually "interesting" and statistically significant, the algorithm relies on core mathematical measures:

#### Support
Support calculates how frequently a specific item (or itemset) appears in the entire dataset. It prevents the algorithm from creating rules based on incredibly rare, fluke occurrences.
$$Support(A) = \frac{\text{Transactions containing A}}{\text{Total number of transactions}}$$

#### Confidence
Confidence calculates the likelihood that an item $B$ is also bought if item $A$ is bought. It measures the absolute reliability of the inference made by the rule.
$$Confidence(A \to B) = \frac{\text{Transactions containing both A and B}}{\text{Transactions containing A}}$$

## The Apriori Algorithm
The **Apriori Algorithm** is the classic, foundational algorithm used to actively mine these frequent itemsets and generate association rules over relational databases.

### How it Works
It operates on a foundational principle: **If an itemset is frequent, then all of its subsets must also be frequent.**
Conversely, if an itemset is deemed infrequent, the algorithm instantly knows that all of its supersets will also be infrequent, allowing it to aggressively prune the search space and save massive amounts of computational power.

- **Iteration 1:** Calculate the Support for all individual items. Discard any items that fall below the minimum support threshold.
- **Iteration 2:** Combine the surviving items into pairs (itemsets of 2). Calculate their Support. Discard the infrequent pairs.
- **Iteration 3:** Combine surviving pairs into triplets. 
- **Completion:** Repeat until no more frequent itemsets can be formed. Finally, calculate the Confidence for the surviving sets to generate the final Association Rules.

####  Example: The Apriori Algorithm
Imagine a small grocery store dataset with **5 total transactions**. We want to find strong association rules.
- **Minimum Support Threshold:** 2 transactions ($2/5 = 40\%$)
- **Minimum Confidence Threshold:** $60\%$

**The Raw Database:**
- **T1:** Apple, Banana, Cherry
- **T2:** Apple, Banana
- **T3:** Apple, Cherry
- **T4:** Apple, Dates
- **T5:** Banana, Eggs

**Step 1: Iteration 1 (Individual Items)**
We scan the database to find the raw frequency count of every single item:
- **Apple:** 4
- **Banana:** 3
- **Cherry:** 2
- **Dates:** 1
- **Eggs:** 1

*Pruning:* The minimum support is 2. Therefore, we immediately permanently discard **Dates** and **Eggs**.

**Step 2: Iteration 2 (Pairs)**
We take the surviving items (`Apple`, `Banana`, `Cherry`) and create all possible 2-item combinations. We scan the database again to count how many times these specific pairs were bought together:
- **{Apple, Banana}:** Found in T1, T2 (Count: 2)
- **{Apple, Cherry}:** Found in T1, T3 (Count: 2)
- **{Banana, Cherry}:** Found in T1 only (Count: 1)

*Pruning:* The pair `{Banana, Cherry}` only has a count of 1, so it is permanently discarded.

**Step 3: Iteration 3 (Triplets) & The Apriori Principle**
Now we try to make 3-item combinations from our surviving pairs (`{Apple, Banana}` and `{Apple, Cherry}`). The only mathematically possible triplet is `{Apple, Banana, Cherry}`.

*The Apriori Shortcut:* Do we need to scan the database to count this? **No.** The mathematical principle of Apriori states that if a subset is infrequent, the superset is guaranteed to be infrequent. Because we already proved that `{Banana, Cherry}` is infrequent, the triplet `{Apple, Banana, Cherry}` is instantly pruned without ever scanning the database!

We have no more combinations to make. The algorithm stops. Our final "Frequent Itemsets" are **{Apple, Banana}** and **{Apple, Cherry}**.

**Step 4: Generate Rules & Calculate Confidence**
Now we extract the final rules from our surviving pairs and calculate their Confidence using the formula: $\frac{\text{Count of Both}}{\text{Count of the "If" item}}$. We will compare this against our $60\%$ Minimum Confidence.

**From {Apple, Banana}:**
1. **Rule:** If Apple $\to$ then Banana
   - *Confidence:* $$\frac{Count(Apple + Banana)}{Count(Apple)} = \frac{2}{4} = \mathbf{50\%}$$
   - *Result:* $50\% < 60\%$. **Discard.**
2. **Rule:** If Banana $\to$ then Apple
   - *Confidence:* $$\frac{Count(Apple + Banana)}{Count(Banana)} = \frac{2}{3} = \mathbf{66.6\%}$$
   - *Result:* $66.6\% \ge 60\%$. **Keep.**

**From {Apple, Cherry}:**
3. **Rule:** If Apple $\to$ then Cherry
   - *Confidence:* $$\frac{Count(Apple + Cherry)}{Count(Apple)} = \frac{2}{4} = \mathbf{50\%}$$
   - *Result:* $50\% < 60\%$. **Discard.**
4. **Rule:** If Cherry $\to$ then Apple
   - *Confidence:* $$\frac{Count(Apple + Cherry)}{Count(Cherry)} = \frac{2}{2} = \mathbf{100\%}$$
   - *Result:* $100\% \ge 60\%$. **Keep.**

> [!NOTE] The Final Result
> The Data Mining algorithm successfully outputs two highly reliable rules for the store manager:
> 1. Customers who buy **Bananas** are highly likely ($66\%$) to also buy **Apples**.
> 2. Customers who buy **Cherries** are guaranteed ($100\%$) to also buy **Apples**.

### Advantages & Disadvantages

**Advantages:**
- **Simplicity:** The underlying mathematical logic is incredibly intuitive and extremely easy to implement from scratch.
- **Exhaustive:** Because it systematically builds combinations from the bottom up, it is guaranteed to find *all* possible rules that meet the thresholds.
- **Effective Pruning:** The Apriori principle aggressively cuts down the search space, saving significant time compared to a brute-force approach.

**Disadvantages:**
- **I/O Bottleneck:** It is computationally expensive. The algorithm must read through the *entire database* from top to bottom during every single iteration to count frequencies.
- **Memory Intensive:** If the minimum support threshold is set too low, the algorithm generates an unimaginably massive number of "Candidate Itemsets" in the early iterations, which can quickly exhaust system memory.
- **Slower than Modern Alternatives:** Newer algorithms like **FP-Growth** (Frequent Pattern Growth) completely bypass the Apriori bottleneck by storing the database in a highly compressed Tree structure, requiring only two database scans total!
