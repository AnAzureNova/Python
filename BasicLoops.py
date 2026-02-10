sum = 0
word = "PYTHON"
for number in range(0,11,1):
    if number == 10:
        print(number)
    else:
        print(number, end=", ")
    sum += number
print(f"\nSUM : {sum}")
for letter in word:
    print(letter, end=" ")
exit(0)