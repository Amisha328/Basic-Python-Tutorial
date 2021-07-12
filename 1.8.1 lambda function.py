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

# Using lambda() Function with map()
# The map() function takes in a function and a list as an argument.
# map() with lambda()
# to get double of a list.
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

final_list = list(map(lambda x: x*2, li))
print(final_list)

animals = ['dog', 'cat', 'parrot', 'rabbit']

# here we intend to change all animal names
# to upper case and return the same
uppered_animals = list(map(lambda animal: str.upper(animal), animals))

print(uppered_animals)

# Using lambda() Function with reduce()
# The reduce() function belongs to the  functools module.
# reduce() with lambda()
# to get sum of a list

from functools import reduce
li = [5, 8, 10, 20, 50, 100]
sum = reduce((lambda x, y: x + y), li)
print (sum)