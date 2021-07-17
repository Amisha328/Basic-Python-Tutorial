# Python's memory allocation and deallocation method is automatic.

# The literal value 9 is an object.
# The reference count of object 9 is incremented to 1 in line 1.
# In line 2 its reference count becomes zero as it is dereferenced.
# So garbage collector deallocates the object.

# Literal 9 is an object
b = 9

# Reference count of object 9 
# becomes 0.
b = 4

# create_cycle() creates an object x which refers to itself, 
# the object x will not automatically be freed when the function returns. 
def create_cycle():

    # create a list x
    x = [ ]

    # A reference cycle is created
    # here as x contains reference to
    # to self.
    x.append(x)
 
create_cycle()


