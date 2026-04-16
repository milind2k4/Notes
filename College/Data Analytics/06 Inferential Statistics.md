Links: [[00 Data Analytics]]
___
# Inferential Statistics

**Inferential Statistics** allows Data Analysts to make predictions ("inferences") from data. Instead of using merely descriptive, factual summary stats, inferential statistics takes data from a **Sample** and makes conclusions about the larger **Population** from which that sample was drawn.

- **Population:** Every single individual or event that exists in a specific group (e.g., Every person in India). Finding the true population mean ($\mu$) is usually impossible.
- **Sample:** A smaller, meticulously chosen, representative fraction of the Population (e.g., 10,000 citizens from various states).

Because working with Samples inherently involves uncertainty (we are *guessing* about the Population), we must use Probability to quantify exactly how confident we are in our conclusions.

## Confidence Interval
A **Confidence Interval (CI)** is a range of values, derived from sample statistics, that is likely to contain the unknown population parameter.

Because we cannot be 100% certain that our sample perfectly matches the population, we instead create a bracket: "I am 95% confident that the true population mean lies between X and Y."

$$CI = \bar{X} \pm Z_{\alpha/2} \left(\frac{s}{\sqrt{n}}\right)$$

Where:
-   $\bar{X}$: Sample Mean.
-   $Z_{\alpha/2}$: The Critical Value (Z-Score) corresponding to the desired confidence level (often $1.96$ for $95\%$).
-   $s$: Sample standard deviation.
-   $n$: Sample size.
-   $\left(\frac{s}{\sqrt{n}}\right)$: The Standard Error of the Mean.

```python
import numpy as np
import scipy.stats as stats

# Sample data: Test scores of 50 students
np.random.seed(42)
sample_scores = np.random.normal(loc=75, scale=10, size=50)

# Calculate Confidence Interval (95%)
ci = stats.norm.interval(confidence=0.95, 
	loc=np.mean(sample_scores),
	scale=stats.sem(sample_scores)
)

print(f"95% Confidence Interval: {ci}")
```

## Significance Level ($\alpha$)
The **Significance Level**, denoted by alpha ($\alpha$), is the probability of rejecting the Null Hypothesis when it is actually true. It represents the "threshold of acceptable error" or the risk we are willing to take.

- If Confidence Level = 95% (0.95), then $\alpha = 1 - 0.95 = 0.05$ (or 5%).
- A 5% $\alpha$ means there is a 5% chance that we conclude a difference exists when there actually is none.

### Types of Errors
1.  **Type I Error (False Positive):** Rejecting the Null hypothesis when it is, in fact, True. (Telling a healthy patient they are sick. The probability of this is exactly $\alpha$).
2.  **Type II Error (False Negative):** Failing to reject the Null hypothesis when it is actually False. (Telling a sick patient they are healthy. Denoted by $\beta$).

## Hypothesis Testing (Significance Testing)
A formal procedure used to statistically determine if an observation is the result of a real, systemic effect or merely random chance variability.

### Structure the Hypotheses
Every test starts with two opposing statements:

- **Null Hypothesis ($H_0$):** The default assumption. It states there is **no difference/no effect/status quo**. (e.g., "The new website design has no effect on user retention.")
- **Alternative Hypothesis ($H_A$ or $H_1$):** What you are trying to mathematically prove. (e.g., "The new website design increases user retention.")

### Choose the Test
- **T-test:** Used when comparing the means of two groups, typically when the sample size is small ($n < 30$) or the population standard deviation is unknown.
- **Z-test:** Used when the sample size is large ($n \ge 30$) and the standard deviation is known.
- **ANOVA:** Used when comparing the means of three or more groups.

### Analyze the P-value
The **P-value** is the actual probability computed by your test. It calculates: "Assuming the Null Hypothesis is true, what is the probability of getting this specific data simply by random chance?"

**The Rule:** If $P < \alpha$, we reject the Null Hypothesis.

- If $P = 0.01$ and $\alpha = 0.05$: "There is only a 1% probability this happened by chance. Because 1% is less than my 5% risk threshold, I declare the result is **Statistically Significant**." ($H_0$ is rejected).
- If $P = 0.20$ and $\alpha = 0.05$: "There is a 20% probability this happened by chance. I cannot confidently claim the new design worked." (Fail to reject $H_0$).

```python
# T-Test Example
# Comparing customer spending on Old Website vs New Website
old_website = [25, 30, 28, 35, 29, 32, 26, 31, 28, 27]
new_website = [35, 42, 38, 45, 39, 41, 36, 40, 37, 39]

# Perform Independent 2-Sample T-Test
t_stat, p_value = stats.ttest_ind(old_website, new_website)

alpha = 0.05
print(f"P-Value: {p_value}")

if p_value < alpha:
    print("Reject Null Hypothesis (Significant Difference)")
else:
    print("Fail to Reject Null Hypothesis (No Significant Difference)")
```

## Bayesian Inference (Bayes' Theorem)
While traditional (Frequentist) statistics like Hypothesis Testing rely solely on current sample data, **Bayesian Statistics** allows us to update our existing beliefs based on *new* evidence.

Bayes' Theorem calculates the probability of an event based on prior knowledge of conditions related to the event.

**The Formula:**
$$P(A|B) = \frac{P(B|A)P(A)}{P(B)}$$

Where:
- **$P(A|B)$ (Posterior):** The probability of hypothesis $A$ being true *given* the new evidence $B$. (What we want to find out).
- **$P(B|A)$ (Likelihood):** The probability of seeing the evidence $B$ *if* the hypothesis $A$ is true.
- **$P(A)$ (Prior):** Our initial belief in hypothesis $A$ *before* seeing the evidence.
- **$P(B)$ (Marginal):** The total probability of seeing the evidence $B$ under all circumstances.

> [!EXAMPLE] Medical Testing for a Rare Disease
> A disease affects 1% of the population ($P(Disease) = 0.01$).
> A test correctly identifies the disease 99% of the time ($P(Positive|Disease) = 0.99$).
> The test has a 5% false positive rate for healthy people ($P(Positive|Healthy) = 0.05$).
> 
> You test **Positive**. What is the actual probability you *have* the disease ($P(Disease|Positive)$)?
> 
> Using Bayes' Theorem, it's not 99%. Because the disease is so rare, the sheer volume of false positives from the healthy 99% drastically shifts the math. The formula reveals you only have roughly a **16% chance** of actually having the disease!
