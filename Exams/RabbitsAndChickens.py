def userInput(message):
    while True:
        try:
            return int(input(f"Enter {message}: "))
        except ValueError:
            print("Invalid input")

def boolInput(message):
    while True:
        value = input(f"{message}: ")
        if value.upper() == "YES" or value.upper() == "Y":
            return True
        elif value.upper() == "NO" or value.upper() == "N":
            return False
        else:
            print("Invalid input")

if boolInput("Specify amount of animals? (YES/NO)"):
    amount_rabbits = userInput("the amount of rabbits")
    amount_chickens = userInput("the amount of chickens")

    total_heads = amount_chickens + amount_rabbits
    total_legs = amount_chickens * 2 + amount_rabbits * 4

    print(f"Theres a total of {total_heads} heads and {total_legs} legs")
else:
    amount_heads = userInput("the amount of heads")
    amount_legs = userInput("the amount of legs")

    total_chickens = 0
    for index in range(amount_heads):
        print(index)
        print(amount_legs % amount_heads-index)
        if amount_legs % amount_heads-index == 0:
            total_chickens = amount_heads-index
            print(f"I:{index} CH:{total_chickens}")
            break
    total_rabbits = amount_heads - total_chickens

    print(f"Theres a total of {total_rabbits} rabbits and {total_chickens} chickens")


