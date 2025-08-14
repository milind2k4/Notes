Links: 
___
# Computer Languages
Human language is not understood by the computer and thus, to give it instruction, we use special types of languages which are designed to be understood by it. 

These languages are known as computer languages. 

Examples are, C, C++, Java, B, JS, Rust etc. 

## Generations of Languages 
- **Ist:** Machine language (0s and 1s) 
- **IInd:** Assembly (we can use symbols alongside 0s and 1s). Assembly is used in microprocessors and microcontrollers. 
- **IIIrd:** Middle (C, C++, Pascal, Cobol)/High level languages (C++, Python, ) 
- **IVth:** Non Procedural language (SQL, database related commands)
- **Vth:** Natural Language Processing (NLP) (chatbots)

There are 3 software which are used for reading the language.

In natural language processing, interpreter is used as a mediator. 
In NLP, we first define a dictionary containing all the terms and their semantics. 

#### Assembler 
It converts program written in assembly language (or symbolic language) to machine code (binary). 

It reads the whole file at once. 

%%draw diagram%%

#### Compiler 
It converts program written in middle level language into object code/file. 

It checks whole code syntactically, logically and semantically. If any error is found, then it gives message to the programmer and ceases the conversion.
%%draw diagram%%

#### Interpreter
It converts program into machine language by reading it line by line. 

If any error is found in any line, the execution is the program is halted. 

%%draw diagram%%

### Compilation of C program
C is a compiled language. I.e. C source code is converted into machine code by a compiler. 

#### Linker
Some built in and essential files and libraries are stored that need to be included for the basic functions during the execution of the program. 

Therefore, these files are linked to the source code being executed by a program called linker. 

The compiler automatically invokes the linker as the last step in compilation of the program. 

%%draw diagram%%
%% compilation of c program %%

#### Loader
It is a part of OS that brings and executable file residing on disk into memory and starts it running. 

Loading of program involves the reading of executable files into memory. 

