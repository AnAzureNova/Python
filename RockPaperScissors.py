import random
score = 0

def userInput():
    while True:
        print(">", end=" ")
        usrinput = input()
        if usrinput == "quit":
            exit(0)
        elif usrinput == "rock" or usrinput == "paper" or usrinput == "scissors":
            return usrinput
        else:
            print("> Invalid input")
def play(playerGuess, botGuess):
    global score

    print(f"# Computer: {botGuess}")
    print(f"# YOU: {playerGuess}")

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


print(f"ROCK PAPER SCISSORS - [quit] to stop playing\n-----------------------------------")
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
    result = play(playerGuess, botGuess)
    print(result)


