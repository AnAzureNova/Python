import random
dealerHand = []
playerHand = []

def actionBool(message):
    while True:
        action = input(message)
        match action.lower():
            case "hit" | "hi" | "h":
                return True
            case "stand" | "stan" | "sta" | "st" | "s":
                return False
        print("ERROR: Try again")


def pullCard(who, count):
    for index in range(count):
        rng = random.randint(0, 13)

        match rng:
            case 0:
                rng = "A"
            case 11:
                rng = "J"
            case 12:
                rng = "D"
            case 13:
                rng = "K"

        if who == "player":
            playerHand.append(rng)
        else:
            dealerHand.append(rng)

def total(hand):
    total = 0
    if hand == "player":
        for card in playerHand:
            match card:
                case "A":
                    if total > 10:
                        card = 1
                case "J":
                    card = 11
                case "D":
                    card = 11
                case "K":
                    card = 11
            total += card
        return total
    else:
        for card in dealerHand:
            match card:
                case "A":
                    if total > 10:
                        card = 1
                case "J":
                    card = 11
                case "D":
                    card = 11
                case "K":
                    card = 11
            total += card
        return total

def wincheck(count):
    if count == 21:
        return True
    elif count > 21:
        return False
    return "next"

def result(result):
    match result:
        case "win":
            print("You won!")
            exit(0)
        case "loss":
            print("You bust!")
            exit(0)
        case "match":
            print("Match!")
            exit(0)
def printhands():
    print(f"PLAYER: {playerHand} ({total("player")})")
    print(f"DEALER: {dealerHand} ({total("dealer")})")

def dealerPull(match):
    dealerAIlimit = 0
    rng = random.randint(0, 3)
    match rng:
        case 0:
            dealerAIlimit = 15
        case 1:
            dealerAIlimit = 16
        case 2:
            dealerAIlimit = 17
        case 3:
            dealerAIlimit = match
    while total("dealer") < dealerAIlimit:
        pullCard("dealer", 1)
        printhands()

    printhands()
    if wincheck(total("dealer")) == match: result("match")
    else: result("win")


while True:
    if total("player") == 0:
        pullCard("player", 2)
    if total("dealer") == 0:
        pullCard("dealer", 2)
    printhands()
    if not wincheck(total("player")) == "next":
        if wincheck(total("player")): result("win")

    if actionBool("HIT OR STAND?"):
        pullCard("player", 1)
        printhands()
        if not wincheck(total("player")) == "next":
            if wincheck(total("player")):
                result("win")
            elif not wincheck(total("player")):
                result("loss")
    else:
        dealerPull(wincheck(total("player")))


