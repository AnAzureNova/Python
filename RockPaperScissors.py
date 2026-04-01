import random
score = 0
wins = 0
loses = 0
playedHands = {
    "Rock": 0,
    "Paper": 0,
    "Scissors": 0
}
isShot = False

def userInput():
    global score
    global isShot
    while True:
        print(">", end=" ")
        usrinput = input()
        if usrinput == "quit" or usrinput == "exit" or usrinput == "end" or usrinput == "q" or usrinput == "stop":
            if not isShot:
                print("----------GAME END----------")
                print(f"FINAL SCORE: {score}\nRounds Won: {wins}\nRounds Lost: {loses}\n\nDetailed stats:\n{playedHands}")
                print("----------------------------")
            else:
                print("----------GAME END----------")
                print(f"FINAL SCORE: {score}")
                print("You have been arrested for murder")
                print("----------------------------")
            exit(0)
        elif usrinput == "gun" and not isShot:
            print("> You shot the opponent")
            score = "Life in prison"
            print(f"YOUR SCORE: {score}")
            isShot = True
        elif usrinput == "rock" or usrinput == "paper" or usrinput == "scissors":
            return usrinput
        else:
            print("> Invalid input")
def play(playerGuess, botGuess):
    global score
    global wins
    global loses
    global playedHands

    print(f"# YOU: {playerGuess} vs Computer: {botGuess}")

    match playerGuess:
        case "rock":
            playedHands["Rock"] += 1
            match botGuess:
                case "rock":
                    return "!! DRAW !!"
                case "paper":
                    loses += 1
                    score -= 1
                    return "!! YOU LOST !!"
                case "scissors":
                    wins += 1
                    score += 1
                    return "!! YOU WIN !!"
        case "paper":
            playedHands["Paper"] += 1
            match botGuess:
                case "rock":
                    wins += 1
                    score += 1
                    return "!! YOU WIN !!"
                case "paper":
                    return "!! DRAW !!"
                case "scissors":
                    loses += 1
                    score -= 1
                    return "!! YOU LOST !!"
        case "scissors":
            playedHands["Scissors"] += 1
            match botGuess:
                case "rock":
                    loses += 1
                    score -= 1
                    return "!! YOU LOST !!"
                case "paper":
                    wins += 1
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