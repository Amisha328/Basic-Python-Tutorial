#
# Working with loops
#

def main():
  x = 0
  
  # define a while loop
  while (x < 5):
     print (x)
     x = x + 1

  # Using else statement with while loops
  # The else clause is only executed when your while condition becomes false.
  # If you break out of the loop, or if an exception is raised, it won't be executed. 

  #Python program to illustrate
  # combining else with while
  count = 0
  while (count < 3):    
      count = count + 1
      print("Hello Geek")
  else:
      print("In Else Block")

  # define a for loop
  for x in range(5,10):
    print (x)

  
 # use a for loop over a collection
  days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
  for d in days:
    print (d)
  
  # use the break and continue statements
  for x in range(5,10):
    #if (x == 7): break
    #if (x % 2 == 0): continue
    print (x)
  
  #using the enumerate() function to get index 
  days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
  for i, d in enumerate(days):
    print (i, d)  
     
if __name__ == "__main__":
  main()
