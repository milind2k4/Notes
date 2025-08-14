Links: [[03 T ratio of Sum and Difference of 2 Angles]], [[05 Sum and Difference of T ratios]], [[06 Multiples of Angles]]
___
# Conditional Identities 
#formula 

$$A+B+C = \pi$$

### Collectively to remember
In sum and prod notation,
$$\begin{split}
\sum \sin (2A) &= 4\prod \sin A \\
\\
\sum \cos (2A) &= -1 - 4\prod \cos A \\
\\
\sum \sin (A) &= 4\prod \cos \frac{A}{2} \\
\\
\sum \cos (A) &= 1 + 4\prod \sin \frac{A}{2} \\
\\
\sum \tan A &= \prod \tan A \\
\\
\sum \tan \frac{A}{2} \tan \frac{B}{2} &= 1 \\
\\
\sum \cot A \cot B &= 1 \\
\\
\sum \cot \frac{A}{2}  &= \prod \cot \frac{A}{2} \\
\\
\sum \sin A \cos B \cos C &= \prod \sin A \\
\\
\sum \sin A \sin B \cos C &= 1 + \prod \cos A
\end{split}$$

Without sum or prod notation,
$$\begin{split}
\sin (2A) + \sin (2B) + \sin (2C) &= 4\sin A \sin B \sin C \\\\
\cos (2A) + \cos (2B) + \cos (2C) &= -1 - 4\cos A \cos B \cos C \\\\
\sin (A) + \sin (B) + \sin (C) &= 4\cos  \frac{A}{2} \cos  \frac{B}{2} \cos \frac{C}{2} \\\\
\cos (A) + \cos (B) + \cos (C) &= 1 + 4\sin  \frac{A}{2} \sin \frac{B}{2} \sin \frac{C}{2} \\\\
\tan A + \tan B + \tan C &= \tan A \tan B \tan C \\\\
\tan \frac{A}{2} \tan \frac{B}{2} + \tan \frac{B}{2} \tan \frac{C}{2} + \tan \frac{C}{2} \tan \frac{A}{2} &= 1 \\\\
\cot A \cot B + \cot B \cot C + \cot C \cot A &= 1 \\\\
\cot \frac{A}{2} + \cot \frac{B}{2} + \cot \frac{C}{2} &= \cot \frac{A}{2}\cot \frac{B}{2}\cot \frac{C}{2} \\\\
\sin A \cos B \cos C + \cos A \sin B \cos C + \cos A \cos B \sin C &= \sin A \sin B \sin C \\\\
\sin A \sin B \cos C + \sin A \cos B \sin C + \cos A \sin B \sin C &= 1 + \cos A \cos B \cos C
\end{split}$$

## Proofs
1. $\sin (2A) + \sin (2B) + \sin (2C) = 4\sin A \sin B \sin C$ 
> Proof:
> $$\begin{split}
> \sin 2A + \sin 2B + \sin 2C &= 2\sin (A+B)\cos (A-B) + 2\sin C \cos C \\
> &= 2 \sin (\pi - C) \cos (A-B) + 2\sin C \cos C \\
> &= 2 \sin C (\cos(A-B) + \cos (A+B)) \\
> &= 2 \sin C (2 \sin A \sin B)\\
> &= 4 \sin A \sin B \sin C
> \end{split}$$


1. $\cos (2A) + \cos (2B) + \cos (2C) = -1 - 4\cos A \cos B \cos C$ 
Proof:
> $$\begin{split}
> \cos 2A + \cos 2B + \cos 2C &= 2\cos (A+B) \cos (A-B) + 2\cos ^{2}C - 1 \\
> &= 2 \cos (\pi - C)\cos (A-B) + 2\cos ^{2}C - 1\\
> &= -2\cos C (\cos (A-B) - \cos C) - 1 \\
> &= -1 -2\cos C [\cos (A-B) - \cos (\pi -(A+B))] \\
> &= -1 -2\cos C [\cos (A-B) + \cos (A+B)] \\
> &= -1 -2\cos C [2\cos A \cos B] \\
> &= -1 -4 \cos A \cos B \cos C
> \end{split}$$
 

