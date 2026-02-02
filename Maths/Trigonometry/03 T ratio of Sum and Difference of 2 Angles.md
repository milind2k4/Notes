Links: [[00 Trigonometry]]
___
# T ratio of Sum and Difference of 2 Angles
#formula 

### Collectively, to remember
> $$\begin{split}
> \sin (A \pm B) &= \sin A \cos B \pm \cos A \sin B \\\\
> \cos (A \pm B) &= \cos A \cos B \mp \sin A \sin B \\\\
> \tan (A \pm B) &= \frac{\tan A \pm \tan B}{1 \mp \tan A \tan B} \\\\
> \end{split}$$


## Proofs
1. $$\sin (A + B) = \sin A \cos B + \cos A \sin B$$

	> **Proof:** [See this](https://youtu.be/Gsw56fzQdDg?list=PL_A4M5IAkMafhPkzpa16mbUDqD8d7bBhL&t=222)
	> 
	> ![[sin A + B derivation.png|400]]
	> $$\begin{split}
	> \text{In } \triangle OPT, & \\
	> \sin (A + B) &= \frac{PT}{OP} \\
	> &= \frac{PR + RT}{OP} \\
	> &= \frac{PR}{OP} + \frac{QU}{OP}\ (\because RT = QU)\\
	> &= \frac{PR}{PQ} \cdot \frac{PQ}{OP} + \frac{QU}{OQ} \cdot \frac{OQ}{OP}\\
	> &= \cos A \cdot \sin B + \sin A \cdot \cos B \\
	> & \text{Henc Prooved}
	> \end{split}$$

$\\$

2. $$\sin (A - B) = \sin A \cos B - \cos A \sin B$$
$\\$

3. $$\cos (A + B) = \cos A \cos B - \sin A \sin B$$
   
	> Proof: Put $A = \displaystyle \frac{\pi}{2} + A$ in 1.
	> Then,
	> $$\begin{split}
	> \sin\left( \frac{\pi}{2} + A + B \right) &= \sin \left(\frac{\pi}{2} + A\right) \cos B + \sin B \cos \left(\frac{\pi}{2} + A\right) \\\\
	> \cos (A + B) &= \cos A \cos B + \sin B (-\sin A)
	> \end{split}
	> $$

$\\$

4. $$\cos (A - B) = \cos A \cos B + \sin A \sin B$$
$\\$

5. $$\tan (A + B) = \frac{\tan A +\tan B}{1 - \tan A \tan B}$$
   
	> Proof:
	> $$\begin{split}
	> \tan (A+B) &= \frac{\sin (A+B)}{\cos (A+B)} \\\\
	> &= \frac{\sin A \cos B + \cos A \sin B}{\cos A \cos B -\sin A \sin B} \\\\
	> \text{Dividing both by } & \cos A \cos B, \\\\
	> &= \frac{\tan A +\tan B}{1 - \tan A \tan B}
	> \end{split}$$

$\\$

6. $$\tan (A - B) = \frac{\tan A - \tan B}{1 + \tan A \tan B}$$
$\\$

7. $$\cot (A + B) = \frac{\cot A \cot B - 1}{\cot B + \cot A}$$

	> Proof: 
	> $$\begin{split}
	> \cot (A + B) &= \frac{1}{\tan (A+B)} \\\\
	> &= \frac{1 - \tan A \tan B}{\tan A + \tan B} \\\\
	> \text{Dividing by } & \tan A \tan B, \\\\
	> &= \frac{\cot A \cot B - 1}{\cot B + \cot A}
	> \end{split}$$

$\\$

8. $$\cot (A - B) = \frac{\cot A \cot B + 1}{\cot B - \cot A}$$

## Extra results to remember
1. $$\tan A \pm \tan B = \frac{\sin (A \pm B)}{\cos A \cos B}$$

2. $$\cot A \pm \cot B = \frac{ \sin(B \pm A) }{ \sin A \sin B }$$

3. $$\tan(A+B)\tan A \tan B = \tan(A+B) - \tan A - \tan B$$
   sum . 1st . 2nd = sum - 1st - 2nd
   
   If A+B is a multiple of $\pi / 4$,
	$$
	\begin{split}
	\tan A \tan B &= 1 - \tan A - \tan B \\
	(1 + \tan A)(1 + \tan B) &= 2
	\end{split}
	$$

4. $$\sin (A+B) \cdot \sin (A - B) = \sin ^{2}A - \sin ^{2}B$$
   $$\phantom{\sin (A+B) \cdot \sin (A - B)} = \cos ^{2}B - \cos ^{2}A$$

2. $$\cos (A+B) \cdot \cos (A-B) = \cos ^{2}A - \sin ^{2}B$$
      $$\phantom{\cos (A+B) \cdot \cos (A-B)} = \cos ^{2}B - \sin ^{2}A$$

4. $$\tan (45^{\circ} \pm A) = \frac{1 \pm \tan A}{1 \mp \tan A}$$

## Tangent of sum of many angles

$$\tan (A + B + C + D + ....) = \frac{S_{1} - S_{3} + S_{5} - S_{7} + ...}{1 - S_{2} + S_{4} - S_{6} + ...}$$

where,
$S_{1}$ = sum of tan of angles taken one at a time,
i.e. $\tan A + \tan B + \tan C + ...$

$S_{2}$ = sum of product of angles taken 2 at a time,
i.e. $\tan A \tan B + \tan A \tan C + \tan A \tan D + ...$

$S_{2}$ = sum of product of angles taken 3 at a time,
i.e. $\tan A \tan B \tan C + \tan A \tan B \tan D + \tan A \tan B \tan E + ...$
.
.
.
.

For 3 angles, 
$$\begin{split}\tan (A + B + C) &= \frac{S_{1} - S_{3}}{1 - S_{2}} \\\\
&= \frac{\sum \tan A  - \prod \tan A }{1 - \sum \tan A \tan B} \\\\
&= \frac{(\tan A + \tan B + \tan C) - \tan A \tan B \tan C}{1 - \tan A \tan B - \tan B \tan C - \tan C \tan A}
\end{split}$$

Using this we can find $\sin (A + B + C)$ and $\cos (A + B + C)$
$$\begin{split}
\sin (A + B + C) &=  \left( \sum \tan A  - \prod \tan A \right) \left( \prod \cos A \right) \\\\
&= \sum \sin A \cos B \cos C - \prod \sin A \\\\
&= \sin A \cos B \cos C + \cos A \sin B \cos C + \cos A \cos B \sin C \\
&\ \ \ \ \  - \sin A \sin B \sin C 
\end{split}$$

$\\$

$$\begin{split}
\cos (A + B + C) &=  \left( 1 - \sum \tan A \tan B \right) \left( \prod \cos A \right) \\\\
&= \prod \cos A - \sum \cos A \sin B \sin C \\\\
&= \cos A \cos B \cos C - \cos A \sin B \sin C - \sin A \cos B \cos C \\
&\ \ \ \ \  - \sin A \sin B \sin C 
\end{split}$$



