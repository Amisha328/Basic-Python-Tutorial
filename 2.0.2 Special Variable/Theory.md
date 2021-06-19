## __ name__() (Sepcial Variable) in Python

- Since there is no main() function in Python, when the command to run a python program is given to the interpreter, the code    that is at level 0 indentation is to be executed. 
- However, before doing that, it will define a few special variables. 
-**__ name__** is one such special variable. 
- If the source file is executed as the main program, the interpreter sets the __ name__ variable to have a value "__ main__". 
- If this file is being imported from another module, __ name__ will be set to the module's name.
- **__ name__ is a built-in variable which evaluates to the name of the current module.**
- Thus it can be used to check whether the current script is being run on its own or being imported somewhere else by combining it with if statement.



