import math

def userInput(message):
    while True:
        try:
            return int(input(f"Enter {message}: "))
        except ValueError:
            print("Invalid input")

value = userInput("a value (in meters)")
capacity = ((4/3)*math.pi*(math.pow(value, 3)))*1000
days_available = math.floor(capacity/5)

print(f"The capacity of the cylinder is: {capacity} l and will last (for one person) for {days_available} days.")
