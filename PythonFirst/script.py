var = 55
print("Variable", var)
if var>10:
    print("TRUTH NUKE")
elif var<10:
    print("so untrue")
else:
    print("10 detected")

tempDict = {
    "String": "YUP",
    "Number": 123,
    "Bool": True,
    "Dict":{
        "Key1": 1,
        "Key2": 2,
    },
    "List": ["Yes", "Maybe", "No"]
}
print(f"Dictionary contents:\n- {tempDict['String']}\n- {tempDict['Number']}\n- {tempDict['Bool']}\n- {tempDict['Dict']['Key2']}\n- {tempDict['List'][1]}")