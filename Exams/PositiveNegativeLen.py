def userInput(message):
    while True:
        try:
            return int(input(f"Enter {message}: "))
        except ValueError:
            print("Invalid input")

value = userInput("a number")
if value > 0:
    print("Number is POSITIVE")
    if value % 2 == 0:
        print("Number is EVEN")
    else:
        print("Number is ODD")

    S = value * value
    O = value * 4

    print(f"O = {O}, S = {S}")

elif value < 0:
    print("Number is NEGATIVE")
    value = -value
    mmvalue = value * 1000

    print(f"{value} meters = {mmvalue} milimeters")

elif value == 0:
    print("Number is 0, not counted")