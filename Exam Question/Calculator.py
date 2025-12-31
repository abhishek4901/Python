while True:
    # Input numbers
    n1 = float(input("Enter the first number: "))
    n2 = float(input("Enter the second number: "))

    # Show menu
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    # Input choice
    choice = int(input("Enter your choice (1-4): "))

    # match-case (Python 3.10+)
    match choice:
        case 1:
            print(n1, "+", n2, "=", n1 + n2)
        case 2:
            print(n1, "-", n2, "=", n1 - n2)
        case 3:
            print(n1, "*", n2, "=", n1 * n2)
        case 4:
            if n2 != 0:
                print(n1, "/", n2, "=", n1 / n2)
            else:
                print("Error: Division by zero!")
        case _:
            print("Invalid input")

    again = input("Do you want to continue (yes or no): ").lower()
    if again != "yes":
        print("Thank you for using the calculator")
        break
