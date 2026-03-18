import math
import operator

operation ={
    "+":operator.add,
    "-":operator.sub,
    "*":operator.mul,
    "/":operator.truediv,
    "exp":operator.pow,
    "sqrt":math.sqrt,
}

def fltinput(message):
    while True:
        try:
            return float(input(f"Enter {message}: "))
        except ValueError:
            print("Invalid input")

def limcharinput(message):
    while True:
        c = input(f"Enter {message}: ")
        if operation[c]:
            return c

def calculate(x,c,y):
    if operation[c]:
        match c:
            case "sqrt":
                return operation[c](x)
            case _:
                return operation[c](x, y)
    return False

print(f"AVAILABLE OPERANTS: {operation.keys()} \n----------------------------------")
val1 = fltinput("the first number")
while True:
    op = limcharinput("an operant")
    if op:
        break
    else:
        print("ERROR")

if op != "sqrt":
    val2 = fltinput("the second number")
else:
    val2 = math.nan

print("----------------------------------")
res = calculate(val1, op, val2)
if op != "sqrt":
    print(f"{val1} {op} {val2} = {res}")
else:
    print(f"{val1} {op} = {res}")
