import math
import operator

operation ={
    "+":operator.add,
    "-":operator.sub,
    "*":operator.mul,
    "/":operator.truediv,
    "exp":operator.pow,
    "sqrt":math.sqrt,
    "sin":math.sin,
    "cos":math.cos,
    "tan":math.tan,
}

isOneVal = False
def stringinput():
    print(">", end="")
    return input()
def error(message, code):
    print(f"{message} ({code})")

def calculate(x,c,y):
    global isOneVal
    if operation[c]:
        match c:
            case "sqrt" | "sin" | "cos" | "tan":
                isOneVal = True
                return operation[c](x)
            case _:
                return operation[c](x, y)
    return False

print("AVAILABLE OPERANTS: ", end="")
for ex in operation:
    print(ex, end=" ")
print("\n----------------------------------")
while True:
    fullstring = stringinput()
    splitstring = fullstring.split()

    if len(splitstring) > 3:
        error("SYNTAX ERROR", 0)
        break

    match splitstring[0]:
        case "exit":
            exit(0)
        case "sqrt" | "sin" | "cos" | "tan":
            isOneVal = True
            op = splitstring[0]
        case _:
            val1 = int(splitstring[0])

    match splitstring[1]:
        case "+" | "-" | "*" | "/" | "exp":
            op = splitstring[1]
        case _:
            val1 = int(splitstring[1])

    if isOneVal:
        res = calculate(val1, op, math.nan)
    else:
        val2 = int(splitstring[2])
        res = calculate(val1, op, val2)
    print(res)