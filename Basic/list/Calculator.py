num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("Enter the choice:")
print("1 for Addition")
print("2 for Subtraction")
print("3 for Multiplication")
print("4 for Integer Division")
print("5 for Float Division")
print("6 for Remainder")
print("7 for Power")
print("8 for Exit")

while True:
    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            print("Addition:", num1 + num2)
        case 2:
            print("Subtraction:", num1 - num2)
        case 3:
            print("Multiplication:", num1 * num2)
        case 4:
            print("Integer Division:", num1 // num2)
        case 5:
            print("Float Division:", num1 / num2)
        case 6:
            print("Remainder:", num1 % num2)
        case 7:
            print("Power:", num1 ** num2)
        case 8:
            print("Exit")
            break
        case _:
            print("Invalid choice")