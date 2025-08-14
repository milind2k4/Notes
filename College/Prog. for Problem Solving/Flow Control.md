Links: [[C Programming Language]]
___
# Flow Control

### Conditional Statements 
#### n no. of conditions
we will use `switch case` statements. 

Syntax is,
```c
switch (var){
	case x:
		do something;
		break;
	case y:
		do something;
		break;
	default:
		do something;
		break;
}
```

`break` allows the flow of control to go exit form the switch block. 

#### Uncertain count of conditions 
i.e. when we use "otherwise"

We will use, 
- if statements 
- if - else statements 
- nested if statements 

```c
if (condition){
	statements
} else if (condition 2){
	statements
} else {
	statements
}
```

The if ends wherever we put the semicolon, ";". 

Thus,
```c
a = 10
if (a == 10);
	printf("%d", a);
```

