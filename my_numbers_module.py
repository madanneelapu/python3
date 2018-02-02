import math

print("This is my numbers module")


def printmsg():
    print("Inside printmsg function")
    print("Module name is: ", __name__)


if __name__ == "__main__":
    print("executing  my numbers module as a script")
    printmsg()

iseven = lambda n: n % 2 == 0

isodd = lambda n: n % 2 == 1

def isprime(n):
    for f in range(2, int(math.sqrt(n)) + 1):
        if n % f == 0:
            return "No! Not a Prime Number"

    return "Yes! Prime Number"