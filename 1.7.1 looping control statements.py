
# Loop Control Statements

# Loop control statements change execution from its normal sequence.
# When execution leaves a scope, all automatic objects that were created in that scope are destroyed.


# Continue Statement
# It returns the control to the beginning of the loop.

# Prints all letters except 'p' and 'n'
for letter in 'python programming': 
    if letter == 'p' or letter == 'n':
         continue
    print('Current Letter :', letter)
    var = 10

# Break Statement
# It brings control out of the loop.

# break the loop as soon it sees 'n' or 'g'
for letter in 'python programming': 
    if letter == 'n' or letter == 'g':
         break
print('Current Letter :', letter)
