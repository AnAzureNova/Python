import math

def intInput(message):
    while True:
        try:
            return int(input(f"Enter {message}: "))
        except ValueError:
            print("Invalid input")

def factorial(number):
    if number < 0:
        number *= -1
    result = number
    if number != 0:
        for i in range(number - 1, 0, -1):
            result *= i
    else:
        result = 1
    return result

number = intInput("a number")
fact = factorial(number)
#print(math.factorial(number))

print(fact)



