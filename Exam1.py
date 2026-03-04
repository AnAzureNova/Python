import math

def intinput(message):
    while True:
        try:
            return int(input(f"Enter {message}: "))
        except ValueError:
            print("Invalid input")
isExit = False
while not isExit:
    isNotPrime = False
    number = intinput("a number")
    if number == 0:
        isExit = True
        break

    for i in range(2, number):
        if number % i == 0:
            isNotPrime = True

    if not isNotPrime:
        print("Prime number")
    else:
        print("Not a prime number")

exit(0)