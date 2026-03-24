import random
score = 0
isShot = False

def userInput():
    global score
    global isShot
    while True:
        print(">", end=" ")
        usrinput = input()
        if usrinput == "quit" or usrinput == "exit" or usrinput == "end" or usrinput == "q" or usrinput == "stop":
            exit(0)
        elif usrinput == "gun" and not isShot:
            print("> You shot the opponent")
            score = 99
            print(f"YOUR SCORE: {score}")
            isShot = True
        elif usrinput == "rock" or usrinput == "paper" or usrinput == "scissors":
            return usrinput
        else:
            print("> Invalid input")
def play(playerGuess, botGuess):
    global score
    print(f"# YOU: {playerGuess} vs Computer: {botGuess}")

    match playerGuess:
        case "rock":
            match botGuess:
                case "rock":
                    return "!! DRAW !!"
                case "paper":
                    score -= 1
                    return "!! YOU LOST !!"
                case "scissors":
                    score += 1
                    return "!! YOU WIN !!"
        case "paper":
            match botGuess:
                case "rock":
                    score += 1
                    return "!! YOU WIN !!"
                case "paper":
                    return "!! DRAW !!"
                case "scissors":
                    score -= 1
                    return "!! YOU LOST !!"
        case "scissors":
            match botGuess:
                case "rock":
                    score -= 1
                    return "!! YOU LOST !!"
                case "paper":
                    score += 1
                    return "!! YOU WIN !!"
                case "scissors":
                    return "!! DRAW !!"


print(f"ROCK PAPER SCISSORS\n-----------------------------------")
while True:
    print(f"YOUR SCORE: {score}")
    currRoll = random.randint(0, 2)
    playerGuess = userInput().lower()
    match currRoll:
        case 0:
            botGuess = "rock"
        case 1:
            botGuess = "paper"
        case 2:
            botGuess = "scissors"
        case _:
            break
    if not isShot:
        result = play(playerGuess, botGuess)
        print(result)



