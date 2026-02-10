def userInput(message):
    while True:
        try:
            return int(input(f"Enter the {message}: "))
        except ValueError:
            print("Invalid input")

bookValue = userInput("value of the book")
salePercentage = userInput("percentage of the sale")

print(f"\nBook value: {bookValue-((bookValue/100)*salePercentage)}$ ({salePercentage}% sale)")
print(f"Originally worth: {bookValue}$")

