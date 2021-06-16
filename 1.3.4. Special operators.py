#
# Examples of Special operators
#

def main():
    # Examples of Identity operators
    a1 = 3
    b1 = 3
    a2 = 'PythonBasicTutorial'
    b2 = 'PythonBasicTutorial'
    a3 = [1,2,3]
    b3 = [1,2,3]


    print(a1 is not b1)


    print(a2 is b2)

    # Output is False, since lists are mutable.
    print(a3 is b3)


    # Examples of Membership operator

    x = 'Python Basic Tutorial'
    y = {3:'a',4:'b'}


    print('P' in x)

    print('python' not in x)

    print('Python' not in x)

    print(3 in y)

    print('b' in y)

if __name__ == "__main__":
  main()       