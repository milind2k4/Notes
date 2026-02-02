Links: [[06 Coordinates of Centres and Area of Triangle]]
___
# Notation and Results in a Triangle
### Standard Notation
[[00 Solutions of Triangles#05 Notations and Results in a Triangle General Notation]]

For vertex and angle the point is used, A, B, C. 

To denote side lengths we use small letters opposite to the vertex. 

![[Pasted image 20230705090800.png]]

$s$ is semi perimeter, 
$$s = \frac{ a + b + c }{ 2 }$$

For Area of triangle ABC, we use $\Delta, S\ or\ [ABC]$, which is,
$$\Delta  = \sqrt{ s(s-a)(s-b)(s-c) }$$
##### Centroid (G)
G is used for **Centroid** which is point of concurrency of medians.

$$\frac{ AG }{ GM_{1} } = \frac{ 2 }{ 1 }$$

![[Pasted image 20230705091119.png]]

##### Orthocentre (H)
H is used for **Orthocentre** which is point of concurrency of altitudes. 
![[Pasted image 20230705091219.png]]

##### Incentre (I)
I is used for **Incentre** which is point of concurrency of angular bisectors. It is also the centre of the circle inscribed in the triangle.
The radius of this incircle is called **Inradius** and is denoted by $r$.

![[Pasted image 20230705091407.png]]

##### Circumcentre (K/O)
O or K is used for **Circumcentre** which is point of concurrency of perpendicular bisectors of sides and is also the centre of circle which circumscribes (encircles) the triangle. 
The radius of this circle is called circumradius and is denoted by $R$. 

![[Pasted image 20230705091737.png]]

##### Excentres ($I_{1},I_{2},I_{3}$)
$I_{1},I_{2},I_{3}$ are used to denote **Excentres** which are centres of circles which touch one side and the extensions of the other two. They also lie on the angular bisectors but two of the 3 AB are external and are 3 in a triangle.
Their radii are denoted by $r_{1},r_{2},r_{3}$.

![[Pasted image 20230705092249.png]]

### Some Results in a Triangle
In a right triangle, the vertex with 90 is the orthocentre and the mid point of hypotenuse is the circumcentre. 
![[Pasted image 20230705092636.png]]

Incentre and centroid always lie within the triangle. 

Orthocentre and circumcentre will lie,
1. Inside the triangle if triangle is acute angled
2. On the triangle if triangle is right angled
3. Outside the triangle if triangle is obtuse angled


#### Results Relating to Centroid
![[Pasted image 20230705095740.png]]

Centroid Divides median in ratio 2:1.

The centroid of DEF will also be G. 
DD$_{1}$, EE$_{1}$, FF$_{1}$ are medians of DEF.

FE is parallel to BC and half of it.
FD is parallel to AC and half of it.
DE is parallel to AB and half of it.

FEDB is a parallelogram. 

Area of each of the 4 triangles is the same,
$$[AFE] = [FBD] = [EDC] = [DEF] = \frac{1}{4}[ABC] $$

All 4 triangles, AFE, FBD, EDC, DEF are congruent with sides as $\displaystyle \frac{ c }{ 2 }, \frac{ a }{ 2 }, \frac{ b }{ 2 }$ respectively. 

Area of the two big triangles is the same,
$$[ABD] = [ADC] = \frac{ 1 }{ 2 }[ABC]$$

The area of the triangles formed using G as one of its vertices is the same,
$$[ABG] = [BCG] = [ACG] = \frac{ 1 }{ 3 }[ABC]$$

##### Apollonius's Theorem

$$AB^{2} + AC^{2} = 2(AD^{2} + DC^{2})$$
$$AB^{2} + AC^{2} = 2(AD^{2} + BD^{2})$$
![[Pasted image 20230705100207.png]]

#### Results Relating to Incentre
![[Pasted image 20230706072428.png]]

The angular bisector divides opposite side in the ratio of adjacent sides.

$$
\begin{split}
\frac{ BD }{ DC } &= \frac{ AB }{ AC } = \frac{ c }{ b } \\
\frac{ AE }{ EC } &= \frac{ AB }{ BC }
\end{split}
$$

Also, the radius of the incentre,
$$r = \frac{ \Delta }{ s }$$

#### Results Relating to Orthocentre

![[Pasted image 20230706072742.png]]

The reflection of H on any side will lie on circumcircle. 

![[Pasted image 20230706073315.png]]

If orthocentre of triangle ABC is H then orthocentre of triangle formed by any 3 of the 4, A, B, C, H will be the remaining. 
Thus  the orthocentre of AHB is C, of BHC is A and so on.

![[Pasted image 20230706073615.png]]

In any triangle, orthocentre, centroid and circumcentre are collinear. G divides HO in the ratio 2:1. #important 
$$\Delta AHG \sim \Delta DOG$$
$$\frac{ AG }{ GD } = \frac{ AH }{ OD } = \frac{ HG }{ GO } = \frac{ 2 }{ 1 }$$
$$OH = 3OG$$

#### Results Relating to Other Shapes

###### Rectangle
![[Pasted image 20230706074003.png]]

Diagonals bisect each other and are equal. 
In general, diagonals are not angular bisectors. 

###### Square

![[Pasted image 20230706074024.png]]

Diagonals are equal, perpendicular to each other and are angular bisectors as well.

###### Parallelogram 
![[Pasted image 20230706074125.png]]

Diagonals are not equal but they bisect each other.
Diagonals are not angular bisectors.
Diagonals are not perpendicular to each other. 

###### Rhombus
![[Pasted image 20230706074350.png]]

Diagonals are mutually perpendicular and bisect each other but not equal.
They are also the angular bisectors.