3. $\displaystyle \sin (A) + \sin (B) + \sin (C) = 4\cos  \frac{A}{2} \cos  \frac{B}{2} \cos \frac{C}{2}$ 
> Proof:
> $$\begin{split}
> \sin A + \sin B + \sin C &= 2\sin \frac{A+B}{2} \cos \frac{A-B}{2} + 2\sin \frac{C}{2} \cos \frac{C}{2} \\
> &=  2 \cos \frac{C}{2} \left( \cos \frac{A-B}{2} + \sin \frac{C}{2} \right) \\
> &=  2 \cos \frac{C}{2} \left( \cos \frac{A-B}{2} + \sin (\frac{\pi}{2} - \frac{A+B}{2}) \right) \\
> &=  2 \cos \frac{C}{2} \left( \cos \frac{A-B}{2} + \cos \frac{A+B}{2} \right) \\
> &=  2 \cos \frac{C}{2} \left( 2\cos \frac{A}{2} \cos \frac{B}{2} \right) \\
> &= 4 \cos \frac{A}{2}\cos \frac{B}{2}\cos \frac{C}{2}
> \end{split}$$


5. $\displaystyle \cos (A) + \cos (B) + \cos (C) = 1 + 4\sin  \frac{A}{2} \sin \frac{B}{2} \sin \frac{C}{2}$
> Proof: 
> $$\begin{split}
> \cos A+ \cos B + \cos C &= 2 \cos \frac{A+B}{2} \cos \frac{A-B}{2} + \cos C \\
> 
> &= 2 \cos \left( \frac{\pi}{2} - \frac{C}{2} \right) \cos \left( \frac{A-B}{2} \right) + 1 - 2 \sin ^{2} \frac{C}{2} \\
> 
> &= 2 \sin \frac{C}{2} \cos \left( \frac{A-B}{2} \right) + 1 - 2\sin ^{2} \frac{C}{2}\\
> 
> &= 1 + 2 \sin \frac{C}{2} \left( \cos \frac{A-B}{2} - \sin \left( \frac{\pi}{2} - \frac{A+B}{2} \right) \right) \\
> 
> &= 1 + 2 \sin \frac{C}{2} \left( \cos \frac{A-B}{2} -\cos \frac{A+B}{2} \right) \\
> 
> &= 1 + 2\sin \frac{C}{2} \left( 2 \sin \frac{A}{2} \sin \frac{B}{2} \right) \\
> 
> &= 1 + 4 \sin \frac{A}{2}\sin \frac{B}{2}\sin \frac{C}{2}
> \end{split}$$


5. $\tan A + \tan B + \tan C = \tan A \tan B \tan C$
> Proof: From [[03 T ratio of Sum and Difference of 2 Angles#Tangent of sum of many angles]]


6. $\displaystyle \tan \frac{A}{2} \tan \frac{B}{2} + \tan \frac{B}{2} \tan \frac{C}{2} + \tan \frac{C}{2} \tan \frac{A}{2} = 1$
> Proof: From [[03 T ratio of Sum and Difference of 2 Angles#Tangent of sum of many angles]]


7. $\cot A \cot B + \cot B \cot C + \cot C \cot A = 1$
> Proof: Put $\displaystyle \tan A = \frac{1}{\cot A}$ in 5.


8. $\displaystyle \cot \frac{A}{2} + \cot \frac{B}{2} + \cot \frac{C}{2} = \cot \frac{A}{2}\cot \frac{B}{2}\cot \frac{C}{2}$ 
> Proof: Put $\displaystyle \tan \frac{A}{2} = \frac{1}{\cot \frac{A}{2}}$ in 6.


9. $\sin A \cos B \cos C + \cos A \sin B \cos C + \cos A \cos B \sin C = \sin A \sin B \sin C$
> Proof: Break and simplify in 5.


10. $\sin A \sin B \cos C + \sin A \cos B \sin C + \cos A \sin B \sin C = 1 + \cos A \cos B \cos C$
> Proof: Can be derived by putting $A+B+C = \pi$ in $\cos (A+B+C)$.














