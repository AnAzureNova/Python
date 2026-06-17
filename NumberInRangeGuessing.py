import random

leniency = 3
width = 1

guesscache = []
randguesscache = []
guessrange = {
    "from": 0,
    "to": 0,
}


def boolinput():
    while True:
        inputmsg = input("> ").lower()
        if inputmsg == "yes":
            return True
        elif inputmsg == "no":
            return False

def intinput():
    while True:
        try:
            return int(input("> "))
        except ValueError:
            print("!! Invalid input")

def modeslct():
    print("CHOOSE RANGE\n[1] - From 1 to 10\n[2] - From 1 to 50\n[3] - From 1 to 100\n[4] - Custom (NOT FINISHED)\n[5] - End program\n")
    userchoice = intinput()

    match userchoice:
        case 1:
            guessrange["from"] = 1
            guessrange["to"] = 10
            return True
        case 2:
            guessrange["from"] = 1
            guessrange["to"] = 50
            return True
        case 3:
            guessrange["from"] = 1
            guessrange["to"] = 100
            return True
        case 4:
            print("TEMP")
            exit(0)
        case 5:
            exit(0)
        case _:
            print("!! Invalid input")
    return False

def guess(point, comparator):
    match comparator:
        case '>':
            print(f"Is the number greater than {point}?")
            ans = boolinput()
            if ans:
                guessrange["from"] = point
            else:
                guessrange["to"] = point
            guesscache.append(point)

        case '<':
            print(f"Is the number lesser than {point}?")
            ans = boolinput()
            if ans:
                guessrange["to"] = point
            else:
                guessrange["from"] = point
            guesscache.append(point)
        case _:
            print("!! UNKNOWN ERROR")
            exit(0)


def coinflip():
    x = random.randint(0, 1)
    match x:
        case 0:
            return '>'
        case 1:
            return '<'
        case _:
            print("!! UNKNOWN ERROR")
            exit(0)

def loop():
    #print(f"_DEBUG: {guessrange["to"] - guessrange["from"]}")
    #print(f"_DEBUG: {len(randguesscache)}")
    point = 0
    comparator = 0

    isSkip = False
    if not (guessrange["to"] - guessrange["from"]) - len(randguesscache) <= 1:
        isCache = True
        while True:
            point = random.randint(guessrange["from"], guessrange["to"])
            comparator = coinflip()
            if point not in guesscache:
                break
            #print(f"_DEBUG: {point} IS IN CACHE - SKIPPING")

        #print(f"_DEBUG: ANS CACHE {guesscache}")
        #print(f"_DEBUG: GUESSING FROM {guessrange['from']} TO {guessrange['to']}")
        #print(f"_DEBUG: SELECTED POINT {point}")
        guess(point, comparator)
    else:
        isSkip = True


    if guessrange["to"] - guessrange["from"] < random.randint(leniency - 1, leniency + 1) or isSkip:
        #print(f"_DEBUG: CACHE {randguesscache}")
        isCache = True
        randguess = 0
        while True:
            randguess = random.randint(guessrange["from"], guessrange["to"])
            if randguess not in randguesscache:
                break

        print(f"The number is {randguess}?")
        ans = boolinput()
        if ans:
            exit(0)
        else:
            randguesscache.append(randguess)




check = False
while not check:
    check = modeslct()
while True:
    loop()



