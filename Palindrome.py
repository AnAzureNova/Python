def userInput(message):
    return input(message)

def reverse(input):
    reversedmsg = ""
    for char in reversed(input):
        reversedmsg += char
    return reversedmsg

usrinput = userInput("Enter a message: ").lower()
reversedusrinput = reverse(usrinput)
#reverse = usrinput.lower() [::-1]

print(f"{usrinput} to {reversedusrinput}")

if reversedusrinput == usrinput:
    print("Is a palindrome")
else:
    print("Is not a palindrome")