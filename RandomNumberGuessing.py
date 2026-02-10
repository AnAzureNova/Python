import random

atts = 1
fromRange = 1
toRange = 15
print(f"Guess the number ({fromRange}-{toRange})")
rngnum = random.randint(fromRange, toRange)
#test

def intinput():
    while True:
        try:
            return int(input(f"[{atts}] > "))
        except ValueError:
            print("Invalid input")

while True:
    guess = intinput()
    if guess == rngnum:
        print(f"You guessed the number in {atts} attempts")
        exit(0)
    else:
        atts += 1