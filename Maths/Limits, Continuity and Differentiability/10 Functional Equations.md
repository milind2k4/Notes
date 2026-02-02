Links: [[09 Differentiability]]
___
# Functional Equations
In functional equations, we can discard options but cannot select them. If we assume a function, we will have to be careful to only discard options and not select them. This is because there could be many functions and we have assumed one of them.

We should verify if there is an option like "there is no such function." Verification means that finally there should be 0 = 0 and nothing else.

If $f(x)$ is differentiable function then, 


| Functional Rule                                                                              | Function                       |
| -------------------------------------------------------------------------------------------- | ------------------------------ |
| $$f(x+y) = f(x) + f(y),\ \forall\ x,y \in R$$                                                | $$f(x) = kx$$                  |
| $$f\left( \frac{ x+y }{ n } \right) = \frac{ f(x) + f(y) }{ n }$$                            | $$f(x)= kx$$                   |
| $$f(xy) = f(x) + f(y),\ \forall\ x,y \in R$$                                                 | $$f(x) = 0$$                   |
| $$f(xy) = f(x) + f(y),\ \forall\ x,y \in R - \{ 0 \}$$                                       | $$f(x) = k \ln \| x \| $$      |
| $$f(xy) = f(x) + f(y),\ \forall\ x,y \in R^{+}$$                                             | $$f(x) = k \ln x$$             |
| $$f\left( \frac{x}{y} \right) = f(x) - f(y),\ \forall\ x,y \in R^{+}$$                       | $$f(x) = k\ln x$$              |
| $$f(x+y) = f(x). f(y),\ \forall\ x,y \in R$$                                                 | $$f(x) = a^{x}\ or\ 0$$        |
| $$f(x.y) = f(x).f(y),\ \forall\ x,y \in R$$                                                  | $$f(x) = 0 \ or\ \|x\|^{k}$$   |
| $$f(x) + f\left( \frac{ 1 }{ x } \right) = f(x).f\left( \frac{ 1 }{ x } \right),\ x \neq 0$$ | $$f(x) = 1 \pm x^{n}, n\in N$$ |

### Finding Functions Using Differentiability 
The question needs to say that the function is differentiable. Otherwise we cannot do this. 

If it does not say differentiable and we still find a function using differentiable, which satisfies all the conditions in the question, we can reject options using it. 

#### Using First Principle 
1. Write $f'(x)$ using first principle.
2. Convert RHS using given functional rule,
   
   $$f'(x) = f'(a). g(x,f(x))$$
	This will give a [[00 Differential Equation|differential equation]] in x and f(x) solving which will give f(x)

We will write,
$$f'(a) = \lim_{ h \to 0 } \frac{ f(a + h) - f(a) }{ h }$$
Now if we have,
$$\lim_{ h \to 0 } \frac{ f(\text{some variable in h})(\to k) - c }{ h }$$
then it may be $f'(k)$ provided $f(k) = c$.

![[Pasted image 20230813163227.png]]
![[Pasted image 20230813163559.png]]

#### Using Differentiation 
1. Differentiate the given equation wrt x (partial differentiation)
2. Put x = something to get differential equation in y and $f'(y)$. 
   Alternatively, differentiate given functional rule wrt y and eliminate $f'$ of joint expression from this and step 1. 
   
   Now put y = something to get differential equation.

![[Pasted image 20230813165641.png]]
![[Pasted image 20230813170640.png]]


### Examples
#### Having Single Variable
We try to interchange the terms.

![[Pasted image 20230812131502.png]]
![[Pasted image 20230812131754.png]]

![[Pasted image 20230812133404.png]]
![[Pasted image 20230812133736.png]]


#### Having Multiple Variables
and terms without $f$ are also present. 

Try to substitute (putting x or y as constant or some expression) such that one argument of f has variable and other argument is constant. 

In these questions, verification is important. Below, since 0 = 0 did not come, there is no function which satisfies the given condition.
![[Pasted image 20230812132510.png]]

In some questions, we just put one of the variables as 0,
![[Pasted image 20230812133351.png]]

![[Pasted image 20230812134244.png]]
![[Pasted image 20230812134300.png]]

![[Pasted image 20230813171158.png]]

We can save time by trying to make the functional rule into one of the ones we already know,
![[Pasted image 20230813173848.png]]

![[Pasted image 20230813174527.png]]
