def userInput(message):
    while True:
        try:
            return int(input(f"Enter {message}: "))
        except ValueError:
            print("Invalid input")

number = userInput("a number")
numLength = len(str(number))
match numLength:
    case 1: print("Jednociferné")
    case 2: print("Dvouciferné")
    case 3: print("Trojciferné")
    case _: print("Víceciferné")