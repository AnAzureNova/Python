def userInput(message):
    while True:
        try:
            return int(input(f"Enter the {message}: "))
        except ValueError:
            print("Invalid input")

width = userInput("width of the field")
length = userInput("length of the field")
lapAmount = userInput("amount of laps")

oneLap = 2*(width+length)
print(f"Field width is {width}m and field length is {length}m")
print(f"One lap is {oneLap}m")
print(f"After {lapAmount} laps i will run {oneLap * lapAmount}m")