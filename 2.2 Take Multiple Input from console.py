# What is Console in Python? 

# Console (also called Shell) is basically a command line interpreter that takes input from the user.
# If it is error free then it runs the command and gives required output otherwise shows the error message. 


# use raw_input() two times
x, y = input(), input()

print(x,y)

#  use split()
#  split() uses any whitespace characters as a delimiter by default
x, y = input().split()

print(x,y)

# In above two methods  both x and y would be of string.
# We can convert them to int using another line
# x, y = [int(x), int(y)]

# print(type(x),type(y))

# We can also use  list comprehension
# x, y = [int(x) for x in input().split()]  

# print(type(x),type(y))

# We can also use  map function
x, y = map(int, input().split())

print(type(x),type(y))
