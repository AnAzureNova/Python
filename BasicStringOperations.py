def userInput(message):
    return input(message)
checks = {
    "isUpper": False,
    "isNum": False,
    "isChar": False,
}
def check(password):
    if len(password) < 8:
        return False
    for letter in word:
        if letter.isupper():
            checks["isUpper"] = True
        elif letter.isdigit():
            checks["isNum"] = True
        elif not letter.isalnum():
            checks["isChar"] = True
    vidx = 0
    for check in checks:
        if checks[check]:
            vidx += 1
    return vidx

word = userInput("Enter password: ")
validity = check(word)
print(validity)
match validity:
    case False:
        print("Password is unusable")
    case 0:
        print("Password is really weak")
    case 1:
        print("Password is weak")
    case 2:
        print("Password is strong")
    case 3:
        print("Password is really strong")

exit(0)