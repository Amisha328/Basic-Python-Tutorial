# range() and xrange() are two functions that could be used to iterate a certain number of times in for loops in Python.

# In Python 3, there is no xrange , but the range function behaves like xrange in Python 2.

# range() - This returns a range object (a type of iterable).
# xrange() - This function returns the generator object that can be used to display numbers only by looping.
#            Only particular range is displayed on demand and hence called "lazy evaluation".

# Python code to demonstrate range() vs xrange()
# on  basis of return type

import sys

# initializing a with range()
a = range(1,10000)

# initializing a with xrange()
x = xrange(1,10000)   # not defined in python 3

# testing the type of a
print ("The return type of range() is : ")
print (type(a))       # o/p: <type 'list'> 
                        

# testing the type of x
print ("The return type of xrange() is : ")
print (type(x))      # o/p: <type 'xrange'> 

# The variable storing the range created by range() takes more memory as compared to variable storing the range using xrange(). 
# The basic reason for this is the return type of range() is list and xrange() is xrange() object.

# Python code to demonstrate range() vs xrange()
# on  basis of memory

# initializing a with range()
a = range(1,10000)

# initializing a with xrange()
x = xrange(1,10000)      # not defined in python 3

# testing the size of a
# range() takes more memory
print ("The size allotted using range() is : ")
print (sys.getsizeof(a))    # o/p: 80064

# testing the size of a
# range() takes less memory
print ("The size allotted using xrange() is : ")
print (sys.getsizeof(x))    # o/p: 40


