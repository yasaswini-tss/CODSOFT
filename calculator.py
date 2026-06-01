import math

while True:
    print("\n" + "=" * 40)
    print("      ADVANCED CALCULATOR")
    print("=" * 40)

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Square Root")
    print("7. Percentage")
    print("8. Exit")

    choice = input("Choose an operation (1-8): ")

    if choice == "8":
        print("Thank you for using Calculator!")
        break

    elif choice == "6":
        num = float(input("Enter a number: "))

        if num < 0:
            print("Cannot find square root of a negative number.")
        else:
            print("Result =", math.sqrt(num))

    elif choice == "7":
        total = float(input("Enter total marks: "))
        obtained = float(input("Enter obtained marks: "))

        if total == 0:
            print("Total marks cannot be zero.")
        else:
            percentage = (obtained / total) * 100
            print(f"Percentage = {percentage:.2f}%")

    elif choice in ["1", "2", "3", "4", "5"]:

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            print("Result =", num1 + num2)

        elif choice == "2":
            print("Result =", num1 - num2)

        elif choice == "3":
            print("Result =", num1 * num2)

        elif choice == "4":
            if num2 == 0:
                print("Cannot divide by zero")
            else:
                print("Result =", num1 / num2)

        elif choice == "5":
            print("Result =", num1 ** num2)

    else:
        print("Invalid Choice! Please try again.")