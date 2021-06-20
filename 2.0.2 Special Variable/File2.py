# File2.py 

import File1 

print ("File2 __name__ = %s" %__name__) 

if __name__ == "__main__": 
    print ("File2 is being run directly")
else: 
    print ("File2 is being imported")


# When File1.py is run through File2.py by importing, the __name__ variable is set as the name of the python script, i.e. File1.
# Thus, it can be said that if __name__ == "__main__" is the part of the program that runs when the script is run from the command line using a command like python File1.py.     