import math

ammnt = 0
numberSum = 0
numberMax = -math.inf

def intinput(message):
    while True:
        try:
            return int(input(f"{message}"))
        except ValueError:
            print("Invalid input")

print("TYPE 0 TO QUIT\n")
while True:
    num = intinput(f"Number {ammnt+1}: ")
    if num == 0:
        print("QUITTING")
        break
    if num > numberMax:
        numberMax = num
    numberSum += num
    ammnt += 1

print(f"\nSum = {numberSum}")
print(f"Count = {ammnt}")
print(f"Max = {numberMax}")
print(f"Average = {numberSum/ammnt}")