# the lambda keyword is used to define an anonymous function.
# lambda functions are syntactically restricted to a single expression.
# It can have any number of arguments but only one expression, which is evaluated and returned.

def cube(y):
    return y*y*y

lambda_cube = lambda y: y*y*y

# using the normally
# defined function
print(cube(5))

# using the lambda function
print(lambda_cube(5))

# Using lambda() Function with filter()
# filter() offers elegant way to filter out all the elements of a sequence "sequence", for which the function returns True. 

# filter() with lambda()
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

final_list = list(filter(lambda x: (x%2 != 0) , li))
print(final_list)