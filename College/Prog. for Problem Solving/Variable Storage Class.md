Links: 
___
# Variable Storage Class

1. `auto`
	- Scope: Local
	- Accessibility: Accessible within the block or function where it is declared. 
	- Lifetime: Exists when function or block in which it is declared is entered. Ceases existence when control exits the block.
	- Memory: Main memory (RAM)
	- Default value: Garbage
	  $\\$

2. `extern` (External)
	- Scope: Global
	- Accessibility: Accessible within all the program files that are part of the program.  
	- Lifetime: Exists for the duration of the execution of program. 
	- Memory: Main memory (RAM)
	- Default value: 0
	  $\\$
	
1. `register`
	- Scope: Local
	- Accessibility: Accessible within the block.  
	- Lifetime: Exists withing the function or block where it is declared. Except in the case of storage full, it transfers to main memory. 
	- Memory: CPU Register
	- Default value: Garbage
	  $\\$


1. `static`
	- Scope: Local or Global
	- Accessibility: Access depends on scope.
	- Lifetime: Exists withing the function or block where it is declared. Except in the case of storage full, it transfers to main memory. 
	- Memory: Main memory
	- Default value: 0
	  $\\$