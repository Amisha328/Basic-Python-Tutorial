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