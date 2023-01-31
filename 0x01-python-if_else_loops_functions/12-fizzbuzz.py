#!/usr/bin/python3
def fizzbuzz():
    for num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz ", end="")
elif num % 3:
    print("Fizz " end="")
elif num % 5:
    print("Buzz " end="")
else:
    print("{} ".format(num), end="")
