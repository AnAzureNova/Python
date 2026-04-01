
def int_input(message):
    while True:
        print(f"{message}")
        userinput = input(f"> ")
        if userinput == "end" or userinput == "exit" or userinput == "0" or userinput == "null":
            return False
        try:
            return int(userinput)
        except ValueError:
            print("Invalid input")

def get_range(list):
    list_max = list[0]
    list_min = list[0]
    for list_number in list:
        if list_number > list_max:
            list_max = list_number
        if list_number < list_min:
            list_min = list_number
    #print(f">> DEBUG list_max({list_max}) list_min({list_min})")
    return list_max - list_min

def remove_dividable(list, divideBy):
    newlist = []
    for list_number in list:
        if not list_number % divideBy == 0:
            newlist.append(list_number)
    return newlist

index = 0
resList = []

while True:
    number = int_input(f"{index+1}. number: ")
    if not number:
        break
    resList.append(number)
    index += 1

print(f"---\nLIST RANGE: {get_range(resList)}")
for number in resList:
    print(number, end=" ")

dividableBy = int_input("\nEnter a number to divide by: ")
print(f"---\nLIST WITHOUT NUMBERS DIVIDABLE BY {dividableBy}: {remove_dividable(resList, dividableBy)}")

exit(0)