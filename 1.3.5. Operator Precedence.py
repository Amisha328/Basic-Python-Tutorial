#
# Examples of Operator Precedence
#

def main():
    
    # Precedence of '+' & '*' 
    expr = 10 + 20 * 30
    print(expr) 

    # Precedence of 'or' & 'and' 
    name = "Alex"
    age = 0
    
    if name == "Alex" or name == "John" and age >= 2 :  
        print("Hello! Welcome.") 
    else : 
        print("Good Bye!!")


if __name__ == "__main__":
  main()      