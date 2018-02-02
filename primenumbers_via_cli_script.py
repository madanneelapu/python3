# Take multiple numbers a CLI arguments and check if each number is a prime number.
# Display an error message if no parameters are given executing the module as a script.

import sys # import built-in sys module
from my_numbers_module import isprime # importing a function in custom module

if __name__ == "__main__": # if module is run as a script
    if len(sys.argv) < 2: # check if parameters are passed
        print("Parameters missing...", "Please add one or more parameters and try again")
    else:
        for idx in range(1, len(sys.argv)): #iterating over parameters
            print(sys.argv[idx], isprime(int(sys.argv[idx]))) #converting parameter to integer and checking the prime-ness
