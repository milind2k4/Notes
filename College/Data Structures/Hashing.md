Links: 
___
# Hashing

A hash function is a function that takes a value as input and gives out a (preferably) unique index to store the value at. 

For example if we want to store "Alice", we pass it though a hash function. It gives out a value, say 4, then we store "Alice" in an array at index 4. 

#### Types of Hashing 

- **Direct:** h(x) = x. So the value x is stored at location x.
- **Subtraction:** h(x) = k - m.
- **Division:** h(x) = k % m 
- **Folding Method:**
  If location range = 00 - 99
  And k = 67394
  Then we do 67 + 39 + 40 or 67 + 39 + 04
  And if the result exceeds 99, we mod by 100. 
- **Fold Boundary Method:** 
  Instead of making pairs from one side, we star making pairs from both sides. 
- **Digit Extraction method:**
  where if k_134 and key is given as k = 124203957 then we take out the first, 3rd and the 4th digits and sum them and then if the sum is outside the range then we take mod. 
- **Mid square method:** We square the key and then take out the middle digit. 

Where k = key.


Load Factor($\alpha$): Tells how full a hash table is.
$$\alpha = \frac{n}{m} = \ce{ \frac{ no of ele }{ no of slots } }$$