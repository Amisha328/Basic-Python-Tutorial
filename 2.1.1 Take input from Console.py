# What is Console in Python? 

# Console (also called Shell) is basically a command line interpreter that takes input from the user.
# If it is error free then it runs the command and gives required output otherwise shows the error message. 


def main():
    
    # To take input from the user we make use of a built-in function input().

    # input
    input1 = input()

    # output
    print(input1)

    # Type cast the user input 

    # Typecasting the input to Integer

    # input
    num1 = int(input())
    num2 = int(input())

    # printing the sum in integer
    print(num1 + num2)

    # Typecasting the input to Float

    # input
    num1 = float(input())
    num2 = float(input())

    # printing the sum in float
    print(num1 + num2)

    # Typecasting the input to String

    # input
    string = str(input())

    # output
    print(string)

if __name__=="__main__":
        main()
