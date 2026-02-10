def intinput(message):
    while True:
        try:
            return int(input(f"Enter {message}: "))
        except ValueError:
            print("Invalid input")
def boolinput():
    while True:
        inputmsg = input().lower()
        if inputmsg == "yes":
            return True
        elif inputmsg == "no":
            return False

def mainloop():
    price = 0
    height = intinput("height")
    if height < 87:
        print ("!! Access denied: Height requirement not met")
        mainloop()
    age = intinput("age")
    if age < 12:
        price = 50
    elif age < 18:
        price = 100
    elif age < 65:
        price = 150
    else:
        print("!! Access denied: You're too old")
        mainloop()
    print("Would you like a photo (+ 40 Czk)")
    if boolinput():
        price += 40
    print(f"PRICE: {price} Czk")
    print("Enjoy your time horse riding!")
    exit(0)
mainloop()