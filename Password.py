def userInput(message):
    return input(message)

isExit = False
strikeCount=0
password = userInput("Enter password: ")
while not isExit:
    if strikeCount > 2:
        print("Too many attempts")
        isExit = True
    else:
        if password == userInput("Re-Enter your password: "):
            isExit = True
            if len(password) < 8:
                print("Password is unusable: Less than 8 characters")
            else:
                print("Password is valid")
        else:
            print("Passwords don't match")
            strikeCount += 1