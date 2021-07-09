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

# Return sends a specified value back to its caller whereas Yield can produce a sequence of values. 
# We should use yield when we want to iterate over a sequence, but don't want to store the entire sequence in memory.   

# Yield are used in Python generators. 
# A generator function is defined like a normal function, but whenever it needs to generate a value, it does so with the yield keyword rather than return.

# A Python program to generate squares from 1 to 100 using yield and therefore generator.

# An infinite generator function that prints
# next square number.
def nextSquare():
    i = 1;

    # An Infinite loop to generate squares 
    while True:
        yield i*i                
        i += 1  # Next execution resumes 
                # from this point     

# Driver code to test above generator 
# function
for num in nextSquare():
    if num > 100:
         break    
    print(num)
