def intinput(message):
    while True:
        try:
            return int(input(f"{message}"))
        except ValueError:
            print("Invalid input")

fromval = intinput("Enter FROM value: ")
toval = intinput("Enter TO value: ")
step = intinput("Enter STEP value: ")

if toval < fromval:
    temp = fromval
    fromval = toval
    toval = temp

###########################
print("")
ammnt = 0
numberSum = [0,0]

for num in range(fromval,toval+1,step):
    ammnt += 1
    numberSum[0] += num
    print(num, end=" ")

###########################
print("")

for num in range(toval,fromval-1,-step):
    numberSum[1] += num
    print(num, end=" ")

print("\n")
print(f"TOTAL NUMBERS: {ammnt}")
if numberSum[0] != numberSum[1]:
    print(f"SUM: {numberSum[0]} ({numberSum[1]})")
    print(f"AVERAGE: {numberSum[0] / ammnt} ({numberSum[1] / ammnt})")
else:
    print(f"SUM: {numberSum[0]}")
    print(f"AVERAGE: {numberSum[0] / ammnt}")
exit(0)