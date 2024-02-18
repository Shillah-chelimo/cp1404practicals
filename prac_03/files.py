user_name = input("Enter your name: ")
with open("name.txt", "w") as file:
    file.write(user_name)

with open("name.txt", "r") as file:
    name = file.read()
print(f"Your name is {name}")

with open("numbers.txt", "r") as file:
    number1 = int(file.readline())
    number2 = int(file.readline())
total = number1 + number2
print("Total of first two numbers:", total)

total = 0
with open("numbers.txt", "r") as file:
    for line in file:
        total += int(line)
print("Total of all numbers in numbers.txt:", total)
