Links: [[00 Probability]]
___
# Binomial Distribution for Repeated Trials
Bernoulli's Trials #removed 

If experiment is repeated $n$ times and occurrence of an event (success) has probability $p$ and not occurrence of it has probability $q$

Here, $p + q = 1$

$(p+q)^{n} = {}^{n}C_{0}\ q^{n}p^{0} + {}^{n}C_{1}\  q^{n-1} p^{1} + {}^{n}C_{2}\ q^{n-2}p^{2} + {}^{n}C_{3}\ q^{n-3}p^{3} + \dots {}^{n}C_{n}\ q^{0} p^{n}$
$p^{0}$ means 0 times success, and so on.

Probability of Occurrence of Exactly $r$ time success,
$$P = {}^{n}C_{r}\ q^{n-r}p^{r}$$

Probability of Occurrence of at most $r$ times success,
$$P = \sum _{t=0}^{r} {}^{n}C_{t}\ q^{n-t}p^{t}$$

Probability of Occurrence of at least $r$ times success,
$$P = \sum _{t=r}^{n} {}^{n}C_{t}\ q^{n-t}p^{t}$$

Mean,
$$\bar{x} = nP$$

Variance,
$$\sigma^{2} = npq$$

Standard Deviation,
$$\sigma = \sqrt{ npq }$$
