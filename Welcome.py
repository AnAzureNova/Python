def userInput(message):
    return input(f"Enter your {message.lower()}: ")

name = userInput("Name").capitalize()
surname = userInput("Surname").capitalize()
print(f"Hello, {name} {surname}!")
