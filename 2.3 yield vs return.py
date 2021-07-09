# The yield statement suspends function's execution and sends a value back to the caller,
# but retains enough state to enable function to resume where it is left off. 

# A generator function that yields 1 for the first time,
# 2 second time and 3 third time
def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3

# Driver code to check above generator function
for value in simpleGeneratorFun(): 
    print(value)


