def intinput(message):
    while True:
        try:
            return int(input(f"Enter {message}: "))
        except ValueError:
            print("Invalid input")

fromVal = intinput("starting number")
toVal = intinput("ending number")

if fromVal > toVal:
    temp = fromVal
    fromVal = toVal
    toVal = temp

for number in range(fromVal, toVal+1):
    isPrime = True
    for i in range(2, number):
        if number % i == 0:
            isPrime = False

    if isPrime:
        print(f"{number} - Prime number")
    #else:
        #print(f"{number} - Not a prime number")

exit (0)