import math

def intinput(message):
    while True:
        try:
            return int(input(f"Enter {message}: "))
        except ValueError:
            print("Invalid input")

cash = [2000,1000,500,200,100,50,20,10,5,2,1]
cashback = {
    "2000" : 0,
    "1000" : 0,
    "500" : 0,
    "200" : 0,
    "100" : 0,
    "50" : 0,
    "20" : 0,
    "10" : 0,
    "5" : 0,
    "2" : 0,
    "1" : 0
}
price = intinput("amount of money to exchange (czk)")

for value in cash:
    #print (price)
    #print (value)
    if price % value != 0:
        amount = math.floor(price / value)
        #print(amount)
        cashback[f"{value}"] += amount
        price = price - (value * amount)
    elif price == value:
        amount = 1
        #print(amount)
        cashback[f"{value}"] += amount
        price = price - (value * amount)

print(cashback)

exit(0)