# There are two types of Type Conversion in Python:
    # Implicit Type Conversion
    # Explicit Type Conversion

# Implicit Type Conversion

# In Implicit type conversion of data types in Python, 
# the Python interpreter automatically converts one data type to another without any user involvement. 


def main():

    x = 10

    print("x is of type:",type(x))

    y = 10.6
    print("y is of type:",type(y))

    x = x + y

    print(x)
    print("x is of type:",type(x))

if __name__ == "__main__":
  main()     


# You can see the type of 'x' got automatically changed to the "float" type from the "integer" type. 
# This is a simple case of Implicit type conversion in python.    



