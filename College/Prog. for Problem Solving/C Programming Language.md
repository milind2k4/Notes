Links: [[Computer Languages]]
___
# C Programming Language
### C Character Set 
C char set includes, 
- A-Z, 
- a-z, 
- 0-9, 
- &, $, #, ;, ?, /, \\, !, (, ), +, -, <, >, {, }. =, etc.

#### Tokens 
Token is a small unit of a program consisting of variable, identifiers, keywords and constants. 

##### Variables
Variables are a names which are given to any memory location which may change its value during the execution of the program. 

The purpose of variable is to store the data value, the compiler will access the address of the variable  and the user will access it by the variable name. 

A variable name,
1. Can be upper, lower or mixed in cases
2. Cannot be a keyword 
3. Can consist of alphanumerical
4. Cannot start or contain any special character other than "\_". 
5. Cannot start with a digit

##### Identifier
Identifier is a name given to a variable, a constant, a function name, array, micros etc. 

It is a user defined name. 

It is superset of variable.

##### Keywords 
Reserved, or predefined words in which the meaning is already defined by the compiler.

All the keywords are lower case. 

C has 32 keywords. 
For example,
```
true, flase, int, float, char, while, for, break, do, goto, etc.
```

##### Constants 
Constant is a variable that does not change during the execution of the program. 

There are two types of constant. 
1. **Numerical** 
	1. *Integer:* They are nothing but numerical values that can be +ve or -ve and by default, they are +ve. 
	   E.g. 
	   `const PI = 3.14`
	   `#define PI 3.14`
	1. *Real:* They are the values with decimal and fractional points. It consists of 2 parts, Mantissa and Exponent. 
	   E.g. 
	   `const PI = 3.14`
	   3 is mantissa and .14 is exponent.
2. **Character:** Every key on the keyboard acts as a character. And character which are enclosed in single quotations act as character constant. 
   
	If there are more than one character, then it has to be enclosed in double quotes. Hence, they are called string constant.  

	All strings end in `\0` which is the null value. 

### Datatypes
There are 5 primitive or primary data types in C.
```c
int (integer)
float (decimal)
double (large decimal)
char (A-Z, a-z, 0-9, special characters)
void (NULL)
```

##### MACROS
`int`
INT_MIN 
INT_MAX 

`float`
FLT_MIN
FLT_MAX

`double`
DBL_MIN 
DBL_MAX 

`long double`
LDBL_MIN 
LDBL_MAX
#### `int`: Integer 
Range: (-32,768 to 32767)
Format Specifier: %d or %i (signed)
Return: `int`

E.g. -32, 34, 3342, -31099, etc. 

#### `float`: Floating Point Integer 
Range: ($-3.14\times e^{ 38 }$ to $3.14 \times e^{ 38 }$)
Format Specifier: %f, %g, %e (for exponential format) 
Return: `float`

E.g. 0.1, 234.04, 3.14, -3.33333 etc. 

To print a certain no. of digits after the decimal, we use `%.nf` where n is the no. of digits after decimal to show. 

#### `double`: Larger float 
Range: $-1.7 \times 10^{308}$ to $1.7 \times 10^{308}$
Format Specifier: `%ld` or `%LF`

E.g. more value with 15 decimal value range. 

#### `char`: Character 
Range: -128 to 127 (ASCII codes)
Format Specifier: `%c` (single character)

E.g. 'a', 'b', 'C', '5', '&' etc.

#### `void`: NULL 
It is null value.

### Data Modifiers 
```c
short
long 
signed 
unsigned 
```

Modifiers change the range and/or the memory allocated to the value. 

`short` and `long` change the memory allocated and thus the range.
`signed` and `unsigned` change the range. 

Size is in bytes.


| Data Type              | Size | Range                                           | Format Specifier |
| ---------------------- | ---- | ----------------------------------------------- | ---------------- |
| `signed short int`     | 2    | -32,768 to 32,767                               | `%d/%i`          |
| `unsined short int`    | 2    | 0 to 65,535                                     | `%u`             |
| `unsigned int`         | 4    | 0 to 4,294,967,295                              | `%u`             |
| `signed long int`      | 4    | -2,147,483,648 to 2,147,483,648                 | `%ld/%li`        |
| `unsigned long`        | 4    | 0 to 4,294,967,295                              | `%lu`            |
| `signed char`          | 1    | -128 to 127                                     | `%c`             |
| `long double`          | 10   | -3.4$\times 10^{4982}$ to 3.4$\times 10^{4982}$ | `%lf/%Lf`        |
| `unsigned char`        | 1    | 0 to 255                                        | `%c`             |


For `unsinged long int` we use lu at the end. E.g. 56lu. 

## Operators 
C has various operators,

1. Arithmetic -> Number output
	- \+
	- \-
	- \*
	- /
	- %
	  $\\$
1. Relational -> 0/1
	- <
	- <=
	- \>
	- \>=
	- \==
	- !=
	  $\\$

1. Logical -> 0/1
	- &&
	- || 
	- ! 
	- XOR
	  $\\$
1. Bitwise -> 0/1
	- bitwise AND
	- bitwise OR
	- bitwise NOT
	- bitwise XOR
	- << (bitwise left shift) 
	- \>> (bitwise right shift)
	  $\\$
1. Unary -> Any value
	- = (assignemnt operator)
	- !
	- ~
	- &
	- \*(at given value)
	- +=
	- -=,
	- \*=
	- /=
	- %=
	- ++ (post + pre)
	- \-- (post + pre)
	  $\\$
	  
1. Conditional/Ternary -> out1/out2
	- `(condition exp.) ? out1:out2 `
	  $\\$
	  
1. sizeof -> unsiged iteger 
	- `sizeof(var)`
	  $\\$
	  
1. comma 
	- ,
	- ;
	  $\\$
	  
1. Equality -> 0/1
	- \==
	- =!
	  $\\$

For floating modulation, we need to use `fmod(num1, num2)`

### Precedence and Associativity 
Precedence is the priority of order, i.e. which operator will first be performed. 

Associativity means how the operator will work, i.e. left to right or right to left. 

Whenever we have expression with multiple operators having the same precedence, then we execute the statement according to associativity. 

If we have an expression having operators which have different precedence, then we execute the statement according to the priority order. 

|              | Operators                                                                                          | Associativity |
| ------------ | -------------------------------------------------------------------------------------------------- | ------------- |
| Highest pre. | () function call, \[\] subscription, -> pointer to no. access, . meant to access, ++, -- (postfix) | Left to Right |
| UNARY        | ! not, ~ compliment, +=, -=, \*=, /=, %=, ++ -- (prefix), &, \*, sizeof(), typecast()              | Right to Left |
| Arithmetic   | \* / %                                                                                             | Left to Right |
| Arithmetic   | + -                                                                                                | Left to Right |
| Bitwise      | << (left shift), >> (right shift)                                                                  | Left to Right |
| Relational   | <, <=, >, >=                                                                                       | Left to Right |
| Relational   | \==, !=                                                                                            | Left to Right |
| Bitwise      | & (bw AND), \| (bw OR), ^ (bw NOT)                                                                 | Left to Right |
| Logical      | && (AND), \|\| (OR)                                                                                | Left to Right |
| Conditional  | () ? ():()                                                                                         | Right to Left |
| Assignment   | =, +=, -=, \*=, /=, %=, <<=, >>=, &=, ^=, \|=                                                      | Left to Right |
| Separator    | , and ;                                                                                            | Left to Right |




