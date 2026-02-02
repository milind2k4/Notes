Links: [[02 Elementary Graphs#Greatest Integer Function|Greatest Integer Function]], [[02 Elementary Graphs#Fractional part Function|Fractional part Function]]
___
# Properties of GIF and FPF

- $[x]$ changes definition (i.e. value) at every integral point.
- $\{ x \}$ changes definition at every integral point. 
  $\{ x \} = x - I$ where $I$ is an integer just less than x.
$\\$

#### Equalities
$[x] = I \implies x \in [I, I+1)$
$\{ x \} \in [0,1)$

$\{x\} = 0 \implies x \in I$ 
$\{x\} \neq 0 \implies x \in R-I$

#### Two Times
$[[x]] = [x]$
$\{ \{ x \} \} = \{ x \}$
$\{[x]\} = 0$
$[\{ x \}] = 0$


#### Integers
$[x + I] = [x] + I$
$\{x+I\} = \{x\}$
$[I. x] \neq I[x]$, in general
$\{ I.x \} \neq I\{ x \}$, in general

#### Addition in Argument
$[x+y] \neq [x] + [y]$
$\{ x+y \} \neq \{ x \} + \{ y \}$
$[x + y] = [[x] + \{ x \} + [y] + \{ y \}] \implies [x] + [y] +[\{ x \} + \{ y \}]$
  thus,
  $[x+y] = [x] + [y]$ if $\{ x \} + \{ y \} \in [0,1)$
  $[x+y] = [x] + [y] + 1$ if $\{ x \} + \{ y \} \in [1,2)$
$\\$

#### Addition of -ve
$[x] + [-x] = -1$, $x \notin I$
$[x] + [-x] = 0$, $x \in I$
$\{x\} + \{-x\} = 1,\ x \notin I$
$\{x\} + \{-x\} = 0,\ x \in I$

#### Inequalities
$[x] \geq I \implies x \in [I, \infty)$
$[x] > I \implies x \in [I+1, \infty)$
$[x] \leq I \implies x \in (-\infty, I+1)$
$[x] < I \implies x \in (-\infty, I)$


#### Adding Reciprocals of Natural Numbers
$$[x] + \left[ x + \frac{1}{n} \right] + \left[ x + \frac{2}{n} \right] + \left[ x+ \frac{3}{n} \right] + \dots \left[ x + \frac{ n-1 }{ n } \right] = [n \cdot x]$$
where n is a natural number

For example,
$$[x] + \left[ x + \frac{1}{2} \right] = [2x]$$
$$[x] + \left[ x + \frac{1}{3} \right] + \left[ x + \frac{2}{3} \right] = [3x]$$

