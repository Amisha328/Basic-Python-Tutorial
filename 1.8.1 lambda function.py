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

