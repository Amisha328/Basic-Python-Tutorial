# Iterators in Python

# A C-style way of accessing list elements
cars = ["Aston", "Audi", "McLaren"]
i = 0
while (i < len(cars)):
    print(cars[i])
    i += 1

# Use of for each loop
cars = ["Aston", "Audi", "McLaren"]
for x in cars:
    print(x)    
   
# Indexing using Range function
cars = ["Aston", "Audi", "McLaren"]
for i in range(len(cars)):
    print(cars[i])

#using the enumerate() function to get index 
days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
for i, d in enumerate(days):
    print (i, d)   

# Looping extensions
# Two iterators for a single looping construct

# a list and dictionary are to be used for each iteration in a single looping block using enumerate function.
cars = ["Aston", "Audi", "McLaren"]
accessories = ["GPS kit", "Car repair-tool kit"]

# Single dictionary holds prices of cars and 
# its accessories.
# First three items store prices of cars and
# next two items store prices of accessories.
prices = {1:"570000$", 2:"68000$", 3:"450000$",
          4:"8900$", 5:"4500$"}

# Printing prices of cars
for index, c in enumerate(cars, start=1):
    print("Car: %s Price: %s"%(c, prices[index]))

# Printing prices of accessories
for index, a in enumerate(accessories,start=1):
    print ("Accessory: %s Price: %s"\
           %(a,prices[index+len(cars)]))          