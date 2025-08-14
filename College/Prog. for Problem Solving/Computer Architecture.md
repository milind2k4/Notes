Links: 
___
# Computer Architecture

Computer is an electronic device that takes input, processes it and gives output. It also processes data as per the instruction given. 

### Computer Architecture

A compute consists of 4 units, 
- Input
- Control (CPU)
- Memory/Storage 
- Output

![[Computer_architecture_block_diagram.png]]

1. **Input Unit:** Used for entering data and programs into the computer system by the user for processing. 
	E.g. Mouse, Keyboard, Joystick etc.
	$\\$

2. **Storage Unit:** Used for storage of data and instruction before and after processing. Memory can be classified into two types.
	- *Primary:* RAM, ROM, Cache, Registers.
	- *Secondary:* HDD, SSD, Magnetic Tapes etc. 
	$\\$

3. **Output Unit:** Used for displaying/emitting/manifesting the result  produced by the computer after processing. 
	E.g. Monitor, Printer, Speaker, 3D Printer etc.
	$\\$

4. **Processing Unit:** The task of performing arithmetic and logical operations and controlling where what data is sent/received is performed by the CPU. It consists of the *Control Unit (CU)* and the *Arithmetic Logic Unit (ALU).* 
	- *CU:* Controls all operations like input, processing and output. It takes care of step by step processing of all operations inside the computer. 
	- *ALU:* Performs all the instruction operations related to calculation and comparisons.

### Memory 
Memory is arranged in its access time and this arrangement is called **Memory Hierarchy.**

![[Memory-Hierarchy-Design-768.png]]

Levels 0 through 2 are primary memory and the rest are secondary. 

#### Register
It is a temporary and small amount of storage as a part of CPU and is used to hold information on a temporary basis. 

Data from the main memory is stored here for computation and manipulation. The manipulated data is often stored back into the main memory. 

There are different types of registers available. Some of them are,
1. **Address:** Holds/Stores the address of the active memory location.
2. **Accumulator:** Holds the data which is to be operated upon, the intermediate result and the final result of the processing. 
3. **Instruction:** Holds the current instruction being executed. 

#### Cache 
It is extremely fast and small memory located between the CPU and the main memory. Its access time is close to the processing speed of the CPU. 

It acts as a high speed buffer between the CPU/registers and the main memory. 

It is used to store active data and instructions temporarily during processing. 

![[cache between CPU and MM.png]]

If the data being searched is available in the cache, then the event is called a *Cache Hit* otherwise it is called a *Cache Miss.*

![[Cache Hit and Miss.jpg]]

#### Main Memory
##### Random Access Memory (RAM)
It is the place in computer where the OS, applications and the data in current used are kept temporarily so that they can be accessed by the CPU. 

RAM is volatile because it its content is deleted when the computer is turned off. 

![[RAM.jpg]]

##### Read Only Memory 
It is a special type of memory which can only be read and it's contents are not deleted even when the computer is turned off. This is why it is called non volatile memory. 

It typically contains manufacturer's instructions. 

![[ROM.jpg]]

### Secondary Memory 
##### Hard Disk Drive (HDD)
Hard disks are made up of rigid material and are usually a stack of metal disks sealed in a box. 

The hard disk and the hard disk drive exist together as a unit and is a permanent part of the computer where data and programs are saved. 

These disks have storage capacity ranging from gigabytes (GB) to petabytes (PB). These are rewritable. 

![[hard-drive.webp]]

### History of the Computer 
####  Ist Generation (1942-55)
##### Key Hardware
Vacuum Tubes, Punch Cards.

##### Key Software
Machine and Assembly Language.

##### Characteristics
   Bulky in Size, Unreliable, Difficult to use and Limited Commercial use. 
##### Examples 
ENIAC, EDBAC 

#### IInd (1955-64)
##### Key Hardware
Transistors, Magnetic Tapes, Hard disks.

##### Key Software
Mid Level language and introduction to high level language for scientific and commercial application.

##### Characteristics
Faster, Smaller, More reliable and easy to program. 

##### Example
IBM 7030.

#### IIIrd (1964-75)
##### Key Hardware
Integrated Circuits (ICs) with small scale integration and medium scale integration tech., larger capacity disk and magnetic tapes, chips. 

##### Key Software
Time sharing operating system (OS)

##### Characteristics
Cheaper to use and faster, smaller and more reliable.

##### Examples
IBM 360 and 370.

#### IVth (1975-89)
##### Key Hardware 
ICs with VLSI (Very Large Scale Integration) technology, micro processor, semi conductor memory and larger capacity hard disk.

##### Key Software
OS for personal computers (PC) like Windows, MacOS and Unix/Linux.

##### Characteristics
Small, Affordable, more efficient and totally general purpose machines. 

##### Examples 
Laptops, PCs, etc.

#### Vth (1989-Present)
##### Key Hardware
ICs with ULSI (Ultra Large Scale Integration).

##### Key Software
World Wide Web, Internet.

##### Characteristics
Super Fast, easy to use, portable, time sharing.

##### Examples
Smartphones, Smartwatches, Supercomputers, Robots

## Operating System (OS)
OS is the program that acts as an interface between user (software) and hardware and controls the computer. 

Functions of OS:
1. Process management
2. Memory management
3. Security management 
4. File management
5. Command Interpreter 

Examples are Windows, MacOS, Linux, Unix, android, iOS, etc.

### Types of OS
1. **Real Time:** Allows multiple processes to run at a specified time interval. 
   
	It has two types,
	- **Hard RT:** fixed time interval, i.e. after delay process will be terminated. They are used in Rockets. 
	- **Soft RT:** process can extend the time interval even after delay. 
	  $\\$

2. **Multiprocessor:** Allows more than one processor to be there for the processing. 
	  $\\$

4. **Multiprogramming/Multitasking:** Allows running of many software processes at the same time. 
	  $\\$

5. **Single user:** Only one user can access the computer at a time.
	  $\\$

6. **Multiuser:** Many users can access the same computer at the same time, or different times at multiple locations .
	  $\\$

7. **Multithreading:** The smallest task of a process is called a thread. 
   
	A multithreading OS can do multiple of these threads at once. 
