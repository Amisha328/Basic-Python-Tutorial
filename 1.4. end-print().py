# Python end parameter in print

# By default python's print() function ends with a newline.
# A programmer with C/C++ background may wonder how to print without newline.
# Python's print() function comes with a parameter called 'end'. 
# By default, the value of this parameter is '\n', i.e. the new line character.
# You can end a print statement with any character/string using this parameter.


# ends the output with a <space> 
print("Welcome to" , end = ' ') 
print("Python Basics", end = ' ')
print("Tutorial", end = ' ')


# ends the output with '@'
print("Learning" , end = '@') 
print("Python Basic Tutorial")



